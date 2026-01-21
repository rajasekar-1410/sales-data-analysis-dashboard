import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("database/sales.db")

# -----------------------------
# 1. Total Sales & Profit
# -----------------------------
query_total = """
SELECT 
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales;
"""
total_df = pd.read_sql(query_total, conn)
print("\n📊 Total Sales & Profit")
print(total_df)

# -----------------------------
# 2. Sales by Region
# -----------------------------
query_region = """
SELECT 
    Region,
    ROUND(SUM(Sales), 2) AS Region_Sales
FROM sales
GROUP BY Region
ORDER BY Region_Sales DESC;
"""
region_df = pd.read_sql(query_region, conn)
print("\n🌍 Sales by Region")
print(region_df)

# -----------------------------
# 3. Top 10 Products by Sales
# -----------------------------
query_products = """
SELECT 
    "Product Name",
    ROUND(SUM(Sales), 2) AS Product_Sales
FROM sales
GROUP BY "Product Name"
ORDER BY Product_Sales DESC
LIMIT 10;
"""
products_df = pd.read_sql(query_products, conn)
print("\n🏆 Top 10 Products by Sales")
print(products_df)

# -----------------------------
# 4. Monthly Sales Trend
# -----------------------------
query_monthly = """
SELECT 
    substr("Order Date", 1, 7) AS Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales
FROM sales
GROUP BY Month
ORDER BY Month;
"""
monthly_df = pd.read_sql(query_monthly, conn)
print("\n📈 Monthly Sales Trend")
print(monthly_df)

conn.close()
