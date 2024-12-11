# 10 years
from datetime import date

my_birthday = date(1990, 5, 21)
today = date.today()

# print(my_birthday, today.isoformat())


d1 = date(2022, 5, 17)
d2 = date(2023, 10, 14)
# print("Is d2 older?", d1 > d2)
#


d1 = date(2024, 1, 1)
d2 = date(2023, 10, 14)
delta = d1 - d2
# print(delta.days, "days")
# print(delta.months, "months")
# print(delta.years, "years")

from datetime import date

# print("Min date:", date.min)
# print("Max date:", date.max)


d = date(2024, 10, 14)
print(str(d))
