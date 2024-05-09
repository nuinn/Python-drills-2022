small = None
large = None
while True:
    user = input("Enter a number:")
    if user == "done":
        break
    try:
        num = int(user)
        if large is None:
            large = num
        elif large < num:
            large = num
        if small is None:
            small = num
        elif small > num:
            small = num
    except:
        print("Invalid input")
print("Maximum is", large)
print("Minimum is", small)
