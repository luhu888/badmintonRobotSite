# coding=utf-8
# author:luhu
import requests

data = {"id":3,
        "name":'trtre'}

# res = requests.post(url='http://127.0.0.1:8000/api/badminton/',json=data)
# print(res.text)
# str = str(b'{"name": "trtre", "id": 3}')
# str1 = str[2:]
# str2= str1[:-1]
# print(str2)

data1 = {"user_id": '3434', "name": 'te', "activity_num": 678}
res = requests.post(url='http://127.0.0.1:8000/api/join_activity/', json=data1)
print(res.text)