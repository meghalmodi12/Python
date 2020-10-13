def find_subsets(nums):
  subsets = [[]]

  for num in nums:
    for i in range(len(subsets)):
      newSet = list(subsets[i])
      newSet.append(num)
      subsets.append(newSet)

  return subsets


def main():
  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))

main()
