
import pickle
from flask import Flask, request
from flasgger import Swagger
import numpy as np
import pandas as pd


with open('./rf.pkl', 'rb') as f:
  model = pickle.load(f)

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict')
def predict_iris():
    '''Example end point returning a prediction
    ---
    parameters:
        - name: s_length
          in: query
          type: number
          required: True   
        - name: s_width
          in: query
          type: number
          required: True   
        - name: p_length
          in: query
          type: number
          required: True    
        - name: p_width
          in: query
          type: number
          required: True
    '''
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')
      
    ls = np.array([[s_length, s_width, p_length, p_width]])
      
    prediction = model.predict(ls)
    return str(prediction)


@app.route('/predict_from_df', methods = ['POST'])
def predict_iris_df():
    '''Example end point returning a prediction
    ---
    parameters:
        - name: input_file
          in: formData
          type:file
          required: True   
    '''
    input_data = pd.read_csv(request.files.get('input_file'), header = None)  
    prediction = model.predict(input_data)
    return str(prediction)


if __name__ == '__main__':
    app.run()
  

  
#URL: localhost:5000/apidocs
