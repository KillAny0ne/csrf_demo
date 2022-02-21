from flask import Flask
from flask import request,make_response
import os
import base64


password = base64.b64encode(os.urandom(16))
name = 'Alice'
app = Flask(__name__)


@app.route("/")
def index():
    if(request.cookies.get("password")!=password.decode()):
        return "Login First!"
    else:
        return "Your name is "+name+" !"


@app.route("/login")
def login():
    if(request.args.get("password")=='123456'):
        resp = make_response("Login success!")
        resp.set_cookie("password",password)
        return resp
    else:
        return "password error!"


@app.route("/change_name")
def hello():
    global name
    if request.headers.get('Referer'):
        if(request.headers.get('Referer')!='http://192.168.17.134:5565'):
            name += '\nYou are Just Attacked by someone!Please check it!'
            return "No CSRF Attack !"
    else:
        print('No ref')
    if not request.args.get("name"):
        return 'Whats your name?'
    if(request.cookies.get("password")!=password.decode()):
        return "No Login No change! Stupid "+request.args.get("name")+" !"
    name = request.args.get("name")
    return "Change name success!"



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5565)
