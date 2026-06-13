# Open Product Data ETL Pipeline for Catalog Analytics

## Project Overview

This is an academic data engineering project developed for a Master's program in Business Intelligence and Data Analytics.  
The project uses **real open product data from the Open Food Facts API** and demonstrates a complete ETL workflow:

1. Ingest product data from a public API
2. Clean and transform raw JSON data into structured tables
3. Apply data quality checks
4. Load processed data into a SQL database
5. Generate reporting-ready CSV outputs for Power BI / Excel
6. Document the pipeline for reproducible analysis


## API Endpoint Fix

This project uses the current Open Food Facts API v2 search endpoint:

```text
https://world.openfoodfacts.org/api/v2/search
```

The older endpoint:

```text
https://world.openfoodfacts.org/cgi/search.pl
```

can return `503 Service Temporarily Unavailable`, so this project avoids the legacy endpoint.

## Data Source

**Open Food Facts API**  
Open Food Facts is an open product database containing product names, brands, categories, countries, ingredients, nutrition information, Nutri-Score, and other product attributes.

Official API documentation:  
https://openfoodfacts.github.io/openfoodfacts-server/api/

Data reuse information:  
https://wiki.openfoodfacts.org/Reusing_Open_Food_Facts_Data

## Why This Project

This project is designed to demonstrate practical skills required for a Data Engineering working student role:

- Python programming
- API-based data ingestion
- ETL pipeline development
- Batch ingestion
- SQL database loading
- Data quality checks
- Git/GitHub project structure
- Documentation
- Reporting-ready outputs
- Power BI / Excel analytics preparation

## Tech Stack

- Python
- Requests
- Pandas
- SQLite
- SQL
- Git/GitHub
- Jupyter Notebook
- Power BI / Excel

## Project Structure

```text
open-product-data-etl-catalog-analytics/
│
├── README.md
├── requirements.txt
├── .gitignore
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
│   ├── powerbi_dashboard_guide.md
│   └── github_upload_steps.md
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
└── tests/
    └── test_transform.py
```



## Important: Use the Updated API File

If your error URL still contains:

```text
search_simple=1&action=process&json=1
```

you are still running an old version of `src/openfoodfacts_api.py`.

The updated project uses the API v2 endpoint with retry handling and fallback query parameters.

## Important Real Data Note

This project is designed to use **real Open Food Facts API data**.  
Run the pipeline locally to generate real product records:

```bash
python run_pipeline.py --page-size 100 --search-terms chocolate
```

This creates real API-based output files in:

```text
data/raw/
data/processed/
reports/
```

The generated data can then be committed to GitHub as proof of the working ETL pipeline.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Subashsuresh99/open-product-data-etl-catalog-analytics.git
cd open-product-data-etl-catalog-analytics
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the ETL pipeline

Fetch 100 real products:

```bash
python run_pipeline.py --page-size 100 --search-terms chocolate
```

Fetch 200 real products:

```bash
python run_pipeline.py --page-size 200 --search-terms coffee
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

## Pipeline Steps

### 1. Extract

The pipeline sends a request to the Open Food Facts API v2 search endpoint and retrieves product catalog data in JSON format.

### 2. Transform

Raw product records are cleaned and converted into structured data fields such as:

- product code
- product name
- brand
- main category
- country
- Nutri-Score
- NOVA group
- quantity
- ingredient length
- packaging
- labels

### 3. Validate

The pipeline checks for common data quality issues:

- missing product names
- missing brands
- missing categories
- missing countries
- duplicate product codes
- missing nutrition grades
- invalid NOVA group values

### 4. Load

Processed data is loaded into a SQLite database.

### 5. Report

Summary tables are generated for Power BI / Excel reporting.

## Example Business Questions

- Which product categories have the most records?
- Which brands appear most frequently?
- Which countries have the highest number of products?
- What percentage of products have missing Nutri-Score values?
- Which categories have better data completeness?
- What data quality gaps exist in the product catalog?

## Suggested Power BI Dashboard Pages

1. Product catalog overview
2. Brand and category analysis
3. Country distribution
4. Nutri-Score and NOVA group overview
5. Data quality monitoring

## Resume Entry

**Open Product Data ETL Pipeline for Catalog Analytics**  
Developed a Python-based ETL pipeline using real open product data from the Open Food Facts API. Collected product catalog records, cleaned and validated fields such as product name, brand, category, country, Nutri-Score, and NOVA group, loaded structured data into SQLite, and prepared reporting-ready outputs for Power BI analytics. Documented the workflow in GitHub with reusable scripts, data quality checks, SQL schema, and pipeline documentation.

## Skills Demonstrated

- Data engineering
- API ingestion
- ETL/ELT concepts
- Batch data processing
- Python scripting
- SQL database loading
- Data quality validation
- Reporting and dashboard preparation
- Technical documentation
- GitHub project organization


## Troubleshooting

If pandas installation fails on Windows with a `pyproject.toml` or Visual Studio error, run:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

See:

```text
docs/troubleshooting.md
```
