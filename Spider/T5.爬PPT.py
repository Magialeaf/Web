import requests

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"文件已成功下载到：{save_path}")
    else:
        print("下载文件时出错")

# 示例链接
for i in range(21):
    if i < 10:
        i = "0" + str(i)
    else:
        i = str(i)
    url = "https://file4.renrendoc.com/view/8cae3f46f4aa826fbfb35ee4b0267a90/8cae3f46f4aa826fbfb35ee4b0267a90" + i + ".gif"
    save_path = "AnHen/" + i + ".gif"
    download_file(url, save_path)
