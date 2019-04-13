import re


def match_date(date):
    a2 = r"(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2}):(\d{2})"
    pattrern1 = re.compile(a2)
    matcher1 = re.search(pattrern1,date)
    return matcher1.group(0)




if __name__ == "__main__":
    date = r"2019-04-11 18:55:00"
    print(match_date(date))




def match_date(date):
    a2 = r"[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) ([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]"


    pattrern1 = re.compile(a2)
    matcher1 = re.search(pattrern1,date)
    return matcher1.group(0)




if __name__ == "__main__":

    date = r"2019-12-11 23:59:59"
    print(match_date(date))
