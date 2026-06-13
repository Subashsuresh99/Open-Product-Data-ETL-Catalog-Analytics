#!/bin/bash
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running Open Food Facts real-data ETL pipeline..."
python run_pipeline.py --page-size 100 --search-terms chocolate

echo "Pipeline finished."
echo "Generated files:"
echo "data/raw/openfoodfacts_raw_products.csv"
echo "data/processed/openfoodfacts_clean_products.csv"
echo "data/processed/openfoodfacts_products.db"
echo "reports/data_quality_report.csv"
echo "reports/category_summary.csv"
echo "reports/brand_summary.csv"
echo "reports/country_summary.csv"
