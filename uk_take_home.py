def uk_take_home(gross):
    # --- Income Tax Bands (England) ---
    personal_allowance = 12570
    basic_rate_limit = 50270
    basic_rate = 0.20
    higher_rate = 0.40

    # --- NI (Class 1 Employee) ---
    ni_primary_threshold = 12570  # aligned with PA for simplicity
    ni_upper_earnings_limit = 50270
    ni_main_rate = 0.08
    ni_upper_rate = 0.02

    # --- Income Tax Computation ---
    taxable = max(0, gross - personal_allowance)

    if taxable <= (basic_rate_limit - personal_allowance):
        tax = taxable * basic_rate
    else:
        basic_band = basic_rate_limit - personal_allowance
        higher_band = taxable - basic_band
        tax = (basic_band * basic_rate) + (higher_band * higher_rate)

    # --- NI Computation ---
    if gross <= ni_primary_threshold:
        ni = 0
    elif gross <= ni_upper_earnings_limit:
        ni = (gross - ni_primary_threshold) * ni_main_rate
    else:
        main_band = ni_upper_earnings_limit - ni_primary_threshold
        upper_band = gross - ni_upper_earnings_limit
        ni = (main_band * ni_main_rate) + (upper_band * ni_upper_rate)

    # --- Net ---
    net = gross - tax - ni
    return tax, ni, net


# Example
hourly_rate = input("How much do you earn per hour: ")
weekly_hours = input("How many hours did you work this week: ")
gross_salary = float(hourly_rate) * int(weekly_hours)
tax, ni, net = uk_take_home(int(gross_salary))
print(f"Tax: £{tax:.2f}, NI: £{ni:.2f}, Take-home: £{net:.2f}")
print(f"Monthly: Tax: £{round(tax/12, 2)} \n")
print(f"Monthly: Take home: £{net/12}")
