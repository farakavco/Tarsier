
import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from tarsier.model.github import Commit
from tarsier.config.local_cnf import host, port, username, password


DEFAULT_DATE_FORMAT = '%Y-%m-%dT00:00:00'


class ScheduledReport(object):
    """Scheduled report """

    @classmethod
    def daily_commits(cls, authors=None, repositories=None):
        # Get today date.
        date = datetime.today()

        # Define query params of Github api.
        kwargs = {
            'since': date.strftime(DEFAULT_DATE_FORMAT),
            'until': (date + timedelta(days=1)).strftime(DEFAULT_DATE_FORMAT)
        }

        if not repositories:
            # Define repositories list.
            repositories = [
                'farakavco/Tarsier', 'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
            ]

        if not authors:
            # Define authors list.
            authors = [
                dict(
                    login='pylover',
                    email='vahid.mardani@gmail.com',
                    avatar_url='https://avatars.githubusercontent.com/u/1302253?v=3',
                    html_url='https://github.com/pylover'
                ),
                dict(
                    login='Sharez',
                    email='shahabrezaee@gmail.com',
                    avatar_url='https://avatars.githubusercontent.com/u/328063?v=3',
                    html_url='https://github.com/Sharez'
                ),
                dict(
                    login='aida-mirabadi',
                    email='aida.mirabadi@gmail.com',
                    avatar_url='https://avatars.githubusercontent.com/u/7857775?v=3',
                    html_url='https://api.github.com/users/aida-mirabadi'
                ),
            ]

        commits = Commit.get_all(repositories, authors, **kwargs)
        cls.create_email_content(commits)

    @classmethod
    def create_email_content(cls, authors):
        for author in authors:
            message = '<p style="font-size:14px"><b>Today:<b></p>'
            if author.commits:
                for repo, commit in author.commits.items():
                    if commit:
                        message += '<span style="font-size:14px">[%s]: </span>' % repo
                        message += '<ul>'
                        for v in commit:
                            message += '<li style="font-size:12px">%s</li>' % v.message
                        message += '</ul>'
                if author.has_commit is False:
                    message += '<p>You have no commit today.</p>'
            message += """
            <p style="font-size:14px">
                <b>Tomorrow:<b>
            </p>
            <br>
            <p style="font-size:14px">
                <b>Blocking:<b>
            </p>
            <br>"""

            cls.send_mail(recipient=author.email, message=message)

    @classmethod
    def send_mail(cls, recipient, message):
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Daily report - %s' % datetime.today().strftime('%Y-%m-%d')

            message = MIMEText(message, 'html')
            msg.attach(message)

            server = smtplib.SMTP(host, port)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(username, [recipient], msg.as_string())
            server.close()
            print("success")
        except:
            print("failed")


if __name__ == '__main__':
    ScheduledReport.daily_commits()
