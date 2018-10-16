; Simple math functions
; To load these functions in another program use
; (load "math.lsp")
; then you can use the functions like (triple 10)

(defun triple (X)
  (* 3 X)
)
(print (triple 3))

(defun cube (x)
	(* x x x)
)
(print (cube 3))

(print 3)

(print (+ 10 10))

(print (* 5 5))
