
import asyncio
from datetime import datetime, timedelta

from tarsier.model.author import Author
from tarsier.data_services.github import GithubDataService
from tarsier.messaging.daily_report import DailyReport
from tarsier.config import app_cfg


async def main():

    # Define query params of Github api.
    kwargs = {
        'since': '2016-01-01',
        # 'until': (datetime.today() + timedelta(days=1)).strftime(app_cfg.END_DATE_FORMAT)
    }
    # kwargs = {
    #     'since': datetime.today().strftime(app_cfg.START_DATE_FORMAT),
    #     'until': (datetime.today() + timedelta(days=1)).strftime(app_cfg.END_DATE_FORMAT)
    # }

    # Define repositories list.
    repositories = [
        'farakavco/Tarsier', 'farakavco/kakapo',
        'farakavco/blueprint',
        # 'farakavco/lutino', 'farakavco/tutorials'
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
            email='shahabrezaee@gmail.com',
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

    author_index = 0
    repo_count = 0
    reports = []

    for repo_commit in commits:
        repo_count += 1
        reports = reports + repo_commit

        if author_index < len(authors) and repo_count == len(repositories):

            daily_report = DailyReport()
            daily_report.smtp_send(
                authors[author_index].email,
                app_cfg.EMAIL_SUBJECT,
                {
                    'author': authors[author_index],
                    'commits': reports,
                    'commits_flag': True if reports else False,
                    'title': app_cfg.EMAIL_SUBJECT,
                },
                template_filename='daily_report.mak'
            )

            author_index += 1
            repo_count = 0
            reports = []


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
