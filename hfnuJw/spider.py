# -*-coding:utf-8-*-
import os
import re
from imp import reload
from this import s

from lxml import etree
import requests
import sys
from bs4 import BeautifulSoup

class Sqider:
    studentNumber = "1510431010"
    studentPasswd = "lrr1996429"
    checkCode = ""
    def setStudent(self,number,passwd,code):
        self.studentNumber = number
        self.studentPasswd = passwd
        self.checkCode = code

    def login(self,url):
        s = requests.session()
        #
        response = s.get(url)
        selector = etree.HTML(response.content)
        __VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]

        #构建post数据
        datas = {
            "__VIEWSTATE": __VIEWSTATE,
            "txtUserName": self.studentNumber,
            "TextBox2": self.studentPasswd,
            "txtSecretCode": self.checkCode,
            "Button1": "",
        }

        # 提交表头，里面的参数是电脑各浏览器的信息。模拟成是浏览器去访问网页。
        headers = {
            "User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

        # 登陆教务系统
        response = s.post(url, data=datas)

        # 获取课表，kburl是课表页面url,为什么有个Referer参数,这个参数代表你是从哪里来的。就是登录后的主界面参数。这个一定要有。
        kburl = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/xskbcx.aspx?xh=1510431010&xm=%C0%EE%C8%BD%C8%BD&gnmkdm=N121603"
        headers = {"Referer": "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        response = s.get(kburl, headers=headers)
        # html代表访问课表页面返回的结果就是课表。下面做的就是解析这个html页面# 。
        html = response.content.decode("gb2312")
        selector = etree.HTML(html)
        #print(html)

        content = selector.xpath('//*[@id="Table1"]/tr/td/text()')
        return content
