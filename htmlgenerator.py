__author__ = 'Irrevocable Cascade'

"""
This will create valid HTML 5 files
"""

DOCTYPES = (
    'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
    'b', 'base', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button',
    'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'command', 'datalist', 'dd', 'del',
    'details', 'dfn', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset',
    'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4',
    'h5', 'h6', 'head', 'header', 'hgroup', 'hr', 'html', 'i', 'iframe', 'img',
    'input', 'ins', 'kbd', 'keygen', 'label', 'legend', 'li', 'link', 'map',
    'mark', 'menu', 'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup', 'option',
    'output', 'p', 'param', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp',
    'script', 'section', 'select', 'small', 'source', 'span', 'strong', 'style', 'sub', 'summary',
    'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr',
    'track', 'ul', 'var', 'video', 'wbr')


class IllegalDoctypeError(ValueError):
    def __init__(self, doctype):
        self.month = doctype
    def __str__(self):
        return "Bad doctype %r; must be valid HTML 5 doctyoe" % self.doctype

class PageTemplate(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def adddoctype(self, doctype):

        if doctype not in DOCTYPES:
            raise IllegalDoctypeError(doctype)
        else:
            return '<!doctype {0}>'.format(str(doctype))


p = PageTemplate('index', 'html')

print(p.adddoctype('html'))
