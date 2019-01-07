from datetime import datetime
import hashlib
import urllib
import urllib.request

APP_ID_VALUE = "RVJpNFXUlgoCcvIFJYpbigQIXELMXEno"
APP_SECRET_VALUE = "qF1r6m7Z0oY1ntuarkLWiFjysxTPlxMVK9e1r0PiV2jTj66fNK1WSHkaCNWnvseY"
APP_SECRET = "appSecret"
APP_ID = "appId"
BIZ_CONTENT = "bizContent"
TIMESTAMP = "timestamp"
SIGN = "sign"
OPEN_API_URL = "http://openapi.epandian.cn/v1/openCompany/addCompany"

def dateToString():
    dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def addCompanyContent(companyCode = "", name = ""):
    return '{"companyCode":"' + companyCode + '",' + '"name":"' + name + '"}'

def signList():
    myList = list()
    myList.append(APP_ID + '=' + APP_ID_VALUE)
    myList.append(TIMESTAMP + '=' + dateToString())
    myList.append(BIZ_CONTENT + '=' + addCompanyContent(companyCode = "001", name = "传化化工"))
    myList.sort()
    myString = ""
    mylen = len(myList) - 1
    for i in range(mylen):
        myString += myList[i]
        myString += "&"
    myString += myList[mylen]
    myString = myString + "&" + APP_SECRET + "=" + APP_SECRET_VALUE
    s1 = hashlib.sha1()
    s1.update(myString.encode("utf8"))
    return s1.hexdigest()

def addCompanyRequest():
    #test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
    date_string = dateToString()
    biz_content_string = addCompanyContent(companyCode = "001", name = "传化化工")
    sign_string = signList()
    test_data = {APP_ID:APP_ID_VALUE,TIMESTAMP:date_string,BIZ_CONTENT:biz_content_string,SIGN:sign_string}
    print(test_data)
    test_data_urlencode = urllib.parse.urlencode(test_data).encode(encoding='UTF8')
    requrl = OPEN_API_URL
    req = urllib.request.Request(url = requrl,data =test_data_urlencode)
    print(req)
    res_data = urllib.request.urlopen(req)
    res = res_data.read()
    print(res)
        
        
    

   

