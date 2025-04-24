# utils.py
import re
import os
import json

storage_path = "masked_data_storage"
os.makedirs(storage_path, exist_ok=True)

patterns = {
    "full_name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
    "email": r"[\w\.-]+@[\w\.-]+",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",
    "credit_debit_no": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "aadhar_num": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
     
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b\d{2}/\d{2}\b"
}

def mask_pii(text, email_id):
    entities = []
    original = text
    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entity_value = match.group()
            start, end = match.span()
            masked_text = f"[{label}]"
            text = text[:start] + masked_text + text[end:]
            # Offset all future spans due to change in length
            entities.append({
                "position": [start, start + len(masked_text)],
                "classification": label,
                "entity": entity_value
            })
    with open(f"{storage_path}/{email_id}.json", "w") as f:
        json.dump(entities, f)
    return text, entities

def unmask_pii(masked_text, email_id):
    try:
        with open(f"{storage_path}/{email_id}.json", "r") as f:
            entities = json.load(f)
        for entity in entities:
            classification = entity["classification"]
            placeholder = f"[{classification}]"
            masked_text = masked_text.replace(placeholder, entity["entity"], 1)
        return masked_text
    except FileNotFoundError:
        return masked_text