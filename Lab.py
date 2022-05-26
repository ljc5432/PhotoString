# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:42:51 2019

@author: Administrator
"""

from flask import Flask

from api_bp import api_bp
from search_bp import search_bp
from show_bp import show_bp
from upload_bp import upload_bp

app = Flask(__name__)

app.register_blueprint(upload_bp)
app.register_blueprint(show_bp)
app.register_blueprint(search_bp)
app.register_blueprint(api_bp)


@app.route("/")
def start():
    return '''
<h2>This is the beginning</h2>
<a href="/show">展示</a><br>
<a href="/search">搜索</a><br>
<a href="/upload">上传</a><br>
<a href="/api/json">api 接口</a><br>
'''


if __name__ == '__main__':
    app.run(debug=True)
