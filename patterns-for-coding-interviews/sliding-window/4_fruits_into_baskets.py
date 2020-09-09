"""
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.
"""

import sys
def fruits_into_baskets(fruits):
  maxFruits = -sys.maxsize
  windowStart = 0
  fruitFreq = {}

  for i in range(len(fruits)):
    if fruits[i] not in fruitFreq:
      fruitFreq[fruits[i]] = 0
    fruitFreq[fruits[i]] += 1

    while len(fruitFreq.keys()) > 2:
      if fruitFreq[fruits[windowStart]] == 1:
        del fruitFreq[fruits[windowStart]]
      else:
        fruitFreq[fruits[windowStart]] -= 1
      windowStart += 1

    maxFruits = max(maxFruits, i - windowStart + 1)

  return maxFruits

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()