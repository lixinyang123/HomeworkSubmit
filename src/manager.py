from flask import *
import os,datetime,io,json,sys,zipfile

savePath = sys.argv[1] + "/Homework"
folderName = sys.argv[2]

# 创建默认存储路径
if not os.path.exists(savePath):
    try:
        os.mkdir(savePath)
    except:
        raise Exception("无法创建输入的目录")

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
    pathName = "%s/%s/%s/"%(savePath,request.form["homework"],folderName)
    if not os.path.exists(pathName):
        os.makedirs(pathName)

    return pathName + fileName

# 检查作业是否存在
def Exists():
    return os.path.exists(GetFullPath())

# 保存作业
def SaveHomework():
    request.files["file"].save(GetFullPath())

# 打包作业
def PackHomework():
    packer = zipfile.ZipFile("Homework.zip","w",zipfile.ZIP_DEFLATED)
    packer.write(packer)
    packer.close()

# 读取所有作业
def GetAllFiles(homeworkPath):
    for path in os.listdir(homeworkPath):
        fileName = homeworkPath + "/" + path
        if os.path.isfile(fileName):
            print(fileName)
        else:
            GetAllFiles(fileName)
