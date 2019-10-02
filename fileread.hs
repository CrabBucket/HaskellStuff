import Algo
import qualified Data.Vector as V
import System.Random
import Data.Sort
import Control.DeepSeq
import Control.Exception
import System.CPUTime
main = do
    withFile "inputs.data" ReadMode (\handle -> do
        --Seed
    gen <-getStdGen

        --Gets the contents of the file as a string binds it to raw

    raw <- hGetContents handle

        -- We map the string words to their read values as ints this our list of inputs

    let inputs = map (read::String->Int)(words raw)

        -- we map our take such that we create a list of lists of random ints from -1000 to 1000 of varying sizes of varying sizes

    let rands = map (\input -> take input (randomRs (-1000,1000) gen)::[Int])

        --We now map sort to all the lists in rands so that we can get a sorted list of random numbers to perform our search algorithm on
        -- we then map all those lists of sorted random ints into a list of vectors containing the same 

    vectors <- evaluate $ force $ map (V.fromList) (map sort rands)

        -- we map evaluate to all the vectors we just made

    

        --I know I need some kind of double mapping because now I have two dimensions I need iterate/map over our list of vectors. 
        --And our list of random keys, which I just realized isn't yet defined but we can get one from rands using like rands !! 1

    

        --I now think I need to define my own map function that maps and also after its maps then evals then  returns what time it finished
        -- by spitting out a tuple that contains both the CPUTime at completion and our list of bools i think
    putStrLn "test"

    )
    -- input <- readLn
    -- gen <-getStdGen
    -- let rands = take input (randomRs (-1000,1000) gen)::[Int]
    -- let sortedlist = sort (rands)::[Int]
    -- --let randkey = take input (randomRs (-1000,1000) gen)::[Int]
    -- let vector = V.fromList sortedlist
    -- evaluate(rnf vector)
    -- start <- getCPUTime
    -- let bool = map (binarysearch vector) rands
    -- evaluate(rnf bool)
    -- end <- getCPUTime
    -- putStrLn (show ((end - start) `div` (10^3)))