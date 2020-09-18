def make_squares(arr):
  squares = [0 for i in range(len(arr))]
  left, right = 0, len(arr) - 1
  heightSqureIdx = len(arr) - 1

  while left <= right:
    leftSeqare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSeqare > rightSquare:
      squares[heightSqureIdx] = leftSeqare
      left += 1
    else:
      squares[heightSqureIdx] = rightSquare
      right -= 1
    heightSqureIdx -= 1
  
  return squares

def main():
  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()