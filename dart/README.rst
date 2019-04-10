Dart Language Notes
===================

Build from source
-----------------

Follow the instructions on https://github.com/dart-lang/sdk/wiki/Building

Then run::

    sudo apt-get install g++-multilib git python curl
    git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
    export PATH="$PATH:$PWD/depot_tools"
    mkdir dart-sdk
    cd dart-sdk
    fetch dart
    cd dart-sdk/sdk
    ./tools/build.py --mode release --arch x64 create_sdk

The output will be in out/ReleaseX64/dart_sdk

Package repository
------------------

https://pub.dartlang.org/

Building
--------

One potential option is to build with ``build_runner`` https://github.com/dart-lang/build
which works well with JavaScript target.

Or install the ``webdev`` tool::

  pub global activate webdev

and then run::

  webdev serve
  webdev build

To build the JavaScript output file, use ``dart2js``::

  dart2js -o output.js source.dart

To run JavaScript on the server, run with the d8 preamble::

  d8 <dart-sdk>/lib/_internal/js_runtime/lib/preambles/d8.js output.js

To install ``d8`` try https://github.com/v8/v8

  fetch v8
  cd v8
  gclient sync
  tools/dev/gm.py x64.release

To create a standalone executable, update the ``pubspec.yaml`` to include::

  executables:
    myexecutablefilename: nameofdartfile

Then to create the executable file::

  pub global activate --source path <path to Dart project>

Pub will install executables into ``$HOME/.pub-cache/bin``.
All it really does is create a script to call ``pub run``.
