# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467641710.5796463
_enable_loop = True
_template_filename = '/home/aida/Desktop/tg/practice/practice/templates/index.mak'
_template_uri = '/home/aida/Desktop/tg/practice/practice/templates/index.mak'
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
        __M_writer('\n<div class="row">\n    <div class="col-md-12">\n\n        <div class="box">\n            <form action="/" method="get">\n                <label class="lable">Since Date: </label><input type="text" name="date" class="date  form-control"/>\n                <button type="submit" class="btn btn-warning">Submit</button>\n            </form>\n        </div>\n\n        <div class="jumbotron box">\n            <h1 class="center-block text-center">Commits List</h1>\n')
        if items:
            for item in items:
                __M_writer('                    <article>\n                        <header class="col-md-12 center-block padding-bottom">\n                            <a href="')
                __M_writer(escape(item.github_url))
                __M_writer('" title="')
                __M_writer(escape(item.username))
                __M_writer('" class="avatar help-block col-md-2 center-block text-center">\n                                <img src="')
                __M_writer(escape(item.avatar))
                __M_writer('" class="img-circle help-block center-block">\n                            </a>\n                            <h3 class="col-md-12 center-block text-center username">')
                __M_writer(escape(item.username))
                __M_writer('</h3>\n                        </header>\n                        <div class="col-md-12 commit-list">\n')
                for key, val in item.commits.items():
                    __M_writer('                                <h3>')
                    __M_writer(escape(key))
                    __M_writer('  <span class="smallest">( commits: ')
                    __M_writer(escape(len(val)))
                    __M_writer(' )</span></h3>\n                                <ul class="commit-container col-md-12">\n')
                    for v in val:
                        __M_writer('                                        <a href="')
                        __M_writer(escape(v.url))
                        __M_writer('" title="')
                        __M_writer(escape(v.sha))
                        __M_writer('" class="col-md-5 commit-box">\n                                             <li>\n                                                <p class="smaller text-sha"><b>Sha: </b> ')
                        __M_writer(escape(v.sha))
                        __M_writer('</p>\n                                                <p class="smallest">')
                        __M_writer(escape(v.time))
                        __M_writer('</p>\n                                                <p class="message smaller"><b>Message: </b>')
                        __M_writer(escape(v.message))
                        __M_writer('</p>\n                                            </li>\n                                        </a>\n\n')
                    __M_writer('                                  </ul>\n')
                __M_writer('                        </div>\n                    </article>\n')
        else:
            __M_writer('                <p>There is no commit.</p>\n')
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
{"filename": "/home/aida/Desktop/tg/practice/practice/templates/index.mak", "source_encoding": "utf-8", "line_map": {"64": 35, "65": 36, "66": 36, "67": 41, "68": 43, "69": 46, "70": 47, "71": 49, "72": 50, "73": 50, "79": 3, "83": 3, "89": 83, "28": 0, "36": 1, "37": 5, "38": 18, "39": 19, "40": 20, "41": 22, "42": 22, "43": 22, "44": 22, "45": 23, "46": 23, "47": 25, "48": 25, "49": 28, "50": 29, "51": 29, "52": 29, "53": 29, "54": 29, "55": 31, "56": 32, "57": 32, "58": 32, "59": 32, "60": 32, "61": 34, "62": 34, "63": 35}, "uri": "/home/aida/Desktop/tg/practice/practice/templates/index.mak"}
__M_END_METADATA
"""
