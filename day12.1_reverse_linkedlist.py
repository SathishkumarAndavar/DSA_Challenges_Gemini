# Day 12 Problem: Reverse Linked List (LeetCode #206)
# Given the head of a singly linked list, reverse the list and return its new head.Input: head of a linked list (e.g., 1 -> 2 -> 3 -> 4 -> 5 -> None)
# Output: The head of the reversed list (e.g., 5 -> 4 -> 3 -> 2 -> 1 -> None)
# Complexity AnalysisTime
#  Complexity: $\mathcal{O}(N)$The algorithm traverses the linked list of $N$ nodes exactly once. For each node, pointer reassignment is done in constant time $\mathcal{O}(1)$.
# Space Complexity: $\mathcal{O}(1)$The list is reversed in-place using three pointer variables (previous, current, next_node). No extra memory or dynamic arrays are allocated, resulting in constant auxiliary space.

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

def reverselinklist(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev

        prev = current
        current = next_node

    return prev
        
       

if __name__ == '__main__':

    nums = [int(i) for i in input().split()]
    print(nums)

    linklist = createlinklist(nums)
    
    result = hascyle(linklist)

    result1 = reverselinklist(linklist)
    print(result1)
    current = result1

    while current:
        print(current.val, end="\n")
        current = current.next

    print(result)


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# class linkedlist:

#     def __init__(self,val=0, next=None):
#         self.val = val
#         self.next = next

# def createlinkedlist(nums):

#     nodes = [linkedlist(i) for i in nums]

#     for i in range(len(nums)-1):

#         nodes[i].next = nodes[i+1]
    
#     return nodes[0]

# def reveresedlist(head):

#     previous = None
#     current = head
#     while current:

#         next_node = current.next
#         current.next = previous
#         previous = current
#         current = next_node
#     return previous


# if __name__ == '__main__':

#     nums = [i for i in input().split()]

#     print(nums)

#     requiredlinkedlist = createlinkedlist(nums)
#     result = reveresedlist(requiredlinkedlist)

#     while result:
#         print(result.val, end = " ")
#         result = result.next



