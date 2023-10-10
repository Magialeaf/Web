import sys
import threading
from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QLabel,QPushButton,QApplication,QWidget,QDesktopWidget,QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import requests
import subprocess


class Login(QThread):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        res = "Bad!"
        try:
            self.spider()
            if self.Ping() == 0:
                res = "登录成功！"
            else:
                res = "登录失败！"
        except Exception as e:
            res = e
            self.driver.close()
        finally:
            res = "End!"
            self.my_signal.emit(res)


    def find_ser(self):
        file = r"C:\Users\11323\Desktop\Update\chromedriver.exe"
        try:
            fp = open(file, 'r')
            fp.close()
            return 0
        except:
            return -1

    def spider(self):

        # op = Options()
        # op.add_argument('--headless')
        # op.add_argument('--disable-gpu')
        # op.add_experimental_option('excludeSwitches', ['enable-automation'])
        f = self.find_ser()
        if f == 0:
            ser = Service(r"C:\Users\11323\Desktop\Update\chromedriver.exe")
            self.driver = webdriver.Chrome(service=ser)  # options=op
            self.driver.get("http://172.21.255.105/?isReback=1")  # 这里输入你的校园网登录网址
            time.sleep(1)
            input_tag1 = self.driver.find_element(by=By.XPATH,value="//form[@name='f1']/input[@name = 'DDDDD']")  # 通过xpath确定账号框位置
            input_tag1.send_keys("2020211044")  # 输入账号
            input_tag2 = self.driver.find_element(by=By.XPATH,value="//form[@name='f1']/input[@name = 'upass']")  # 通过xpath确定密码框位置
            input_tag2.send_keys("0AngelBeats0")  # 输入密码
            input_tag3 = self.driver.find_element(by=By.NAME, value="ISP_select")  # 找到组合框，这个可以通过name直接找
            input_tag3.send_keys("中国移动")  # 这是组合框，要选择你的宽带的运营商
            action = ActionChains(self.driver)
            action.move_by_offset(420, 420).perform()
            action.click().perform()
            time.sleep(3)  # 3秒后自动关闭浏览器
            self.driver.close()
            return 0
        else:
            return -1

    # 网络式
    # def spider():
    #     session = requests.Session()
    #     url = "http://172.21.255.105/a79.htm?userip=172.22.252.77&wlanacname=&wlanacip=172.21.255.106&usermac=555e8adc040a24ce9ddb2e6b08065be4832d21333493c982"
    #     header = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"}
    #     response = session.get(url=url, timeout=15, headers=header)

    # 测试网络是否连通
    def Ping(self):
        backinfo = subprocess.call('ping www.baidu.com -n 1', shell=True, stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if backinfo:
            return -1
        else:
            return 0


class Spider(QWidget):
    def __init__(self):
        super(Spider, self).__init__()
        self.Win()

    def Win(self):
        # 设置窗口标题
        self.setWindowTitle("校园网登录")
        # 展示窗口
        width = 500
        height = 400
        self.resize(width, height)
        center_point = QDesktopWidget().availableGeometry().center()
        x = center_point.x()
        y = center_point.y()
        self.move(x - width // 2,y - height // 2)

        # 布局
        self.main = QVBoxLayout(self)
        self.top = QHBoxLayout()

        self.tip = QLabel("登录：")
        self.bt = QPushButton("确认")

        self.lo = Login()
        self.lo.my_signal.connect(self.finish_login)

        self.bt.clicked.connect(self.login)
        self.text = QTextEdit()

        self.top.addWidget(self.tip)
        self.top.addWidget(self.bt)
        self.main.addLayout(self.top)
        self.main.addWidget(self.text)

    def login(self):
        res = "开始登录......"
        self.text.setPlaceholderText(res)
        self.lo.start()

    def finish_login(self,res):
        self.text.setPlainText(res)

if __name__ =="__main__":
    app = QApplication(sys.argv)

    demo = Spider()
    demo.show()

    app.exec()