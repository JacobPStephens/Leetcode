import pytest
from longestSubstringWithKElements import Solution

sol = Solution()
def test_example1():
    assert sol.solve("araaci", 2) == 4

def test_example2():
    assert sol.solve("araaci", 1) == 2

def test_example3():
    assert sol.solve("cbbebi", 3) == 5

def test_k_zero():
    assert sol.solve("abcdef", 0) == 0

def test_all_zero():
    assert sol.solve("", 0) == 0

def test_symbols():
    assert sol.solve("   555 ^*(# )", 2) == 7
