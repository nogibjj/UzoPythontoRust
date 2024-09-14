import pandas as pd
import matplotlib.pyplot as plt


# Function to load data from a CSV file
def load_data():
    """This function loads data from a CSV file."""
    return pd.read_csv("Top_1000_wealthiest_people.csv")


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart():
    """This function plots the pie chart."""
    twp = load_data()

    # Group by Industry and sum Net Worth
    industry_net_worth = twp.groupby("Industry")["Net Worth (in billions)"].sum()

    # Plot the pie chart
    industry_net_worth.plot(kind="pie", autopct="%1.3f%%")
    plt.title("Net Worth Distribution by Industry")
    plt.ylabel("")
    plt.show()


# Function to print summary statistics
def summary_stats():
    """This function loads data from a CSV and prints summary statistics."""
    data = load_data()
    sum_stats = data.describe()
    print(sum_stats)


# Plot the summary statistics as a table
fig, ax = plt.subplots(figsize=(10, 2))  # Adjust the size as needed
ax.axis("tight")
ax.axis("off")
x = summary_stats
table = ax.table(
    cellText=x.values,
    colLabels=x.columns,
    rowLabels=x.index,
    cellLoc="center",
    loc="center",
)

# Save the table as an image
plt.savefig("x.png")
plt.show()


# Example usage
plot_pie_chart()
summary_stats()
