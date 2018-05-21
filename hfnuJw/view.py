from django.http import HttpResponse

from hfnuJw.spider import Sqider


def hello(request):
    #url = "http://jwxt.hfnu.edu.cn/(1aloxqa0g1ns0f45t3dht232)/default2.aspx"
    #spider = Sqider()
    #image = spider.login(url)
    #return HttpResponse(image,content_type="image/jpg")
    return HttpResponse("helloWorld!")