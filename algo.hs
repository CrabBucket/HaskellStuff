module Algo where
import qualified Data.Vector as V
linearsearch :: V.Vector (Int) -> Int -> Bool
linearsearch v key
    |V.length v == 1 = V.head v == key
    |otherwise = if key == V.head v
                    then True
                    else linearsearch (V.tail v) key

binarysearch :: V.Vector (Int) -> Int -> Bool
binarysearch v key
    | V.length v == 1 = V.head v == key
    | otherwise = 
        let midpoint = V.length v `div` 2
            elem = (V.!) v midpoint
        in if key < elem 
            then binarysearch (V.take midpoint v) key
            else if key > elem
                then binarysearch (V.drop midpoint v) key
                else True


