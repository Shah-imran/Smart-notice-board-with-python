import pymysql
import var



HOST = '192.168.0.113'  # The server's hostname or IP address
PORT = 3306

def dbPost(): 
    try:
        # print("here")
        db = pymysql.connect(HOST, 'pi', '1234', 'eee')
        cursor = db.cursor()
        mySql_insert_query = """SELECT data, timestamp FROM post WHERE status = 0"""
        cursor.execute(mySql_insert_query)
        data = cursor.fetchall()
        # print(data[0][1])
        # print(type(str(data[0][1])))
        if data:
            mySql_insert_query = """UPDATE post SET status = 1 WHERE status = 0"""
            cursor.execute(mySql_insert_query)
            db.commit()
            
            for i in data:
                var.postQ.put(i[0] + " - " + str(i[1]))
            
        # print("done")
        return True

    except Exception as e:
        print(e)
        return False

def getList(): 
    try:
        # print("here")
        db = pymysql.connect(HOST, 'pi', '1234', 'eee')
        cursor = db.cursor()
        mySql_insert_query = """SELECT courseName, courseCode, timestamp FROM results"""
        cursor.execute(mySql_insert_query)
        data = cursor.fetchall()
        if data:
            temp = list()
            temp = set(data)
            if var.tempCourseList != temp:
                var.tempCourseList = temp
                for i in temp:
                    var.courseList.append(i[0] + " - " + i[1] + " - " + i[2])
            print(var.courseList)
            
        # print("got list")
        return True

    except Exception as e:
        print(e)
        return False

def getResults(data): 
    try:
        # print("here")
        db = pymysql.connect(HOST, 'pi', '1234', 'eee')
        cursor = db.cursor()
        mySql_insert_query = """SELECT studentName, regNo, markGrade FROM results where courseCode = %s"""
        temp = (data[1])
        cursor.execute(mySql_insert_query, temp)
        data = cursor.fetchall()
        if data:
            # print(data)
            pass
            
        # print("got results")
        return data

    except Exception as e:
        print(e)
        return False


