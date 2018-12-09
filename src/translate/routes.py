#从app模块中即从__init__.py中导入创建的app应用
from translate import app
from flask import render_template
#from translate import engtoch
from flask import request
import sys
sys.path.append(r'/Users/shenhua/code/shaniuWeb/src/translate')
import baidu
import json

#建立路由，通过路由可以执行其覆盖的方法，可以多个路由指向同一个方法。
@app.route('/')
@app.route('/index')
def index():
    print(request.values)
    if 'eng2ch_search' in request.values.to_dict() and request.values['eng2ch_search'] != "":
        print("hello world")
        rsp = baidu.engtoch(request.values['eng2ch_search'])
        print(json.loads(rsp)["trans_result"][0]["dst"])
        return render_template("main_afterSearch.html", eng2ch_result = json.loads(rsp)["trans_result"][0]["dst"])
    #user = {'username':'shaniu'}
    if 'ch2eng_search' in request.values.to_dict() and request.values['ch2eng_search'] != "":
        print("hello world")
        rsp = baidu.chtoeng(request.values['ch2eng_search'])
        print(json.loads(rsp)["trans_result"][0]["dst"])
        return render_template("main_afterSearch.html", eng2ch_result = json.loads(rsp)["trans_result"][0]["dst"])
    else:
        return render_template("main.html")