from mylib.utils import load_data as load_data


# Define a small library function that includes the required functionality
class WealthDataAnalyzer:
    def __init__(self, data):
        self.data = data

    def top_wealthiest_by_country(self, country, top_n=5):
        """Returns the top N wealthiest individuals in a specified country."""
        country_data = self.data[self.data["Country"] == country]
        top_wealthy = country_data.nlargest(top_n, "Net Worth (in billions)")
        return top_wealthy[["Name", "Net Worth (in billions)", "Industry", "Company"]]

    def average_net_worth_by_industry(self):
        """Calculates and returns the average net worth in billions by industry."""
        avg_net_worth = (
            self.data.groupby("Industry")["Net Worth (in billions)"]
            .mean()
            .sort_values(ascending=False)
        )
        return avg_net_worth


# Load data
data_frame = load_data()

# Instantiate the analyzer with the wealth data
analyzer = WealthDataAnalyzer(data_frame)

# Example outputs from the functions
top_wealthiest_in_usa = analyzer.top_wealthiest_by_country("USA", top_n=5)
avg_net_worth_by_industry = analyzer.average_net_worth_by_industry()

# Display results if running this as the main script
if __name__ == "__main__":
    print(top_wealthiest_in_usa)
    print(avg_net_worth_by_industry)
