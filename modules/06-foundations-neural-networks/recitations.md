# Foundations of Neural Networks – Recitations

🎓 MIT Open Learning via 3MTT  

---

## Recitation 1: Neural Networks for Tabular Data

**Taught by:** Professor Yu Ma, Assistant Professor at the University of Wisconsin.  
**Notebook Path:** [mod5_rec1.ipynb](file:///C:/Users/USER/Downloads/mod5_rec1.ipynb)

---

### Step-by-Step Hands-On Notebook Walkthrough

#### 1️⃣ Load and Explore the Dataset
The dataset contains weather observations and a label indicating whether tennis was played.
* **Features**:
  * `outlook` (sunny, overcast, rainy)
  * `temp` (hot, mild, cool)
  * `humidity` (high, normal)
  * `windy` (True, False)
* **Target**: `play` (yes, no)

```python
import pandas as pd
import kagglehub

# Download and load the Tennis Weather dataset
path = kagglehub.dataset_download("pranavpandey2511/tennis-weather")
df = pd.read_csv(path + "/tennis.csv")
pd.set_option('future.no_silent_downcasting', True)
df.head()
```

---

#### 2️⃣ Data Preprocessing & Categorical Encoding
Since machine learning models require numerical inputs, categorical columns are encoded to integer values:

| Column | Mapping Values |
| :--- | :--- |
| `outlook` | sunny $\rightarrow$ 0, overcast $\rightarrow$ 1, rainy $\rightarrow$ 2 |
| `temp` | hot $\rightarrow$ 0, mild $\rightarrow$ 1, cool $\rightarrow$ 2 |
| `humidity` | high $\rightarrow$ 0, normal $\rightarrow$ 1 |
| `windy` | False $\rightarrow$ 0, True $\rightarrow$ 1 |
| `play` (Target) | no $\rightarrow$ 0, yes $\rightarrow$ 1 |

```python
# Encoding mappings
outlook_mapping = {"sunny": 0, "overcast": 1, "rainy": 2}
temp_mapping = {"hot": 0, "mild": 1, "cool": 2}
humidity_mapping = {"high": 0, "normal": 1}
windy_mapping = {False: 0, True: 1}
play_mapping = {"no": 0, "yes": 1}

# Apply mappings
df["outlook"] = df["outlook"].replace(outlook_mapping)
df["temp"] = df["temp"].replace(temp_mapping)
df["humidity"] = df["humidity"].replace(humidity_mapping)
df["windy"] = df["windy"].replace(windy_mapping)
df["play"] = df["play"].replace(play_mapping)

# Separate features and target
X = df.drop(columns=['play']).values.tolist()
y = df['play'].tolist()
```

---

#### 3️⃣ Training a Linear Perceptron
We split the data (80% training, 20% testing) and train a standard Perceptron.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# 80/20 train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Perceptron
model = Perceptron(max_iter=1000, tol=1e-3)
model.fit(X_train, y_train)

# Evaluate Accuracy
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

print(f"Train Model Accuracy: {accuracy_score(y_train, y_pred_train):.2f}")
print(f"Test Model Accuracy: {accuracy_score(y_test, y_pred_test):.2f}")
```

---

#### 4️⃣ Calculating Decision Scores (Raw Boundary Value)
The Perceptron makes binary predictions using the sign function:
$$y = sign(w_1 x_1 + w_2 x_2 + w_3 x_3 + w_4 x_4 + b)$$

We can calculate the **raw score** (value before thresholding/activation) either manually or using scikit-learn's built-in `.decision_function()`.

##### Method A: Extracting Coefficients & Intercept
Extracting the parameters learned by the Perceptron on the Tennis dataset:
* **Learned Coefficients (Weights)**: `[2, 0, 7, -5]`
  * Outlook ($w_1 = 2$): Moderate positive influence.
  * Temperature ($w_2 = 0$): No contribution to the decision boundary in this run (not important).
  * Humidity ($w_3 = 7$): Highest positive influence (most important feature).
  * Windy ($w_4 = -5$): Strong negative influence.
* **Intercept (Bias $b$)**: `4`

```python
w1, w2, w3, w4 = model.coef_[0] # w1=2, w2=0, w3=7, w4=-5
b = model.intercept_[0] # b=4
print(f"Decision Boundary Equation: {w1:.2f}*x1 + {w2:.2f}*x2 + {w3:.2f}*x3 + {w4:.2f}*x4 + {b:.2f} = 0")
```

##### Method B: Raw Score of the Second Data Point ($X[1]$)
The second row ($X[1]$) has features that yield a raw decision function score of `-1.0` (predicting `0` or `no` when thresholded):

```python
row = X[1]

# Using scikit-learn's decision_function()
raw_score_sklearn = model.decision_function([row])[0]

# Manually calculating decision function: 2*x1 + 0*x2 + 7*x3 - 5*x4 + 4
raw_score_manual = (w1 * row[0]) + (w2 * row[1]) + (w3 * row[2]) + (w4 * row[3]) + b

print(f"Sklearn Decision Function score: {raw_score_sklearn}") # Output: -1.0
print(f"Manually calculated raw score: {raw_score_manual}") # Output: -1.0
```

---

#### 5️⃣ Hidden Layers & Multi-Layer Perceptrons (MLPs)
To test how network capacity and complexity affect accuracy and generalization, we train MLPs with different hidden layer architectures on the 14-sample weather dataset:

##### Case 1: Simple 2-layer MLP (hidden_layer_sizes=(5, 2))
* **Training Accuracy**: `1.0` (100%) — the model completely memorized the training set.
* **Testing Accuracy**: `0.67` (67%)
* **Gap**: `33%` (The model has clearly begun to overfit because it has higher capacity than the 14-sample dataset requires).

```python
from sklearn.neural_network import MLPClassifier

model_simple = MLPClassifier(hidden_layer_sizes=(5, 2), activation='relu', solver='adam', max_iter=1000, random_state=42)
model_simple.fit(X_train, y_train)

# Accuracy results
# Train: 1.00, Test: 0.67
```

##### Case 2: Deep 3-layer MLP (hidden_layer_sizes=(10, 10, 10))
* **Training Accuracy**: `1.0` (100%) — complete training data memorization.
* **Testing Accuracy**: `0.33` (33%)
* **Gap / Drop**: `67%` (Severe overfitting. The excessive number of weights and layers allowed the network to learn spurious noise patterns, rendering it useless on unseen test data).

```python
model_deep = MLPClassifier(hidden_layer_sizes=(10, 10, 10), activation='relu', solver='adam', max_iter=1000, random_state=42)
model_deep.fit(X_train, y_train)

# Accuracy results
# Train: 1.00, Test: 0.33
```

---

### Core Concept: Overfitting Variables & Solutions

**Overfitting** occurs when a model memorizes details and noise in the training set instead of learning generalizable patterns, leading to high training accuracy but low test accuracy.

#### Key Overfitting Variables
1. **Model Parameters (Capacity)**: Too many parameters ($W$, $b$, layers $L$, neurons $N$) relative to data size make the hypothesis space too flexible, enabling memorization.
2. **Training Data Size ($M$)**: Small datasets make it easy for networks to find and memorize spurious noise correlations. 
   * *Example*: In this lab, $M = 14$ is extremely small, making it very easy for deep MLPs to overfit. Training on **50** weather observations will still likely cause memorization, while training on **10,000** observations allows the model to learn generalized patterns.
3. **Feature Space Complexity ($d$)**: Having too many input features relative to the number of samples increases the risk of high-dimensional overfitting (e.g., 500 features with only 100 samples). 
   * *Solution*: Apply feature selection or dimensionality reduction like **PCA**.
4. **Learning Rate ($\eta$)**: 
   * *Too Small*: The model takes tiny gradient steps and gets stuck in local patterns, memorizing training noise.
   * *Too Large*: The model takes excessively large steps, jumping past optimal boundaries and causing underfitting.
5. **Training Epochs ($E$)**: Training for too many cycles will eventually cause the network to fit training anomalies:
   * **$E = 5$**: Model is still learning.
   * **$E = 50$**: Potential inflection point where overfitting begins.
   * **$E = 500$**: Almost certainly overfitting (unless training on very large datasets like images where high epochs are needed).

#### Standard Solutions to Overfitting
* **Feature Selection**: Drop irrelevant or redundant features.
* **Dimensionality Reduction**: Apply PCA (Principal Component Analysis).
* **Early Stopping**: Stop training when the training loss continues to decrease/plateau but the **validation/test loss begins to increase**.
* **Regularization**: Penalize large weight values to keep the decision boundary simple.
* **General Balance**: Maintain a balance between model complexity, sufficient training data size, and regularization.

---

### Recitation 1 Summary & Key Takeaways

In this recitation, we walked through the step-by-step process of building and evaluating a simple neural network for tabular data. Using the classic “play tennis” dataset, we examined how to prepare categorical features, train a perceptron model, and interpret its outputs. We also examined the phenomenon of overfitting, learning how to detect it and apply strategies to ensure better generalization.

#### Key Takeaways:
1. **Data Preparation Foundations**: Building a neural network begins with preprocessing: encoding categorical features into numerical form, handling missing values, and scaling inputs.
2. **The Perceptron as a Building Block**: It serves as a foundational model by applying weights and a bias to input features, then passing the linear combination through an activation/threshold function to generate predictions.
3. **Generalization Evaluation**: Model evaluation requires comparing performance on training and testing sets. A small performance gap indicates good generalization, while a large gap signals overfitting.
4. **Overfitting Causes**: Overfitting occurs when a model memorizes the training data instead of learning generalizable patterns. It can be caused by excessive model parameters, small datasets ($M$), high feature dimensionality ($d$), inappropriate learning rates ($\eta$), or excessive training epochs ($E$).
5. **Mitigation Techniques**: Overfitting is mitigated by using feature selection, dimensionality reduction (PCA), tuning learning rates, limiting training epochs, and early stopping.

---
---

## Recitation 2: Unstructured Data & Representation Learning

**Taught by:** Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.  
**Notebook Path:** [mod5_rec2.ipynb](file:///C:/Users/USER/Downloads/mod5_rec2.ipynb)

---

### Step-by-Step Hands-On Notebook Walkthrough

#### 1️⃣ Load and Explore the Fashion MNIST Dataset
Fashion MNIST consists of grayscale, $28 \times 28$ low-resolution images of 10 clothing categories:
* **Training Set**: 60,000 samples
* **Test Set**: 10,000 samples
* **Categories**:
  * 0: T-shirt/top
  * 1: Trouser
  * 2: Pullover
  * 3: Dress
  * 4: Coat
  * 5: Sandal
  * 6: Shirt
  * 7: Sneaker
  * 8: Bag
  * 9: Ankle boot

```python
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist

# Load dataset
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
print("Training set shape:", X_train.shape) # Output: (60000, 28, 28)
print("Test set shape:", X_test.shape)     # Output: (10000, 28, 28)
```

##### Scaling and Flattening
We scale pixel intensities to $[0,1]$ for numerical stability, and flatten the 2D images ($28 \times 28$) into 1D vectors ($784$ values) since standard Feedforward MLPs require vector inputs:

```python
# Scale pixel intensities to [0, 1]
X_train_scaled = X_train / 255.0
X_test_scaled = X_test / 255.0

# Flatten images for MLP
X_train_flat = X_train_scaled.reshape(-1, 784)
X_test_flat  = X_test_scaled.reshape(-1, 784)
```

---

#### 2️⃣ Baseline Classifier: MLP on Raw Pixels
We train a standard Multi-Layer Perceptron (MLP) on the raw 784-dimensional flat vectors to see how well it classifies the images.

* **Architecture**: Input (784) $\rightarrow$ Dense (128 units, ReLU) $\rightarrow$ Dense (10 units, Softmax, for probability distribution).
* **Compilation**: `sparse_categorical_crossentropy` loss, Adam optimizer ($\eta = 0.001$), accuracy metric.
* **Training Details**: Trained for 8 epochs, batch size 128, 10% validation split.
* **Epoch-to-Epoch Behavior**: 
  * Training loss decreases and accuracy increases.
  * Validation accuracy increases and validation loss drops initially but stabilizes in the last 2-3 epochs. 
  * *Takeaway*: Once validation loss plateaus/stabilizes, further training is counterproductive as it can lead to overfitting without improving generalization.
* **Evaluation**: Test set accuracy of **87.14%** (`0.8714`). This shows that the dataset is relatively easy, even for standard feedforward neural networks designed for tabular data.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

# Define baseline MLP
model_raw = Sequential([
    Input(shape=(784,)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model_raw.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=Adam(0.001),
    metrics=['accuracy']
)

# Train the model
history_raw = model_raw.fit(
    X_train_flat, y_train,
    epochs=8,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)

# Evaluate
test_loss, acc_raw = model_raw.evaluate(X_test_flat, y_test, verbose=0)
print("Test Accuracy (Raw Pixels):", acc_raw) # Output: 0.8714
```

---

#### 3️⃣ Exploiting Spatial Structure: Convolutional Neural Networks (CNNs)
To demonstrate the performance of an architecture tailored for image data, we train a simple CNN.

* **High-Level Concept**: CNNs process local regions of the image to extract edges, textures, and shapes. They exploit the image's 2D spatial layout directly rather than flattening it.
* **Hierarchical Learning**: Multiple stacked layers allow the model to learn hierarchies of features (edges $\rightarrow$ textures $\rightarrow$ shapes $\rightarrow$ full objects).
* **Architecture**: Input (28, 28, 1) $\rightarrow$ Conv2D (32, 3x3, ReLU) $\rightarrow$ MaxPool2D (2x2) $\rightarrow$ Conv2D (64, 3x3, ReLU) $\rightarrow$ MaxPool2D (2x2) $\rightarrow$ Flatten $\rightarrow$ Dense (64, ReLU) $\rightarrow$ Dense (10, Softmax).
* **Evaluation**: Test set accuracy of **90.14%** (`0.9014`). This is a 3% improvement over the raw-pixel MLP, showing that exploiting spatial configurations leads to superior image classification.

```python
from tensorflow.keras import layers, models

# Reshape data for CNN (N, Height, Width, Channels)
X_train_cnn = X_train_scaled.reshape(-1, 28, 28, 1)
X_test_cnn  = X_test_scaled.reshape(-1, 28, 28, 1)

# Define simple CNN
cnn = models.Sequential([
    layers.Conv2D(32, kernel_size=3, activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(pool_size=2),
    layers.Conv2D(64, kernel_size=3, activation='relu'),
    layers.MaxPooling2D(pool_size=2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the CNN
history_cnn = cnn.fit(
    X_train_cnn, y_train,
    epochs=8,
    batch_size=128,
    validation_split=0.1,
    verbose=1
)

# Evaluate
cnn_test_acc = cnn.evaluate(X_test_cnn, y_test, verbose=0)[1]
print("CNN Test Accuracy:", cnn_test_acc) # Output: 0.9014
```

---

#### 4️⃣ Representation Learning Part I: Principal Component Analysis (PCA)
PCA is a linear dimensionality reduction technique that finds the directions of greatest variance in raw images.

* **How PCA Works Intuitively**:
  * It scans thousands of training images to identify recurring, large-scale structures (edges, curves, templates). These templates are called **Principal Components**.
  * Instead of storing all $784$ pixels, each image is projected into a lower-dimensional space representing the weights/coefficients of these templates.
  * The compressed vector tells us how to mix the principal components linearly to reconstruct the image.
* **Selecting Components**:
  * We can specify a fixed number of components (e.g. `n_components=50`).
  * Alternatively, we can specify the fraction of variance to preserve (e.g. `PCA(0.95)` to preserve 95% variance).
  * For Fashion MNIST, preserving 95% variance results in **187 components** (dimensions reduced from 784 to 187).
* **Linear Limitation**: Because PCA operates by taking linear combinations of pixels, it cannot capture complex, curved, or nonlinear structures as effectively as neural-network-based autoencoders.

```python
from sklearn.decomposition import PCA

# Initialize PCA to keep 95% of cumulative variance
pca = PCA(n_components=0.95)

# Fit and transform the flattened training set
X_train_pca = pca.fit_transform(X_train_flat)

# Transform the test set
X_test_pca = pca.transform(X_test_flat)

# Check new shape
print("PCA shape:", X_train_pca.shape) # Output: (60000, 187)
```

##### Visualizing Principal Components
We can access the learned templates via `pca.components_`. Visualizing the first few components shows the global shape layouts (e.g., trousers, shirts, sandals) that PCA uses as basic building blocks:

```python
plt.figure(figsize=(10, 4))
for i in range(6):
    plt.subplot(2, 3, i+1)
    # Reshape component template back to 28x28
    plt.imshow(pca.components_[i].reshape(28, 28), cmap="gray")
    plt.title(f"PC {i+1}")
    plt.axis("off")
plt.show()
```

---

#### 5️⃣ Representation Learning Part II: Autoencoders
Autoencoders are deep learning architectures designed for unsupervised representation learning.

* **Conceptual Workflow**:
  * **Encoder**: Takes a high-dimensional input $X$ (784-dimensional flat vector) and projects it into a lower-dimensional bottleneck representation $Z$ (latent dimension = 187).
  * **Decoder**: Takes the latent bottleneck vector $Z$ and attempts to reconstruct the original input as closely as possible ($\hat{X}$).
* **Comparison with PCA**:
  * PCA finds linear patterns to maximize variance.
  * Autoencoders learn **nonlinear**, data-specific features by passing vectors through nonlinear layers (e.g. ReLU activations).
  * PCA directly minimizes MSE via linear projections, whereas Autoencoders create representations structured to maximize reconstruction fidelity.
* **Architecture Details**:
  * Latent Dimension is set to **187** for a direct 1-to-1 comparison with the 95% variance PCA projection.
  * Encoder: `Input(784)` $\rightarrow$ `Dense(256, ReLU)` $\rightarrow$ `Dense(187)`
  * Decoder: `Input(187)` $\rightarrow$ `Dense(256, ReLU)` $\rightarrow$ `Dense(784, Sigmoid)` (outputs are bounded to $[0,1]$ to match scaled pixels).
  * Training Loss: Mean Squared Error (`mse`).
  * Setup: Fit with $X$ as both input and target (`X_train_flat, X_train_flat`).

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

# Latent bottleneck dimension (matching PCA)
latent_dim = 187

# Define Encoder
encoder = Sequential([
    Input(shape=(784,)),
    Dense(256, activation='relu'),
    Dense(latent_dim)
])

# Define Decoder
decoder = Sequential([
    Input(shape=(latent_dim,)),
    Dense(256, activation='relu'),
    Dense(784, activation='sigmoid') # output scaled pixels [0, 1]
])

# Stack Encoder and Decoder
autoencoder = Sequential([encoder, decoder])
autoencoder.compile(optimizer=Adam(0.001), loss='mse')

# Train Autoencoder (unsupervised: target is input itself)
autoencoder.fit(
    X_train_flat, X_train_flat,
    epochs=8,
    batch_size=256,
    validation_split=0.1,
    verbose=1
)
```

##### Visualizing Reconstructions
Evaluating the autoencoder on the test set shows that the reconstructed clothing shapes remain highly recognizable but are slightly blurrier. This blurriness represents the information discarded during bottleneck compression:

```python
# Predict reconstructions on the first 5 test samples
recons = autoencoder.predict(X_test_flat[:5])

plt.figure(figsize=(10,3))
for i in range(5):
    # Original image
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test_flat[i].reshape(28, 28), cmap="gray")
    plt.title("Original")
    plt.axis("off")

    # Reconstructed image
    plt.subplot(2, 5, 6+i)
    plt.imshow(recons[i].reshape(28, 28), cmap="gray")
    plt.title("Reconstruction")
    plt.axis("off")
plt.show()
```

---

#### 6️⃣ Quantitative Evaluation of Representations
We evaluate the quality of the learned representations using three methodologies.

##### Method A: Reconstruction Loss (Mean Squared Error)
We reconstruct the entire test set using both techniques and calculate the MSE between original and reconstructed pixels:
* **PCA Reconstruction Error**: `0.0044`
* **Autoencoder Reconstruction Error**: `0.0083`
* *Why is PCA error lower?* PCA directly minimizes the least-squares reconstruction error via linear projection. Autoencoders minimize MSE indirectly via nonlinear layers, which can lead to slightly blurrier reconstructions but potentially richer semantic latent representations.

```python
# PCA: project -> reconstruct
recons_pca = pca.inverse_transform(X_test_pca)

# AE: project -> reconstruct
recons_ae = autoencoder.predict(X_test_flat)

# Compute MSE
pca_recon_error = np.mean((X_test_flat - recons_pca)**2)
ae_recon_error  = np.mean((X_test_flat - recons_ae)**2)

print("PCA Reconstruction Error:", pca_recon_error) # Output: 0.0044
print("AE Reconstruction Error: ", ae_recon_error)  # Output: 0.0083
```

##### Method B: Classifier Performance on Reconstructed Images
We pass the reconstructed images back into our pre-trained MLP and CNN models (which were trained on raw, undistorted pixels) to measure how well the classifiers can discriminate them:

| Model on Reconstructed Images | Accuracy |
| :--- | :--- |
| **MLP on PCA Reconstructions** | `0.8681` (86.81%) |
| **CNN on PCA Reconstructions** | `0.8860` (88.60%) |
| **MLP on AE Reconstructions** | `0.8541` (85.41%) |
| **CNN on AE Reconstructions** | `0.8173` (81.73%) |

* *Takeaway*: Since PCA reconstructions contain less pixel-level distortion (lower MSE), they are more easily classified by models that were trained on the raw, clean pixel distributions.

```python
def evaluate_mlp_on_recons(recons_flat, y_true):
    preds = model_raw.predict(recons_flat)
    labels = preds.argmax(axis=1)
    return np.mean(labels == y_true)

def evaluate_cnn_on_recons(recons_imgs, y_true):
    preds = cnn.predict(recons_imgs)
    labels = preds.argmax(axis=1)
    return np.mean(labels == y_true)

mlp_pca_recon_acc = evaluate_mlp_on_recons(recons_pca, y_test)
cnn_pca_recon_acc = evaluate_cnn_on_recons(recons_pca.reshape(-1, 28, 28, 1), y_test)
mlp_ae_recon_acc = evaluate_mlp_on_recons(recons_ae, y_test)
cnn_ae_recon_acc = evaluate_cnn_on_recons(recons_ae.reshape(-1, 28, 28, 1), y_test)
```

##### Method C: Classifier Training Directly on Latent Vectors
We train a new MLP classifier from scratch directly using the 187-dimensional compressed latent vectors:
* **Raw Pixel baseline (784 features)**: `0.8714` (87.14%)
* **PCA features (187 features)**: `0.8759` (87.59%)
* **Autoencoder features (187 features)**: `0.8673` (86.73%)
* *Takeaway*: The 187-dimensional PCA representation matches or slightly exceeds the performance of raw pixels. By compressing the representation space, we achieve equivalent performance with smaller architectures, fewer parameters, and faster training.
* *Note on Autoencoder*: The slightly lower performance of the autoencoder in this specific setup is due to Fashion MNIST being a relatively simple dataset. Linear projections (PCA) are highly effective here. For complex, high-resolution datasets, the nonlinear capacity of autoencoders is essential.

```python
# 1) Train MLP on PCA Features
model_pca = Sequential([
    Input(shape=(187,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])
model_pca.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(0.001), metrics=['accuracy'])
model_pca.fit(X_train_pca, y_train, epochs=8, batch_size=128, validation_split=0.1, verbose=1)
_, acc_pca = model_pca.evaluate(X_test_pca, y_test, verbose=0)

# 2) Train MLP on Autoencoder Latent Features
X_train_latent = encoder.predict(X_train_flat)
X_test_latent  = encoder.predict(X_test_flat)

model_latent = Sequential([
    Input(shape=(187,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])
model_latent.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(0.001), metrics=['accuracy'])
model_latent.fit(X_train_latent, y_train, epochs=8, batch_size=128, validation_split=0.1, verbose=1)
_, acc_latent = model_latent.evaluate(X_test_latent, y_test, verbose=0)
```

---

#### 7️⃣ Qualitative & Semantic Exploration of Representations
We explore the semantic structure of the latent spaces qualitatively using nearest-neighbor searches and average class centroids.

##### Nearest Neighbors Analysis
In raw pixel space, distance is measured by simple differences in pixel intensities. This fails to reflect semantic relationships since shifts, brightness, and background alignments distort distances. PCA and Autoencoders map images into latent spaces where distance is based on structural patterns rather than raw pixels.

We analyze the 10 nearest neighbors of test sample `idx=14` (a **Coat**, Class 4):
* **Result**: In all three spaces (Raw Pixels, PCA, and Autoencoder), only 3 out of 10 nearest neighbors belong to the correct class (Coat), with the remaining neighbors being Shirts and other similar garments. In this simple dataset, the representations show comparable boundary performance on this ambiguous sample.

```python
def plot_neighbors(idx, X_flat, labels, X_embed, title, k=10):
    # Calculate Euclidean distance in embedding space
    dists = np.linalg.norm(X_embed - X_embed[idx], axis=1)
    nn_indices = np.argsort(dists)[1:k+1] # skip itself
    
    # Plotting code (Anchor vs Neighbors)
    # ...
```

##### Class Centroids Analysis
A class centroid is the average representation vector of all test examples belonging to a specific class. We compute centroids in all three spaces:
1. **Raw Pixel Centroids**: Directly average the 784-dimensional flat pixel vectors. Produces a very blurry prototype image.
2. **PCA Latent Centroids**: Average the 187-dimensional PCA features, then decode using `pca.inverse_transform()`. Produces a blurry, linearly averaged template.
3. **Autoencoder Latent Centroids**: Average the 187-dimensional bottleneck features, then decode using the trained `decoder` network.
* **Result**: Reconstructed Autoencoder centroids are significantly sharper, less blurry, and show much clearer features (e.g. the average sandal or boot is highly recognizable to the human eye). This is because the decoder mapping is nonlinear and constrained to map back to the manifold of realistic images.

```python
centroid_pixel = []
centroid_pca = []
centroid_ae = []

for c in range(10):
    idx = np.where(y_test == c)[0]
    centroid_pixel.append(X_test_flat[idx].mean(axis=0))
    centroid_pca.append(X_test_pca[idx].mean(axis=0))
    centroid_ae.append(latent_test[idx].mean(axis=0))

# Decode PCA and AE centroids back to pixel space
recon_pca_centroid = pca.inverse_transform(np.array(centroid_pca))
recon_ae_centroid = decoder.predict(np.array(centroid_ae))
```

##### Classifier Confidence on Centroids
We pass these class prototypes into our pre-trained MLP classifier to test how confidently it predicts the correct category. High confidence is reflected in a high average probability on the correct class (the diagonal values of the prediction table):
* **Pixel Centroid Average Diagonal Probability**: `0.8795` (87.95%)
* **PCA Centroid Average Diagonal Probability**: `0.8767` (87.67%)
* **Autoencoder Centroid Average Diagonal Probability**: `0.8895` (88.95%)
* *Takeaway*: The sharper, less-blurry structures reconstructed by the autoencoder help the classifier predict difficult classes with higher confidence (e.g., Pullover accuracy increases to 73% under AE vs 63% under Pixel/PCA; Shirt accuracy increases to 51% under AE vs ~45% under Pixel/PCA).

---

### Recitation 2 Summary & Key Takeaways

In this recitation, we studied representation learning for unstructured image data using the Fashion MNIST dataset. We began by training baseline classifiers on raw pixel inputs and then compared different ways of representing images, including raw pixels, PCA, and autoencoders. 

We evaluated these representations through reconstruction quality, classification performance, and qualitative analyses such as nearest neighbors and class centroids. This helped illustrate how representation choices affect both learning efficiency and semantic similarity.

#### Key Takeaways:
1. **Raw Pixels Limitations**: Raw pixel representations are high-dimensional, redundant, and often inefficient for learning (Euclidean distance on pixels is sensitive to shifts and does not reflect semantic similarity).
2. **PCA (Principal Component Analysis)**: Provides a simple, linear method for compressing images while preserving the directions of greatest variance. It is simple, highly efficient, and effective for simpler datasets like Fashion MNIST (reconstructed test set accuracy of **87.59%** using 187 features).
3. **Autoencoders**: Neural networks that learn nonlinear latent representations optimized directly for reconstruction (reconstruction loss). They preserve fine-grained, curved structures, producing sharper and less-blurry class centroids (average prototypes) compared to PCA.
4. **Trade-offs**: Different representations involve trade-offs between simplicity, reconstruction quality, and downstream performance. PCA emphasizes global variance, Autoencoders preserve fine-grained structures, and CNNs directly exploit 2D spatial layouts (achieving the highest test accuracy of **90.14%**).
5. **Efficiency Gains**: Compressing the representation space allows us to train smaller models with fewer parameters and faster training times while maintaining comparable classification accuracy.
