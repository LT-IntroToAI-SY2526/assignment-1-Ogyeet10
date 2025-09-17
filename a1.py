# Assignment 1: AI-Generated Python Problems
# Name: Aidan Leuenberger

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

# These problems were a bit hard but I wanted to challenge myself so instead of asking for easier problems I just stuck with the ones it originally gave me.

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have a good amount of
experience with JavaScript/TypeScript. Please generate 5 practice problems (increasing in
difficulty) that cover: booleans/conditionals, loops/math, string manipulation,
list processing, and a small algorithmic challenge. Include clear descriptions
and example inputs/outputs.
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Even or Odd
Write a function `is_even(n: int) -> bool` that returns True if `n` is even
and False otherwise.

Example inputs/outputs:
- is_even(4) -> True
- is_even(7) -> False
"""
from typing import List

def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

"""
PROBLEM 2: Sum of Multiples
Write a function `sum_of_multiples(limit: int, divisors: list[int]) -> int`
that returns the sum of all non-negative integers strictly less than `limit`
that are divisible by any number in `divisors`.
"""
def sum_of_multiples(limit: int, divisors: List[int]) -> int:
    """Sum numbers x in [0, limit) divisible by any non-zero divisor."""
    total = 0
    for x in range(limit):
        for d in divisors:
            if d != 0 and x % d == 0:
                total += x
                break
    return total

"""
PROBLEM 3: Run-Length Encoding (Simple Compression)
Write a function `compress_string(s: str) -> str` that compresses a string by
replacing consecutive runs of the same character with the character followed by
the run length. Single characters remain as just the character.
"""
def compress_string(s: str) -> str:
    """Return run-length–encoded string."""
    if not s:
        return ""
    parts: List[str] = []
    current = s[0]
    count = 1
    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(current if count == 1 else f"{current}{count}")
            current = ch
            count = 1
    parts.append(current if count == 1 else f"{current}{count}")
    return "".join(parts)

"""
PROBLEM 4: Second Largest Unique Number
Return the second largest unique number in the list, or raise ValueError if
fewer than two unique numbers exist.
"""
def second_largest(nums: List[int]) -> int:
    """Return the second largest unique value."""
    unique = sorted(set(nums))
    if len(unique) < 2:
        raise ValueError("Need at least two unique numbers")
    return unique[-2]

"""
PROBLEM 5: Rotate List Right by k
Return a new list which is the result of rotating the input list to the right
by `k` positions.
"""
def rotate_right(lst: List[int], k: int) -> List[int]:
    """Return a right-rotated copy of lst by k steps."""
    if not lst:
        return []
    n = len(lst)
    k_norm = k % n
    if k_norm == 0:
        return lst.copy()
    return lst[-k_norm:] + lst[:-k_norm]

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
assert is_even(4) is True
assert is_even(7) is False
assert is_even(0) is True
print("  Problem 1 passed")

print("\nTesting Problem 2:")
assert sum_of_multiples(10, [3, 5]) == 23
assert sum_of_multiples(1, [2]) == 0
assert sum_of_multiples(20, [4]) == sum(x for x in range(20) if x % 4 == 0)
assert sum_of_multiples(15, [0, 5]) == sum(x for x in range(15) if x % 5 == 0)
print("  Problem 2 passed")

print("\nTesting Problem 3:")
assert compress_string("") == ""
assert compress_string("a") == "a"
assert compress_string("aaabbc") == "a3b2c"
assert compress_string("abbbbccdaa") == "ab4c2da2"
print("  Problem 3 passed")

print("\nTesting Problem 4:")
assert second_largest([1, 2, 3, 4]) == 3
assert second_largest([10, 10, 9]) == 9
try:
    second_largest([5])
    raise AssertionError("Expected ValueError")
except ValueError:
    pass
print("  Problem 4 passed")

print("\nTesting Problem 5:")
assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
assert rotate_right([], 3) == []
assert rotate_right([1, 2, 3], 0) == [1, 2, 3]
print("  Problem 5 passed")

print("\nAll tests passed!")


