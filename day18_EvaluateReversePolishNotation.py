# Welcome to **Day 18 of 30**!

# Today we continue with the **Stacks & Queues** module by covering a fundamental evaluation problem that comes up constantly in technical interviews: **Evaluate Reverse Polish Notation**.

# ---

# ### Day 18 Problem: Evaluate Reverse Polish Notation (LeetCode #150)

# You are given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation** (Postfix Notation).

# Evaluate the expression and return an integer that represents the value of the expression.

# **Rules:**

# * The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
# * Each operand may be an integer or another expression.
# * The division between two integers always **truncates toward zero** (e.g., `int(a / b)` in Python).
# * There will not be any division by zero.
# * The input represents a valid arithmetic expression.
# * **Example 1:**
# * **Input:** `tokens = ["2","1","+","3","*"]`
# * **Output:** `9`
# * **Explanation:** `((2 + 1) * 3) = 9`


# * **Example 2:**
# * **Input:** `tokens = ["4","13","5","/","+"]`
# * **Output:** `6`
# * **Explanation:** `(4 + (13 / 5)) = 6`


# * **Example 3:**
# * **Input:** `tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]`
# * **Output:** `22`



# ---

# ### Key Intuition: Stack Evaluation

# In Postfix notation, operators follow their operands. A stack makes evaluating this straightforward:

# 1. Iterate through `tokens` left to right.
# 2. If the token is a **number**, convert it to an integer and push it onto the stack.
# 3. If the token is an **operator** (`+`, `-`, `*`, `/`):
# * Pop the second operand (`b = stack.pop()`).
# * Pop the first operand (`a = stack.pop()`).
# * Perform `a operator b` and push the result back onto the stack.
# * *Note for Division:* Use `int(a / b)` in Python to ensure truncation toward zero (standard integer division `a // b` rounds down towards $-\infty$, which causes bugs for negative numbers like `-3 // 2 = -2`).


# 4. At the end, the stack will contain exactly one element—the final result!

# ---

### Starter Python Template


def calcul(list1):

  stack = []

  for i in list1:
    if i in '+-/*':
      b = stack.pop()
      a = stack.pop()

      if i == '+':
        stack.append(a+b)
      elif i == '-':
        stack.append(a-b)
      elif i == "*":
        stack.append(a * b)
      elif i == "/":
                # int(a / b) truncates toward zero (e.g., int(-3 / 2) -> -1)
        stack.append(int(a / b))
    else:
      stack.append(int(i))

    print(stack)
      

  return stack[0]

if __name__ == '__main__':

  list1 = [i for i in input().split()]
  print(list1)

  result = calcul(list1)
  print(result)


# ---

# ### Complexity Targets

# * **Time Complexity:** $\mathcal{O}(N)$ — Single pass through the `tokens` array of length $N$.
# * **Space Complexity:** $\mathcal{O}(N)$ — Stack space to hold up to $N$ numbers in the worst case.

# Give it a try in your Python environment and share your code when you're ready!