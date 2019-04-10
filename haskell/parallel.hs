-- compile with optimization 2, threads and tsopts
-- ghc -O2 --make parallel.hs -threaded -rtsopts
import Control.Parallel
 
main = a `par` b `par` c `pseq` print (a + b + c)
    where
        a = ack 3 10
        b = fac 42
        c = fib 34
 
fac 0 = 1
fac n = n * fac (n-1)
 
ack 0 n = n+1
ack m 0 = ack (m-1) 1
ack m n = ack (m-1) (ack m (n-1))
 
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)