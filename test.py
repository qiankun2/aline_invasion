def add(x,y,f):
    return f(x) + f(y)

print(add(-5,6,abs))


p = abs
print (p(-2))


print(abs(-10))

def f(x):
    return x * x

r = map(f,[1,3,5,7,10,12])
print (list(r))

list2 = []
for n in [1,2,3,4,5,6,7,8,9]:
    list2.append(f(n))
print (list2)
