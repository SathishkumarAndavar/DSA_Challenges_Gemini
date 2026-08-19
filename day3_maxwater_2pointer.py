# """
# Day 3: Container With Most Water (LeetCode #11)

# Problem:
# You are given an integer array `height` of length `n`.

# There are `n` vertical lines drawn such that the two endpoints of the `i`th line are
# `(i, 0)` and `(i, height[i])`. Find two lines that, together with the x-axis,
# form a container that holds the most water. Return the maximum amount of water
# that can be stored.

# Note:
# You may not slant the container.

# Example 1:
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49

# Explanation:
# The maximum area is between index 1 and index 8.
# Area = width * min(height[1], height[8])
#      = (8 - 1) * min(8, 7)
#      = 7 * 7
#      = 49

# Example 2:
# Input: height = [1, 1]
# Output: 1

# Constraints:
# - `n == height.length`
# - `2 <= n <= 10^5`
# - `0 <= height[i] <= 10^4`

# Target Complexity:
# - Time: O(n)
# - Space: O(1)
# """

def max_area(height):

    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:

        current_water = (right - left) * min(height[right],height[left])

        max_water = max(current_water, max_water)

        if height[left] > height[right]:

            right = right - 1
        
        else:
            left = left + 1


    return max_water


if __name__ == "__main__":

    nums = input("Enter the heights of the lines separated by spaces: ")
    nums = [int(num) for num in nums.split()]

    print("Heights of the lines:", nums)

    result = max_area(nums)
    print("Maximum area of water that can be stored:", result)

# Time Complexity: O(n)
# Space Complexity: O(1)

