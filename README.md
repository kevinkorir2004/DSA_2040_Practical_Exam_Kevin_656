# DSA 2040 Practical Exam - Kevin (ID: 656)

## 📝 Overview
This repository contains my submission for the DSA 2040 End Semester Practical Exam covering Data Warehousing and Data Mining concepts. The project demonstrates practical implementation of star schema design, ETL processes, OLAP queries, and data mining techniques.

## 📂 Project Structure
DSA_2040_Practical_Exam_Kevin_656/
├── README.md # This documentation file
├── requirements.txt # Python dependencies
├── Section1_DataWarehousing/ # Data Warehousing tasks (50 marks)
│ ├── Task1_SchemaDesign/ # Star schema design (15 marks)
│ │ ├── schema_design.sql # SQL table definitions
│ │ └── schema_diagram.png # Schema visualization
│ ├── Task2_ETLProcess/ # ETL implementation (20 marks)
│ │ ├── etl_retail.py # Python ETL script
│ │ ├── retail_data.csv # Sample dataset
│ │ └── retail_dw.db # SQLite database
│ └── Task3_OLAPQueries/ # OLAP analysis (15 marks)
│ ├── olap_queries.sql # OLAP SQL queries
│ ├── sales_visualization.png # Sales analysis chart
│ └── olap_analysis.md # Query insights report
└── Section2_DataMining/ # Data Mining tasks (50 marks)
├── Task1_Preprocessing/ # Data preprocessing (15 marks)
│ ├── preprocessing_iris.py # Preprocessing script
│ ├── iris_data.csv # Iris dataset
│ └── visualizations/ # Exploratory visuals
│ ├── pairplot.png # Feature relationships
│ ├── heatmap.png # Correlation matrix
│ └── boxplots.png # Outlier detection
├── Task2_Clustering/ # Clustering (15 marks)
│ ├── clustering_iris.py # K-Means implementation
│ ├── elbow_curve.png # K-selection visual
│ └── clusters.png # Cluster visualization
└── Task3_ClassificationARM/ # Classification & ARM (20 marks)
├── mining_iris_basket.py # Mining scripts
├── decision_tree.png # Classifier visualization
├── transaction_data.csv # Synthetic market basket data
└── rules.txt # Association rules output

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
