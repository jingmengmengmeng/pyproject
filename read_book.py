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


def read_files(dir):
    files = os.listdir(dir) #列举一个目录下所有文件名称，得到一个数组['poem_1.txt', 'poem_2.txt', 'poem_3.txt']
    poems = []
    for file in files:
        file_name = dir + '\\' + file #遍历文件列表，和父级目录拼接在一起，形成完整的文件名 d:\poems + \ + poem_1.txt
        poem = read_file(file_name)
        poems.append(poem)
    return poems


def read_file(file_name):
    f = open(file_name, "r+", encoding='utf-8') #以读方式打开文件
    poem = f.readline()#从文件中读取一行，返回该行内容
    return poem


if __name__ == "__main__":
    print(read_files('d:\poems'))