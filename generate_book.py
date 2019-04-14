import urllib.request
import json
import os


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


if __name__ == "__main__":
    book_list = get_book(4)
    write_files(book_list)
    print(book_list)
