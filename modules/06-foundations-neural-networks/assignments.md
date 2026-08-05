# Module 6: Foundations of Neural Networks — Assignment 1 Answers

This document details the analysis and solutions for Module 6 (Foundations of Neural Networks), Assignment 1 (Parts 1 & 2), based on the outputs of the pre-run Jupyter Notebooks:
* **Part 1 Notebook**: `mod5_assign1.ipynb` (Titanic Survival Prediction)
* **Part 2 Notebook**: `mod5_assign2.ipynb` (MNIST Digit Classification)

---

## 🚢 Part 1: Predicting Titanic Survival (`mod5_assign1.ipynb`)

### Question 1: Feature Relevance (Name)
**Mary says "Name should be dropped immediately." Peter says "Name could help, but only after processing." Which statements are correct?**

* **Correct Choices**:
  * **Raw Name is not directly usable as a numeric feature**: The raw string values cannot be fed directly into numerical models or neural network layers.
  * **Titles extracted from Name can be predictive**: Extracted titles (such as "Mr.", "Mrs.", "Miss", "Master", "Dr.") carry significant predictive information about gender, age, and social status, which directly relates to survival probability ("women and children first").
* **Incorrect Choices**:
  * *Name is guaranteed to be the strongest feature*: No feature is ever guaranteed to be the strongest, and features like "Sex" or "Pclass" are typically much stronger.
  * *PassengerId is more meaningful than Name*: PassengerId is merely an arbitrary sequential index, containing no semantic information.

---

### Question 2: Preprocessing Needs
**Which feature(s) might need preprocessing before being used in a machine learning model?**

* **Correct Choices**:
  * **Embarked**: Categorical string inputs containing missing values; requires mode imputation and one-hot encoding.
  * **Sex**: Categorical string input; requires encoding (e.g., binary or one-hot encoding).
* **Incorrect Choices**:
  * *Age*: Already numerical (does not strictly require encoding to be used, although in practice it is imputed and standardized).
  * *PassengerId*: This is just a passenger identifier, which is not useful at all and is dropped.

---

### Question 3: Handling Missing Values
**You can see that there are missing values in features like Age and Embarked. Why don’t we just drop those rows?**

* **Correct Choice**:
  * **Because dropping rows would waste too much data, and filling with the median (for Age) or most frequent value (for Embarked) keeps more information**.
* **Explanation**: Dropping rows with missing values would severely shrink the dataset (e.g., losing ~20% of passengers due to missing Age values). Imputing allows the model to utilize the remaining valid feature values of those passengers.

---

### Question 4: Appropriate Preprocessing Transformations
**Which transformations are appropriate?**

* **Correct Choices**:
  * **One-hot encode Sex**: Appropriately transforms the binary categories ('male', 'female') into numeric form.
  * **Standardize Fare**: Fare has a wide numerical range; scaling ensures it does not dominate other features in the neural network's gradient updates.
  * **Mode-impute Embarked**: Fills missing categories with the most frequent value ('S'), which is mathematically sound for categorical data.
* **Incorrect Choices**:
  * *Median-impute Embarked*: Median is not defined for non-ordinal categorical strings.

---

### Question 5: Model Capacity and Training Set size
**Suppose the perceptron achieves similar accuracy whether trained on 30% or 80% of the training data. What is the most plausible explanation?**

* **Correct Choice**:
  * **The model’s capacity is too limited to benefit from additional data**.
* **Explanation**: The Perceptron is a simple linear model. If the true decision boundary is non-linear, or if the perceptron has already reached its representation limit (underfitting), adding more data cannot improve its performance.

---

### Question 6: Value of Thresholding
**Why is thresholding a useful tool after a classifier has already been trained?**

* **Correct Choices**:
  * **It allows adapting predictions to different real-world costs without retraining the model**: Adjusts predictions dynamically when false positives and false negatives carry different operational penalties.
  * **It lets us reinterpret the same model outputs under different decision priorities**: Enables trading off precision and recall after training is complete.
* **Incorrect Choices**:
  * *It improves model generalization by reducing overfitting*: Post-training thresholding does not change the model weights/generalization capability.
  * *It changes how features contribute to the final prediction*: Feature weights remain completely fixed.

---

### Question 7: Secondary Threshold Criteria
**Two thresholds miss the same number of survivors. What’s a sensible next criterion?**

* **Correct Choice**:
  * **Choose the one with fewer false positives**.
* **Explanation**: "Missing the same number of survivors" means both thresholds yield the same number of False Negatives (FN). To break the tie, we select the threshold that minimizes False Positives (FP) to reduce overall classification errors.

---

### Question 8: Threshold Adjustments & Confusion Matrix
**How does changing the classification threshold generally affect the number of false positives (FP) and false negatives (FN) in a binary classifier?**

* **Correct Choices**:
  * **Lowering the threshold → more FPs, fewer FNs**: A lower threshold makes the model more willing to predict "1" (survived), which flags more actual survivors (fewer FNs) but incorrectly labels more non-survivors as survivors (more FPs).
  * **Raising the threshold → fewer FPs, more FNs**: A higher threshold makes the model more conservative in predicting "1", reducing incorrect positive claims (fewer FPs) but failing to identify some actual survivors (more FNs).

---

### Question 9: Reducing the Generalization Gap
**Which are plausible actions to reduce the train–test gap?**

* **Correct Choices**:
  * **Regularization (e.g., weight decay)**: Penalizes excessively large weights to limit model complexity.
  * **Early stopping**: Halts optimization when validation metrics begin to degrade, preventing overfitting.
  * **Adding more data**: Provides the model with a more resilient representation of the true data distribution.
* **Incorrect Choices**:
  * *Increasing model size*: Larger models typically worsen the generalization gap by increasing overfitting capacity.

---

### Question 10: Model Complexity and Performance
**Why doesn’t a “more complex model” guarantee better test performance?**

* **Correct Choice**:
  * **Because it can memorize noise when data is limited**.
* **Explanation**: Overly complex models can fit small random fluctuations (noise) in the training data, leading to high training accuracy but poor generalization to unseen test data.

---

### Question 11: Deep Model Training Latency
**Mary claims: "Deeper models take longer because they begin with worse starting weights." What is the best correction?**

* **Correct Choice**:
  * **Training takes longer mainly because deeper models have more parameters and more complex optimization, not because their initial weights are worse**.
* **Explanation**: Weight initialization protocols (like Xavier/He) are equally effective for deep models. The longer training time is driven by the computational cost of forward/backward passes over millions of additional parameters and the difficulty of navigating highly non-convex loss landscapes.

---

## 🔢 Part 2: Handwritten Digit Classification (`mod5_assign2.ipynb`)

### Question 1: MNIST Storage Format
**How are MNIST digit images stored in this dataset?**

* **Correct Choices**:
  * **As flattened grayscale vectors of length 784 (28×28)**: The $28 \times 28$ grayscale grids are unrolled into a 1D array of 784 numerical features.
  * **As integers 0–255 representing pixel intensity**: Each pixel is represented by a single integer value from 0 (black background) to 255 (white foreground stroke).
* **Incorrect Choices**:
  * *As 28×28 color (RGB) images with 3 channels each*: MNIST contains only single-channel grayscale data.
  * *As 1D audio-like signals of length 28*: MNIST is 2D image data.

---

### Question 2: The Importance of Feature Scaling
**Two students train identical MLPs on MNIST using the same architecture and optimizer. One scales pixel values to [0,1], while the other leaves them in [0,255]. The scaled model converges faster and reaches higher test accuracy. What is the most reasonable explanation?**

* **Correct Choice**:
  * **Scaling changes the magnitude of gradients, making optimization behave more predictably for a fixed learning rate**.
* **Explanation**: Leaving pixel values at $0-255$ results in large inputs to the neural network layers, producing excessively large gradients during backpropagation. This causes wild weight updates or activation saturation (for a fixed learning rate). Scaling to $[0, 1]$ stabilizes gradient magnitudes and gradient descent steps.

---

### Question 3: Input Layer Neurons
**Mary says: "We have 10 digits, so the input layer should have 10 neurons." Why is that wrong?**

* **Correct Choice**:
  * **Input size must match the number of pixel features, not the number of classes**.
* **Explanation**: The size of the input layer of a neural network must equal the number of features of each sample ($784$ for MNIST). The number of classes ($10$ digits) determines the size of the output layer, not the input layer.

---

### Question 4: Confusion Matrix Interpretation
**A teacher notices the model frequently predicts "9" when the true digit is "4." What would this look like in the confusion matrix?**

* **Correct Choice**:
  * **A bright off-diagonal cell at row 4, column 9**.
* **Explanation**: In standard confusion matrices, rows represent the true labels while columns represent the predicted labels. If true $4$s are misclassified as $9$s, this registers in row 4, column 9 as a high count (a bright cell).

---

### Question 5: OvR (One-vs-Rest) Prediction Flow
**Which statements correctly describe how prediction works in an OvR (One-vs-Rest) setup?**

* **Correct Choices**:
  * **One binary classifier is trained per class to separate that class from all others**: For $N$ classes, $N$ independent models are fit (e.g., class $i$ vs. all non-$i$).
  * **At prediction time, the class whose classifier produces the highest decision score is selected**: The final prediction is determined by taking the argmax of the individual models' output scores.
  * **Different classes can end up with different decision boundaries and margins**: Because each binary classifier is trained independently, their learned decision surfaces and separating margins are completely distinct.
* **Incorrect Choices**:
  * *All OvR classifiers are constrained to produce comparable probability distributions*: OvR classifiers are trained independently with no coupling constraints.

---

### Question 6: OvR Drawbacks
**In which situation might One-vs-Rest (OvR) be a poor choice despite achieving slightly higher accuracy?**

* **Correct Choice**:
  * **When computational resources or training time are limited**.
* **Explanation**: Training $N$ classifiers scales linearly with the number of classes. For datasets with many categories, training $N$ separate neural networks is highly expensive and slow compared to training a single multiclass neural network.

---

### Question 7: PCA Dimensionality Reduction
**After Principal Component Analysis (PCA), a student prints X_pca.shape and sees (60000, 50). What does the 50 indicate?**

* **Correct Choice**:
  * **50 principal component coefficients per image**.
* **Explanation**: Each of the 60,000 images is projected onto the 50 orthogonal principal components (eigenvectors), reducing its feature representation from 784 raw pixels to 50 linear coordinates.

---

### Question 8: PCA Utility
**Why might this new Principal Component Analysis (PCA) representation be helpful for training a neural network?**

* **Correct Choice**:
  * **It focuses on the most important variations across digits and ignores small details or noise**.
* **Explanation**: PCA identifies directions of maximum variance (retaining global patterns like strokes and loops) and discards high-frequency pixel variations, background noise, and uniform border areas.

---

### Question 9: Accuracy vs. Setup Conclusion
**Looking at the test accuracies of the three setups (Single MLP: 0.9646, OvR MLP: 0.9812, PCA+MLP: 0.9634), what is the most reasonable conclusion?**

* **Correct Choice**:
  * **Different setups can change performance, and OvR performed best here, but this does not mean it will always be the best**.
* **Explanation**: While OvR obtained the highest accuracy here, performance is highly empirical and dataset-dependent. OvR carries higher training costs, and other architectures (like CNNs) or representation sizes might yield different trade-offs on other tasks.

---

## 📝 Assignment 1 Summary & Key Takeaways

In this assignment, we reviewed how neural networks can be applied to both structured and unstructured data. Through guided exercises, we explored preprocessing steps for tabular datasets in binary classification tasks, examined the role of simple vs. deeper networks, and analyzed how models handle handwritten digit images.

### Key Takeaways:
1. **Tabular Preprocessing**: Learned how to prepare features, handle missing values, and transform categorical variables appropriately for neural network inputs (e.g., using one-hot encoding for strings, and mode/median imputation).
2. **Linear Perceptrons**: Established linear baselines to diagnose model capacity issues like underfitting, and analyzed model generalization.
3. **Thresholding Trade-offs**: Swept decision thresholds to examine the balance between False Positives (FP) and False Negatives (FN) for different real-world decision costs.
4. **Model Expressiveness**: Explored Multi-Layer Perceptrons (MLPs) to capture non-linear patterns, identifying parameters like capacity and depth that govern generalization.
5. **Image Processing and Scaling**: Applied normalization to pixel values (scaling from $[0, 255]$ to $[0, 1]$) to stabilize backpropagation gradients and accelerate optimization.
6. **OvR (One-vs-Rest) & Dimensionality Reduction**: Compared multiclass single networks with OvR ensembles and PCA feature extraction, balancing accuracy, representation complexity, and training overhead.
7. **Detailed Error Auditing**: Used confusion matrices to evaluate class-specific errors (such as confusing "4"s for "9"s) to gain granular insights beyond aggregate accuracy scores.
