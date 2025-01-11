def a(b,c):
    total = b*(1+0.01*(c))
    total = round(total,2)
    print(f"Please pay ${total}")
a(150,20)
