from flask import  Flask
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def home():

    return("hello world")
app.run(port=8081)
