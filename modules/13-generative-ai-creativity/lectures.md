# Lecture Notes – Generative AI, the Future of Work, and Human Creativity

---

## 🏗️ Lecture 1: AI and the Future of Work

### 1. Discriminative AI vs. Generative AI

Traditional AI models were **discriminative**, learning mapping boundaries $P(Y \mid X)$ to classify inputs or predict continuous scalar targets. 

**Generative AI** models joint or conditional distributions over complex unstructured data $P(X)$ or $P(X \mid Y)$, generating completely novel artifacts across text, images, audio, video, and code.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AI Modeling Paradigms                                │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Discriminative Models         │ Learns decision boundaries P(Y | X)              │
│ P(Y | X)                      │ (Logistic Regression, ResNet, XGBoost)           │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ Generative Models             │ Models sample distributions P(X) or P(X | Text)  │
│ P(X) or P(X | Y)              │ (Diffusion Models, Transformers, VAEs, GANs)     │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

### 2. Task Augmentation vs. Automation & Economic Potential

Rather than replacing entire occupations, Generative AI targets specific **workplace tasks**:
* **Automation**: Full replacement of repetitive, structured tasks without human intervention.
* **Augmentation**: Elevating human capability by handling draft creation, ideation, and retrieval while humans provide direction, domain expertise, and final verification.

#### Economic Productivity Function
Let total worker production $Y$ be a function of human capital $H$, physical capital $K$, and AI task augmentation factor $A(G)$:

$$Y = A(G) \cdot K^\alpha H^{1-\alpha}$$

Studies from MIT and McKinsey indicate that AI task augmentation produces a 15–40% increase in task completion speed while increasing work quality across technical writing, customer support, and software synthesis.

---

### 3. Deploying Generative AI Models

Organizations choose between three deployment paradigms based on latency, data privacy, and hardware budget:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            AI Model Deployment Trade-Offs                        │
├───────────────────┬─────────────────────────────┬────────────────────────────────┤
│ Deployment Mode   │ Key Advantages              │ Primary Constraints            │
├───────────────────┼─────────────────────────────┼────────────────────────────────┤
│ Local Open-Source │ 100% Data Privacy, No APIs  │ Requires Local GPU Memory      │
├───────────────────┼─────────────────────────────┼────────────────────────────────┤
│ Cloud API         │ Zero Local Hardware Setup   │ Recurring API Token Costs      │
├───────────────────┼─────────────────────────────┼────────────────────────────────┤
│ Web Application   │ Turnkey Consumer UX         │ Closed Black-Box Control       │
└───────────────────┴─────────────────────────────┴────────────────────────────────┘
```

---

## 🎨 Lecture 2: Gen AI and Creative Problem Solving

### 1. Divergent vs. Convergent Thinking

Creative problem solving requires balancing two complementary cognitive modes:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                          Creative Cognitive Frameworks                           │
├───────────────────┬──────────────────────────────────────────────────────────────┤
│ Divergent Mode    │ Broad option generation, exploring wide solution spaces.      │
│ (AI Augmented)    │ (Generates 50 diverse product concepts in seconds).          │
├───────────────────┼──────────────────────────────────────────────────────────────┤
│ Convergent Mode   │ Critical evaluation, filtering for feasibility and value.    │
│ (Human Directed)  │ (Selects, refines, and tests top 2 feasible prototypes).     │
└───────────────────┴──────────────────────────────────────────────────────────────┘
```

---

### 2. Three Types of Creativity (Boden's Framework)

1. **Combinatorial Creativity**: Unifying unfamiliar combinations of familiar ideas (e.g., combining "cyberpunk aesthetic" with "Renaissance oil painting").
2. **Exploratory Creativity**: Investigating the boundaries of an existing conceptual style space (e.g., exploring prompt variations within watercolor landscape rendering).
3. **Transformational Creativity**: Altering the fundamental rules or boundaries of the conceptual space itself (e.g., inventing text-to-image latent diffusion).

---

### 3. Human-AI Collaboration Models

* **Centaur Model**: Clear task division where human and AI handle distinct sub-tasks sequentially (e.g., Human writes outline $\rightarrow$ AI generates code $\rightarrow$ Human debugs).
* **Cyborg Model**: Deeply interwoven, continuous real-time collaboration where human and AI inputs alternate line-by-line or phrase-by-phrase.

---

## ⚖️ Lecture 3: Gen AI & Human-AI Balance in Decision Making

### 1. Mitigating Cognitive Biases in Screening

Human decision-makers suffer from cognitive fatigue, halo effects, and recency bias when screening large proposal volumes.

AI-assisted screening models provide consistent, objective evaluation by scoring proposals against explicit multi-criteria rubrics $R = \{r_1, r_2, \dots, r_m\}$.

---

### 2. Case Study: MIT Solve Innovation Screening Pipeline

```
  [1,000+ Proposals] ──► AI Rubric Scoring ──► Pairwise Comparison ──► Filtered Top 10% ──► Human Expert Panel
                                                                                                  │
                                                                                                  ▼
                                                                                           [Final Winners]
```

#### Methodology
1. **Rubric Alignment**: AI evaluates each proposal across structured criteria (Novelty, Feasibility, Social Impact, Financial Sustainability) on a 1–5 scale.
2. **Pairwise Comparison**: AI compares candidate proposals head-to-head ($P_A$ vs. $P_B$) to eliminate scoring calibration drift.
3. **Human-in-the-Loop Validation**: Human expert panels review AI-screened shortlists, ensuring contextual nuance and ethical integrity.

---

## 🖼️ Lecture 4: Diffusion Models for Text-to-Image Generation

### 1. Generative Model Comparison

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            Generative Vision Architectures                       │
├───────────────────┬─────────────────────────────┬────────────────────────────────┤
│ Architecture      │ Mechanism                   │ Trade-offs                     │
├───────────────────┼─────────────────────────────┼────────────────────────────────┤
│ GANs              │ Adversarial Generator/Disc  │ Fast, but unstable training    │
├───────────────────┼─────────────────────────────┼────────────────────────────────┤
│ VAEs              │ Encoder-Decoder Latent      │ Stable, but blurrier outputs   │
├───────────────────┼─────────────────────────────┼────────────────────────────────┤
│ Diffusion Models  │ Iterative Denoising         │ High quality, stable training  │
└───────────────────┴─────────────────────────────┴────────────────────────────────┘
```

---

### 2. Forward Diffusion Process (Noise Addition)

The **Forward Process** progressively corrupts a clean data sample $x_0 \sim q(x)$ by adding Gaussian noise over $T$ timesteps according to a variance schedule $\beta_1, \beta_2, \dots, \beta_T$:

$$q(x_t \mid x_{t-1}) = \mathcal{N}\left(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t \mathbf{I}\right)$$

#### Closed-Form Forward Sampling
Let $\alpha_t = 1 - \beta_t$ and $\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$. We can sample $x_t$ directly at any arbitrary timestep $t$ without iterating:

$$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon \quad \text{where } \epsilon \sim \mathcal{N}(0, \mathbf{I})$$

* At $t = 0$, $x_0$ is the clean image.
* At $t = T$, $x_T$ becomes pure, unconditioned Gaussian noise $\mathcal{N}(0, \mathbf{I})$.

---

### 3. Reverse Diffusion Process & UNet Loss

The **Reverse Process** trains a neural network $\epsilon_\theta(x_t, t)$ (typically a UNet architecture with self-attention) to predict and subtract the added noise $\epsilon$:

$$p_\theta(x_{t-1} \mid x_t) = \mathcal{N}\left(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t)\right)$$

#### Objective Function (Simplified Denoising Loss)
$$\mathcal{L}_{\text{simple}}(\theta) = \mathbb{E}_{t, x_0, \epsilon} \left[ \left\| \epsilon - \epsilon_\theta(x_t, t) \right\|^2 \right]$$

---

### 4. Text Conditioning & Cross-Attention

To steer image generation via text prompts, text conditions $y$ are encoded via a text transformer (e.g., CLIP Text Encoder) into embeddings $\mathbf{c} = \tau_\theta(y)$.

Cross-attention layers inside the UNet inject text embeddings $\mathbf{c}$ into intermediate spatial feature maps $\mathbf{F}$:

$$\mathbf{Q} = \mathbf{F} \mathbf{W}_Q, \quad \mathbf{K} = \mathbf{c} \mathbf{W}_K, \quad \mathbf{V} = \mathbf{c} \mathbf{W}_V$$

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q} \mathbf{K}^T}{\sqrt{d_k}} \right) \mathbf{V}$$

---

### 5. CLIP (Contrastive Language-Image Pretraining)

CLIP creates a shared multimodal embedding space where matching text-image pairs $(\mathbf{t}_i, \mathbf{i}_i)$ have high cosine similarity while mismatched pairs have low similarity.

```
                  Image Encoder ──► Image Vectors  I_1, I_2, ..., I_N
                                                           │
  Text ──► Text Encoder ──► Text Vectors   T_1, T_2, ..., T_N
                                                           │
                                                           ▼
                                               [Cosine Similarity Matrix]
```

#### Contrastive Loss Function
For a batch of $N$ (text, image) pairs, CLIP maximizes diagonal cosine similarities while minimizing off-diagonal similarities:

$$\mathcal{L}_{\text{CLIP}} = -\frac{1}{2N} \sum_{i=1}^N \left( \log \frac{\exp(\text{sim}(\mathbf{t}_i, \mathbf{i}_i) / \tau)}{\sum_j \exp(\text{sim}(\mathbf{t}_i, \mathbf{i}_j) / \tau)} + \log \frac{\exp(\text{sim}(\mathbf{t}_i, \mathbf{i}_i) / \tau)}{\sum_j \exp(\text{sim}(\mathbf{t}_j, \mathbf{i}_i) / \tau)} \right)$$
