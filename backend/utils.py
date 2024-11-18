import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_email_content(prompt, company_name):
    return prompt.replace("{company_name}", company_name)

def send_email(to_email, subject, body):
    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"
    try:
        # Create email
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to SMTP server
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        return "Sent"
    except Exception as e:
        return f"Failed: {str(e)}"
 
