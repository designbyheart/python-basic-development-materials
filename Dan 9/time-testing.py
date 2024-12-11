# You need to prepare a date-formatted weekly sales report.
# The date must appear in MM/DD/YYYY format
# at the top of the report.

from datetime import datetime

today = datetime.now()
print(today.strftime("%m/%d/%Y"))


birthdateStr = "Jan 20, 1994"

print("Ovo je datum rodjenja", datetime.strptime(birthdateStr, "%b %d, %Y"))
