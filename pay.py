hours = input('How many hours have you worked this week?')
rate = input('What is your hourly rate?')
pay = (float(hours)*float(rate))*0.93
print('Your pay this week will be', round(pay), 'euros')
