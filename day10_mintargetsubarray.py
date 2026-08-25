# high-frequency Two Pointers problem to cap off this section!

# Problem: Minimum Size Subarray Sum (LeetCode #209)
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.  

# Examples  
# Example 1:  
# Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
# Output: 2

# Explanation: The subarray [4, 3] has the minimal length under the problem constraint with sum = 7 >= 7.  

# Example 2:
# Input: target = 4, nums = [1, 4, 4]
# Output: 1
# Explanation: The subarray [4] has length 1.

# Example 3:
# Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
# Output: 0

# Explanation: No valid subarray sums up to 11.
# Key Intuition: Sliding Window (Two Pointers)
# Use two pointers, left and right, to define a moving window.

# Expand the window by adding nums[right] to current_sum.

# While current_sum >= target:

# Update your minimum length found so far (right - left + 1).

# Shrink the window from the left by subtracting nums[left] and incrementing left.

def min_target_subarray(nums, target):

    if sum(nums) < target:
        return 0, []
    
    left = 0
    min_len = float('inf')
    min_sub = []
    current_sum = 0

    best_start, best_end = -1,-1


    for right in range(len(nums)):

        current_sum +=nums[right]

        while current_sum >= target:

            if min_len >  right - left + 1:
                min_len = right - left + 1
                best_start = left
                best_end = right
            
            current_sum -= nums[left]
            left += 1

    min_sub = nums[best_start:best_end+1]
    
    return min_len, min_sub

if __name__ == '__main__':

    nums = [int(i) for i in input().split()]
    print(nums)

    target = 10

    result=min_target_subarray(nums, target)
    print(result)

#Execution Walkthrough (nums = [2, 3, 1, 2, 4, 3], target = 10)Sum check: sum(nums) = 15 >= 10 $\rightarrow$ Proceed.Window Expansion (right = 0 to 3): current_sum = 2 + 3 + 1 + 2 = 8 ($< 10$).right = 4 (nums[4] = 4): current_sum = 12 ($\ge 10$).min_len updated to 5 (best_start = 0, best_end = 4). Subarray: [2, 3, 1, 2, 4].Shrink left: current_sum drops to 10 ($\ge 10$).min_len updated to 4 (best_start = 1, best_end = 4). Subarray: [3, 1, 2, 4].Shrink left: current_sum drops to 7 ($< 10$).right = 5 (nums[5] = 3): current_sum = 7 + 3 = 10 ($\ge 10$).Shrink left: current_sum drops to 9 ($< 10$).min_len updated to 4 (best_start = 2, best_end = 5). Subarray: [1, 2, 4, 3].Final Output: (4, [3, 1, 2, 4])

# Performance SummaryTime Complexity: $\mathcal{O}(N)$ — The sum(nums) check takes $\mathcal{O}(N)$, and the sliding window takes $\mathcal{O}(N)$. Slicing happens once at the end in $\mathcal{O}(\text{min\_len})$ time.Space Complexity: $\mathcal{O}(\text{min\_len})$ — Only stores the single sliced subarray at the very end.
