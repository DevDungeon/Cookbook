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

Settings files
==============

User settings are stored in ``~/.config/Code`` for VSCode proper or ``~/.config/code-oss-dev`` for the open source dev version.

You can have specific settings for each project.
Create a ``.vscode`` directory inside any workspace folder and add the files needed. For example::

- ``launch.json`` - Debug launch 
- ``settings.json`` - Custom settings, extension configurations
- ``tasks.json`` - 

This is a sample ``settings.json`` file from ``~/.config/code-oss-dev/User/settings.json``::

	{
	    "telemetry.enableTelemetry": false,
	    "telemetry.enableCrashReporter": false,
	    
	    "workbench.colorTheme": "One Dark Pro",
	    "workbench.iconTheme": "material-icon-theme",
	    
	    "editor.cursorBlinking": "phase",
	    "editor.fontFamily": "'Hack', 'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback'",
	    
	    "window.zoomLevel": -1,
	    
	    "workbench.startupEditor": "newUntitledFile", // No welcome page

	    "keyboard.dispatch": "keyCode", // To allow Caps->Escape dconf mapping (good for vim mode)
	    
	    "vim.enableNeovim": true,
	    "vim.neovimPath": "/usr/bin/nvim",
	}


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

- Run ``Tasks: Configure Tasks`` from the command palette
- Select the ``Create tasks.json file from template``

To run a task:

- Run ``Tasks: Run Task`` from the command palette.
- Choose the task you created.

To modify tasks:

- Run ``Tasks: Configure Task`` from the command palette.
- It will ask which task to configure, or prompt for a new ``tasks.json`` file if none exists.

An example ``{workspaceFolder}/.vscode/tasks.json`` file::

	{
	    // See https://go.microsoft.com/fwlink/?LinkId=733558
	    // for the documentation about the tasks.json format
	    "version": "2.0.0",
	    "tasks": [
		{
		    "label": "Run the date command",
		    "type": "shell",
		    "command": "date",
		    "problemMatcher": []
		}
	    ]
	}

Custom launchers
================

Go to the Debug tab (``CTRL-SHIFT-D``) and choose `Add Config` or modify the ``.vscode/launch.json`` file in the workspace directory directly.

For example, if the ``Debugger for Chrome`` extension is installed, you can add::
        
	{
            "type": "chrome",
            "request": "launch",
            "name": "Open Chrome for Angular app",
            "url": "http://localhost:4200",
            "webRoot": "${workspaceFolder}",
            "runtimeExecutable": "/usr/bin/chromium-browser",
        }

Or to launch a Django app::

        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "console": "integratedTerminal",
            "args": [
                "runserver",
                "--noreload",
                "--nothreading"
            ],
            "django": true
        },



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
