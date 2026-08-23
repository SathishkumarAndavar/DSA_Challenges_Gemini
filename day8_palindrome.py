# """
# Problem: Valid Palindrome II (LeetCode #680)

# Given a string `s`, return `True` if the string can be a palindrome after deleting
# at most one character from it.

# A palindrome is a word, phrase, or sequence that reads the same backward as forward.

# Example 1:
# Input: s = "aba"
# Output: True

# Example 2:
# Input: s = "abca"
# Output: True
# Explanation:
# You could delete the character 'c' to get "aba", or delete 'b' to get "aca".

# Example 3:
# Input: s = "abc"
# Output: False
# Explanation:
# Deleting any single character will not make it a palindrome.

# Constraints:
# - 1 <= s.length <= 10^5
# - s consists of lowercase English letters.

# Key Intuition & Hints:
# - Two Pointers: Start with a pointer at the beginning (`left = 0`) and
#   the end (`right = len(s) - 1`).
# - Matching Characters: While `s[left] == s[right]`, increment `left` and
#   decrement `right`.
# - First Mismatch: When `s[left] != s[right]`, you have two choices:
#   - Skip the left character and check whether
#     `s[left + 1 : right + 1]` is a palindrome.
#   - Skip the right character and check whether
#     `s[left : right]` is a palindrome.
# - Helper Function: Write a small helper function `is_palindrome(sub_str)`
#   that checks if a string is a normal palindrome.
# """

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

def valid_palindrome(string):

    def is_palindrome(string):
        return string == string[::-1]


    left, right = 0,len(string)-1
    while left < right:
        if string[left] == string[right]:
            left +=1
            right -=1 
        
        else:
            return is_palindrome(string[left+1:right+1]) or is_palindrome(string[left:right])

    
    return True

if __name__ == '__main__':

    string = input().strip()
    print(string)

    result = valid_palindrome(string)
    print(result)

# Time Complexity: O(n)
# - The two-pointer scan moves inward at most once.
# - Each palindrome check on the remaining substring is at most O(n),
#   and only one of the two checks is needed after the mismatch.
#
# Space Complexity: O(1)
# - Only a few pointer variables are used.
# - The helper uses sliced strings, which creates new substrings, so the practical
#   extra memory is still O(n) in the worst case for the substring copies.


