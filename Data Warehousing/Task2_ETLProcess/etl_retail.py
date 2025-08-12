import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import random
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_synthetic_data(num_rows=1000):
    """Generate synthetic retail data without Faker"""
    products = [
        ("Laptop", "Electronics", 999.99),
        ("T-Shirt", "Clothing", 19.99),
        ("Smartphone", "Electronics", 699.99)
    ]
    countries = ["UK", "US", "Germany", "Kenya", "France"]
    
    data = {
        "InvoiceNo": [f"INV{10000+i}" for i in range(num_rows)],
        "StockCode": [f"SKU{20000+i}" for i in range(num_rows)],
        "Description": [random.choice(products)[0] for _ in range(num_rows)],
        "Quantity": [random.randint(1, 10) for _ in range(num_rows)],
        "InvoiceDate": [datetime(2024, random.randint(1,12), random.randint(1,28)) for _ in range(num_rows)],
        "UnitPrice": [random.choice(products)[2] for _ in range(num_rows)],
        "CustomerID": [f"CUST{30000+i}" for i in range(num_rows)],
        "Country": [random.choice(countries) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

def extract_data():
    """Extract data - generate synthetic data"""
    df = generate_synthetic_data()
    logger.info(f"Extracted {len(df)} rows of data.")
    return df

def transform_data(df):
    """Transform the raw data"""
    # Calculate TotalSales
    df["TotalSales"] = df["Quantity"] * df["UnitPrice"]
    
    # Filter for the last year (assuming current date is August 12, 2025)
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    last_year = pd.Timestamp("2024-08-12")
    df = df[df["InvoiceDate"] >= last_year]
    
    # Remove outliers
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    
    logger.info(f"Transformed data: {len(df)} rows remaining.")
    return df

def load_data(df):
    """Load data into SQLite database"""
    conn = None
    try:
        # Absolute path to ensure proper file location
        db_path = os.path.join(os.path.dirname(__file__), "retail_dw.db")
        logger.info(f"Database path: {db_path}")
        
        conn = sqlite3.connect(db_path)
        
        # Create table
        conn.execute("""
        CREATE TABLE IF NOT EXISTS SalesFact (
            invoice_no TEXT,
            stock_code TEXT,
            description TEXT,
            quantity INTEGER,
            unit_price REAL,
            total_sales REAL,
            customer_id TEXT,
            country TEXT,
            invoice_date TEXT
        )
        """)
        
        # Insert data
        df.to_sql("SalesFact", conn, if_exists="replace", index=False)
        conn.commit()
        logger.info("Data successfully loaded!")
        return True
        
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return False
    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed.")

def run_etl_pipeline():
    """Run the complete ETL pipeline"""
    try:
        logger.info("Starting ETL pipeline...")
        # Extract
        raw_data = extract_data()
        # Transform
        transformed_data = transform_data(raw_data)
        # Load
        if load_data(transformed_data):
            # Verify file creation
            db_path = os.path.join(os.path.dirname(__file__), "retail_dw.db")
            if os.path.exists(db_path):
                logger.info(f"✅ Database verified at: {db_path}")
                logger.info(f"File size: {os.path.getsize(db_path)} bytes")
            else:
                logger.error("❌ Database file not found after creation!")
        logger.info("ETL pipeline completed!")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}")
        raise

if __name__ == "__main__":
    run_etl_pipeline()
