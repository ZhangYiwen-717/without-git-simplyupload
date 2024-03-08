# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:22:58 2024

@author: Eeven
"""

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__=="__main__":
    app.run()
    