import Data.IntMap.Strict qualified as IntMap
import Data.List (group, sort)

parse :: String -> ([Int], [Int])
parse = unzip . map (toTuple . map read . words) . lines
 where
  toTuple [a, b] = (a, b)

solve1 :: ([Int], [Int]) -> Int
solve1 =
  sum . compareLists . sortFstAndSnd
 where
  sortFstAndSnd (a, b) = (sort a, sort b)
  compareLists (a, b) = zipWith (\m n -> abs (m - n)) a b

solve2 :: ([Int], [Int]) -> Int
solve2 (xs, ys) = undefined

main :: IO ()
main = do
  input <- readFile "input"
  let parsedInput = parse input
  print . solve1 $ parsedInput
  print . solve2 $ parsedInput
