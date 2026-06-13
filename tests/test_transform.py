"""
Basic tests for transformation logic.
"""

import pandas as pd

from src.transform import clean_product_data


def test_clean_product_data_basic_fields():
    raw_df = pd.DataFrame(
        [
            {
                "code": "123456",
                "product_name": "Sample Product",
                "brands": "Sample Brand, Another Brand",
                "categories": "Snacks, Chocolate",
                "countries": "Germany, France",
                "nutriscore_grade": "b",
                "nova_group": 3,
                "quantity": "100g",
                "packaging": "Plastic",
                "labels": "Vegetarian",
                "ingredients_text": "Sugar, cocoa, milk",
                "image_url": "https://example.com/image.jpg",
            }
        ]
    )

    clean_df = clean_product_data(raw_df)

    assert clean_df.loc[0, "product_code"] == "123456"
    assert clean_df.loc[0, "product_name"] == "Sample Product"
    assert clean_df.loc[0, "brand"] == "Sample Brand"
    assert clean_df.loc[0, "main_category"] == "Snacks"
    assert clean_df.loc[0, "country"] == "Germany"
    assert clean_df.loc[0, "has_nutriscore"] is True or clean_df.loc[0, "has_nutriscore"] == True
