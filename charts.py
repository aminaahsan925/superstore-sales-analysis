# ============================================================
# SUPERSTORE SALES ANALYSIS — CHARTS
# By: Amina | CS Student | Data Analysis Portfolio Project
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ---- Recreate the dataset (same as analysis.py) ----
data = {
    'Order_ID':    ['CA-001','CA-002','CA-003','CA-004','CA-005',
                    'CA-006','CA-007','CA-008','CA-009','CA-010',
                    'CA-011','CA-012','CA-013','CA-014','CA-015',
                    'CA-016','CA-017','CA-018','CA-019','CA-020'],

    'Order_Date':  ['2023-01-05','2023-01-12','2023-02-03','2023-02-18','2023-03-07',
                    '2023-03-22','2023-04-11','2023-04-28','2023-05-15','2023-05-30',
                    '2023-06-08','2023-06-25','2023-07-14','2023-07-29','2023-08-10',
                    '2023-08-27','2023-09-05','2023-09-20','2023-10-11','2023-11-03'],

    'Region':      ['East','West','Central','East','West',
                    'South','Central','West','East','South',
                    'West','East','Central','South','West',
                    'East','South','Central','West','East'],

    'Category':    ['Furniture','Technology','Office Supplies','Technology','Furniture',
                    'Office Supplies','Technology','Furniture','Office Supplies','Technology',
                    'Furniture','Technology','Office Supplies','Furniture','Technology',
                    'Office Supplies','Technology','Furniture','Office Supplies','Technology'],

    'Sub_Category':['Chairs','Phones','Paper','Laptops','Tables',
                    'Binders','Accessories','Bookcases','Envelopes','Monitors',
                    'Chairs','Phones','Paper','Tables','Laptops',
                    'Binders','Accessories','Bookcases','Envelopes','Monitors'],

    'Sales':       [1200, 850, 150, 2500, 900,
                    200,  450, 780, 90,  1800,
                    1100, 920, 130, 860, 2700,
                    175,  480, 810, 95,  1950],

    'Quantity':    [3, 2, 5, 1, 2,
                    8, 3, 2, 10, 1,
                    2, 2, 6, 2, 1,
                    7, 3, 2, 9, 1],

    'Discount':    [0.1, 0.0, 0.2, 0.0, 0.3,
                    0.1, 0.0, 0.2, 0.0, 0.1,
                    0.1, 0.0, 0.2, 0.3, 0.0,
                    0.1, 0.0, 0.2, 0.0, 0.1],

    'Profit':      [300, 200, 20,  800, -150,
                    40,  120, 80,  15,  500,
                    280, 230, 18,  -200, 850,
                    35,  130, 90,  12,  520],

    'Customer_Segment': ['Consumer','Corporate','Consumer','Corporate','Home Office',
                         'Consumer','Corporate','Consumer','Home Office','Corporate',
                         'Consumer','Corporate','Consumer','Home Office','Corporate',
                         'Consumer','Corporate','Home Office','Consumer','Corporate']
}

df = pd.DataFrame(data)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.month
df['Month_Name'] = df['Order_Date'].dt.strftime('%b')
df['Year'] = df['Order_Date'].dt.year

# Set visual style — makes all charts look professional
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['font.size'] = 11

# ============================================================
# CHART 1 — Sales by Category (Bar Chart)
# ============================================================
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure()
bars = plt.bar(category_sales.index, category_sales.values,
               color=['#4C72B0','#DD8452','#55A868'], edgecolor='white', linewidth=1.2)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 50,
             f'${height:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.title('Total Sales by Category', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Category')
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('chart1_sales_by_category.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 1 saved — Sales by Category")

# ============================================================
# CHART 2 — Profit by Region (Horizontal Bar)
# ============================================================
region_profit = df.groupby('Region')['Profit'].sum().sort_values()

colors = ['#d73027' if x < 0 else '#4CAF50' for x in region_profit.values]

plt.figure()
bars = plt.barh(region_profit.index, region_profit.values, color=colors, edgecolor='white')

for bar, val in zip(bars, region_profit.values):
    plt.text(val + 10, bar.get_y() + bar.get_height()/2,
             f'${val:,.0f}', va='center', fontweight='bold')

plt.title('Total Profit by Region', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Total Profit ($)')
plt.ylabel('Region')
plt.axvline(x=0, color='black', linewidth=0.8, linestyle='--')
plt.tight_layout()
plt.savefig('chart2_profit_by_region.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 2 saved — Profit by Region")

# ============================================================
# CHART 3 — Monthly Sales Trend (Line Chart)
# ============================================================
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

plt.figure()
plt.plot(monthly_sales['Month'], monthly_sales['Sales'],
         marker='o', linewidth=2.5, color='#4C72B0',
         markerfacecolor='white', markeredgewidth=2, markersize=8)

plt.fill_between(monthly_sales['Month'], monthly_sales['Sales'],
                 alpha=0.1, color='#4C72B0')

for _, row in monthly_sales.iterrows():
    plt.text(row['Month'], row['Sales'] + 30, f"${row['Sales']:,.0f}",
             ha='center', fontsize=9)

plt.title('Monthly Sales Trend (2023)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(monthly_sales['Month'],
           ['Jan','Feb','Mar','Apr','May','Jun',
            'Jul','Aug','Sep','Oct','Nov'])
plt.tight_layout()
plt.savefig('chart3_monthly_sales_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 3 saved — Monthly Sales Trend")

# ============================================================
# CHART 4 — Discount vs Profit (Scatter Plot)
# ============================================================
plt.figure()
colors_scatter = df['Profit'].apply(lambda x: '#d73027' if x < 0 else '#4CAF50')

plt.scatter(df['Discount'], df['Profit'],
            c=colors_scatter, s=100, alpha=0.8, edgecolors='white', linewidth=1)

plt.axhline(y=0, color='black', linewidth=0.8, linestyle='--', alpha=0.5)
plt.title('Discount vs Profit (Does more discount = more loss?)',
          fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Discount Rate')
plt.ylabel('Profit ($)')

# Add legend manually
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#4CAF50', label='Profitable'),
                   Patch(facecolor='#d73027', label='Loss')]
plt.legend(handles=legend_elements)
plt.tight_layout()
plt.savefig('chart4_discount_vs_profit.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 4 saved — Discount vs Profit")

# ============================================================
# CHART 5 — Sales by Customer Segment (Pie Chart)
# ============================================================
segment_sales = df.groupby('Customer_Segment')['Sales'].sum()

plt.figure(figsize=(7,7))
colors_pie = ['#4C72B0','#DD8452','#55A868']
wedges, texts, autotexts = plt.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct='%1.1f%%',
    colors=colors_pie,
    startangle=140,
    wedgeprops={'edgecolor':'white','linewidth':2}
)

for text in autotexts:
    text.set_fontweight('bold')

plt.title('Sales Distribution by Customer Segment',
          fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('chart5_sales_by_segment.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Chart 5 saved — Sales by Segment")

print("\n🎉 All 5 charts saved as PNG files in your project folder!")
print("📁 Check the left file panel — you'll see 5 new .png files")git add .