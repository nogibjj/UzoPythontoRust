use polars::prelude::*;
use std::fs::File;
use std::error::Error;

// Constant for the CSV file path
const CSV_FILE: &str = "Top_1000_wealthiest_people.csv";

// Function to load data from a CSV file
fn load_data() -> Result<DataFrame, Box<dyn Error>> {
    let file = File::open(CSV_FILE)?;
    let df = CsvReader::new(file).infer_schema(Some(100)).finish()?;
    println!("Data loaded from {}", CSV_FILE);
    Ok(df)
}

// Manually compute summary statistics for the DataFrame
fn summary_stats(df: &DataFrame) {
    let columns = df.get_columns();

    println!("Summary Statistics:");
    for col in columns {
        let name = col.name();
        let mean = col.mean().unwrap_or(f64::NAN);
        let min = col.min::<f64>().unwrap_or(f64::NAN);
        let max = col.max::<f64>().unwrap_or(f64::NAN);
        let std_dev = calculate_std_dev(col);

        println!("Column: {}", name);
        println!("  Mean: {:.2}", mean);
        println!("  Min: {:.2}", min);
        println!("  Max: {:.2}", max);
        println!("  Std Dev: {:.2}", std_dev);
    }
}

// Helper function to calculate the standard deviation manually
fn calculate_std_dev(series: &Series) -> f64 {
    if let Some(mean) = series.mean() {
        let squared_diffs: f64 = series
            .f64()
            .expect("Column should be of type f64")
            .into_iter()
            .filter_map(|value| value)
            .map(|value| (value - mean).powi(2))
            .sum();

        let count = series.len() as f64;
        (squared_diffs / count).sqrt()  // Calculate std from variance
    } else {
        f64::NAN
    }
}


// Function to grab the mean of a specific column
fn grab_mean(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.mean()
}

// Function to grab the minimum of a specific column
fn grab_min(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.min()
}

// Function to grab the standard deviation of a specific column
fn grab_std(df: &DataFrame, col: &str) -> Option<f64> {
    let series = df.column(col).ok()?;
    Some(calculate_std_dev(series))
}

// Main workflow function
fn mini_project_2() -> Result<(), Box<dyn Error>> {
    let df = load_data()?;

    // Print general summary statistics
    summary_stats(&df);

    // Compute specific statistics on the "Net Worth (in billions)" column
    let column_name = "Net Worth (in billions)";
    if let Some(mean) = grab_mean(&df, column_name) {
        println!("Mean {}: {:.2}", column_name, mean);
    }
    if let Some(min) = grab_min(&df, column_name) {
        println!("Min {}: {:.2}", column_name, min);
    }
    if let Some(std) = grab_std(&df, column_name) {
        println!("Std Dev {}: {:.2}", column_name, std);
    }

    Ok(())
}

fn main() {
    if let Err(e) = mini_project_2() {
        eprintln!("Error: {}", e);
    }
}

