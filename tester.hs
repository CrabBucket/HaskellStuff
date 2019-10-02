import Algo
import qualified Data.Vector as V
import System.Random
import Data.Sort
import Control.DeepSeq
import Control.Exception
import System.CPUTime
import System.IO
main = do
    putStr "Input Size:"
    hFlush stdout
    input <- readLn
    putStr "Average Over:"
    hFlush stdout
    trials <- readLn :: IO Int
    gen <-getStdGen
    let maxkey = take trials [5000,5000..]
    let rands = take input (randomRs (-1000,1000) gen)::[Int]
    let sortedlist = sort (rands)::[Int]
    let randkey = take trials (randomRs (-1000,1000) gen)::[Int]
    vector <- evaluate $ force (V.fromList sortedlist)
    start <- getCPUTime
    bool <- evaluate $ force (map (binarysearch vector) randkey)
    evaluate(rnf bool)
    end <- getCPUTime
    putStr (show (cpuTimePrecision))


    let time1 = (end - start) `div` fromIntegral trials

    start <- getCPUTime
    --bool <- evaluate $ force (map (linearsearch vector) maxkey)
    end <- getCPUTime

    let time2 = (end - start) `div` fromIntegral (trials * (10^6))
    putStrLn (show bool)
    putStrLn ("Binary Search Average run time over " ++ show(trials) ++ " lists:" ++ (show time1) ++ " 10^-12 seconds vs Linear Search Average Runtime over " ++ show(trials) ++ " lists:" ++ (show time2) ++ " 10^-6 seconds")