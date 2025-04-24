#api.py
from fastapi import FastAPI
from pydantic import BaseModel
from utils import mask_pii, unmask_pii
from models import classify_email
import uuid

app = FastAPI()

class EmailRequest(BaseModel):
    email_body: str

@app.post("/classify")
def classify(request: EmailRequest):
    email_id = str(uuid.uuid4())
    masked_email, entities = mask_pii(request.email_body, email_id)
    category = classify_email(masked_email)
    unmasked_email = unmask_pii(masked_email, email_id)

    return {
        "input_email_body": request.email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
