
from mako.lookup import TemplateLookup, Template
from wheezy.core.descriptors import attribute
from tarsier.configuration import settings


class Messenger(object):
    """
    The abstract base class for all messaging operations
    """

    def render_body(self, body, template_string=None, template_filename=None):
        if template_string:
            mako_template = Template(template_string)
        elif template_filename:
            mako_template = self.lookup.get_template(template_filename)
        else:
            mako_template = None

        if mako_template:
            return mako_template.render(**body)
        else:
            return body

    @attribute
    def lookup(self):
        return TemplateLookup(
            directories=settings.mako.directories,
            module_directory=settings.mako.module_directory,
            input_encoding='utf8'
        )
