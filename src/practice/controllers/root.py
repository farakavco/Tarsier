# -*- coding: utf-8 -*-
"""Main Controller"""
import datetime
from khayyam import *
from tg import expose
from tg import request, tmpl_context
from practice import model
from practice.controllers.secure import SecureController
from practice.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from practice.lib.base import BaseController
from practice.controllers.error import ErrorController
from practice.model.github import Commit

__all__ = ['RootController']


class RootController(BaseController):
    """The root controller for the practice application."""
    secc = SecureController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "practice"

    @expose('practice.templates.index')
    def index(self):
        """Handle the front-page."""

        if 'date' in request.GET:
            date = request.GET['date']
            date = JalaliDate(date[:4], date[5:7], date[8:10]).todate()
        else:
            date = datetime.datetime.now()

        # kwargs = {'since': str(date), 'until': str(date + datetime.timedelta(days=1))}
        kwargs = {'since': str(date)}

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
