def a(x):
    '''Write integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*a(x-1)
print(a.__doc__)
print("Factorial of 0 is ", a(0))
print("Factorial of 1 is ", a(1))
print("Factorial of 2 is ", a(2))
print("Factorial of 5 is ", a(5))
print("Factorial of 10 is ", a(10))
