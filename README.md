# 🌍 Global Health Indicators – Power BI Dashboard

## 📌 Overview
This project presents an interactive **Power BI dashboard** that analyzes global health outcomes using data from the **World Bank API**.  
The dashboard highlights key health indicators to support **data-driven decision-making** for policymakers, researchers, and analysts.

---

## 🎯 Purpose of the Dashboard
The primary objective of this dashboard is to:

- Analyze how **health expenditure impacts life expectancy**
- Identify **trends in infant and maternal mortality**
- Compare **health indicators across countries and over time**

The dashboard provides a comprehensive, visual understanding of global health patterns.

---

## 🗂️ Data Source & Preparation
- **Data Source:** World Bank Open Data API
- **Data Processing Tool:** Python (executed inside Power BI)

### Data Preparation Steps:
- Fetch multiple health indicators via API
- Filter records from **2016 onwards**
- Handle missing values
- Reshape data into a **single analytical table**

### Final Dataset Includes:
- Country  
- Year  
- Life Expectancy  
- Health Expenditure (% of GDP)  
- Infant Mortality Rate  
- Maternal Mortality Ratio  
- Immunization Rate (Measles)

✔ Ensures **fresh, reliable, and standardized global data**

---

## 📊 KPI Section (Top of Dashboard)
KPIs provide an **instant snapshot** of global health performance.

### Key KPIs:
- **Average Life Expectancy** – Overall population health outcome  
- **Average Health Expenditure (% GDP)** – Investment in healthcare  
- **Average Infant Mortality Rate** – Quality of maternal and child care  

📍 This section answers:  
> *“How is the world performing overall?”*

---

## 📈 Trend Analysis (Line Charts)
Line charts are used to:

- Track changes over time  
- Identify long-term improvements or declines  

### Visuals Included:
- Life Expectancy vs Year  
- Health Expenditure vs Year  

📍 Helps identify:
- Whether higher spending improves health outcomes  
- Years with significant progress or setbacks  

---

## 🌍 Geographic Analysis (Map Visual)
The map visual highlights **regional disparities in health outcomes**.

### Map Features:
- Countries displayed geographically  
- Color/size represents **Life Expectancy**  
- Tooltips show:
  - Health Expenditure  
  - Infant Mortality Rate  

📍 Reveals:
- Inequality between developed and developing regions  
- Regional clusters of strong or weak health performance  

---

## 📉 Correlation Analysis (Scatter Plot)
The scatter plot explores **relationships between key indicators**.

### Interpretation:
- **X-axis:** Health Expenditure (% GDP)  
- **Y-axis:** Life Expectancy  
- **Bubble Size:** Immunization Rate  
- **Each Point:** A Country  

📍 Key Insight:
> Countries investing more in healthcare generally achieve higher life expectancy.

This is one of the **strongest analytical visuals** in the dashboard.

---

## 🎛️ Filters & Interactivity
Interactive slicers allow users to:
- Filter by **Year**
- Filter by **Country**

✔ Makes the dashboard:
- Interactive  
- User-driven  
- Suitable for multiple stakeholders  

---

## 🧠 Insights Section (Business Interpretation)
A dedicated insights section summarizes findings in **plain language** for non-technical users.

### Example Insights:
- Higher immunization rates lead to lower infant mortality  
- Developing nations show faster improvement trends  
- Healthcare investment strongly correlates with longevity  

---

## 🎨 Design & Usability
The dashboard follows best visualization practices:
- Clean and uncluttered layout  
- Consistent color theme  
- Logical visual placement  
- Easy navigation  

✔ Improves:
- Readability  
- Executive usability  
- Presentation quality  

---

## 🚀 Overall Value
This project demonstrates:

- Python + REST API integration  
- Data modeling in Power BI  
- KPI design and DAX usage  
- Strong analytical thinking  
- Effective storytelling with data  

---

## 🏆 Use Case
This dashboard can be used by:
- Government health departments  
- Policy researchers  
- NGOs and public health analysts  
- Data analysts building global insight solutions  

