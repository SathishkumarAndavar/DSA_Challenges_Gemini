# Day 16 Problem: Valid Parentheses (LeetCode #20)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:  

# Open brackets must be closed by the same type of brackets.  

# Open brackets must be closed in the correct order.  

# Every close bracket has a corresponding open bracket of the same type.  

# Example 1:  

# Input: s = "()"

# Output: True

# Example 2:  

# Input: s = "()[]{}"

# Output: True

# Example 3:

# Input: s = "(]"

# Output: False

# Example 4:

# Input: s = "([])"

# Output: True

# # Key Intuition: Stack (Last-In, First-Out)
# # Since the most recently opened bracket must be the first one closed, a Stack (Python list) is the perfect data structure here.

# # Create a hash map mapping closing brackets to their matching opening brackets:

# # mapping = {')': '(', '}': '{', ']': '['}

# # Iterate through each character in s:

# # If it's an opening bracket ((, {, [), push it onto the stack (stack.append(char)).

# # If it's a closing bracket:

# # Check if the stack is empty (unmatched closing bracket).

# # Pop the top element from the stack (stack.pop()).

# # If the popped element doesn't match mapping[char], return False.

# # At the end, return True only if the stack is completely empty (len(stack) == 0).



def check_valid(s:str) -> bool:

    stack = []
    mappings = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }

    for char in s:

        if char in "{([":
            stack.append(char)
        
        elif char in "})]":

            if not stack:
                return False

            elif stack[-1] != mappings[char]:
                return False
            
            stack.pop()

    return len(stack) ==0

if __name__ == '__main__':

    s = input("Enter the brackets: ")
    print(s)

    result = check_valid(s)
    print(result)


# Complexity TargetsTime Complexity: 
# $\mathcal{O}(N)$ — Single pass over string length $N$
# Space Complexity: $\mathcal{O}(N)$ — Stack size in worst-case scenario (e.g., "(((((((").
