# develop date:2023/6/17
import requests
import urllib.request
from bs4 import BeautifulSoup

def getMoviesImg():
    url = requests.get('https://www.vcg.com/creative-image/nanshengzhaopian/')
    #获取网站数据
    html = url.text
    #解析网页
    soup = BeautifulSoup(html,'html.parser')
    #获取所有的img标签
    movie = soup.find_all('img')
    x = 1
    for i in movie:
        # 获取src路径
        imgsrc = i.get('src')
        #判断图片src路径是否以指定内容开头（过滤页面中的其它不想要的图片）
        # if imgsrc.startswith('http://static.jstv.com/gather/hl/20171018/'):
            # print(imgsrc)
            #本地路径
        filename = '"D:/AAA软件使用测试/python/研一下大数据培训/img"/%s.jpg'%x
        #将URL表示的网络对象复制到本地文件
        urllib.request.urlretrieve(imgsrc , filename)
        print('下载第%d张' % x)
        x += 1
    print('**下载完成!**')

getMoviesImg()
