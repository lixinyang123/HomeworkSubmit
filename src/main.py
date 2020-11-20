import os
from flask import *
import validator,manager,minifier

minifier.Minify()

app = Flask(__name__)

def GetPage(name):
    path = "./src/static/view/" + name + ".html"
    with open(path,encoding="utf-8") as sourceFile:
        return sourceFile.read()

# 主页
@app.route("/")
def Index():
    return render_template('index.html', content = GetPage("home"))

# 提交作业
@app.route("/submit", methods=["post"])
def Submit():

    if not validator.VerifyRequire():
        return render_template('index.html', content = "请完善数据")
    
    if not validator.VerifyUser():
        return render_template('index.html', content = "用户错误")
    
    if not validator.VerifyFile():
        return render_template('index.html', content = "提交文件格式错误")

    manager.SaveHomework()

    return render_template('index.html', content = "上传成功")

# 下载作业
@app.route("/download")
def Download():
    manager.PackHomework()
    response = make_response(send_file("./Homework.zip"))
    response.headers["Content-Disposition"] = "attachment; filename={};".format("./Homework.zip")
    return response

app.run(host="0.0.0.0")
