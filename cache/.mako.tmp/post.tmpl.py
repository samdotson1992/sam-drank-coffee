# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559506000.8755019
_enable_loop = True
_template_filename = 'themes/detox/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        math = _mako_get_namespace(context, 'math')
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        math = _mako_get_namespace(context, 'math')
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        messages = context.get('messages', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post">\n\t<header class="post-header">\n        <h3 class="p-post-title">')
        __M_writer(str(post.title()))
        __M_writer('</h3>\n    </header>\n\n    <section class="post-content">\n\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n </section>\n\n    <hr>\n\n    <footer class="post-footer">\n        <section class="f-1">\n\n            <section class="author"><p>\n')
        if author_pages_generated:
            __M_writer('                <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('                ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('            </p></section>\n\n\n            <p class="f-post-time"><time datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('">')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('</time></p>\n        </section>\n        <section class="f-2">\n            <section class="share">\n                <span>Share:\n                <a class="icon-twitter" href="http://twitter.com/share?text=')
        __M_writer(filters.url_escape(str(post.title())))
        __M_writer('&url=')
        __M_writer(filters.url_escape(str(post.permalink(absolute=True))))
        __M_writer('"\n                    onclick="window.open(this.href, \'twitter-share\', \'width=550,height=235\');return false;">\n                    <i class="fa fa-twitter"></i>\n                </a>\n                <a class="icon-facebook" href="https://www.facebook.com/sharer/sharer.php?u=')
        __M_writer(filters.url_escape(str(post.permalink(absolute=True))))
        __M_writer('"\n                    onclick="window.open(this.href, \'facebook-share\',\'width=580,height=296\');return false;">\n                    <i class="fa fa-facebook"></i>\n                </a>\n                <a class="icon-google-plus" href="https://plus.google.com/share?url=')
        __M_writer(filters.url_escape(str(post.permalink(absolute=True))))
        __M_writer('"\n                   onclick="window.open(this.href, \'google-plus-share\', \'width=490,height=530\');return false;">\n                    <i class="fa fa-google-plus"></i>\n                </a>\n                </span>\n            </section>\n\n\n        </section>\n\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n\n    </footer>\n\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/detox/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "57": 2, "58": 3, "59": 4, "60": 5, "61": 6, "66": 27, "71": 89, "77": 8, "87": 8, "88": 9, "89": 9, "90": 10, "91": 11, "92": 11, "93": 11, "94": 13, "95": 13, "96": 13, "97": 14, "98": 15, "99": 15, "100": 15, "101": 15, "102": 15, "103": 17, "104": 18, "105": 18, "106": 18, "107": 18, "108": 18, "109": 20, "110": 21, "111": 23, "112": 23, "113": 23, "114": 24, "115": 24, "116": 25, "117": 25, "118": 26, "119": 26, "125": 29, "139": 29, "140": 32, "141": 32, "142": 37, "143": 37, "144": 46, "145": 47, "146": 47, "147": 47, "148": 47, "149": 47, "150": 48, "151": 49, "152": 49, "153": 49, "154": 51, "155": 54, "156": 54, "157": 54, "158": 54, "159": 59, "160": 59, "161": 59, "162": 59, "163": 63, "164": 63, "165": 67, "166": 67, "167": 77, "168": 78, "169": 79, "170": 79, "171": 80, "172": 80, "173": 83, "174": 83, "175": 83, "176": 88, "177": 88, "183": 177}}
__M_END_METADATA
"""
