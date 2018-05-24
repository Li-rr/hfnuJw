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

import getinfo



# reload(sys)
# sys.setdefaultencoding('utf-8')
studentNumber = "1510431010"
password = "lrr1996429"
s = requests.session()
url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"
response = s.get(url)
selector = etree.HTML(response.content)

__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]

imgUrl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/CheckCode.aspx"
imgresponse = s.get(imgUrl,stream=True)
print (s.cookies)
image = imgresponse.content
DstDir = os.getcwd()+"\\"
print ("保存验证码到："+DstDir+"code.jpg"+"\n")
try:
    if os.path.exists(DstDir+"code.jpg") == True:
        os.remove(DstDir+"code.jpg")

    with open(DstDir+"code.jpg","wb") as jpg:
        jpg.write(image)
except IOError:
    print ("IO Error\n")
finally:
    jpg.close

#手动输入验证码
code = input("验证码是")
#构建post数据
datas = {
"__VIEWSTATE":__VIEWSTATE,
"txtUserName":studentNumber,
"TextBox2":password,
"txtSecretCode":code,
"Button1":"",
}

#提交表头，里面的参数是电脑各浏览器的信息。模拟成是浏览器去访问网页。
headers = {
    "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
#登陆教务系统
response = s.post(url,data=datas)
print ("成功进入")
#得到登录信息，个人感觉有点多余。
def getInfor(response,xpath):
    content = response.content.decode('gb2312') #网页源码是gb2312要先解码
    selector = etree.HTML(content)
    #print (content)
    infor = selector.xpath(xpath)[0]
    return infor

#获取学生基本信息
# text = getInfor(response,'//*[@id="xhxm"]/text()')
# text = text.replace(" ","")
# print text
#获取课表，kburl是课表页面url,为什么有个Referer参数,这个参数代表你是从哪里来的。就是登录后的主界面参数。这个一定要有。
kburl="http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xskbcx.aspx?xh=1510431010&xm=%C0%EE%C8%BD%C8%BD&gnmkdm=N121603"
headers = {
    "Referer":"http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
response = s.get(kburl,headers=headers)
#html代表访问课表页面返回的结果就是课表。下面做的就是解析这个html页面# 。
html = response.content.decode("gb2312")
selector=etree.HTML(html)
soup = BeautifulSoup(html,'lxml')

lesson = soup.find(id="Table1")

lesson2 = soup.body.form.div.div.span
# print('lesson2',lesson)
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
print('==========================')
j = 0
for tr in lesson.children:
    print("--------------------------------",j)
    j+=1
    #print(str(tr)+'########################################')
    #print(type(tr))
    
    if type(tr) is bs4.element.Tag:
        i = 0
        
        for td in tr.findAll('td'):
            result = td.getText()
            if len(result) == 1:
                continue
            print("===================",i,type(result),len(result))
            print("***",td.getText())
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

        # if j == 3:
        #     break
for i in lecture:
    if isinstance(i,list):
        if(len(i) <= 1):
            continue
        print("-----------------------")
        for j in i:
            
            print(j,len(i))
            # findLessonName(j)
            # findLessonWeekday(j)
            # findLessonWeekTIme(j)
            # findLessonTime(j)
            # findLessonLessonTeacher(j)
            # findLessonLocation(j)

    print()


print(type(lesson))
print(type(lesson2))

