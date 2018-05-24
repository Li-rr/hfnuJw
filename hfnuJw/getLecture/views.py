# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from . import fuckSpider as fS
from . import course as cS
from . import sql as cSQL

# Create your views here.
url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"

fuck_spider = fS.simpleSpider()

def index(request):
    fuck_spider.getImage()
    return render(request,'login2.html')

def login(request):
    lecture = []

    user = request.POST['user']
    passwd = request.POST['passwd']
    checkCode = request.POST['checkCode']

    flag = cSQL.queryDataById(user+'0')

    user = str(user)
    passwd = str(passwd)
    checkCode = str(checkCode)
    if int(flag) == 0:
        fuck_spider.setStudent(user,passwd,checkCode)
        fuck_spider.login()

        lesson_tag = fuck_spider.getStudentLessonPage()

        s_page = fS.FuckPage()
        s_page.getLesson(lesson_tag)
        s_page.getFinialLecture()

        course = cS.Course()
        for i in s_page.finial_lecture:
            course.getLesson(i)
        k = 0
        for i in course.lecture:
            course.findLessonName(i)
            course.findLessonTeacher(i)
            course.findLessonLocation(i)
            course.findLessonDayTime(i)
            course.findLessonWeekday(i)
            course.findLessonWeekNumber(i)

            data=(course.cName,course.cTeacher,course.cLoc,int(course.cTimeStart),
                    int(course.cTimeEnd),course.weekDay,course.cWeekStart,course.cWeekEnd,
                    user+str(k),user)
            flag = cSQL.queryDataById(fuck_spider.studNumber+str(k))

            cSQL.insertData(data)
            k += 1

    data = cSQL.queryDataByStudentId(user)

    context = {
                'lecture' : data
                }
    return render(request,'result3.html',context)

def page_not_found(request):
    return render(request,'404.html')

def page_error(request):
    return render(request,'500.html')

def permission_denied(request):
    return render(request,'403.html')
