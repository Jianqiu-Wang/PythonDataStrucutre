def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer

# Compare 4 different methods to build list data structure
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")


pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(pop_zero.timeit(number=1000))

x = list(range(2000000))
print(pop_end.timeit(number=1000))

# Validate pop(0) is O(n) and pop() is O(1)
"""
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")
print("pop(0) pop()")
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = pop_end.timeit(number=1000)
    x = list(range(i))
    pz = pop_zero.timeit(number=1000)
    print("%15.5f, %15.5f" %(pz,pt))
"""

# Verify the list index operator is O(1)
index = Timer("x[i]", "from __main__ import x,i")
x = list(range(0, 100000, 10000))
for i in range(10):
    x[i]
    print(index.timeit(number=1000000))
