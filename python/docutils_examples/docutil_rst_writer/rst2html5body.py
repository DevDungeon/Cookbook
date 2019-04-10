"""
A custom docutils writer that will convert reStructuredText (RST) to html5,
but slightly modified from the html5_polyglot writer. The goal is to output
only the HTML body with the intention of embedding it inside a larger HTML
document using a content management system (CMS) like Drupal, Wordpress,
or Django.

- It only outputs the body, from subtitle to end of document, no HTML
  boilerplate, no CSS, no title.
- It lowers the heading level by one. It assumes the h1 is being output
  as the document title by the CMS. The output starts with the subtitle,
  and goes to the end of the document.

Built using
http://www.arnebrodowski.de/blog/write-your-own-restructuredtext-writer.html
as a reference.

It has a translator and a writer.

The translator is a  defines how to wrap or output each type of node.
At it's core, the translator is actually a ``nodes.GenericNodeVisitor``
that visits each node and decides how to process it.

The writer is what gets passed to the ``publish_*`` functions in the end
that process the document and provide HTML output.
The writer contains a reference to which translator it will use.

To use this writer, see the __main__ section at the bottom.
You call ``docutils.core.publish_*`` and pass it your customer writer.
"""
from docutils.writers import html5_polyglot
from docutils import nodes
import os


class HTMLBodyTranslator(html5_polyglot.HTMLTranslator):
    """
    Contains all the logic on how to wrap various nodes with HTML.
    For each node type, you can write a ``visit_*`` and ``depart_*``
    method. Copy the existing method from
    ``docutils.writers.html5_polyglot.HTMLTranslator`` if there is one,
    and modify it from there.

    Get list of all node types::
    
      >>> import docutils.nodes
      >>> docutils.nodes.node_class_names
      >>> help(docutils.nodes)

      node_class_names:
        Text
        abbreviation acronym address admonition attention attribution author
            authors
        block_quote bullet_list
        caption caution citation citation_reference classifier colspec comment
            compound contact container copyright
        danger date decoration definition definition_list definition_list_item
            description docinfo doctest_block document
        emphasis entry enumerated_list error
        field field_body field_list field_name figure footer
            footnote footnote_reference
        generated
        header hint
        image important inline
        label legend line line_block list_item literal literal_block
        math math_block
        note
        option option_argument option_group option_list option_list_item
            option_string organization
        paragraph pending problematic
        raw reference revision row rubric
        section sidebar status strong subscript substitution_definition
            substitution_reference subtitle superscript system_message
        table target tbody term tgroup thead tip title title_reference topic
            transition
        version
        warning
    """

    def visit_title(self, node):
        # Modifed code, copied from parent class
        check_id = 0  # TODO: is this a bool (False) or a counter?
        close_tag = '</p>\n'
        if isinstance(node.parent, nodes.topic):
            self.body.append(
                  self.starttag(node, 'p', '', CLASS='topic-title first'))
        elif isinstance(node.parent, nodes.sidebar):
            self.body.append(
                  self.starttag(node, 'p', '', CLASS='sidebar-title'))
        elif isinstance(node.parent, nodes.Admonition):
            self.body.append(
                  self.starttag(node, 'p', '', CLASS='admonition-title'))
        elif isinstance(node.parent, nodes.table):
            self.body.append(
                  self.starttag(node, 'caption', ''))
            close_tag = '</caption>\n'
        elif isinstance(node.parent, nodes.document):
            self.body.append(self.starttag(node, 'h1', '', CLASS='title'))
            close_tag = '</h1>\n'
            self.in_document_title = len(self.body)
        else:
            assert isinstance(node.parent, nodes.section)
            h_level = self.section_level + self.initial_header_level# - 1
            atts = {}
            if (len(node.parent) >= 2 and
                isinstance(node.parent[1], nodes.subtitle)):
                atts['CLASS'] = 'with-subtitle'
            self.body.append(
                  self.starttag(node, 'h%s' % h_level, '', **atts))
            atts = {}
            if node.hasattr('refid'):
                atts['class'] = 'toc-backref'
                atts['href'] = '#' + node['refid']
            if atts:
                self.body.append(self.starttag({}, 'a', '', **atts))
                close_tag = '</a></h%s>\n' % (h_level)
            else:
                close_tag = '</h%s>\n' % (h_level)
        self.context.append(close_tag)

    # Required override
    def should_be_compact_paragraph(self, node):
        if(isinstance(node.parent, nodes.block_quote)):
            return 0


class HTMLBodyWriter(html5_polyglot.Writer):
    """
    A ``docutils`` writer that will output HTML intended to be used within
    a larger existing HTML document, like within a content management system
    blog post.

    Writer that inherits from ``distutils.writers.html5_polyglot.Writer``.
    but overrides the ``translator_class`` which makes a few tweaks
    like lowering the heading levels by one.
    """
    
    def __init__(self ):
        self.parts = {}
        self.translator_class = HTMLBodyTranslator


if __name__ == '__main__':  # rst2html5body.py
    """
    Take a filename from the first command-line argument,
    process it using the custom writer, and output the body section
    only to standard output.

    Example usage::

      rst2html5body.py readme.rst > readme.html

    Then use that output as the content for your blog post.
    """
    from docutils.core import publish_parts
    import sys

    # First argument provided on the command line is the RST file name
    with open(sys.argv[1]) as rst_file:
        rst_content = rst_file.read()

    # publish_parts() will return a dictionary with the different
    # parts of the document, like head, stylesheet, body, already
    # processed and turned in to HTML, just separated for us.
    # There are other ``publish_*`` options like publish_cmdline,
    # publish_file, publish_string, and more.
    # If you want the final full standalone HTML document with all the
    # boilerplate,use ``publish_string()`` instead.
    output_document_parts = publish_parts(source=rst_content,
                                          writer=HTMLBodyWriter())

    # >>> output_parts.keys()  # List all of the parts available

    # ['whole', 'encoding', 'version', 'head_prefix', 'head', 'stylesheet',
    # 'body_prefix', 'body_pre_docinfo', 'docinfo', 'body', 'body_suffix',
    # 'title', 'subtitle', 'header', 'footer', 'meta', 'fragment',
    # 'html_prolog', 'html_head', 'html_title', 'html_subtitle', 'html_body']

    print(output_document_parts['stylesheet'])
    print(output_document_parts['body'])
