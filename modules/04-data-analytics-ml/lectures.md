# Foundations of Data Analytics and Machine Learning – Lectures

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Lecture 1: Introduction to Data Analytics and Machine Learning  
- [x] Lecture 2: Categorical and Time Series Data  
- [x] Lecture 3: Descriptive Statistics  
- [x] Lecture 4: Spatial Data and Mapping  
- [x] Lecture 5: Machine Learning Fundamentals  
- [x] Lecture 6: Reproducibility and Data Management  
- [x] Lecture 7: Effective Data Visualization  

---

## Lecture 1: Introduction to Data Analytics and Machine Learning

### Overview

Taught by **Ana Trisovic**, Research Scientist at the FutureTech Lab at MIT. This lecture lays the foundation for the entire module by defining what data is and how it flows through the analytics pipeline. We learn how raw facts — numbers, text, images, audio, or GPS signals — become structured, meaningful insights through careful organization and analysis.

### Learning Objectives
- Distinguish between different types of data and variables.  
- Understand the data analysis pipeline: collection, cleaning, exploration, modeling, and communication.  
- Identify key challenges in data analysis, including bias and interpretability.  

### Key Concepts

- **Data** — Raw, unprocessed facts that we can observe, measure, or record. Includes numbers, text, images, audio, GPS coordinates, and timestamps.  
- **Quantitative data** — Numerical data we can measure or count (height, income, test scores).  
- **Qualitative data** — Descriptive data about categories and labels (eye color, satisfaction level, urban vs rural).  
- **Variables** — The type of information we are interested in (age, favorite color, GPA). Variables form columns in datasets; rows represent observations.  
- **Continuous variables** — Can take any value within a range (height, temperature, time).  
- **Discrete variables** — Countable values (number of pets, books on a shelf).  
- **Ordinal variables** — Categories with a clear order (freshman → sophomore → junior → senior).  
- **Nominal variables** — Labels with no particular order (race, marital status, favorite color).  
- **Binary variables** — Only two possible values (yes/no, 1/0, adult/minor).  
- **Data lifecycle** — Collection → Cleaning/Pre-processing → Integration → Visualization → Analysis → Modeling → Presentation → Sharing/Reuse.  
- **Data analytics** — The process of examining data to uncover trends, answer questions, and support decisions.  
- **Machine learning** — A type of advanced analytics where computers use algorithms to learn from data and make predictions, instead of following manually programmed rules.  

---

## Lecture 2: Categorical and Time Series Data

### Overview

This lecture broadens data exploration skills by focusing on two important data types: categorical and time series. Categorical data classifies observations into groups for frequency comparisons and association detection. Time series data captures observations over time, enabling trend, seasonality, and pattern identification.

### Learning Objectives
- Represent and summarize categorical data using tables and plots.  
- Interpret frequencies, proportions, and contingency tables.  
- Recognize misleading representations in categorical data visualization.  

### Key Concepts

- **Categorical data** — Data consisting of categorical variables — nominal (gender, eye color) or ordinal (rating scales, BMI categories).  
- **Time series data** — A sequence of data points collected at successive intervals over time.  
- **BMI categories** — Underweight, Normal weight, Overweight, Obese — established by the CDC and WHO.  
- **Absolute vs relative frequency** — Raw counts vs percentages. Relative frequencies are essential for comparing groups across time.  
- **Bar charts** — Rectangular bars with length representing magnitude. Effective for numerical comparisons across categories.  
- **Grouped bar charts** — Each category represented by a cluster of bars, showing changes across multiple data series (e.g., years).  
- **Stacked bar charts** — Each bar represents one data series adding up to 100%, emphasizing relative distributions.  
- **Pie charts** — Display proportions of a whole (100%). Useful but can become cluttered with many categories — use with caution.  
- **Line charts** — Connect data points over time, making changes and variations clearly visible.  
- **Dot plots** — Emphasize individual data points. When data is sparse, trends can be harder to identify.  
- **LOWESS** — Locally Weighted Scatterplot Smoothing. A statistical technique that fits polynomial functions to data subsets to create a smooth trend line, adapting locally rather than fitting one overall line.  
- **Time series metrics** — Yearly averages, moving averages, absolute changes, and relative percentage changes.  

---

## Lecture 3: Descriptive Statistics

### Overview

This lecture explores how descriptive statistics form the foundation of data analytics by helping us summarize, visualize, and interpret raw data. Through measures of central tendency and variability, as well as visual tools such as histograms, box plots, and scatter plots, we identify patterns and relationships that guide deeper analysis.

### Learning Objectives
- Use statistical measures (mean, median, mode, variance) to summarize numerical data.  
- Understand distribution shapes and how to identify outliers.  
- Apply percentiles and box plots for effective comparison.  

### Key Concepts

#### Measures of Central Tendency
- **Mean** — The arithmetic average. Appropriate when data is symmetrical but sensitive to outliers.  
- **Median** — The middle value when data is sorted. Resilient to extreme values and outliers.  
- **Mode** — The most frequent value. Typically used for categorical data.  

#### Visualizing Distributions
- **Histogram** — Shows how often values occur in each bin, revealing the shape of a distribution.  
- **Bin size** — Smaller bins show more granularity but can be noisy; larger bins reduce detail but may oversimplify.  
- **Kernel Density Estimation (KDE)** — A smooth alternative to histograms that does not rely on bin sizes.  
- **Violin plot** — A mirrored KDE, useful for comparing two distributions (e.g., male vs female heights).  
- **Skewness** — Measures asymmetry. Positive skew = long tail on the right; negative skew = long tail on the left. In a symmetric distribution, mean ≈ median ≈ mode.  
- **Outliers** — Unusually high or low values. A single outlier can heavily distort the mean but leaves the median relatively unaffected.  

#### Measures of Variability
- **Variance** — Sum of squared deviations from the mean, divided by n−1.  
- **Standard deviation** — Square root of variance. Shows how spread out data points are around the mean.  
- **Empirical rule (68-95-99.7)** — In a normal distribution, approximately 68% of data falls within ±1 SD, 95% within ±2 SD, and 99.7% within ±3 SD.  

#### Quantiles and Box Plots
- **Quantiles and percentiles** — Quantiles divide data into equal-sized intervals. Quartiles split into four parts. Percentiles represent rank position within a dataset.  
- **Box plot** — Summarizes five key statistics: minimum, Q1 (25th percentile), median (50th), Q3 (75th), and maximum. Outliers shown as individual dots.  

#### Bivariate Analysis and Correlation
- **Univariate analysis** — Analyzing a single variable using descriptive statistics and visualizations.  
- **Bivariate analysis** — Exploring two variables and their relationship using scatter plots.  
- **Scatter plot** — Plots two variables against each other. Helps identify linear, non-linear, or absent associations.  
- **Correlation coefficient** — Ranges from −1 to 1. Quantifies both strength and direction of linear association.  
- **Covariance** — Measures how two variables vary together — positive, negative, or near zero.  
- **Correlation does not imply causation** — Two variables moving together does not mean one causes the other.  
- **Simpson's paradox** — A trend that appears in different subgroups disappears or reverses when groups are combined, caused by confounding variables.  
- **Spurious correlation** — Two variables appear related but the connection is driven by an external factor (e.g., ice cream sales and shark attacks — both driven by hot weather).  

---

## Lecture 4: Spatial Data and Mapping

### Overview

This lecture explores spatial data and mapping. Spatial data adds a powerful dimension to analytics by linking information to geographic locations. Maps transform complex data into intuitive visual stories, helping us uncover geographic relationships, clusters, and disparities.

### Learning Objectives
- Choose appropriate maps (dot, choropleth, cartogram) for spatial data.  
- Understand map projections and how they distort data.  
- Apply spatial metrics like density and spatial autocorrelation.  

### Key Concepts

#### Why Maps and Their History
- Use maps when data contains geographical attributes (latitude, longitude, city, state, country). Maps emphasize relationships between data and geography.  
- Oldest maps date back approximately 8,000–9,000 years (Çatalhöyük wall painting, ~6200 BCE; Nebra sky disk, ~1600 BCE; Babylonian road map, ~2,500 years old).  
- **Spatial hierarchy** — Data can be explored at multiple levels: global, national, state, county, neighborhood, or household.  

#### Map Projections
- **Map projections** — Mathematical transformation from a 3D sphere to a 2D surface. Every projection introduces distortions — you cannot preserve area, shape, and distance simultaneously.  
- **Projection types** — Planar, conic, or cylindrical. Classified by distortion properties (area, shape, or distance).  
- **Web Mercator** — Cylindrical projection used by Google Maps. Preserves angles and shapes (useful for navigation) but distorts area near poles. Greenland appears similar in size to Africa, but Africa is over 14 times larger.  

#### Types of Maps
- **Dot distribution map** — Each dot represents a single feature or location (e.g., airports). Can use color to encode density.  
- **Proportional symbol map** — Dot size represents a quantitative variable (e.g., airport size: small, medium, large).  
- **Flow map** — Shows movement of people, goods, or entities between locations. Line thickness represents volume; color can represent direction. Famous example: Minard's chart of Napoleon's 1812 Russian campaign.  
- **Choropleth maps** — Regions colored based on a data variable. The most common way to visualize regional data. Can represent categorical data (languages spoken) or numerical data (airport counts).  
- **Cartograms** — Distort shape and size of regions to reflect a specific variable (e.g., population). Not geographically accurate but emphasize important differences that normal maps obscure.  

#### Spatial Metrics
- **Density** — How much of something exists relative to a unit of area (per square kilometer). Per-capita density reflects the experience of the average person. Normalization radically changes interpretation.  
- **Spatial autocorrelation** — Measures how similar values tend to group together geographically. High values near high values indicate clustering; random or mixed patterns suggest no clear spatial structure.  
- **Proximity and accessibility** — Calculating distances on a map to evaluate how close essential services (schools, hospitals) are within a given area.  

---

## Lecture 5: Machine Learning Fundamentals

### Overview

This lecture introduces the foundations of machine learning, a core component of modern data analytics. We explore what machine learning is, how it differs from traditional programming, and why it matters for solving real-world problems. Through concepts and examples, we lay the groundwork for understanding supervised and unsupervised learning, model training, and performance evaluation.

### Learning Objectives
- Get familiar with the difference between supervised, unsupervised, and reinforcement learning.  
- Get introduced to core tasks: regression, classification, clustering, and dimensionality reduction.  
- Learn how to evaluate model performance using appropriate metrics (e.g., MAE, RMSE, R², silhouette score).  

### Key Concepts

#### What is Machine Learning?
- **Machine learning (ML)** — The science of enabling computers to learn from data and improve over time, without being explicitly programmed. A subset of artificial intelligence.  
- **Deep learning** — A specialized branch of ML using multi-layered neural networks to model complex patterns in large datasets.  
- **Traditional computing vs ML** — In traditional computing, we provide rules and logic. In ML, we provide inputs and outputs, and the model learns the rules by finding patterns.  
- **When to use ML** — When human expertise does not exist (Mars navigation), when humans cannot explain their expertise (speech recognition), when models need huge data (genomics), or when models must be customized (policymaking).  

#### The ML Lifecycle
- **Model** — A simplified mathematical representation trained on data to recognize patterns and make predictions. A function that takes input and produces output.  
- **ML lifecycle** — Model building (create → collect data → train → evaluate) → Inference (deploy to make predictions on new data) → Customization (fine-tune for specific use cases).  
- **Scale evolution** — Early 2000s: models trained on thousands of rows (e.g., 10,000 emails for spam). Today: GPT-3 trained on 500+ billion tokens (45+ TB of text), requiring thousands of GPUs for weeks.  

#### Three Types of Machine Learning
- **Supervised learning** — Machine given labeled examples (input x, desired output y). Goal: learn a function mapping inputs to outputs. Encompasses regression and classification.  
- **Unsupervised learning** — No labels provided. Goal: discover hidden patterns, clusters, or structures. Like handing the computer a puzzle and asking "what do you see?"  
- **Reinforcement learning** — An agent interacts with an environment, receives rewards or penalties, and learns a strategy through trial and error.  

#### Core Tasks
- **Regression** — Predicting continuous outcomes (e.g., study hours → exam score). Fit a line through data to capture the general pattern.  
- **Classification** — Predicting discrete category labels (e.g., cat vs dog based on weight). Uses a decision boundary to separate groups.  
- **Clustering** — Unsupervised technique grouping similar data points (e.g., k-means). Used for customer segmentation, anomaly detection, and data compression.  
- **Dimensionality reduction (PCA)** — Principal Component Analysis reduces input features while preserving structure. Projects high-dimensional data into 2D or 3D space for visualization. Useful for interpreting word embeddings in models like BERT and GPT, exposing semantic patterns and biases.  

#### Evaluation and Overfitting
- **Overfitting** — A complex model memorizes training data noise instead of learning the true pattern. Predictions on new data worsen. A good model generalizes well, not perfectly fits training data.  
- **Evaluation metrics (regression)** — Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE).  
- **Evaluation metrics (classification)** — Confusion matrix, accuracy, precision, recall, F1 score. Classification error rate = 1 − accuracy.  
- **Silhouette score** — Measures cluster quality. Ranges from −1 to 1; higher values indicate more coherent, well-separated clusters.  

#### AlphaGo — A Unifying Example
- **AlphaGo** — Developed by Google DeepMind, first program to defeat a world champion in Go. Used supervised learning (expert games), then reinforcement learning (self-play millions of times). Discovered innovative strategies beyond human knowledge, including the famous Move 37.  

---

## Lecture 6: Reproducibility and Data Management

### Overview

This lecture covers reproducibility and data management — essential pillars of responsible scientific practice. Reproducibility ensures that research findings can be independently verified, while strong data management practices ensure that data remain organized, interpretable, and accessible over time.

### Learning Objectives
- Understand the importance of reproducibility and transparency in data science.  
- Learn the role of version control (e.g., Git) and documentation.  
- Apply tools for ensuring consistent analysis workflows.  

### Key Concepts

#### Reproducibility
- **Reproducibility** — The ability to obtain consistent computational results using the same input data, computational steps, methods, code, and conditions. Fundamentally about transparency.  
- **Why it matters** — Boosts productivity, supports collaboration (including with your future self), facilitates troubleshooting, enhances education, supports building upon previous work.  
- **Reproducibility crisis** — A Nature survey found that more than 70% of researchers failed to reproduce another scientist's experiments; over 50% failed to reproduce their own results.  
- **Best practices for reproducibility:**  
  - Use code-based tools (Python, R) instead of GUI point-and-click interfaces.  
  - Organize workspace with a logical folder structure (separate data, scripts, results).  
  - Use modular design — each file should have a clear purpose and contain reusable, documented code.  
  - Document methodology transparently — transformations, steps, and assumptions.  
  - Provide starter code or Jupyter Notebooks with examples.  
  - Document hyperparameters (learning rate, batch size) and random seeds.  
  - Record software dependencies with specific versions (e.g., PyTorch 2.1, CUDA 11.8).  
  - Specify hardware used (GPU types, CPUs).  
- **Version control (Git)** — Manages code versions, enables reverting to previous states, facilitates sharing via GitHub. Consider open-source licensing.  
- **Cross-referencing** — Link papers to code repositories and vice versa.  
- **Real-world example** — Stable Diffusion: publicly available model with clear environment specs, package dependencies, and hardware requirements. Enabled global remix, fine-tuning, and deployment.  

#### Data Management
- **Data management** — Practices and decisions that make data easier to find, understand, and use. Spans the entire data lifecycle.  
- **Data provenance** — Origin, history, and context of data. Key questions: Who produced it? How was it collected? What does it represent? When and where was it collected? Why was it collected?  
- **Raw vs processed data** — Always preserve raw data without changes. Make copies for processing.  
- **File naming** — Use descriptive, standardized names. Start general (date), end specific (identifiers).  
- **Data dictionary** — A document outlining structure, context, and definitions of variables. Includes variable names, units, types, value ranges, descriptions, and data origins.  
- **Data sharing** — Use proper repositories (Zenodo, Kaggle, Dataverse, Dryad, Figshare). Include licenses. Enable data citation.  
- **Ethical data sharing** — Not all data should be shared. Check for personal, confidential, or sensitive information. Treat all data as your own. Anonymize when needed.  
- **Ethical responsibilities** — Ensure models and visuals do not reinforce stereotypes. Promote transparency. Avoid misleading graphics. Consider real-world impact, especially in healthcare and public policy.  

---

## Lecture 7: Effective Data Visualization

### Overview

Data visualization is the bridge between raw information and human understanding. This lecture explores how effective visualizations transform complex data into clear, actionable insights, from principles of design to selecting the right chart types.

### Learning Objectives
- Create clear and effective plots by applying design principles (e.g., data-ink ratio, visual hierarchy).  
- Choose proper color scales and chart types for different data types.  
- Identify and avoid common visualization mistakes.  

### Key Concepts

#### Design Principles
- **Dual purpose** — Visualization helps with data exploration (discovering patterns) and communication (enabling others to understand findings).  
- **Data-ink ratio (Tufte)** — The proportion of ink (or pixels) used to represent actual data versus total ink in the graphic. Prioritize increasing the data-ink ratio for effective data display.  
- **Visual hierarchy** — Key points of interest should stand out. Use bold colors for important data and softer tones for background elements. Viewers scan top-to-bottom, left-to-right.  

#### Color
- **Color as encoding tool** — Not decoration. Three types of color scales:  
  - **Sequential** — Low to high values (light to dark gradient).  
  - **Diverging** — Diverge from a midpoint (e.g., red for below average, blue for above).  
  - **Qualitative** — For distinct, non-numeric categories.  
- **Color blindness** — Approximately 8% of men and 0.5% of women are red-green colorblind. Avoid red-green pairings; choose accessible palettes.  
- **Color by expectation** — Follow conventional color schemes (e.g., Democrats = blue, Republicans = red). Rainbow color schemes can mislead with sequential data.  

#### Enhancing Readability
- **Highlighting** — Direct attention using different color, border, size, or line thickness (e.g., shaded recession periods).  
- **Annotations** — Explain how to read the plot and what the data means. Highlighting shows where to look; annotations explain why.  
- **Titles** — Should tell a story, not just name a variable. Descriptive titles communicate the main message.  
- **Axis labels** — Should be fully spelled out, unambiguous, and include appropriate units.  

#### Common Mistakes
- Missing or unclear axis labels and titles.  
- Using 3D charts — outdated and distort visual perception.  
- Pie charts with too many slices — more than five is risky.  
- Bar charts that do not start at zero — exaggerate differences.  
- Using raw counts instead of normalizing (per capita or per area).  
- Overdecorating with clip art or shadows.  

#### Best Practices
- **Chart selection** — Bar charts for comparisons; line charts for trends over time; scatter plots for relationships; histograms and box plots for distributions; stacked bar charts for part-to-whole.  
- Focus on accuracy, not just creativity.  
- Keep fonts, colors, and styles consistent.  
- Avoid clutter — clean layouts are easier to read.  
- Tailor charts to the audience's background.  
- Always ask: Is the message clear? What do I want the audience to notice?  
- **Use tables** when exact values are important or the reader needs a reference, not just a trend.  
- **Aesthetics matter** — People judge visualizations by how they are shown. Poor design can undermine trust even with valid data.  
- **Iterate** — Share charts, get feedback, refine.  

---

## My Reflections

**Lecture 1** established the vocabulary for the entire module. Understanding the difference between quantitative and qualitative data, and between continuous, discrete, ordinal, nominal, and binary variables, is the foundation for choosing the right analysis and visualization. The data lifecycle framework gave me a mental model for how to approach any data project from start to finish.  

**Lecture 2** showed how different data types demand different visualizations. Bar charts for categories, line charts for trends, pie charts for proportions — each has its place, but also its limitations. The discussion of LOWESS smoothing was new to me and gave me a powerful technique for extracting trends from noisy temporal data.  

**Lecture 3** was the most statistically dense. Learning about the empirical rule and how standard deviations describe spread gave me a quantitative way to evaluate data consistency. Simpson's paradox was eye-opening — it reinforced that I should always question aggregate trends and look for confounding variables. The reminder that correlation does not imply causation is something I want to apply rigorously, especially when analyzing health data in Nigeria.  

**Lecture 4** connected data to geography in ways I had not considered before. The map projection discussion — showing how Mercator distorts Africa's true size — resonated with me as someone who grew up seeing those distorted maps. Understanding choropleths, density metrics, and spatial autocorrelation equips me to analyze and visualize geographic challenges, from healthcare access to infrastructure gaps across the continent.  

**Lecture 5** clarified the machine learning landscape. The distinction between supervised learning (labeled data), unsupervised learning (hidden patterns), and reinforcement learning (trial and error) gave me a clear framework. The overfitting example — where a more complex model performed worse on new data — was a powerful lesson about generalization over memorization. AlphaGo's Move 37 inspired me: it demonstrated how ML can discover strategies beyond human knowledge.  

**Lecture 6** emphasized that good science is reproducible science. The best practices — version control with Git, documenting hyperparameters, preserving raw data, ethical data sharing — are directly applicable to my own repository and future projects. The Stable Diffusion example showed how strong reproducibility practices can enable global innovation and collaboration.  

**Lecture 7** taught me that design is communication. The data-ink ratio, visual hierarchy, and color accessibility principles are practical rules I can apply immediately to every chart I create. The common mistakes section serves as a useful checklist: always start bar charts at zero, avoid 3D charts, keep pie chart slices under five, and normalize data when comparing across groups.  

**Key takeaway:** Data analytics is not just about crunching numbers — it is about structuring data thoughtfully, analyzing it rigorously, visualizing it clearly, and doing it all responsibly. These seven lectures gave me a coherent toolkit that bridges coding, statistics, visualization, machine learning, and ethics.  

---
