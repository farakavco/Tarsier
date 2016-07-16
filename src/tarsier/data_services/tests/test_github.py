
import asyncio

from tarsier.model.author import Author
from tarsier.data_services.github import GithubDataService
from tarsier.controller.report import ScheduledReport


async def main():

    # Define query params of Github api.
    kwargs = {
        'since': '2016-01-01',
    }

    # Define repositories list.
    repositories = [
        'farakavco/Tarsier', 'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
    ]

    # Define authors list.
    authors = [
        # Author(
        #     username='pylover',
        #     email='vahid.mardani@gmail.com',
        #     avatar_url='https://avatars.githubusercontent.com/u/1302253?v=3',
        #     html_url='https://github.com/pylover',
        #     token='7806436fae6d41b039b9d9320481e1279c29a2e0'
        # ),
        # Author(
        #     username='Sharez',
        #     email='shahabrezaee@gmail.com',
        #     avatar_url='https://avatars.githubusercontent.com/u/328063?v=3',
        #     html_url='https://github.com/Sharez',
        #     token='7806436fae6d41b039b9d9320481e1279c29a2e0'
        # ),
        Author(
            username='aida-mirabadi',
            email='aida.mirabadi@gmail.com',
            avatar_url='https://avatars.githubusercontent.com/u/7857775?v=3',
            html_url='https://api.github.com/users/aida-mirabadi',
            token='7806436fae6d41b039b9d9320481e1279c29a2e0'
        ),
    ]

    commits = await GithubDataService(repositories, authors).get_commits(**kwargs)
    ScheduledReport(authors, commits).send_email()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
