def shutdown(a):
    if a.lower()=="yes":
        exit()
    else:
        print("OK")
while True:
    a=input("Do you want to shutdown (yes or no): ")
    shutdown(a)
