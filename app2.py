import requests
from flask import Flask, render_template, request, jsonify, request, session, redirect, url_for

import jwt
import datetime
import hashlib
from datetime import timedelta
from datetime import datetime

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@Cluster0.vcwg4i3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

SECRET_KEY = 'SPARTA'


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.members.find_one({"id": payload['id']})
        return render_template('search.html', nickname=user_info["nickname"])

    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/nickname')
def nickname():
    token_receive = request.cookies.get('mytoken')
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    user_info = db.members.find_one({"id": payload['id']})
    return render_template('header.html', nickname=user_info["nickname"])


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.members.find_one({'id': username_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/register')
def register():
    return render_template('register.html')


@app.route("/join", methods=["GET"])
def join_get():
    member_list = list(db.members.find({}, {'_id': False}))
    return jsonify({'memberList': member_list})


@app.route("/join", methods=["POST"])
def join_post():
    id_receive = request.form['userId_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.members.insert_one({'nickname': nickname_receive, 'pw': pw_hash, 'id': id_receive})

    return jsonify({'msg': '회원가입이 완료되었습니다!'})


@app.route("/double", methods=["GET"])
def double_get():
    member_list = list(db.members.find({}, {'_id': False}))
    return jsonify({'memberList': member_list})


@app.route('/mise')
def mise():
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    return render_template("search.html", rows=rows)


@app.route("/index")
def result():
    return render_template('index.html')


@app.route("/index/info", methods=["GET"])
def info_get():
    station_info = list(db.stations.find({}, {'_id': False}))
    return jsonify({'station_info': station_info})


@app.route("/index/review", methods=["GET"])
def review_get():
    review_list = list(db.review.find({}, {'_id': False}))
    return jsonify({'reviewList': review_list})


@app.route("/index/review", methods=["POST"])
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

    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/search", methods=["GET"])
def search_get():
    station_list = list(db.stations.find({}, {'_id': False}))
    return jsonify({'stationList': station_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
