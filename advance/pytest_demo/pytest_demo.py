import pytest


class TestDemo:
    
    def test_example01(self):
        print("Hello, pytest!")

    def test_example02(self):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-sv', 'pytest_demo.py'])
