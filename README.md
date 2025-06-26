# HR Analytics Dashboard

## 📊 Overview
This project demonstrates a full-cycle **HR analytics workflow**, starting from raw data with missing and duplicate values to a fully interactive **Tableau dashboard**. The goal was to generate actionable insights for HR managers about workforce distribution, salary patterns, and employee demographics.

## 🛠️ Tools Used
- **Python** (`ydata_profiling`) – for Exploratory Data Analysis (EDA)
- **Power Query (Excel)** – for data cleaning and transformation
- **Draw.io** – for dashboard mockup design
- **Tableau** – for final dashboard visualization (dark theme)

---

## 🚀 Project Workflow

1. Started with raw HR data containing errors, duplicates, and nulls.
2. Performed EDA using `ydata_profiling` to detect outliers, missing values, and patterns.
3. Cleaned and reshaped the dataset using Power Query (Excel).
4. Created new columns such as:
   - `Age` (calculated from birthdate)
   - `Age Group Segments`
5. Handled `Termdate` nulls to distinguish **active employees**.
6. Checked and fixed all column data types (Date, Number, Text).
7. Generated statistical summaries: **Mean, Median, Mode** for salary and age.
8. Designed dashboard layout using **Draw.io** (Mockup planning).
9. Built an interactive **HR Dashboard in Tableau** using dark theme visuals.

---

## 📸 Sample Dashboard Screenshot

![HR Dashboard](ScreenShots/Screenshot%202025-06-26%20183010.png)

---

## 📈 Key Visual Insights

- **Employee Distribution** by Department & Job Title  
- **Salary Comparison** across Education Levels & Gender *(Barbell Chart)*  
- **Age vs Salary Correlation** for each Department *(Scatter Plot with Trend Lines)*  
- **HQ vs Branch Employee Count**  
- **Demographics by City and State**  
- **Current Employees Filtered by Termdate**

---

## 🧠 Author

**Ayman Reda**  
📍 Data Analyst | Passionate about Python, Excel, Power BI, and Tableau  
📫 Contact: aymannredaa22@gmail.com



