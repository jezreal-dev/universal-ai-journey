# Module 8: Deep Learning and Computer Vision — Recitation Notes

## 💻 Recitation 1: Deep Learning for Image Classification

### Overview & Setup
**Instructor**: Vassilina Stoumpou (PhD Candidate, MIT Operations Research Center)  
**Notebook**: [mod7_rec1.ipynb](file:///C:/Users/USER/Downloads/mod7_rec1.ipynb)  
**Covered Lectures**: Lecture 1 (Introduction to Deep Learning) & Lecture 2 (Computer Vision and Transfer Learning)

#### Frameworks & Hardware Runtime
* **PyTorch vs. TensorFlow**:
  * **PyTorch**: Preferred in academic research and custom architecture design due to adaptive computation graphs and explicit control over training loops.
  * **TensorFlow / Keras**: Streamlined for rapid prototyping, production deployment, and high-level abstractions.
* **Hardware Acceleration (GPU)**:
  * Training CNNs on multi-channel image tensors involves intense parallel matrix multiplications.
  * Switching runtime to GPU (e.g. NVIDIA T4 GPU) accelerates training by orders of magnitude compared to standard CPUs.

---

### 1️⃣ Data Preparation and Loaders in PyTorch

#### The CIFAR-10 Dataset
* **Specifications**: 60,000 $32 \times 32$ RGB color images across 10 balanced categories (6,000 images/class).
* **Standard Split**: 50,000 training images and 10,000 test images.
* **Classes (Labels 0–9)**:
  | Label | Category | Label | Category |
  | :---: | :--- | :---: | :--- |
  | `0` | Airplane | `5` | Dog |
  | `1` | Automobile | `6` | Frog |
  | `2` | Bird | `7` | Horse |
  | `3` | Cat | `8` | Ship |
  | `4` | Deer | `9` | Truck |

#### PyTorch Transformation & Loading Pipeline
```python
import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

# 1. Image Preprocessing Transformation
transform = transforms.Compose([
    transforms.ToTensor()  # Converts PIL/NumPy uint8 [0, 255] (HxWxC) to FloatTensor [0.0, 1.0] (CxHxW)
])

# 2. Download and Load Dataset
train_set = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_set = torchvision.datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

# 3. Train-Validation Split (80% Train, 20% Validation)
train_size = int(0.8 * len(train_set))  # 40,000 samples
eval_size = len(train_set) - train_size  # 10,000 samples
train_set, eval_set = torch.utils.data.random_split(
    train_set, [train_size, eval_size], generator=torch.Generator().manual_seed(42)
)

# 4. DataLoader Construction
BATCH_SIZE = 32
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
eval_loader = DataLoader(eval_set, batch_size=BATCH_SIZE, shuffle=False)
test_loader = DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=False)
```

#### Key DataLoader Parameters & Concepts
1. **`transforms.ToTensor()`**:
   * Reorders dimensions from Matplotlib/Image format $(H \times W \times C)$ to PyTorch Tensor format $(C \times H \times W)$.
   * Automatically rescales integer pixel values $[0, 255]$ into floating-point range $[0.0, 1.0]$.
2. **Batching (`batch_size=32`)**:
   * Divides data into mini-batches to balance memory efficiency, gradient update stability, and training throughput.
3. **Shuffling (`shuffle=True`)**:
   * Randomizes mini-batch sequence ordering every epoch during training to prevent the model from learning artificial sequence dependencies.

#### Image Visualization Tensor Permutation
PyTorch stores image tensors in Channel-First format $(C \times H \times W)$, whereas `matplotlib.pyplot.imshow` requires Channel-Last format $(H \times W \times C)$. Thus, visualizing tensors requires `.permute(1, 2, 0)`:

```python
import matplotlib.pyplot as plt

sample_image, sample_label = train_set[0]
# Permute (C, H, W) -> (H, W, C) for Matplotlib rendering
plt.imshow(sample_image.squeeze().permute(1, 2, 0).numpy())
plt.title(f"Label: {sample_label} ({classes[sample_label]})")
plt.show()
```

---

### 2️⃣ Feedforward Neural Network (FNN) Baseline in PyTorch

#### Architecture Definition (`nn.Module`)
A simple multi-layer feedforward neural network (MLP) flattens 3D RGB images ($3 \times 32 \times 32 = 3072$ inputs) into a 1D vector and passes them through dense linear layers:

```python
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self):
        super(NeuralNet, self).__init__()
        self.flatten = nn.Flatten()  # Flattens (B, 3, 32, 32) into (B, 3072)
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(3 * 32 * 32, 512),  # Layer 1: 3072 -> 512
            nn.ReLU(),                    # Non-linear activation
            nn.Linear(512, 10)            # Layer 2 (Output): 512 -> 10 classes
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
```

#### Parameter Breakdown
* **Layer 1 (`Linear(3072, 512)`)**: $3072 \times 512 + 512 = 1,573,376$ parameters.
* **Layer 2 (`Linear(512, 10)`)**: $512 \times 10 + 10 = 5,130$ parameters.
* **Total Trainable Parameters**: **1,578,506** (~6.02 MB).

#### Training Pipeline Setup
```python
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
net = NeuralNet().to(device)

# Loss Function & Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
```

#### Training Loop Execution & Convergence Results
The model was trained for 5 epochs over 1,250 mini-batches per epoch (batch size 32):

```python
def train_model(net, train_loader, eval_loader, optimizer, criterion, num_epoch=5):
    for epoch in range(num_epoch):
        running_loss = 0.0
        net.train()
        for i, (inputs, labels) in enumerate(train_loader):
            inputs, labels = inputs.to(device), labels.to(device)
            
            optimizer.zero_grad()   # 1. Reset gradients
            outputs = net(inputs)   # 2. Forward pass
            loss = criterion(outputs, labels) # 3. Compute loss
            loss.backward()         # 4. Backpropagation
            optimizer.step()        # 5. Weight update
            running_loss += loss.item()
            
        # Validation Evaluation
        net.eval()
        correct, total = 0, 0
        with torch.no_grad():
            for images, labels in eval_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = net(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
        
        accuracy = 100 * correct / total
        print(f"Epoch {epoch+1} Accuracy: {accuracy:.2f}%")
```

#### FNN Baseline Performance Log:
* **Epoch 1**: Validation Accuracy = **35.07%**
* **Epoch 2**: Validation Accuracy = **39.73%**
* **Epoch 3**: Validation Accuracy = **40.51%**
* **Epoch 4**: Validation Accuracy = **42.61%**
* **Epoch 5**: Validation Accuracy = **44.43%**
* **Final Test Accuracy (10,000 images)**: **44.86%**

#### Validation Tracking & Generalizable Evaluation
* **Why Track Validation Metrics?**: During training, validation accuracy is evaluated at the end of each epoch rather than relying solely on training loss. Unseen validation performance is the true measure of generalization.
* **`torch.no_grad()` Context**: Temporarily disables autograd engine and gradient computation during validation and test loops, dramatically reducing GPU memory footprint and preventing unwanted parameter updates.

#### Diagnostic Error Analysis & Confusion Matrix
To pinpoint where the feedforward model fails, we compute the confusion matrix (`sklearn.metrics.confusion_matrix`) and display it using `ConfusionMatrixDisplay`:

```python
import sklearn.metrics as metrics

def compute_confusion_matrix(net, test_loader, classes):
    all_labels, all_predicted = [], []
    net.eval()
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = net(images)
            _, predicted = torch.max(outputs, 1)
            all_labels.extend(labels.cpu().numpy())
            all_predicted.extend(predicted.cpu().numpy())
    return metrics.confusion_matrix(all_labels, all_predicted)
```

##### Class-Level Error Patterns:
* **Hardest Classes**:
  * **Birds**: Frequently misclassified as deer, dogs, or cats due to lack of spatial feature extraction.
  * **Cats**: High confusion rate with dogs and other quadrupeds.
* **Best Performing Classes**:
  * **Airplanes** and **Frogs**: Highest diagonal counts due to distinct sky background/wing shapes and green color profiles.
* **Misclassified Example Inspection**:
  * Visualizing false predictions (e.g. *Ship* predicted as *Truck*, *Frog* predicted as *Deer*) confirms that global pixel intensity alone fails to capture localized shapes.

#### Section Takeaway & Motivation for CNNs
The feedforward baseline achieves an unsatisfactory test accuracy of **~44.86%**. Flattening $32 \times 32 \times 3$ image matrices into 1D vectors destroys spatial pixel adjacencies and demands 1.57 million unconstrained dense weights without spatial translation invariance. This directly motivates **Convolutional Neural Networks (CNNs)**.

---

### 3️⃣ Convolutional Neural Networks (CNN) in PyTorch

#### Architectural Concepts & Layer Roles
1. **Convolutional Layers (`torch.nn.Conv2d`)**:
   * Replace fully connected linear layers in the feature extraction stage.
   * Slide small parameter filters (kernels) across local receptive fields to detect localized visual primitives (edges, textures, shapes).
   * **Parameter Sharing**: The same 2D filter weights are reused across the entire image, dramatically reducing parameter count while achieving spatial translation invariance.
2. **Pooling Layers (`torch.nn.MaxPool2d`)**:
   * Downsample feature map spatial dimensions $(H \times W)$, reducing computational complexity and memory footprint.
   * Enforce local spatial invariance: small translations in input features produce identical pooled outputs.
3. **Flattening & Classification Stage**:
   * Transition from 3D spatial feature maps $(C \times H \times W)$ to a 1D vector (`x.view(-1, 256 * 8 * 8)` or `nn.Flatten()`) before feeding into dense linear classifier layers (`fc1`, `fc2`).

#### PyTorch `CNN` Class Architecture
```python
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # Conv Block 1
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # Conv Block 2
        self.conv3 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1)
        self.conv4 = nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1)

        # Fully Connected Classification Stack
        self.fc1 = nn.Linear(256 * 8 * 8, 512)
        self.fc2 = nn.Linear(512, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))      # Shape: (B, 64, 32, 32)
        x = F.relu(self.conv2(x))      # Shape: (B, 128, 32, 32)
        x = self.pool(x)               # Shape: (B, 128, 16, 16)
        x = F.relu(self.conv3(x))      # Shape: (B, 256, 16, 16)
        x = F.relu(self.conv4(x))      # Shape: (B, 256, 16, 16)
        x = self.pool(x)               # Shape: (B, 256, 8, 8)
        x = x.view(-1, 256 * 8 * 8)    # Flatten 3D map -> 1D vector (16,384 dims)
        x = F.relu(self.fc1(x))        # Dense Layer 1: 16,384 -> 512
        x = self.fc2(x)                # Output Layer: 512 -> 10 classes
        return x
```

#### Step-by-Step Spatial Feature Map Derivation
* **Input Image**: $3 \times 32 \times 32$
* **`conv1` ($3 \to 64, k=3, p=1$)**: Zero-padding ($p=1$) preserves spatial resolution $\Rightarrow 64 \times 32 \times 32$.
* **`conv2` ($64 \to 128, k=3, p=1$)**: Resolution preserved $\Rightarrow 128 \times 32 \times 32$.
* **`pool1` ($k=2, s=2$)**: Max pooling with stride 2 halves height and width $\Rightarrow 128 \times 16 \times 16$.
* **`conv3` ($128 \to 256, k=3, p=1$)**: Resolution preserved $\Rightarrow 256 \times 16 \times 16$.
* **`conv4` ($256 \to 256, k=3, p=1$)**: Resolution preserved $\Rightarrow 256 \times 16 \times 16$.
* **`pool2` ($k=2, s=2$)**: Max pooling with stride 2 halves height and width $\Rightarrow 256 \times 8 \times 8$.
* **Flattening Calculation**: $256 \text{ channels} \times 8 \text{ height} \times 8 \text{ width} = \mathbf{16,384 \text{ elements}}$.

#### Optimization with Adam & Weight Decay
```python
net = CNN().to(device)
criterion = nn.CrossEntropyLoss()

# Adam Optimizer with weight_decay for L2 regularization
optimizer = optim.Adam(net.parameters(), lr=0.001, weight_decay=1e-4)

# Train CNN for 5 Epochs
train_model(net, train_loader, eval_loader, optimizer, criterion, num_epoch=5)
test_model(net, test_loader)
```

#### Convergence & Test Performance
* **Epoch 1**: Validation Accuracy = **60.91%**
* **Epoch 2**: Validation Accuracy = **70.02%**
* **Epoch 3**: Validation Accuracy = **73.45%**
* **Epoch 4**: Validation Accuracy = **72.87%**
* **Epoch 5**: Validation Accuracy = **73.94%**
* **Final Test Accuracy (10,000 images)**: **73.10%**

#### Performance Comparison: FNN vs. CNN
| Model Architecture | Input Format | Spatial Invariance | Train/Test Accuracy | Key Advantage / Drawback |
| :--- | :---: | :---: | :---: | :--- |
| **Feedforward NN (FNN)** | Flattened 1D ($3072$) | ❌ No | **44.86%** | High parameter cost, ignores pixel geometry. |
| **Convolutional NN (CNN)** | 3D Tensor ($3 \times 32 \times 32$) |  Yes | **73.10%** | Preserves spatial structure, parameter sharing. |

#### Further CNN Optimization Strategies
* **Deeper Architectures**: Adding residual connections (ResNet) or additional convolution blocks.
* **Dropout Regularization**: Adding `nn.Dropout(p=0.5)` after dense layers to prevent co-adaptation.
* **Data Augmentation**: Applying random horizontal flips, cropping, and color jitter to increase training variance.
* **Learning Rate Schedules & Early Stopping**: Dynamically decaying learning rate on loss plateaus and terminating training when validation loss stops improving.

---

### 4️⃣ Deep Learning with Keras and TensorFlow

#### Data Loading with `tensorflow_datasets` (TFDS)
Keras provides high-level abstractions via `tensorflow_datasets` to download, split, and batch datasets cleanly:

```python
import tensorflow as tf
import tensorflow_datasets as tfds

ds_name = 'cifar10'

# Train (80%) and Validation (20%) Split
(train_ds, val_ds), info = tfds.load(
    ds_name, split=["train[:80%]", "train[80%:]"], batch_size=32, as_supervised=True, with_info=True
)

test_ds, info_test = tfds.load(
    ds_name, split="test", batch_size=32, as_supervised=True, with_info=True
)

# Pixel Normalization [0, 255] -> [0.0, 1.0]
def preprocess(image, label):
    image = tf.cast(image, tf.float32) / 255.0
    return image, label

train_ds_processed = train_ds.map(preprocess).shuffle(len(train_ds))
val_ds_processed = val_ds.map(preprocess)
test_ds_processed = test_ds.map(preprocess)
```

#### Keras FNN Baseline Implementation
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, ReLU, Input

model_fnn = Sequential([
    Input(shape=(32, 32, 3)),
    Flatten(),
    Dense(512),
    ReLU(),
    Dense(10, activation='softmax')
])

model_fnn.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model_fnn.fit(train_ds_processed, epochs=5, validation_data=val_ds_processed)
test_loss, test_acc = model_fnn.evaluate(test_ds_processed, verbose=0)
print(f"Keras FNN Test Accuracy: {test_acc * 100:.2f}%")  # Output: 41.02%
```

#### Keras CNN Implementation (`padding='same'`)
In Keras, specifying `padding='same'` automatically calculates and injects zero-padding so spatial dimensions remain unchanged across convolutions:

```python
from tensorflow.keras.layers import Conv2D, MaxPooling2D

model_cnn = Sequential([
    Input((32, 32, 3)),
    # Block 1
    Conv2D(64, kernel_size=3, padding='same'),
    ReLU(),
    Conv2D(128, kernel_size=3, padding='same'),
    ReLU(),
    MaxPooling2D(pool_size=2, strides=2),  # 32x32 -> 16x16

    # Block 2
    Conv2D(256, kernel_size=3, padding='same'),
    ReLU(),
    Conv2D(256, kernel_size=3, padding='same'),
    ReLU(),
    MaxPooling2D(pool_size=2, strides=2),  # 16x16 -> 8x8

    # Classification Head
    Flatten(),                             # 8x8x256 = 16,384
    Dense(512),
    ReLU(),
    Dense(10, activation='softmax')
])

model_cnn.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model_cnn.fit(train_ds_processed, epochs=5, validation_data=val_ds_processed)
test_loss, test_acc = model_cnn.evaluate(test_ds_processed, verbose=0)
print(f"Keras CNN Test Accuracy: {test_acc * 100:.2f}%")  # Output: 73.59%
```

---

### 5️⃣ Transfer Learning and Fine-Tuning with MobileNetV2

#### Core Transfer Learning Workflow
Transfer learning leverages pre-trained feature representations from large-scale datasets (e.g. **ImageNet** with 1.4 million images and 1,000 classes) to solve new tasks with limited training samples.

```
+------------------------------------+
|  Pre-trained Base (MobileNetV2)    |  <-- FROZEN (154 Base Layers)
|  Extracts Low & High-Level Features|      `base_model.trainable = False`
+------------------------------------+
                  |
                  v
+------------------------------------+
|  GlobalAveragePooling2D + Dropout  |  <-- Feature Vector (1280 dims)
+------------------------------------+
                  |
                  v
+------------------------------------+
|  Dense Output Layer (10 classes)   |  <-- TRAINABLE Classifier
+------------------------------------+
```

#### Step 1: Bottleneck Feature Extraction (Frozen Base)
We use `MobileNetV2(include_top=False)` to strip the original 1000-class ImageNet top classifier, keeping the **bottleneck layer** for feature extraction:

```python
SIZE = 128  # Resizing 32x32 image input closer to MobileNetV2 standard (224x224)

# 1. Load Pre-trained Base
base_model = tf.keras.applications.MobileNetV2(
    weights="imagenet",
    input_shape=(SIZE, SIZE, 3),
    include_top=False  # Exclude top 1000-class classification head
)
base_model.trainable = False  # Freeze all base layers

# 2. Build Pipeline Graph
inputs = tf.keras.Input(shape=(32, 32, 3))
x = tf.keras.layers.Resizing(SIZE, SIZE)(inputs)
x = tf.keras.applications.mobilenet_v2.preprocess_input(x)  # Scales [0, 255] -> [-1, 1]

# Pass through base model in inference mode to preserve BatchNorm statistics
x = base_model(x, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)  # Averages 4x4x1280 -> 1280 vector
x = tf.keras.layers.Dropout(0.2)(x)              # Regularization
outputs = tf.keras.layers.Dense(10, activation="softmax")(x)

model_transfer = tf.keras.Model(inputs, outputs)
model_transfer.summary()
```

##### Parameter Breakdown (Feature Extraction):
* **Total Parameters**: **2,270,794** (8.66 MB)
* **Trainable Parameters**: **12,810** (50.04 KB) — Only dense output layer!
* **Non-trainable Parameters**: **2,257,984** (8.61 MB) — Frozen MobileNetV2 base.

##### Training Feature Extractor (5 Epochs):
```python
model_transfer.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model_transfer.fit(train_ds, epochs=5, validation_data=val_ds)
test_loss, test_acc = model_transfer.evaluate(test_ds, verbose=0)
print(f"Feature Extraction Test Accuracy: {test_acc * 100:.2f}%")  # Output: 84.31%
```
* **Performance Jump**: Reaches **84.31%** test accuracy (+11.2% over custom 73.1% CNN)!

---

#### Step 2: Fine-Tuning (Unfreezing Upper Layers)
To adapt general ImageNet representations to CIFAR-10 specific visual features, we unfreeze the top layers of `MobileNetV2` while leaving early low-level edge/texture layers frozen:

```python
# 1. Set entire base model to trainable
base_model.trainable = True

# 2. Freeze all layers before the 50th layer (out of 154 total layers)
fine_tune_at = 50
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False

# 3. Re-compile with a VERY LOW learning rate to prevent destroying pre-trained weights
model_transfer.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),  # Low LR = 1e-4!
    metrics=['accuracy']
)

# 4. Resume training for 2 additional fine-tuning epochs (Epochs 6 & 7)
fine_tune_epochs = 2
total_epochs = 5 + fine_tune_epochs

history_fine = model_transfer.fit(
    train_ds,
    epochs=total_epochs,
    initial_epoch=history.epoch[-1] + 1,  # Resume from Epoch 5
    validation_data=val_ds
)

test_loss, test_acc = model_transfer.evaluate(test_ds, verbose=0)
print(f"Fine-Tuning Test Accuracy: {test_acc * 100:.2f}%")  # Output: 90.15%
```

##### Critical Rules for Fine-Tuning:
1. **Low Learning Rate ($\eta = 10^{-4}$)**: A standard learning rate ($10^{-3}$) will cause massive gradient updates that overwrite pre-trained representations.
2. **Short Epoch Count (1–3 Epochs)**: Prevents catastrophic forgetting and overfitting on small target datasets.
3. **BatchNorm Inference Mode (`training=False`)**: Keep Batch Normalization layers in inference mode during fine-tuning so running means/variances are not distorted by small mini-batches.

##### Fine-Tuning Performance Log:
* **Epoch 6**: Validation Accuracy = **89.10%**
* **Epoch 7**: Validation Accuracy = **90.69%**
* **Final Test Accuracy (10,000 images)**: **90.15%** (Surpassing **90%** benchmark!).

---

### 6️⃣ Summary of Recitation 1 Results & Framework Synthesis

| Model Architecture | Framework | Training Strategy | Trainable Parameters | Validation Accuracy | Final Test Accuracy | Key Takeaway / Benchmark Impact |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **PyTorch FNN** | PyTorch | SGD + Momentum (5 Ep) | 1,578,506 | 44.43% | **44.86%** | Ignores 2D spatial layout; parameter bloat. |
| **Keras FNN** | Keras / TF | SGD + Momentum (5 Ep) | ~1.57M | 42.21% | **41.02%** | Validates baseline across frameworks (~41–45%). |
| **PyTorch CNN** | PyTorch | Adam + Weight Decay (5 Ep) | ~1.18M | 73.94% | **73.10%** | Massive **+28.2%** gain via spatial convolutions. |
| **Keras CNN** | Keras / TF | Adam (5 Ep) | ~1.18M | 74.20% | **73.59%** | Identical performance with Keras `padding='same'`. |
| **MobileNetV2 Feature Extraction** | Keras / TF | Frozen Base (5 Ep) | 12,810 | 85.24% | **84.31%** | Reuses ImageNet representations; **+11.2%** gain. |
| **MobileNetV2 Fine-Tuning** | Keras / TF | Unfreeze Top 104 Layers (2 Ep) | ~1.5M | 90.69% | **90.15%** | Reaches **90.15%** test accuracy on CIFAR-10. |

#### Key Takeaways:
1. **FNNs vs. CNNs for Vision**:
   * FNNs flatten images, discarding spatial grid geometry and generating over a million unconstrained parameters that struggle to generalize (~41–45%).
   * CNNs preserve 2D grid structure using parameter sharing and pooling layers to achieve spatial translation invariance and superior performance (~73–74%).
2. **Framework Complementarity**:
   * **PyTorch** excels in research flexibility, explicit tensor permuting (`.permute(1, 2, 0)`), and fine-grained autograd control.
   * **Keras / TensorFlow** excels in rapid prototyping with built-in preprocessing layers (`Resizing`, `preprocess_input`), `tfds` data loaders, and concise high-level `fit()` / `evaluate()` APIs.
3. **Transfer Learning Mastery**:
   * Leveraging pre-trained feature extractors (e.g. MobileNetV2 trained on ImageNet) boosts performance dramatically while using only a fraction of trainable parameters (12.8k params $\to$ 84.31%).
   * Unfreezing deep layers for fine-tuning with a very small learning rate ($\eta = 10^{-4}$) yields elite performance (**90.15%** test accuracy).

---

### 📝 Official Recitation Summary

In this recitation, we explored how to implement deep learning models for image classification using both PyTorch and TensorFlow. Starting with the CIFAR-10 dataset, we prepared and visualized the data, constructed feedforward neural networks (FNNs), and examined their limitations on image tasks. We then introduced convolutional neural networks (CNNs), showing how convolutional and pooling layers improve performance by capturing spatial hierarchies. Finally, we applied transfer learning with MobileNetV2 in Keras, first freezing pretrained layers and then fine-tuning upper layers to further boost accuracy.

#### Key Takeaways:
* **Data Preparation for Images**: Involves converting images to tensors, normalizing pixel values, batching, and shuffling. DataLoaders (PyTorch) and preprocessing pipelines (TensorFlow/Keras) streamline this process.
* **Feedforward Neural Networks**: Can be trained on flattened images but generally underperform because they ignore spatial structure; in our case, accuracy was around **45%**.
* **Convolutional Neural Networks**: Introduce convolutional filters, ReLU activations, and pooling layers to preserve local patterns and reduce dimensionality, leading to much stronger performance (**~75% accuracy**).
* **Transfer Learning**: Allows us to leverage pretrained models such as MobileNetV2. Freezing the base model and retraining only the classifier boosted accuracy to **~85%**, while fine-tuning selected layers increased it further to **~90%**.
* **Regularization Techniques**: Such as dropout, weight decay, early stopping, and careful choice of learning rate help avoid overfitting during training and fine-tuning.




