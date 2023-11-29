try:
    n= input("enter a value: ")
    print(int(n))
except:
    print("Not int value")
########

try:
    n= input("enter a value: ")
    print(int(n))
except Exception as exc:
    print("Not int value", type(exc))
##########

