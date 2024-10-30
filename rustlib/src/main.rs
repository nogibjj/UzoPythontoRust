use polars::prelude::*;
use std::fs::File;
use std::error::Error;
use std::time::Instant;
use std::process;
use sysinfo::{Pid, Process, System, SystemExt, ProcessExt};  // Import ProcessExt for memory method

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

// Function to measure time and memory usage for executing a function
fn calculate_time_memory<F>(function: F) -> (i64, f64)
where
    F: FnOnce(),
{
    // Record the start time
    let start_time = Instant::now();

    // Set up system information to measure initial resource usage
    let mut system = System::new_all();
    system.refresh_all();
    
    // Measure initial memory usage
    let start_mem_usage = system
        .process(Pid::from(process::id() as usize))  // Cast process::id() to usize
        .expect("Failed to get current process")
        .memory();  // Memory in kilobytes

    // Execute the function to measure
    function();

    // Refresh system information and measure final memory usage
    system.refresh_all();
    let end_mem_usage = system
        .process(Pid::from(process::id() as usize))  // Cast process::id() to usize
        .expect("Failed to get current process")
        .memory();  // Memory in kilobytes

    // Calculate elapsed time and memory change
    let elapsed_time = start_time.elapsed().as_secs_f64();
    let memory_change = end_mem_usage as i64 - start_mem_usage as i64;

    println!("Elapsed Time: {:.7} seconds", elapsed_time);
    println!("Memory Usage Change: {} kilobytes", memory_change);

    (memory_change, elapsed_time)
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

// Helper functions for specific column statistics
fn grab_mean(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.mean()
}

fn grab_min(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.min()
}

fn grab_std(df: &DataFrame, col: &str) -> Option<f64> {
    let series = df.column(col).ok()?;
    Some(calculate_std_dev(series))
}

// Main function
fn main() {
    // Measure the time and memory of the mini_project_2 function
    let (mem_usage, elapsed_time) = calculate_time_memory(|| {
        if let Err(e) = mini_project_2() {
            eprintln!("Error: {}", e);
        }
    });

    // Optionally print the results outside of the function
    println!("Total Memory Change: {} kilobytes", mem_usage);
    println!("Total Elapsed Time: {:.7} seconds", elapsed_time);
}

