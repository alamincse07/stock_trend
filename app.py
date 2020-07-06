from flask import Flask,render_template,redirect,request, url_for, jsonify, make_response
from get_stock import get_charts
import matplotlib
import os 


app = Flask(__name__)


@app.route('/',methods=['GET'])
def index(): 
    return render_template('index.html')

@app.route('/',methods=['POST'])
def get_chart(): 
    ticker = request.form.get('ticker')
    get_charts(ticker)
    data = ['static/' + sub for sub in  os.listdir('static')]
    return render_template('chart.html', name = ticker, url =f'static/{ticker}.png', data=data)

if __name__ == '__main__':
    app.run()

