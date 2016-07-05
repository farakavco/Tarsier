# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467627578.8616598
_enable_loop = True
_template_filename = '/home/aida/Desktop/tg/practice/practice/templates/date.mak'
_template_uri = '/home/aida/Desktop/tg/practice/practice/templates/date.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        items = context.get('items', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n<div class="row">\n    <div class="col-md-12">\n        <form action="/date" method="get">\n            <input type="text" class="example1"/>\n            <button type="submit">submit</button>\n        </form>\n        <div class="jumbotron">\n            <h1 class="center-block text-center">Farakavco</h1>\n')
        for item in items:
            __M_writer('                <article class="box well col-md-12">\n                    <header class="col-md-12 center-block padding-bottom">\n                        <a href="')
            __M_writer(escape(item.github_url))
            __M_writer('" title="')
            __M_writer(escape(item.username))
            __M_writer('" class="avatar help-block col-md-2 center-block text-center">\n                            <img src="')
            __M_writer(escape(item.avatar))
            __M_writer('" class="img-circle help-block center-block">\n                        </a>\n                        <h3 class="col-md-12 center-block text-center username">')
            __M_writer(escape(item.username))
            __M_writer('</h3>\n                    </header>\n                    <div class="col-md-12">\n')
            for key, val in item.commits.items():
                __M_writer('                            <h3><b>Repository:</b> ')
                __M_writer(escape(key))
                __M_writer(' - ')
                __M_writer(escape(len(val)))
                __M_writer('</h3>\n                            <ul class="border-bottom">\n')
                for v in val:
                    __M_writer('                                    <li>\n                                        <a href="')
                    __M_writer(escape(v.url))
                    __M_writer('" title="')
                    __M_writer(escape(v.sha))
                    __M_writer('" class="smaller text-danger">\n                                            <b>Sha: </b> ')
                    __M_writer(escape(v.sha))
                    __M_writer('\n                                        </a>\n                                        <p class="message smaller"><b>Time: </b>')
                    __M_writer(escape(v.date))
                    __M_writer('</p>\n                                        <p class="message smaller"><b>Message: </b>')
                    __M_writer(escape(v.message))
                    __M_writer('</p>\n                                    </li>\n')
                __M_writer('                              </ul>\n')
            __M_writer('                    </div>\n                </article>\n')
        __M_writer('            <a class="btn btn-primary btn-lg opacity" href="http://www.turbogears.org" target="_blank">\n            ')
        __M_writer(escape(h.icon('book')))
        __M_writer(' Learn more\n            </a>\n        </div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  Commit\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/home/aida/Desktop/tg/practice/practice/templates/date.mak", "line_map": {"64": 32, "65": 32, "66": 35, "67": 37, "68": 40, "69": 41, "70": 41, "76": 3, "80": 3, "86": 80, "28": 0, "36": 1, "37": 5, "38": 14, "39": 15, "40": 17, "41": 17, "42": 17, "43": 17, "44": 18, "45": 18, "46": 20, "47": 20, "48": 23, "49": 24, "50": 24, "51": 24, "52": 24, "53": 24, "54": 26, "55": 27, "56": 28, "57": 28, "58": 28, "59": 28, "60": 29, "61": 29, "62": 31, "63": 31}, "filename": "/home/aida/Desktop/tg/practice/practice/templates/date.mak", "source_encoding": "utf-8"}
__M_END_METADATA
"""
