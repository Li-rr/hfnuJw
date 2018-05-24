# -*- coding: utf-8 -*-
import pymysql
import traceback 
def getDataBase():

    connect = pymysql.connect(
        host='localhost',
        # port = 3306,    
        user='lrr',
        passwd='lrr1996429',
        db='persontable',
        charset='utf8')
    return connect
def insertData(data):
    connect = getDataBase()
    sql = (
        "insert into course(c_id,c_name,c_teacher,c_loc,c_time) "
        + "VALUES ( '%d','%s','%s','%s','%s')"
        ) 
    sql2 = '''
        insert into course(c_id,c_name,c_teacher,c_loc,c_time_start,
        c_time_end,weekday,studentId) VALUES('%d','%s','%s','%s','%d','%d','%s','%s')
        '''
    sql3 = '''
        insert into course(c_name,c_teacher,c_loc,c_time_start,
        c_time_end,weekday,student_cid) VALUES('%s','%s','%s','%d','%d','%s','%s')    
        '''
    sql4 = '''
    insert into course(c_name,c_teacher,c_loc,c_time_start,
    c_time_end,weekday,student_cid,student_id) VALUES('%s','%s','%s','%d','%d','%s','%s','%s')    
    '''
    iD = data[0]

    # flag = queryDataById(iD)
    # if int(flag) == 1:
    #     return

    # print('student --> ',stud)
    # data=(0,"数据结构","王群芳","逸夫楼202","1-2节")
    
    cursor = connect.cursor()
    try:
        cursor.execute(sql4%data) #执行插入语句
        connect.commit()    #执行sql语句
        print('成功插入', cursor.rowcount, '条数据')
    except:
        traceback.print_exc() 
        connect.rollback()
    
    closeDataBase(connect)
    # cursor.execute(sql % data)
    # connect.commit()
    
def queryDataById(student_cid):
    flag = 0
    connect = getDataBase()
    sql = "select * from course where student_cid = " + "'%s'"

    cursor = connect.cursor()
    try:
        cursor.execute(sql%student_cid)
        results = cursor.fetchall()
        print("result: ",results,type(results))
        print("result length: ",len(results))
        if len(results) > 0:
            flag = 1
            print("查询成功 flag:",flag)
        else:
            print("查询无此数")
    except:
        print("查询失败")
        traceback.print_exc() 
        connect.rollback()        
    return flag

def queryDataByStudentId(studentId):
    flag = 0
    connect = getDataBase()
    sql = "select * from course where studentId = " + "%s"

    cursor = connect.cursor()
    try:
        cursor.execute(sql%studentId)
        results = cursor.fetchall()
        for row in results:
            for i in row:
                print(i,end=" ")
            print(type(row))
        # print("result: ",results,type(results))
        print("result length: ",len(results))
        if len(results) > 0:
            flag = 1
            print("查询成功 flag:",flag)
        else:
            print("查询无此数")
    except:
        print("查询失败")
        traceback.print_exc() 
        connect.rollback()        
    return results   

def queryData():
    connect = getDataBase()
    sql = "select * from course;"

    cursor = connect.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()   #fetchall():接收全部的返回结果行
        for row in results:
            for i in row:
                print(i,end=' ')
            print()
        
        print("result: ",results,type(results))
        print("result length: ",len(results))
            # cId = row[0]
            # cName = row[1]
            # cTeacher = row[2]
            # cLoc = row[3]
            # cTime = row[4]
            # print(cId,cName,cTeacher,cLoc,cTime)
    except:
        traceback.print_exc() 
        print("Error: unable to fetch data")
    closeDataBase(connect)
    # cursor.execute(sql)
    # for row in cursor.fetchall():
    #     print("Name:%s\tSaving:%.2f" % row)
def updateData(connection,target,data):
    print("暂时用不到")

def deleteData():
    connect = getDataBase()

    sql_delete = 'delete from course;'
    cursor = connect.cursor()
    try:
        cursor.execute(sql_delete)  
        connect.commit()    #执行sql语句
        print("删除成功")
        
    except:
        traceback.print_exc()
        print("删除失败")
    closeDataBase(connect)
def closeDataBase(connect):
    connect.close()

# if __name__ == '__main__':
#     db = getDataBase()
#     print("asd")
#     insertData(db)
#     queryData(db)
#     closeDataBase(db)

# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()