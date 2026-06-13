"""
Main entry point for the Open Product Data ETL Pipeline.

This script runs the full pipeline:
1. Fetch real product data from Open Food Facts API
2. Save raw product data
3. Clean and transform product records
4. Run data quality checks
5. Load clean data into SQLite
6. Generate reporting outputs
"""

import argparse
from pathlib import Path

from src.openfoodfacts_api import fetch_products
from src.transform import clean_product_data
from src.data_quality_checks import run_data_quality_checks
from src.load_to_sql import load_to_sqlite
from src.reporting import create_brand_summary, create_category_summary, create_country_summary
from src.utils import save_dataframe


RAW_PATH = Path("data/raw/openfoodfacts_raw_products.csv")
CLEAN_PATH = Path("data/processed/openfoodfacts_clean_products.csv")
DB_PATH = Path("data/processed/openfoodfacts_products.db")

DQ_REPORT_PATH = Path("reports/data_quality_report.csv")
CATEGORY_SUMMARY_PATH = Path("reports/category_summary.csv")
BRAND_SUMMARY_PATH = Path("reports/brand_summary.csv")
COUNTRY_SUMMARY_PATH = Path("reports/country_summary.csv")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Open Food Facts ETL pipeline.")
    parser.add_argument(
        "--page-size",
        type=int,
        default=100,
        help="Number of products to fetch from the Open Food Facts API.",
    )
    parser.add_argument(
        "--search-terms",
        type=str,
        default="chocolate",
        help="Search term used for collecting product records.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print("Starting Open Product Data ETL Pipeline")
    print(f"Search terms: {args.search_terms}")
    print(f"Requested product count: {args.page_size}")

    print("Step 1: Fetching real product data from Open Food Facts API")
    raw_df = fetch_products(search_terms=args.search_terms, page_size=args.page_size)
    save_dataframe(raw_df, RAW_PATH)

    print("Step 2: Cleaning and transforming product data")
    clean_df = clean_product_data(raw_df)
    save_dataframe(clean_df, CLEAN_PATH)

    print("Step 3: Running data quality checks")
    dq_report = run_data_quality_checks(clean_df)
    save_dataframe(dq_report, DQ_REPORT_PATH)

    print("Step 4: Loading structured data into SQLite")
    load_to_sqlite(
        clean_df=clean_df,
        dq_report=dq_report,
        db_path=DB_PATH,
    )

    print("Step 5: Creating reporting outputs")
    category_summary = create_category_summary(clean_df)
    brand_summary = create_brand_summary(clean_df)
    country_summary = create_country_summary(clean_df)

    save_dataframe(category_summary, CATEGORY_SUMMARY_PATH)
    save_dataframe(brand_summary, BRAND_SUMMARY_PATH)
    save_dataframe(country_summary, COUNTRY_SUMMARY_PATH)

    print("Pipeline completed successfully.")
    print(f"Raw data: {RAW_PATH}")
    print(f"Clean data: {CLEAN_PATH}")
    print(f"SQLite database: {DB_PATH}")
    print(f"Data quality report: {DQ_REPORT_PATH}")
    print(f"Category summary: {CATEGORY_SUMMARY_PATH}")
    print(f"Brand summary: {BRAND_SUMMARY_PATH}")
    print(f"Country summary: {COUNTRY_SUMMARY_PATH}")


if __name__ == "__main__":
    main()
