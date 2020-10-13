def find_permutations(nums):
  result = []
  queue = [[]]

  for num in nums:
    n = len(queue)
    for _ in range(n):
      oldPermutation = queue.pop(0)
      for i in range(len(oldPermutation) + 1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(i, num)
        if len(newPermutation) == len(nums):
          result.append(newPermutation)
        else:
          queue.append(newPermutation)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()
