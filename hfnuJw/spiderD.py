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
# import getinfo as info
# import sql as myDb

#构建课程表数据
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

def loginJw(url,studentNumber,passwd,code):
    # studentNumber = "1510431010"
    # passwd = "lrr1996429"
    
    s = requests.session()      
    '''
    构建会话对象，可以跨请求保持某些参数
    它也会在同一个session实例发出的所有请求之间
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
        print("请求验证码超时")
    
    
    image = imgresponse.content
    workDir = os.getcwd()+'\\'
    print ("保存验证码到："+ workDir +"code.jpg"+ "\n")
    
    try:
        if os.path.exists(workDir+"code.jpg") == True:
            os.remove(workDir+"code.jpg")  
        with open(workDir+"code.jpg","wb") as jpg:
            jpg.write(image)     
    except IOError:
        print("IO Error\n")
    finally:
        jpg.close()


    #输入验证码
    code = input("验证码是：")

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
        print("登录成功")
        return s
    except requests.exceptions.Timeout:
        print("登录超时")

def getLessonPage(session):
    studentNumber = "1510431010"
    kburl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xskbcx.aspx?xh="+studentNumber+"&xm=%C0%EE%C8%BD%C8%BD&gnmkdm=N121603"
    headers = {
        "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
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

    print(html)
    lesson = soup.find(id="Table1")
    #print(lesson)
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

