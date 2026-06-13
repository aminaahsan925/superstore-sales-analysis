# ============================================================
# SUPERSTORE SALES ANALYSIS
# By: Amina | CS Student | Data Analysis Portfolio Project
# ============================================================

# ---- STEP 1: Import Libraries ----
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("✅ Libraries imported successfully!")

# ---- STEP 2: Create the Dataset (no download needed) ----
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

# Turn this dictionary into a DataFrame (like an Excel table in Python)
df = pd.DataFrame(data)

print("✅ Dataset created successfully!")
print(f"📊 Total rows: {len(df)}")
print(f"📋 Total columns: {len(df.columns)}")

# ---- STEP 3: Data Cleaning ----
print("\n--- DATA CLEANING ---")

# Convert Order_Date from text to actual date format
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Extract Month and Year as separate columns (useful for trend analysis)
df['Month'] = df['Order_Date'].dt.month
df['Month_Name'] = df['Order_Date'].dt.strftime('%b')  # Jan, Feb, Mar etc
df['Year'] = df['Order_Date'].dt.year

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check for duplicate rows
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Data types of each column
print("\nData types:")
print(df.dtypes)

# ---- STEP 4: Exploratory Data Analysis (EDA) ----
print("\n--- EXPLORATORY DATA ANALYSIS ---")

# Basic statistics (mean, min, max etc)
print("\nBasic statistics for numerical columns:")
print(df[['Sales', 'Quantity', 'Discount', 'Profit']].describe().round(2))

# Total sales and profit
print(f"\n💰 Total Sales:  ${df['Sales'].sum():,.0f}")
print(f"📈 Total Profit: ${df['Profit'].sum():,.0f}")
print(f"📉 Loss-making orders: {len(df[df['Profit'] < 0])}")

# Sales by Region
print("\nSales by Region:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

# Sales by Category
print("\nSales by Category:")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

print("\n✅ EDA complete! Run charts.py next.")