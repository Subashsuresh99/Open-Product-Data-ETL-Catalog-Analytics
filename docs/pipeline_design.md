# Pipeline Design

## Architecture

```text
Open Food Facts API
        ↓
Python API ingestion
        ↓
Raw CSV
        ↓
Data cleaning and transformation
        ↓
Clean CSV
        ↓
Data quality validation
        ↓
SQLite database
        ↓
Reporting CSV outputs
        ↓
Power BI / Excel dashboard
```

## Extract

The extraction layer uses the Open Food Facts API search endpoint to collect real product records in JSON format.

## Transform

The transformation layer standardizes product fields and creates analysis-ready columns.

Main transformation steps:

- Clean product names
- Extract primary brand
- Extract primary category
- Extract primary country
- Standardize Nutri-Score
- Convert NOVA group to numeric value
- Calculate ingredient text length
- Create data completeness flags
- Remove duplicate product codes

## Validate

Data quality checks are applied to identify:

- missing product names
- missing brands
- missing categories
- missing countries
- invalid Nutri-Score values
- invalid NOVA group values
- duplicate product codes

## Load

The cleaned product data and data quality report are loaded into SQLite.

## Report

The reporting layer creates CSV files for:

- category summary
- brand summary
- country summary
- data quality report
