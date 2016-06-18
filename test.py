import urllib.request
import http.cookiejar

url = "http://www.baidu.com"

print ("first method")
response1=urllib.request.urlopen(url)
print (response1.getcode())
print (len(response1.read()))


print ('second method')
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print (response2.getcode())
print (len(response2.read()))


print ('third method')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print (response3.getcode())
print(cj)
print (len(response3.read()))