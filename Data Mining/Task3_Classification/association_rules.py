# association_rules.py
import pandas as pd
import random
import os
import sys
from datetime import datetime
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Configure output directory
OUTPUT_DIR = r"C:\Users\Admin\Desktop\Summer semester 2024\DSA_2040_Practical_Exam_Kevin_656\Data Mining\Task3_Classification\output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    try:
        # 1. Generate synthetic transaction data
        items = ['milk', 'bread', 'eggs', 'cheese', 'butter', 
                'yogurt', 'diapers', 'beer', 'fruit', 'vegetables']
        transactions = [random.sample(items, k=random.randint(3,5)) for _ in range(100)]
        
        # 2. Transform data for Apriori
        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        
        # 3. Mine association rules
        frequent_itemsets = apriori(df, min_support=0.15, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
        top_rules = rules.sort_values('lift', ascending=False).head(10)
        
        # 4. Save results with UTF-8 encoding
        top_rules.to_csv(os.path.join(OUTPUT_DIR, 'association_rules.csv'), 
                        index=False, encoding='utf-8-sig')
        
        # 5. Generate report (ASCII-only for Windows compatibility)
        report = f"""# Association Rule Mining Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

## Top 5 Rules by Lift
{top_rules.head(5).to_string(index=False)}

## Key Insights
1. STRONGEST ASSOCIATION: 
   - When people buy {list(top_rules.iloc[0]['antecedents'])}, they also buy {list(top_rules.iloc[0]['consequents'])}
   - Confidence: {top_rules.iloc[0]['confidence']:.2f}, Lift: {top_rules.iloc[0]['lift']:.2f}

2. MOST FREQUENT ITEMSET: 
   - {list(max(frequent_itemsets['itemsets'], key=lambda x: len(x)))}
   - Support: {max(frequent_itemsets['support']):.2f}
"""
        with open(os.path.join(OUTPUT_DIR, 'association_report.txt'), 
                 'w', encoding='utf-8') as f:
            f.write(report)

        print("SUCCESS! Results saved to:")
        print(f"- {os.path.join(OUTPUT_DIR, 'association_rules.csv')}")
        print(f"- {os.path.join(OUTPUT_DIR, 'association_report.txt')}")

    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()