
import System.Environment (getArgs)

main = do
	[inpFile] <- getArgs
	input <- readFile inpFile
	let thelines = lines input
	let thewords = words $ thelines !! 0
	mapM_ putStrLn $ thewords


