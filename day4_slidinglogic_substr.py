# """
# Problem: Longest Substring Without Repeating Characters (LeetCode #3)

# Given a string `s`, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note: "pwke" is a subsequence and not a substring, because the characters must be contiguous.

# Constraints:
# - 0 <= s.length <= 5 * 10^4
# - s consists of English letters, digits, symbols, and spaces.

# Target Complexity:
# - Time Complexity: O(n) — Process each character at most twice.
# - Space Complexity: O(k) — Where `k` is the size of the character set
#   (at most O(1) space since the ASCII set is capped at 128 characters).

# Key Intuition: Sliding Window
# Think of a sliding window `[left ... right]` over the string:
# - Move `right` forward one step at a time to expand the window.
# - Store visited characters in a `set()` or `dict()`.
# - If `s[right]` is already in the set (a duplicate), shrink the window from the left
#   by moving `left` forward and removing `s[left]` from the set until the duplicate is gone.
# - Update `max_len` at each valid step.
# """
#20-Aug-2026

def all_longest_unique_substrings(string):
    substring = ""
    max_len = 0
    longest_set = set()

    for char in string:
        while char in substring:
            substring = substring[1:]
        substring += char

        # Case A: Found a NEW strictly longer substring -> Reset tracker
        if len(substring) > max_len:
            max_len = len(substring)
            longest_set = {substring}

        # Case B: Tied for max length -> Add to tracker
        elif len(substring) == max_len:
            longest_set.add(substring)

    return list(longest_set), max_len


# Example run: "pwwkew"
# "pwe", "wke", "kew" all have length 3!
print(all_longest_unique_substrings("pwwkew"))
# Output: (['pwe', 'wke', 'kew'], 3)

# Time Complexity: O(n)
# Space Complexity: O(k), where k is the size of the character set
