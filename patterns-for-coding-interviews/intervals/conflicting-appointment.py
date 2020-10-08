def can_attend_all_appointments(intervals):
  start, end = 0, 1
  intervals.sort(key = lambda x: x[start])

  stack = [intervals[0]]
  for i in range(1, len(intervals)):
    if intervals[i][start] < stack[-1][end]:
      return False
    else:
      stack.append(intervals[i])

  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()