
# Serverless Email API (Python)

This project is a Serverless REST API built with Python and the Serverless Framework. It allows sending emails using Mailtrap SMTP. This project was created as part of the Python Developer shortlisting task.

# Features
Sends emails via SMTP (Mailtrap).

## Takes JSON input with:

receiver_email

subject

body_text

## Returns proper HTTP response codes:

200 – Email sent successfully.

400 – Missing required parameters.

401 – SMTP Authentication failed.

502 – SMTP error.

500 – Other server errors.

Fully testable locally with serverless-offline.

## Notes

This project meets the shortlisting task requirements:

Rest API with input parameters.

Sends email using SMTP.

Returns appropriate HTTP responses.

Local testing via serverless-offline.## Author

👤 **Author:** Raghu Ram  
🌐 **GitHub:** [raghuram-007](https://github.com/raghuram-007)  



![Author](https://img.shields.io/badge/Author-Raghu%20Ram-blue?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-raghuram--007-black?style=for-the-badge&logo=github&logoColor=white)
# Serverless Email API (Python) 🚀


![Python Version](https://img.shields.io/badge/python-3.9-blue)
![Serverless](https://img.shields.io/badge/Serverless-Framework-orange)
![Status](https://img.shields.io/badge/status-completed-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
# Tech Stack

| Component              | Technology                          |
| ---------------------- | ----------------------------------- |
| Backend Framework      | Django 5.x                          |
| API Framework          | Django REST Framework               |
| Authentication         | JWT (via SimpleJWT)                 |
| Database               | SQLite (default) / MySQL (optional) |                      |
| Testing                | Django TestCase / DRF APITestCase   |

# Tech Stack

Python 3.9

Serverless Framework

SMTP (Mailtrap)

serverless-offline for local testing
## ⚙️ Setup Instructions
## Clone the Repository

git clone https://github.com/raghuram-007/serverless-email-api-mailtrap

cd email-api

## Install Serverless Framework (if not installed)

npm install -g serverless

## 3️⃣ Install Dependencies
pip install -r requirements.txt


## Configuration

Set the following environment variables in serverless.yml (or .env if preferred):

provider:

  environment:
  
    SENDER_EMAIL: "your-email@example.com"
    SMTP_USERNAME: "your-mailtrap-username"
    SMTP_PASSWORD: "your-mailtrap-password"
    SMTP_HOST: "smtp.mailtrap.io"
    SMTP_PORT: 587

# Run Locally

## Start the offline server:
serverless offline
# API ENDPOINT

Your API will be available at:

POST http://localhost:3000/send-email


## Sample Request Body (JSON):

{
  "receiver_email": "test@example.com",
  "subject": "Hello",
  "body_text": "This is a test email."
}
# Project Structure

email-api/

├─ handler.py
            # Lambda function for sending email

├─ serverless.yml        # Serverless configuration

├─ requirements.txt      # Python dependencies

└─ README.md
