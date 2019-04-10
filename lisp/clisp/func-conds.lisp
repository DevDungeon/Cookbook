; Multiple paraments with optional ones
(defun add(a b c &optional d e)
	(cond
		( (eq d nil)
			(+ a b c)
		)
		( (not (eq e nil))
			(+ a b c d e))
		( (not(eq d nil))
			(+ a b c d))

	)
)

(print (add 1 1 1))
(print (add 1 1 1 1))
(print (add 1 1 1 1 1))