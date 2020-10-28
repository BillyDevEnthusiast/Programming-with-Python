import  math
centuries = int(input())
day_year = 365.2422
hours_day = 24
minutes_hour = 60

years = centuries * 100
days = int(years * day_year)
hours = int(days * hours_day)
minutes = int(hours * minutes_hour)

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
