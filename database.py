import csv
import os

FILE_NAME = "data/bmi_data.csv"

def save_data(name, weight, height, bmi):

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Name", "Weight", "Height", "BMI"]
            )

        writer.writerow(
            [name, weight, height, bmi]
        )