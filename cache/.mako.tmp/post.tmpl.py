# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494877920.9213693
_enable_loop = True
_template_filename = 'c:/users/redwan huq/anaconda3/lib/site-packages/nikola/data/themes/bootstrap3/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        parent = context.get('parent', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        def content():
            return render_content(context)
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="post-')
        __M_writer(str(post.meta('type')))
        __M_writer(' h-entry hentry postpage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n    <div class="e-content entry-content" itemprop="articleBody text">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <aside class="postpromonav">\n    <nav>\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n    </nav>\n    </aside>\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
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
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if show_sourcelink:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post.tmpl", "filename": "c:/users/redwan huq/anaconda3/lib/site-packages/nikola/data/themes/bootstrap3/templates/post.tmpl", "source_encoding": "utf-8", "line_map": {"128": 8, "129": 9, "130": 10, "131": 10, "132": 10, "133": 12, "134": 12, "135": 12, "136": 13, "137": 14, "138": 14, "139": 14, "140": 14, "141": 14, "142": 16, "143": 17, "144": 17, "145": 17, "146": 17, "147": 17, "148": 19, "149": 20, "150": 22, "23": 3, "152": 22, "153": 23, "26": 2, "155": 24, "156": 24, "29": 4, "162": 50, "35": 0, "171": 50, "154": 23, "173": 52, "174": 53, "175": 53, "176": 53, "177": 53, "172": 51, "54": 2, "55": 3, "56": 4, "57": 5, "151": 22, "62": 25, "67": 48, "72": 56, "183": 177, "78": 27, "90": 27, "91": 28, "92": 28, "93": 29, "94": 29, "95": 31, "96": 31, "97": 35, "98": 35, "99": 36, "100": 36, "101": 39, "102": 40, "103": 41, "104": 41, "105": 42, "106": 42, "107": 45, "108": 45, "109": 45, "110": 47, "111": 47, "117": 7, "126": 7, "127": 8}}
__M_END_METADATA
"""
