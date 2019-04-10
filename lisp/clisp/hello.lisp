; Hello world
; keywords like DEFUN are case in-sensitive

; Define function called hello that writes a string
(deFUN hello()
	(write-line "Hello world!")
)

; Define a main function just cause..
(DEFUN main() 
	(hello)
)

; Call main
(main)
