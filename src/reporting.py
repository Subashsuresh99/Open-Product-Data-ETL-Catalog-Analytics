"""
Reporting output generation for product catalog analytics.
"""

import pandas as pd


def create_category_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create category-level product summary.
    """
    summary = (
        df.groupby("main_category", dropna=False)
        .agg(
            product_count=("product_code", "count"),
            unique_brands=("brand", "nunique"),
            products_with_nutriscore=("has_nutriscore", "sum"),
            average_ingredient_text_length=("ingredient_text_length", "mean"),
        )
        .reset_index()
        .rename(columns={"main_category": "category"})
    )

    summary["nutriscore_completeness_rate"] = (
        summary["products_with_nutriscore"] / summary["product_count"]
    ).round(2)

    return summary.sort_values(by="product_count", ascending=False)


def create_brand_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create brand-level summary.
    """
    summary = (
        df.groupby("brand", dropna=False)
        .agg(
            product_count=("product_code", "count"),
            unique_categories=("main_category", "nunique"),
            products_with_nutriscore=("has_nutriscore", "sum"),
        )
        .reset_index()
    )

    summary["brand"] = summary["brand"].replace("", "Unknown")
    summary["nutriscore_completeness_rate"] = (
        summary["products_with_nutriscore"] / summary["product_count"]
    ).round(2)

    return summary.sort_values(by="product_count", ascending=False)


def create_country_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create country-level summary.
    """
    summary = (
        df.groupby("country", dropna=False)
        .agg(
            product_count=("product_code", "count"),
            unique_brands=("brand", "nunique"),
            unique_categories=("main_category", "nunique"),
        )
        .reset_index()
    )

    summary["country"] = summary["country"].replace("", "Unknown")

    return summary.sort_values(by="product_count", ascending=False)
