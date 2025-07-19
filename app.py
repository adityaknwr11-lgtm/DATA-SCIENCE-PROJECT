from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler.pkl")


@app.route('/')
def home():
    return render_template("index.html")

# Route for form submission (HTML frontend)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from HTML form
        input_data = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        input_array = np.array(input_data).reshape(1, -1)
        scaled_input = scaler.transform(input_array)

        prediction = model.predict(scaled_input)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        return render_template("index.html", prediction_text=f"Prediction: {result}")
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

# API route (for Postman or programmatic testing)
@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        input_json = request.json
        input_data = input_json['data']

        input_array = np.array(input_data).reshape(1, -1)
        scaled_input = scaler.transform(input_array)

        prediction = model.predict(scaled_input)
        result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

        return jsonify({'prediction': result})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
