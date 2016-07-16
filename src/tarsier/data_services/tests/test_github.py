
import asyncio
from datetime import datetime, timedelta

from tarsier.model.author import Author
from tarsier.data_services.github import GithubDataService
from tarsier.messaging.daily_report import DailyReport
from tarsier.config import app_cfg


async def main():

    # Define query params of Github api.
    kwargs = {
        'since': datetime.today().strftime(app_cfg.START_DATE_FORMAT),
        'until': (datetime.today() + timedelta(days=1)).strftime(app_cfg.END_DATE_FORMAT)
    }

    # Define repositories list.
    repositories = [
        'farakavco/Tarsier', 'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
    ]

    # Define authors list.
    authors = [
        Author(
            username='pylover',
            email='vahid.mardani@gmail.com',
            avatar_url='https://avatars.githubusercontent.com/u/1302253?v=3',
            html_url='https://github.com/pylover',
            token=''
        ),
        Author(
            username='Sharez',
            email='aida.mirabadi@gmail.com',
            avatar_url='https://avatars.githubusercontent.com/u/328063?v=3',
            html_url='https://github.com/Sharez',
            token=''
        ),
        Author(
            username='aida-mirabadi',
            email='aida.mirabadi@gmail.com',
            avatar_url='https://avatars.githubusercontent.com/u/7857775?v=3',
            html_url='https://api.github.com/users/aida-mirabadi',
            token=''
        )
    ]

    commits = await GithubDataService(repositories, authors).get_commits(**kwargs)

    for index, commit in enumerate(commits):
        daily_report = DailyReport()
        daily_report.smtp_send(
            authors[index].email,
            app_cfg.EMAIL_SUBJECT,
            {
                'author': authors[index],
                'commits': commit,
                'title': app_cfg.EMAIL_SUBJECT,
            },
            template_filename='daily_report.mak'
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
