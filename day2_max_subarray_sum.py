# Problem: Maximum Subarray (LeetCode #53)
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Examples
# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum $= 6$.
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum $= 1$.
# Example 3:
# Input: nums = [5, 4, -1, 7, 8]
# Output: 23
# Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum $= 23$.
# Constraints
# $1 \le \text{nums.length} \le 10^5$
# $-10^4 \le \text{nums}[i] \le 10^4$
# Target Complexity
# Time Complexity: $\mathcal{O}(n)$ — Your solution must traverse the array in a single pass.
# Space Complexity: $\mathcal{O}(1)$ — Do not allocate extra arrays.

#Kadane's Algorithm -- "Is my running sum actually helping me, or is it dragging me down?"

def max_sum_array(nums):
    n = len(nums)
    current_sum = nums[0]
    max_sum = nums[0]
    current_sub = [nums[0]]

    for i in range(1, n ):

        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_sub = [nums[i]]
        
        else:
            current_sum = current_sum + nums[i]
            current_sub.append(nums[i])

        if current_sum > max_sum:
            max_sum = current_sum
            best_sub = list(current_sub)

    return max_sum, best_sub

if __name__ == '__main__':

    nums = list(map(int, input("enter number with comma: ").strip().split()))
    print(nums)

    result = max_sum_array(nums)
    print(result)