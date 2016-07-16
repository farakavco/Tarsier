
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tarsier.config.local_cfg import HOST, PORT, USERNAME, PASSWORD


DEFAULT_DATE_FORMAT = '%Y-%m-%dT00:00:00'


class ScheduledReport(object):
    """Scheduled report """
    def __init__(self, authors, commits):
        self.authors = authors
        self.commits = commits

    def send_email(self):
        for c in self.commits:
            print('c', c.username, c.message)

        for author in self.authors:
            message = '<p style="font-size:14px"><b>Today:<b></p>'
            for commit in self.commits:
                if commit.username == author.username:
                    message += '<span style="font-size:14px">[%s]: </span>' % commit.repo
                    message += '<ul>'
                    message += '<li style="font-size:12px">%s</li>' % commit.message
                    message += '</ul>'
            message += """
            <p style="font-size:14px">
                <b>Tomorrow:<b>
            </p>
            <br>
            <p style="font-size:14px">
                <b>Blocking:<b>
            </p>
            <br>"""

            self.config_email(recipient=author.email, message=message)

    @staticmethod
    def config_email(recipient, message):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Daily report - %s' % datetime.today().strftime('%Y-%m-%d')

            message = MIMEText(message, 'html')
            msg.attach(message)

            server = smtplib.SMTP(HOST, PORT)
            server.ehlo()
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, [recipient], msg.as_string())
            server.close()
            print("success")
        except:
            print("failed")
