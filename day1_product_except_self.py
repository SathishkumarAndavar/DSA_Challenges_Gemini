# Problem: Product of Array Except Self (LeetCode #238)
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The algorithm must run in O(n) time and without using the division operation.
# Examples
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# Example 2:
# Input: nums = [-1, 1, 0, -3, 3]
# Output: [0, 0, 9, 0, 0]

# Constraints
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# Follow-up Challenge: Can you solve the problem with O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

def product_except_self(nums):
    n = len(nums)
    product_array = [1] * n

    prefix = 1
    suffix = 1

    for i in range(n):
        product_array[i] = prefix
        prefix *= nums[i]
        print("prefix loop",product_array[i], prefix, nums[i])

    for i in range(n - 1, -1, -1):
        product_array[i] *= suffix
        suffix *= nums[i]
        print("suffix loop",product_array[i], suffix, prefix, nums[i])

    return product_array

    # Complexity Analysis:
    # Time Complexity: O(n)
    # We iterate through the array twice with two separate loops (one for prefix, one for suffix).
    # This results in O(n) + O(n) = O(2n), which simplifies to O(n).
    # Space Complexity: O(1)
    # The problem states the output array does not count as extra space.
    # We only use a few constant-size variables (prefix, suffix, n, i), so the extra space is O(1).

if __name__ == '__main__':

    nums = list(map(int, input("Enter the array elements separated by space: ").strip().split()))


    result = product_except_self(nums)
    print(result)
