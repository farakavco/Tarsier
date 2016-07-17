from datetime import datetime

from tarsier.model.author import Author


# Date configs.
START_DATE_FORMAT = '%Y-%m-%dT00:00:00Z'
END_DATE_FORMAT = '%Y-%m-%dT23:59:59Z'

# SMTP configs.
HOST = 'smtp.gmail.com'
PORT = 587
USERNAME = 'falcon.farakav@gmail.com'
PASSWORD = 'himopolooK90'
EMAIL_SUBJECT = "Daily report - %s " % datetime.today().strftime('%Y-%m-%d')

# Github base url.
GITHUB_BASE_URL = 'http://api.github.com'

# Github repositories list.
GITHUB_REPOSITORIES = [
    'farakavco/Tarsier', 'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
]

# Github authors list.
GITHUB_AUTHORS = [
    Author(
        username='pylover',
        email='vahid.mardani@gmail.com',
        avatar_url='https://avatars.githubusercontent.com/u/1302253?v=3',
        html_url='https://github.com/pylover',
        token=''
    ),
    Author(
        username='Sharez',
        email='aida.mirabadi@gmail.com',
        avatar_url='https://avatars.githubusercontent.com/u/328063?v=3',
        html_url='https://github.com/Sharez',
        token=''
    ),
    Author(
        username='aida-mirabadi',
        email='aida.mirabadi@gmail.com',
        avatar_url='https://avatars.githubusercontent.com/u/7857775?v=3',
        html_url='https://github.com/aida-mirabadi',
        token=''
    )
]
