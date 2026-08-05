# Assignment 1 – Python Coding, Part 2

📅 Certificate earned: MAY 2026  
🎓 MIT Open Learning via 3MTT  

---

## Overview
Welcome to Assignment 1!  

In this notebook, you will analyze **journal entry data** using the concepts learned in this module. The assignment demonstrates how Python can combine **data structures, visualization, and machine learning** to generate insights.  

**Lectures covered in this assignment:**
- Lecture 1: Working with Dictionaries in Python  
- Lecture 2: Processing and Analyzing Data in Python  
- Lecture 3: Plotting and Data Visualization  
- Lecture 4: Type Abstraction  
- Lecture 5: Brief Introduction to Machine Learning  

**Logistics:**
- The notebook is complete — all code has been written and run for you.  
- Your task is to interpret the outputs and answer the questions.  
- Dataset used: `journal_data.csv`.  
- If you’re new to Jupyter Notebooks, check out the *Introduction to Jupyter Notebooks* resource.  

---

## Program Features
- Loads and stores entries from a CSV file.  
- Calculates overall average mood.  
- Calculates average mood by specific tags (e.g., `"travel"`, `"work"`).  
- Generates two visualizations: mood over time and average mood by tag.  
- Uses a Random Forest Classifier to predict mood category (low, medium, high) from tags.  
- Reports model accuracy and predicts tomorrow’s mood category based on tags.  

---

## Part 1 – Quiz Questions

**Question 1**  
Which of the following are true about the JournalTracker class?  
- A JournalTracker object is represented by a dictionary ✅  
- Tags for an entry are stored as a list ✅  
- The mood for an entry is stored as an int ✅  
- Adding an entry for an existing date overwrites the previous one ✅  
- `tracker = JournalTracker()` creates a new object with no entries ✅  

---

**Question 2**  
Which shared behavior allows `average_mood` and `average_mood_by_tag` to work even as new entries are added?  
- They recompute results dynamically from `self.entries` ✅  

---

**Question 3**  
Why is sorting by date important before plotting?  
- To ensure the line plot reflects the true temporal order of entries ✅  
- To ensure earlier dates appear on the left side of the x-axis ✅  

---

**Question 4**  
In `plot_avg_mood_by_tag` which of the following are true?  
- It uses a vertical bar chart to display average mood by tag ✅  
- If no tags are present, it prints a message and ends the function ✅  

---

**Question 5**  
In `predict_mood_category` which of the following are true?  
- Each tag is encoded as a binary feature ✅  
- The code trains a RandomForestClassifier with 100 estimators ✅  

---

**Question 6**  
Which conclusion would be unsafe to draw from the `plot_mood_over_time` chart?  
- Mood will increase next week ✅  

---

**Question 7**  
What additional analysis would most strengthen conclusions drawn from this plot?  
- Adding confidence intervals or error bars for each tag ✅  

---

**Question 8**  
Which change would most plausibly improve predictive performance?  
- Including the text content of journal entries as features ✅  

---

## Assignment Summary
In this assignment, we applied Python to **store, analyze, visualize, and model journal data**.  

**Key takeaways:**
- Nested dictionaries can store structured information like entries, moods, and tags.  
- Functions compute averages overall and by tag, returning meaningful values.  
- Visualizations reveal mood trends over time and differences between tags.  
- Certain activities (e.g., exercise, family) are linked to higher moods.  
- A Random Forest classifier predicts mood categories from tags, though accuracy is modest with limited features.  
