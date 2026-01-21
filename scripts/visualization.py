import matplotlib
matplotlib.use("Agg")  
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd


# Connect to database
conn = sqlite3.connect("database/sales.db")

# -----------------------------
# 1. Sales by Region (Bar Chart)
# -----------------------------
query_region = """
SELECT 
    Region,
    SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region;
"""
region_df = pd.read_sql(query_region, conn)

plt.figure()
plt.bar(region_df["Region"], region_df["Total_Sales"])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_region.png")
plt.close()

# -----------------------------
# 2. Monthly Sales Trend (Line Chart)
# -----------------------------
query_monthly = """
SELECT 
    substr("Order Date", 1, 7) AS Month,
    SUM(Sales) AS Monthly_Sales
FROM sales
GROUP BY Month
ORDER BY Month;
"""
monthly_df = pd.read_sql(query_monthly, conn)

plt.figure()
plt.plot(monthly_df["Month"], monthly_df["Monthly_Sales"])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_sales_trend.png")
plt.close()

conn.close()

print("✅ Charts created and saved in visuals/ folder")
