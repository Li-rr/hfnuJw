class Course:

    def __init__(self):
        self.cId = 0
        self.cName = ""
        self.cTeacher = ""
        self.cLoc = ""
        self.cTimeStart = ""
        self.cTimeEnd = ""
        self.cWeekStart = ""
        self.cWeekEnd = ""
        self.weekDay = ""
        self.studentId = "" 

        self.build = ['博约楼','躬行楼','逸夫楼','履知楼']
        self.lecture = []

    def getBuildIndex(self,str):
        index_build = -1
        for i in self.build:
            index_build = str.find(i)
            if index_build != -1:
                break
        return index_build   

    def getLesson(self,str):
        index_start = -1
        index_end = -1
        temp = str.find("*")
        if temp != -1:
            str = str[:temp]
            print(str)
        index_start = self.getBuildIndex(str)    #此处为上课地点开始索引
        index_end = index_start + 6         #此处一般为课程信息结尾
        str_length = len(str)

        #print(index_start,index_start,str_length)
        lesson = str[:index_end]
        self.lecture.append(lesson)
        #print(lesson)
        # if index_end == str_length:
        #     print("一节")
        # else:
        #     print(str[index_end:])
        while index_end != str_length:
            str = str[index_end:]

            #print(str)

            lesson = str[:index_end]
            self.lecture.append(lesson)
            
            str_length = len(str)
            index_start = self.getBuildIndex(str)
            index_end = index_start + 6       

    def findLessonName(self,str):
        index = str.find("周")
        if index != -1:
            lessonName = str[0:index]
            #print ("\n课程："+lessonName)
            self.cName = lessonName
            # return lessonName
        else:
            print ("ErrorLesson")
            return ""

    def findLessonTeacher(self,str):
        index_build = -1
        for i in self.build:
            index_build = str.find(i)
            
            if index_build != -1:
                break
        index_right = str.find("}")

        if index_build != -1 and index_right != -1:
            teacher = str[index_right+1:index_build]
            #print("教师："+teacher)
            self.cTeacher = teacher
            # return teacher
        else:
            print("ErrorName ")
            return ""

    def findLessonLocation(self,str):
        
        #print()
        index_build = -1
        for i in self.build:
            index_build = str.find(i)

            if index_build != -1:
                end = index_build + 6
                length = len(str)
                break
        if index_build != -1:
            classroom = str[index_build:end]
            #printprint("教室："+classroom)
            self.cLoc = classroom
            return classroom
        else:
            print("ErrorClassroom ")
            return ""

    def findLessonDayTime(self,str):
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
                self.cTimeStart = start
                self.cTimeEnd = end
                # return start,end
            else:
                start = str[index_start+1:index_1]
                end = str[index_2+1:index_end]
                #print(start,end)
                self.cTimeStart = start
                self.cTimeEnd = end
                # return start,end
        else:
            print("ErrorLessonTime ")

    def findLessonWeekNumber(self,str):
        index = str.find("{")
        index_end = str.find("}")
        if index != -1:
            #print("周数："+str[index+1:index_end])
            temp = str.find("-")
            start = int(str[index+1+1:temp])
            end = int(str[temp+1:index_end-1])
            #print(start,end)
            self.cWeekStart = start
            self.cWeekEnd = end
        else:
            print("ErrorWeekTime ")

    def findLessonWeekday(self,str):
        index1 = str.find("周")

        if index1 != -1:
            weekday = str[index1:index1+2]
            #print("周几："+weekday)
            self.weekDay = weekday
            # return weekday
        else:
            print("ErrorWeekday ")
            # return ""

    def print(self):
        print(self.cId,self.cName,self.cTeacher,
            self.cLoc,self.cTimeStart,self.cTimeEnd,
            self.cWeekStart,self.cWeekEnd,self.weekDay,
            self.studentId)
