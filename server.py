import pandas as pd
from flask import Flask,render_template
import plotly.express as px


app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/projects/')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/test/')
def test():
    df = pd.DataFrame(pd.read_csv('data.csv'))
    fig = px.line(data_frame=df,x='Time', y='Temperature',facet_col='Date')
    file = fig.to_html()
    return render_template('test.html', file = file)
