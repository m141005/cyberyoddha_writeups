from flask import Flask, jsonify, session, request
from flask_cookie_decode import CookieDecode

app = Flask(__name__)
app.config.update({'SECRET_KEY': '9c4d697c-36ac-4d00-9076-b9e1e424bb52'})
cookie = CookieDecode()
cookie.init_app(app)

@app.route('/')
def index():
    a = request.args.get('a')
    session['a'] = a
    return jsonify(dict(session))

