# Dynamic Rolling Forecast & Variance Analysis Engine

## 📊 Executive Summary
Traditional FP&A relies on static annual budgets that become obsolete within months. This project demonstrates a modern approach: using **Python** to generate algorithmic rolling forecasts and **Power BI** to visualize variance velocity.

## 🚀 Business Problem
* **Static Planning:** Annual Operating Plans (AOP) fail to account for mid-year market volatility.
* **Lagging Insights:** Traditional variance analysis explains *what* happened, not *what is about to happen*.
* **Manual Effort:** Analysts spend 80% of time cleaning data and only 20% interpreting it.

## 🛠️ The Solution
I built a prototype to automate the forecasting baseline, allowing Finance to focus on strategic intervention.

### 1. The Engine (Python)
* Leveraged `Pandas` and `Numpy` to simulate a 36-month financial dataset.
* Modeled **Seasonality** (Sine wave logic) and **Market Volatility** (Random noise distribution) to create realistic variance scenarios.
* Calculated automated Variance % to flag risk areas immediately.

### 2. The Dashboard (Power BI)
* **Visual Strategy:** Area Chart implementation to highlight the "Variance Gap" between Budget (Grey) and Actuals (Blue).
* **Time Intelligence:** Utilized DAX (`TOTALYTD`) to calculate year-to-date performance dynamically.
* **Outcome:** Instantly identifies if revenue dips are seasonal (predictable) or operational (requiring action).

## 📂 Files Included
* `forecast_engine.py`: The Python logic used to generate the financial dataset.
* `Revenue_Dashboard.pbix`: The interactive Power BI file containing the executive dashboard.

## 👤 Author
**Sendhil Kumar S.**
*Specializing in FP&A Strategy, Forecasting, and Financial Modeling.*
