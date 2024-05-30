import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load your dataset
data = pd.read_csv('train.csv')  # Adjust the path based on your directory structure

# Print the column names to verify 'SalePrice' is present
print(data.columns)

# Preprocess your data
try:
    X = data.drop('SalePrice', axis=1)
    y = data['SalePrice']
except KeyError as e:
    print(f"Error: {e}. Check if 'SalePrice' column exists in the dataset.")
    exit()

# Handle categorical data
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model to the predictor/model directory
model_path = '../predictor/model/house_price_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")
