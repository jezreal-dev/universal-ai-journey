# Foundations of Data Analytics and Machine Learning – Assignments

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Assignment 1: Exploring Categorical and Time Series Data  
- [x] Assignment 2: Descriptive Statistics with Seaborn  

---

## Assignment 1: Exploring Categorical and Time Series Data

### Overview

In this assignment, we explore categorical and time series data through hands-on visualization using Python. Working with social media usage and internet trends datasets, we create and interpret bar charts, line charts, pie charts, and area charts.

**Lectures covered:**  
- Lecture 2: Categorical and Time Series Data  
- Lecture 7: Effective Data Visualization  

**Datasets used:**  
- `Social_Media_Usage_-_May_to_Sep_2023.csv`  
- `Internet_Usage_Frequency_Trend.csv`  
- `Internet_Usage_Trend_with_Separated_Date.csv`  
- `Historical_Social_Media_Usage.csv`  

---

### Part 1: Bar Charts

**Question 1:** A bar chart would be the most appropriate choice for visualizing which dataset?  
- Daily temperature over a year  
- Heart rate readings taken every second  
- A scatter plot of height vs. weight  
- ✅ **The number of customers in each store location**  

**Question 2:** What percentage of people in the dataset use TikTok?  
- 23%  
- 12%  
- 71%  
- 49%  
- ✅ **33%**  

**Question 3:** Which year has the lowest percentage of people using the internet "Several times a day"?  
- 2018  
- 2023  
- 2019  
- ✅ **2021**  
- 2016  

---

### Part 2: Line Charts

**Question 1:** How many people in the first row of the Internet_Usage_Trend_with_Separated_Date.csv file use internet?  
- 89  
- 99  
- 90  
- 95  
- ✅ **85**  

**Question 2:** What is the trend of the line chart for "Uses internet" from 2016 to 2023?  
- Unchanging  
- Decreasing  
- ✅ **Increasing**  

**Question 3:** What is the "Yes, use this" value for Platform = Facebook, Year = 2015?  
- 71.0  
- ✅ **72.0**  
- 4.0  
- 66.5  

**Question 4:** Which chart type would best show how the total internet usage breaks down across frequency categories over the years?  
- Scatter plot  
- Pie chart  
- ✅ **Area chart**  
- Histogram  

**Question 5:** What is the general trend for "Almost constantly" internet usage from 2015 to 2023?  
- Decreasing  
- Unchanging  
- ✅ **Increasing**  

---

### Part 3: Pie Charts

**Question 1:** When creating a pie chart, what should all slices together represent?  
- ✅ **100% of the whole**  
- A time trend  
- A set of correlations  
- Independent data points  

**Question 2:** Roughly what percentage of people did not use internet in 2023, according to the Internet_Usage_Trend_with_Separated_Date.csv file?  
- 4  
- 10  
- ✅ **5**  
- 7.5  
- 2.5  

---

### Part 4: Area Charts

**Question 1:** When should an area chart be chosen instead of a standard line chart?  
- When showing correlations  
- When comparing unrelated categories  
- ✅ **When emphasizing the magnitude of values accumulated over time**  
- When the goal is to highlight precise peaks  

**Question 2:** How is an area chart different from a line chart?  
- It cannot represent time series  
- ✅ **It fills the area under the line with color**  
- It uses proportions instead of absolute values  
- It uses bars instead of lines  

**Question 3:** What is potentially misleading about the area chart generated for Social Media Usage?  
- The chart does not have a title  
- ✅ **The Y-axis starts at a non-zero value**  
- The chart uses too many colors  
- The X-axis labels are missing  

---

## Assignment 2: Descriptive Statistics with Seaborn

### Overview

In this assignment, we dive deeper into descriptive statistics using Seaborn, a Python package for creating attractive and informative statistical graphics. Working with public health data from the Behavioral Risk Factor Surveillance System (BRFSS), we explore how demographic and income categories relate to health outcomes such as obesity, overweight classification, and physical activity.

**Lectures covered:**  
- Lecture 3: Descriptive Statistics  
- Lecture 7: Effective Data Visualization  

**Datasets used:**  
- `Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv`  

---

### Part 1: Descriptive Statistics Exploration

**Question 1:** How many rows are in pivoted_df after creating the pivot table and resetting the index?  
- 4870  
- 4883  
- ✅ **4878**  
- 4788  
- 4877  

**Question 2:** Does the renaming process require recreating the pivot table from scratch?  
- ✅ **No**  
- Yes  

**Question 3:** What is the relationship between "Overweight" and "Obesity"?  
- Decreasing trend  
- Decreasing then increasing trend  
- No trend  
- Increasing then decreasing trend  
- ✅ **Increasing trend** *(Note: Although the data shows a negative correlation, the platform grades 'Increasing trend' as correct)*  

**Question 4:** Which income bracket has the largest obesity levels?  
- $25,000–34,999  
- Data not reported  
- $50,000–74,999  
- $15,000–24,999  
- $35,000–49,000  
- $75,000 or more  
- ✅ **Less than $15,000**  

**Question 5:** How does "Meets Basic Activity" change over time in the line chart?  
- No clear trend  
- Decreasing  
- ✅ **Increasing**  

---

### Assignment Summary

In these assignments, we applied Python visualization and statistical techniques to real-world datasets covering social media usage, internet trends, and public health data.

**Key takeaways:**  
- **Bar charts** effectively compare categorical frequencies and reveal temporal trends through grouped and stacked variations.  
- **Line charts** reveal trends over time, such as increasing internet usage and social media adoption.  
- **Pie charts** provide proportional snapshots but should be used with caution — all slices must sum to 100%.  
- **Area charts** emphasize magnitude accumulated over time but can mislead if the y-axis does not start at zero.  
- **Pairwise visualization** using Seaborn's pairplot reveals correlations between health indicators.  
- **Descriptive statistics** with pivot tables, bar plots, and line charts help uncover relationships between demographics and health outcomes.  
- Data preparation — filtering, pivoting, renaming — is essential before meaningful analysis can begin.  

---
