from flask import Flask, render_template, request, flash
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load models
try:
    linear_model = pickle.load(open('/Users/charanamith/Desktop/house-price-prediction/backend/models/linear_model.pkl', 'rb'))
    gb_model = pickle.load(open('/Users/charanamith/Desktop/house-price-prediction/backend/models/gradient_boosting_model.pkl', 'rb'))
    print("Models loaded successfully")
except Exception as e:
    print(f"Error loading models: {e}")

# Conversion rate from USD to INR
usd_to_inr_rate = 84.86

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.form
            features = [
                float(data['sqft_living']),
                int(data['bedrooms']),
                float(data['bathrooms']),
                float(data['floors']),
                float(data['sqft_basement']),
                float(data['sqft_above']),
                int(data['waterfront']),
                float(data['sqft_lot']),
                int(data['zipcode'])
            ]
            features_array = np.array(features).reshape(1, -1)

            prediction = gb_model.predict(features_array)[0]
            prediction_inr = prediction * usd_to_inr_rate
            return render_template('prediction.html', prediction=round(prediction, 2), prediction_inr=round(prediction_inr, 2))
        except Exception as e:
            print(f"Error making prediction: {e}")
            flash('Error making prediction', 'error')
    return render_template('predict_form.html')

if __name__ == '__main__':
    app.run(debug=True)
