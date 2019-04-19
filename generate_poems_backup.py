import pymysql
import os


def get_mysql_connection():
    # 打开数据库连接
    db = pymysql.connect("100.73.141.147", "root", "root", "test")

    return db



def read_mysql(table_name):
    db = get_mysql_connection()
    cursor = db.cursor()
    sql = "select * from " + table_name
    cursor.execute(sql)
    results = cursor.fetchall()
    poems_list = []
    for row in results:
        poems = {}
        poems['id'] = row[0]
        poems['content'] = row[1]
        poems_list.append(poems)
    return poems_list


def insert(db, table_name, content):
    cursor = db.cursor()
    sql = "insert into " + table_name + "(content) " + "values(\"" + content + "\")"
    print(sql)
    cursor.execute(sql)

    db.commit()


def write_mysql(contents):
    db = get_mysql_connection()
    for i in range(0,len(contents)):
        insert(db, "poems_backup", contents[i]["content"])
    db.close()


if __name__ == "__main__":
    print(read_mysql("poems"))
    write_mysql(read_mysql("poems"))