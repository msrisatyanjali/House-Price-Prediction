from flask import Flask, request, jsonify
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data['sqft_living'],
        data['bedrooms'],
        data['bathrooms'],
        data['zipcode']
    ]
    prediction = model.predict([features])
    return jsonify({'prediction': round(prediction[0], 2)})

if __name__ == '__main__':
    app.run(debug=True)
