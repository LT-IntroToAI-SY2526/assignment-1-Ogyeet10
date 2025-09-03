# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

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

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some
experience with Java. Can you create 6 practice problems that cover variables,
conditionals, loops, functions, and basic list operations? Make them
progressively more challenging with clear instructions and examples.
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Even or Odd
Write a function `is_even(n: int) -> bool` that returns True if n is even and
False otherwise.

Examples:
- is_even(4) -> True
- is_even(7) -> False
"""


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise.

    Approach:
    - Use the modulo operator to check remainder when divided by 2.
    """
    return n % 2 == 0


"""
PROBLEM 2: FizzBuzz
Write a function `fizz_buzz(n: int) -> list[str]` that returns a list of
strings from 1..n where:
- multiples of 3 are "Fizz"
- multiples of 5 are "Buzz"
- multiples of both 3 and 5 are "FizzBuzz"
- all other numbers appear as their string form

Example for n=5:
["1", "2", "Fizz", "4", "Buzz"]
"""


def fizz_buzz(n: int) -> list[str]:
    """Generate the FizzBuzz sequence from 1 to n inclusive.

    Approach:
    - Iterate 1..n and apply divisibility rules with clear precedence for 15.
    """
    result: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


"""
PROBLEM 3: Count Vowels
Write a function `count_vowels(s: str) -> int` that returns the number of
vowels in a string. Treat both uppercase and lowercase vowels (a, e, i, o, u)
as vowels.

Examples:
- count_vowels("apple") -> 2
- count_vowels("Sky") -> 0
"""


def count_vowels(s: str) -> int:
    """Return the number of vowels in s (case-insensitive).

    Approach:
    - Normalize to lowercase and count membership in a vowel set.
    """
    vowels = {"a", "e", "i", "o", "u"}
    total = 0
    for ch in s.lower():
        if ch in vowels:
            total += 1
    return total


"""
PROBLEM 4: Sum of Squares
Write a function `sum_of_squares(nums: list[int]) -> int` that returns the sum
of the squares of the numbers in the list.

Example:
- sum_of_squares([1, 2, 3]) -> 14
"""


def sum_of_squares(nums: list[int]) -> int:
    """Return the sum of squares of the integers in nums.

    Approach:
    - Accumulate value*value for each element.
    """
    total = 0
    for x in nums:
        total += x * x
    return total


"""
PROBLEM 5: Max in List
Write a function `max_in_list(nums: list[int]) -> int` that returns the
maximum value in a non-empty list without using the built-in `max`.

Example:
- max_in_list([3, 7, 2, 9]) -> 9
"""


def max_in_list(nums: list[int]) -> int:
    """Return the largest integer in a non-empty list.

    Approach:
    - Track a running maximum initialized to the first element.
    """
    if len(nums) == 0:
        raise ValueError("max_in_list requires a non-empty list")
    current_max = nums[0]
    for x in nums[1:]:
        if x > current_max:
            current_max = x
    return current_max


"""
PROBLEM 6: Reverse Words in a Sentence
Write a function `reverse_words(s: str) -> str` that returns a new string with
the order of words reversed. Words are separated by one or more spaces and you
should collapse multiple spaces to single spaces in the result.

Examples:
- reverse_words("hello world") -> "world hello"
- reverse_words("  a   b  c ") -> "c b a"
"""


def reverse_words(s: str) -> str:
    """Return s with word order reversed and single spaces between words.

    Approach:
    - Split on whitespace, reverse the list, then join with single spaces.
    """
    parts = s.split()
    parts.reverse()
    return " ".join(parts)
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
print(f"is_even(4): {is_even(4)}")  # True
print(f"is_even(7): {is_even(7)}")  # False
assert is_even(0) is True
assert is_even(-2) is True
assert is_even(5) is False

print("\nTesting Problem 2:")
print(f"fizz_buzz(5): {fizz_buzz(5)}")
assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizz_buzz(15)[-1] == "FizzBuzz"

print("\nTesting Problem 3:")
print(f"count_vowels('Apple'): {count_vowels('Apple')}")
assert count_vowels("Apple") == 2
assert count_vowels("SKY") == 0

print("\nTesting Problem 4:")
print(f"sum_of_squares([1,2,3]): {sum_of_squares([1,2,3])}")
assert sum_of_squares([1, 2, 3]) == 14
assert sum_of_squares([]) == 0

print("\nTesting Problem 5:")
print(f"max_in_list([3,7,2,9]): {max_in_list([3,7,2,9])}")
assert max_in_list([3, 7, 2, 9]) == 9
assert max_in_list([-5, -2, -9]) == -2

print("\nTesting Problem 6:")
print(f"reverse_words('hello   world'): {reverse_words('hello   world')}")
assert reverse_words("hello   world") == "world hello"
assert reverse_words("  a   b  c ") == "c b a"


