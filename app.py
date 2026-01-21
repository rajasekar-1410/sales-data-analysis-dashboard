import streamlit as st
import sqlite3
import pandas as pd

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Sales Data Analysis Dashboard",
    layout="wide"
)

st.title("📊 Sales Data Analysis Dashboard")

# ---------------------------------
# Load data from SQLite
# ---------------------------------
@st.cache_data
def load_data():
    conn = sqlite3.connect("database/sales.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return df

df = load_data()

# ---------------------------------
# KPIs
# ---------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("🧾 Total Orders", total_orders)

st.divider()

# ---------------------------------
# Sidebar Filters
# ---------------------------------
st.sidebar.header("🔍 Filters")

regions = df["Region"].unique()
selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=regions,
    default=regions
)

filtered_df = df[df["Region"].isin(selected_regions)]

# ---------------------------------
# Sales by Region
# ---------------------------------
st.subheader("🌍 Sales by Region")

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

st.bar_chart(region_sales.set_index("Region"))

# ---------------------------------
# Monthly Sales Trend
# ---------------------------------
st.subheader("📈 Monthly Sales Trend")

filtered_df = filtered_df.copy()
filtered_df["Order Month"] = filtered_df["Order Date"].str[:7]

monthly_sales = (
    filtered_df.groupby("Order Month")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Order Month")
)

if not monthly_sales.empty:
    st.line_chart(monthly_sales.set_index("Order Month"))
else:
    st.info("No data available for selected filters.")

