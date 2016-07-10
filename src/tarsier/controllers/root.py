
from datetime import datetime, timedelta

from tg import expose
from tg import request, tmpl_context
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from tarsier import model
from tarsier.controllers.secure import SecureController
from tarsier.model import DBSession
from tarsier.lib.base import BaseController
from tarsier.controllers.error import ErrorController
from tarsier.model.github import Commit

__all__ = ['RootController']


START_DATE_FORMAT = '%Y-%m-%dT00:00:00'
END_DATE_FORMAT = '%Y-%m-%dT23:59:59'


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
        start_date_string = request.GET.get('start_date', None)
        end_date_string = request.GET.get('end_date', None)

        start_date = datetime.fromtimestamp(int(start_date_string)/1000) if start_date_string else datetime.today()
        end_date = datetime.fromtimestamp(int(end_date_string)/1000) if end_date_string else (start_date + timedelta(days=1))

        # Define query params of Github api.
        kwargs = {
            'since': start_date.strftime(START_DATE_FORMAT),
            'until': end_date.strftime(END_DATE_FORMAT)
        }

        # Define repositories list.
        repositories = [
            'farakavco/Tarsier', 'farakavco/kakapo', 'farakavco/blueprint', 'farakavco/lutino', 'farakavco/tutorials'
        ]

        result = Commit.get_all(repositories, **kwargs)

        return dict(items=result)
