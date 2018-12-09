#/usr/bin/env python
#coding=utf8
 
import http.client
import hashlib
import urllib
import random

appid = '' #你的appid
secretKey = '' #你的密钥

 
httpClient = None

def engtoch(q):
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf8"))
    sign = m1.hexdigest()
    myurl = '/api/trans/vip/translate'
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        return response.read()
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
def chtoeng(q):
    fromLang = 'zh'
    toLang = 'en'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf8"))
    sign = m1.hexdigest()
    myurl = '/api/trans/vip/translate'
    myurl = myurl+'?appid='+appid+'&q='+urllib.parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        return response.read()
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
