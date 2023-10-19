# Automatic Output Generation

## Sending Emails from Python

Most of us use email for a bunch of different things, all the time. We type up an email message, sometimes attach a picture or a document, and send it to someone in our contact list.

### Introduction to Python Email Library

Email messages look simple in an email client. But behind the scenes the client is doing a lot of work to make that happen! Email messages --even messages with images and attachments -- are actually complicated text structures made entirely of redable strings!

The [Simple Mail Transfer Protocol (SMTP)](https://datatracker.ietf.org/doc/html/rfc2821.html) and [Multipurpose Internet Mail Extension (MIME)](https://datatracker.ietf.org/doc/html/rfc2045) standards define how email messages are constructed. You could read the standards documentation and create email messages all on your own, but you don't need to go to all that trouble. The [email built-in Python module](https://docs.python.org/3/library/email.html) lets us easily construct email messages. 

We'll start by using the ```email.message.EmailMessage class``` to create an empty email message. 

```
>>> from email.message import EmailMessage
>>> message = EmailMessage()
>>> print(message)
```

As usual, printing the message object gives us the string representation of that object. The email library has a function that converts the complex EmailMessage object into something that is fairly human-readable. Since this is an empty message, there isn't anythign to see yet. Let's try adding the sender and recipient to the message and see how that looks. 

We'll define a couple of variables so that we can reuse them later. 

```
>>> sender = "me@example.com"
>>> recipient = "you@example.com"
```

And now, add them to the From and To fields of the message. 

```>>> message['From'] = sender
>>> message['To'] = recipient
>>> print(message)
From: me@example.com
To: you@example.com
```

That's starting to look a bit more like an email message now. How about a subject?

```
>>> message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
>>> print(message)
From: me@example.com
To: you@example.com
Subject: Greetings from me@example.com to you@example.com!
```

**From**, **To**, and **Subject** are examples of **email header fields**. They're **key-value pairs** of labels and instructions used by email clients and servers to route and display the email. They're reparate from the email's **message body**, which is the main content of the message. 

Let's go ahead and add a message body!

```
>>> body = """Hey there!
...
... I'm learning to send emails using Python!"""
>>> message.set_content(body)
```
Alright, now what does that look like? 

```
>>> print(message)
From: me@example.com
To: you@example.com
Subject: Greetings from me@example.com to you@example.com!
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hey there!

I'm learning to send email using Python!
```

The message has a body! the **set_content()** method also automatically added a couple of headers that the email infrastructire will use when sendign this message to another machine.  Remember in an earlier course, when we talked about **character encodings**? The **Content-Type** and **Content-Transfer-Encoding** headers tell email clients and servers how to interpret the bytes in this email message into a string. Now, what about this other header? What is MIME? We'll learn about that next! 

### Adding Attachments

Remember, email messages are made completely of strings. When you add an attachment to an email, whatever type the attachment happens to be, it's encoded as some form of text. The **Multipurpose Internet Mail Extensions (MIME)** standard is used to encode all sorts of files as text strings that can be sent via email. 

In order for the recipient of your message to understand what to do with an attachment, you need to label the attachment with a **MIME type** and **subtype** to tell them what sort of file you're sending. The **Internet Assigned Numbers Authority (IANA) [iano.org](https://www.iana.org/) hosts a registry of valid MIME types**. If you know the correct type and subtype of the files you'll be sending, you can use those values directly. if you don't know, you can use the Python **mimetypes** module to make a good guess!

```
>>> import os.path
>>> attachment_path = "/tmp/example.png"
>>> attachment_filename = os.path.basename(attachment_path)
>>> import mimetypes
>>> mime_type, _ = mimetypes.guess_type(attachment_path)
>>> print(mime_type)
image/png
```
Alright, that mime_type string contains the MIME type and subtype, seperated by a slash. The **EmailMessage** type needs a MIME type and subtypes as separate strings, so let's split this up: 

```>>> mime_type, mime_subtype = mime_type.split('/', 1)
>>> print(mime_type)
image
>>> print(mime_subtype)
png
```
Let's add the attachments to our message and see what it looks like. 

```
with open(attachment_path, 'rb') as ap:
...     message.add_attachment(ap.read(),
...                            maintype=mime_type,
...                            subtype=mime_subtype,
...                            filename=os.path.basename(attachment_path))
... 
>>> print(message)
Content-Type: multipart/mixed; boundary="===============5350123048127315795=="

--===============5350123048127315795==
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit

Hey there!

I'm learning to send email using Python!

--===============5350123048127315795==
Content-Type: image/png
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="example.png"
MIME-Version: 1.0

iVBORw0KGgoAAAANSUhEUgAAASIAAABSCAYAAADw69nDAAAACXBIWXMAAAsTAAALEwEAmpwYAAAg
AElEQVR4nO2dd3wUZf7HP8/M9k2nKIJA4BCUNJKgNJWIBUUgEggCiSgeVhA8jzv05Gc5z4KHiqin
eBZIIBDKIXggKIeCRCAhjQAqx4UiCARSt83uzDy/PzazTDZbwy4BnHde+9qZydNn97Pf5/uUIZRS
(...We deleted a bunch of lines here...)
wgAAAABJRU5ErkJggg==

--===============5350123048127315795==--
```

The entire message can still be serialized as a text string, including the image that we attached! The Email message as a whole has the MIME type "multipart/mixed". Each **part** of the messafe has ot own MIME type. The message body is still there as a "text/plain" part, and the image attachment is a "image/png" part. 

### Sending the Email Through an SMTP Server 

To send emails, our computers use the **Simple Mail Transfer Protocol (SMTP)**. This protocol specifies how computers can deliver email to each other. There are certain steps that need to be followed to do this correctly. But, as usual, we won't do this manually; we'll send the message using the built-in **smtplib Python module**. Let's start by importing the module. 

```
>>> import smtplib
```

With smtplib, we'll create an object that will represent our mail server, and handle sending messages to that server. if you're using a Linux computer, you might already have configured SMTP server like postfix or sendmail. But maybe not. Let's create a smtplib.SMTP object and try to connect to the local machine/ 

```
>>> mail_server = smtplib.SMTP('localhost')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  (...We deleted a bunch of lines here...)
ConnectionRefusedError: [Errno 61] Connection refused
```

This error means that there's no local SMTP server configured. However, you can still connect to the SMTP server for your personal email address. Most personal email services have instructions for sending email through SMTP; just search for the name of your email service and "SMTP connection settings". 

When setting this up, there are a couple of things that you'll probably need to do: Use a secure transport layer and authenticate to the service using a username and password. Let's see what this means in practice. 

You can connect to a remote SMTP server using **Transport Layer Security (TLS)**. An earlier version of the TLS protocol was called **Secure Sockets layer (SSL)**, and you'll sometimes see TLS and SSL: used interchangeably. This SSL/TLS is the same protocol that's used to add a secure transmission layer to HTTP, making it HTTPS. Within the smtplib, there are two classes for making connections to an SMTP server: The **SMTP class** will make a direct SMTP connection, and the **SMTP SSL class** will make a SMTP connection over SSL/TLS like this:

```
>>> mail_server = smtplib.SMTP_SSL('smtp.example.com')
```

If you want to see the SMTP messages that are being setn back and forth by the smtplib module behind that scenes, you can set the debug level of the SMTP or SMTP_SSL object. 

```
mail_server.set_debuglevel(1)
```

Now that we've made a connection to the SMTP server, the next thing we need to do is authenticate to the SMTP server. Typically, email providers wants us to provide a username and password to connect. Let's put the password into a varaible so its's not visible on the screen. 

```
>>> import getpass
>>> mail_pass = getpass.getpass('Password? ')
Password?
>>>
```
The example above uses the **getpass module** so that passers-by won't see the password on the screen. Watch out though; the **mail_pass** variable is still just an ordinary string!

```
>>> print(mail_pass)
It'sASecr3t!
```

Now that we have the email user and password configured, we can authenticate to the email server using the SMTP object's **login method**.

```
>>> mail_server.login(sender, mail_pass)
(235, b'2.7.0 Accepted')
```

if the login attempt succeeds, the login method will return a tuple of the **SMTP status code** and a message explaining the reason for the status. If the login attempts fails, the module will raise a **SMTPAuthenticationError** exception. 

If you wrote a script to send an email message, how would you handle this exception?

We're connected and authenticated to the SMTP server. Now, how do we send the message?

```
>>> mail_server.send_message(message)
{}
```
Okay, well that last bit was pretty easy! We did the hard part first! the **send message method** returns a dictionary of any recipients that weren't able to receieve the message. Out message was delivered successfully, so send_message returned an empty dictionary. Finally, now that the email is sent, let's close the connection to the mail server. 

```
>>> mail_server.quit()
```

