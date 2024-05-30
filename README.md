# Django House Price Prediction

## Overview

This Django project implements a simple API for predicting house prices based on a trained machine learning model. The project includes a Django app named `predictor`, which contains the machine learning model and API endpoint for making predictions.

## Features

- **House Price Prediction API**: Provides an API endpoint (`/api/predict/`) to accept POST requests with house features and return predicted prices.
- **Machine Learning Model**: Utilizes a trained machine learning model to make predictions based on input features.
- **SQLite Database**: Uses SQLite as the default database engine for development and testing.

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/ManhCang/house-price-prediction.git

2. **Navigate to the Project Directory**:
   ```sh
   cd house-price-prediction

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt

4. **Run Migrations**:
   ```sh
   python manage.py migrate

5. **Start the Development Server**:
   ```sh
   python manage.py runserver
6. **Test the API**: \
Access the API at http://127.0.0.1:8000/api/predict/ and send POST requests with JSON data to make predictions.

## Usage
- **API Endpoint**: `/api/predict/`
- **Method**: POST
- **Request Body**: JSON object with house features
```json
{
    "LotArea": 8450,
    "OverallQual": 7,
    "YearBuilt": 2003,
    "TotRmsAbvGrd": 8
}
```
- **Response**: JSON object with predicted price
```json
{
    "predicted_price": 124657.15
}
```

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
