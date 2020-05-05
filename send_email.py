import smtplib
from validate_email import validate_email

class Gmail(object):
    def __init__(self, sender, password, receiver):
        sender_valid = self.validate_email(sender)
        receiver_valid = self.validate_email(receiver)
        self.sender = sender
        self.receiver = receiver
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        self.message = """
                This is an e-mail message to be sent in HTML format
                <b>This is HTML message.</b>
                <h1>This is headline.</h1>
            """
        self.subject = "email from server"

    def validate_email(self, email):
        assert(isinstance(email, str)), (
            "Error: Email not a string type'")
        is_valid = validate_email(email, verify = True)
        if(is_valid):
            print(email + " is valid")
            return is_valid
        else:
            print("Incorrect form " + email)
            quit()

    def send_message(self):
        session = self.create_SMTP()
        headers = [
            "From: " + self.sender,
            "Subject: " + self.subject,
            "To: " + self.receiver,
            "MIME-Version: 1.0",
            "Content-Type: text/html"
        ]
        headers = "\r\n".join(headers)
        session.sendmail(self.sender, self.receiver, headers + "\r\n\r\n" + self.message)

    def create_SMTP(self):
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.sender, self.password)
        return session
gm = gmail('sender_email', 'password', 'receiver')
gm.send_message()
