from unittest import TestCase
from hypothesis import given
from hypothesis.strategies import lists, integers


def merge(left, right):
    result = []
    i, j = 0, 0

    if len(left) > 5:
        return left

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)


# ------------------------------------------------------------------------------
# Traditional (example-based) testing vs property-based testing

# Example-based testing:
#   - come up with some inputs
#   - come up with some outputs
#   - check if they match


# Property-based testing:
#   - Describe input (e.g. a list of integers, some JSON, a string, ...)
#   - Describe properties of output
#   - Auto-generate hundreds of sets of inputs and see if they match


# Haskell: QuickCheck
# Scala: ScalaCheck
# Clojure: test.check
# ...
# Python: Hypothesis


# ------------------------------------------------------------------------------
# Canonical Property-based testing example: a sorted list

class MergeSortTest(TestCase):

    @given(lists(integers()))
    def test_sorting_list_of_integers(self, xs):
        res = mergesort(xs)
        assert isinstance(res, list)
        assert len(res) == len(xs)
        assert all(x <= y for x, y in zip(res, res[1:]))



# What happens if we introduce a bug in the implementation?


# Minimal failing case


# ------------------------------------------------------------------------------
# Real-world use cases:
#
# sanity check function APIs, e.g.
#   - should never throw an exception
#   - return value should always have a certain type

# sanity check REST APIs, e.g.
#   - return value should always be valid JSON
#   - status code should always be 2xx or 4xx

# functions that are inverses of each other
#   - encode/decode
#   - serialise/deserialise

# idempotent functions
#   - output should stay the same

# "Test Oracle": first implement an easily verified, slow version.
# Then implement an optimised version. Use property-based testing
# to verify that both work the same way.


# ------------------------------------------------------------------------------
# Conclusion

# - Great for making silly bugs fall out, like sorting an empty lists

# - Verify library APIs

# - Makes testing more like coding, gets you thinking about how to generate
#   inputs and what the output properties are


# ------------------------------------------------------------------------------
# Resources
#
# http://hypothesis.readthedocs.io
# https://www.infoq.com/presentations/hypothesis-afl-property-testing
