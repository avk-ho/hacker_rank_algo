# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true

# switch of calendar in Russia 31/01/1918 => 14/02/1914 (the next day)
# leap year (gregorian): divisible by 400; divisible by 4 but not 100
# leap year (julian): divisible by 4
# february has 29 days during a leap year, 28 the others
# find the 256th day of the year

def find_day_of_programmer(year):
    is_leap_year_j = year % 4 == 0
    is_leap_year_g = year % 400 == 0 or (year % 4 == 0 and not year % 100 == 0)

    target_day = 256
    month = 1

    while target_day >= 28:
        if month <= 7:
            if month % 2 == 1: # odd months
                target_day -= 31
            elif month == 2: # february
                if year < 1918:
                    if is_leap_year_j:
                        target_day -= 29
                    else:
                        target_day -= 28
                elif year == 1918: # not a leap year
                    target_day -= (28-13)
                elif year > 1918:
                    if is_leap_year_g:
                        target_day -= 29
                    else:
                        target_day -= 28
            elif month % 2 == 0: # even months (excluding february)
                target_day -= 30
        else:
            if month % 2 == 1: # odd months
                target_day -= 30
            elif month % 2 == 0: # even months
                target_day -= 31

        month += 1
    
    if month < 10:
        month = "0" + str(month)

    return f"{target_day}.{month}.{year}"


years = [2017, 1918, 1984, 1800]
for year in years:
    print(find_day_of_programmer(year))