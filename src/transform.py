"""
Transformation module for Open Food Facts product data.
"""

import pandas as pd


def _clean_text(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def _first_item_from_comma_list(value: object) -> str:
    value = _clean_text(value)
    if not value:
        return ""
    return value.split(",")[0].strip()


def _ingredient_length(value: object) -> int:
    value = _clean_text(value)
    return len(value)


def clean_product_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw Open Food Facts product records.

    Args:
        raw_df: Raw product records from the API.

    Returns:
        Cleaned and analytics-ready product DataFrame.
    """
    df = raw_df.copy()

    required_columns = [
        "code",
        "product_name",
        "brands",
        "categories",
        "countries",
        "nutriscore_grade",
        "nova_group",
        "quantity",
        "packaging",
        "labels",
        "ingredients_text",
        "image_url",
    ]

    for column in required_columns:
        if column not in df.columns:
            df[column] = ""

    clean_df = pd.DataFrame()
    clean_df["product_code"] = df["code"].apply(_clean_text)
    clean_df["product_name"] = df["product_name"].apply(_clean_text)
    clean_df["brand"] = df["brands"].apply(_first_item_from_comma_list)
    clean_df["main_category"] = df["categories"].apply(_first_item_from_comma_list)
    clean_df["country"] = df["countries"].apply(_first_item_from_comma_list)
    clean_df["nutriscore_grade"] = df["nutriscore_grade"].apply(_clean_text).str.lower()
    clean_df["nova_group"] = pd.to_numeric(df["nova_group"], errors="coerce")
    clean_df["quantity"] = df["quantity"].apply(_clean_text)
    clean_df["packaging"] = df["packaging"].apply(_clean_text)
    clean_df["labels"] = df["labels"].apply(_clean_text)
    clean_df["ingredients_text"] = df["ingredients_text"].apply(_clean_text)
    clean_df["ingredient_text_length"] = df["ingredients_text"].apply(_ingredient_length)
    clean_df["image_url"] = df["image_url"].apply(_clean_text)

    clean_df["has_product_name"] = clean_df["product_name"].ne("")
    clean_df["has_brand"] = clean_df["brand"].ne("")
    clean_df["has_category"] = clean_df["main_category"].ne("")
    clean_df["has_country"] = clean_df["country"].ne("")
    clean_df["has_nutriscore"] = clean_df["nutriscore_grade"].isin(["a", "b", "c", "d", "e"])

    clean_df = clean_df.drop_duplicates(subset=["product_code"])
    clean_df = clean_df.sort_values(by=["main_category", "brand", "product_name"]).reset_index(drop=True)

    return clean_df
