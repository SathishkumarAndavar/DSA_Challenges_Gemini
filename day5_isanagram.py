# """
# Problem: Valid Anagram (LeetCode #242)

# Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`,
# and `False` otherwise.

# An anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: True

# Example 2:
# Input: s = "rat", t = "car"
# Output: False

# Constraints:
# - 1 <= s.length, t.length <= 5 * 10^4
# - s and t consist of lowercase English letters.

# Target Complexity:
# - Time Complexity: O(n) — Single or double pass over strings of length n.
# - Space Complexity: O(1) or O(k) — Where `k` is the alphabet size
#   (at most 26 unique lowercase letters).

# Key Approaches to Consider:
# 1. Sorting Approach:
#    - Sort both strings and check if `sorted(s) == sorted(t)`.
#    - Time Complexity: O(n log n)
#    - Easy to write, but not optimal.

# 2. Frequency Count (Hash Map / Dictionary):
#    - First, check if `len(s) != len(t)`. If lengths differ, return `False`.
#    - Count character occurrences using a Python dictionary or `collections.Counter`.
#    - Compare the character frequencies between `s` and `t`.
# """


#from collections import Counter

# def is_anagram(string1:str, string2:str) -> bool:

#     return Counter(string1) == Counter(string2)

from collections import defaultdict

def is_anagram(string1:str, string2:str) -> bool:

    if len(string1) != len(string2):
        return False

    # dict1 = {}
    # dict2 = {}

    # for char in string1:
    #     dict1[char] = dict1.get(char, 0) + 1

    # for char in string2:
    #     dict2[char] = dict2.get(char, 0) + 1
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for char in string1:
        dict1[char] += 1

    for char in string2:
        dict2[char] += 1

    if dict1 == dict2:

        return True
    else:
        return False

if __name__ == '__main__':

    string1 = input()
    string2 = input()

    result = is_anagram(string1, string2)
    print(result)

# Time Complexity: O(n)
# Space Complexity: O(k), where k is the number of unique characters in the strings

# Python
# # 1. Standard dict with .get()
# dict1[char] = dict1.get(char, 0) + 1

# # 2. defaultdict (Your Refactored Version)
# dict1[char] += 1

# # 3. collections.Counter
# dict1 = Counter(string1)

