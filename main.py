import fuckSpider as fS
import course as cS

if __name__ == '__main__':
    s_spider = fS.simpleSpider()

    s_spider.setStudent(studNumber="",passwd="")
    s_spider.setCheckCode()
    s_spider.login()
    lesson_tag = s_spider.getStudentLessonPage()
    
    s_page = fS.FuckPage()

    s_page.getLesson(lesson_tag)
    s_page.getFinialLecture()

    course = cS.Course()

    for i in s_page.finial_lecture:
        course.getLesson(i)

    for i in course.lecture:
        print(i)