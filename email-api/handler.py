import json
import smtplib
from email.mime.text import MIMEText
import os

def send_email(event, context):
    """
    Lambda function to send emails via Mailtrap SMTP.
    Expects JSON body with:
        - receiver_email
        - subject
        - body_text
    Uses environment variables for sensitive SMTP credentials.
    """

    try:
        # Parse request body
        body = json.loads(event.get('body', '{}'))
        receiver = body.get('receiver_email')
        subject = body.get('subject')
        message_text = body.get('body_text')

        # Validate input
        if not receiver or not subject or not message_text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'receiver_email, subject, and body_text are required.'})
            }

        # Mailtrap SMTP configuration from environment variables
        smtp_host = os.environ.get('SMTP_HOST', 'smtp.mailtrap.io')
        smtp_port = int(os.environ.get('SMTP_PORT', 587))
        sender_email = os.environ['SENDER_EMAIL']
        smtp_username = os.environ['SMTP_USERNAME']
        smtp_password = os.environ['SMTP_PASSWORD']

        # Create the email message
        msg = MIMEText(message_text)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver

        # Send the email with timeout
        with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver, msg.as_string())

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent successfully!'})
        }

    except KeyError as ke:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Missing environment variable: {ke}'})
        }

    except smtplib.SMTPAuthenticationError:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'SMTP Authentication failed. Check credentials.'})
        }

    except smtplib.SMTPException as e:
        return {
            'statusCode': 502,
            'body': json.dumps({'error': f'SMTP error: {str(e)}'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
