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
tax_rate = .20

# Overtime
did_overtime = input("Did you work overtime (y/n): ")
if did_overtime != 'y' or 'n':
    did_overtime = input("Did you work overtime (y/n): ")



# totals
gross_pay = days_worked * (hourly_rate * hours_per_day)
tax_amount = (days_worked + hours_per_day) * tax_rate
total_pay = gross_pay - tax_amount

# if did_overtime == "y":
#     overtime_rate = float(input("What is the overtime rate (1.5 etc): "))
#     overtime_hours = float(input("How many overtime hours: "))
#     total_overtime = overtime_hours * overtime_rate
#
#     print(f"Your take home pay for this working week is: {round(total_pay + total_overtime, 2)}")
#
# else:
#     print(f"Your take home pay for this working week is: {round(total_pay, 2)}")

print(f"Your total pay this week after deductions is: £{round(total_pay, 2)}")