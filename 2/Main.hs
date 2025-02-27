parse :: String -> [[Int]]
parse = map (map read . words) . lines

data Trend = Inc | Dec deriving (Eq)

solve1 :: [[Int]] -> Int
solve1 reports =
  let
    solveReport :: [Int] -> Maybe Int -> Maybe Trend -> Int
    solveReport [] _ _ = 1
    solveReport (x1 : x2 : xs) Nothing Nothing =
      case x1 `compare` x2 of
        LT -> if abs (x1 - x2) <= 3 then solveReport xs (Just x2) (Just Inc) else 0
        EQ -> 0
        GT -> if abs (x1 - x2) <= 3 then solveReport xs (Just x2) (Just Dec) else 0
    solveReport (x : xs) (Just y) (Just trend) =
      case y `compare` x of
        LT -> if abs (x - y) <= 3 && trend == Inc then solveReport xs (Just x) (Just Inc) else 0
        EQ -> 0
        GT -> if abs (x - y) <= 3 && trend == Dec then solveReport xs (Just x) (Just Dec) else 0
   in
    sum $ map (\report -> solveReport report Nothing Nothing) reports

main :: IO ()
main = do
  input <- readFile "input"
  let parsedInput = parse input
  print $ solve1 parsedInput
