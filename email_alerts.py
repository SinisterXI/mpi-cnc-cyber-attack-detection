import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def send_email_sendgrid(subject, body, to_email):
    # Replace 'your_sendgrid_api_key' with the actual API key from SendGrid
    sg = sendgrid.SendGridAPIClient(api_key="your_sendgrid_api_key")
    
    # Replace 'your_email@example.com' with your sender email address
    from_email = Email("shameerawais16@gmail.com")  # Your sender email
    to_email = To(to_email)  # Recipient email
    content = Content("text/plain", body)  # Email body content
    
    # Create the email
    mail = Mail(from_email, to_email, subject, content)
    
    try:
        # Send the email
        response = sg.send(mail)
        print(f"Email sent successfully. Status code: {response.status_code}")
        print(f"Response body: {response.body}")
        return response.status_code
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
        return None

# Example usage
send_email_sendgrid("Test Subject", "This is a test email body.", "recipient_email@example.com")

