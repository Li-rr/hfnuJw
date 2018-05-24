import fuckSpider as fS
import course as cS
import sql as cSQL
if __name__ == '__main__':
    # s_spider = fS.simpleSpider()

    # s_spider.setStudent(studNumber="",passwd="")
    # s_spider.setCheckCode()
    # s_spider.login()
    # lesson_tag = s_spider.getStudentLessonPage()
    
    # s_page = fS.FuckPage()

    # s_page.getLesson(lesson_tag)
    # s_page.getFinialLecture()

    course = cS.Course()

    # for i in s_page.finial_lecture:
    #     print("\n=======================================")
    #     course.getLesson(i)
    
    # # k = 0
    # # a = input("是否删除数据库：")

    # # if int(a) == 1:
    # #     cSQL.deleteData()
    # # for i in course.lecture:
    # #     print(i)
    # for i in course.lecture:
    #     print("\n------------------------------------- k ->")        
    #     print(i)
    #     course.findLessonName(i)
    #     course.findLessonTeacher(i)
    #     course.findLessonLocation(i)
    #     course.findLessonDayTime(i)
    #     course.findLessonWeekday(i)
    #     course.findLessonWeekNumber(i)
    #     course.print()
    # # #     data=(int(k),course.cName,course.cTeacher,course.cLoc,int(course.cTimeStart),
    # # #                     int(course.cTimeEnd),course.weekDay,s_spider.studNumber)
    #     data=(course.cName,course.cTeacher,course.cLoc,int(course.cTimeStart),
    #                     int(course.cTimeEnd),course.weekDay,s_spider.studNumber+str(k),s_spider.studNumber)
    # #     flag = cSQL.queryDataById(s_spider.studNumber+str(k))
    # #     if flag == 0:
    # #         cSQL.insertData(data)
    # #     k += 1

    
    # print("=====================================")
    # cSQL.queryDataById(123)
    # print("=====================================")
     #cSQL.queryData()
    # data =  cSQL.queryDataByStudentId("1510431010")
    # print("======================================")
    # for i in data:
    #     for j in i:
    #         print(j,end=" ")
    #     print("")
    str="计算机网络实验周五第3,4节{第5-12周}程昆山躬行楼302计算机网络周五第3,4节{第1-4周}程昆山博约楼216*"
    course.getLesson(str)
    for i in course.lecture:
        print(i)