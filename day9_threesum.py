
# Problem: 3Sum (LeetCode #15)
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example:
# Input:  nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation: The triplets that sum to zero are (-1, -1, 2) and (-1, 0, 1).


def find_sum_zero(nums: list[int]) -> list[list[int]]:
    # Time Complexity: O(n^2)
    # - Sorting takes O(n log n)
    # - The two-pointer scan for each fixed value takes O(n^2) in total
    # Space Complexity: O(1) auxiliary space
    # - Extra space excluding the output list of triplets
    # - The result list itself uses O(k) space, where k is the number of triplets
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            sum_three = nums[left] + nums[right] + nums[i]

            if sum_three == 0:
                res.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif sum_three < 0:
                left += 1
            else:
                right -= 1

    return res


if __name__ == '__main__':
    nums = [int(i) for i in input().split()]
    print(nums)

    result = find_sum_zero(nums)
    print(result)

