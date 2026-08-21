# """
# Problem: Group Anagrams (LeetCode #49)

# Given an array of strings `strs`, group the anagrams together.
# You can return the answer in any order.

# An anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# - 1 <= strs.length <= 10^4
# - 0 <= strs[i].length <= 100
# - strs[i] consists of lowercase English letters.

# Key Intuition: The Hash Key Trick
# To group anagrams together, you need a way to assign the same key to words that are
# anagrams of each other.

# There are two common ways to create this key:

# 1. Sorted String as Key:
#    - Sorting "eat", "tea", and "ate" all yield "aet".
#    - Map: "aet" -> ["eat", "tea", "ate"]
#    - Complexity: O(N * K log K), where N is the number of strings and K is the
#      maximum length of a string.

# 2. Character Count Tuple as Key (Optimal):
#    - Build a frequency array of size 26 for each word.
#    - Convert the array into a tuple, since tuples are hashable in Python and can
#      be used as dictionary keys.
#    - Complexity: O(N * K) time.
# """


from collections import Counter, defaultdict

# def is_anagram(string1:str, string2:str) -> bool:

#     return Counter(string1) == Counter(string2)


def anagram_grp(list_str):

    dict1 = defaultdict(list)

    for i in list_str:

        sorted_keys = ''.join(sorted(i))
        
        dict1[sorted_keys].append(i)

        print(dict1)


    return list(sorted(dict1.values(), key = len,reverse=True))

if __name__ == '__main__':

    #string1 = input()
    #string2 = input()
    #strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    list_str = [i for i in input("").strip().split()]
    print(list_str)
    result = anagram_grp(list_str)
    print(result)
    #result = is_anagram(string1, string2)
    #print(result)


# Complexity Analysis:
# - Time Complexity: O(N * K log K)
#   where N is the number of strings and K is the maximum length of a string.
#   This is because each word is sorted using Python's Timsort.
#
# - Space Complexity: O(N * K)
#   because all grouped strings are stored in the dictionary.
#
# Step-by-step breakdown:
# 1. Outer loop runs N times.
# 2. Sorting a single word of length K takes O(K log K).
# 3. Joining the sorted characters back into a string takes O(K).
# 4. So each word costs O(K log K), and across all words the total is:
#    O(N * K log K).
#
# Pro-tip for optimization:
# To remove the log K factor, use a 26-size frequency array as the key instead of
# sorting the string. Then each word can be hashed in O(K) time, giving:
# O(N * K) total time.
#
# Example:
# count = [0] * 26
# for char in word:
#     count[ord(char) - ord('a')] += 1
#
# dict1[tuple(count)].append(word)