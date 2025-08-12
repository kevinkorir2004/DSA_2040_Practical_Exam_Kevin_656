-- Time Dimension
CREATE TABLE TimeDim (
    date_key INTEGER PRIMARY KEY, -- Format YYYYMMDD
    date TEXT,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);

-- Customer Dimension
CREATE TABLE CustomerDim (
    customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id TEXT UNIQUE,
    name TEXT,
    gender TEXT,
    age INTEGER,
    country TEXT
);

-- Product Dimension
CREATE TABLE ProductDim (
    product_key INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT UNIQUE,
    product_name TEXT,
    category TEXT,
    price REAL
);

-- Store Dimension
CREATE TABLE StoreDim (
    store_key INTEGER PRIMARY KEY AUTOINCREMENT,
    store_id TEXT UNIQUE,
    store_name TEXT,
    city TEXT,
    country TEXT
);

-- Fact Table
CREATE TABLE SalesFact (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_key INTEGER,
    product_key INTEGER,
    customer_key INTEGER,
    store_key INTEGER,
    quantity INTEGER,
    unit_price REAL,
    total_sales REAL,
    FOREIGN KEY (date_key) REFERENCES TimeDim(date_key),
    FOREIGN KEY (product_key) REFERENCES ProductDim(product_key),
    FOREIGN KEY (customer_key) REFERENCES CustomerDim(customer_key),
    FOREIGN KEY (store_key) REFERENCES StoreDim(store_key)
);
