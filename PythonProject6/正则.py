import re
# lst = re.findall("\\d+","我的电话是10086,我聘用是的23482")
# print(lst)
#
# it = re.finditer(r"\d+","我的电话是10086,我聘用是的23482")
# for i in it:
#  print(i.group())

# s = re.search(r"\d+","我的电话是10086,我聘用是的23482")
# print(s.group())

# s = re.match(r"\d+","10086,我聘用是的23482")
# print(s.group())

s = r"我的电话是10086,我聘用是的23482"
obj = re.compile(r"\d+")
ret = obj.finditer(s)
for match in ret:
 print(match.group())

 #re.S能匹配换行符
 #(?P<kjwekf>.*?) 提取特定的东西
 #it.group("kjwekf")
