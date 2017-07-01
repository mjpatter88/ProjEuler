def is_leap_year(year):
    # If year is divisible by 4, and not a century unless it is divisible by 400.
    return (year % 4 == 0) and (not (year % 100 == 0) or(year % 400 == 0))

def is_sunday(day_num):
    # This function accepts the number of the day since 1 Jan 1900.
    # Ex: 1 = Jan 1, 1900
    # Ex: 2 = Jan 2, 1900

    return (day_num % 7) == 0


def get_days_in_next_month():
    # This generator returns # days in next month accounting for leap year
    # Starts on Jan 1901

    days_in_months = [
            31, # Jan
            28, # Feb
            31, # Mar
            30, # Apr
            31, # May
            30, # Jun
            31, # Jul
            31, # Aug
            30, # Sep
            31, # Oct
            30, # Nov
            31  # Dec
    ]

    year = 1901
    month = 0

    while True:
        days = days_in_months[month]
        if is_leap_year(year) and month == 1:
            days += 1

        yield days

        month = month + 1
        if month % 12 == 0:
            month = 0
            year += 1


starting_day = 366 # first day in problem is Jan 1 1901, but my functions treat day 1 as jan 1 1900)
years = 100
leap_years = 100//4
non_leap_years = years - leap_years
days_in_year = 365
days_in_leap_year = 366

total_days = (days_in_year * non_leap_years) + (days_in_leap_year * leap_years)
print(f"Total Days: {total_days}")

day_getter = get_days_in_next_month()
next_first = starting_day
sundays_on_first_of_month = 0
while next_first < starting_day + total_days:
    next_first += next(day_getter)
    if is_sunday(next_first):
        sundays_on_first_of_month += 1
        print(next_first)

print(f"Total Sundays on first of month: {sundays_on_first_of_month}")

