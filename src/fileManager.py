from flask import *
import os,datetime

savePath = "./Homeworks"

# 创建默认存储路径
if not os.path.exists(savePath):
    os.mkdir(savePath)

# 保存作业
def SaveHomeWork():

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

    tempFile.save(pathName + fileName)
