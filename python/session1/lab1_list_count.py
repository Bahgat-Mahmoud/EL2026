"""Write a Python program to count the number 4 in a given list."""


import re


def count(lst):
    """Write your solution here. Don't forget to return the result at the end...."""
    return lst.count(4)
    # count = 0
    # for i in lst:
    #     if i==4:
    #         print("Hello from the function")
    #         count+=1
    # return count


if __name__ == "__main__":
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"


