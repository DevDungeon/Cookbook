(setq x 1.5)

(loop while (<= x 10) do
	(print x)
	(setq x (+ x 1))
)

(write-line "Completed")
