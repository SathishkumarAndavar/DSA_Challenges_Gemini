# Day 12 — Linked List Cycle Detection
# Question

# Given the head of a linked list, determine whether the linked list contains a cycle.

# A cycle exists if a node can be reached again by continuously following the next pointer.

# Example 1:

# 1 → 2 → 3 → 4 → None

# Output:

# False

# Example 2:

# 1 → 2 → 3 → 4
#     ↑       ↓
#     └───────┘

# Output:

# True
# Expected solution

# Use Floyd's Tortoise and Hare algorithm:

# def hasCycle(head):
#     slow = head
#     fast = head

#     while fast and fast.next:

#         slow = slow.next
#         fast = fast.next.next

#         if slow == fast:
#             return True

#     return False
# Complexity
# Complexity	Result	Why
# Time	O(n)	Traverse the linked list using slow/fast pointers
# Space	O(1)	Only slow and fast pointers are used
# Interview explanation

# "I use two pointers, slow and fast. Slow moves one node at a time, while fast moves two nodes. If there is no cycle, fast eventually reaches None. If there is a cycle, fast will eventually catch up with slow, so when slow == fast, I return True. The time complexity is O(n) and space complexity is O(1)."

class linkedlist:

    def __init__(self,val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def createlinklist(nums):

    node = [linkedlist(i) for i in nums]
    
    print([n.val for n in node])

    for i in range(len(nums)):
        if i <  len(nums) -1 and i >=0:

            node[i].next = node[i+1]

        if i > 0:

            node[i].prev = node[i-1]

    node[-1].next = node[0] #to keep cycle, if you want to keep it as a normal linked list, comment this line
    
    return node[0]


def hascyle(head):
    slow = head
    fast = head

    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

if __name__ == '__main__':

    nums = [int(i) for i in input().split()]
    print(nums)

    linklist = createlinklist(nums)
    
    result = hascyle(linklist)

    print(result)
