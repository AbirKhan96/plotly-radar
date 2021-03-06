from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

app = Flask(__name__)


@app.route('/')
def index():
    # by default august
    feature = 'August' 
    
    scatter_polar = create_plot(feature)
    
    return render_template('index.html', plot=scatter_polar)

def create_plot(feature):
    if feature == 'August':
       
      
        data =  [go.Scatterpolar( r = [9, 0, 3.76, 27.71, 14.72],  theta = ["svrly_stntd", "svr_wstg", "wasting_percent", "stunting_percent", "underweight_percent"],  mode = 'markers',)]
       
    elif feature == 'September':
       
        data =  [go.Scatterpolar( r = [115,1,3.29,24.28,12.69],  theta = ["svrly_stntd", "svr_wstg", "wasting_percent", "stunting_percent", "underweight_percent"],  mode = 'markers',)]
        
    else:
       
        data =  [go.Scatterpolar( r = [692,27,3.01,24.33,11.32],  theta = ["svrly_stntd", "svr_wstg", "wasting_percent", "stunting_percent", "underweight_percent"],  mode = 'markers',)]
        

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/scatter_polar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    
    graphJSON = create_plot(feature)
  
    return graphJSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug= True)