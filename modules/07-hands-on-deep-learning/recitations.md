# Module 6: Hands-On Deep Learning — Recitation Notes

## 🧠 Recitation 1: Introduction to Tensors and Keras

### Overview
Welcome to Recitation 1: Tabular Data Prediction & Hyperparameter Optimization, taught by Professor Rama Ramakrishnan, Professor of the Practice in AI/ML at MIT.

In this recitation, we begin with a concise introduction to tensors—the fundamental data structure underpinning deep learning models. We explore tensors as multidimensional arrays, covering their different ranks (from scalars to high-dimensional tensors) and real-world examples, such as images and videos. Building on this foundation, we introduce Keras as the high-level API for defining and training neural networks, and explain its relationship with backends like TensorFlow, PyTorch, and JAX. We then transition into a hands-on walkthrough of training a heart disease prediction model using Keras, discussing the network architecture, choice of activation functions, loss functions, optimizers, and the role of early stopping.

---

### 1️⃣ Tensors & The Deep Learning Software Stack

#### What is a Tensor?
A **tensor** is a generalization of scalars, vectors, and matrices to arbitrary multidimensional arrays.

#### Tensor Rank & Dimensionality
The **rank** of a tensor refers to its number of independent axes or dimensions:
* **Rank 0 (Scalar)**: A single number (e.g. `42`).
* **Rank 1 (Vector)**: A 1D list of numbers (e.g. `[42, 23.4, 11.2]`).
* **Rank 2 (Matrix)**: A 2D table with rows and columns.
* **Rank 3 (3D Tensor)**: A cube of numbers (e.g. a color RGB image with dimensions `[Height, Width, 3 Channels]`).
* **Rank 4 (4D Tensor)**: A sequence/list of 3D tensors (e.g. a single video clip consisting of a sequence of color frames `[Frames, Height, Width, Channels]`).
* **Rank 5 (5D Tensor)**: A list of 4D tensors (e.g. a YouTube video playlist or batch of video clips).

*Pro Tip*: A **Rank $k$ tensor** can be conceptualized as a list of **Rank $(k-1)$ tensors**.

#### Deep Learning Software Hierarchy
Modern AI software is organized into a modular layered architecture:

```
+-----------------------------------------------------------+
|                   High-Level API (Keras)                   |
+-----------------------------------------------------------+
|    Computation & Gradient Backends (TensorFlow / PyTorch) |
+-----------------------------------------------------------+
|   Hardware Acceleration Layer (CPUs / GPUs / TPUs)        |
+-----------------------------------------------------------+
```

1. **Hardware Acceleration Layer**: Hardware accelerators (GPUs, TPUs) execute high-throughput parallel matrix operations.
2. **Backends (TensorFlow, PyTorch, JAX)**:
   * Automatic differentiation (calculates exact gradients automatically using backpropagation).
   * Built-in optimizers (SGD, Adam, AdamW).
   * Distributed computing across multi-core CPUs/GPUs.
3. **High-Level API (Keras)**:
   * Operates as a user-friendly frontend on top of underlying backends (TensorFlow, PyTorch, or JAX).
   * Offers modular abstractions for layers (`Input`, `Dense`), activation functions, model APIs, data preprocessing pipelines, loss functions, and evaluation metrics.

#### Keras Model-Building APIs
Keras provides three main approaches to construct models:
1. **Sequential API**: Simple linear stack of single-input, single-output layers.
2. **Functional API**: Flexible approach allowing arbitrary non-linear topologies, multi-input/output architectures, and shared layers.
3. **Subclassing API**: High-control object-oriented approach for custom low-level forward pass logic.

---

### 📝 Recitation 1 Summary & Key Takeaways

In this recitation, we learned about tensors as the building blocks of deep learning and explored Keras for building neural networks. We discussed how tensors generalize scalars, vectors, and matrices into multidimensional arrays, and saw examples ranging from numbers to images and videos. We also introduced Keras as a high-level interface to frameworks like TensorFlow and PyTorch, providing convenient tools for defining layers, activations, and training workflows.

#### Key Takeaways:
3. **Functional API**: Provides an ideal balance of clarity and structural flexibility when designing multi-layer neural network graphs.

---
---

## 🧠 Recitation 2: Training Neural Networks in Keras

### Overview
Welcome to Recitation 2: Training Neural Networks in Keras, taught by Professor Rama Ramakrishnan, Professor of the Practice in AI/ML at MIT.

In this recitation, we walk through hands-on examples and practice exercises to reinforce the concepts covered in the lectures, focusing on Deep Learning for structured data. The accompanying notebook `mod6_rec2.ipynb` explores binary classification on tabular data (predicting heart disease) with a mix of numerical and categorical features.

### Practical Workflow & Dataset Background
* **Dataset**: Cleveland Clinic Heart Disease dataset containing 303 patient records.
* **Target Variable**: `Target` (1 = Heart disease diagnosed, 0 = No heart disease).
* **Feature Processing**:
  * Numerical features (e.g. `Age`, `Trestbpd`, `Chol`, `Thalach`, `Oldpeak`, `Slope`).
  * Categorical features (e.g. `Sex`, `CP`, `FBS`, `RestECG`, `Exang`, `CA`, `Thal`) require one-hot encoding, expanding 13 original attributes to 29 binary/numerical inputs.

---

### 1️⃣ Setting Up Environment & Managing Randomness
* **Keras Backend Setup**: Configure environment to set TensorFlow as the computational backend before importing Keras:
  ```python
  import os
  os.environ["KERAS_BACKEND"] = "tensorflow"
  import keras
  ```
* **Controlling Randomness for Reproducibility**:
  Randomness enters neural network training via:
  1. Initial weight and bias initialization.
  2. Dataset batch shuffling.
  3. Train/Validation data splitting.
  * *Solution*: Fix the random seed explicitly using `keras.utils.set_random_seed(42)` (a reference to Douglas Adams' *Hitchhiker's Guide to the Galaxy*).

---

### 2️⃣ Data Preprocessing & Feature Engineering
* **Categorical One-Hot Encoding**: Use Pandas `pd.get_dummies(df, columns=categorical_cols)` to split categorical variables (e.g., `CP` chest pain values 0-4 into separate columns `cp_0` to `cp_4`).
* **Feature Standardization**: Neural networks optimize best when numerical inputs occupy narrow, consistent ranges:
  \[x_{\text{scaled}} = \frac{x - \mu}{\sigma}\]
  Calculate $\mu$ (mean) and $\sigma$ (standard deviation) **strictly on the training set** to prevent data leakage, then apply to both train and validation sets.
* **Data Splitting**: Split the 303 samples into an 80/20 train-validation ratio (242 training samples, 61 validation samples).
* **Format Conversion**: Convert Pandas DataFrames into NumPy arrays via `.to_numpy()` for optimal Keras processing.

---

### 3️⃣ Network Construction & Compilation
* **Keras Functional API Construction**:
  ```python
  # Adaptive input shape matching feature dimension (29 features)
  inputs = keras.layers.Input(shape=(train_x.shape[1],), name="input")

  # 1 Hidden Dense layer with 16 ReLU units
  hidden = keras.layers.Dense(16, activation="relu", name="hidden")(inputs)

  # Output Dense layer with 1 Sigmoid unit
  outputs = keras.layers.Dense(1, activation="sigmoid", name="output")(hidden)

  model = keras.Model(inputs=inputs, outputs=outputs, name="heart_disease_model")
  ```
* **Parameter Verification**:
  * Input to Hidden: $(29 \times 16) + 16 = 480$ parameters.
  * Hidden to Output: $(16 \times 1) + 1 = 17$ parameters.
  * Total Parameters: $480 + 17 = 497$ parameters. Verifiable via `model.summary()`.
* **Model Compilation**:
  ```python
  model.compile(
      optimizer="adam",
      loss="binary_crossentropy",
      metrics=["accuracy"]
  )
  ```

---

### 4️⃣ Training, Evaluation & Prediction
* **Execution Parameters**:
  * Batch size: 32 (yielding 8 batches per epoch for 242 training samples).
  * Epochs: 50.
* **Training Call**:
  ```python
  history = model.fit(
      train_x, train_y,
      batch_size=32,
      epochs=50,
      validation_data=(val_x, val_y),
      verbose=1
  )
  ```
* **Analyzing Loss Curves & Overfitting**:
  * Training loss steadily declines across epochs.
  * Validation loss hits its minimum ($\approx 0.3305$) around epoch 42 and validation accuracy plateaus at $\approx 85.25\%$ by epoch 33.
* **Evaluation & Inference**:
  * Evaluate final performance using `model.evaluate(val_x, val_y)`.
  * Generate patient risk probabilities using `model.predict(new_patient_data)`.

---

### 📝 Recitation 2 Summary & Key Takeaways

In this recitation, we moved from theory to practice by training a neural network in Keras to predict heart disease using patient data from the Cleveland Clinic. Learners worked through the complete workflow, from setting up the environment to preparing data, defining a network, training it, and evaluating performance.

#### Key Takeaways:
1. **Setup and Reproducibility**: Control randomness using fixed random seeds (`keras.utils.set_random_seed(42)`).
2. **Data Preparation**: One-hot encode categorical features, standardize numerical features based strictly on training set metrics ($\mu, \sigma$), and split into train/validation sets.
3. **Model Design & Compilation**: Construct the architecture using the Keras Functional API, compile with `binary_crossentropy` loss, `adam` optimizer, and `accuracy` metric.
4. **Training & Evaluation**: Train with minibatches, monitor training vs. validation loss to identify overfitting plateaus, verify accuracy with `model.evaluate`, and perform inference using `model.predict`.
* **Architecture Setup**:
  * Input layer: 29 input nodes.
  * Hidden layer: 1 Dense layer with 16 ReLU neurons.
  * Output layer: 1 Dense layer with Sigmoid activation.
* **Compilation & Training**:
  * Loss function: `binary_crossentropy`
  * Optimizer: `adam`
  * Early Stopping callback configured on validation loss to halt training when performance flattens.
