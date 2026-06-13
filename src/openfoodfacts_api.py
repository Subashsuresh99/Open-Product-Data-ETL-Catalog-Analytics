"""
Open Food Facts API ingestion module.

This module fetches real product data from the Open Food Facts public API.

It uses the current API v2 endpoint:
https://world.openfoodfacts.org/api/v2/search

The code includes retries and fallback query styles because public APIs can
occasionally return temporary 503 errors.
"""

from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API_URL = "https://world.openfoodfacts.org/api/v2/search"

FIELDS = [
    "code",
    "product_name",
    "brands",
    "categories",
    "countries",
    "nutriscore_grade",
    "nutrition_grades",
    "nova_group",
    "quantity",
    "packaging",
    "labels",
    "ingredients_text",
    "image_url",
]


def _create_session() -> requests.Session:
    """
    Create a requests session with retry handling for temporary API failures.
    """
    retry_strategy = Retry(
        total=4,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session = requests.Session()
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update(
        {
            "User-Agent": (
                "open-product-data-etl-catalog-analytics/1.0 "
                "(academic data engineering project; GitHub: Subashsuresh99)"
            )
        }
    )

    return session


def _request_products(
    session: requests.Session,
    params: Dict[str, Any],
) -> Optional[List[Dict[str, Any]]]:
    """
    Request products from the Open Food Facts API.

    Returns:
        List of products if successful, otherwise None.
    """
    try:
        response = session.get(API_URL, params=params, timeout=45)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
        products: List[Dict[str, Any]] = data.get("products", [])
        return products if products else None
    except requests.RequestException as error:
        print(f"API request failed for params {params}: {error}")
        return None


def fetch_products(search_terms: str = "chocolate", page_size: int = 100) -> pd.DataFrame:
    """
    Fetch product data from Open Food Facts API v2.

    Args:
        search_terms: Keyword/category used for collecting products.
                      Examples: chocolate, coffee, pasta, beverages, biscuits.
        page_size: Number of product records to request.

    Returns:
        Raw product records as a pandas DataFrame.
    """
    session = _create_session()
    field_string = ",".join(FIELDS)

    query_attempts = [
        {
            "categories_tags_en": search_terms,
            "page_size": page_size,
            "fields": field_string,
            "sort_by": "last_modified_t",
        },
        {
            "search_terms": search_terms,
            "page_size": page_size,
            "fields": field_string,
            "sort_by": "last_modified_t",
        },
        {
            "categories_tags": search_terms,
            "page_size": page_size,
            "fields": field_string,
            "sort_by": "last_modified_t",
        },
    ]

    for params in query_attempts:
        products = _request_products(session=session, params=params)
        if products:
            print(f"Fetched {len(products)} products from Open Food Facts.")
            return pd.DataFrame(products)

    raise RuntimeError(
        "Could not fetch product data from Open Food Facts after multiple attempts. "
        "This is usually a temporary public API availability issue. "
        "Try again later or reduce the page size, for example: "
        "`python run_pipeline.py --page-size 20 --search-terms chocolate`."
    )
