import requests
import json

# response =requests.get('http://www.baidu.com')
# response.encoding = "utf-8"
# print(response.text)
# # content is binary data
# print(response.content) 
# print(response.content.decode("utf-8"))

# # request
# data = {
#     "name":'zhaofan',
#     "age":22
# }
# response = requests.get("http://www.baidu.com", params=data)
# print(response.url)
# print(response.content.decode("utf-8"))

# # json
# response =requests.get('http://httpbin.org/get')
# print(response.text)
# print(type(response.text))
# print(response.json())
# # response.json() equals json.loads()
# print(type(response.json()))
# print(json.loads(response.text)) 

# # data
# data = {
#     "name":"zhaofan",
#     "age":23
# }
# response = requests.get('https://www.zhihu.com', data=data)
# print(response.text)

# # file
# files= {"files":open("git.jpeg","rb")}
# response = requests.post("http://httpbin.org/post",files=files)
# print(response.text)

# # cookie
# response = requests.get("http://www.baidu.com")
# print(response.cookies)

# for key,value in response.cookies.items():
#     print(key+"="+value)

# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)

# proxies= {
#     "http":"http://127.0.0.1:9999",
#     "https":"http://127.0.0.1:8888"
# }
# response  = requests.get("https://www.baidu.com",proxies=proxies)
# print(response.text)