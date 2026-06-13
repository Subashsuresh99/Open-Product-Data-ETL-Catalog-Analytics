# Data Model

## Table: products

| Column | Description |
|---|---|
| product_code | Product barcode or product identifier |
| product_name | Product name |
| brand | Main brand name |
| main_category | First listed product category |
| country | First listed country |
| nutriscore_grade | Nutri-Score grade, if available |
| nova_group | NOVA food processing group |
| quantity | Product quantity |
| packaging | Packaging information |
| labels | Product labels |
| ingredients_text | Ingredient text |
| ingredient_text_length | Character length of ingredient text |
| image_url | Product image URL |
| has_product_name | Product name completeness flag |
| has_brand | Brand completeness flag |
| has_category | Category completeness flag |
| has_country | Country completeness flag |
| has_nutriscore | Nutri-Score completeness flag |

## Table: data_quality_report

| Column | Description |
|---|---|
| check_name | Name of the data quality check |
| status | PASS or FAIL |
| failed_count | Number of failed records |
| total_count | Total records checked |
| failure_rate | Failed records divided by total records |
