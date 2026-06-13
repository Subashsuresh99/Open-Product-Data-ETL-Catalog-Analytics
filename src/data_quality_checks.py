"""
Data quality checks for Open Food Facts product data.
"""

from typing import Dict, List

import pandas as pd


def _build_check(check_name: str, failed_count: int, total_count: int) -> Dict[str, object]:
    return {
        "check_name": check_name,
        "status": "PASS" if failed_count == 0 else "FAIL",
        "failed_count": failed_count,
        "total_count": total_count,
        "failure_rate": round(failed_count / total_count, 4) if total_count else 0,
    }


def run_data_quality_checks(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run data quality checks on cleaned product records.

    Args:
        df: Clean product DataFrame.

    Returns:
        DataFrame with data quality results.
    """
    total_count = len(df)
    results: List[Dict[str, object]] = []

    results.append(
        _build_check(
            "missing_product_name",
            int(df["product_name"].eq("").sum()),
            total_count,
        )
    )

    results.append(
        _build_check(
            "missing_brand",
            int(df["brand"].eq("").sum()),
            total_count,
        )
    )

    results.append(
        _build_check(
            "missing_main_category",
            int(df["main_category"].eq("").sum()),
            total_count,
        )
    )

    results.append(
        _build_check(
            "missing_country",
            int(df["country"].eq("").sum()),
            total_count,
        )
    )

    results.append(
        _build_check(
            "missing_or_invalid_nutriscore",
            int((~df["nutriscore_grade"].isin(["a", "b", "c", "d", "e"])).sum()),
            total_count,
        )
    )

    results.append(
        _build_check(
            "invalid_nova_group",
            int((~df["nova_group"].dropna().between(1, 4)).sum()),
            total_count,
        )
    )

    results.append(
        _build_check(
            "duplicate_product_code",
            int(df["product_code"].duplicated().sum()),
            total_count,
        )
    )

    return pd.DataFrame(results)
