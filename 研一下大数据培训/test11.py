# develop date:2023/6/17
# 帅哥图片91-120
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=0%2C0&fp=detail&logid=9452893277938860863&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=undefined&word=%E7%94%B7%E7%94%9F&z=0&ic=undefined&hd=undefined&latest=undefined&copyright=undefined&s=undefined&se=&tab=0&width=undefined&height=undefined&face=undefined&istype=0&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=2148224005%2C1852072151&catename=&nojc=undefined&album_id=&album_tab=&cardserver=&tabname=&pn=30&rn=60&gsm=1e&1687013732249='

response = requests.get(url,headers=headers)
# print(response.status_code)
p_url = response.json()['data']
for i in range(91):
    # 用n标记图片名字
    n = str(i+91)
    i = p_url[i]['hoverURL']
    # print(i)
    res = requests.get(url=i,headers = headers)
    # with open('img\\'+i[29:36]+'.jpeg',mode='wb')as f:
    with open('img-handsome\\' + n + '.jpeg', mode='wb') as f:
        f.write(res.content)
