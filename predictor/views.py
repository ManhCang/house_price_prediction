from django.shortcuts import render

# Create your views here.
import os
import pandas as pd
import pickle
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'model', 'house_price_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@api_view(['POST'])
def predict_price(request):
    data = request.data
    # Extract features from the request data and convert to DataFrame
    features = pd.DataFrame([data])
    # Ensure the order of features matches the training data
    features = features.reindex(columns=model.feature_names_in_, fill_value=0)
    # Make prediction
    prediction = model.predict(features)
    return JsonResponse({'predicted_price': prediction[0]})
