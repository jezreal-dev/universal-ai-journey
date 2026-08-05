# Module 6: Hands-On Deep Learning — Assignment Notes

## 📋 Assignment 1: Deep Neural Networks in Keras

### Overview
In this assignment, we explored how to create, train, and modify deep neural networks using Keras on the **California Housing** tabular regression dataset (20,640 census block groups, 8 numerical features).

* **Dataset Features**: `MedInc`, `HouseAge`, `AveRooms`, `AveBedrms`, `Population`, `AveOccup`, `Latitude`, `Longitude`.
* **Target**: Median house value in census block group (dollars).
* **Standardization**: Applied using training set statistics: $\bar{x} = \frac{x - \mu_{\text{train}}}{\sigma_{\text{train}}}$.

---

### Model Architectures & Results Summary

| Model Architecture | Trainable Params | Test Set MSE | Normalized MSE | $R^2$ Score | Key Finding |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Part 2: Single Hidden Layer** (16 units) | 161 | 39,278,600,192.00 | 1.000 | -1.955 | Underfits due to single shallow representation layer. |
| **Part 3: Two Hidden Layers** (16 & 16 units) | 433 | 4,710,387,712.00 | 0.120 | 0.646 | **Best performance**; additional depth unlocks non-linear interactions. |
| **Part 4: Skip Connection Model** (8+16 input) | 169 | 37,417,168,896.00 | 0.953 | -1.815 | Skip connection bypasses non-linearity, leading to linear domination & underfitting. |
| **Part 5: Optimal Tuned Model** (8 & 4 units) | 113 | 4,756,561,408.00 | 0.121 | 0.642 | Highly efficient; matches 2-layer performance with only 113 params. |

---

### Detailed Architecture Breakdown

#### 1. Single Hidden Layer (`model_part1`)
* Input: 8 features (`shape=(8,)`).
* Hidden Layer: `Dense(16, activation='relu')` $\to (8 \times 16) + 16 = 144$ params.
* Output Layer: `Dense(1)` $\to (16 \times 1) + 1 = 17$ params.
* **Total Parameters**: $161$.

#### 2. Two Hidden Layers (`model_part2`)
* Input: 8 features (`shape=(8,)`).
* Hidden Layer 1: `Dense(16, activation='relu')` $\to (8 \times 16) + 16 = 144$ params.
* Hidden Layer 2: `Dense(16, activation='relu')` $\to (16 \times 16) + 16 = 272$ params.
* Output Layer: `Dense(1)` $\to (16 \times 1) + 1 = 17$ params.
* **Total Parameters**: $433$.

#### 3. Skip Connection Model (`model_part3`)
* Input: 8 features (`shape=(8,)`).
* Hidden Layer: `Dense(16, activation='relu')` $\to (8 \times 16) + 16 = 144$ params.
* Concatenation: `Concatenate()([inputs, hidden])` $\to$ Length $8 + 16 = 24$ (0 params).
* Output Layer: `Dense(1)(concat)` $\to (24 \times 1) + 1 = 25$ params.
* **Total Parameters**: $169$.

#### 4. Optimal Tuned Model (`best_model`)
* Discovered via `keras_tuner.GridSearch`: 2 layers with 8 units (layer 1) and 4 units (layer 2).
* Dense 1: $(8 \times 8) + 8 = 72$ params.
* Dense 2: $(8 \times 4) + 4 = 36$ params.
* Output Dense: $(4 \times 1) + 1 = 5$ params.
* **Total Parameters**: $113$.

---

### 📝 Key Takeaways:
1. **Depth vs. Performance**: Adding a second hidden layer reduced MSE by $\approx 88\%$ and increased $R^2$ from $-1.955$ to $+0.646$.
2. **Skip Connections**: Direct raw-input to output connections in tabular regression without sufficient depth can degrade non-linear feature learning.
3. **Hyperparameter Tuning**: Keras Tuner identified a compact architecture (113 params) that achieved competitive performance ($R^2 = 0.642$) with less than $\frac{1}{3}$ of the model parameters.

---

### 📝 Assignment 1 Summary & Key Takeaways

In this assignment, we built, trained, and evaluated deep neural networks using Keras with the California Housing dataset, applying concepts of standardization, architecture design, and hyperparameter tuning.

#### Key Takeaways:
1. **Data Preparation**: Standardized input features to ensure comparable scales ($\mu=0, \sigma=1$), preventing unstable optimization and unequal parameter updates.
2. **Single Hidden Layer Model**: Defined and trained a simple neural network; evaluated performance with training/validation loss curves and test MSE ($39.28\text{B}$).
3. **Two Hidden Layers Model**: Added a second hidden layer, increasing parameter count ($433$) and expressive power. Achieved improved convergence and significantly lower test error ($4.71\text{B}$, $R^2 = 0.646$).
4. **Skip Connection Model**: Implemented a network feeding inputs directly to both hidden and output layers ($24$-length concatenated vector, $169$ parameters), analyzing skip-connection interactions on tabular regression data.
5. **Overfitting Analysis**: Compared loss curves across training and validation sets to monitor convergence stability and detect potential overfitting plateaus.
6. **Hyperparameter Tuning**: Used Keras Tuner (`GridSearch`) to find an optimal $2$-layer configuration ($8$ and $4$ units, $113$ parameters) that matched top performance while maintaining extreme efficiency.
