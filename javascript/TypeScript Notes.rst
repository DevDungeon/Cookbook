TypeScript Notes
================


Getting started
---------------

To install the TypeScript compiler::

  npm install -g typescript

To compile TypeScript files::

  tsc myfile.ts

To auto-compile on change, use watch flag::

  tsc --watch myfile.ts
  tsc --watch dir/*

TSLint
------

Install with::

  npm install -g tslint

Initialize inside a project directory::

  tslint --init

Then run with::

  tslint ./*.ts
  tslint -c tslint.json ./**/*.ts

