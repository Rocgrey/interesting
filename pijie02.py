'''
# from .myzipfile import sizeFileHeader
# from .myselfpackage import bao1
from .myselfpackage.bao1 import myzipfile
# from myselpackage import myzipf
filezip = myzipfile.ZipFile("080.zip")
password = '123456'
# password = str(password).encode("gbk")
# filezip.extractall(pwd=password)
filezip.extractall("E:\\python_practice\\yixuewenjian\\test003\\加密方法",pwd=password)



'''
import zipfile
# 生成密码本,zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
f = open("pwd1.txt", "w+")
for id in range(1000000):
    sixword = str(id).zfill(6)+"\n"
    f.write(sixword)
    threeword = str(id).zfill(3)+ "\n"
    f.write(threeword)
    eightword = str(id).zfill(8)+ "\n"
    f.write(eightword)
f.close()
# 验证：原始密码：password = "123"
# 这个压缩文件必须得是以传统加密方法加密的才可以
zfile = zipfile.ZipFile("呵呵.zip")
# 这个是没有破解出来，可能不是以传统方式加密的
# zfile = zipfile.ZipFile("《Python数据分析与数据化运营(宋天龙)》PDF高清+源代码+数据.zip")
# 读取设定的密码：
passFile = open('pwd1.txt')
for line in passFile.readlines():
    try:
        password = line.strip('\n')
        zfile.extractall(path="E:\\python_practice\\yixuewenjian\\test003\\加密方法", members=zfile.namelist(),
                 pwd=password.encode("utf-8"))
        print("正确密码是：%s" % password)
        break
    except:
        print("又错了")