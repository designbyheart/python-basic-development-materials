# fileManager
import csv

def load_csv(file_path, cls=None):
    items = []
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(f"{row}")
            if cls:
                items.append(  # `cls(**row)` is a Python expression that creates an instance of a class
                    # using keyword arguments extracted from the `row` dictionary.
                    cls(**row)
                )
            else:
                items.append(row)
    return items


def save_csv(file_path, items):
    if not items:
        return
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=items[0].to_dict().keys())
        writer.writeheader()
        for item in items:
            writer.writerow(item.to_dict())
