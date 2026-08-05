# Recitation Notes – Generative AI, the Future of Work, and Human Creativity

---

## 🔬 Recitation 1: Generative AI in Python and Web Applications

### 1. Three Deployment Paradigms for Generative AI

Generative models can be accessed via three primary deployment modalities:

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                                Deployment Paradigm Comparison                            │
├──────────────────────┬────────────────────────────┬──────────────────────────────────────┤
│ Metric               │ Local Open-Source Models   │ Cloud API Services                   │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Privacy & Security   │ 100% Private / On-Premise  │ Data transmitted to vendor cloud     │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Hardware Needed      │ Dedicated GPU VRAM         │ Standard CPU / HTTP Client           │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Operating Cost       │ Fixed Hardware Capital     │ Variable Pay-per-Token               │
├──────────────────────┼────────────────────────────┼──────────────────────────────────────┤
│ Customizability      │ Full Weight Access & LoRA  │ Restricted to API Hyperparameters    │
└──────────────────────┴────────────────────────────┴──────────────────────────────────────┘
```

---

## 🖼️ Recitation 2: Text-to-Image Generation (Stable Diffusion & StabilityAI)

### 1. Local Diffusers Pipeline Execution

```python
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Load model pipeline from Hugging Face
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

if torch.cuda.is_available():
    pipe = pipe.to("cuda")

prompt = "A futuristic city with flying vehicles at sunset, photorealistic, 8k"
image = pipe(prompt, guidance_scale=7.5, num_inference_steps=30).images[0]
image.save("futuristic_city.png")
```

---

### 2. StabilityAI API Client Integration

```python
import os
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from stability_sdk import client

# Set API key
os.environ['STABILITY_KEY'] = 'your-api-key-here'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0",
)

answers = stability_api.generate(
    prompt="A serene mountain lake surrounded by pine trees, digital art",
    seed=42,
    steps=30,
    cfg_scale=7.0,
    width=1024,
    height=1024,
    samples=1,
)

for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FINISH_SUCCESS:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save("mountain_lake.png")
```

---

## 👁️ Recitation 3: Image-to-Text Captioning (BLIP Model)

Image captioning translates visual spatial features into descriptive natural language text using vision-language models like BLIP (Bootstrapping Language-Image Pre-training).

```python
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load processor and BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

raw_image = Image.open("futuristic_city.png").convert("RGB")

# Conditional vs Unconditional Captioning
inputs = processor(raw_image, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=50)
caption = processor.decode(out[0], skip_special_tokens=True)

print("Generated Image Caption:", caption)
```

---

## 📝 Recitation 4: Text-to-Text Generation & Summarization

### 1. GPT-2 Text Generation Pipeline

```python
from transformers import pipeline

gpt2_generator = pipeline("text-generation", model="gpt2")
text_prompt = "The mission of the MIT Sloan School of Management is"

output = gpt2_generator(text_prompt, max_length=50, num_return_sequences=1)
print("Generated Text:\n", output[0]['generated_text'])
```

---

### 2. Pegasus Abstractive Summarization Pipeline

```python
# Summarization using Pegasus model
pegasus_summarizer = pipeline("summarization", model="google/pegasus-xsum")

article = """
Scientists have developed a new artificial intelligence system that can analyze satellite 
imagery to detect environmental deforestation in real time. The system leverages deep 
learning convolutional neural networks trained on multi-spectral satellite imagery to identify 
illegal logging activity with 95% accuracy.
"""

summary = pegasus_summarizer(article, max_length=40, min_length=15)
print("Abstractive Summary:\n", summary[0]['summary_text'])
```

---

## 📚 Recitation 5: Glossary of Key Terms

* **Diffusion Models**: Generative architectures that model data distributions by learning to reverse a gradual Gaussian noise addition process.
* **BLIP (Bootstrapping Language-Image Pre-training)**: A vision-language model trained for multi-modal tasks including image captioning and visual question answering.
* **CLIP (Contrastive Language-Image Pre-training)**: A multimodal neural network trained to align text and image embeddings in a shared latent vector space.
* **Guidance Scale (CFG / Classifier-Free Guidance)**: Parameter controlling how strictly an image generation model adheres to the input text prompt vs. exploring unconditioned image features.
* **Inference Steps**: The number of iterative denoising steps performed during reverse diffusion sampling (balancing output quality vs. computational latency).
