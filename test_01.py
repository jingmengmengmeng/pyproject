import urllib.request
import json
import os
import pymysql


def get_book(n):
    url = "https://www.apiopen.top/novelApi"
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    book = json.loads(content)
    book_list = []
    for i in range(0, n):
        book_name = book["data"][i]["bookname"]
        author_name = book["data"][i]["author_name"]
        book_map = {"bookname": book_name, "author_name": author_name}
        book_list.append(book_map)
    return book_list


def write_mysql(contents):
    db = get_mysql_connection()
    for i in range(0, len(contents)):
        insert(db, "books", contents[i]["bookname"],contents[i]["author_name"])

    db.close()


def read_mysql(table_name):
    db = get_mysql_connection()
    cursor = db.cursor()
    sql = "select * from " + table_name
    cursor.execute(sql)
    results = cursor.fetchall()
    book_list = []
    for row in results:
        book = {}
        book['bookname'] = row[0]
        book['author_name'] = row[1]
        book_list.append(book)
    return book_list


def get_mysql_connection():
    # 打开数据库连接
    db = pymysql.connect("100.73.141.147", "root", "root", "test")

    return db


def insert(db, table_name, bookname, author_name):
    cursor = db.cursor()
    sql = "insert into " + table_name + "(book_name,author_name) " + "values(\"" + bookname + "\",\"" + author_name + "\")"
    print(sql)
    cursor.execute(sql)
    db.commit()


def write_files(book_list):
    path = "d:\\books"
    create_dir(path)
    for i in range(0, len(book_list)):
        file_name = path + "\\book_" + str(i+1) + ".txt"
        write_file(file_name, book_list[i]["bookname"])
        write_file(file_name, book_list[i]["author_name"])


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def write_file(file_name, content):
    f = open(file_name, 'a+', encoding='utf8')
    f.write(content+"\n")
    f.close()


def read_files(dir):
    files = os.listdir(dir)
    books = []
    for file in files:
        file_name = dir + '\\' + file
        book = read_file(file_name)
        books.append(book)
    return books


def read_file(file_name):
    f = open(file_name, "r+", encoding='utf-8')
    book = {}
    bookname = f.readline().strip()

    author_name = f.readline().strip()
    book['bookname'] = bookname
    book['author_name'] = author_name
    return book


if __name__ == "__main__":
    book_list = get_book(3)
    write_files(book_list)
    books = read_files("d:\\books")
    write_mysql(books)
    book_list = read_mysql("books")
    write_files(book_list)
