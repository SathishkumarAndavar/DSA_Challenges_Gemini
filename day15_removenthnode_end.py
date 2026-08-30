# Day 15 Problem: Remove Nth Node From End of List (LeetCode #19)
# Given the head of a linked list, remove the $n$-th node from the end of the list and return its head.
# Example 1:Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5] (Node with value 4 is removed)
# Example 2:Input: head = [1], n = 1
# Output: []
# Example 3:Input: head = [1, 2], n = 1
# Output: [1]
# Key Intuition: Two-Pointer Offset Strategy (One-Pass)
# While you could count the total length first and make two passes, you can solve this in a single pass using a fast and slow pointer with an $n$-node gap:
# Dummy Node: Place a dummy node before head to handle edge cases like removing the very first element (head itself).
# Create the Gap: Advance the fast pointer $n + 1$ steps ahead so that the distance between fast and slow is exactly $n$ nodes.
# Move Together: Advance both fast and slow one step at a time until fast hits None.Remove Node: slow will now sit right before the node to be deleted! Update slow.next = slow.next.next.


class linked_list:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createlinkedist(list1):
    if not list1:
        return None

    nodes = [linked_list(i) for i in list1]
    for i in range(len(list1) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]


def remove_nnode(head, n):
    dummy = linked_list(-1)
    dummy.next = head

    slow = dummy
    fast = dummy

    # 1. Advance fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next

    # 2. Move fast to the last node while maintaining the n-node gap
    while fast.next:
        slow = slow.next
        fast = fast.next

    # 3. Bypass the target node
    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    list1 = [int(i) for i in input("list1: ").split()]

    nodeinklist = createlinkedist(list1)

    # Removing 2nd node from end as a standard test
    result = remove_nnode(nodeinklist, 2)

    print("Result:", end=" ")
    while result:
        print(result.val, end=" ")
        result = result.next
    print()

# Complexity AnalysisTime Complexity: 
# $\mathcal{O}(N)$The fast pointer traverses the list of length $N$ exactly once.
# Space Complexity: $\mathcal{O}(1)$The operation modifies pointers in-place, using only dummy, slow, and fast pointers.
