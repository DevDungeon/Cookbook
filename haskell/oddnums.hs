--main = go 0
	--where
--		go :: Int -> IO ()
		--go i | i < 100 = go (i+1)
--			| otherwise = return()


checkOdd :: Int -> Int
checkOdd n = print(n)

main = do
	print(checkOdd(2))
