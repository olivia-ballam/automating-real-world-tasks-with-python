#! /usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
    """Creates an email with attachment."""

    # Basic Email formating. 
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path is not None:
        # Process the attachment and add to the Email.  
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(), 
                                   maintype = mime_type,
                                   subtype = mime_subtype, 
                                   filename = attachment_filename)

    return message

def send(message): 
    """Sends Email message to the configured SMTP server."""

    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == "__main__":
    
    # Parameters for generate_email() function.  
    sender = ""
    recipient = ""
    subject = ""
    body = ""
    attachment_path = ""
    
    # Generate email message. 
    message = generate(sender, recipient, subject, body, attachment_path)
    
    try:
        # Send email message. 
        send(message)
    except Exception as e:
        print(f"Error: {e} an error occurred")

    


