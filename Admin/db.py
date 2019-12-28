import pymysql


with open("config.conf", "r", encoding="utf-8") as f:
    HOST = f.read()
# HOST = '192.168.0.113'  # The server's hostname or IP address
print(HOST)
PORT = 3306

def dbPost(post): 
    try:
        db = pymysql.connect(HOST, 'pi', '1234', 'eee')
        cursor = db.cursor()
        mySql_insert_query = """INSERT INTO post (data) 
                                        VALUES (%s) """
        data = (post)
        cursor.execute(mySql_insert_query, data)
        db.commit()
        print("done")
        return True

    except Exception as e:
        print(e)
        return False

def dbResult(result):
    try: 
        db = pymysql.connect(HOST, 'pi', '1234', 'eee')
        cursor = db.cursor()
        mySql_insert_query = """INSERT INTO results (courseName, courseCode, studentName, regNo, markGrade, timestamp) 
                                        VALUES (%s, %s, %s, %s, %s, %s) """

        for i in result:
            data = (i["courseName"], i["courseCode"], i["studentName"], i["regNo"], i["markGrade"], i["timestamp"])
            # print(data)
            cursor.execute(mySql_insert_query, data)
            db.commit()
        print("done")
        return True

    except Exception as e:
        print(e)
        return False

