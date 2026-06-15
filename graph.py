import pandas as pd
import matplotlib.pyplot as plt

def show_graph():

    data = pd.read_csv(
        "data/bmi_data.csv"
    )

    plt.plot(data["BMI"], marker='o')

    plt.title("BMI Trend")

    plt.xlabel("Records")

    plt.ylabel("BMI")

    plt.grid(True)

    plt.show()