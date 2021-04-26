"""
def power(x, n, val=None):
    if n == 1:
        return x
    elif val is None:
        val = x
        n = n - 1
        x = x * x
        return power(x, n, val)
    else:
        n = n - 1
        x = x * val
        return power(x, n, val)


print(power(5, 3))

def reverse(x):
    new_list = []
    for element in x:
        new_list.insert(0,element*2)
    for element in new_list:
        print(element, end=" ")
    return ""


print(reverse([4,8,7,5,6,2,10]))
"""
def fun(x):
    if x>0:
        x-=1
        fun(x)
        print(x,end=" ")
        x-=1
        fun(x)

a=3
fun(3)