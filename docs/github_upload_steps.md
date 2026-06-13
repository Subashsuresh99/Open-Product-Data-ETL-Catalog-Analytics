# GitHub Upload Steps

## Repository Name

```text
open-product-data-etl-catalog-analytics
```

## Description

```text
Python ETL pipeline using real Open Food Facts product data for catalog analytics
```

## Upload Using GitHub Website

1. Go to GitHub.
2. Click **New repository**.
3. Use the repository name above.
4. Select **Public**.
5. Do not add a README because this project already includes one.
6. Click **Create repository**.
7. Click **uploading an existing file**.
8. Upload all files and folders from this project folder.
9. Click **Commit changes**.

## Upload Using Git Commands

```bash
cd open-product-data-etl-catalog-analytics
git init
git add .
git commit -m "Initial commit: Open Food Facts ETL pipeline"
git branch -M main
git remote add origin https://github.com/Subashsuresh99/open-product-data-etl-catalog-analytics.git
git push -u origin main
```

## After Running the Pipeline

Run:

```bash
python run_pipeline.py --page-size 100 --search-terms chocolate
```

Then commit the generated real data outputs:

```bash
git add data reports
git commit -m "Add Open Food Facts ETL output files"
git push
```
