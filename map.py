'''

   自己写一个map()函数

'''

from functools import reduce
def new_map(x):
    def f(x):
        return x * x
    list = []
    for y in x:
        list.append(f(y))
    return list

n = new_map([1,2,3,4,5])
print(n)


