centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
delimiter = "="
print(f'{centuries} centuries {delimiter} {years} years {delimiter} {days:.0f} days {delimiter} {hours:.0f} hours {delimiter} {minutes:.0f} minutes')

