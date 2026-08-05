# Lecture Notes – Multimodal AI

---

## 🏗️ Lecture 1: Introduction to Multimodal AI

### 1. Modality Definition & Taxonomy

A **modality** refers to a distinct physical channel or information format through which an entity perceives or encodes information:
* **Human Sensory Modalities**: Vision, Hearing, Touch, Taste, Smell.
* **Machine Modalities**: Natural Language Text, 2D Images, 3D Point Clouds, Audio Spectrograms, EHR Tabular Features, ECG Time-Series Signals, Spatio-Temporal Radar Arrays.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             Multimodal AI Taxonomies                             │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Single-Modality (Unimodal)    │ Text-only (GPT-3), Image-only (ResNet)           │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ Cross-Modal Translation       │ Text-to-Image (Stable Diffusion), Speech-to-Text │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ Multimodal Fusion             │ Fusing EHR + CXR + ECG + Text (HAIM Framework)   │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

### 2. The 6 Core Challenges of Multimodal AI

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           6 Core Multimodal Challenges                           │
├───────────────────┬──────────────────────────────────────────────────────────────┤
│ 1. Representation │ Learning Joint vs. Coordinated latent embedding spaces.      │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ 2. Translation    │ Mapping signals from modality A to modality B (e.g. BLIP).   │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ 3. Alignment      │ Identifying sub-component cross-modal relationships.         │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ 4. Fusion         │ Combining information streams at Early, Mid, or Late stages. │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ 5. Co-learning    │ Transferring knowledge from resource-rich to sparse modal.   │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ 6. Reasoning      │ Performing multi-step compositional inference across inputs. │
└───────────────────┴──────────────────────────────────────────────────────────────┘
```

---

## 🏥 Lecture 2: HAIM: Holistic AI for Medicine

### 1. Multimodal Clinical Integration Framework

Clinical healthcare is inherently multimodal. Single-modality models (e.g., image-only CXR classifiers) miss critical patient context contained in lab values or clinical notes.

The **HAIM (Holistic AI for Medicine)** framework unifies 4 distinct patient data streams:

```
  [EHR Tabular (Labs/Vitals)] ──┐
  [CXR Chest X-Ray Images]     ──┼──► Multimodal Feature Processor ──► Joint Fusion Network ──► 33 Clinical Targets
  [ECG Time-Series Signals]    ──┤
  [Clinical Notes Text]        ──┘
```

#### Modality Feature Projections
$$\mathbf{x}_{\text{tab}} \in \mathbb{R}^{d_{\text{tab}}}, \quad \mathbf{x}_{\text{img}} = \text{CNN}(\text{CXR}) \in \mathbb{R}^{d_{\text{img}}}, \quad \mathbf{x}_{\text{ecg}} = \text{ResNet1D}(\text{ECG}) \in \mathbb{R}^{d_{\text{ecg}}}, \quad \mathbf{x}_{\text{txt}} = \text{BioBERT}(\text{Notes}) \in \mathbb{R}^{d_{\text{txt}}}$$

---

### 2. Fusion Architectures: Early vs. Intermediate vs. Late Fusion

#### A. Early Fusion (Feature-Level Concatenation)
Concatenates raw feature vectors into a single unified input vector prior to model training:

$$\mathbf{x}_{\text{early}} = [\mathbf{x}_{\text{tab}} \parallel \mathbf{x}_{\text{img}} \parallel \mathbf{x}_{\text{ecg}} \parallel \mathbf{x}_{\text{txt}}] \in \mathbb{R}^{d_{\text{total}}}$$

$$\hat{y} = f_\theta(\mathbf{x}_{\text{early}})$$

#### B. Intermediate Fusion (Joint Layer Projection)
Projects each modality through a dedicated encoder into a shared latent space where cross-attention or tensor fusion layers interact:

$$\mathbf{z}_m = g_m(\mathbf{x}_m) \quad \text{for } m \in \{\text{tab}, \text{img}, \text{ecg}, \text{txt}\}$$

$$\mathbf{z}_{\text{joint}} = \text{CrossAttention}(\mathbf{z}_{\text{tab}}, \mathbf{z}_{\text{img}}, \mathbf{z}_{\text{ecg}}, \mathbf{z}_{\text{txt}})$$

#### C. Late Fusion (Decision-Level Ensemble Averaging)
Trains independent unimodal classifiers $f_m(\mathbf{x}_m)$ and combines final output class probabilities:

$$\hat{y}_{\text{late}} = \sum_{m=1}^M w_m \cdot \sigma\left( f_m(\mathbf{x}_m) \right) \quad \text{where } \sum_{m=1}^M w_m = 1.0$$

---

## 🤖 Lecture 3: Large Multimodal Models & Adapter Layers

### 1. Adapting LLMs for Vision & Multimodal Inputs

Rather than training a multimodal model from scratch, **Large Multimodal Models (LMMs)** (e.g., LLaVA, Flamingo) connect a frozen pre-trained Vision Encoder (CLIP ViT) to a frozen LLM (Vicuna, LLaMA) using parameter-efficient adapters.

```
  [Input Image] ──► Vision Encoder (CLIP ViT) ──► Linear Projection Adapter (W) ──┐
                                                                                  ├──► Frozen LLM ──► Text Answer
  [Input Text Prompt] ──────────────────────────► Word Embedding Matrix ──────────┘
```

---

### 2. Parameter-Efficient Adapter Mechanics

An **Adapter Layer** injects a bottleneck projection network alongside frozen transformer layers, learning multimodal projections with $< 1\%$ parameter overhead:

$$\mathbf{h}_{\text{adapter}} = \mathbf{x} + f\left( \mathbf{x} \mathbf{W}_{\text{down}} \right) \mathbf{W}_{\text{up}}$$

* $\mathbf{W}_{\text{down}} \in \mathbb{R}^{d \times r}$: Down-projection matrix ($r \ll d$).
* $f(\cdot)$: Non-linear activation function (GELU / ReLU).
* $\mathbf{W}_{\text{up}} \in \mathbb{R}^{r \times d}$: Up-projection matrix.

---

## 🌪️ Lecture 4: Case Study – Multimodal Hurricane Forecasting

Climate science requires fusing spatio-temporal satellite arrays, physical sensor networks, and radar feeds:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                      Hurricane Multimodal Data Streams                           │
├───────────────────┬──────────────────────────────────────────────────────────────┤
│ Satellite IR      │ 2D Thermal spatial imagery tracking eye wall structure.       │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ Doppler Radar     │ 3D Wind velocity and precipitation density.                  │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ Tabular Metrics   │ Sea-surface temperature (SST), central pressure, latitude.   │
└───────────────────┴──────────────────────────────────────────────────────────────┘
```

#### Multimodal Forecasting Objective
$$\hat{\mathbf{y}}_{\text{track}}, \hat{y}_{\text{intensity}} = F_\theta\left( \mathbf{I}_{\text{sat}}, \mathbf{R}_{\text{radar}}, \mathbf{X}_{\text{tabular}} \right)$$

Fusing satellite IR imagery with tabular atmospheric dynamics reduces 24-hour hurricane intensity prediction error (RMSE) by 28% compared to single-source numerical weather prediction models.

---

## 🎯 Lecture 5: Multimodal Multitask Learning ($M^3H$)

### 1. Multitask Loss Formulation
In clinical and real-world environments, models predict multiple target outputs simultaneously across $K$ heterogeneous tasks (e.g., mortality, length of stay, pathology tags):

$$\mathcal{L}_{\text{total}}(\theta) = \sum_{k=1}^K w_k \cdot \mathcal{L}_k\left( y_k, \hat{y}_k(\theta) \right)$$

* adaptive loss weighting $w_k$ balances loss magnitudes across binary classification and continuous regression tasks.
