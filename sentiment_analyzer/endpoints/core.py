import pandas as pd
import joblib
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


classifier = joblib.load('lr_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
   
def predict_sentiment(text):
    text_transformed = vectorizer.transform([text])
    prediction = classifier.predict(text_transformed)
    return prediction[0]

def analyse_text(body):

    text = body.get("text")
    result = predict_sentiment(text)
    return jsonify({"status": 1, "sentiment": result})