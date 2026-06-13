# Troubleshooting

## Pandas installation error on Windows

If you see an error like:

```text
Preparing metadata (pyproject.toml) ... error
Could not find Microsoft Visual Studio
```

it usually means pip is trying to build pandas from source instead of installing a ready-made wheel.

### Fix

Upgrade pip first:

```bash
python -m pip install --upgrade pip setuptools wheel
```

Then install dependencies again:

```bash
pip install -r requirements.txt
```

This project uses:

```text
pandas>=2.2.3
```

because pandas 2.2.3 and newer versions provide better compatibility with Python 3.13.

### Run the pipeline

```bash
python run_pipeline.py --page-size 100 --search-terms chocolate
```

### If it still fails

Install Python 3.12 64-bit from python.org, create a new virtual environment, and run the commands again.


## HTTP 503 from Open Food Facts

If you see:

```text
HTTPError: 503 Server Error: Service Temporarily Unavailable
```

it means the API service is temporarily unavailable or the legacy endpoint is being used.

This project should use:

```text
https://world.openfoodfacts.org/api/v2/search
```

Check `src/openfoodfacts_api.py` and confirm:

```python
API_URL = "https://world.openfoodfacts.org/api/v2/search"
```

Then retry:

```bash
python run_pipeline.py --page-size 50 --search-terms chocolate
```

You can also try:

```bash
python run_pipeline.py --page-size 50 --search-terms coffee
python run_pipeline.py --page-size 50 --search-terms pasta
python run_pipeline.py --page-size 50 --search-terms beverages
```


## Still seeing HTTP 503

If you still see a 503 error, first confirm that your file uses the updated API code.

Open:

```text
src/openfoodfacts_api.py
```

Confirm this line exists:

```python
API_URL = "https://world.openfoodfacts.org/api/v2/search"
```

Also confirm your traceback URL does **not** contain the old parameters:

```text
search_simple=1&action=process&json=1
```

If your traceback still contains those old parameters, you are running the old folder.

Try smaller requests:

```bash
python run_pipeline.py --page-size 20 --search-terms chocolate
python run_pipeline.py --page-size 20 --search-terms coffee
python run_pipeline.py --page-size 20 --search-terms pasta
```

Public APIs can be temporarily unavailable. If all categories return 503, wait a few minutes and retry.
