from urllib import request, parse
import http.cookiejar

# # urlopen(url, data, timeout)
# url = "http://www.bilibili.com"
# response1 = request.urlopen(url)

# data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
# print(data)
# response2 = request.urlopen(url, data=data)

# response3 = request.urlopen(url, timeout=1)
# result = response1.read().decode('utf-8')

# # request
# req = request.Request('https://python.org')
# response1 = request.urlopen(req)
# print(response.read().decode('utf-8'))

# # request with header
# url = 'http://httpbin.org/post'
# dic = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dic), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# # requesr with proxy
# proxy_handler = request.ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = request.build_opener(proxy_handler)
# response = opener.open('http://httpbin.org/get')
# print(response.read())

# # cookie
# cookie = http.cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)

# # MozillaCookieJar
# filename = "cookie_MozillaCookieJar.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# # LWPCookieJar
# filename = 'cookie_LWPCookieJar.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# # load cookie
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie_LWPCookieJar.txt', ignore_discard=True, ignore_expires=True)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# # urlparse
# result = parse.urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# print(result)

# # urlunparse
# data = ['http','www.baidu.com','index.html','user','a=123','commit']
# url = parse.urlunparse(data)
# print(url)

# # urljoin
# print(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
# print(parse.urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
# print(parse.urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
# print(parse.urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
# print(parse.urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
# print(parse.urljoin('http://www.baidu.com', '?category=2#comment'))
# print(parse.urljoin('www.baidu.com', '?category=2#comment'))
# print(parse.urljoin('www.baidu.com#comment', '?category=2'))

# # urlencode
# params = {
#     'name':'zhaofan',
#     'age':'23'
# }
# base_url = "http://baidu.com"
# url = base_url + parse.urlencode(params)
# print(url)