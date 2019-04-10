#!/usr/bin/guile -s
!#

(define (cube x)
	(display (* x x x)))

(cube 4)

(define (\n)
	(newline))
(\n)
