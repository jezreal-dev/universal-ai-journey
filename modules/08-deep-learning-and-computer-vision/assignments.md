# Module 8: Deep Learning and Computer Vision — Assignment Notes

## 📝 Assignment 1: Introduction to Deep Learning with TensorFlow (Fashion MNIST)

### Overview & Setup
**Notebook**: [mod7_assign1.ipynb](file:///C:/Users/USER/Downloads/mod7_assign1.ipynb)  
**Dataset**: Fashion MNIST (Zalando Research)  
**Framework**: TensorFlow 2.x / Keras  
**Random Seed**: `42` (ensuring deterministic initialization and reproducibility)

---

### 1️⃣ Dataset Exploration and Visualization

#### Dataset Structure
* **Training Set**: 60,000 grayscale images, each of size $28 \times 28$ pixels (`x_train.shape = (60000, 28, 28)`).
* **Test Set**: 10,000 grayscale images, each of size $28 \times 28$ pixels (`x_test.shape = (10000, 28, 28)`).
* **Pixel Intensity Range**: Integers from `0` (black background) to `255` (white foreground).

#### Class Labels and Distribution
The dataset contains 10 balanced categories with exactly **6,000 images per class** in the training set:

| Class Index | Label Name | Training Count |
| :---: | :--- | :---: |
| `0` | T-shirt/top | 6,000 |
| `1` | Trouser | 6,000 |
| `2` | Pullover | 6,000 |
| `3` | Dress | 6,000 |
| `4` | Coat | 6,000 |
| `5` | Sandal | 6,000 |
| `6` | Shirt | 6,000 |
| `7` | Sneaker | 6,000 |
| `8` | Bag | 6,000 |
| `9` | Ankle boot | 6,000 |

---

### 2️⃣ Feedforward Neural Networks (FNN)

#### Data Preprocessing & Vector Reshaping
1. **Normalization**: Pixel intensities scaled to $[0.0, 1.0]$ via floating-point division (`x_train / 255.0`).
2. **Flattening**: 2D matrices ($28 \times 28$) reshaped into 1D 784-element vectors (`x_train.reshape(60000, 784)`).

#### FNN Architecture 1 (Single Hidden Layer)
```python
import tensorflow as tf
from tensorflow import keras

model_fnn1 = keras.Sequential([
    keras.Input(shape=(28 * 28,)),
    keras.layers.Dense(256, activation="relu", name="Hidden"),
    keras.layers.Dense(10, activation="softmax", name="Output")
])

model_fnn1.compile(
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
```

##### Parameter Breakdown:
* **`Hidden` (`Dense(784, 256)`)**: $784 \times 256 + 256 = \mathbf{200,960}$ parameters.
* **`Output` (`Dense(256, 10)`)**: $256 \times 10 + 10 = \mathbf{2,570}$ parameters.
* **Total Trainable Parameters**: **203,530** (~795 KB).

##### FNN 1 Training Log (10 Epochs, Batch Size 64, 20% Val Split):
* **Epoch 1**: Train Acc = 76.76%, Val Acc = **85.65%**, Val Loss = 0.4108
* **Epoch 5**: Train Acc = 89.20%, Val Acc = **88.25%**, Val Loss = 0.3393
* **Epoch 10**: Train Acc = 91.64%, Val Acc = **88.52%**, Val Loss = 0.3334
* **Final Evaluation**:
  * **Train Accuracy**: **90.86%**
  * **Test Accuracy**: **87.40%**

#### FNN Architecture 2 (Two Hidden Layers + Dropout Regularization)
To test if added depth improves generalization, a second 256-node hidden layer and two 20% Dropout layers (`Dropout(0.2)`) were added:

```python
model_fnn2 = keras.Sequential([
    keras.Input(shape=(28 * 28,)),
    keras.layers.Dense(256, activation="relu", name="Hidden_1"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(256, activation="relu", name="Hidden_2"),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation="softmax", name="Output")
])
```

##### Parameter Breakdown:
* **`Hidden_1` (`Dense(784, 256)`)**: $200,960$ params.
* **`Dropout`**: $0$ params.
* **`Hidden_2` (`Dense(256, 256)`)**: $256 \times 256 + 256 = \mathbf{65,792}$ params.
* **`Dropout`**: $0$ params.
* **`Output` (`Dense(256, 10)`)**: $2,570$ params.
* **Total Trainable Parameters**: **269,322** (1.03 MB).

---

### 3️⃣ Convolutional Neural Network (CNN)

#### Spatial Reshaping & Architecture
Images are reshaped back into 3D tensors $(28 \times 28 \times 1)$ for 2D spatial convolution:

```python
# Reshape 1D vector -> 3D Image Tensor (H, W, C)
x_train_cnn = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test_cnn = x_test.reshape(x_test.shape[0], 28, 28, 1)

model_cnn = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),
    
    # Conv Block 1
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'), # Output: (26, 26, 32)
    keras.layers.MaxPooling2D(pool_size=(2, 2)),                     # Output: (13, 13, 32)
    
    # Conv Block 2
    keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'), # Output: (11, 11, 64)
    keras.layers.MaxPooling2D(pool_size=(2, 2)),                     # Output: (5, 5, 64)
    
    # Dense Classifier Head
    keras.layers.Flatten(),                                         # 5x5x64 = 1600 dims
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
```

#### Detailed Layer-by-Layer Shape & Parameter Derivation

| Layer Name | Layer Type | Output Feature Map Shape | Weight & Bias Calculation Formula | Parameter Count |
| :--- | :---: | :---: | :---: | :---: |
| `input` | `InputLayer` | `(None, 28, 28, 1)` | N/A | `0` |
| `conv2d_2` | `Conv2D` (32 filters, $3 \times 3$) | `(None, 26, 26, 32)` | $(3 \times 3 \times 1 \times 32) + 32$ | **320** |
| `max_pooling2d_2` | `MaxPooling2D` ($2 \times 2$) | `(None, 13, 13, 32)` | Downsamples height & width by 2 | `0` |
| `conv2d_3` | `Conv2D` (64 filters, $3 \times 3$) | `(None, 11, 11, 64)` | $(3 \times 3 \times 32 \times 64) + 64$ | **18,496** |
| `max_pooling2d_3` | `MaxPooling2D` ($2 \times 2$) | `(None, 5, 5, 64)` | Downsamples height & width by 2 | `0` |
| `flatten_1` | `Flatten` | `(None, 1600)` | $5 \times 5 \times 64 = 1600$ | `0` |
| `dense_2` | `Dense` (128 units) | `(None, 128)` | $(1600 \times 128) + 128$ | **204,928** |
| `dense_3` | `Dense` (10 units) | `(None, 10)` | $(128 \times 10) + 10$ | **1,290** |
| **Total** | | | | **225,034** (~879 KB) |

#### CNN Training & Loss Trajectory Analysis
```python
opt = keras.optimizers.Adam(learning_rate=0.001)
model_cnn.compile(
    loss='sparse_categorical_crossentropy',
    optimizer=opt,
    metrics=['accuracy']
)

history_cnn = model_cnn.fit(
    x_train_cnn, y_train, batch_size=64, epochs=10, validation_split=0.2
)
```

##### Epoch-by-Epoch Progress:
* **Epoch 1**: Train Acc = 74.20%, Loss = 0.7241 | Val Acc = **87.37%**, Val Loss = **0.3625**
* **Epoch 4**: Train Acc = 90.31%, Loss = 0.2690 | Val Acc = **89.92%**, Val Loss = **0.2790** *(Minimum Val Loss)*
* **Epoch 5**: Train Acc = 91.39%, Loss = 0.2396 | Val Acc = **89.88%**, Val Loss = **0.2805**
* **Epoch 10**: Train Acc = 95.23%, Loss = 0.1354 | Val Acc = **89.75%**, Val Loss = **0.3335**

##### Final Test Set Evaluation:
* **Test Accuracy**: **89.33%** (Outperforming the FNN baseline of **87.40%** by **+1.93%**).

##### Loss Curve & Overfitting Analysis:
* **Optimal Epoch Window**: Validation loss reaches its global minimum at **Epoch 4–5 (~0.2790)**.
* **Overfitting Onset**: Beyond Epoch 5, training loss drops steeply from `0.2396` to `0.1354` (training accuracy climbing to `95.23%`), while validation loss increases back up to `0.3335`. This widening gap indicates that training for 10 epochs causes slight overfitting, making **Epoch 4–5 or Early Stopping** ideal.

---

### 4️⃣ Comprehensive Performance & Model Comparison

| Model Architecture | Input Shape | Spatial Feature Extraction | Total Parameters | Train Accuracy | Test Accuracy | Overfitting / Generalization Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **FNN 1 (Single Hidden 256)** | Flattened 1D ($784$) | ❌ No | 203,530 | 90.86% | **87.40%** | Moderate performance; ignores pixel geometry. |
| **FNN 2 (2 Hidden 256 + Dropout)** | Flattened 1D ($784$) | ❌ No | 269,322 | — | — | Dropout reduces co-adaptation; higher capacity. |
| **CNN (Conv32-Conv64-Dense128)** | 2D Tensor ($28 \times 28 \times 1$) |  Yes | 225,034 | 95.23% | **89.33%** | **Best Accuracy**; slight overfitting after Ep 5. |
| **State-of-the-Art (SOTA)** | Various |  Yes | Various | — | **96.91%** | Benchmark target on Fashion MNIST. |

#### Key Takeaways:
1. **Convolutions Outperform Flattened Dense Layers**: CNN achieves **89.33%** test accuracy compared to **87.40%** for FNN, verifying that preserving 2D spatial structure and extracting local features (edges, textures) yields superior image classification.
2. **Parameter Efficiency**: The CNN achieves higher accuracy with only **225,034** parameters compared to FNN 2's **269,322** parameters due to weight sharing.
3. **Validation Loss Monitoring**: Tracking validation loss identifies overfitting early (Epoch 5 in CNN), highlighting the need for early stopping or dropout in deep vision architectures.

---

### 📝 Official Assignment Summary

In this assignment, you reviewed key concepts in building and evaluating neural networks for image classification. Through guided questions, you explored data preprocessing, the role of Feedforward Neural Networks (FNNs) as a baseline, and how Convolutional Neural Networks (CNNs) improve performance by capturing spatial structure. You also examined training dynamics, model evaluation, and common challenges such as overfitting.

#### Key Takeaways:
* **Proper Data Preparation**: Reshaping and normalization (e.g. scaling $[0, 255] \to [0, 1]$) are essential prior to training.
* **FNNs as Baselines**: Provide a simple baseline but underperform on image data because they discard 2D spatial relationships.
* **CNN Performance**: Leverage convolutions, pooling, and weight sharing to preserve spatial patterns and boost accuracy.
* **Overfitting Detection**: Comparing training vs. validation loss curves identifies the onset of overfitting and optimal early stopping points.
* **Error Diagnostics**: Tools like the confusion matrix provide targeted insights into common class misclassifications (e.g. Shirt vs. Pullover vs. T-shirt).

