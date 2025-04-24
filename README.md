
# Email Classification and PII Masking API

This project provides an API that processes support emails by masking personally identifiable information (PII), classifying the emails into predefined categories, and then restoring the masked information.

## 🚀 Features
- ✅ Detect and mask sensitive PII and PCI data using regex (non-LLM).
- ✅ Classify emails into categories such as:
  - Billing Issues
  - Technical Support
  - Account Management
- ✅ Restore original information after classification.
- ✅ API built using FastAPI.
- ✅ Docker-ready for Hugging Face Spaces deployment.

## 📁 Project Structure

email-classifier/
├── api.py              # FastAPI app
├── models.py           # Classification model and logic
├── utils.py            # PII masking and demasking utilities
├── requirements.txt    # Python dependencies
├── Dockerfile          # Container configuration for deployment
├── README.md           # Project overview and usage
```

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/email-classifier
cd email-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the API locally
```bash
uvicorn api:app --reload
```

### 4. Test the API
Send a POST request to `/classify` endpoint with an email body:
```http
POST /classify
Content-Type: application/json

{
  "email_body": "Hello, my name is Priya Sharma. My email is priya.sharma@example.com..."
}
```

## 📦 Deployment
To deploy on Hugging Face Spaces:

1. Make sure your repo includes a `Dockerfile`.
2. Push the code to your GitHub.
3. Create a new Space on [Hugging Face Spaces](https://huggingface.co/spaces).
4. Choose Docker SDK and link your GitHub repo.

## 📊 API Response Format
```json
{
  "input_email_body": "Original email string",
  "list_of_masked_entities": [
    {
      "position": [start_index, end_index],
      "classification": "entity_type",
      "entity": "original_value"
    }
  ],
  "masked_email": "Masked email string",
  "category_of_the_email": "Predicted class"
}
```


