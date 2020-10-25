def find_subsets_duplicates(nums):
  subsets = [[]]
  nums.sort()
  startIdx, endIdx = 0, 0

  for i in range(len(nums)):
    startIdx = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIdx = endIdx
    endIdx = len(subsets)

    for j in range(startIdx, endIdx):
      newSet = list(subsets[j])
      newSet.append(nums[i])
      subsets.append(newSet)

  return subsets 


def main():
  print("Here is the list of subsets: " + str(find_subsets_duplicates([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets_duplicates([1, 5, 3, 3])))

main()
