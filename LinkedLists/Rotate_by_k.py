""" AirBNB:

Given a linked list and a number k, rotate the linked list by k places.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        current = self
        ret = ''
        while current:
            ret += str(current.value)
            current = current.next
        return ret


def rotate_list(list, k):
    if not list:
        return None

    lastElement = list
    length = 1

    while lastElement.next:
        lastElement = lastElement.next
        length += 1

    k = k % length

    lastElement.next = list

    temp = list
    for _ in range(length - k - 1):
        temp = temp.next

    ans = temp.next
    temp.next = None

    return ans


# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
