# Day 14 Problem: Merge Two Sorted Lists (LeetCode #21)
# Given the heads of two sorted linked lists list1 and list2, 
# merge the two lists into a single sorted linked list by splicing together the existing nodes, and return its head.Input: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
# Complexity AnalysisTime Complexity: 
# $\mathcal{O}(N + M)$Where $N$ is the number of nodes in list1 and $M$ is the number of nodes in list2. The while loop runs at most $N + M$ times, processing one node per step in constant time $\mathcal{O}(1)$.
# Space Complexity: $\mathcal{O}(1)$The algorithm merges the lists in-place by rewiring the existing next pointers. Apart from the single dummy reference node and pointer variables (curr, current, current2), no additional heap memory or dynamic data structures are created.
                                        
class linked_list:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createlinkedist(list1, list2):

    nodeinklist1 = [linked_list(i) for i in list1]
    nodeinklist2 = [linked_list(i) for i in list2]

    for i in range(len(list1) - 1):
        nodeinklist1[i].next = nodeinklist1[i + 1]

    for j in range(len(list2) - 1):
        nodeinklist2[j].next = nodeinklist2[j + 1]

    return nodeinklist1[0], nodeinklist2[0]


def sorted_linkedlist(head):

    dummy = linked_list(-1)

    current = head[0]
    current2 = head[1]

    curr = dummy

    while current and current2:

        if current.val <= current2.val:

            curr.next = current
            curr = curr.next
            current = current.next

        else:

            curr.next = current2
            curr = curr.next
            current2 = current2.next

    curr.next = current if current else current2
    
    return dummy.next


if __name__ == '__main__':

    list1 = [int(i) for i in input("list1: ").split()]
    list2 = [int(i) for i in input("list2: ").split()]

    nodeinklist = createlinkedist(list1, list2)

    sort_merge_list = sorted_linkedlist(nodeinklist)

    while sort_merge_list:

        print(sort_merge_list.val)

        sort_merge_list = sort_merge_list.next

