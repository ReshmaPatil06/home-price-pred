#from flask import Flask, request, jsonify
#import joblib
#import numpy as np

#app = Flask(__name__)
#model = joblib.load('models/model.pkl')

#@app.route('/')
#def home():
 #   return "Home Price Prediction API is Running"

#@app.route('/predict', methods=['POST'])
#def predict():
 #   data = request.get_json(force=True)
  #  area = data['area']
   # prediction = model.predict(np.array([[area]]))
    #return jsonify({'predicted_price': prediction[0]})

#if __name__ == '__main__':
#    app.run(host='127.0.0.1', port=5001, debug=True)
#2from flask import Flask, request, jsonify, render_template
#import joblib

#app = Flask(__name__)
#model = joblib.load("models/model.pkl")

#@app.route('/')
#def home():
 #   return render_template('index.html')

#@app.route('/predict', methods=['POST'])
#def predict():
 #   try:
  #      area = float(request.form['area'])  # from HTML form
   # except:
    #    return render_template('index.html', prediction="Invalid input")

    #prediction = model.predict([[area]])[0]
    #return render_template('index.html', prediction=round(prediction, 2))

#if __name__ == '__main__':
 #   app.run(host='127.0.0.1', port=5001, debug=True)    

 from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('models/model.pkl')  # Make sure this path is correct
history = []


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html',Prediction=None, history=history)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])  # Get the input from form
        prediction = model.predict([[area]])[0]  # Predict using the model
        history.append({'area' : area, 'prediction': prediction})
        return render_template('index.html', prediction=prediction, history=history)  # Show result
    except:
        return render_template('index.html', prediction=None, history=history)

#if __name__ == '__main__':
 #   app.run(host='127.0.0.1', port=5001, debug=True)