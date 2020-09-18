def search_triplets(arr):
  triplets = set()
  arr.sort()
  
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i - 1]:
      continue

    left = i + 1
    right = len(arr) - 1

    while left < right:
      if arr[i] + arr[left] + arr[right] == 0:
        triplets.add((arr[i], arr[left], arr[right]))
        left += 1
        right -= 1
      elif arr[i] + arr[left] + arr[right] < 0:
        left += 1
      else:
        right -= 1

  return [list(t) for t in triplets]

def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))

main()