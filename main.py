# Time
days_worked = int(input("How many days did you work this week: "))
while days_worked > 7:
    print(f"There are only 7 days in a week. You typed {days_worked} days")
    days_worked = int(input("How many days did you work this week: "))

hours_per_day = float(input("How many hours per day: "))
while hours_per_day > 12:
    check_hours = input(f"Are you sure you worked {hours_per_day} hours? ")
    if check_hours != 'n':
        break
    else:
        hours_per_day = float(input("How many hours per day: "))
# Rate
hourly_rate = float(input("What is your hourly rate: £"))


tax_rate = 20

# totals
gross_pay = days_worked * (hourly_rate * hourly_rate)
net_pay = gross_pay * (tax_rate / 100)



print(net_pay)