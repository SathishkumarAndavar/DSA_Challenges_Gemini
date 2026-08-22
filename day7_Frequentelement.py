# """
# Problem: Top K Frequent Elements (LeetCode #347)

# Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.
# You may return the answer in any order.

# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Explanation:
# - 1 appears 3 times
# - 2 appears 2 times
# - 3 appears 1 time

# The 2 most frequent elements are 1 and 2.

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
# - k is in the range [1, number of unique elements in the array]
# - It is guaranteed that the answer is unique.

# Key Intuition & Hints:
# Step 1: Frequency Count
# First, count how many times each number appears using a Hash Map
# (`Counter` or `defaultdict`).

# Step 2: Selection Strategy
# Sorting Approach:
# - Sort the unique numbers by their counts.
# - Complexity: O(N log N) or O(U log U), where U is the number of unique elements.

# Bucket Sort Approach (Optimal O(N)):
# - Create an array of buckets where the index represents the frequency count.
# - Each bucket holds a list of numbers that appear that many times.
# """

def find_top2repat(nums, k=2):

    dict1 = {}

    for i in nums:
        dict1[i] = dict1.get(i,0) + 1

    print(dict1)


    return [num for num, count in sorted(dict1.items(),key = lambda item:item[1], reverse=True)[:2]]

if __name__ == '__main__':

    nums = list(map(int, (i for i in input().split())))
    print(nums)

    result = find_top2repat(nums, k=2)
    print(result)

# Complexity Analysis:
# Time Complexity: O(U log U)
# - U is the number of unique elements.
# - Building the frequency map takes O(N).
# - Sorting the unique items by frequency takes O(U log U).
#
# Space Complexity: O(U)
# - The hash map stores one frequency count for each unique element.