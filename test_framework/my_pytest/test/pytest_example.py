import pytest


class TestCase:
    def test_passing(self):
        assert (1, 2, 3) == (1, 2, 3)

    def test_failing(self):
        assert (1, 2, 3) == (3, 2, 1)


if __name__ == '__main__':
    pytest.main(['-q', 'pytest_example.py'])
