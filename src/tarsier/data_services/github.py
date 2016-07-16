
import asyncio
import aiohttp

from tarsier.data_services.base import BaseDataService
from tarsier.config.app_cfg import GITHUB_BASE_URL
from tarsier.model.commit import Commit


class GithubDataService(BaseDataService):
    """Class of github service."""

    def __init__(self, repositories, authors):
        self.repositories = repositories
        self.authors = authors

    async def get_commits(self, **kwargs):

        with aiohttp.ClientSession() as session:

            async def fetch(repo, params, author):
                url = '%s/repos/%s/commits' % (GITHUB_BASE_URL, repo)

                async with session.get(url, params=params, headers={'Authorization': 'token %s' % author.token}) as resp:
                    return [
                        Commit(
                                username=r['author']['login'],
                                sha=str(r['sha'])[:8],
                                time=str(r['commit']['author']['date'])[11:19],
                                message=r['commit']['message'],
                                url=r['html_url'],
                                repo=repo
                        )
                        for r in await resp.json() if r['author']['login'] == author.username]

            return await asyncio.gather(*[fetch(repo, kwargs, a) for a in self.authors for repo in self.repositories])
