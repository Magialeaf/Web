import requests
import json

def getHTML(value:str)->str:
    url = "https://movie.douban.com/j/chart/top_list?"
    param = { "type":"25","interval_id":"100:90","action":"","start":value,"limit":"20"}
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url=url,timeout=15,params=param,headers=header)
    list_json = response.json()
    response.encoding = "UTF-8"
    return list_json

def Save(value:str,res:str)->None:
    filename = "from" + value + "to" + str(int(value)+20) + ".json"
    with open(filename,"w",encoding="UTF-8") as f:
        json.dump(res,f,ensure_ascii=False)
    print("已存入{}".format(filename))

if __name__ == '__main__':
    value = input("输入开始电影位置:")
    list_json = getHTML(value)
    for i in list_json:
        print(i["title"])
    Save(value,list_json)