# Function to load data from a CSV file
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
import psutil

CSV_FILE = (
    os.path.join(os.path.dirname(__file__), "Top_1000_wealthiest_people.csv")
    or "Top_1000_wealthiest_people.csv"
)


def load_data():
    """This function loads data from a CSV file."""
    data_frame = pd.read_csv(CSV_FILE)
    print(f"Data loaded from {CSV_FILE}")
    return data_frame


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart(data_frame):
    """This function plots the pie chart."""
    # Group by Industry and sum Net Worth
    industry_net_worth = data_frame.groupby("Industry")["Net Worth (in billions)"].sum()

    # Plot the pie chart
    industry_net_worth.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Net Worth Distribution by Industry")
    plt.ylabel("")
    plt.show()


# Function to print summary statistics
def summary_stats(data_frame):
    """This function prints summary statistics."""
    sum_stats = data_frame.describe()
    print(sum_stats)


def grab_mean(data_frame, col):
    """This function is meant to grab the mean from the summary stats."""
    return data_frame[col].mean()


def grab_min(data_frame, col):
    """This function is meant to grab the minimum net worth from the summary stats."""
    return data_frame[col].min()


def grab_std(data_frame, col):
    """This function is meant to grab the standard deviation from the summary stats."""
    return data_frame[col].std()


def mini_project_2():
    """This function runs the main workflow."""
    data_frame = load_data()
    plot_pie_chart(data_frame)
    summary_stats(data_frame)


def calculate_time_memory(path):
    """Function to calculate runtime and memory usage for loading and processing data."""

    # Record the start time
    start_time = time.time()

    # Measure the initial resource usage
    process = psutil.Process()
    start_mem_usage = process.memory_info().rss  # in bytes

    # Load data and compute summary statistics
    data = load_data()
    summary_stats(data)

    # Record the end time
    end_time = time.time()

    # Measure the final resource usage
    end_mem_usage = process.memory_info().rss  # in bytes

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Convert memory usage from bytes to kilobytes
    memory_change = (end_mem_usage - start_mem_usage) / 1024

    print(f"Python-Elapsed Time: {elapsed_time:.7f} seconds")
    print(f"Python-Memory Usage Change: {memory_change:.2f} kilobytes")

    return memory_change, elapsed_time


# if __name__ == "__main__":
#     mini_project_2()
