import requests
import json

def getHTML(value:str)->str:
    url = "https://fanyi.baidu.com/sug"
    data = { "kw":value }
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.post(url=url,timeout=15,data=data,headers=header)
    dic_json = response.json()
    response.encoding = "UTF-8"
    return dic_json

def Save(value:str,res:str)->None:
    filename = value + ".json"
    with open(filename,"w",encoding="UTF-8") as f:
        json.dump(res,f,ensure_ascii=False)
    print("已存入{}".format(filename))

if __name__ == '__main__':
    value = input("输入单词:")
    dic_json = getHTML(value)
    Save(value,dic_json)