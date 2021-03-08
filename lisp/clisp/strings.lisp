; Simple string var and write-line call
(setq str "test string")
(write-line str)

; format text ~% is like a \n. ~d and ~s are %d %s printf equivs 
(format t "Hello, world. ~d ~s ~%" 10 str)
