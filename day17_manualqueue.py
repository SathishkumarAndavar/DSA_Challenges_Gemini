# ---

# ### Key Intuition: Two Stacks (In-Stack & Out-Stack)

# A single stack reverses order (LIFO). Reversing data **twice** restores original FIFO order!

# * Maintain two stacks: `instack` (for receiving new incoming elements) and `outstack` (for serving elements from the front).
# * **Push:** Always append to `instack`.
# * **Pop / Peek:** 
#   * If `outstack` is empty, pop all elements from `instack` one by one and append them to `outstack`. This reverses their order!
#   * Now the top of `outstack` holds the oldest element (front of the queue). Pop or inspect `outstack[-1]`.

# ---

# ### Starter Python Template

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


class MyQueue:

  def __init__(self):
    self.instack = []
    self.outstack = []

  def push(self,x):
    self.instack.append(x)
    
  def transfer(self):
    if not self.outstack:
      while self.instack:
        self.outstack.append(self.instack.pop())

  def pop(self):
    self.transfer()
    return self.outstack.pop()

  def peek(self):
    self.transfer()
    return self.outstack[-1]

  def empty(self):
    return not self.instack and not self.outstack
    

if __name__ == '__main__':

  myQueue = MyQueue()

  myQueue.push(1)
  myQueue.push(1)
  myQueue.push(2)

  print("Peek front element:", myQueue.peek())  # Returns 1
  print("Popped element:", myQueue.pop())  # Returns 1
  print("Is queue empty?", myQueue.empty())  # Returns False

You fixed the `self` parameters and instance references, but `pop()` and `peek()` are still pulling from `self.instack` instead of calling `self.transfer()` and pulling from `self.outstack`.

Pulling from `instack` keeps LIFO order (Last-In, First-Out) instead of restoring FIFO queue order (First-In, First-Out).

---

### Remaining Logic Bugs

1. **`pop()` logic:** Needs to call `self.transfer()` first, then pop from `self.outstack`.
2. **`peek()` logic:** Needs to call `self.transfer()` first, then return the last element of `self.outstack` (`self.outstack[-1]`).

---

### Corrected Code

```python
class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x):
        self.instack.append(x)

    def transfer(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

    def pop(self):
        self.transfer()  # Ensure outstack has elements in FIFO order
        return self.outstack.pop()

    def peek(self):
        self.transfer()  # Ensure outstack has elements in FIFO order
        return self.outstack[-1]

    def empty(self):
        return not self.instack and not self.outstack


if __name__ == "__main__":
    myQueue = MyQueue()

    myQueue.push(1)
    myQueue.push(2)

    print("Peek front element:", myQueue.peek())  # Returns 1
    print("Popped element:", myQueue.pop())  # Returns 1
    print("Is queue empty?", myQueue.empty())  # Returns False

# ```

# ---

# ### Output

# ```text
# Peek front element: 1
# Popped element: 1
# Is queue empty? False

# ```

# ---

# ### Complexity Analysis

# * **Time Complexity:**
# * `push`: $\mathcal{O}(1)$
# * `pop` / `peek`: **Amortized $\mathcal{O}(1)$** (each item moves to `outstack` exactly once)
# * `empty`: $\mathcal{O}(1)$


# * **Space Complexity:** $\mathcal{O}(N)$ total space for elements across both stacks.
