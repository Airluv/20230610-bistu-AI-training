# develop date:2023/6/17
import requests
from bs4 import BeautifulSoup

def download(url):
    res = requests.get(url)
    img = res.content
    filename = 'img/' + url.split("/")[-1]
    with open(filename,"wb") as f:
        f.write(img)

def get_html():
    url='http://www.netbian.com/e/search/result/?searchid=747'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.encoding='gbk'
    if res.status_code == 200:
        html = res.text
        soup = BeautifulSoup(html,'lxml')
        all_list = soup.find(class_="pic_box")
        all_img = all_list.find_all("img")
        for img in all_img:
            src = img['src']
            download(src)
if __name__=='__main__':
    get_html()

