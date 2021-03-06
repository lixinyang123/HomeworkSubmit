import os,json
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
    return render_template('index.html', title = "6班作业提交", content = GetPage("home"))

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

    return render_template('index.html', title = "作业提交", content = "提交成功")

# 未交名单
@app.route("/undo")
def Undo():
    return render_template('index.html', title = "未交名单", content = GetPage("undo"))

@app.route("/undolist")
def UndoList():
    subject = request.args["subject"]
    return json.dumps(manager.GetUndo(subject))

app.run(host="0.0.0.0")
