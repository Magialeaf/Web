import requests
from bs4 import BeautifulSoup

def getHTML(url:str)->str:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    response = requests.get(url=url, timeout=15, headers=header)
    response.encoding = "UTF-8"
    page_text = response.text
    return page_text

if __name__ == '__main__':
    s = input("确认爬取？\ninput:")
    url = "https://www.shicimingju.com/book/sanguoyanyi.html"
    page_text = getHTML(url)

    soup = BeautifulSoup(page_text,"lxml")
    li_list = soup.select(".book-mulu > ul > li")
    fp  = open("三国演义.txt", "w", encoding="UTF-8")
    count = 0
    for li in li_list:
        title = li.a.text
        title.strip("\n")
        detail_url = li.a["href"]
        new_url = "https://www.shicimingju.com" + detail_url
        page = getHTML(new_url)

        new_soup = BeautifulSoup(page, "lxml")
        text = new_soup.select(".chapter_content")
        content = text[0].text
        content = content.strip(" ")
        res = ""
        length = 60
        for i in range(len(content) // length + 1):
            res = res + content[i*length:(i+1)*length] + "\n"
        fp.write(title+":"+res)
        print(title+" 成功存入")
        count += 1
        if count == 5:
            break
    fp.close()





