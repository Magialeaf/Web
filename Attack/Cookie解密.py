import sqlite3
import sys
import win32crypt

outFile_path = r"D:\Cookies.txt"
sql_file = r'C:\Users\walk\AppData\Local\Google\Chrome\User Data\Default\Cookies'
sql_exe = "select host_key,name,value,encrypted_value from Cookies"
conn = sqlite3.connect(sql_file)
for row in conn.execute(sql_exe):
    pwdHash = str(row[3])
    try:
        ret = win32crypt.CryptUnprotectData(pwdHash,None,None,None,0)
    except:
        print("Fail to decrypt Chrome Cookies")
        sys.exit(-1)
    with open(outFile_path,'a+') as outFile:
        outFile.write('host_key: {0:<20} name: {1:<20} value: {2} \r\n'.format(row[0].encode('gbk'),row[1].encode('gbk'),ret[1].encode('gbk')))
conn.close()
print("All Chrome cOOKIES SAVED TO:\n" + outFile_path)