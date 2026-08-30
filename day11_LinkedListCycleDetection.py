
# Day 11 Problem: Linked List Cycle (LeetCode #141)
# Given head, the head of a singly linked list, determine if the linked list contains a cycle.

# A cycle exists if there is a node in the list that can be reached again by continuously following the next pointer.

# Input: head of a linked list (e.g., 3 -> 2 -> 0 -> -4 where -4 points back to 2)

# Output: True if a cycle exists, False otherwise.

class listnode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hascycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next  # Move slow 1 step
        fast = fast.next.next  # Move fast 2 steps

        if slow == fast:
            print(f"Matches at node value: {slow.val}")
            return True

        print(f"slow: {slow.val}, fast: {fast.val}")

    return False


if __name__ == "__main__":
    node1 = listnode(3)
    node2 = listnode(2)
    node3 = listnode(0)
    node4 = listnode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1  # Creates cycle back to start

    print("Has Cycle:", hascycle(node1))

# Complexity AnalysisTime Complexity: $\mathcal{O}(N)$No Cycle Case: fast reaches the end (None) in $N/2$ steps, taking linear time proportional to the number of nodes $N$.Cycle Case: Once slow enters the cycle of length $K$, fast reduces the gap between them by 1 step every iteration. fast catches slow in at most $K$ steps. Thus, the total iterations remain $\mathcal{O}(N)$.Space Complexity: $\mathcal{O}(1)$The algorithm only allocates two pointer variables (slow and fast). No extra memory or additional data structures (like sets or hashes) are created, resulting in constant auxiliary space