import os
import re
from imp import reload
import  chardet
from lxml import etree
import requests
import sys
from bs4 import BeautifulSoup
import bs4

url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"
class simpleSpider:

    def __init__(self):
        self.studNumber = ""
        self.passwd = ""
        self.checkCode = ""
        self.sess = requests.session()
    
    def setStudent(self,studNumber,passwd):
        self.studNumber = input("学号：")
        self.passwd = input("密码:")
    
    def setCheckCode(self):
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
        self.checkCode = input("验证码是: ")       

    def login(self):
        try:
            response = self.sess.get(url)
        except requests.exceptions.Timeout:
            print("请求超时")

        selector = etree.HTML(response.content)
        __VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]

        datas = {
            "__VIEWSTATE":__VIEWSTATE,
            "txtUserName":self.studNumber,
            "TextBox2":self.passwd,
            "txtSecretCode":self.checkCode,
            "Button1":"",       
        }                
        try:

            response = self.sess.post(url,data=datas) 
            #html = response.content.decode('gb2312')
        except requests.exceptions.Timeout:
            print("登录超时")
        
    def getStudentLessonPage(self):
        kburl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xskbcx.aspx?xh="+self.studNumber+"&xm=%C0%EE%C8%BD%C8%BD&gnmkdm=N121603"
        headers = {
            "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }        
        try:
            reponse = self.sess.get(kburl,headers=headers)
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


class FuckPage:

    def __init__(self):
        self.week=[]
        self.firstLesson=[]
        self.secondLesson=[]
        self.thirdLesson=[]
        self.fourthLesson=[]
        self.fifthLesson=[]
        self.sixthLesson=[]
        self.sevenLesson=[]
        self.eightLesson=[]
        self.ninthLesson=[]
        self.tenthLesson=[]
        self.eleventhLesson=[]
        self.finial_lecture=[]

        self.lecture=[
            self.week,self.firstLesson,self.secondLesson,
            self.thirdLesson,self.fourthLesson,self.fifthLesson,
            self.sixthLesson,self.sevenLesson,self.eightLesson,
            self.sevenLesson,self.eightLesson,self.ninthLesson,
            self.tenthLesson,self.eleventhLesson
        ]


    def getLesson(self,tag):
        #print(tag)
        j = 0
        for tr in tag.children:
            #print("--------------------------------",j)
            j+=1

            if type(tr) is bs4.element.Tag:
                i = 0

                for td in tr.findAll('td'):
                    result = td.getText()
                    if len(result) == 1:
                        continue
                    
                    #print("===================",i,type(result),len(result))
                    #print("***",td.getText())
                    if j == 1:
                        self.week.append(result)
                    elif j == 3:
                        self.firstLesson.append(result)
                    elif j == 4:
                        self.secondLesson.append(result)
                    elif j == 5:
                        self.thirdLesson.append(result)
                    elif j == 6:
                        self.fourthLesson.append(result)
                    elif j == 7:
                        self.fifthLesson.append(result)
                    elif j == 8:
                        self.sixthLesson.append(result)
                    elif j == 9:
                        self.sevenLesson.append(result)
                    elif j == 10:
                        self.eightLesson.append(result)
                    elif j == 11:
                        self.ninthLesson.append(result)
                    elif j == 12:
                        self.tenthLesson.append(result)
                    elif j == 13:
                        self.eleventhLesson.append(result)   
                    i+=1    

    def getFinialLecture(self):
        for i in self.lecture:
            if isinstance(i,list):
                for j in i:
                    #print(j,len(j))
                    if len(j) <= 4:
                        continue
                    self.finial_lecture.append(j)        