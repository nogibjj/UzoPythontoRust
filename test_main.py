from main2 import load_data, plot_pie_chart, summary_stats, generate_summary
import pandas as pd
import io
import os


def test_load_data():
    """Test the load_data function to ensure it loads CSV data correctly."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Tech,200
Finance,150
Retail,100
Tech,50
Retail,80
    """
    )

    df = load_data(csv_data)
    # Check if the data is loaded correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 2)  # The DataFrame should have 5 rows and 2 columns


def test_plot_pie_chart():
    """Test the plot_pie_chart function to ensure it executes without error."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Tech,200
Finance,150
Retail,100
Tech,50
Retail,80
    """
    )

    # This should run without raising an exception
    plot_pie_chart(csv_data)


def test_summary_stats():
    """Test the summary_stats function to ensure it generates statistics correctly."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Tech,200
Finance,150
Retail,100
Tech,50
Retail,80
    """
    )

    # This should run without raising an exception
    summary_stats(csv_data)


def test_generate_summary():
    """Test the generate_summary function to ensure it creates an HTML file."""
    # Create a small in-memory CSV file for testing
    csv_data = io.StringIO(
        """
Industry,Net Worth (in billions)
Tech,200
Finance,150
Retail,100
Tech,50
Retail,80
    """
    )

    # This should run without raising an exception
    generate_summary(csv_data)
    assert os.path.exists("profile.html"), "Profile report was not created"

    # Clean up the generated file after test
    os.remove("profile.html")


if __name__ == "__main2__":
    test_load_data()
    test_plot_pie_chart()
    test_summary_stats()
    test_generate_summary()
    print("All tests passed successfully.")
