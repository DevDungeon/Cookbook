Batch (.bat/.cmd) scripting notes
=================================

Comments
--------

    rem this is a comment. short for 'reminder'
    :: another comment option. Only work at start of lines

Get help
--------

    dir /?

Set env variable for single run
-------------------------------

    set PATH C:\bin;%PATH% C:\run.bat

Permanently alter env variable
------------------------------

    setx set PATH C:\bin;%PATH%

cat equivalent
----------------

    type myfile.txt

List dir in order of time
-------------------------

    dir /OD

Print something to screen
-------------------------

    echo "hello"

Print paged output (more)
------------------

    dir | more

Print paths matching command (like which)
-----------------------------

    where php
    