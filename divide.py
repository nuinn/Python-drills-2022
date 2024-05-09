x = input("What number do you want to divide? ")
y = input("What number would you like to divide it by? ")
while int(x) > 0 and int(x) > int(y):
    x = int(x) - int(y)
if x == 0:
    print("It divides perfectly!")
if x != 0:
    print("It doesn't divide; the remainder is:",x)