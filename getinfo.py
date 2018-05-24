import re
build=['博约楼','躬行楼']
lecture=[]
def findLessonName(str):
    index = str.find("周")
    if index != -1:
        lessonName = str[0:index]
        #print ("\n课程："+lessonName)
        return lessonName
    else:
        print ("ErrorLesson")
        return ""

def findLessonWeekday(str):
    index1 = str.find("周")

    if index1 != -1:
        weekday = str[index1:index1+2]
        #print("周几："+weekday)
        return weekday
    else:
        print("ErrorWeekday ")
        return ""

def findLessonDayTime(str):
    index_start = str.find("第")
    index_end = str.find("节")
    index_1 = str.find(",",index_start)
    index_2 = str.rfind(",")

    if index_start != -1:
        #print("时间："+str[index:index+5])
        #print(index_1,index_1)
        if index_1 == index_2:
            start = str[index_start+1]
            end = str[index_start+3]
            return start,end
        else:
            start = str[index_start+1:index_1]
            end = str[index_2+1:index_end]
            #print(start,end)
            return start,end
    else:
        print("ErrorLessonTime ")

def findLessonWeekNumber(str):
    index = str.find("{")
    index_end = str.find("}")
    if index != -1:
        #print("周数："+str[index+1:index_end])
        temp = str.find("-")
        start = int(str[index+1+1:temp])
        end = int(str[temp+1:index_end-1])
        #print(start,end)
        return start,end
    else:
        print("ErrorWeekTime ")

def findLessonTeacher(str):
    index_build = -1
    for i in build:
        index_build = str.find(i)
        
        if index_build != -1:
            break
    index_right = str.find("}")

    if index_build != -1 and index_right != -1:
        teacher = str[index_right+1:index_build]
        #print("教师："+teacher)
        return teacher
    
    else:
        print("ErrorName ")
        return ""

def getBuildIndex(str):
    index_build = -1
    for i in build:
        index_build = str.find(i)
        if index_build != -1:
            break
    return index_build

def getLesson(str):
    
    index_start = -1
    index_end = -1
    temp = str.find("*")
    if temp != -1:
        str = str[:temp]
        print(str)
    index_start = getBuildIndex(str)    #此处为上课地点开始索引
    index_end = index_start + 6         #此处一般为课程信息结尾
    str_length = len(str)

    #print(index_start,index_start,str_length)
    lesson = str[:index_end]
    lecture.append(lesson)
    print(lesson)
    # if index_end == str_length:
    #     print("一节")
    # else:
    #     print(str[index_end:])
    while index_end != str_length:
        str = str[index_end:]

        print(str)

        lesson = str[:index_end]
        lecture.append(lesson)
        
        str_length = len(str)
        index_start = getBuildIndex(str)
        index_end = index_start + 6

def findLessonLocation(str):
    #print()
    index_build = -1
    for i in build:
        index_build = str.find(i)

        if index_build != -1:
            end = index_build + 6
            length = len(str)
            break
    if index_build != -1:
        classroom = str[index_build:end]
        #printprint("教室："+classroom)
        return classroom
    else:
        print("ErrorClassroom ")
        return ""


def remain_zh(word):
    zh_pattern = re.compile(u'[^\u4e00-\u9fa5]+')
    word = re.sub(zh_pattern,"", word)
    return word

# if __name__ == '__main__':
#     lesson_info1 =("面向对象程序设计实验"
#                 +"周二第1,2节{第9-16周}黄大君"
#                 +"躬行楼202面向对象程序设计周二"
#                 +"第1,2节{第1-8周}"
#                 +"黄大君躬行楼202")
#     lesson_info2 = ("论文写作与文献检索"
#                 +"周三第1,2节{第1-8周}"
#                 +"钟锦躬行楼202"

#     )
#     #print(lesson_info1)
#     getLesson(lesson_info1)
#     print()
#     for i in lecture:
#         print("--------------------")
#         print(i)
#         start,end = findLessonWeekNumber(i)
#         print('-->',start,end)
#         for j in range(start,end+1):    #此处是针对数据库设计的方式进行处理
#             print(j)
    #     findLessonName(i)
    #     findLessonWeekday(i)
    #     findLessonDayTime(i)
    #     findLessonWeekNumber(i)
    #     findLessonTeacher(i)
    #     findLessonLocation(i)
    # print(lesson_info2)
    # findLessonLocation(lesson_info1)
    # findLessonLocation(lesson_info2)