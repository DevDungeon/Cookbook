#!/usr/bin/guile -s
!#

; This doesn't appear to be required
;(import (rnrs))

; Displays "/path/to/cmdArgs.scm arg arg arg",
; which is usually "./cmdArgs.scm arg arg arg"
; if run directly or
; "cmdArgs.scm arg arg arg" if run using guile cmdArgs.scm 
(display (command-line))
(newline)

; Display arguments minus the actual calling program name
; Empty list if no arguments passed to program
(display (cdr (command-line)))
(newline)
