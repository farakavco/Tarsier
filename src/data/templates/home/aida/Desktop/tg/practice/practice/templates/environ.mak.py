# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1466601952.341427
_enable_loop = True
_template_filename = '/home/aida/Desktop/tg/practice/practice/templates/environ.mak'
_template_uri = '/home/aida/Desktop/tg/practice/practice/templates/environ.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['title', 'head_content']


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
        sorted = context.get('sorted', UNDEFINED)
        environment = context.get('environment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n  <div class="row">\n    <div class="col-xs-12">\n      <h2>The WSGI nature of the framework</h2>\n\n      <p>In this page you can see all the WSGI variables your request object has,\n         the ones in capital letters are required by the spec, then a sorted by\n         component list of variables provided by the Components, and at last\n         the "wsgi." namespace with very useful information about your WSGI Server</p>\n      <p>The keys in the environment are:</p>\n\n      <div class="table-responsive">\n        <table class="table table-hover">\n')
        for key in sorted(environment):
            __M_writer('          <tr>\n              <td>')
            __M_writer(escape(key))
            __M_writer('</td>\n              <td>')
            __M_writer(escape(environment[key]))
            __M_writer('</td>\n          </tr>\n')
        __M_writer('        </table>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  Learning TurboGears 2.3: Information about TG and WSGI\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n  <style>\n    .table {\n      word-wrap: break-word;\n      table-layout: fixed;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 7, "35": 1, "36": 5, "37": 14, "38": 28, "39": 29, "40": 30, "41": 30, "42": 31, "43": 31, "44": 34, "70": 64, "60": 7, "50": 3, "54": 3, "28": 0}, "source_encoding": "utf-8", "uri": "/home/aida/Desktop/tg/practice/practice/templates/environ.mak", "filename": "/home/aida/Desktop/tg/practice/practice/templates/environ.mak"}
__M_END_METADATA
"""
