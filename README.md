# Superstore-Sale-Dashboard
This repository contains an interactive Power BI dashboard built using the Superstore Sales dataset. The project demonstrates how business insights can be derived from sales data through data cleaning, visualization, and analysis. This dashboard provides insights into Superstore sales performance

## Features
- KPI Cards showing:
  * Total Sales
  * Total Profit
  * Total Quantity
- Pie Chart – Distribution of Sales/Profit by Category or Region
- Scatter Plot – Sales vs. Discount analysis to understand impact on profitability
- Filters/Slicers for dynamic exploration of data

## Objective
- To analyze sales performance, profit trends, and customer behavior by visualizing data in an interactive and business-friendly manner.

## Tech Stack
- Power BI (Dashboard creation & data visualization)
- Python (optional) – Dataset cleaning/preprocessing
- Superstore Dataset (static dataset from kaggle)

## Steps Followed

### 🔗 Dataset
- This Superstore sale dataset is downloaded from kaggle.
- You can easily download it from `archieve1.zip`

### 🧹 Data Preprocessing
- Raw dataset was cleaned using Python (pandas, numpy).
- Steps included handling missing values, Removing dupliactes, and removing null categorical columns.
- Script included in `Sample.py` for reference.

### 📊 Data Visualization (Power BI)
- Import cleaned_superstore.csv into Power BI
- Build dashboard with:
- KPI Cards → Total Sales, Total Profit, Total Orders
- Pie Chart → Category-wise Sales Distribution
- Line Chart → Sales Trend over Time

### 📷 Dashboard Screenshot
<img width="1252" height="706" alt="SuperStore sales Dashboard" src="https://github.com/user-attachments/assets/71868dc0-271a-44d7-8089-540ac1ea7ea8" />

### 📈 Key Insights
- Technology category contributes the highest sales.
- Profits vary significantly across states, highlighting focus areas.
- Discounts drive sales but reduce profitability.

## Contributing
- Feel free to fork, improve, add features or difficulty levels, and submit pull requests!

## License
- This project is open source and available under the MIT License.
