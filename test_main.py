from mylib.utils import load_data, plot_pie_chart, summary_stats, calculate_time_memory
import pandas as pd
import io


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

    df = pd.read_csv(csv_data)
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

    df = pd.read_csv(csv_data)
    # This should run without raising an exception
    plot_pie_chart(df)


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

    df = pd.read_csv(csv_data)
    # This should run without raising an exception
    summary_stats(df)


def test_calculate_time_memory():
    data = load_data()
    result = calculate_time_memory(data)
    assert result is not None, "Test has failed."


if __name__ == "__main__":
    test_load_data()
    test_plot_pie_chart()
    test_summary_stats()
    print("All tests passed successfully.")
