import base64

import requests
import re

if __name__ == '__main__':
    url = "https://www.sohu.com/a/162341279_667858"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url=url,headers=header).text
    ex = '<p><img data-src="(.*?)" /></p>'
    img_lst = re.findall(ex,response,re.S)
    for i in img_lst:
        s = base64.b64decode(i)
        print(s)
    # res = response.content
    # with open("img/1.png","wb") as f:
    #     f.write(res)
    # print("OK")

#ex = '<article class="article" id="mp-editor">.*?<p>./*?<img src="(.*/?)"</p></article>'