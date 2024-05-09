small = None
large = None
sum = 0
total = 0
while True:
    user = input("Enter a number:")
    if user == "done":
        break
    try:
        num = float(user)
        sum = sum + 1
        total = total + num
        if large is None:
            large = num
        elif large < num:
            large = num
        if small is None:
            small = num
        elif small > num:
            small = num
        #print(sum)
        #print(total)

    except:
        print("Invalid input")
print("Maximum is", large)
print("Minimum is", small)
try:
    print("Average is", total / sum)
except:
    print("Average is None")
