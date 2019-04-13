import re



key=r"abAC2355_ssss"
a1=r"[a-zA-Z0-9_-]{10,16}"
pattern1=re.compile(a1)
matcher1=re.search(pattern1,key)
print(matcher1.group(0))


