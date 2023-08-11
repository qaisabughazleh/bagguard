from flask import Flask,request,jsonify
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
app =Flask(__name__)
@app.route('/')
def hello_world():
  return "QAIS"
