"""
Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates in-place return the new length of the array.
"""
def remove_duplicates(arr):
  result = []
  nextNonDuplicate, nextItem = 1, 1

  while nextItem < len(arr):
    if arr[nextNonDuplicate - 1] != arr[nextItem]:
      arr[nextNonDuplicate] = arr[nextItem]
      nextNonDuplicate += 1
    nextItem += 1

  for i in range(nextNonDuplicate):
    result.append(arr[i])

  return result

def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))

main()