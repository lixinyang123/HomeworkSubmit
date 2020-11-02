from flask import *
import os,datetime,io,json

savePath = json.loads(io.open("./config/config.json","r").read())["SavePath"]

# 创建默认存储路径
if not os.path.exists(savePath):
    os.mkdir(savePath)

# 生成文件完整名称（保存路径 + 文件名称）
def GetFullPath():

    # 获取班级id
    userId = request.form["userId"].replace("0223012006","")
    name = request.form["name"]

    tempFile = request.files["file"]

    # 读取文件扩展名
    extName = tempFile.filename.split(".").pop()

    fileName = "%s_%s.%s"%(userId, name, extName)

    # 生成保存路径
    date = datetime.datetime.now().date()
    pathName = "%s/%s/%s/"%(savePath,request.form["homework"],date)
    if not os.path.exists(pathName):
        os.makedirs(pathName)

    return pathName + fileName

# 检查作业是否存在
def Exists():
    return os.path.exists(GetFullPath())

# 保存作业
def SaveHomework():
    request.files["file"].save(GetFullPath())
