# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1467637646.5195012
_enable_loop = True
_template_filename = '/home/aida/Desktop/tg/practice/practice/templates/master.mak'
_template_uri = '/home/aida/Desktop/tg/practice/practice/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['footer', 'main_menu', 'body_class', 'meta', 'title', 'head_content', 'content_wrapper']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer('\n    <title>')
        __M_writer(escape(self.title()))
        __M_writer('</title>\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer('" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer('" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/persian-datepicker-0.4.5.css')))
        __M_writer('" />\n    ')
        __M_writer(escape(self.head_content()))
        __M_writer('\n</head>\n<body class="')
        __M_writer(escape(self.body_class()))
        __M_writer('">\n    ')
        __M_writer(escape(self.main_menu()))
        __M_writer('\n  <div class="container">\n    ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer('\n  </div>\n    ')
        __M_writer(escape(self.footer()))
        __M_writer('\n  <script src="http://code.jquery.com/jquery.js"></script>\n  <script src="')
        __M_writer(escape(tg.url('/javascript/bootstrap.min.js')))
        __M_writer('"></script>\n  <script src="')
        __M_writer(escape(tg.url('/javascript/pwt-date.js')))
        __M_writer('"></script>\n  <script src="')
        __M_writer(escape(tg.url('/javascript/persian-datepicker-0.4.5.js')))
        __M_writer('"></script>\n  <script type="text/javascript">\n    $(document).ready(function() {\n        $(".date").pDatepicker();\n    });\n  </script>\n</body>\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        getattr = context.get('getattr', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <footer class="footer hidden-xs hidden-sm">\n    <a class="pull-right" href="http://www.turbogears.org"><img style="vertical-align:middle;" src="')
        __M_writer(escape(tg.url('/img/under_the_hood_blue.png')))
        __M_writer('" alt="TurboGears 2" /></a>\n    <p>Copyright &copy; ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'TurboGears2')))
        __M_writer(' ')
        __M_writer(escape(h.current_year()))
        __M_writer('</p>\n  </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        getattr = context.get('getattr', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        page = context.get('page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <!-- Navbar -->\n  <nav class="navbar navbar-default">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">\n        <img src="')
        __M_writer(escape(tg.url('/img/turbogears_logo.png')))
        __M_writer('" height="20" alt="TurboGears 2"/>\n        ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'turbogears2')))
        __M_writer('\n      </a>\n    </div>\n\n    <div class="collapse navbar-collapse" id="navbar-content">\n      <ul class="nav navbar-nav">\n        <li class="')
        __M_writer(escape(('', 'active')[page=='index']))
        __M_writer('"><a href="')
        __M_writer(escape(tg.url('/')))
        __M_writer('">Home</a></li>\n      </ul>\n\n    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer('" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer('\n')
        if flash:
            __M_writer('      <div class="row">\n        <div class="col-md-8 col-md-offset-2">\n              ')
            __M_writer(flash )
            __M_writer('\n        </div>\n      </div>\n')
        __M_writer('  ')
        __M_writer(escape(self.body()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/aida/Desktop/tg/practice/practice/templates/master.mak", "uri": "/home/aida/Desktop/tg/practice/practice/templates/master.mak", "source_encoding": "utf-8", "line_map": {"129": 49, "155": 29, "133": 49, "162": 35, "172": 166, "139": 47, "17": 0, "148": 28, "154": 28, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 8, "34": 8, "35": 9, "36": 9, "37": 11, "38": 11, "39": 12, "40": 12, "41": 14, "42": 14, "43": 16, "44": 16, "45": 18, "46": 18, "47": 19, "48": 19, "49": 20, "50": 20, "51": 40, "52": 42, "53": 46, "54": 47, "55": 49, "56": 56, "57": 81, "163": 35, "159": 31, "63": 51, "160": 32, "71": 51, "72": 53, "73": 53, "74": 54, "75": 54, "76": 54, "77": 54, "83": 58, "164": 39, "91": 58, "92": 68, "93": 68, "94": 69, "95": 69, "96": 70, "97": 70, "98": 76, "99": 76, "100": 76, "101": 76, "165": 39, "161": 33, "107": 42, "116": 43, "121": 43, "122": 44, "123": 44, "166": 39}}
__M_END_METADATA
"""
