# Supervised and Unsupervised Learning – Assignment 3

📅 Completed — June 2026  
🎓 MIT Open Learning via 3MTT  

---

## Section Progress
- [x] Part 1: Exploration and Normalization of Airlines frequent flyer dataset  
- [x] Part 2: Hierarchical Clustering and Interpreting  
- [x] Part 3: K-Means Clustering and Decision Trees  

---

## Part 1: Exploration and Normalization

### Overview
In this assignment, we examine the `AirlinesCluster.csv` dataset, which contains metrics on 3,999 members of a frequent flyer program. The objective is to use unsupervised clustering methods (Hierarchical and K-Means) to perform market segmentation so that the airline can target different segments with tailored mileage offers.

---

### Questions and Solutions

#### Question 1: Variable Means Below 20
Using the summary statistics, how many variables have a mean value less than 20?
- ✅ **`2`** (`BonusTrans` and `FlightTrans`)
> **Explanation:** The means for the seven variables are:
> * `Balance`: 73,601.33
> * `QualMiles`: 144.11
> * `BonusMiles`: 17,144.85
> * `BonusTrans`: **11.60** ($<20$)
> * `FlightMiles`: 460.06
> * `FlightTrans`: **1.37** ($<20$)
> * `DaysSinceEnroll`: 4,118.56
> 
> Exactly **2** variables (`BonusTrans` and `FlightTrans`) have mean values less than 20.

#### Question 2: Largest Mean Variables
Which TWO variables have (on average) the largest values?
- ✅ **`Balance`** (mean: 73,601.33)
- ✅ **`BonusMiles`** (mean: 17,144.85)
> **Explanation:** The variable representing the overall miles balance has the largest average value (73,601.33 miles), followed by non-flight bonus miles (17,144.85 miles).

#### Question 3: Effect of Normalization
After normalizing the airline data, what happens to the mean of each variable?
- ✅ **`The mean becomes 0`**
- The mean remains unchanged
- The mean becomes the original median
- The mean becomes 1
> **Explanation:** Standard normalization (z-score scaling) subtracts the mean of each variable from its values and divides by its standard deviation. This mathematical transformation centers the distribution at **0** and sets the standard deviation to **1** for all scaled variables.

#### Question 4: Maximum Value After Normalization
After normalization, which variable has a maximum value greater than 20?
- ✅ **`FlightMiles`** (maximum: `21.680292`)
- `BonusMiles`
- `DaysSinceEnroll`
- `QualMiles`
- `BonusTrans`
- `FlightTrans`
- `Balance`
> **Explanation:** Running max check on the normalized variables gives:
> * `FlightMiles`: **21.680292** ($>20$)
> * `Balance`: 16.186811
> * `QualMiles`: 14.223084
> * `FlightTrans`: 13.610351
> * `BonusMiles`: 10.208293
> * `BonusTrans`: 7.746727
> * `DaysSinceEnroll`: 2.022842

#### Question 5: Minimum Values Below -0.7
How many normalized variables have minimum values below −0.7?
- ✅ **`4`** (`Balance`, `BonusMiles`, `BonusTrans`, `DaysSinceEnroll`)
- `5`
- `3`
- `2`
> **Explanation:** Slicing the minimums of the normalized columns:
> * `DaysSinceEnroll`: **$-1.993361$** ($<-0.7$)
> * `BonusTrans`: **$-1.208052$** ($<-0.7$)
> * `Balance`: **$-0.730348$** ($<-0.7$)
> * `BonusMiles`: **$-0.709903$** ($<-0.7$)
> * `FlightTrans`: $-0.362123$
> * `FlightMiles`: $-0.328562$
> * `QualMiles`: $-0.186275$
> 
> Exactly **4** variables have minimum values below $-0.7$.

#### Question 6: Impact of Omitting Normalization
If we run k-means on the original airline dataset without normalization, which two variables would contribute least to cluster differences?
- ✅ **`BonusTrans`**
- ✅ **`FlightTrans`**
- `Balance`
- `BonusMiles`
- `QualMiles`
- `DaysSinceEnroll`
> **Explanation:** Without normalization, variables with huge scales (like `Balance` and `BonusMiles`, which have standard deviations of 100,775.7 and 24,150.9 respectively) will completely dominate the distance calculations in the k-means algorithm. Variables with tiny ranges and standard deviations like `FlightTrans` (std: 3.79) and `BonusTrans` (std: 9.60) will contribute almost nothing to the calculated distances.

---

## Part 2: Hierarchical Clustering and Interpreting

### Questions and Solutions

#### Question 1: Dendrogram cluster numbers suitability
Looking at the dendrogram, which number of clusters would be least appropriate if the airline wants clearly separated groups?
- ✅ **`8 clusters`**
- `3 clusters`
- `4 clusters`
- `2 clusters`
> **Explanation:** Cutting the dendrogram into 2, 3, or 4 clusters falls in regions with large vertical gaps between merges, indicating well-defined and stable splits. Cut at 8 clusters intersects many short vertical branches that are closely merged together, meaning the resulting groups are not well-separated and lack distinct boundaries.

#### Question 2: Smallest Cluster size
Based on the dendrogram, which cluster number is most likely the smallest group?
- ✅ **`Cluster 1`** (size: `48`)
- `Cluster 2` (size: `53`)
- `Cluster 3` (size: `360`)
- `Cluster 4` (size: `1737`)
- `Cluster 5` (size: `1801`)
> **Explanation:** Cutting the Ward's linkage tree into 5 groups results in the following sizes: Cluster 1: **48**, Cluster 2: **53**, Cluster 3: **360**, Cluster 4: **1737**, Cluster 5: **1801**. Cluster 1 is the smallest.

#### Question 3: Cluster 1 Median Average Variables
Compared to the other clusters, Cluster 1 has the median average values in which variables (if any)? (Select all that apply.)
- ✅ **`Balance`** (Rank 3.0)
- ✅ **`FlightMiles`** (Rank 3.0)
- ✅ **`FlightTrans`** (Rank 3.0)
- ✅ **`DaysSinceEnroll`** (Rank 3.0)
- `QualMiles` (Rank 5.0)
- `BonusMiles` (Rank 2.0)
- `BonusTrans` (Rank 2.0)
> **Explanation:** Ranking the centroids across the 5 clusters (where 1 is lowest and 5 is highest) for Cluster 1 shows: Balance: **3.0** (Median), FlightMiles: **3.0** (Median), FlightTrans: **3.0** (Median), DaysSinceEnroll: **3.0** (Median).

#### Question 4: Cluster 1 Profile Description
Which description best fits Cluster 1?
- ✅ **`Moderate flyers with strong elite qualification`**
- `Heavy non-flight bonus users`
- `Highest flight-frequency customers`
- `Low-tenure casual travelers`
> **Explanation:** Cluster 1 represents customers with a very high average of qualifying miles for top-flight status (`QualMiles` = 5,870.06, Rank 5), but only moderate average flight miles, transaction counts, and program tenure (all Rank 3/median).

#### Question 5: Cluster 2 Smallest Average Variables
Compared to the other clusters, Cluster 2 has the smallest average values in which variables (if any)?
- ✅ **`None`**
- `Balance`
- `BonusMiles`
- `DaysSinceEnroll`
- `FlightMiles`
> **Explanation:** Cluster 5 has the smallest average values (Rank 1) for all variables in the dataset. Therefore, Cluster 2 does not have the smallest average in any category.

#### Question 6: Cluster 2 Profile Description
Which activity pattern most characterizes Cluster 2?
- ✅ **`Intensive flying and transactions`**
- `Bonus-only earning`
- `Short tenure`
- `Low balance accumulation`
> **Explanation:** Cluster 2 contains frequent flyers who fly heavily and generate many transactions. They have the highest average flight miles (`FlightMiles` = 8,752.62, Rank 5), flight transactions (`FlightTrans` = 23.68, Rank 5), and bonus transactions (`BonusTrans` = 33.47, Rank 5).

#### Question 7: Cluster 3 Median Average Variables
Compared to the other clusters, Cluster 3 has the median average values in which variables (if any)?
- ✅ **`QualMiles`** (Rank 3.0)
- `Balance`
- `BonusMiles`
- `DaysSinceEnroll`
- `None`
> **Explanation:** Ranking variables for Cluster 3 shows: `QualMiles`: **3.0** (Median), `Balance`: 5.0, `DaysSinceEnroll`: 5.0, `BonusMiles`: 5.0, `BonusTrans`: 4.0, `FlightMiles`: 4.0, `FlightTrans`: 4.0.

#### Question 8: Cluster 3 Profile Description
Which behavior is most characteristic of Cluster 3?
- ✅ **`Long-term accumulation of miles`**
- `Elite qualification`
- `Bonus transactions`
- `Minimal engagement`
> **Explanation:** Cluster 3 represents customers with the longest tenure in the program (`DaysSinceEnroll` = 4,744.16, Rank 5) and the highest accumulated points balance (`Balance` = 204,316.23, Rank 5), pointing to long-term loyalty and miles accumulation.

#### Question 9: Cluster 4 Second Largest Average Variables
Compared to the other clusters, Cluster 4 has the second largest average values in which variables (if any)?
- ✅ **`DaysSinceEnroll`** (Rank 4.0)
- `Balance`
- `BonusMiles`
- `FlightMiles`
- `None`
> **Explanation:** Ranking centroids shows that Cluster 4 has Rank **4.0** (second largest) in `DaysSinceEnroll` (4,727.47 days), while other variables are Rank 2 or 3.

#### Question 10: Cluster 4 Profile Description
How would you describe the customers in Cluster 4?
- ✅ **`Relatively loyal customers who have not traveled that much.`**
- `Median frequency travels and primarily takes elite status flights.`
- `Loyal customers who have accumulated a lot of points and awards to be redeemed through both flight and non-flight transactions.`
- `Relatively new customers who don't use the airline very often.`
> **Explanation:** Cluster 4 represents long-term members (second highest tenure: 4,727.47 days) but with very low flight frequency and miles (`FlightTrans` = 0.48, `FlightMiles` = 148.67), characterizing them as loyal but inactive flyers.

#### Question 11: Cluster 5 Second Largest Average Variables
Compared to the other clusters, Cluster 5 has the second largest average values in which variables (if any)?
- ✅ **`None`**
- `Balance`
- `BonusMiles`
- `DaysSinceEnroll`
> **Explanation:** Cluster 5 has Rank 1.0 (lowest values) across all variables in the dataset, meaning it has the second-largest average in none of them.

#### Question 12: Cluster 5 Profile Description
How would you describe the customers in Cluster 5?
- ✅ **`Relatively new customers who don't use the airline very often.`**
- `Loyal customers who have accumulated a lot of points and awards to be redeemed through both flight and non-flight transactions.`
- `Customers who have accumulated a large amount of miles, and the ones with the largest number of flight transactions.`
- `Relatively loyal customers who have not traveled that much.`
> **Explanation:** Cluster 5 has the lowest enrollment duration (3,402.97 days, Rank 1) and the lowest points balance and transactions across the board, matching newer customers with minimal participation.

---

## Part 3: K-Means Clustering and Decision Trees

### Questions and Solutions

#### Question 1: Small K-Means Clusters
Based on the reported cluster sizes, how many clusters contain less than 500 observations?
- ✅ **`2`** (Clusters 2 and 3)
> **Explanation:** Fitting k-means with $k=5$ and random state 88 yields the following cluster sizes:
> * Cluster 1: `1656`
> * Cluster 0: `1384`
> * Cluster 4: `764`
> * Cluster 2: `138` ($<500$)
> * Cluster 3: `57` ($<500$)
> 
> Exactly **2** clusters (Cluster 2 and Cluster 3) contain less than 500 observations.

#### Question 2: Cluster Similarity Between Methods
Do you expect Cluster 1 of the K-Means clustering output to necessarily be similar to Cluster 1 of the Hierarchical clustering output?
- ✅ **`No, because cluster ordering is not meaningful in either k-means clustering or hierarchical clustering.`**
- Yes, because the clusters are displayed according to the properties of the centroid, so the cluster order will be similar.
- No, because the clusters produced by the k-means algorithm will never be similar to the clusters produced by the Hierarchical algorithm.
- Yes, because the clusters are displayed in order of size, so the largest cluster will always be first.
> **Explanation:** Cluster labeling is arbitrary. K-means assigning label "1" to a group does not correspond to hierarchical clustering assigning label "1" to its first group. Both methods define labels randomly or by order of execution.

#### Question 3: Interpretable Tree Cluster Target
According to the decision tree, which cluster corresponds to customers with long enrollment duration and low flight activity?
- ✅ **`Cluster c0`**
- `Cluster c4`
- `Cluster c1`
- `Cluster c2`
> **Explanation:** Inspecting the trained decision tree rules:
> * If `DaysSinceEnroll > 4022.00` (Long enrollment duration)
> * And `BonusMiles <= 29283.50`
> * And `FlightTrans <= 10.50` (Low flight activity)
> * The predicted leaf node belongs to **`class: 0`** (which corresponds to Cluster c0).

---

## 🔗 Documented Links and Resources

The following external links and data references were identified and documented in this module's curriculum content:

1. **Airlines frequent flyer program website**:
   - **URL**: [http://www.dataminingbook.com/](http://www.dataminingbook.com/)
   - **Context**: The companion website for the book *"Data Mining for Business Intelligence"* by Galit Shmueli, Nitin R. Patel, and Peter C. Bruce, which is the source of the `AirlinesCluster.csv` dataset.

2. **LendingClub platform**:
   - **URL**: [http://lendingclub.com/](http://lendingclub.com/)
   - **Context**: Peer-to-peer LendingClub platform from which the credit loan payment records dataset (`loans_imputed.csv`) was derived in Assignment 2, Part 1.

3. **Infochimps API/Dataset hosting**:
   - **URL**: [http://infochimps.org/](http://infochimps.org/)
   - **Context**: The repository hosting page historically used for fetching historical monthly stock returns in Assignment 2, Part 2.

4. **Climate Change data sources**:
   - **URL**: [https://crudata.uea.ac.uk/cru/data/temperature/](https://crudata.uea.ac.uk/cru/data/temperature/)
     - *Context*: Climatic Research Unit (CRU) at the University of East Anglia temperature data.
   - **URL**: [https://gml.noaa.gov/ccgg/](https://gml.noaa.gov/ccgg/)
     - *Context*: Global Monitoring Laboratory (GML) carbon dioxide tracking records.
   - **URL**: [http://data.giss.nasa.gov/modelforce/strataer/](http://data.giss.nasa.gov/modelforce/strataer/)
     - *Context*: NASA Goddard Institute for Space Studies stratospheric aerosol optical thickness models.
   - **URL**: [http://solarisheppa.geomar.de/solarisheppa/cmip5](http://solarisheppa.geomar.de/solarisheppa/cmip5)
     - *Context*: GEOMAR Helmholtz Centre for Ocean Research solar irradiance (CMIP5) records.
   - **URL**: [http://en.wikipedia.org/wiki/El_nino](http://en.wikipedia.org/wiki/El_nino)
     - *Context*: Theoretical context on El Niño (ENSO) weather patterns.
   - **URL**: [http://www.esrl.noaa.gov/psd/enso/mei](http://www.esrl.noaa.gov/psd/enso/mei)
     - *Context*: NOAA Earth System Research Laboratory Multivariate ENSO Index.
