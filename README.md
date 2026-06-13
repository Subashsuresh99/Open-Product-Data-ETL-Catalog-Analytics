# Open Product Data ETL Pipeline for Catalog Analytics

## Project Overview

This project demonstrates an end-to-end ETL pipeline using real open product data from the **Open Food Facts API**. The pipeline collects product catalog data, transforms raw JSON records into structured datasets, performs data quality checks, loads the processed data into a SQLite database, and generates reporting-ready outputs for analysis.

## Data Source

**Open Food Facts API**
Open Food Facts is an open product database containing product names, brands, categories, countries, ingredients, nutrition information, Nutri-Score, NOVA group, and other product attributes.

API documentation:
https://openfoodfacts.github.io/openfoodfacts-server/api/

Data reuse information:
https://wiki.openfoodfacts.org/Reusing_Open_Food_Facts_Data

## Tech Stack

* Python
* Requests
* Pandas
* SQLite
* SQL
* Jupyter Notebook
* Git/GitHub
* Power BI / Excel

## Project Structure

```text
open-product-data-etl-catalog-analytics/
│
├── README.md
├── requirements.txt
├── run_pipeline.py
│
├── src/
│   ├── openfoodfacts_api.py
│   ├── transform.py
│   ├── data_quality_checks.py
│   ├── load_to_sql.py
│   ├── reporting.py
│   └── utils.py
│
├── sql/
│   └── create_tables.sql
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│
├── docs/
│   ├── data_source.md
│   ├── pipeline_design.md
│   ├── data_model.md
│   └── powerbi_dashboard_guide.md
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
└── tests/
    └── test_transform.py
```

## Pipeline Workflow

### 1. Extract

Product data is collected from the Open Food Facts API using the API v2 search endpoint.

```text
https://world.openfoodfacts.org/api/v2/search
```

### 2. Transform

Raw JSON product records are cleaned and converted into structured fields, including:

* product code
* product name
* brand
* main category
* country
* Nutri-Score
* NOVA group
* quantity
* packaging
* labels
* ingredient text length

### 3. Validate

The pipeline performs data quality checks for:

* missing product names
* missing brands
* missing categories
* missing countries
* duplicate product codes
* missing or invalid Nutri-Score values
* invalid NOVA group values

### 4. Load

The cleaned product dataset and data quality report are loaded into a SQLite database.

### 5. Report

Summary CSV files are generated for further analysis in Power BI, Excel, or other BI tools.

## Installation

Clone the repository:

```bash
git clone https://github.com/Subashsuresh99/open-product-data-etl-catalog-analytics.git
cd open-product-data-etl-catalog-analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Pipeline

Fetch 100 product records:

```bash
python run_pipeline.py --page-size 100 --search-terms chocolate
```

Fetch records for another category:

```bash
python run_pipeline.py --page-size 100 --search-terms coffee
```

## Output Files

After running the pipeline, the following files are created:

```text
data/raw/openfoodfacts_raw_products.csv
data/processed/openfoodfacts_clean_products.csv
data/processed/openfoodfacts_products.db
reports/data_quality_report.csv
reports/category_summary.csv
reports/brand_summary.csv
reports/country_summary.csv
```

## Reporting Outputs

The generated reports include:

* category-level product summary
* brand-level product summary
* country-level product summary
* data quality report

These outputs can be used to build dashboards showing product distribution, brand coverage, country coverage, Nutri-Score completeness, and data quality gaps.

## Example Analysis Questions

* Which product categories contain the most records?
* Which brands appear most frequently in the collected dataset?
* Which countries have the highest number of products?
* How complete is the Nutri-Score information?
* Which fields have the highest number of missing values?
* What are the main data quality issues in the product catalog?

## Skills Demonstrated

* API data ingestion
* ETL pipeline development
* Data cleaning and transformation
* Data quality validation
* SQL database loading
* Batch data processing
* Reporting output generation
* Technical documentation
* Reproducible project structure

## Project Summary

This project shows how real product data can be collected from an open API, transformed into structured datasets, checked for quality issues, stored in a SQL database, and prepared for business intelligence reporting.
