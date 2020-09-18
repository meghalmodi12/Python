import sys
def triplet_sum_close_to_target(arr, target_sum):
  tempResult = sys.maxsize
  arr.sort()

  for i in range(len(arr)):
    left = i + 1
    right = len(arr) - 1

    while left < right:
      tempSum = arr[i] + arr[left] + arr[right]
      if tempSum - target_sum == 0:
        return tempSum
      if abs(target_sum - tempSum) < tempResult:
        tempResult = abs(target_sum - tempSum)
      if tempSum < target_sum:
        left += 1
      else:
        right -= 1

  return target_sum - tempResult

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))

main()