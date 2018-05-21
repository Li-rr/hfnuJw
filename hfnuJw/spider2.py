# -*-coding:utf-8-*-
import os
import re
import sys
from lxml import etree
import requests
import sys
from bs4 import BeautifulSoup
import bs4
sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__))))
import lessonData

class SimpleSpider:
    studentNumber = ""
    passwd = ""
    checkCode = ""

    def setStudent1(self,studentNumber,passwd,checkCode):
        self.studentNumber = studentNumber
        self.passwd = passwd
        self.checkCode = checkCode
        self.sess = requests.session()
        
   
    def __init__(self):
        self.studentNumber = ""
        self.passwd=""
        self.checkCode=""
        self.sess = requests.session()

    def setStudent(self,studentNumber,passwd):
        self.studentNumber = studentNumber
        self.passwd = passwd

        self.sess = requests.session()
	
    def getImage(self):
        print("this is getImage")
        imgUrl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/CheckCode.aspx"
        try:
            imgresponse = self.sess.get(imgUrl,stream=True)
        except requests.exceptions.Timeout:
            print("请求验证码超时")

        image = imgresponse.content
        workDir = 'E:\code\hfnuJw\getScore\static\images\\'
        print ("保存验证码到："+ workDir +"code.png"+ "\n")

        try:
            if os.path.exists(workDir+"code.png") == True:
                os.remove(workDir+"code.png")  
            with open(workDir+"code.png","wb") as jpg:
                jpg.write(image)     
        except IOError:
            print("IO Error\n")
        finally:
            jpg.close()	

    def login(self,url):
        
        
        # s = requests.session()

        try:
            #response = s.get(url)
            response = self.sess.get(url)

        except requests.exceptions.Timeout:
            print("请求超时")

        selector = etree.HTML(response.content)
        __VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
        
        
        # imgUrl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/CheckCode.aspx"

        # try:
        #     #imgresponse = s.get(imgUrl,stream=True)
        #     imgresponse = self.sess.get(imgUrl,stream=True)
        # except requests.exceptions.Timeout:
        #     print("请求验证码超时")

        # image = imgresponse.content
        # workDir = os.getcwd()+'\\'
        # workDir = 'E:\code\hfnuJw\getScore\static\images\\'
        # print ("保存验证码到："+ workDir +"code.png"+ "\n")
        
        # try:
        #     if os.path.exists(workDir+"code.png") == True:
        #         os.remove(workDir+"code.png")  
        #     with open(workDir+"code.png","wb") as jpg:
        #         jpg.write(image)     
        # except IOError:
        #     print("IO Error\n")
        # finally:
        #     jpg.close()


        # # #输入验证码
        # code = input("验证码是：")
        #构建post数据
        datas = {
            "__VIEWSTATE":__VIEWSTATE,
            "txtUserName":self.studentNumber,
            "TextBox2":self.passwd,
            "txtSecretCode":self.checkCode,
            "Button1":"",       
        }
        try:

            response = self.sess.post(url,data=datas) 
            html = response.content.decode('gb2312')
            # mainUrl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xs_main.aspx?xh=1510431002"
            # headers = {
            #     "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
            #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) C3gqrhrome/59.0.3071.115 Safari/537.36"
            # }   
            # mainPage = self.sess.post(mainUrl,headers=headers)        
            # print(mainPage.text)
            print("登录成功")
            #return s
        except requests.exceptions.Timeout:
            print("登录超时")
    
    def getLessonPage(self,session):
        print("this is getLessonPage")
        temp = str(self.studentNumber)
        print(self.studentNumber,type(self.studentNumber))
        print(self.passwd,type(self.passwd))
        print(self.checkCode,type(self.checkCode))
        kburl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xskbcx.aspx?xh="+self.studentNumber+"&xm=%C0%EE%C8%BD%C8%BD&gnmkdm=N121603"
        headers = {
            "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }

        try:
            #reponse = session.get(kburl,headers=headers)
            reponse = self.sess.get(kburl,headers=headers)
            #requests.session().delete()
            print("访问成功")
        except requests.exceptions.Timeout:
            print("访问超时")
        
        #解析html
        html = reponse.content.decode('gb2312')
        print("----------------------------")
        #print(html)
        selector = etree.HTML(html)
        soup = BeautifulSoup(html,'lxml')

        lesson = soup.find(id="Table1")
        #print(soup)
        #print("lesson-->",lesson)
        return lesson
    
    def getLesson(self,tag):
        j = 0
        #删除上一次产生的数据
        del lessonData.week[:]
        del lessonData.firstLesson[:]
        del lessonData.secondLesson[:]
        del lessonData.thirdLesson[:]
        del lessonData.fourthLesson[:]
        del lessonData.fifthLesson[:]
        del lessonData.sixthLesson[:]
        del lessonData.sevenLesson[:]
        del lessonData.eightLesson[:]
        del lessonData.ninthLesson[:]
        del lessonData.tenthLesson[:]
        del lessonData.eleventhLesson[:]
        for tr in tag.children:
            j += 1

            if type(tr) is bs4.element.Tag:
                i = 0
                for td in tr.findAll('td'):
                    result = td.getText()
                    if len(result) == 1:
                        continue

                    if j == 1:
                        lessonData.week.append(result)
                    elif j == 3:
                        lessonData.firstLesson.append(result)
                    elif j == 4:
                        lessonData.secondLesson.append(result)
                    elif j == 5:
                        lessonData.thirdLesson.append(result)
                    elif j == 6:
                        lessonData.fourthLesson.append(result)
                    elif j == 7:
                        lessonData.fifthLesson.append(result)
                    elif j == 8:
                        lessonData.sixthLesson.append(result)
                    elif j == 9:
                        lessonData.sevenLesson.append(result)
                    elif j == 10:
                        lessonData.eightLesson.append(result)
                    elif j == 11:
                        lessonData.ninthLesson.append(result)
                    elif j == 12:
                        lessonData.tenthLesson.append(result)
                    elif j == 13:
                        lessonData.eleventhLesson.append(result) 
                    i+=1
        return lessonData.lecture
    


    def getFinialLecture(self,lecture_atgu):
        lessonData.finial_lecture=[]
        for i in lecture_atgu:
            if isinstance(i,list):
                for j in i:
                    if len(j) <= 4:
                        continue
                    #print(j)
                    lessonData.finial_lecture.append(j)
        return lessonData.finial_lecture