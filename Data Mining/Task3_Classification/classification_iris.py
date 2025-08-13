# classification_iris.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (accuracy_score, precision_score, 
                           recall_score, f1_score)
from sklearn.model_selection import train_test_split
import os
import sys

# =============================================
# CONFIGURATION (UPDATE THESE PATHS)
# =============================================
INPUT_FILE = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Mining\Task1_Preprocessing\iris_visualizations\processed_data.csv"
OUTPUT_DIR = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Mining\Task3_Classification\output"

def main():
    print("=== SCRIPT STARTED ===")
    
    # 1. Verify and create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"[1/5] Output directory ready: {OUTPUT_DIR}")
    print(f"Directory writable: {os.access(OUTPUT_DIR, os.W_OK)}")

    # 2. Load data
    try:
        print(f"[2/5] Loading data from: {INPUT_FILE}")
        df = pd.read_csv(INPUT_FILE)
        print(f"Data loaded successfully! Shape: {df.shape}")
    except Exception as e:
        print(f"ERROR LOADING DATA: {str(e)}", file=sys.stderr)
        return

    # 3. Prepare data
    X = df.drop('species', axis=1)
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("[3/5] Data split complete")

    # 4. Train models
    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=3),
        "KNN": KNeighborsClassifier(n_neighbors=5)
    }
    
    results = {}
    for name, model in models.items():
        print(f"[4/5] Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        results[name] = {
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred, average='weighted'),
            "Recall": recall_score(y_test, y_pred, average='weighted'),
            "F1": f1_score(y_test, y_pred, average='weighted')
        }
        
        # Save decision tree visualization
        if name == "Decision Tree":
            plt.figure(figsize=(20,10))
            plot_tree(model, feature_names=X.columns, 
                     class_names=y.unique(), filled=True)
            tree_path = os.path.join(OUTPUT_DIR, 'decision_tree.png')
            plt.savefig(tree_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Decision tree saved to: {tree_path}")

    # 5. Save results
    report_path = os.path.join(OUTPUT_DIR, 'classification_report.txt')
    with open(report_path, 'w') as f:
        f.write("=== CLASSIFICATION RESULTS ===\n")
        for model_name, metrics in results.items():
            f.write(f"\n{model_name}:\n")
            for metric, value in metrics.items():
                f.write(f"{metric}: {value:.4f}\n")
    
    print(f"[5/5] Report saved to: {report_path}")
    print("=== SCRIPT COMPLETED SUCCESSFULLY ===")
    print(f"Files generated in {OUTPUT_DIR}: {os.listdir(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()