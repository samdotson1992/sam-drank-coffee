# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1559506255.2102118
_enable_loop = True
_template_filename = 'themes/detox/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        index_teasers = context.get('index_teasers', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        permalink = context.get('permalink', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content_header():
            return render_content_header(context._locals(__M_locals))
        index_file = context.get('index_file', UNDEFINED)
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
        parent = context.get('parent', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        permalink = context.get('permalink', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        posts = context.get('posts', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        index_teasers = context.get('index_teasers', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        pagekind = context.get('pagekind', UNDEFINED)
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('\n')
        for post in posts:
            __M_writer('<article class="li post">\n    <header class="post-header">\n        <h3 class="post-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h3>\n        <p class="post-time"><time datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n        by\n')
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
            __M_writer('        </p>\n    </header>\n\n\n\n    <section class="post-excerpt">\n')
            if index_teasers:
                __M_writer('    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </section>\n\n    <footer class="post-footer">\n        <span>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('\n            &nbsp;&nbsp;\n\n        </span>\n    </footer>\n</article>\n')
        __M_writer('\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/detox/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "69": 2, "70": 3, "71": 4, "72": 5, "73": 6, "78": 14, "83": 65, "89": 8, "100": 8, "101": 9, "102": 9, "103": 10, "104": 11, "105": 11, "106": 11, "107": 13, "108": 13, "109": 13, "115": 16, "140": 16, "145": 17, "146": 18, "147": 19, "148": 19, "149": 19, "150": 21, "151": 22, "152": 22, "153": 22, "154": 24, "155": 25, "156": 26, "157": 28, "158": 28, "159": 28, "160": 28, "161": 29, "162": 29, "163": 29, "164": 29, "165": 31, "166": 32, "167": 32, "168": 32, "169": 32, "170": 32, "171": 33, "172": 34, "173": 34, "174": 34, "175": 36, "176": 42, "177": 43, "178": 43, "179": 43, "180": 44, "181": 45, "182": 45, "183": 45, "184": 47, "185": 51, "186": 52, "187": 52, "188": 52, "189": 54, "190": 61, "191": 62, "192": 62, "193": 63, "194": 63, "195": 64, "196": 64, "202": 17, "213": 202}}
__M_END_METADATA
"""
