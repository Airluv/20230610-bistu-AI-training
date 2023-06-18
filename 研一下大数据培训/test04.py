# develop date:2023/6/17
# 美女图片1-30
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=2166044012%2C3847352253&fp=detail&logid=9037746020871234985&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=0&lpn=0&st=-1&word=%E5%B8%85%E5%93%A5&z=0&ic=&hd=&latest=&copyright=&s=undefined&se=&tab=0&width=&height=&face=undefined&istype=2&qc=&nc=&fr=&simics=&srctype=&bdtype=0&rpstart=0&rpnum=0&cs=4233695404%2C3304185403&catename=&nojc=undefined&album_id=&album_tab=&cardserver=&tabname=&pn=0&rn=30&gsm=1e&1687012470695='

response = requests.get(url,headers=headers)
# print(response.status_code)
p_url = response.json()['data']
for i in range(29):
    # 用n标记图片名字
    n = str(i+1)
    i = p_url[i]['hoverURL']
    # print(i)
    res = requests.get(url=i,headers = headers)
    # with open('img\\'+i[29:36]+'.jpeg',mode='wb')as f:
    with open('img-beauty\\' + n + '.jpeg', mode='wb') as f:
        f.write(res.content)
