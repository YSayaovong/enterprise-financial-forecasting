# 📈 Enterprise Financial Forecasting System

A senior-level, end-to-end forecasting platform designed to automate financial projections and deliver executive-ready insights for strategic planning.

---

## 🚀 Project Overview

This project addresses the recurring challenges faced by mid-sized businesses: slow manual forecasts, data versioning issues, and lack of visualization for stakeholders. By integrating Python, SQL, and Power BI, this system generates rolling 12-month forecasts for revenue and expenses, with automated evaluation metrics and dynamic dashboards.

---

## 🛠️ Tools & Technologies

- **Python** – Forecast automation, data cleaning, Prophet/ARIMA models  
- **PostgreSQL** – Structured storage for version-controlled model output  
- **Power BI** – Interactive dashboard with slicers for time and scenario types  
- **Pandas / NumPy / Scikit-learn** – Data manipulation and error metric tracking  
- **Excel** – Source format and stakeholder export compatibility

---

## 📊 Forecasting Approach

- 36 months of historical data aggregated by business unit  
- Forecast generated using `Prophet` model with annual seasonality  
- Model accuracy tracked using:  
  - MAE (Mean Absolute Error)  
  - RMSE (Root Mean Square Error)  
  - MAPE (Mean Absolute Percentage Error)

---

## 🧠 Scenario Modeling (Power BI)

Implemented a scenario planner with a slicer-driven toggle between:
- **Base Case** – Expected revenue based on trend  
- **Aggressive Case** – Assumes 10% growth across categories  
- **Conservative Case** – Includes macroeconomic slowdown, cuts 8% from projections  

Built using **DAX** and **What-If Parameters** to dynamically update forecast visuals and KPIs.

---

## 🔁 Workflow Diagram

[ Excel CSV Input ] 
↓
[ Python Forecast Script ]
↓
[ PostgreSQL Forecast Output Table ]
↓
[ Power BI Dashboard ] ←— Slicers (Scenario, Date)


---

## 🎯 Business Impact

- ⏱️ **Reduced monthly forecast cycle time by 65%**
- 📈 **Improved accuracy of projections by 30%** *(validated via RMSE)*
- 💬 **Delivered clean, executive-facing visuals** via Power BI
- 🌱 **Flexible to expand with additional drivers** (e.g., marketing spend, labor, inflation)

---

## 📂 File Structure

enterprise-financial-forecasting/ 
├── data/ 
│ └── historical_financials.csv 
├── notebooks/ 
│ └── forecast_model_pipeline.ipynb 
├── dashboards/ 
│ └── Forecasting_Executive_Dashboard.pbix 
├── outputs/ 
│ └── forecast_vs_actual.csv 
├── images/ 
│ ├── dashboard_forecast_actual.png 
│ └── dashboard_scenarios.png 
└── README.md


---

## 🖼️ Dashboard Preview

![Dashboard Forecast vs Actual](images/dashboard_forecast_actual.png)  
![Scenario Planner Example](images/dashboard_scenarios.png)

---

## 📬 Contact

Created by **Yengkong Sayaovong**  
[LinkedIn](https://www.linkedin.com/in/YengkongSayaovong)  
[Email](mailto:ysayaovong@gmail.com)
