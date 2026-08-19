# Problem: Maximum Subarray (LeetCode #53)
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Examples
# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6.
# Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum = 1.
# Example 3:
# Input: nums = [5, 4, -1, 7, 8]
# Output: 23
# Explanation: The subarray [5, 4, -1, 7, 8] has the largest sum = 23.
# Constraints
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# Target Complexity
# Time Complexity: O(n) — Your solution must traverse the array in a single pass.
# Space Complexity: O(1) — Do not allocate extra arrays.

#Kadane's Algorithm -- "Is my running sum actually helping me, or is it dragging me down?"

def max_sum_array(nums):
    if not nums:
        return 0, []

    max_so_far = nums[0]
    current_max = nums[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        num = nums[i]
        # If the current number is greater than the running sum plus the current number,
        # it's better to start a new subarray from the current number.
        if num > current_max + num:
            current_max = num
            temp_start = i
        else:
            # Otherwise, extend the current subarray.
            current_max += num

        # If the sum of the current subarray is the best we've seen so far, update our answer.
        if current_max > max_so_far:
            max_so_far = current_max
            start = temp_start
            end = i

    return max_so_far, nums[start:end+1]

    # Complexity Analysis:
    # Time Complexity: O(n)
    # The algorithm iterates through the input array `nums` exactly once with a single for loop.
    # All operations inside the loop are constant time, O(1). Thus, the total time complexity is O(n).
    # Space Complexity: O(1)
    # The algorithm uses a fixed number of variables (max_so_far, current_max, start, end, etc.)
    # regardless of the size of the input array. No additional data structures that scale with n are used.

if __name__ == '__main__':
    nums_str = input("Enter the array elements separated by space: ").strip().split()
    nums = [int(n) for n in nums_str if n] # Handle multiple spaces between numbers
    max_sum, subarray = max_sum_array(nums)
    print(f"Maximum subarray sum: {max_sum}")
    print(f"Subarray with the largest sum: {subarray}")