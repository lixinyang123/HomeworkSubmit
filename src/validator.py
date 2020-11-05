from flask import *
import json,io

# 读取学生信息
students = json.loads(io.open("./config/students.json","r").read())

# 验证必须数据
def VerifyRequire():

    tempFile = request.files["file"]

    if request.files["file"].filename == "":
        return False

    if request.form["userId"] == "":
        return False

    if request.form["name"] == "":
        return False

    if request.form["homework"] == "":
        return False

    return True

# 验证用户
def VerifyUser():
    userId = request.form["userId"]
    if len(userId) == 2:
        userId = "0223012006" + userId

    if not userId.startswith("0223012006") or not len(userId) == 12:
        return False
    
    for student in students:
        if student["id"] == userId and student["name"] == request.form["name"]:
            return True

    return False

# 验证文件
def VerifyFile():

    tempFile = request.files["file"]

    # 默认允许压缩文件
    if request.files["file"].filename.endswith(".zip") or request.files["file"].filename.endswith(".rar") or request.files["file"].filename.endswith(".7z"):
        return True

    # 检测上传文件格式是否正确
    if request.form["homework"] == "HTML":
        return request.files["file"].filename.endswith(".html")

    elif request.form["homework"] == "SQL":
        return request.files["file"].filename.endswith(".sql")

    elif request.form["homework"] == "Python":
        return request.files["file"].filename.endswith(".py")

    else:
        return False