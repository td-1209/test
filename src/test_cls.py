from cls import Cls


def test_field_access():
    c = Cls("a", "b", 1)
    assert c.f1 == "a"
    assert c.f2 == "b"
    assert c.f3 == 1
