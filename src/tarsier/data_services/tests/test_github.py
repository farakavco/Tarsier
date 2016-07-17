
import asyncio
from datetime import datetime, timedelta

from tarsier.data_services.github import GithubDataService
from tarsier.messaging.daily_report import DailyReport
from tarsier.config import settings


async def main():

    # Define query params of Github api.
    kwargs = {
        'since': datetime.today().strftime(settings.START_DATE_FORMAT),
        'until': (datetime.today() + timedelta(days=1)).strftime(settings.END_DATE_FORMAT)
    }
    # Get all Github commits.
    commits = await GithubDataService(settings.GITHUB_REPOSITORIES, settings.GITHUB_AUTHORS).get_commits(**kwargs)

    author_index = 0
    repo_count = 0
    reports = []
    for repo_commit in commits:
        repo_count += 1
        reports = list(reports) + list(repo_commit)

        if author_index < len(settings.GITHUB_AUTHORS) and repo_count == len(settings.GITHUB_REPOSITORIES):
            daily_report = DailyReport()
            daily_report.smtp_send(
                settings.GITHUB_AUTHORS[author_index].email,
                '%s - %s' % (settings.EMAIL_SUBJECT, settings.EMAIL_DATE),
                {
                    'author': settings.GITHUB_AUTHORS[author_index],
                    'commits': reports,
                    'commits_flag': True if reports else False,
                    'subject': settings.EMAIL_SUBJECT,
                    'date': settings.EMAIL_DATE,
                },
                template_filename='daily_report.mak'
            )

            author_index += 1
            repo_count = 0
            reports = []


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
