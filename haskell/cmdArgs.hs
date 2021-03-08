import System.Environment


main = do
     args <- getArgs
     putStrLn $ head args
