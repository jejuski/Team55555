from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@Cluster0.vcwg4i3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def main():
    r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    response = r.json()
    rows = response['RealtimeCityAir']['row']
    return render_template("test.html", rows=rows)


@app.route('/station', methods=["GET"])
def station():
    station_list = list(db.subway.find({}, {'_id': False}))
    return jsonify({'stations': station_list})


@app.route("/review", methods=["GET"])
def review_get():
    review_list = list(db.review.find({}, {'_id': False}))
    return jsonify({'reviewList': review_list})


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

    return jsonify({'msg': 'POST 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)
