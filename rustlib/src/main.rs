use polars::prelude::*;
use std::fs::File;
use std::path::PathBuf;
use std::error::Error;
use plotters::prelude::*;

// Constant for the CSV file path
const CSV_FILE: &str = "Top_1000_wealthiest_people.csv";

// Function to load data from a CSV file
fn load_data() -> Result<DataFrame, Box<dyn Error>> {
    let file = File::open(CSV_FILE)?;
    let df = CsvReader::new(file).infer_schema(Some(100)).finish()?;
    println!("Data loaded from {}", CSV_FILE);
    Ok(df)
}

// Function to plot a pie chart of net worth distribution by industry
fn plot_pie_chart(df: &DataFrame) -> Result<(), Box<dyn Error>> {
    let industry_series = df.column("Industry")?;
    let net_worth_series = df.column("Net Worth (in billions)")?.cast(&DataType::Float64)?;

    // Aggregate by industry
    let grouped = df.groupby("Industry")?.sum()?;
    let industry_net_worth = grouped.column("Net Worth (in billions)")?.cast(&DataType::Float64)?;

    // Plotting setup
    let root_area = BitMapBackend::new("industry_net_worth.png", (800, 600)).into_drawing_area();
    root_area.fill(&WHITE)?;

    let mut chart = ChartBuilder::on(&root_area)
        .caption("Net Worth Distribution by Industry", ("Arial", 20).into_font())
        .build_pie()?;

    for (i, value) in industry_net_worth.iter().enumerate() {
        let pct = value.f64().unwrap_or(0.0) / industry_net_worth.sum::<f64>().unwrap_or(1.0);
        chart.draw_sector(&value, pct, &format!("{}", industry_series.get(i).unwrap()))?;
    }
    Ok(())
}

// Function to print summary statistics
fn summary_stats(df: &DataFrame) {
    let summary = df.describe(None).unwrap();
    println!("{:?}", summary);
}

// Helper functions to grab mean, min, and standard deviation
fn grab_mean(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.mean()
}

fn grab_min(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.min()
}

fn grab_std(df: &DataFrame, col: &str) -> Option<f64> {
    df.column(col).ok()?.std()
}

// Main workflow function
fn mini_project_2() -> Result<(), Box<dyn Error>> {
    let df = load_data()?;
    plot_pie_chart(&df)?;
    summary_stats(&df);
    Ok(())
}

fn main() {
    if let Err(e) = mini_project_2() {
        eprintln!("Error: {}", e);
    }
}
