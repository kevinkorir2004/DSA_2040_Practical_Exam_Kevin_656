# preprocessing_iris.py - Complete Data Preprocessing Script
import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def main():
    try:
        # 1. SETUP OUTPUT DIRECTORY
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, "output")
        os.makedirs(output_dir, exist_ok=True)
        
        print("="*50)
        print("IRIS DATASET PREPROCESSING SCRIPT")
        print(f"All outputs will be saved to: {output_dir}")
        print("="*50 + "\n")

        # 2. LOAD DATA
        print("[1/4] Loading Iris dataset...")
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        df['species'] = iris.target_names[iris.target]
        
        # 3. PREPROCESSING
        print("\n[2/4] Preprocessing data...")
        # Handle missing values
        if df.isnull().sum().sum() > 0:
            print(" - Found missing values, filling with median...")
            df = df.fillna(df.median())
        else:
            print(" - No missing values found")
        
        # Normalize features
        print(" - Normalizing features...")
        scaler = MinMaxScaler()
        features = iris.feature_names
        df[features] = scaler.fit_transform(df[features])
        
        # 4. EXPLORATORY ANALYSIS
        print("\n[3/4] Performing exploratory analysis...")
        # Summary statistics
        stats = df.describe()
        stats.to_csv(os.path.join(output_dir, "summary_stats.csv"))
        print(" - Saved summary statistics to 'summary_stats.csv'")
        
        # Visualizations
        plt.figure(figsize=(12,8))
        sns.pairplot(df, hue='species', palette='viridis')
        plt.savefig(os.path.join(output_dir, "pairplot.png"), bbox_inches='tight')
        plt.close()
        print(" - Saved pairplot to 'pairplot.png'")
        
        plt.figure(figsize=(10,8))
        sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm')
        plt.title('Feature Correlation Heatmap')
        plt.savefig(os.path.join(output_dir, "heatmap.png"), bbox_inches='tight')
        plt.close()
        print(" - Saved heatmap to 'heatmap.png'")
        
        # 5. SPLIT DATA
        print("\n[4/4] Splitting data...")
        X_train, X_test, y_train, y_test = train_test_split(
            df[features], df['species'], test_size=0.2, random_state=42
        )
        
        # Save processed data
        df.to_csv(os.path.join(output_dir, "processed_data.csv"), index=False)
        print(" - Saved processed data to 'processed_data.csv'")
        
        print("\n" + "="*50)
        print("PREPROCESSING COMPLETED SUCCESSFULLY!")
        print(f"Check {output_dir} for all output files")
        print("="*50)
        
    except Exception as e:
        print("\nERROR:", str(e))
        print("Script failed. Check your Python environment and dependencies.")
        sys.exit(1)

if __name__ == "__main__":
    main()
