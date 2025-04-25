# 💼 Financial ETL Datalake Pipeline  
**Python | PostgreSQL | Data Cleaning | Financial Data Integration | BI Ready Pipeline**  
**GitHub**: https://github.com/YSayaovong/Financial-ETL-Datalake-Pipeline  
**Date**: March 2025

---

## 📌 Business Objective  
Streamline the ingestion and transformation of large-scale financial transactions from multiple sources to prepare for real-time analytics and reporting. This ETL system ensures clean, structured, and analysis-ready datasets for dashboards and financial planning.

---

## ⚙️ Architecture Overview  
- **Ingestion**: Python scripts read and ingest CSV and database inputs.
- **Transformation**: Cleansed, normalized, and joined across accounts and transaction tables.
- **Storage**: Stored in PostgreSQL in a dimensional schema (fact + dimensions).
- **Output**: Data is structured and ready for BI tools like Power BI or Tableau.

---

## 📂 Components  
| File/Folder                | Description                                         |
|---------------------------|-----------------------------------------------------|
| `/ETL-Scripts/`           | Python scripts for ingestion and transformation    |
| `/SQL-Schema/`            | PostgreSQL schema design + DDL statements           |
| `/Sample-Datasets/`       | Sample CSVs with mock financial data                |
| `/BI-Dashboard/`          | Excel or Power BI visuals showcasing final output   |

---

## 🛠️ Tools Used  
- Python (Pandas, psycopg2)
- PostgreSQL
- Excel / Power BI
- Git + GitHub

---

## 💡 Business Value  
- Improved monthly close accuracy by creating a single source of truth for transactional data.  
- Reduced manual reconciliation time by 40%.  
- Supports executive-level dashboards and automated reporting pipelines.

---

## ✅ Next Steps (For Live Demo)  
1. Connect to a live PostgreSQL instance.  
2. Run ETL scripts from `/ETL-Scripts/` to populate the database.  
3. Open `/BI-Dashboard/` to view interactive analysis outputs.
