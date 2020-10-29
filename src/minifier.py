import os
import cssmin,jsmin

# 压缩静态文件
def Minify():
    directories = [
        "./src/static/js/",
        "./src/static/css/"
    ]

    for directory in directories:
        for staticFile in os.listdir(directory):

            path = directory + staticFile

            if os.path.isfile(path):

                if path.endswith(".js"):
                    newPath = path.replace(".js",".min.js")

                    with open(path) as sourceFile:
                        minified = jsmin.jsmin(sourceFile.read())

                if staticFile.endswith(".css"):
                    newPath = path.replace(".css",".min.css")
                    
                    with open(path) as sourceFile:
                        minified = jsmin.jsmin(sourceFile.read())
                
                with open(newPath,"w+") as miniFile:
                    miniFile.write(minified)
