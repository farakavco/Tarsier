import smtplib
import datetime

from practice.model.github import Commit


class ScheduledReport(object):

    @classmethod
    def daily_commits(cls, authors=None, repositories=None):
        # Get today date.
        date = datetime.datetime.now()
        kwargs = {'since': str(date), 'until': str(date + datetime.timedelta(days=1))}

        if not repositories:
            # Define repositories list.
            repositories = [
                'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
            ]

        if not authors:
            # Define authors list.
            authors = [
                {'login': 'Sharez',
                 'email': 'shahabrezaee@gmail.com',
                 'avatar_url': 'https://avatars.githubusercontent.com/u/328063?v=3',
                 'html_url': 'https://github.com/Sharez'},
                {'login': 'pylover',
                 'email': 'vahid.mardani@gmail.com',
                 'avatar_url': 'https://avatars.githubusercontent.com/u/1302253?v=3',
                 'html_url': 'https://github.com/pylover'},
            ]

        commits = Commit.get_all(repositories, authors, **kwargs)
        cls.create_email_content(commits)

    @classmethod
    def create_email_content(cls, result):

        for author in result:
            message = ''
            print('username', author.username)
            for repo, val in author.commits.items():
                message += '<p>repository: %s <br></p>' % repo
                for v in val:
                    message += '<p>%s</p>' % v.message

            cls.send_mail(recipient=author.email, message=message)

    @classmethod
    def send_mail(cls, recipient, message, username='falcon.farakav@gmail.com', password='himopolooK90', subject='Report'):

        print('message', message, recipient)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
           """ % (username, ", ".join([recipient]), subject, message)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(username, [recipient], message)
            server.close()
            print("success")
        except:
            print("failed")


if __name__ == '__main__':
    ScheduledReport.daily_commits()
