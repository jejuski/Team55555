import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@Cluster0.vcwg4i3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    return render_template("search.html", rows=rows)


@app.route("/search", methods=["GET"])
def search_get():
    station_list = list(db.subway.find({}, {'_id': False}))
    return jsonify({'stations': station_list})


@app.route("/index")
def result():
    return render_template('index.html')


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

    return jsonify({'msg': '등록 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
