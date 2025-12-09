# RIWI Sales Analysis - Performance Test

## Project Overview
This project involves an end-to-end data analysis pipeline developed for **RIWI**. The goal was to transform a raw, noisy dataset containing sales records into a robust Business Intelligence solution.

The process includes **ETL** (Extraction, Transformation, Loading) using Python, **Data Modeling** (Star Schema) in PostgreSQL, and **Advanced Reporting** in Power BI.

---

## Prerequisites
Before running the project, ensure you have the following installed on **Windows**:
*   **Python 3.10+**
*   **PostgreSQL 15+**
*   **DBeaver** (Database Manager)
*   **Power BI Desktop**
*   **VS Code** or **Jupyter Notebook**

---

## Installation & Setup Guide (Windows)

Follow these steps strictly to set up the environment.

### 1. Database Setup (PostgreSQL)
First, you need to create the database using **SQL Shell (psql)** or **DBeaver**.

**Step A: Create Database**
Run the following SQL commands in your SQL Shell or DBeaver console:
```sql
CREATE DATABASE ventas OWNER postgres;
GRANT ALL PRIVILEGES ON DATABASE ventas TO postgres;
```
**Step B: Create Schema (Tables)**
1. Open DBeaver and connect to the new ```ventas``` database.
2. Open the file ```PostgreSQL RIWI_VENTAS.sql``` (provided in this repository).
3. Execute the script to create the empty Star Schema tables (```fact_ventas```, ```dim_producto```, ```dim_cliente```, ```dim_ubicacion```, ```dim_canal```).

### 2. Python Environment Setup
Open your terminal (Command Prompt or PowerShell) in the project folder and run:
```
# 1.Create Virtual Environment
python -m venv venv

# 2. Activate Environment (Windows)
venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

```
1. Running the ETL Pipeline
Run all cells (This script performs data cleaning, ML imputation, mathematical validation, and automatically loads the clean data into the PostgreSQL ```ventas``` )
---
## Methodology & Technical Details

1. **Data Cleaning Strategy**

* **Noise Removal**: Regex patterns were used to clean text fields from artifacts like ??? or @.
* **Garbage Collection:** Example Shipping Cost > 50M were removed to preserve statistical integrity.
* **Category Standardization:** Enforced a "Single Source of Truth" dictionary to fix inconsistencies (example; ensuring "Leche" is always classified as "Lácteo")

2. **Advanced Imputation (Machine Learning)**
* **Decision Trees:** A classifier was trained to predict missing ```Ciudad``` and ```Tipo_Cliente``` based on transaction patterns (```Costo_Envio```, ```Venta_Total```).
* **Mathematical Imputation:** Recovered missing Prices and Quantities by reverse-engineering the business formula

3. **Data Integrity & Logic**
* **Mathematical Balancing:**  A "Master Fix" algorithm ensured 100% of the rows respect the accounting equation Total=P×Q−D+E
* **Business Rules:** Discounts > 60% were capped or removed to align with realistic commercial policies.
---
## Power BI Connection
1. Open **Power BI Desktop**
2. Click on **Get Data** → **PostgreSQL**
3. Connection settings:
* **Server:** ```localhost```
* **Database:** ```ventas```
4. Import all tables.
5. Check the **Model View** to ensure relationships are active (1-to-Many) between Dimensions and Fact Table.
---
## Key Insights from Analysis
1. **Wholesale vs. Retail:** The analysis reveals distinct clusters ("Whales" buying 20k+ units vs. Retailers).
2. **Data Recovery:** The Python ETL recovered ~40% of the dataset that would have been discarded due to missing values.
3.**Mathematical Accuracy:** The final dataset achieves 100% mathematical consistency after the balancing process.




