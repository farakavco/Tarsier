
import smtplib
from email.mime.text import MIMEText

from tarsier.messaging.messenger import Messenger
from tarsier.config import app_cfg


class DailyReport(Messenger):
    """
    The class for sending email via smtp server.
    """

    def smtp_send(self, to, subject, body, from_=app_cfg.USERNAME, cc=None, bcc=None, template_string=None, template_filename=None):
        try:
            body = self.render_body(body, template_string, template_filename)

            smtp_server = smtplib.SMTP(
                host=app_cfg.HOST,
                port=app_cfg.PORT
            )
            smtp_server.starttls()
            smtp_server.login(app_cfg.USERNAME, app_cfg.PASSWORD)

            msg = MIMEText(body, 'html')
            msg['Subject'] = subject
            msg['From'] = from_
            msg['To'] = to
            if cc:
                msg['Cc'] = cc
            if bcc:
                msg['Bcc'] = bcc

            smtp_server.send_message(msg)
            smtp_server.close()
            print('Success')

        except Exception as ex:
            print('Error %s:', ex)
