"""
SQLite loading module.
"""

import sqlite3
from pathlib import Path

import pandas as pd


def load_to_sqlite(clean_df: pd.DataFrame, dq_report: pd.DataFrame, db_path: Path) -> None:
    """
    Load cleaned data and data quality report into SQLite.

    Args:
        clean_df: Clean product DataFrame.
        dq_report: Data quality report DataFrame.
        db_path: SQLite database path.
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        clean_df.to_sql("products", conn, if_exists="replace", index=False)
        dq_report.to_sql("data_quality_report", conn, if_exists="replace", index=False)
