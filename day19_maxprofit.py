# Welcome to **Day 19 of 30**!

# Today we transition into a foundational algorithmic pattern: **Sliding Window & Two Pointers**. We start with a classic sliding window question: **Best Time to Buy and Sell Stock**.

# ---

# ### Day 19 Problem: Best Time to Buy and Sell Stock (LeetCode #121)

# You are given an array `prices` where `prices[i]` is the price of a given stock on the $i$-th day.

# You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

# Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

# * **Example 1:**
# * **Input:** `prices = [7, 1, 5, 3, 6, 4]`
# * **Output:** `5`
# * **Explanation:** Buy on day 2 (`price = 1`) and sell on day 5 (`price = 6`), $\text{profit} = 6 - 1 = 5$.


# * **Example 2:**
# * **Input:** `prices = [7, 6, 4, 3, 1]`
# * **Output:** `0`
# * **Explanation:** In this case, no transactions are done and $\text{max profit} = 0$.



# ---

# ### Key Intuition: Two Pointers / Dynamic Tracking

# Instead of checking every pair of days with nested loops ($\mathcal{O}(N^2)$), you can track the minimum buying price as you iterate forward in a single pass ($\mathcal{O}(N)$):

# 1. Maintain two tracking variables: `min_price` (initialized to infinity) and `max_profit` (initialized to `0`).
# 2. Iterate through each price in `prices`:
# * If the current price is lower than `min_price`, update `min_price`.
# * Otherwise, calculate the potential profit (`price - min_price`) and update `max_profit` if this profit is greater than the previous maximum.


# 3. Return `max_profit`.

# ---

# ### Starter Python Template

# ```python
# def maxProfit(prices: list[int]) -> int:
#     min_price = float("inf")
#     max_profit = 0

#     for price in prices:
#         # TODO: Update min_price and max_profit

#         pass

#     return max_profit

# ```

# ---

# ### Complexity Targets

# * **Time Complexity:** $\mathcal{O}(N)$ — Single pass through the `prices` array.
# * **Space Complexity:** $\mathcal{O}(1)$ — Constant extra space used for tracking variables.

# Give it a try and share your Python implementation when you are ready!

def calc_maxprofit(prices):
  max_profit = 0
  min_price = float('inf')
                    
  for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

  return max_profit

if __name__ == '__main__':

  prices = [int(i) for i in input().split()]
  print(prices)

  result = calc_maxprofit(prices)

  print(result)

