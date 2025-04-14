import pandas as pd
import numpy as np
import psycopg2
from datetime import datetime

# 🛠️ Configure your database credentials here
conn = psycopg2.connect(
    dbname="postgres",         # or enterprise_forecasting if that's your DB
    user="postgres",
    password="Au$tin2018",
    host="localhost",
    port="5432"
)

# 🔢 Generate 2 years of monthly data
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

# 📥 Insert into PostgreSQL
cur = conn.cursor()
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO financial_transactions (department, category, period, revenue, expenses)
        VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cur.close()
conn.close()
print("✅ 2 years of sample data inserted.")
