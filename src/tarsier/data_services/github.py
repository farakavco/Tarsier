
import asyncio
import aiohttp
from urllib.parse import urlencode

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
                url = '%s/repos/%s/commits?%s' % (GITHUB_BASE_URL, repo, urlencode(params))
                print('url', url)
                async with session.get(url, headers={'Authorization': 'token %s' % author.token}) as resp:
                    for result in await resp.json():
                        return Commit(
                            username=result['author']['login'],
                            sha=str(result['sha'])[:8],
                            time=str(result['commit']['author']['date'])[11:19],
                            message=result['commit']['message'],
                            url=result['html_url'],
                            repo=repo
                        )

            return await asyncio.gather(*[fetch(repo, kwargs, a) for repo in self.repositories for a in self.authors])
