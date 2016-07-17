
import asyncio
import aiohttp
import traceback

from tarsier.data_services.base import BaseDataService
from tarsier.config.settings import GITHUB_BASE_URL
from tarsier.model.commit import Commit


class GithubDataService(BaseDataService):
    """Class of github service."""

    def __init__(self, repositories, authors):
        self.repositories = repositories
        self.authors = authors

    async def get_commits(self, **kwargs):

        with aiohttp.ClientSession() as session:

            async def fetch(repo, params, author):
                try:
                    branch_url = '%s/repos/%s/branches' % (GITHUB_BASE_URL, repo)
                    async with session.get(branch_url, headers={'Authorization': 'token %s' % author.token}) as branch_resp:
                        result = set()
                        branches = await branch_resp.json()
                        print('branches', branches)

                        for branch in await branch_resp.json():
                            commit_url = '%s/repos/%s/commits' % (GITHUB_BASE_URL, repo)

                            # Define author and branch_name params for commit API.
                            params['author'] = author.username
                            params['sha'] = branch['name']

                            async with session.get(commit_url, params=params, headers={'Authorization': 'token %s' % author.token}) as commit_resp:

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

            return await asyncio.gather(*[fetch(repo, kwargs, a) for a in self.authors for repo in self.repositories])
