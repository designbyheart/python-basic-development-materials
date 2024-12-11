import csv

count = 0

with open("people.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if int(row["age"]) > 30:
            count += 1

print(f"Number of people older than 30: {count}")
