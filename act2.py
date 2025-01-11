def a(b):
    return b**3
def c(b):
    if b%3==0:
        return a(b)
    else:
        return False
print(c(9))
print(c(4))
    
