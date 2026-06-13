DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_code TEXT,
    product_name TEXT,
    brand TEXT,
    main_category TEXT,
    country TEXT,
    nutriscore_grade TEXT,
    nova_group REAL,
    quantity TEXT,
    packaging TEXT,
    labels TEXT,
    ingredients_text TEXT,
    ingredient_text_length INTEGER,
    image_url TEXT,
    has_product_name BOOLEAN,
    has_brand BOOLEAN,
    has_category BOOLEAN,
    has_country BOOLEAN,
    has_nutriscore BOOLEAN
);

DROP TABLE IF EXISTS data_quality_report;

CREATE TABLE data_quality_report (
    check_name TEXT,
    status TEXT,
    failed_count INTEGER,
    total_count INTEGER,
    failure_rate REAL
);
