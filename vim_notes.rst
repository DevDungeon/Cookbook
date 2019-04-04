Vim Cheatsheet
==============


Bash/Zsh vi mode
----------------
You can use vi mode in your shell by setting the mode. By default
Bash uses emacs mode but you can update your .bashrc or set it
manually. By default, it puts you in insert mode, so it doesn't
feel very different from emacs mode. You can switch in to
command mode when you need to manipulate or navigate the line.

- Switch shell modes with ``set -o vi`` and back with ``set -o emacs``.
- In Zsh, there is a ``vi-mode`` plugin that can be enabled which allows
  themes to show an indicator if you are in command mode. For example,
  the ``avit`` theme.
- Go through previous/next commands with ``j`` and ``k`` when in command mode.
  CTRL-P and CTRL-N may or may not still work since they are emacs binds.
  Up and down arrows usually still work.
- Search history with ``/``. ``CTRL-R`` and ``CTRL-S`` might still work.
- Press ``v`` in command mode to pull up the full editor with the command
  in the open buffer. When you save and exit, the final output from the
  editor is dropped in your shell ready to run. Change the default editor
  that is opened when pressing ``v`` by changing ``EDITOR`` environment
  variable. For example, ``export EDITOR=vim``.

Switch between modes
--------------------
- ``CTRL-[`` or ``ESC`` to to command mode.
- ``i``, ``a``, and ``o`` to go in to insert mode.
- ``I``, ``A``, and ``O`` to go in to insert mode alternate ways.

Launching vim
-------------
- Run ``vim`` by itself to open an unnamed buffer
- Open a single file with ``vim filename``
- Open multiple buffers (single window) ``vim file1 file2 file3``
- Open multiple buffers (split windows)
  + Horizontally split: ``vim -o file1 file2``
  + Vertically split: ``vim -O file1 file2``

Managing windows
----------------
- Split with current file using ``:vsplit`` or ``:split``.
- Optionally open new files like ``:vsplit filename``.
- Switch windows with ``CTRL-W CTRL-W``.
- Resize windows with ``CTRL-W`` to intiate the chord,
  then follow up with one of:
  + Shrink and expand vertical with ``-`` or ``+``.
  + Shrink and expand horizontal with ``<`` and ``>``.
  + Maximize vertical with ``_``.
  + Maximize width with ``|`` .
  + Split everything equally with ``=``.
- Resize using commands:
  + Horizontal resize with ``:resize 20``, ``:res -3``, or ``:res +3``
  + Vertical resize with ``:vertical resize 20``, ``:vertical res -3``, or ``:vertical res +3``

Buffers, reading & opening files
--------------------------------
Buffers (open files) are separate from windows.
You can have multiple windows all for the same buffer.
You can also have one window with multiple buffers
open in the background. Buffers are always in-memory.
It is only when you **write** using a command
that the changes are saved to disk.

Loading files in to buffers
- Open a file for editing with ``:e filename``
- Split window w/ new unnamed buffer using ``:vnew`` or ``:new``.
- Use ``:enew`` to edit new buffer in current window.
- Use ``:tabnew`` to open tab w/ new buffer.

- List available buffers with ``:ls``.
- Create a new unnamed 
- Switch current window buffer with ``:b2`` or ``:b!2``, ``:bnext`` ``:bprevious``.

Saving and exiting
------------------
- Simple exit with ``q``.
- Force quit (ignore changes) with ``q!``.
- Save/write with ``:w``
- Save and quit with ``:wq`` or ``:x`` or ``ZZ``.

Moving around
-------------
You can multiply any of these commands by pressing a number first.

- General move with ``j``, ``k``, ``l``, ``h``
- Scroll up and down full/half pages with ``CTRL-D``, ``CTRL-U``, ``CTRL-B``, ``CTRL-F``.
- Go forward and backward with ``w``, ``b``, ``W``, ``B``.
- Go to beginning and end of file with ``gg`` and ``G``.
- Go to specific lines (e.g. 33) with ``:33`` or ``33G``.
- Go to beginning and end of lines with ``$``, ``^``, and ``0``.

Cut, paste, delete
------------------
- Delete character with ``x``.
- Make visual selections with ``v`` or ``V``.
- Copy/yank selection with ``y``.
- Delete/cut selection with ``d``.
- Copy/yank line with ``yy``.
- Delete/cut a line with ``dd``.
- Paste with ``p`` or ``P``.

Undo
----
- Just press ``u`` in command mode
- Type ``:u`` command and press enter.

Editing
-------
Delete and change are similar but change will delete the item
and switch in to insert mode. Delete will only delete.
For both, you can work "inside" an element, or on "all" of the
element, signified with the keys ``a`` or ``i``. For example
"delete inside )" will delete everything inside the parenthesis.
"delete all-of )" will delete the everythign inside AND parenthesis.
This works with words, quotation marks, parenthesis, brackets, braces, etc.

- Change inside/all word with ``caw`` or ``ciw``.
- Change inside/all like ``ci)`` or ``ci"``.
- Delete to something like ``dt)`` or ``dt"``.
- Delete inside something like ``di}`` or ``di]``.
- Delete a/all like ``daw``, ``da)``, ``da"``.

Search, find, and replace
-------------------------
- Search with ``/`` and type in the query.
- Re-run last search with just a blank ``/``.

Running shell commands
----------------------
- Execute commands like this ``:!ls``.
- Can also read output in to file with ``:r !ls``

Misc
-----
- Repeat last command with ``.``
- Read file contents and output at cursor with ``:r filename``
- Bind ``CAPS LOCK`` to ``Escape``/``CTRL-[`` for convenience.

.. vimrc/vimscript
.. ---------------
.. Coming soon
.. syntax on, line numbers

My ``~/.vimrc``::

    set number

    " show existing tab with 4 spaces width
    set tabstop=4
    " when indenting with '>', use 4 spaces width
    set shiftwidth=4
    " On pressing tab, insert 4 spaces
    set expandtab

    set showcmd     " Show (partial) command in status line.
    set showmatch       " Show matching brackets.
    set ignorecase      " Do case insensitive matching
    "set smartcase      " Do smart case matching
    set incsearch       " Incremental search
    "set autowrite      " Automatically save before commands like :next and :make
    "set hidden     " Hide buffers when they are abandoned
    "set mouse=a        " Enable mouse usage (all modes)

    if filereadable("${HOME}/.vimrc.local")
      source ${HOME}/.vimrc.local
    endif
