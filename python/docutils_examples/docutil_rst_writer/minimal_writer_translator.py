# Minimal example for a custom writer/translator to customize
# docutils output
from docutils.writers import html5_polyglot
from docutils.core import publish_string


class MyCustomHTMLTranslator(html5_polyglot.HTMLTranslator):
    pass


class MyCustomHTMLWriter(html5_polyglot.Writer):
    def __init__(self ):
        html5_polyglot.Writer.__init__(self)
        self.translator_class = MyCustomHTMLTranslator


if __name__ == '__main__':
    html_output = publish_string(source='Put reStructured text here.',
                                 writer=MyCustomHTMLWriter())
    print(html_output)
