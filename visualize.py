import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/pratu/Downloads/Cancer_Data.csv")
df["diagnosis"] = df["diagnosis"].map({"M":1, "B":0})

df["diagnosis"].value_counts().plot(kind="bar")
plt.show()

