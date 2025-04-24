# test_api.py
import pandas as pd
import requests

# Load your CSV
df = pd.read_csv("your_file.csv")  # replace with actual filename

# API endpoint
url = "http://127.0.0.1:8000/classify"

# Send each email to the API
for i, row in df.iterrows():
    payload = {"email_body": row["email"]}
    response = requests.post(url, json=payload)

    print(f"--- Email {i+1} ---")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response.status_code, response.text)
