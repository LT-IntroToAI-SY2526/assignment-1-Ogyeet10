"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check and we'll be doing them in class.

Make sure to complete the a1.py problems which should be AI generated.
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    # Return the non-negative value of n without using abs()
    if n < 0:
        return -n
    return n


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    result = 1
    # By convention, 0! == 1
    for i in range(2, n + 1):
        result *= i
    return result


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    # Take every other element starting at index 0
    return lst[0::2]


def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    total = 0
    for value in lst:
        total += value
    return total


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    if len(lst) == 0:
        raise ValueError("mean of empty list is undefined")
    return sum_list(lst) / len(lst)


def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    if len(lst) == 0:
        raise ValueError("median of empty list is undefined")
    n = len(lst)
    mid = n // 2
    # List is documented as ordered
    if n % 2 == 1:
        return float(lst[mid])
    # even length: average the two middle values
    return (lst[mid - 1] + lst[mid]) / 2


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ["roscoe", "kim", "woz", "solin"], you'd first
    knock out woz. Then first 'duck' on solin, wrap around to 'duck' on roscoe and
    'goose' on kim - knocking him out and leaving only roscoe and solin.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    if len(lst) < 3:
        raise ValueError("list must have at least 3 names")
    # Remove every 3rd item, wrapping around, until two remain
    idx = 0
    names = list(lst)
    while len(names) > 2:
        idx = (idx + 2) % len(names)
        names.pop(idx)
        # idx now points at the element after the removed one
    return names


# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert absolute(0) == 0, "absolute of 0 failed"
    assert absolute(7) == 7, "absolute of 7 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert factorial(0) == 1, "factorial of 0 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert every_other(["a", "b", "c", "d"]) == ["a", "c"], "every_other strings failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert sum_list([-2, 2, -3, 3]) == 0, "sum_list with negatives failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4]) == 2.5, "median of even-length list failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]
    assert duck_duck_goose(["a", "b", "c"]) == ["a", "b"], "duck_duck_goose 3 names failed"

    print("All tests passed!")