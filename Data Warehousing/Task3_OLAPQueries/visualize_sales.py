import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import os

# ===== CONFIG =====
DB_PATH = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Warehousing\Task2_ETLProcess\retail_dw.db"
OUTPUT_IMAGE = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Warehousing\Task3_OLAPQueries\sales_by_country.png"

# ===== VERIFICATION =====
if not os.path.exists(DB_PATH):
    print(f"❌ ERROR: Database not found at:\n{DB_PATH}")
    print("Solution: Re-run etl_retail.py in Task2_ETLProcess")
    exit()

# ===== VISUALIZATION =====
try:
    # 1. Connect to database
    conn = sqlite3.connect(DB_PATH)
    
    # 2. Execute query
    query = """
    SELECT 
        Country, 
        strftime('%Y-Q%q', InvoiceDate) AS Quarter,
        SUM(TotalSales) AS TotalSales
    FROM SalesFact
    GROUP BY Country, Quarter
    ORDER BY Quarter, Country
    """
    df = pd.read_sql_query(query, conn)
    
    # 3. Create visualization
    plt.figure(figsize=(12, 6))
    df.pivot(index='Quarter', columns='Country', values='TotalSales').plot(
        kind='bar',
        stacked=True,
        colormap='viridis'
    )
    
    plt.title('Quarterly Sales by Country', fontweight='bold')
    plt.ylabel('Total Sales (USD)', fontsize=10)
    plt.xlabel('Quarter', fontsize=10)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # 4. Save and show
    plt.savefig(OUTPUT_IMAGE, dpi=300)
    print(f"✅ Visualization saved to:\n{OUTPUT_IMAGE}")
    plt.show()
    
except Exception as e:
    print(f"❌ Error during visualization: {str(e)}")
    if 'df' in locals():
        print("\nSample data retrieved:", df.head())
finally:
    if 'conn' in locals():
        conn.close()