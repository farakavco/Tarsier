
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

    gitgub_service = GithubDataService(
        settings.github.repositories,
        settings.github.authors
    )

    # Get all Github commits and authors by detail based on query params.
    commits = await gitgub_service.get_commits(**kwargs)
    authors = await gitgub_service.get_authors_fully(**kwargs)

    report = []
    # Prepare result for sending report email.
    for index, repo_commits in enumerate(commits):
        author_index = index // len(settings.github.repositories)
        report += list(repo_commits)

        if not (index + 1) % len(settings.github.repositories):
            daily_report = DailyReport()
            daily_report.smtp_send(
                authors[author_index].email,
                '%s - %s' % (settings.email.subject, JalaliDate.today().strftime(settings.format.persian_date)),
                {
                    'author': authors[author_index],
                    'commits': report,
                    'commits_flag': True if report else False,
                    'subject': settings.email.subject,
                    'date': JalaliDate.today().strftime(settings.format.persian_date),
                },
                template_filename='daily_report.mak'
            )
            report = []


if __name__ == '__main__':
    init_config()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
