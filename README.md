# 🏗️ Enterprise Financial Forecasting (Data Engineering Pipeline)

This project simulates a batch ETL pipeline designed to support enterprise-level financial forecasting using structured financial data, Excel modeling, SQL/Python processing, and a Power BI dashboard.

---


## 🧩 Project Overview

**Enterprise Financial Forecasting** models the financial performance of a mid-sized organization by simulating how financial data flows through a structured data pipeline—from raw input to a reporting-ready dashboard.

This solution highlights:
- ETL principles using SQL and Python
- Forecasting logic in Excel
- Data modeling and visualization in Power BI
- Potential for orchestration via Airflow or Power Query

---

## 🔧 Technologies Used

| Tool           | Function                                |
|----------------|-----------------------------------------|
| Excel          | Forecast calculations & base modeling   |
| SQL (planned)  | Raw data preprocessing & joins          |
| Python (scripts)| ETL transformation logic               |
| Power BI       | KPI dashboard for finance & variance    |
| GitHub         | Version control                         |

---

## 📈 Pipeline Workflow

    A[Raw Financial Data (data_raw)] --> B[Python/SQL Scripts];
    B --> C[Excel Model (forecasting_template.xlsx)];
    C --> D[Power BI Dashboard (.pbix)];
    D --> E[Executive Decision Support];

## 📊 Dashboard Metrics
Monthly Revenue Forecast vs. Actual

Expense Trends by Department

Forecast Variance % (Category-level)

Burn Rate and Net Cash Position

Forecast Accuracy Over Time

## 🧠 Data Engineering Skills Demonstrated
Batch data pipeline simulation

Forecast modeling logic layered post-ingestion

Data cleansing using Excel & Python

Dashboard integration with Power BI

Modular repo design for scalability

## 🔜 Roadmap
 Add SQL staging scripts for raw → clean dataflow

 Schedule automated forecast refresh with Python or Power Query

 Connect to S3 or Azure Blob for real-world simulation

 Dockerize for deployment and scalability

## 📄 Case Study Included
📘 Enterprise_Financial_Forecasting_Case_Study.pdf
Includes context, business goals, assumptions, and how this pipeline supports leadership-level decisions.

## 👤 Author
Yengkong Sayaovong;
Entry-Level Data Engineer | Mechanical Design Background;
GitHub: @YSayaovong;
LinkedIn: linkedin.com/in/yengkongsayaovong

🧩 This project bridges finance and data engineering—demonstrating how forecasting systems can be structured as production-grade data pipelines.
