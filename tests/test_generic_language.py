from tests.helpers import reduce_with

from shrinkray.passes.genericlanguages import (
    combine_expressions,
    reduce_integer_literals,
)


def test_can_reduce_an_integer_in_the_middle_of_a_string():
    assert (
        reduce_with([reduce_integer_literals], b"bobcats99999hello", lambda x: True)
        == b"bobcats0hello"
    )


def test_can_reduce_integers_to_boundaries():
    assert (
        reduce_with([reduce_integer_literals], b"100", lambda x: eval(x) >= 73) == b"73"
    )


def test_can_combine_expressions():
    assert reduce_with([combine_expressions], b"10 + 10", lambda x: True) == b"20"
