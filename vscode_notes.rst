============
VSCode Notes
============


Building from source
====================

Build with:: 

	sudo apt install libsecret-1-0 libsecret-1-dev libxkbfile-dev
	git clone https://github.com/Microsoft/vscode
	cd vscode
	yarn watch

Run with::

	scripts/code.sh

Change logo by replacing image in ``resources`` directory.

Settings stored in
==================

``~/.config/Code`` or ``~/.config/code-oss-dev``

Icon theme: Material


Custom snippets
================

File > Preferences > Users Snippets
Then select, ``New global snippets file``


Custom theme
============

Run from palette::

  Developer: Generate Color Theme from Current Settings

https://medium.com/@caludio/how-to-write-a-visual-studio-code-color-theme-from-scratch-7ccb7e5da2aa


Custom tasks
============

To create a custom task from template:
- Run ``Configure Tasks`` from the command palette
- Select the ``Create tasks.json file from template``

Custom plugin
=============

Generate a plugin with ``yo``::

  npm install -g yo generator-code
  yo code  # Generate a new plugin

Then enter the directory, run ``code`` to load it
and press F5 on ``extension.ts`` to debug.

To package...::

  npm installl -g vsce

  cd <extensionDir>
  vsce package  # Fill out required fields like publisher/license
  #vsce publish


Install a VSIX file with::
  
  code --install-extension my-extension-0.0.1.vsix