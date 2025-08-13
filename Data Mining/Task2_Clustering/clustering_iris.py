# clustering_iris.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import (adjusted_rand_score, 
                           silhouette_score, 
                           calinski_harabasz_score)
import os
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages

# =============================================
# CONFIGURATION (YOUR EXACT PATHS)
# =============================================
INPUT_FILE = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Mining\Task1_Preprocessing\iris_visualizations\processed_data.csv"
OUTPUT_DIR = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Mining\Task2_Clustering\output"

# =============================================
# MAIN SCRIPT
# =============================================
def main():
    # 1. Setup environment
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Load and verify data
    try:
        df = pd.read_csv(INPUT_FILE)
        print("SUCCESS: Data loaded with shape", df.shape)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return

    # 3. Prepare data
    X = df.drop('species', axis=1)
    true_labels = df['species'].astype('category').cat.codes
    
    # 4. Clustering analysis
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(X)
    
    # 5. Calculate metrics
    metrics = {
        "Adjusted Rand Index": adjusted_rand_score(true_labels, clusters),
        "Silhouette Score": silhouette_score(X, clusters),
        "Calinski-Harabasz": calinski_harabasz_score(X, clusters),
        "Inertia": kmeans.inertia_
    }

    # 6. Generate visualizations
    with PdfPages(os.path.join(OUTPUT_DIR, 'clustering_report.pdf')) as pdf:
        # Figure 1: Cluster plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=X.iloc[:, 2], y=X.iloc[:, 3], hue=clusters, 
                       palette='viridis', s=100)
        plt.title(f"K-Means Clustering Results\nARI: {metrics['Adjusted Rand Index']:.2f}")
        plt.xlabel("Petal Length (cm)")
        plt.ylabel("Petal Width (cm)")
        pdf.savefig(bbox_inches='tight')
        plt.close()
        
        # Figure 2: Elbow method
        inertias = []
        for k in range(1, 6):
            km = KMeans(n_clusters=k, random_state=42)
            km.fit(X)
            inertias.append(km.inertia_)
            
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, 6), inertias, 'bo-')
        plt.title("Elbow Method for Optimal k")
        plt.xlabel("Number of Clusters")
        plt.ylabel("Inertia")
        pdf.savefig(bbox_inches='tight')
        plt.close()
        
        # Figure 3: Metric comparison
        plt.figure(figsize=(10, 5))
        plt.bar(metrics.keys(), metrics.values(), color=['blue', 'green', 'orange', 'red'])
        plt.title("Clustering Performance Metrics")
        plt.xticks(rotation=45)
        pdf.savefig(bbox_inches='tight')
        plt.close()

    # 7. Generate markdown report
    report = f"""# Task 2: Clustering Analysis Report

**Date**: {timestamp}  
**Dataset**: Iris (preprocessed)  
**Algorithm**: K-Means Clustering  

## Results Summary
| Metric | Value |
|--------|-------|
| Adjusted Rand Index | {metrics['Adjusted Rand Index']:.2f} |
| Silhouette Score | {metrics['Silhouette Score']:.2f} |
| Calinski-Harabasz | {metrics['Calinski-Harabasz']:.2f} |
| Inertia | {metrics['Inertia']:.2f} |

## Interpretation
- **ARI = {metrics['Adjusted Rand Index']:.2f}**: {
    'Excellent match with true labels' if metrics['Adjusted Rand Index'] > 0.8 
    else 'Good match' if metrics['Adjusted Rand Index'] > 0.5 
    else 'Poor match'
}
- **Silhouette = {metrics['Silhouette Score']:.2f}**: {
    'Strong cluster separation' if metrics['Silhouette Score'] > 0.7 
    else 'Moderate separation' if metrics['Silhouette Score'] > 0.5 
    else 'Weak separation'
}

![Cluster Visualization](cluster_results.png)
![Elbow Method](elbow_plot.png)

## Recommendations
1. Use petal measurements as primary clustering features
2. Consider DBSCAN for density-based clustering alternatives
3. Validate with domain experts for biological significance
"""

    with open(os.path.join(OUTPUT_DIR, 'report.md'), 'w') as f:
        f.write(report)

    print("\nTASK COMPLETED!")
    print(f"PDF Report: {os.path.join(OUTPUT_DIR, 'clustering_report.pdf')}")
    print(f"Markdown Report: {os.path.join(OUTPUT_DIR, 'report.md')}")

if __name__ == "__main__":
    main()