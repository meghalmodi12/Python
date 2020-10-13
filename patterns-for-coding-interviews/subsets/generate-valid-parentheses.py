class ParanthesesString:
  def __init__(self, data, openCount, closeCount):
    self.data = data
    self.openCount = openCount
    self.closeCount = closeCount

def generate_valid_parentheses(num):
  result = []
  queue = [ParanthesesString([], 0, 0)]

  while queue:
    ps = queue.pop(0)
    if ps.openCount == num and ps.closeCount == num:
      result.append("".join(ps.data))
    else:
      if ps.openCount < num:
        newData = list(ps.data)
        newData.append('(')
        queue.append(ParanthesesString(newData, ps.openCount + 1, ps.closeCount))
      if ps.openCount > ps.closeCount:
        newData = list(ps.data)
        newData.append(')')
        queue.append(ParanthesesString(newData, ps.openCount, ps.closeCount + 1))

  return result

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()