# 📊 COVID-19 Global Data Analysis & Pipeline

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)

An end-to-end data engineering and analytical pipeline written in Python that ingests, cleans, processes, and visualizes global COVID-19 epidemiological data. Prepares clean datasets ready for cloud integration (Azure Blob Storage / BigQuery / Databricks).

---

## 🌟 Key Features

- 🧹 **Automated Data Cleaning**:
  - Parses ISO date strings (`pd.to_datetime`) with error coercion.
  - Imputes missing metric values (`df.fillna(0)`).
  - Validates schema structure and checks missing value statistics (`df.isnull().sum()`).
- 📈 **Time-Series Visualization**:
  - Generates global confirmed case trends over time (`global_cases_trend.png`).
- 📊 **Top-10 Country Ranking**:
  - Aggregates maximum confirmed cases grouped by `Country/Region`.
  - Generates custom bar charts (`top10_countries.png`).
- 💾 **Export Pipeline**:
  - Automatically exports cleaned data as `cleaned_covid19_data.csv` for downstream cloud data warehousing and ML pipelines.

---

## 📂 Project Structure

```
covid-19-dataset/
├── covid_analysis.py       # Main Python ETL and visualization pipeline
├── analysis.py             # Additional exploratory data analysis script
├── cleaned_dataset.csv     # Input raw/staging dataset
├── global_cases_trend.png  # Generated global trend chart
└── README.md               # Project documentation
```

---

## ⚡ Quick Start

### 1. Requirements
Ensure you have Python 3.8+ and required libraries installed:
```bash
pip install pandas matplotlib
```

### 2. Execution
Run the analysis pipeline script:
```bash
python covid_analysis.py
```

### 3. Pipeline Output
Upon successful execution, the pipeline prints statistical summaries to the console, displays interactive plots, exports chart images (`global_cases_trend.png`, `top10_countries.png`), and saves the cleaned dataset as `cleaned_covid19_data.csv`.

---

## 📊 Sample Pipeline Output

```text
--- Data Overview ---
        Date Country/Region  Confirmed  Deaths  Recovered
0 2020-01-22    Afghanistan          0       0          0

--- Basic Stats ---
Dataset cleaned and ready for Cloud / Azure / BigQuery upload.
```

---

## 📜 License

Distributed under the MIT License.
