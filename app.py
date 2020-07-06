from flask import Flask,render_template,redirect,request, url_for, jsonify, make_response
from get_stock import get_charts
import matplotlib
import os 


app = Flask(__name__)


@app.route('/',methods=['GET'])
def index(): 
    return render_template('index.html', data = ['static/' + sub for sub in  os.listdir('static')])

@app.route('/',methods=['POST'])
def get_chart(): 
    ticker = request.form.get('ticker')
    get_charts(ticker)
    data = ['static/' + sub for sub in  os.listdir('static')]
    return render_template('chart.html', name = ticker, url =f'static/{ticker}.png', data=data)

@app.route('/delete',methods=['POST'])
def delete_chart(): 
    ticker = request.form.get('ticker')
   
    SYM = ticker.upper()[7:-4]
    os.remove(f'static/{SYM}.png')
    fileList = glob.glob(f'data/{SYM}*.csv')
    for f in fileList:
        os.remove(f)
    data = ['static/' + sub for sub in  os.listdir('static')]
    return render_template('index.html', name = f'Removed {SYM}' , url =f'static/{ticker}.png', data=data)

if __name__ == '__main__':
    app.run()

