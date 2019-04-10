"""""""""
Doc Title
"""""""""
........
Subtitle
........

.. contents:: Overview
   :depth: 2

=========
Section 1
=========

----------------------
Subsection 1 (Level 2)
----------------------

Sub-subsection 1 (level 3)
--------------------------

=========
Section 2
=========

.. This is a comment
   Special notes that are not shown but might come out as HTML comments

Text can be *italicized* or **bolded**  as well as ``monospaced``.
You can \*escape certain\* special characters.

Add an image with:

.. image:: screenshots/file.png
   :height: 100
   :width: 200
   :alt: alternate text if image does not exist/cannot be presented


You can inline an image or other directive with the |customsub| command.

.. |customsub| image:: image/image.png


- Bullet are made like this
- Point levels must be consisten
    * Sub-bullets
        + Sub-sub-bullets
- Lists

term
  Definition here

:Things: 
    item1 - these are 'field lists' not bulleted lists
    item2
    item 3

:Something: single item
:Someitem: single item


A code example/preformatted section must always end with double colon like it's presenting something::

    Anything indented is part of the preformatted block
   Until
  It gets back to
 Allll the way left

Now we're out of the preformatted block.

Hyperlinks
.. _Python: http://www.python.org/




Internal bookmark link
Can link to section with sectionname_.

.. _sectionname:

You can also refer to section by name
This links to `Section 1`_.


Footnote Reference [1]_

.. [1] This is footnote number one

Or autonumbered [#]_

.. [#] This becomes number two since one was already defined.


Footnote Reference [2]_

.. [2] This is footnote number one



