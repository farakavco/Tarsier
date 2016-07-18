
from pymlconf import ConfigManager
from os.path import abspath, join, dirname, exists
from lutino.proxy import ObjectProxy
from appdirs import user_config_dir


__builtin_config = """

debug: true

site:
  name: Tarsier

mako:
  directories:
    - %(tarsier_dir)s/messaging/templates
  module_directory: %(data_dir)s/mako/modules

logging:
  loggers:

    default:
      handlers:
        - console
      level: debug
      formatter: default

  formatters:
    default:
      format: "%%(asctime)s - %%(name)s - %%(levelname)s - %%(message)s"
      date_format: "%%Y-%%m-%%d %%H:%%M:%%S"

smtp:
  host: smtp.gmail.com
  port: 587
  username: 'SMTP_USERNAME_GOES_HERE'
  password: 'SMTP_PASSWORD_GOES_HERE'

email:
  subject: Daily Report

format:
  start_date: '%%Y-%%m-%%dT00:00:00Z'
  end_date: '%%Y-%%m-%%dT23:59:59Z'
  persian_date: '%%E %%d %%G %%Y'

github:
  base_url: http://api.github.com
  token: 'GITHUB_TOKEN_GOES_HERE'
  repositories: [farakavco/Tarsier, farakavco/kakapo, farakavco/blueprint, farakavco/lutino, farakavco/tutorials]
  authors: ((aida-mirabadi, aida.mirabadi@gmail.com), )

"""


_settings = None


def init_config(config=None, directories=None, files=None):
    """
    Initialize the configuration manager
    :param config: `string` or `dict`
    :param directories: semi-colon separated `string` or `list` of director(y|es)
    :param files: semi-colon separated `string` or `list` of file(s)
   """
    global _settings
    context = {
        'data_dir': abspath(join(dirname(__file__), '../../data')),
        'tarsier_dir': abspath(dirname(__file__))
    }
    _settings = ConfigManager(__builtin_config, context=context)

    if config:
        _settings.merge(config)

    local_config_file = join(user_config_dir(), 'tarsier.yaml')
    if exists(local_config_file):
        print('Loading config file: %s' % local_config_file)
        _settings.load_files(local_config_file)

    if directories:
        _settings.load_dirs(directories)

    if files:
        _settings.load_files(files)


settings = ObjectProxy(lambda: _settings)
