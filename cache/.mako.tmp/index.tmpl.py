# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495988822.965645
_enable_loop = True
_template_filename = 'c:/users/redwan huq/anaconda3/lib/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content_header', 'extra_head', 'content']


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
        posts = context.get('posts', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagination = _mako_get_namespace(context, 'pagination')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        pagekind = context.get('pagekind', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
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


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        index_file = context.get('index_file', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
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
        posts = context.get('posts', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        _link = context.get('_link', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        pagination = _mako_get_namespace(context, 'pagination')
        front_index_header = context.get('front_index_header', UNDEFINED)
        def content():
            return render_content(context)
        pagekind = context.get('pagekind', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content_header():
            return render_content_header(context)
        nextlink = context.get('nextlink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
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
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
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
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"201": 45, "193": 38, "23": 2, "151": 16, "26": 3, "175": 32, "156": 17, "157": 18, "158": 19, "159": 19, "160": 19, "161": 21, "162": 22, "163": 22, "164": 22, "165": 24, "38": 0, "167": 26, "168": 26, "169": 26, "170": 28, "171": 28, "172": 28, "173": 28, "174": 31, "29": 4, "176": 32, "177": 32, "178": 32, "179": 32, "180": 33, "181": 34, "182": 34, "183": 34, "184": 36, "185": 37, "186": 37, "187": 37, "188": 37, "189": 37, "190": 37, "191": 37, "192": 37, "32": 5, "194": 39, "195": 39, "196": 39, "69": 2, "70": 3, "71": 4, "72": 5, "73": 6, "202": 46, "203": 47, "204": 48, "205": 48, "78": 14, "207": 53, "208": 54, "209": 54, "210": 55, "83": 57, "212": 56, "206": 50, "197": 41, "89": 17, "219": 213, "211": 55, "199": 44, "198": 43, "100": 8, "166": 25, "111": 8, "112": 9, "113": 9, "114": 10, "115": 11, "116": 11, "117": 11, "118": 13, "119": 13, "120": 13, "200": 45, "126": 16, "213": 56}, "uri": "index.tmpl", "source_encoding": "utf-8", "filename": "c:/users/redwan huq/anaconda3/lib/site-packages/nikola/data/themes/base/templates/index.tmpl"}
__M_END_METADATA
"""
