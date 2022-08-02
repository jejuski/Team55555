from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
import hashlib
ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.okw00rk.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

db = client.dbuserinfo


@app.route('/')
def home():
    return render_template('register.html')


@app.route("/join", methods=["GET"])
def join_get():
    member_list = list(db.members.find({}, {'_id': False}))
    return jsonify({'memberList':member_list})


@app.route("/join", methods=["POST"])
def join_post():
    userId_receive = request.form['userId_give']
    pw_receive = request.form['pw_give']
    nickname_receive = request.form['nickname_give']


    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    db.members.insert_one({'nickname':nickname_receive, 'pw':pw_hash, 'userId':userId_receive})

    return jsonify({'msg':'회원가입이 완료되었습니다!'})


@app.route("/double", methods=["GET"])
def double_get():
    member_list = list(db.members.find({}, {'_id': False}))
    return jsonify({'memberList': member_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)