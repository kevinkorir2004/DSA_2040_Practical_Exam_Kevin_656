# DSA 2040 Practical Exam - Kevin (ID: 656)

## 📝 Overview
This repository contains my submission for the DSA 2040 End Semester Practical Exam covering Data Warehousing and Data Mining concepts. The project demonstrates practical implementation of star schema design, ETL processes, OLAP queries, and data mining techniques.

## 📂 Project Structure
DSA_2040_Practical_Exam_Kevin_656/
├── Data Mining/
│ ├── Task1_Preprocessing/
│ │ ├── preprocessing_iris.py
│ │ └── output/ (processed_data.csv, visualizations)
│ ├── Task2_Clustering/
│ │ ├── clustering_iris.py
│ │ └── output/ (cluster_results.png, elbow_plot.png)
│ └── Task3_Classification/
│ ├── classification_iris.py
│ ├── association_rules.py
│ └── output/ (decision_tree.png, association_rules.csv)
└── README.md

## Task 1: Data Warehouse Design

**Schema Type:** Star Schema

**Why Star Schema?**  
The star schema is denormalized, making queries faster and easier for OLAP operations.  
It simplifies joins between fact and dimensions, which is ideal for analytics and reporting.  
A snowflake schema would require more joins, increasing complexity without much benefit in this case.

### **Task 2: ETL Process**
- Generated synthetic retail data (1000 records)  
- Transformed and loaded to SQLite: [`retail_dw.db`](Data%20Warehousing/Task2_ETLProcess/retail_dw.db)  
- ETL script: [`etl_retail.py`](Data%20Warehousing/Task2_ETLProcess/etl_retail.py)

### **Task 3: OLAP Analysis** *(New!)*
- Executed 3 OLAP queries:  
  - Roll-up (sales by country/quarter)  
  - Drill-down (UK monthly sales)  
  - Slice (electronics category)  
- Visualization:  
  ![Quarterly Sales](Data%20Warehousing/Task3_OLAPQueries/sales_by_country.png)  
- Full analysis: [`analysis_report.md`](Data%20Warehousing/Task3_OLAPQueries/analysis_report.md)

  ## Section 2: Data Mining

### Task 1: Preprocessing & Exploration
- **Script**: `preprocessing_iris.py`  
- **Outputs**:  
  - Normalized dataset (`iris_processed.csv`)  
  - Visualizations (`pairplot.png`, `heatmap.png`)  
  - Summary statistics (`summary_stats.csv`)  

### Task 2: Clustering (Upcoming)
- Will apply K-Means to identify species clusters  
- Metrics: Adjusted Rand Index (ARI)  
- Output: Cluster visualization  


### 🔍 Dataset Sources
| Task | Data Type | Source | Rows | Columns |
|------|-----------|--------|------|---------|
| 1 | Iris | Scikit-learn | 150 | 5 |
| 2 | Retail | Synthetic (Faker) | 1000 | 8 |
| 3 | Market Basket | Synthetic | 50 | 10 |

## Marking Scheme Alignment
| Criteria | Evidence Location |
|----------|-------------------|
| Data Preprocessing (15) | Task1_Preprocessing/output/ |
| Clustering (15) | Task2_Clustering/clustering_iris.py |
| Classification (10) | Task3_Classification/classification_iris.py |
| Association Rules (10) | Task3_Classification/association_rules.py | 
| Documentation (10) | README.md |

### 🚀 Execution Guide
1. Clone repository:
   ```bash
   git clone https://github.com/kevinkorir2004/DSA_2040_Practical_Exam_Kevin_656.git
   cd DSA_2040_Practical_Exam_Kevin_656

# Data Mining Tasks
python "Data Mining/Task1_Preprocessing/preprocessing_iris.py"
python "Data Mining/Task2_Clustering/clustering_iris.py"
python "Data Mining/Task3_Classification/classification_iris.py"
python "Data Mining/Task3_Classification/association_rules.py"

**How to implement:**
1. Open your `README.md` file
2. Paste this at the **bottom** of the file
3. Customize the:
   - Known Issues (if any)
   - Self-Assessment percentages
   - Add/remove visualization images as needed

**Final verification steps:**
1. Check all hyperlinks work
2. Verify image paths match your actual files
3. Ensure the directory structure reflects your actual repo

  
