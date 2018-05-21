from django.shortcuts import render
from django.http import HttpResponse
import types
# Create your views here.
from hfnuJw.spider import Sqider
from hfnuJw.spider2 import SimpleSpider


url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"

# global fuck_session
fuck_spider = SimpleSpider()

fuckTest = 2

def index(request):

    print("this is index",fuckTest + 1)
    fuck_spider.getImage()
    return render(request, 'login2.html')
    # return render(request,'login.html',{'image':image})


def login(request):

    print("this is login",fuckTest)
    lecture = []
    
    user = request.POST['user']
    passwd = request.POST['passwd']
    checkCode = request.POST['checkCode']

    fuck_spider.setStudent1(str(user),str(passwd),str(checkCode))
    fuck_spider.login(url)
    lesson_tag = fuck_spider.getLessonPage(session="")
    lecture_all = fuck_spider.getLesson(lesson_tag)
    lecture = fuck_spider.getFinialLecture(lecture_all)

    # spider = SimpleSpider()
    # # spider.setStudent(str(user),str(passwd))
    # spider.setStudent1(str(user),str(passwd),str(checkCode))
    # #result_session = spider.login(url) 
    # spider.login(url)
    # lesson_tag = spider.getLessonPage(session="")
    # #lesson_tag = spider.getLessonPage(result_session)
    # #print(lesson_tag)
    # lecture_all = spider.getLesson(lesson_tag)
    # count = len(lecture)
    # if count != 0:
    #     print("count->",count)
    #     del lecture[:]
    # lecture = spider.getFinialLecture(lecture_all)
    context = {
        'user':user,
        'passwd':passwd,
        'code':checkCode,
        'lecture':lecture
    }
    # print("this is fuck view")
    # for i in lecture:
    #     print(i)
    return render(request,'result.html',context)