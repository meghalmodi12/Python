class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def check_if_palindrome(head):
    slow, fast = head, head
    elements = []

    while fast is not None and fast.next is not None:
        elements.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        elements.append(slow.value)

    while slow is not None:
        if slow.value != elements.pop():
            return False
        slow = slow.next

    return True

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(check_if_palindrome(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(check_if_palindrome(head)))

main()