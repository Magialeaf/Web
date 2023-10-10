import requests
from lxml import etree

def getHTML(url:str)->str:
    param = {"PGTID":"0d100000-0000-154c-5167-f43a16c126b2","ClickID":"2"}
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url=url, timeout=15, params=param,headers=header)
    response.encoding="UTF-8"
    page_text = response.text
    return page_text

def getRes(text:str,level:int)->dict:
    res = {}
    if level == 1:
        et = etree.HTML(text)
        title = et.xpath('//section[@class="list-main"]//div[@tongji_tag="fcpc_ersflist_gzcount"]//div[@class="property-content-title"]/h3/@title')
        url = et.xpath('//section[@class="list-main"]//div[@tongji_tag="fcpc_ersflist_gzcount"]//a/@href')
        for i in range(len(title)):
            res[title[i]] = url[i]
    elif level == 2:
        pass
    else:
        pass

    return res


def Save(title:str,dic:dict)->None:
    title = title + ".txt"
    ti = list(dic.keys())
    con = list(dic.values())
    with open(title,"w",encoding="UTF-8") as fp:
        for i in range(len(dic)):
            fp.writelines(ti[i] + con[i])
        print("存储成功")

if __name__ == '__main__':
    s = input("确认爬取？\ninput:")
    url = "https://bj.58.com/ershoufang/"
    page_text = getHTML(url)
    dic = getRes(page_text,1)
    Save("house",dic)