def search_quadruplets(arr, target):
  quadruplets = set()
  arr.sort()

  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      left = j + 1
      right = len(arr) - 1

      while left < right:
        if arr[i] + arr[j] + arr[left] + arr[right] == target:
          quadruplets.add((arr[i], arr[j], arr[left], arr[right]))
          left += 1
          right -= 1
        elif arr[i] + arr[j] + arr[left] + arr[right] < target:
          left += 1
        else:
          right -= 1
  
  return [list(q) for q in quadruplets]

def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

main()