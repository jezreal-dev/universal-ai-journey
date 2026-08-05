# Python Coding, Part 2 – Lectures

📅 Certificate earned: MAY 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- ✅ Lecture 1: Working with Dictionaries in Python  
- ✅ Lecture 2: CSV, NumPy, and Pandas  
- ✅ Lecture 3: Visualization  
- ✅ Lecture 4: Type Abstraction  
- ✅ Lecture 5: Machine Learning  

---

## Lecture 1: Working with Dictionaries in Python

### Overview
Introduces **dictionaries**, a flexible key–value structure used in text analysis, expense tracking, and frequency visualization. Unlike lists, which are indexed by position, dictionaries allow direct access to values using descriptive keys.

### Learning Objectives
- Understand and use Python dictionaries.  
- Store and access data using key–value pairs.  
- Apply dictionaries to real‑world problems such as word counts or expense logs.  

### Detailed Concepts
- **Dictionary syntax**: `{key: value}`.  
- **Accessing values**: `dict[key]`.  
- **Updating entries**: `dict[key] = new_value`.  
- **Iteration**: looping through keys, values, or items.  

### Example
```python
expenses = {"food": 120, "transport": 50}
expenses["food"] += 30
for category, amount in expenses.items():
    print(category, ":", amount)
```

---

## Lecture 2: CSV, NumPy, and Pandas

### Overview
Explores how Python handles structured data using CSV files, NumPy arrays, and Pandas DataFrames. Learners practice reading, parsing, and manipulating datasets.

### Learning Objectives
- Understand the CSV format.  
- Read and parse CSV files in Python.  
- Convert CSV data into NumPy arrays and Pandas DataFrames.  
- Perform basic statistics and generate synthetic datasets.  

### Detailed Concepts
- **CSV parsing**: `csv.reader`, `pandas.read_csv()`.  
- **NumPy arrays**: efficient numerical operations on 1D and 2D data.  
- **Pandas DataFrames**: labeled data structures for analysis.  

### Example
```python
import pandas as pd
data = pd.read_csv("data.csv")
print(data.head())
```

---

## Lecture 3: Visualization

### Overview
Focuses on turning raw numbers into insights using plots and charts. Learners practice visualization with matplotlib and NumPy.

### Learning Objectives
- Create line plots, scatter plots, bar charts, and histograms.  
- Use NumPy arrays as the numerical backbone for visualization.  
- Understand how visualization complements statistical analysis.  

### Detailed Concepts
- **Matplotlib basics**: `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.hist()`.  
- **Customization**: labels, titles, colors.  

### Example
```python
import matplotlib.pyplot as plt
values = [5, 10, 15, 20]
plt.bar(range(len(values)), values)
plt.show()
```

---

## Lecture 4: Type Abstraction

### Overview
Introduces type abstraction and object‑oriented programming. Learners explore built‑in types, libraries, and user‑defined classes to design modular programs.

### Learning Objectives
- Understand type abstraction and why it matters.  
- Create user‑defined classes with attributes and methods.  
- Build modular code to simulate real‑world systems.  

### Detailed Concepts
- **Classes**: `class ClassName:`.  
- **Attributes**: variables inside a class.  
- **Methods**: functions inside a class.  

### Example
```python
class Loan:
    def __init__(self, amount, rate):
        self.amount = amount
        self.rate = rate

    def interest(self):
        return self.amount * self.rate
```

---

## Lecture 5: Machine Learning

### Overview
Introduces machine learning concepts with decision trees and random forests. Learners apply Python skills to classification problems using real datasets.

### Learning Objectives
- Understand classification, regression, and clustering.  
- Learn how decision trees and random forests work.  
- Explore entropy, information gain, and ensemble methods.  
- Apply models to real‑world datasets like the Titanic.  

### Detailed Concepts
- **Decision trees**: splitting data based on features.  
- **Random forests**: ensembles of trees to reduce overfitting.  

### Example
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)
print(clf.predict(X[:5]))
```

---

## My Reflections
- Lecture 1 showed how dictionaries are powerful for organizing and analyzing data.  
- Lecture 2 emphasized the importance of structured data and how NumPy/Pandas make analysis efficient.  
- Lecture 3 highlighted visualization as a bridge between raw numbers and insights.  
- Lecture 4 deepened my understanding of abstraction and modular design through classes.  
- Lecture 5 introduced machine learning, showing how Python can be used for predictive modeling.  

**Key takeaway:** Python Part 2 expands programming into **data science and machine learning**, combining data structures, visualization, abstraction, and predictive modeling into a coherent toolkit.