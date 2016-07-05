
from datetime import timedelta

from tg import expose
from tg import request, tmpl_context
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
from khayyam import JalaliDate

from tarsier import model
from tarsier.controllers.secure import SecureController
from tarsier.model import DBSession
from tarsier.lib.base import BaseController
from tarsier.controllers.error import ErrorController
from tarsier.model.github import Commit

__all__ = ['RootController']


DEFAULT_DATE_FORMAT = '%Y-%m-%d'


class RootController(BaseController):
    """The root controller for the tarsier application."""
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "tarsier"

    @expose('tarsier.templates.index')
    def index(self):
        """Handle the front-page."""

        date_string = request.GET.get('date')

        date = JalaliDate.today() if date_string is None else JalaliDate.strptime(DEFAULT_DATE_FORMAT, date_string)

        kwargs = {'since': date.strftime(DEFAULT_DATE_FORMAT), 'until': (date + timedelta(days=1)).strftime(DEFAULT_DATE_FORMAT)}

        # Define repositories list.
        repositories = [
            'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
        ]

        # Define authors list.
        authors = [
            {'login': 'Sharez',
             'email': 'aida.mirabadi@gmail.com',
             'avatar_url': 'https://avatars.githubusercontent.com/u/328063?v=3',
             'html_url': 'https://github.com/Sharez'},
            # {'login': 'pylover',
            #  'avatar_url': 'https://avatars.githubusercontent.com/u/1302253?v=3',
            #  'html_url': 'https://github.com/pylover'},
        ]

        result = Commit.get_all(repositories, authors, **kwargs)
        return dict(items=result)
