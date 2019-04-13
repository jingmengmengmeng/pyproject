import json
import urllib.request
import urllib.parse
import urllib
import re



def get_weather():
    url = "http://t.weather.sojson.com/api/weather/city/101270101"
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return json.loads(content)


data = get_weather()["data"]
#print(get_weather())
#print(get_weather()["data"]["wendu"])
#print(data['wendu'])

#print(get_weather()["cityInfo"]["parent"])
#print(get_weather()["data"]["forecast"][0]["high"])


def set_weather():
    url="https://api.apiopen.top/recommendPoetry"
    response = urllib.request.urlopen(url)
    content =response.read().decode('utf-8')
    return json.loads(content)


def post_weather():
    url="https://api.apiopen.top/recommendPoetry"
    data = {}
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    new_url = urllib.request.Request(url,data)
    response = urllib.request.urlopen(new_url)
    response = response.read().decode('utf-8')
    return json.loads(response)
print(post_weather())




def get_test():
    key = r"abAC2355_ssss"
    a1 = r"[a-zA-Z0-9_-]{10,16}"
    pattern1 = re.compile(a1)
    matcher1 = re.search(pattern1, key)
    return matcher1.group(0)
print(get_test())





#print(set_weather())
#print(set_weather()["result"]["title"])



