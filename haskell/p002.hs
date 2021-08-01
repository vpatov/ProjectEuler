slice :: Int -> Int -> [a] -> [a]
slice from to xs = take (to - from + 1) (drop from xs)
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)
fib n = fibs !! n
solution = print(sum [x | x <- slice 0 1000 fibs, even x && x < 4000000])