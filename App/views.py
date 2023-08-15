from flask import Blueprint, jsonify, render_template
from .models import *
import uuid

user = Blueprint('user', __name__)


# 返回文本
@user.route('/')
def hello_world():  # put application's code here
    return 'User Main Page'


# 返回页面
# @blue.route("/index/")
def mainPage():
    return render_template("index.html")


# 返回带参数的模板渲染
@user.route("/index/")
def mainPageWithParamters():
    return render_template("index.html", name='张三')


# 返回JSON
@user.route("/return_json/")
def return_json():
    return jsonify({"name": "zhangsan"})


"""
the router parameter support

String 
int 
float 
path 
uuid 
any

"""


@user.route("/getUserName/<string:name>/")
def getUserName(name):
    print(type(name))
    return name


"""
return type must be a string , dict , list 
"""


@user.route("/getUserAge/<int:age>/")
def getUserAge(age):
    print(type(age))
    return str(age)


"""
the digital mush be a float number 、 can not be a integer
"""


@user.route("/getUserMoney/<float:money>/")
def getUserMoney(money):
    print(type(money))
    return str(money)


"""
get user path , this path can include '/'
such as if this request path is     getUserPath/sss/ss
the result will be sss/ss
"""


@user.route("/getUserPath/<path:path>/")
def getUserPath(path):
    print(type(path))
    return str(path)


"""
get uuid
a268fb21-a844-4a00-8070-317fa2ac0b01
"""


@user.route("/getUUID/")
def getUUID():
    return str(uuid.uuid4())


"""
this function must receive a valid uuid
such as 8530ab66-0faa-4769-9061-71e9e669b3a9
"""
@user.route("/sendUUID/<uuid:id>")
def sendUUID(id):
    return str(id)


"""
any
"""
@user.route("/any/<any(apple,orange,banana):id>")
def anyFormat(id):
    return str(id)




"""
request method 
"""
@user.route("/any/<any(apple,orange,banana):id>", methods=['POST'])
def postAnyFormat(id):
    return str(id)
