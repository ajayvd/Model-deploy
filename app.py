


#2nd step.....

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle #FOR reading the pickle file ..

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


#home page 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST']) # /predict means it calls the method..
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
  app.run(debug=True)
