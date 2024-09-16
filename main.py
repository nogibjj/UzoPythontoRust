"""This code is for main.py it reads a dataset and prints some summary info about it !"""

import pandas as pd
import matplotlib.pyplot as plt


# Function to load data from a CSV file
def load_data(csv_file):
    """This function loads data from a CSV file."""
    df = pd.read_csv(csv_file)
    return df


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart(df):
    """This function plots the pie chart."""
    # Group by Industry and sum Net Worth
    industry_net_worth = df.groupby("Industry")["Net Worth (in billions)"].sum()

    # Plot the pie chart
    industry_net_worth.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Net Worth Distribution by Industry")
    plt.ylabel("")
    plt.show()


# Function to print summary statistics
def summary_stats(df):
    """This function prints summary statistics."""
    sum_stats = df.describe()
    print(sum_stats)


def grab_mean(df, col):
    return df[col].mean()


def grab_min(df, col):
    return df[col].min()


def grab_std(df, col):
    return df[col].std()


# Example usage
if __name__ == "__main__":
    csv_file = "Top_1000_wealthiest_people.csv"
    df = load_data(csv_file)
    plot_pie_chart(df)
    summary_stats(df)
