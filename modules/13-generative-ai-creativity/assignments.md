# Assignment Solutions – Generative AI, the Future of Work, and Human Creativity

---

## 📝 Assignment 1: Generative AI with Diffusion Models

### 📌 Part 1 — Text-to-Image Generation with Stable Diffusion

#### Problem Description
Initialize the `runwayml/stable-diffusion-v1-5` pipeline using HuggingFace `diffusers` and generate an image from a descriptive text prompt.

#### Python Code Implementation
```python
import torch
from diffusers import StableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

if torch.cuda.is_available():
    pipe = pipe.to("cuda")

prompt = "A majestic lion standing on a cliff during sunrise, hyperrealistic, 8k"
image = pipe(prompt, guidance_scale=7.5, num_inference_steps=30).images[0]
image.save("majestic_lion.png")
print("Image generated and saved successfully!")
```

---

### 📌 Part 2 — CLIP Embeddings & Similarity Calculation

#### Problem Description
Load the OpenAI CLIP model (`openai/clip-vit-base-patch32`). Extract joint text and image embeddings, calculate cosine similarity scores, and compute Softmax probability distributions.

#### Python Code Implementation
```python
import torch
import torch.nn.functional as F
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# Load CLIP model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

raw_image = Image.open("majestic_lion.png").convert("RGB")
candidate_texts = [
    "A photo of a lion on a cliff",
    "A photo of a cat sleeping on a sofa",
    "A futuristic city with cars",
    "A watercolor painting of a mountain"
]

# Process inputs through CLIP processor
inputs = processor(
    text=candidate_texts, 
    images=raw_image, 
    return_tensors="pt", 
    padding=True
)

outputs = clip_model(**inputs)
logits_per_image = outputs.logits_per_image  # Image-to-text similarity logits
probs = logits_per_image.softmax(dim=1)      # Softmax probabilities

print("CLIP Text Match Probabilities:\n")
for text, prob in zip(candidate_texts, probs[0]):
    print(f"  Text: '{text:<40}' -> Prob: {prob.item()*100:.2f}%")
```

#### Analytical Formula
$$\text{Logit}_i = 100 \cdot \frac{\mathbf{v}_{\text{image}} \cdot \mathbf{v}_{\text{text}, i}}{\|\mathbf{v}_{\text{image}}\|_2 \|\mathbf{v}_{\text{text}, i}\|_2}$$

$$P(\text{Text}_i \mid \text{Image}) = \frac{\exp(\text{Logit}_i)}{\sum_j \exp(\text{Logit}_j)}$$

---

### 📌 Part 3 — Prompt Style Comparison

#### Problem Description
Evaluate how adding explicit style modifiers (e.g., photorealistic, digital art, watercolor, cyberpunk) affects the visual rendering and aesthetic output of diffusion models.

#### Python Code Implementation
```python
base_concept = "a lone traveler walking through a forest"
styles = [
    ("Photorealistic", f"{base_concept}, photorealistic, 8k resolution, national geographic style"),
    ("Digital Art", f"{base_concept}, digital art, trending on artstation, vibrant colors"),
    ("Watercolor", f"{base_concept}, soft watercolor painting, artistic brush strokes"),
    ("Cyberpunk", f"{base_concept}, cyberpunk style, neon lighting, futuristic atmosphere")
]

generated_images = {}
for style_name, full_prompt in styles:
    print(f"Generating style: {style_name}...")
    img = pipe(full_prompt, guidance_scale=7.5, num_inference_steps=25).images[0]
    img.save(f"style_{style_name.lower().replace(' ', '_')}.png")
    generated_images[style_name] = img
```

---

### 📌 Part 4 — Modifying Inference Steps & Guidance Scale Parameters

#### Problem Description
Systematically explore parameter variations in `num_inference_steps` (10 vs 30 vs 50) and `guidance_scale` (1.0 vs 7.5 vs 15.0) to observe latency and image fidelity trade-offs.

```python
prompt = "A mystical forest with glowing trees, digital art"

# 1. Varying Inference Steps (Latency vs Detail)
step_options = [10, 30, 50]
for steps in step_options:
    img = pipe(prompt, guidance_scale=7.5, num_inference_steps=steps).images[0]
    img.save(f"steps_{steps}.png")
    print(f"Rendered {steps} inference steps.")

# 2. Varying Guidance Scale (CFG: Adherence vs Saturation)
cfg_options = [1.0, 7.5, 15.0]
for cfg in cfg_options:
    img = pipe(prompt, guidance_scale=cfg, num_inference_steps=30).images[0]
    img.save(f"cfg_{cfg}.png")
    print(f"Rendered guidance scale CFG = {cfg}.")
```

#### Parameter Trade-Off Summary
* **Inference Steps ($N_{\text{steps}}$)**: 10 steps renders quickly but exhibits noise artifacts; 30–50 steps provides optimal fine-detail convergence with diminishing visual returns past 50.
* **Guidance Scale (CFG)**:
  * **CFG = 1.0**: Unconditioned generation; ignores prompt guidance, producing generic image compositions.
  * **CFG = 7.5**: Optimal balance between prompt fidelity and natural visual aesthetics.
  * **CFG = 15.0**: Over-conditioned generation; strict prompt adherence resulting in over-saturated colors and unnatural contrast artifacts.
