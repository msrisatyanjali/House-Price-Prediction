import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import os

try:
    # Load dataset
    data_path = '/Users/charanamith/Downloads/kc_house_data.csv'  # Update this path if needed
    data = pd.read_csv(data_path)

    # Features and target
    features = ['sqft_living', 'bedrooms', 'bathrooms', 'floors', 'sqft_basement', 'sqft_above', 'waterfront', 'sqft_lot', 'zipcode']
    target = 'price'

    X = data[features]
    y = data[target]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Linear Regression Model
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    # Train Gradient Boosting Model
    gb_model = GradientBoostingRegressor()
    gb_model.fit(X_train, y_train)

    # Ensure the directory exists for saving models
    model_save_path = '/Users/charanamith/Desktop/house-price-prediction/backend/models/'
    os.makedirs(model_save_path, exist_ok=True)

    # Save models using pickle
    pickle.dump(linear_model, open(f'{model_save_path}linear_model.pkl', 'wb'))
    pickle.dump(gb_model, open(f'{model_save_path}gradient_boosting_model.pkl', 'wb'))

    print("Models saved successfully!")

except FileNotFoundError as e:
    print(f"Error: {e}. Please ensure the data path is correct.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
