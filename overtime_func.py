def computepay(hours, rate):
    if hours > 40:
        extra = (hours - 40.0)
        over = (rate * 1.5)
        pay = (40 * rate) + (extra * over)
        print("Standard pay: ",(40 * rate))
        print("Overtime:",(extra * over))
        return pay
    else:
        pay = (hours * rate)
        return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

xp = computepay(h,r)

print("Overall Pay", xp)
