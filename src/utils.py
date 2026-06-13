"""
Utility helpers.
"""

from pathlib import Path

import pandas as pd


def save_dataframe(df: pd.DataFrame, path: Path) -> None:
    """
    Save a DataFrame as CSV.

    Args:
        df: DataFrame to save.
        path: Target file path.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
