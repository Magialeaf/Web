import requests
from bs4 import BeautifulSoup

def getHTML(value:str)->str:
    url = "https://www.sogou.com/sogou"
    param = {"query":value}
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response =  requests.get(url=url,timeout=15,params=param,headers=header)
    response.encoding="UTF-8"
    page_text = response.text
    return page_text

def getRes(text:str)->str:
    bf = BeautifulSoup(text,"html.parser")
    text = bf.prettify()
    #print("爬取的网页如下\n",text)
    return text

def Save(value:str,res:str)->None:
    filename = value + ".txt"
    with open(filename,"w",encoding="UTF-8") as fp:
        fp.write(res)
        print(filename,"存储成功")

if __name__ == '__main__':
    value = input("输入参数（搜狗浏览器搜索）:")
    page_text = getHTML(value)
    text = getRes(page_text)
    Save(value,text)