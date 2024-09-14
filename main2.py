import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport


# Function to load data from a CSV file
def load_data(csv_file):
    """This function loads data from a CSV file."""
    return pd.read_csv(csv_file)


# Function to plot a pie chart of net worth distribution by industry
def plot_pie_chart(csv_file):
    """This function plots the pie chart."""
    twp = load_data(csv_file)

    # Group by Industry and sum Net Worth
    industry_net_worth = twp.groupby("Industry")["Net Worth (in billions)"].sum()

    # Plot the pie chart
    industry_net_worth.plot(kind="pie", autopct="%1.3f%%")
    plt.title("Net Worth Distribution by Industry")
    plt.ylabel("")
    plt.show()


# Function to print summary statistics
def summary_stats(csv_file):
    """This function loads data from a CSV and prints summary statistics."""
    data = load_data(csv_file)
    sum_stats = data.describe()
    print(sum_stats)


# Function to generate a profiling report and save it as an HTML file
def generate_summary(csv_file):
    """
    Generates a profiling report of any dataset and saves it as an HTML file.
    """
    # Load the data
    data = load_data(csv_file)

    # Generate the profiling report
    profile = ProfileReport(data, title="Profiling Report")

    # Save the report as an HTML file
    profile.to_file("profile.html")
    print("Profile report saved as profile.html")


# Example usage
csv_file = "Top_1000_wealthiest_people.csv"
plot_pie_chart(csv_file)
summary_stats(csv_file)
generate_summary(csv_file)
