# Assignment Solutions – AI and Entrepreneurship

---

## 📝 Assignment 1: AI Venture Strategy, Unit Economics & GTM Solutions

### 📌 Problem 1 — Stevenson's Entrepreneurship Definition & Venture Lifecycle

#### Question Formulation
An AI startup founder is pitching investors, claiming that because their product uses open-source foundation model APIs, they require zero capital and face no resource constraints. How does Howard Stevenson's definition of entrepreneurship evaluate this statement?

#### Verified Solution & Explanation
* **Correct Answer**: **Entrepreneurship is the pursuit of opportunity without regard to resources currently controlled. Using open APIs reduces initial technical barriers, but execution still requires controlling key non-compute resources such as proprietary domain data, customer trust, and distribution channels.**
* **Explanation**: Stevenson's paradigm emphasizes opportunity pursuit beyond current resources. Access to open APIs lowers seed-stage friction, but sustainable ventures must eventually control proprietary data assets and workflow integration to survive scaling stages.

---

### 📌 Problem 2 — Human-AI Team Architecture: Centaur vs. Cyborg

#### Question Formulation
A medical imaging startup deploys an AI diagnostic system. In Workflow A, radiologists review AI anomaly flags after the scan is complete. In Workflow B, an AI assistant continuously highlights pixels in real-time as the radiologist scans the image. Classify these two team topologies.

#### Verified Solution & Explanation
* **Correct Answer**: **Workflow A is a Centaur topology (modular handoff); Workflow B is a Cyborg topology (continuous real-time co-creation).**
* **Explanation**: Centaur teams operate via explicit division of labor and task handoffs. Cyborg teams operate through continuous, real-time human-machine interaction.

---

### 📌 Problem 3 — SaaS Unit Economics & Financial Health Evaluation

#### Question Formulation
An AI SaaS venture reports the following metrics:
* Monthly ARPU = $\$400$
* Gross Margin = $80\%$
* Monthly Churn Rate = $2.5\%$
* CAC = $\$4,800$

Evaluate the venture's $LTV$, $LTV/CAC$ ratio, and CAC Payback Period. Does it satisfy standard financial health benchmarks?

#### Verified Solution & Explanation
* **Calculations**:
  - $LTV = \frac{\text{ARPU} \times M}{\sigma} = \frac{400 \times 0.80}{0.025} = \frac{320}{0.025} = \mathbf{\$12,800.00}$
  - $LTV / CAC = \frac{12,800}{4,800} = \mathbf{2.67x}$
  - Payback Period = $\frac{CAC}{\text{ARPU} \times M} = \frac{4,800}{320} = \mathbf{15.0 \text{ months}}$

```python
arpu = 400.0
gross_margin = 0.80
monthly_churn = 0.025
cac = 4800.0

ltv = (arpu * gross_margin) / monthly_churn
ltv_cac_ratio = ltv / cac
payback_months = cac / (arpu * gross_margin)

print(f"LTV: ${ltv:,.2f}")
print(f"LTV/CAC Ratio: {ltv_cac_ratio:.2f}x (Passes 3.0x Benchmark? {ltv_cac_ratio >= 3.0})")
print(f"Payback Period: {payback_months:.1f} months (Passes 12m Benchmark? {payback_months <= 12.0})")
```

* **Conclusion**: **The venture fails both standard benchmarks ($LTV/CAC = 2.67x < 3.0x$ and Payback = $15.0\text{ months} > 12.0\text{ months}$). To achieve health, the venture must reduce CAC or lower monthly churn.**

---

### 📌 Problem 4 — The AI & Entrepreneurship Paradox & Moat Defensibility

#### Question Formulation
Why does a startup whose sole feature is an un-tuned wrapper around a commercial LLM API face severe long-term valuation risks?

#### Verified Solution & Explanation
* **Correct Answer**: **Due to the AI Paradox: raw model capabilities rapidly commoditize as foundation model providers update their base models, while competitors can easily replicate simple API wrappers. Long-term value requires proprietary data flywheel loops and deep workflow integration.**
