#pip install flask numpy pandas scikit-learn

from flask import Flask, render_template, request
import numpy as np
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
app.run(debug=True)