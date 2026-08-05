# Foundations of Data Analytics and Machine Learning – Recitations

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Recitation 1: Hands-On Bar and Pie Charts  
- [x] Recitation 2: Deeper Dive Into Data Visualization  

---

## Recitation 1: Hands-On Bar and Pie Charts

### Overview

**Instructor:** Professor Yu Ma, Assistant Professor at the University of Wisconsin.  

This recitation introduces foundational techniques for visualizing categorical and time-series data in Python using Matplotlib and Seaborn. Through hands-on coding examples, we move from raw data to clear, interpretable charts.

**Lectures covered:**  
- Lecture 2: Categorical and Time Series Data  
- Lecture 7: Effective Data Visualization  

### Key Concepts

#### Creating and Displaying Data Frames
- Created a BMI data frame with four categories: Underweight, Normal Weight, Overweight, and Obese.  
- Assigned hypothetical sample counts and computed percentages by dividing each count by the total and scaling to 100.  
- Rounded percentages to one decimal place for cleaner display.  

#### Bar Charts
- **Basic bar chart**: Categories on the x-axis, frequency counts on the y-axis. Figure size set with `plt.figure(figsize=(10, 4.5))`.  
- **Horizontal bar chart**: Flipped axes by assigning categories to the y-axis and counts to the x-axis. Changed grid axis from `x` to `y`.  
- **Percentage bar chart**: Used computed percentages instead of raw counts — values sum to 100%.  
- **Temporal grouped bar chart**: Displayed BMI categories across 2015, 2020, and 2025 with different colors per year, revealing trends such as decreasing normal weight and increasing overweight/obese proportions.  
- **Stacked bar chart**: Each bar represents one year, stacked to show proportional breakdown per category. Useful for quickly assessing the majority category within a year but harder to compare intermediary categories across years.  

#### Pie Charts
- Displays proportions summing to 100%.  
- Dominant categories (e.g., Normal Weight at 71%) draw immediate attention.  
- Less effective for sequential comparisons compared to bar charts.  
- Categories are organized by visual prominence rather than by range.  

### Key Takeaways
- Bar charts are effective for comparing categorical frequencies or percentages — vertically, horizontally, grouped, or stacked.  
- Stacked and grouped bar charts enable visualization of changes across time (e.g., 2015 vs 2020 vs 2025).  
- Pie charts provide a quick proportional snapshot but are less effective for temporal or sequential analysis.  
- Chart customization — figure size, labels, gridlines, colors, and layout — enhances clarity and readability.  

---

## Recitation 2: Deeper Dive Into Data Visualization

### Overview

**Instructor:** Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.  

This recitation expands on descriptive statistics by focusing on how to visualize distributions and relationships in data using Matplotlib, Seaborn, and NumPy. We progress from basic histograms to advanced techniques for comparing distributions and interpreting associations.

**Lectures covered:**  
- Lecture 3: Descriptive Statistics  
- Lecture 7: Effective Data Visualization  

### Key Concepts

#### Generating and Visualizing Distributions
- Generated synthetic height data using `numpy.random.normal` with mean = 65 inches, standard deviation = 3, and n = 100 samples.  
- Set a **random seed** for reproducibility.  
- Plotted individual heights as narrow bars with scatter points on top.  
- Sorted heights in descending order using `numpy.sort` with reversed indexing.  
- Calculated **mean** (65.3), **median** (65.55), and **mode** (64.5) using NumPy and SciPy.  
- Visualized the median split: lower half colored light blue, upper half colored light pink using `fill_between`.  

#### Histograms and Bin Size
- Created dot-stacked histograms and traditional histograms using `plt.hist`.  
- Experimented with bin widths of 1, 2, 3, and 4 to show how bin size affects interpretability — too small adds noise, too large oversimplifies.  
- Applied **KDE (Kernel Density Estimate)** using `sns.kdeplot` for a smoothed distribution view.  
- Enhanced KDE plots with colored regions for each quartile (Q1, Q2, Q3) plus minimum and maximum.  

#### Box Plots and Outliers
- Created box plots using `sns.boxplot` — showing median, Q1, Q3, whiskers, and outliers.  
- **Outlier impact**: Adding a single extreme outlier (>100,000) distorted the mean from ~65 to >1,000, while the median remained ~65.6. This demonstrates the mean's sensitivity to outliers versus the median's resilience.  

#### Comparing Distributions
- Generated height data for males (mean = 70 inches) and females (mean = 65 inches) and visualized with **violin plots** using `sns.violinplot`.  
- Violin plots display median, interquartile range, and mirrored density curves — wider at bottom means more values concentrated at lower levels.  
- Explored **skewness** using exponential distributions: right-skewed (long right tail), left-skewed (long left tail), and symmetric (normal).  
- Compared normal distributions with different standard deviations (0.5, 1, 3) using KDE plots to illustrate how spread varies.  

#### Scatter Plots and Correlation
- Generated height-weight scatter plots for 10 students using a linear relationship with added noise.  
- Visualized three association types: **linear**, **quadratic (non-linear)**, and **no association**.  
- Demonstrated **positive**, **negative**, and **zero** correlations with regression lines using `sns.regplot`.  
- Showed how correlation strength varies: tighter points around the trend line = stronger relationship; more spread = weaker.  
- Displayed correlation coefficients on each plot.  

#### Simpson's Paradox
- Generated synthetic basketball data for males (mean height = 175 cm) and females (mean height = 165 cm) with points scored.  
- **Combined data** showed a strong negative correlation between height and points — counterintuitive.  
- **Separated by gender**: both subgroups showed positive correlation — taller players scored more points in both groups.  
- **Lesson**: Always consider group structure before drawing conclusions. Confounding variables can reverse observed trends when data is aggregated.  

### Key Takeaways
- Histograms, KDEs, box plots, and violin plots each reveal different aspects of distributions — shape, spread, and outliers.  
- Bin size in histograms strongly influences interpretability.  
- Skewness describes distribution asymmetry; standard deviation describes spread.  
- Scatter plots with regression lines reveal linear, non-linear, or absent associations between variables.  
- Correlation coefficient magnitude indicates relationship strength; sign indicates direction.  
- Simpson's paradox warns that trends in combined data can reverse when subgroups are analyzed separately.  
- Good visualization choices make patterns and relationships easier to understand and interpret.  

---

## My Reflections

**Recitation 1** gave me hands-on practice building the charts I learned about in lecture. Writing the actual code — defining figure sizes, choosing colors, flipping axes — made the concepts concrete. The comparison between grouped and stacked bar charts was particularly useful: I now understand when each is appropriate and what trade-offs they involve.  

**Recitation 2** was the most technically rich recitation so far. Building histograms with different bin sizes taught me that visualization is not just about displaying data — it is about choosing the right level of detail. The Simpson's paradox demonstration was the highlight: seeing how gender-separated trends reversed the combined trend was a powerful reminder to always look for hidden subgroups before drawing conclusions. The violin plot comparison of male versus female height distributions was a clear, elegant way to compare populations side by side.  

**Key takeaway:** Recitations bridge theory and practice. Writing the code myself — generating distributions, calculating statistics, building plots — deepened my understanding far more than just reading about these techniques. The hands-on experience with Python visualization libraries is directly applicable to my future data analysis projects.  

---
