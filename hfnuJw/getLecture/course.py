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

        self.build = ['博约楼','躬行楼','逸夫楼','履知楼','锦绣篮球场']
        self.lecture = []

    def getBuildIndex(self,str):
        index_build = -1
        min_build = 9999
        for i in self.build:
            index_build = str.find(i)

            if index_build != -1:
                if index_build < min_build:
                    min_build = index_build
                
        #print("====",min_build)
        if min_build == 9999:
            min_build = -1
        return min_build   

    # def findNumber(self,str,index):
    #     print("this is number")

    #     index_end = 0

    #     for i in range(index-3,index+3):
    #         if i == len(str):
    #             index_end = index
    #             break
    #         if str[i-1].isdigit() == True:
    #             index_end = i 
    #     # if str[index-1].isdigit() == True:
    #     #     print(index,len(str),str[index-1])
    #     #     index_end = index
    #     # elif str[index].isdigit() ==True:
    #     #     index_end = index+1
    #     # if str[index].isdigit() == True and index+1 == len(str):
    #     #     index_end = index+1
    #     #     if index+2 == len(str) and str[index+1].isdigit() == True :
    #     #         index_end = index+2
    #     #         if index+3 == len(str) and str[index+2].isdigit() == True :
    #     #             index_end = index+3
        return index_end
    def getLesson(self,str):
        while True:
            #print("--",str)
            temp = str.find("*")
            if temp != -1:
                str = str[:temp]
            index_left = str.find("(")
            index_right = str.find(")")

            index_end = -1
            if index_left != -1 and index_right != -1:
                str = str[:index_left] + str[index_right+1:]

            index_start = self.getBuildIndex(str)
            #print(str[index_start],len(str))

            temp_pe = str.find("场")
            if temp_pe != -1:
                index_end = temp_pe+1
            elif temp_pe == -1:
                if str[index_start+3].isalpha() == True:
                    index_end = index_start+7       #此处一般为课程信息结尾,针对逸夫楼A206的情况
                else:
                    index_end = index_start + 6   

            str_length = len(str)
            lesson = str[:index_end]
            #print("lesson:",lesson,index_start,index_end,len(str))
            self.lecture.append(lesson) 
            
            str = str[index_end:]
            #print("fuck:",str)
            index_start = self.getBuildIndex(str)
            #print("asd",index_start)
            if index_start == -1:
                break  

  

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
