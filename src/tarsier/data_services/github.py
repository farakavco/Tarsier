
import asyncio
import aiohttp
import traceback

from tarsier.data_services.base import BaseDataService
from tarsier.configuration import settings
from tarsier.model.commit import Commit
from tarsier.model.author import Author


class GithubDataService(BaseDataService):
    """Class of github service."""

    def __init__(self, repositories, authors):
        self.repositories = repositories
        self.authors = authors

    async def get_commits(self, **kwargs):

        with aiohttp.ClientSession() as session:

            async def fetch(repo, params, author):
                try:
                    branch_url = '%s/repos/%s/branches' % (settings.github.base_url, repo)

                    async with session.get(
                            branch_url,
                            headers={'Authorization': 'token %s' % settings.github.token}
                    ) as branch_resp:
                        result = set()

                        for branch in await branch_resp.json():
                            commit_url = '%s/repos/%s/commits' % (settings.github.base_url, repo)

                            # Extra params for commit API as author and branch_name.
                            params['author'] = author[0]  # author username
                            params['sha'] = branch['name']

                            async with session.get(
                                    commit_url,
                                    params=params,
                                    headers={'Authorization': 'token %s' % settings.github.token}
                            ) as commit_resp:
                                for commit in await commit_resp.json():
                                    result.add(
                                        Commit(
                                            username=commit['author']['login'],
                                            sha=commit['sha'],
                                            time=str(commit['commit']['author']['date'])[11:19],
                                            message=commit['commit']['message'],
                                            url=commit['html_url'],
                                            repo=repo.split('/')[1],
                                        )
                                    )
                        return result

                except Exception as ex:
                    traceback.print_exc(ex)

            return await asyncio.gather(
                *[fetch(repo, kwargs, a) for a in self.authors for repo in self.repositories]
            )

    async def get_authors_fully(self, **kwargs):

        with aiohttp.ClientSession() as session:

            async def fetch(author, params):
                try:
                    author_url = '%s/users/%s' % (settings.github.base_url, author[0])

                    async with session.get(
                            author_url,
                            params=params,
                            headers={'Authorization': 'token %s' % settings.github.token}
                    ) as author_resp:
                        aa = await author_resp.json()
                        return (
                            Author(
                                username=author[0],
                                email=author[1],
                                avatar_url=aa['avatar_url'],
                                html_url=aa['html_url']
                            )
                        )

                except Exception as ex:
                    traceback.print_exc(ex)

            return await asyncio.gather(
                *[fetch(a, kwargs) for a in self.authors]
            )
