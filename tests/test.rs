use polars::prelude::*;
use tempfile::NamedTempFile;
use std::io::Write;
use std::error::Error;
use wealth_data_analyzer::{load_data, summary_stats, grab_mean, grab_min, grab_std};

// Helper function to create a temporary CSV file with sample data
fn create_mock_csv() -> Result<NamedTempFile, Box<dyn Error>> {
    let mut temp_file = NamedTempFile::new()?;
    writeln!(temp_file, "Name,Industry,Net Worth (in billions),Country")?;
    writeln!(temp_file, "Alice,Technology,90.0,USA")?;
    writeln!(temp_file, "Bob,Finance,70.0,Canada")?;
    writeln!(temp_file, "Carol,Manufacturing,55.0,USA")?;
    writeln!(temp_file, "Dave,Retail,45.0,UK")?;
    writeln!(temp_file, "Eve,Technology,85.0,USA")?;
    Ok(temp_file)
}

#[test]
fn test_load_data() {
    let mock_csv = create_mock_csv().expect("Failed to create mock CSV file");
    let df = CsvReader::from_path(mock_csv.path()).expect("Failed to load data").finish().unwrap();
    assert!(df.height() > 0, "Data frame should not be empty");
}

#[test]
fn test_summary_stats() {
    let mock_csv = create_mock_csv().expect("Failed to create mock CSV file");
    let df = CsvReader::from_path(mock_csv.path()).expect("Failed to load data").finish().unwrap();
    summary_stats(&df);  // Just checking if it runs without errors
}

#[test]
fn test_grab_mean_min_std() {
    let mock_csv = create_mock_csv().expect("Failed to create mock CSV file");
    let df = CsvReader::from_path(mock_csv.path()).expect("Failed to load data").finish().unwrap();

    let column_name = "Net Worth (in billions)";

    let mean = grab_mean(&df, column_name).expect("Failed to calculate mean");
    let min = grab_min(&df, column_name).expect("Failed to calculate min");
    let std = grab_std(&df, column_name).expect("Failed to calculate std");

    assert!(mean > 0.0, "Mean should be greater than 0");
    assert!(min > 0.0, "Min should be greater than 0");
    assert!(std >= 0.0, "Standard deviation should be non-negative");
}
