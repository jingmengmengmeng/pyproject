import urllib.request
import urllib.parse
import urllib
import json
import os
import pymysql


def get_poems(num):
    contents = []
    for i in range(0, num):
        contents.append(get_poem())
    return contents


def get_poem():
    url = "https://api.apiopen.top/recommendPoetry"
    data = {}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    new_url = urllib.request.Request(url, data)
    response = urllib.request.urlopen(new_url)
    response = response.read().decode('utf-8')
    content = json.loads(response)['result']['content']
    return content


def write_mysql(contents):
    db = get_mysql_connection()
    for i in range(0, len(contents)):
        insert(db, "poems", contents[i])
    db.close()


def get_mysql_connection():
    # 打开数据库连接
    db = pymysql.connect("100.73.141.147", "root", "root", "test")

    return db


def insert(db, table_name, content):
   
    cursor = db.cursor()

    sql = "insert into " + table_name + "(content) " + "values(\"" + content + "\")"
    print(sql)
    cursor.execute(sql)
    db.commit()

    pass


def write_files(contents):
    path = "d:\poems"
    create_dir(path)
    for i in range(0, len(contents)):
        file_name = path + "\poem_" + str(i+1) + ".txt"
        write_file(file_name, contents[i])


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def write_file(file_name, content):
    f = open(file_name, 'w+', encoding='utf8')
    f.write(content)
    f.close()


if __name__ == "__main__":
    contents = get_poems(3)
    write_mysql(contents)