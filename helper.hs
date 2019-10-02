module Helper where
import System.CPUTime
toList :: String -> [Int]
toList s = map (read::String->Int)(words s)


maptime :: (a->b) -> [a] -> ([b],IO Integer)
maptime f list = do
    let start = 

