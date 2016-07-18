
import asyncio
from datetime import datetime, timedelta
from khayyam import JalaliDate

from tarsier.configuration import init_config
from tarsier.data_services.github import GithubDataService
from tarsier.messaging.daily_report import DailyReport
from tarsier.configuration import settings


async def main():

    # Define query params of Github api.
    kwargs = {
        'since': datetime.today().strftime(settings.format.start_date),
        'until': (datetime.today() + timedelta(days=1)).strftime(settings.format.end_date)
    }

    # Get all Github commits.
    commits = await GithubDataService(
        settings.github.repositories,
        settings.github.authors
    ).get_commits(**kwargs)

    author_index = 0
    repo_count = 0
    reports = []
    for repo_commit in commits:
        repo_count += 1
        reports = list(reports) + list(repo_commit)

        if author_index < len(settings.gitgub.authors) and repo_count == len(settings.gitgub.authors):
            daily_report = DailyReport()
            daily_report.smtp_send(
                settings.gitgub.authors[author_index].email,
                '%s - %s' % (settings.email.subject, JalaliDate.today().strftime(settings.format.persian_date)),
                {
                    'author': settings.gitgub.authors[author_index],
                    'commits': reports,
                    'commits_flag': True if reports else False,
                    'subject': settings.email.subject,
                    'date': JalaliDate.today().strftime(settings.format.persian_date),
                },
                template_filename='daily_report.mak'
            )

            author_index += 1
            repo_count = 0
            reports = []


if __name__ == '__main__':
    init_config()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
