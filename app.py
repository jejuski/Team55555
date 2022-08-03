<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST 연결 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
=======
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def main():
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    return render_template("main.html", rows=rows)


@app.route('/gangnam')
def gangnam():
    return render_template("info_gangnam.html")


@app.route('/yeoksam')
def yeoksam():
    return render_template("info_yeoksam.html")


@app.route('/seolleung')
def seolleung():
    return render_template("info_seolleung.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)
>>>>>>> 715419ec94df37b9144394502534e13660361aa6

from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where();

client = MongoClient('mongodb+srv://test:sparta@cluster0.vxtovxz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

import jwt

import datetime

import hashlib


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"id": payload['id']})
        return render_template('index.html', nickname=user_info["nick"])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def api_register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.user.insert_one({'id': id_receive, 'pw': pw_hash, 'nick': nickname_receive})

    return jsonify({'result': 'success'})

---------------------------------------login-------------------------------------------------

@app.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.user.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@app.route('/api/nick', methods=['GET'])
def api_valid():
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        print(payload)

        userinfo = db.user.find_one({'id': payload['id']}, {'_id': 0})
        return jsonify({'result': 'success', 'nickname': userinfo['nick']})
    except jwt.ExpiredSignatureError:
        return jsonify({'result': 'fail', 'msg': '로그인 시간이 만료되었습니다.'})
    except jwt.exceptions.DecodeError:
        return jsonify({'result': 'fail', 'msg': '로그인 정보가 존재하지 않습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    ------------------------------------------상세페이지------------------------------------------------------
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb://test:sparta@cluster0-shard-00-00.hxcfk.mongodb.net:27017,cluster0-shard-00-01.hxcfk.mongodb.net:27017,cluster0-shard-00-02.hxcfk.mongodb.net:27017/?ssl=true&replicaSet=atlas-atkn0l-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/review", methods=["GET"])
def review_get():
    review_list = list(db.review.find({}, {'_id': False}))
    return jsonify({'reviewList':review_list})
@app.route("/review", methods=["POST"])
def review_post():
    nickname_receive = request.form['nickname_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']
    doc = {
        'nickname': nickname_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.review.insert_one(doc)
    return jsonify({'msg':'POST 연결 완료!'})
if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)