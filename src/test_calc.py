import pytest


def test_calc1():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.xfail()
def test_calc1_xfail():
    assert (1, 2, 3) == (1, 3, 3)
