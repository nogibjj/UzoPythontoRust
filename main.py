# Import the packages needed to analyze this data
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


# Import Top 1000 wealthiest
# Look at the data and choose some data points to reflect upon
# We will be looking at networth dsitribution by industry and the amount of billions per one industry!

twp = pd.read_csv("Top_1000_wealthiest_people.csv")
# Plot your pie chart
industry_net_worth = twp.groupby("Industry")["Net Worth (in billions)"].sum()
industry_net_worth.plot(kind="pie", autopct="%1.3f%%")
plt.title("Net Worth Distribution by Industry")
plt.ylabel("")
plt.show()

# Define Summary Statistics (Mean, Median, Standard Deviation) using describe method

Wealthiest_data = twp.describe()
print(Wealthiest_data)

# Turn Pie Chart into an image to store in the ReadMe
# plt.savefig("Net Worth Distribution by Industry.png")
