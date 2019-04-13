import json
import urllib.request
import urllib.parse
import urllib
import re



def get_weather():
    url = "https://api.apiopen.top/recommendPoetry"
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return json.loads(content)
print(get_weather())

fo = open("foo.txt", "w")
fo.write("get_weather")



