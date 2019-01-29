def factorial(n):
    """returns n!"""
    return 1 if n<2 else n*factorial(n-1)


print(factorial(42))
# 1405006117752879898543142606244511569936384000000000

print(factorial.__doc__)
# 'returns n!'

print(type(factorial))
# function

fact = factorial

print(fact)
# <function __main__.factorial(n)>

print(fact(5))
# 120

print(map(factorial, range(11)))
# <map at 0x3029db0>

print(list(map(factorial, range(11))))
# [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=len))
# ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']


def reverse(word):
    return word[::-1]


print(reverse("testing"))
# 'gnitset'

print(sorted(fruits, key=reverse))
# ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

print([fact(n) for n in range(6)])
# [1, 1, 2, 6, 24, 120]

print(list(map(fact, range(6))))
# [1, 1, 2, 6, 24, 120]

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
# [1, 6, 120]

print(list(filter(lambda n: n % 2, range(6))))
# [1, 3, 5]


#*******************************************************************

from operator import *

concat_string=concat("I love", "you!")
print(concat_string)


































