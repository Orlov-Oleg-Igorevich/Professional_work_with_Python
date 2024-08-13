import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class WorkEmail:

    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    def __init__(self, sender, password) -> None:
        self.sender = sender
        self.password = password

    def send_message(self, subject, recipients, message):

        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.sender, self.password)
        ms.sendmail(self.sender,
        ms, msg.as_string())

        ms.quit()

    def recieve(self, header):

        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.sender, self.password)
        mail.list()
        mail.select("inbox")
        criterion = f'(HEADER Subject "{header if header else 'ALL'}")'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':
    client = WorkEmail('login@gmail.com', 'qwerty')
    client.send_message('Subject', ['vasya@email.com', 'petya@email.com'], 'Message')
    client.recieve(None)
