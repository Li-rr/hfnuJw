# -*-coding:utf-8-*-
import os
import re
from imp import reload
import  chardet
from lxml import etree
import requests
import sys
from bs4 import BeautifulSoup
import bs4
import getinfo as info
import sql as myDb
import course as cour
#构建课程表数�?
week=[]
firstLesson=[]
secondLesson=[]
thirdLesson=[]
fourthLesson=[]
fifthLesson=[]
sixthLesson=[]
sevenLesson=[]
eightLesson=[]
ninthLesson=[]
tenthLesson=[]
eleventhLesson=[]
lecture=[week,firstLesson,secondLesson,thirdLesson,fourthLesson,
            fifthLesson,sixthLesson,sevenLesson,eightLesson,
            ninthLesson,tenthLesson,eleventhLesson
            ]
finial_lecture=[]
url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"
def login(url):
    studentNumber = "1510431010"
    passwd = "lrr1996429"
    
    s = requests.session()      
    '''
    构建会话对象，可以跨请求保持某些参数
    它也会在同一个session实例发出的所有�?�求之间
    保持cookie
    '''
    try:
        response = s.get(url)
    except requests.exceptions.Timeout:
        print("请求超时")


    #content为响应体
    selector = etree.HTML(response.content)
    __VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
    imgUrl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/CheckCode.aspx"
    
    
    try:
        imgresponse = s.get(imgUrl,stream=True)
    except requests.exceptions.Timeout:
        print("请求验证码超�?")
    
    
    image = imgresponse.content
    workDir = os.getcwd()+'\\'
    print ("保存验证码到�?"+ workDir +"code.jpg"+ "\n")
    
    try:
        if os.path.exists(workDir+"code.jpg") == True:
            os.remove(workDir+"code.jpg")  
        with open(workDir+"code.jpg","wb") as jpg:
            jpg.write(image)     
    except IOError:
        print("IO Error\n")
    finally:
        jpg.close()


    #输入验证�?
    code = input("验证码是�?")

    #构建post数据
    datas = {
        "__VIEWSTATE":__VIEWSTATE,
        "txtUserName":studentNumber,
        "TextBox2":passwd,
        "txtSecretCode":code,
        "Button1":"",       
    }

    # headers = {
    #     "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    # }    

    try:
        response = s.post(url,data=datas) 
        # mainUrl="http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xs_main.aspx?xh=1510431002"
        headers = {
            "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) C3gqrhrome/59.0.3071.115 Safari/537.36"
        }     
        # mainPage = s.post(mainUrl,headers=headers)
        # print(mainPage.text)
        print("登录成功")
        return s
    except requests.exceptions.Timeout:
        print("登录超时")

def getLessonPage(session):
    studentNumber = "1510431010"
    kburl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xskbcx.aspx?xh="+studentNumber+"&xm=李冉冉&gnmkdm=N121603"
    headers = {
        "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) C3gqrhrome/59.0.3071.115 Safari/537.36"
    }      

    try:
        response = session.get(kburl,headers=headers)
        print("访问成功")
    except requests.exceptions.Timeout:
        print("访问超时")   
    
    #解析html
    html = response.content.decode('gb2312')
    selector = etree.HTML(html)
    soup = BeautifulSoup(html,'lxml')

    #print(html)
    lesson = soup.find(id="Table1")
    print(lesson)
    return lesson
    #print(html)

def getLesson(tag):
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
                    week.append(result)
                elif j == 3:
                    firstLesson.append(result)
                elif j == 4:
                    secondLesson.append(result)
                elif j == 5:
                    thirdLesson.append(result)
                elif j == 6:
                    fourthLesson.append(result)
                elif j == 7:
                    fifthLesson.append(result)
                elif j == 8:
                    sixthLesson.append(result)
                elif j == 9:
                    sevenLesson.append(result)
                elif j == 10:
                    eightLesson.append(result)
                elif j == 11:
                    ninthLesson.append(result)
                elif j == 12:
                    tenthLesson.append(result)
                elif j == 13:
                    eleventhLesson.append(result)   
                i+=1            

def getFinialLectcure(lecture_argu):
    for i in lecture_argu:
        if isinstance(i,list):
            for j in i:
                #print(j,len(j))
                if len(j) <= 4:
                    continue
                finial_lecture.append(j)

if __name__ == '__main__':

    studentNumber = "1510431010"
    url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"
    result = login(url)
    table=getLessonPage(result)
    getLesson(table)
    getFinialLectcure(lecture)
    #finial_lecture =[
    #     "面向对象程序设�?�实验周二�??1,2节{�?9-16周}黄大君躬行楼202面向对象程序设�?�周二�??1,2节{�?1-8周}黄大君躬行楼202",
    #     "论文写作与文�?检索周三�??1,2节{�?1-8周}钟锦�?行楼202",
    #     "面向对象程序设�?�周四�??1,2节{�?1-16周}黄大君躬行楼202",
    #     "概率论与数理统�??A周一�?3,4节{�?1-8周}李美蓉博约楼302*",
    #     "移动设�?�平台开发周二�??3,4节{�?1-8周}李宜兵躬行楼204",
    #     "概率论与数理统�??A周三�?3,4节{�?1-16周}李美蓉博约楼206*",
    #     "移动设�?�平台开发周四�??3,4节{�?1-8周}李宜兵躬行楼204",
    #     "形势与政策周三�??9,10,11节{�?5-8周}胡兵博约�?111*"
    # ]
    k = 0
    course = cour.Course()
    print("=================================")
    for i in finial_lecture:
        course.getLesson(i)
        #print(i)

    
    for j in course.lecture:
        print(j)
    # for i in finial_lecture:
    #     print("--------------------------->")
    #     #print(i)
    #     info.getLesson(i)
    #     k+=1
    #     v = 0
    #     for j in info.lecture:
    #         print(j)
    #         # lessonName = info.findLessonName(j)
    #         # weekDay = info.findLessonWeekday(j)
    #         # dayTime = info.findLessonDayTime(j)
    #         # weekStart,weekEnd = info.findLessonWeekNumber(j)
    #         # teacher = info.findLessonTeacher(j)
    #         # loc = info.findLessonLocation(j)
    #         # print("编号�?",k,"-",v,"课程名称�?",lessonName," 星期几：",weekDay
    #         #     , " 起�?�时间：",weekStart,weekEnd
    #         #     , " 教师�?",teacher
    #         #     ," 教�?�：",loc)
    #         # v+=1
    #     print()
    # print("===================================")
    # k = 0
    # for j in info.lecture:
    #     lessonName = info.findLessonName(j)
    #     weekDay = info.findLessonWeekday(j)
    #     daystart,dayend = info.findLessonDayTime(j)
    #     weekStart,weekEnd = info.findLessonWeekNumber(j)
    #     teacher = info.findLessonTeacher(j)
    #     loc = info.findLessonLocation(j)
    #     print("课程名称:",lessonName," 星期几：",weekDay
    #         , " 起止时间：",weekStart,weekEnd
    #         , "课程时间：",daystart,dayend
    #         , " 教师：",teacher
    #         ," 教室：",loc)
    #     data=(int(k),lessonName,teacher,loc,int(daystart),int(dayend),weekDay,studentNumber)
    #     if myDb.queryDataById(k) == 0:
    #         myDb.insertData(data)
    #         print("插入成功")
    #     else:
    #         print("已存在")
    #     k += 1
    
    # myDb.queryData()
    # myDb.deleteData()
    # print('=====================')
    # myDb.queryData()
    # for i in lecture:
    #     print("-->")
    #     if isinstance(i,list):
    #         for j in i:
    #             if len(j) <= 3:
    #                 continue
    #             print(j,len(i),len(j))