from collections import namedtuple
import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2


def test_member_access():
    t1 = Task('hello, World', 'Tom')
    assert t1.summary == "hello, World"
    assert t1.owner == 'Tom'
    assert (t1.done, t1.id) == (False, None)


if __name__ == "__main__":
    pytest.main(['-v', 'pytest_example02.py::test_member_access'])
