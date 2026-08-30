
# Execution Trace ExamplesInput (1 2 3 4 5): Middle is index 2 (val 3)
# .Output: 3 4 5Input (1 2 3 4 5 6): Middle is index 3 (val 4, second middle).
# Output: 4 5 6
# Complexity AnalysisTime Complexity: 
# $\mathcal{O}(N)$ — Single pass through the list.
# Space Complexity: $\mathcal{O}(1)$ — Uses constant auxiliary memory.

class linked_list:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createlinkedlist(nums):

    nodes = [linked_list(i) for i in nums]

    for i in range(len(nums) - 1):
        nodes[i].next = nodes[i + 1]

    return nodes[0]


def listflow(head, startpoint):

    current = head
    index = 0

    while current:

        if index >= startpoint:
            print(current.val)

        current = current.next
        index += 1


if __name__ == '__main__':

    nums = [int(i) for i in input().split()]

    linkedlist = createlinkedlist(nums)

    startpoint = 3

    listflow(linkedlist, startpoint)
