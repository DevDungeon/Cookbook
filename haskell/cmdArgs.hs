import System.Environment
import Data.List

main = do
     args <- getArgs
     progName <- getProgName
     putStrLn $ head args
