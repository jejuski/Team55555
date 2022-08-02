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
