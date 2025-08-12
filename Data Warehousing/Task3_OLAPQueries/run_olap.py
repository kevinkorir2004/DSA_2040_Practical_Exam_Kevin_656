import sqlite3
import pandas as pd
import os

# ABSOLUTE PATHS (EDIT THESE)
DB_PATH = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Warehousing\Task2_ETLProcess\retail_dw.db"
OUTPUT_FILE = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Warehousing\Task3_OLAPQueries\olap_results.txt"

def verify_database():
    """Check if database exists and has data"""
    if not os.path.exists(DB_PATH):
        print(f"❌ ERROR: Database not found at:\n{DB_PATH}")
        print("Solution: Re-run the ETL script (etl_retail.py)")
        return False
    
    try:
        conn = sqlite3.connect(DB_PATH)
        row_count = conn.execute("SELECT COUNT(*) FROM SalesFact").fetchone()[0]
        conn.close()
        if row_count == 0:
            print("❌ ERROR: SalesFact table is empty!")
            return False
        print(f"✅ Verified: Database exists with {row_count} rows")
        return True
    except Exception as e:
        print(f"❌ Database verification failed: {str(e)}")
        return False

def run_queries():
    """Execute OLAP queries"""
    try:
        conn = sqlite3.connect(DB_PATH)
        queries = [
            ("Sales by Country/Quarter", """
            SELECT Country, strftime('%Y-Q%q', InvoiceDate) AS Quarter,
                   SUM(TotalSales) AS TotalSales
            FROM SalesFact
            GROUP BY Country, Quarter
            ORDER BY Country, Quarter
            """),
            
            ("UK Monthly Sales", """
            SELECT strftime('%Y-%m', InvoiceDate) AS Month,
                   Description, 
                   SUM(Quantity) AS TotalQuantity,
                   SUM(TotalSales) AS TotalSales 
            FROM SalesFact
            WHERE Country = 'United Kingdom'
            GROUP BY Month, Description
            ORDER BY Month
            """)
        ]
        
        with open(OUTPUT_FILE, 'w') as f:
            for name, query in queries:
                df = pd.read_sql_query(query, conn)
                f.write(f"\n=== {name} ===\n")
                f.write(df.to_string(index=False))
                f.write("\n")
                print(f"✔ {name} - Returned {len(df)} rows")
        
        conn.close()
        print(f"\n✅ Results saved to:\n{OUTPUT_FILE}")
    except Exception as e:
        print(f"❌ Query execution failed: {str(e)}")

if __name__ == "__main__":
    print(f"Database path:\n{DB_PATH}")
    if verify_database():
        run_queries()
    else:
        print("\nFix the database first before running queries.")