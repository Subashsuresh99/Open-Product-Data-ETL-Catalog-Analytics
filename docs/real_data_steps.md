# Real Data Generation Steps

This repository is configured to collect **real product data from the Open Food Facts API**.

## Why the CSV is generated locally

The project does not depend on fake or synthetic data.  
When you run the pipeline, it fetches live product records from Open Food Facts and creates the raw, cleaned, SQL, and report files.

## Windows

Double-click:

```text
run_real_data_pipeline.bat
```

Or run manually:

```bash
pip install -r requirements.txt
python run_pipeline.py --page-size 100 --search-terms chocolate
```

## macOS / Linux

```bash
chmod +x run_real_data_pipeline.sh
./run_real_data_pipeline.sh
```

Or run manually:

```bash
pip install -r requirements.txt
python run_pipeline.py --page-size 100 --search-terms chocolate
```

## Generate More Data

For 200 records:

```bash
python run_pipeline.py --page-size 200 --search-terms coffee
```

For another category:

```bash
python run_pipeline.py --page-size 150 --search-terms pasta
```

## Files Created After Running

```text
data/raw/openfoodfacts_raw_products.csv
data/processed/openfoodfacts_clean_products.csv
data/processed/openfoodfacts_products.db
reports/data_quality_report.csv
reports/category_summary.csv
reports/brand_summary.csv
reports/country_summary.csv
```

## Commit Generated Real Data to GitHub

After running the pipeline:

```bash
git add data reports
git commit -m "Add real Open Food Facts ETL output data"
git push
```

## Recommended GitHub Evidence

After pushing, your repository should show:

- Python ETL source code
- README documentation
- data source documentation
- raw real-data CSV
- cleaned real-data CSV
- SQLite database
- data quality report
- summary report files
