Crystal
=======

https://crystal-lang.org

Install
-------
Download the .tar.gz from
https://github.com/crystal-lang/crystal/releases/

Extracted, added bin/ to PATH.

Adds ``crystal`` and ``shards`` to PATH.

Run playground
--------------

``crystal play``

Compile and runs files
----------------------

crystal build hello.cr
crystal build hello.cr --static

crystal run hello.cr

Standard library documentation
------------------------------

https://crystal-lang.org/api

Initializing a library or app
-----------------------------

crstyal init lib mylib
crystal init app myproject


To package and share a module, push to github with the shard.yml file.


To add a package as a dependency in your projects shard.yml::

  dependencies:
  myproject:
      github: your-github-user/myproject
  Run shards install

To require a dependency in the code::

  require "myproject"

Documentation
-------------
Write docstrings with Markdown formatting to generate docs using::

  crystal docs
