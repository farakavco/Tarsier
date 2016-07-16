from datetime import datetime


# Github data service configs.
GITHUB_BASE_URL = 'http://api.github.com'
EMAIL_SUBJECT = "Daily report - %s " % datetime.today().strftime('%Y-%m-%d')

# Date configs.
START_DATE_FORMAT = '%Y-%m-%dT00:00:00'
END_DATE_FORMAT = '%Y-%m-%dT23:59:59'

# SMTP configs.
HOST = 'smtp.gmail.com'
PORT = 587
USERNAME = ''
PASSWORD = ''
