# Data Source

## Source Name

Open Food Facts API

## Source Type

Public open product database / REST API

## Source Links

- API documentation: https://openfoodfacts.github.io/openfoodfacts-server/api/
- Data reuse information: https://wiki.openfoodfacts.org/Reusing_Open_Food_Facts_Data

## Fields Used

The project collects the following product fields:

- code
- product_name
- brands
- categories
- countries
- nutriscore_grade
- nova_group
- quantity
- packaging
- labels
- ingredients_text
- image_url

## Why This Source Was Selected

Open Food Facts provides real product catalog data and is suitable for demonstrating practical data engineering skills such as API ingestion, data cleaning, data quality validation, SQL loading, and analytics reporting.


## API Endpoint Used

```text
https://world.openfoodfacts.org/api/v2/search
```

Example:

```bash
python run_pipeline.py --page-size 100 --search-terms chocolate
```

The value passed through `--search-terms` is used as the `categories_tags_en` filter in the API v2 search endpoint.
