import pickle
from flask import Flask, request
import numpy as np
import pandas as pd


with open('./project/random_forest.pkl', 'rb') as f:
  model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict')
def predict_iris():
  s_length = request.args.get('s_length')
  s_width = request.args.get('s_width')
  p_length = request.args.get('p_length')
  p_width = request.args.get('p_width')
  
  ls = np.array([[s_length, s_width, p_length, p_width]])
  
  prediction = model.predict(ls)
  return str(prediction)


@app.route('/predict_from_df', method = ['POST'])
def predict_iris_df():
  input_data = pd.read_csv(request.files.get('input_file'), header = None)  
  prediction = model.predict(input_data)
  return str(prediction)


if __name__ == '__main__':
  app.run(port=8000)
  

  
#URL: http://127.0.0.1:8000/predict/s_length=10&s_width=2&p_length=8&p_width=10

#URL: http://127.0.0.1:8000/predict_df
