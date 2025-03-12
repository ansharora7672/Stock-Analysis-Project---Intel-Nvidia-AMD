# Stock Analysis - Intel, Nvidia, AMD
# Project Overview
This project is a comprehensive stock analysis for Intel, Nvidia, and AMD, covering over 30 years of stock market data (March 1983 - May 2022). It was built on Azure Databricks, with stock data stored in Azure Blob Storage and processed using Apache Spark and Pandas for efficient data handling.

The project integrates exploratory data analysis (EDA), visualizations, and machine learning to identify trends, irregularities, and stock performance insights, enabling investors to make data-driven investment decisions.


# Features
1. Individual Stock Analysis
   Computes key stock metrics like:
     - Average stock price
     - Highest & lowest close prices
     - Trading volume trends
     - Stock volatility (standard deviation)

2️. Comparative Stock Analysis
 - Daily return percentage calculations for Intel, Nvidia, and AMD.
 - Overall stock price change analysis to determine long-term growth trends.
3. Data Visualization
 - Stock price trends over time
 - Daily return percentage comparison
 - Machine Learning predictions vs. actual stock prices
4. Machine Learning for Stock Prediction
 - This project integrates Linear Regression to forecast stock price movements and investment recommendations.
 - Predict Next-Day Closing Price → Using Linear Regression


# Dataset
The dataset contains historical stock prices with the following attributes:

1. Date
2. Open Price
3. High Price
4. Low Price
5. Close Price
6. Trading Volume
7. Daily Return Percentage (calculated feature)

Data Source: Stored in Azure Blob Storage & processed using Spark in Databricks.

# Technologies Used
Platform: Azure Databricks
Storage: Azure Blob Storage
Data Processing: Apache Spark, Pandas
Visualization: Matplotlib
Machine Learning: Scikit-Learn (Linear Regression)
IDE: Databricks Notebook
Statistical Techniques:
 - Summary Statistics (Mean, Standard Deviation)
 - Daily Return Percentage Calculation
 - Predictive Modeling using Linear Regression
