age = input("How old are you? ")
try:
    if int(age) <18:
        print("You are a child.")
    elif int(age) <30:
        print("Nice!")
    elif int(age) <40:
        print("You're getting old!")
    elif int(age) <66:
        print("You old, sucker!")
    else:
        print("You're basically dead!")
except:
    print("Write a number, stupid.")
