import requests
from bs4 import BeautifulSoup

def getHTML(url:str)->str:
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url=url, timeout=15, headers=header)
    response.encoding="UTF-8"
    page_text = response.text
    return page_text

def getRes(text:str)->str:
    bf = BeautifulSoup(text,"html.parser")
    text = bf.prettify()
    print("爬取的网页如下\n",text)
    return text

def Save(res:str)->None:
    with open("res.txt", "w", encoding="UTF-8") as fp:
        fp.write(res)
        print("存储成功")

#    url = "https://123.sogou.com/"
if __name__ == '__main__':
    url = input("输入爬取的网站网址:")
    url = url
    page_text = getHTML(url)
    text = getRes(page_text)
    Save(text)