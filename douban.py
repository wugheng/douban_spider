import urllib.request
import urllib.parse
import re

class DB:

    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl,start):
        self.baseURL = baseUrl

    # 传入页码，获取该页帖子的代码
    def getPage(self,pagenum):
        try:
            url = self.baseURL +'?start='+str(pagenum);
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            # print(response.read())
            return response.read().decode("UTF-8")
        except urllib.request.URLError as e:
            if hasattr(e, "reason"):
                print(u"错误原因", e.reason)
                return None

    def getTitle(self,pagenum):
        page = self.getPage(pagenum)
        pattern1 = re.compile('<span class="title">(.*?)</span>([\s\S]*?)<span class="(?:.*?)">&nbsp;/&nbsp;(?:.*?)</span>',re.S)
        pattern2=re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
        pattern3=re.compile('<p class="quote">([\s\S]*?)<span class="inq">(.*?)</span>([\s\S]*?)</p>')
        result1 = re.findall(pattern1,page)#使用search寻找函数时要使用编码转换否则会出现乱码
        result2=re.findall(pattern2,page)
        result3=re.findall(pattern3,page)
        if result1 and result2 and result3:
            for index, value in enumerate(result1):
                print("<<"+value[0]+">>:"+result2[index])
                print("引言:"+result3[index][1])
            # print(result3)
            return result1 and result2 and result3
        else:
            print("2222")
            return None

baseURL = 'https://movie.douban.com/top250'
for i in range(4):
    db = DB(baseURL, i+1)
    db.getTitle(i+1)