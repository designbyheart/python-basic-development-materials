from datetime import datetime
from dateutil.relativedelta import relativedelta

initial_payment_date = datetime(2024, 1, 15)
next_payment_date = initial_payment_date + relativedelta(months=1)
print("Next Payment Date:", next_payment_date)
