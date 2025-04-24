# models.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import pickle

# Load training data
data = pd.read_csv("emails.csv")  # replace with your actual CSV name

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["email"])
y = data["type"]

model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

def classify_email(text):
    with open("model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
