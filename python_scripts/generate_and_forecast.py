import pandas as pd
import numpy as np
import psycopg2
from sklearn.linear_model import LinearRegression
from datetime import datetime
import os

# PostgreSQL config - REPLACE these with your actual credentials
DB_NAME = "enterprise_forecasting"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

# Generate 2 years of sample data
departments = ['Sales', 'Marketing', 'Operations']
periods = pd.date_range(start='2022-01-01', periods=24, freq='MS')

data = []
for dept in departments:
    for period in periods:
        revenue = np.random.normal(loc=200000, scale=30000)
        expenses = np.random.normal(loc=120000, scale=15000)
        data.append((dept, 'Revenue', period, revenue, 0))
        data.append((dept, 'Expenses', period, 0, expenses))

df = pd.DataFrame(data, columns=['department', 'category', 'period', 'revenue', 'expenses'])

# Insert into PostgreSQL
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO financial_transactions (department, category, period, revenue, expenses)
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Sample data inserted into database.")
except Exception as e:
    print("❌ Database connection failed:", e)

# Forecast 6 months using linear regression
df_total = df.groupby('period').agg({'revenue': 'sum', 'expenses': 'sum'}).reset_index()
df_total['month_index'] = range(1, len(df_total) + 1)

X = df_total[['month_index']]
y_rev = df_total['revenue']
y_exp = df_total['expenses']

model_rev = LinearRegression().fit(X, y_rev)
model_exp = LinearRegression().fit(X, y_exp)

future_index = np.arange(len(df_total)+1, len(df_total)+7).reshape(-1, 1)
future_dates = pd.date_range(start=df_total['period'].max() + pd.DateOffset(months=1), periods=6, freq='MS')

forecast_df = pd.DataFrame({
    'period': future_dates,
    'forecast_revenue': model_rev.predict(future_index),
    'forecast_expenses': model_exp.predict(future_index)
})
forecast_df['forecast_net_income'] = forecast_df['forecast_revenue'] - forecast_df['forecast_expenses']

# Save forecast to CSV
output_path = r"C:\Users\ysaya\Desktop\Projects\Flagship Project\Enterprise Forecasting System\data_raw\forecast_results.csv"
forecast_df.to_csv(output_path, index=False)
print(f"✅ Forecast saved to: {output_path}")
