import requests
import json

from tarsier.config.app_cfg import base_config


class Author(object):
    """Class of contributors of repositories."""

    def __init__(self, username, email, avatar, github_url, commits):
        self.username = username
        self.email = email
        self.avatar = avatar
        self.github_url = github_url
        self.commits = commits

    @classmethod
    def get_by_repository(self, repo):
        authors = requests.get(
            url='%s/repos/farakavco/%s/contributors' % (base_config.base_url, repo),
            headers={'Authorization': 'token 7806436fae6d41b039b9d9320481e1279c29a2e0'}
        )
        result = json.loads(str(authors.text))
        return result


class Repository(object):
    """Class of repositories."""

    @classmethod
    def get_all(cls, owner):
        repos = requests.get(url='%s/users/%s/repos' % ('http://api.github.com', owner),
                             headers={'Authorization': 'token 7806436fae6d41b039b9d9320481e1279c29a2e0'})
        repos = json.loads(str(repos.text))

        result = [item['name'] for item in repos if not item['fork']]
        return result


class Commit(object):
    """Class of uthors commits."""

    @classmethod
    def get_all(cls, repositories, authors=None, **kwargs):
        result = []

        for repo in repositories:
            repo = repo.split('/')[1]

            # Get authors from by repository if no authors send in input.
            if not authors:
                authors = Author.get_by_repository(repo)

            # Get commits based on repository.
            commits = cls.get_by_repository(repo, **kwargs)

            for author in authors:

                filtered_commits = filter(lambda x: x.username == author['login'], commits)
                filtered_commits = [c for c in filtered_commits]

                if filtered_commits:
                    exist_author = next((aut for aut in result if aut.username == author['login']), None)

                    if not exist_author:
                        author_obj = Author(username=author['login'],
                                            avatar=author['avatar_url'],
                                            email=author['email'] if 'email' in author else '',
                                            github_url=author['html_url'],
                                            commits={})

                        author_obj.commits[repo] = filtered_commits
                        result.append(author_obj)

                    else:
                        exist_author.commits[repo] = filtered_commits

        return result

    @classmethod
    def get_by_repository(cls, repo, **kwargs):
        result = []

        commits = requests.get(
            url=('%s/repos/farakavco/%s/commits?%s') % (base_config.base_url, repo, cls._generate_query_string(**kwargs)),
            headers={'Authorization': 'token 7806436fae6d41b039b9d9320481e1279c29a2e0'}
        )
        commits = json.loads(str(commits.text))

        for commit in commits:
            try:
                commit_obj = Commit()
                commit_obj.__dict__['username'] = commit['author']['login']
                commit_obj.__dict__['sha'] = str(commit['sha'])[:8]
                commit_obj.__dict__['time'] = str(commit['commit']['author']['date'])[11:19]
                commit_obj.__dict__['message'] = commit['commit']['message']
                commit_obj.__dict__['url'] = commit['html_url']
                result.append(commit_obj)
            except:
                continue

        return result

    @staticmethod
    def _generate_query_string(**kwargs):
        query_string = ''
        for k, v in kwargs.items():
            query_string += ('%s=%s&' % (k, v))

        return query_string[:-1] if query_string else ''
