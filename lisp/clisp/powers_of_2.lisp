(defun binary(x)
	(expt 2 x) 
)

(loop for i from 0 to 32 by 4
	do (print (binary i))
)
