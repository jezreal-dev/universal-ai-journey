Explainability and Fairness  
\`\`\`  
Skip to main content  
Module Overview  
Welcome to Explainability and Fairness\!

In this module, you’ll learn how transparency and fairness are essential for building trustworthy AI systems, especially in high-stakes settings such as healthcare, lending, hiring, and criminal justice.

You’ll begin with the foundations of explainable AI. You’ll explore why trust in AI depends on understanding how models use data, how they behave overall, and why they make specific predictions. You’ll examine global, local, and counterfactual explanations, and learn how model choice influences interpretability—whether through inherently transparent models like decision trees or post-hoc explanation tools such as LIME and surrogate models.

Next, you’ll study fairness-aware machine learning, focusing on how bias can emerge from datasets that reflect historical human decisions. You’ll see how fairness metrics formalize disparities across demographic groups and how optimization techniques can mitigate bias while preserving predictive performance.

Finally, you’ll analyze the trade-off between fairness and accuracy, sometimes referred to as the “price of diversity,” and learn how interpretable models can explain fairness adjustments in real-world systems.

By the end of this module, you’ll understand how explainability and fairness work together to make AI systems more transparent, accountable, and aligned with societal values.

Learning Goals  
By the end of this module, learners will be able to:

Explain why transparency is critical for trustworthy AI systems.  
Distinguish between global, local, and counterfactual explanations.  
Compare interpretable models with post-hoc explanation methods.  
Describe how systemic bias emerges in datasets derived from human decisions.  
Define fairness metrics such as α-bias and ε-demographic parity.  
Explain how optimization techniques can mitigate bias while maintaining model performance.  
Analyze the trade-offs between fairness constraints and predictive accuracy.  
\`\`\`

Lecture 1: Explainable AI  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 1: Explainable AI, taught by Professor Georgios Stamou, Professor at the School of Electrical and Computer Engineering at the National Technical University of Athens, Greece, and Visiting Professor at MIT.

What do a denied loan, a flagged chest X-ray, and a “tiger” cat photo have in common? They all force us to ask why the AI decided that—and whether we can trust it.

This lecture surveys the essentials of Explainable AI: how data choices (sources, labeling, size/splits, bias) shape trust; the three lenses for explanations—global (feature importance, surrogate models), local (case-level attributions like LIME), and counterfactuals (“what would need to change?”); the role of interpretable models (e.g., decision trees), how they provide rules and feature importance—and their limits; and why post-hoc stories can mislead, especially when bias is present. We also map explanations to audience needs (users vs. applicants vs. regulators) and pipeline transparency.

By the end, you’ll be able to describe and distinguish these methods, explain their trade-offs, and choose suitable explanation types for different stakeholders—grounded in the examples covered in the lecture.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain why explainability matters for trust and list key risks (privacy, safety, discrimination).  
Identify dataset factors and output signals (sources, labeling, size/splits, bias; confidence/errors) that affect reliability and fairness.  
Distinguish global, local (e.g., LIME), and counterfactual explanations and note when each applies.  
Describe interpretable models—especially decision trees—extract rules/feature importance, and note common limits.  
Summarize post-hoc techniques (surrogates, local attributions, counterfactuals) and typical pitfalls, including unfaithful narratives and bias.  
Align strong explanation types to stakeholders (expert users, affected individuals, regulators) and outline pipeline transparency needs.  
\`\`\`

L1.1 Why Should AI Be Explainable  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Most people believe that artificial intelligence  
is powerful and risky at the same time.  
So ensuring AI trust and, by extension, AI transparency  
is key.  
From model training to decision making,  
it is important to provide explanations  
of how the AI system works.  
Explaining AI systems can be challenging.  
The right form of explanations depend on the context.  
Explanations should be intuitive in the sense  
that humans should be able to understand it.  
At the same time, explanations should be accurate in the sense  
that they should ensure that AI systems  
operation is transparent.  
By addressing these challenges, we  
can move towards responsible, interpretable,  
and human-centered AI.  
In this lecture, we will discuss the need for explainable AI,  
its main challenges, and the technologies that support it.  
Starting with the usefulness of AI and its main risks,  
we will explore the challenges of providing explanations  
that are both intuitive and accurate.  
Next, we will outline the taxonomy  
of methods for explainable AI, providing examples  
and highlighting the key concepts  
behind widely used approaches.  
AI is changing the way we work every day.  
We use AI to automate repetitive, sometimes  
tedious tasks in various domains or to assist humans  
in complex decision making.  
In health care, AI is becoming increasingly prominent.  
For example, AI-driven tools assist doctors  
in detecting diseases with greater precision  
or speed up drug discovery, reducing the time and cost  
of developing new medications.  
In manufacturing, AI is now a game changer.  
AI robots dramatically improve repetitive tasks like assembly,  
disassembly, and packaging.  
AI-automated quality control systems  
can quickly and efficiently detect defects,  
improving product quality.  
In education, AI is creating new learning experiences,  
making education more accessible and  
adaptable to individual needs.  
AI-based technological innovations like gamification,  
virtual reality, chatbots, generative AI, et cetera,  
equip educators with powerful tools.  
AI also plays a crucial role in culture,  
enhancing preservation, accessibility, and creativity.  
Users engage with cultural content  
in more immersive and interactive ways  
through AI technologies.  
Creators are empowered by AI tools, including generative AI.  
AI is also highly anticipated to play an important role  
in sustainability and climate change,  
helping scientists analyze vast amounts of data  
to forecast climate conditions, track ecological changes,  
deforestation, wildlife population shifts, and pollution  
levels.  
Besides its usefulness, AI also comes  
with risks that can cause both material and immaterial harm  
to people.  
For instance, failures in autonomous vehicles  
can lead to accidents.  
Misdiagnosing medical conditions may result in adverse health  
outcomes for patients.  
Breakdowns in industrial automation  
can lead to workplace accidents.  
Failures in algorithmic trading or mistakes in logistics  
can cause financial losses.  
AI-generated deepfakes can impersonate individuals carrying  
out unauthorized transactions.  
AI can also cause immaterial harm.  
Notably, AI poses significant risks  
to personal data protection and privacy.  
AI-powered behavior tracking systems  
can be exploited for mass surveillance  
without control, violating individuals' privacy rights.  
AI's ability to interconnect data from across the web  
can potentially lead to de-anonymization of individuals  
and the exposure of sensitive personal information.  
There are also major concerns related  
to discrimination and fairness.  
Bias in training data can lead to discrimination  
against certain genders, ethnicities, or age groups.  
AI-driven medical and financial services  
may have reduced accuracy for specific demographic groups,  
resulting in unequal access to care or financial opportunities.  
These risks and potential implications associated with AI  
contribute to a lack of trust in its use and recommendations.  
On top of the existing risks, speculative ideas  
such as human-like AI robots with  
artificial superintelligence raise concerns  
that machines could one day surpass humans.  
As a result, end users, especially experts  
such as medical practitioners, often  
hesitate to trust AI recommendations even  
in scenarios where they achieve greater performance  
than human decision makers.  
This phenomenon, known as algorithmic aversion,  
significantly undermines human AI collaboration.  
The only way to enhance AI excellence, usefulness,  
and trust is to promote AI technologies that  
ensure transparency, fairness, and accountability.  
To this end, we should train models  
on well-balanced and diverse data sets  
to minimize biases and evaluate models  
for potential gender, racial, or socioeconomic biases.  
Moreover, AI systems should offer clear insights  
into how they get to their conclusions.  
Ideally, we should be able to understand the reasons  
behind model predictions so that we are able to validate them.  
The compliance to regulatory frameworks for AI  
plays an important role, providing guarantees.  
To reduce potential risks and build trust,  
organizations utilizing AI technologies  
should implement guidelines, standards,  
or regulatory frameworks.  
Technical services that validate compliance  
with these regulations should be developed.  
Based on these technical services,  
high-risk AI systems used in practice,  
like AI-assisted medical diagnosis systems,  
should provide guarantees for compliance  
with the AI regulatory framework.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.2 How AI Systems Explain Their Decisions  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Within this context, let's  
explore how AI explanations should ideally  
be presented to the user to ensure transparency.  
We begin with an example from the medical field,  
an AI-assisted diagnosis system.  
During the learning phase, the AI  
is trained on the data set that includes  
multimodal data such as patient records in tabular format,  
along with medical data like MRIs, EEGs,  
and other diagnostic images.  
In the inference phase, the system  
assists doctors in disease diagnosis  
by generating predictions for a specific patient.  
Understanding the data used to train AI systems  
is crucial for assessing their reliability and fairness.  
Factors like data source, labeling accuracy, data set  
size, and potential biases must be considered  
to ensure transparency and fairness  
in AI-assisted diagnosis systems.  
Moreover, understanding the output  
of an AI-assisted diagnosis system  
is necessary for its integration into  
real-world medical workflows.  
The system's output, which may include predicted diagnosis  
or risk assessments, usually offers insights  
like a confidence score or uncertainty measures.  
This could be something like 85% likelihood of a tumor.  
In evaluating the AI system suitability  
for using clinical practice, key considerations  
include its accuracy, precision, and reliability.  
So we should examine the frequency  
of errors, such as false positives and negatives,  
as well as when the system performs well or poorly.  
To understand how the AI system makes predictions,  
we need to examine the key factors influencing  
its decisions.  
What features does the system Consider Does it rely on patient  
demographics, lab results, or imaging data?  
How specific features such as age or gender impact  
predictions?  
How are different features weighted,  
and which ones are more influential?  
Finally, what kind of algorithm is used,  
and how were its parameters set?  
During the inference phase, it is  
important to understand why the AI  
system made a specific prediction  
for a specific instance.  
To do this, we need to examine which features  
influenced its decision.  
What aspects of this instance determine the outcome?  
Likewise, why was this instance not classified differently?  
If two instances receive the same prediction,  
what shared characteristics led to that result?  
If two instances receive different predictions,  
what key differences led to this divergence?  
Also, we need to understand how an instance can receive  
a different prediction, what changes would alter  
the outcome of the AI system.  
What is the smallest feature adjustment  
needed to shift the prediction?  
How should the specific feature change  
to achieve a different result?  
What happens if a key feature changes?  
How does it respond to a completely different instance?  
Let's turn, now, our attention to the type of explanations.  
The first crucial factor to understand  
is the data set the AI system was trained on.  
First, we need to understand the source of the data.  
Is it from hospitals?  
From research institutions?  
From publicly available medical data sets?  
From private health providers?  
The source is important for assessing its credibility  
and scope.  
For example, a data source explanation  
could inform for the type of data--  
in our example, chest X-ray images--  
its sources-- in our example, radiology departments  
of hospitals, both open data sets and hospital databases,  
all anonymized-- and potential processing of the data--  
in our example, human curation.  
Second, it's essential to understand  
the data labeling process to assess the labeling credibility.  
For example, are experts, radiologists, pathologists,  
or other medical professionals involved  
in the labeling process?  
How many of them?  
And with which labeling methodology?  
Is there any other automated labeling process, for example,  
associating manual annotations found in patient records  
or involving automated labeling systems?  
This information is crucial, as the accuracy of the ground truth  
directly influences the reliability of the model.  
An example of data labeling explanation could include who  
labeled the image-- here, board-certified radiologists--  
the diagnostic labels-- here, pneumonia, et cetera--  
and how consensus is reached, particularly  
in challenging cases--  
here, multiple experts.  
Another issue to consider is the size  
of the data set, for example, the number of patient records,  
MRIs, EEGs, or other medical samples used for training.  
A small or imbalanced data set can lead to biased predictions,  
so understanding these gaps helps us  
identify potential limitations.  
An example of data size explanation  
could clarify, what is the size of the data set?  
Here, 1.2 million medical images.  
Its internal structure-- here, 500,000 CT scans, et cetera.  
And how it is split in the training process  
to ensure model generalization-- here, 80% for training,  
10% for validation, and 10% for testing.  
Of course, although it is highly undesirable,  
almost every data set is biased.  
So it's important to understand possible data set biases.  
Biases can arise from underrepresentation  
of certain patient groups, variations in equipment,  
geographical limitations, or historical disparities.  
For example, one data size bias explanation  
could help identifying potential biases in the data,  
including those arising from its geographical origin--  
here, North American hospitals-- underrepresented populations,  
and their distinctive characteristics-- here,  
low resource or rare diseases.  
Let's now provide examples of instance-based explanations.  
The model identifies key patterns  
in the input data that align with learn patterns  
from training.  
We would like to receive explanations  
that focus on specific features that lead  
to a particular prediction.  
For example, a feature analysis explanation  
could connect pneumonia with increased opacity  
in the lower left lung region of the chest X-ray  
and the shape and distribution of these opacities.  
With this explanation, we understand  
what are the features that played a significant role  
in the pneumonia prediction for this specific patient.  
Comparative explanations analyze the predictions  
for different instances.  
This explanation compares two instances, A and B,  
highlighting the differences between them.  
It helps users see why two cases are treated differently.  
Here, we see that instance A is classified as a normal heart  
rhythm, while instance B is classified  
as atrial fibrillation due to the analysis of their ECGs.  
The irregular RR intervals and the absence of distinct P waves  
in instance B are supposed to--  
the regular sinus rhythm and clearly defined P waves,  
in instance A, are responsible for the different predictions.  
A comparative explanation focuses  
on different predictions for the same instance,  
depending on its features.  
Instead of comparing two different instances,  
this method explains why a specific case was classified  
as one label, P, instead of another,  
Q. Brain MRI scan indicates a benign tumor, B, rather than  
malignant cancer, Q, because the detected lesion in well-defined,  
non-invasive, and does not exhibit irregular borders  
or rapid growth characteristics.  
Another interesting explanation is counterfactual.  
Counterfactual explanations describe  
what changes in input data would have  
led to a different prediction.  
My prediction is no pneumonia, but if the opacity in the lower  
lung field were larger and more consolidated  
or if C-reactive protein, CRP, levels increased,  
I would predict pneumonia instead.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.3 Challenges in Providing Accurate Explanations  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The explanations presented  
earlier represent ideal scenarios  
of how AI systems should justify their predictions.  
The reality is that machine learning  
based AI systems, especially the most accurate ones,  
do not inherently operate within such  
a structured symbolic knowledge framework.  
Most successful AI models, like deep learning systems,  
operate by identifying statistical complex patterns  
in data rather than applying explicit symbolic reasoning.  
While AI can provide highly accurate predictions,  
it often lacks the ability to articulate the reasons  
behind these predictions in a manner that aligns  
with human-like reasoning.  
This limitation makes it difficult to extract  
explanations that are meaningful to humans,  
because AI models don't inherently comprehend concepts  
in the same way humans do.  
So post-hoc interpretations of AI models can be challenging.  
Rather than revealing the actual reasoning process  
behind the prediction, models often  
provide general justifications that  
make the decision appear valid.  
Consequently, post-hoc explanations  
may not accurately reflect the exact thought process  
that led to an AI prediction.  
Let's illustrate this concept with a simple example.  
Imagine an AI system trained to classify images of animals.  
Its training data, data set D, includes  
images of various animals like tigers and domestic cats.  
During the training phase, the parameters of a predictor H  
are adjusted to accurately classify  
the images in the data set.  
The goal is to achieve generalization.  
Remember, this means ensuring that the model correctly  
labels unseen animal images while avoiding overfitting.  
During the inference phase, the predictor  
processes unseen images and assigns  
them a label, for example, tiger or domestic cat.  
Of course, labeling can be challenging,  
as some animal images may be more difficult to classify  
than others.  
Since a human can often identify key features or patterns  
at a glance and label an image as a tiger,  
a question arises, can we semantically explain  
how we recognize these features or patterns?  
Can we describe the cognitive process  
behind this identification and labeling?  
And most importantly, what technical requirements  
would be necessary for the predictor  
to achieve a similar level of explainability?  
Addressing these questions is crucial to ensure that AI models  
not only accurately classify data, but also  
provide the real explanations and reasoning  
behind their prediction.  
Providing semantic explanations for labeling an image  
as a tiger or a domestic cat requires  
describing the typical characteristics  
that distinguish these animals.  
For example, distinguishing characteristics  
could be visual, structural, and behavioral.  
A tiger is typically characterized by its large size,  
muscular build, orange fur with black stripes,  
and distinctive facial markings.  
In contrast, a domestic cat is significantly smaller,  
has a more varied fur pattern, and has  
different body proportions and facial structures.  
By defining these features, we establish a context  
for semantic explanations, enabling both humans and AI  
models to articulate why a particular image belongs to one  
category rather than another.  
With a certain level of abstraction,  
we can identify features that distinguish between categories,  
even though some characteristics may overlap and create  
similarities in appearance.  
These features help in recognizing patterns that  
are crucial for classification.  
For instance, both tigers and certain domestic cats  
may share striped fur patterns, but factors  
like size, body proportions, facial structures, and muscle  
build can help draw clearer distinctions.  
While similarities do exist, focusing  
on the most discriminative features  
makes classification easier, whether performed  
by humans or AI systems.  
The table summarizes these features.  
Explanations based on these features  
can be highly informative.  
For example, instance A was classified  
as a tiger due to its bold black stripes, orange coat,  
large muscular build, and broad face with small rounded ears.  
Or instance B was classified as a domestic cat  
due to its small body size, thinner build,  
rounder eyes, narrow, irregular stripes, and long, thin tail.  
Of course, there are also other contexts  
in which explanation can be extracted,  
referring to the different image backgrounds, a jungle setting  
for a and an indoor environment for B.  
And so the question is, in which context  
is the predictors functioning most effectively described?  
Shifting our focus to the human brain's recognition process,  
it appears that humans rely on a complex interplay  
of visual processing, memory, experience, and cognitive  
reasoning to identify objects and entities.  
Unlike symbolic reasoning, this process  
is not entirely transparent or explicitly rule based.  
Instead, recognition often occurs  
intuitively and subconsciously, saved by learned patterns  
and prior experience.  
In borderline cases, ambiguous situations, or when explaining,  
humans can engage in deliberate thinking and reasoning  
to refine or describe their classification.  
AI predictors, such as deep neural networks,  
rely on nonlinear processes to make predictions.  
Deep neural networks learn intricate patterns  
from vast amounts of data, making  
their decision-making process challenging to interpret.  
Their predictions emerge through layered transformations  
of input data and abstract features that may not always be  
directly explainable to humans.  
While their accuracy can be highly impressive,  
the lack of transparent reasoning  
poses challenges in understanding and validating  
their decisions, necessitating post-hoc explanation techniques  
to approximate their internal logic in human terms.  
However, there is a risk in relying  
on post-hoc explanations that approximate the internal logic  
in human terms.  
They may provide intuitive descriptions  
that might not accurately reflect how the system actually  
makes its predictions, especially  
in the presence of bias.  
Deep neural networks excel at detecting statistical patterns  
within data sets.  
If the training data contains bias,  
the model may learn and reinforce these biases.  
Explanations should not obscure this issue,  
but instead highlight it.  
Rather than simply justifying a prediction,  
an explanation should help reveal  
whether biases in the data influence the outcome.  
Consider the following example.  
An AI model is employed to help to approve or reject  
loan applications by analyzing applicant data.  
The system was trained on historical financial records  
that contain biases.  
In the past, applicants from specific neighborhoods  
were denied loans due to systemic inequalities.  
Suppose that an applicant from a historical underprivileged  
neighborhood applies for a loan and is rejected  
by the AI system that encodes the statistical relevance that  
is a result of bias in this case.  
A standard misleading explanation  
could be the loan application was rejected  
because the applicant's income and credit score did not  
meet the required threshold, while the real reason  
is the underprivileged neighborhood of the applicant.  
In this case, the correct explanation  
should be the applicant's residential area  
is the significant factor for rejecting the loan application.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.4 Methods for Explaining AI Predictions  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now discuss  
the key methods for explaining AI predictions,  
categorized under the broader field of explainable AI.  
We can classify explainability methods  
into two broad categories.  
The straightforward approach is to use models that  
are inherently interpretable.  
Examples include linear regression  
and logistic regression, which offer direct interpretability  
through model coefficients, decision trees and rule fit,  
which provide decision pathways that humans can follow,  
or naive Bayes classifiers, which bases predictions  
on transparent probabilistic reasoning, K-Nearest  
Neighbor, KNN, which classifies based  
on proximity to known examples.  
While these models are easier to understand,  
they may not always achieve the best performance  
for complex tasks.  
For black-box models such as deep neural networks  
and ensemble methods, post hoc explanation techniques  
are essential.  
These techniques analyze and explain  
model behavior after training without modifying  
the model itself.  
There are three key types of post hoc explanations.  
The first is the global explanation methods.  
These methods aim to explain how a model makes  
decisions across all instances.  
Examples include feature importance methods,  
which rank input features based on their contribution  
to the model's output, and surrogate models, where  
we approximate a complex model using an interpretable one.  
The second type is the local explanation methods.  
Here, instead of explaining the entire model,  
local methods focus on the individual predictions.  
Examples include methods that generate  
simplified, interpretable models for specific instances  
or methods that highlight which parts of the input an image,  
for instance, influenced a neural network's decision.  
And finally, the third type is the counterfactual explanations.  
Rather than describing why a prediction was made,  
counterfactuals answer what-if questions.  
For instance, if the income of a loan applicant  
were increased by 10%, would the model approve the loan?  
These explanations are particularly  
useful for decision-making scenarios  
where specific actions are implemented to improve outcomes.  
To summarize, interpretable models  
can offer building transparency.  
But for complex AI systems, post hoc methods  
such as global explanations, local decision interpretations,  
and counterfactuals are essential to build trust.  
Let's now look at key concepts behind interpretable models,  
focusing on decision trees, one of the most transparent machine  
learning models.  
Decision trees offer a structured way  
to understand predictions, and we  
can leverage them in many ways to extract explanations.  
Here is a binary classification problem  
and a simple decision tree predictor  
with two features-- x1 and x2.  
One of the simplest and most intuitive ways  
to interpret a decision tree is by extracting rules  
from each structure.  
Each path from the root to a leaf node  
represents a set of conditions that lead to a prediction.  
These paths can be rewritten as if-then rules,  
making the model's decision-making process  
explicit.  
Here, we can see that two different paths  
lead to a green leaf node.  
So the rule if x2 less than 3, et cetera, then green  
is an explanation of the trained classifier.  
Another way to interpret decision trees  
is by analyzing feature importance.  
The importance of a feature is determined  
by how often it is used for splitting  
and how much it contributes to reducing uncertainty  
in the data set.  
To compute this, we first identify all nodes where a given  
feature is used, then measure the information gain or variance  
reduction each time it appears.  
And finally, aggregate these values across the tree  
to quantify the feature's influence.  
It's more challenging to calculate,  
but if we apply this to our example,  
we'll discover that both features are crucial.  
Another explanation technique is to decompose the decision paths.  
For instance, specific explanations,  
we can decompose the decision path  
followed by a particular input.  
Instead of looking at the entire tree,  
we analyze the specific sequence of splits leading  
to the final prediction.  
At each decision node, we examine the feature's  
contribution and how it influences the probability  
of the final class.  
This method breaks down the prediction  
into interpretable steps, making it easier to justify  
and debug individual decisions.  
In our example, we can observe that x1 greater than 4  
always means red.  
This provides a global explanation,  
helping us understand which features  
have the greatest impact on the model's overall decision-making.  
The above techniques make decision trees  
one of the most interpretable models providing transparency  
while maintaining strong predictive power.  
While decision trees are known for their transparency,  
it's important to recognize their limitations  
in interpretability.  
Decision trees are easier to understand when they are small,  
typically when they have a limited number of splits.  
But larger trees are more complex,  
making rule extraction impractical.  
For instance, a tree with just 10 to 15 levels  
can have thousands of decision paths,  
making it as opaque as a neural network model.  
Moreover, decision trees are highly  
sensitive to data set variations, which can  
lead to unstable explanations.  
This highlights the trade-off between complexity  
and explainability.  
And it is the main reason why carefully designing  
decision trees for interpretability  
is so important.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.5 Post-hoc Explanations in AI  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Turning our attention to post-hoc interpretation,  
particularly to global explanation methods,  
let's explore one of the most interesting methods,  
the interpretable surrogate models.  
A global explanation helps us understand the general decision  
rules the model follows, how different features influence  
predictions, whether the model exhibits systematic biases  
or relies too heavily on specific features.  
For example, consider a classification model  
where we analyze how it makes predictions.  
A global explanation might reveal  
I classify instances as category X when feature A is high  
and feature B is low.  
However, when feature A is moderate but feature C is high,  
I classify instances as category Y.  
This tells us the general decision  
structure the model follows, making it easier to verbalize  
and therefore validate.  
Another aspect of global explanations  
is identifying which features drive the model's decisions.  
For instance, overall, my predictions  
are most influenced by feature A,  
feature B, and feature C. Feature A contributes  
to 40% of the decisions, feature B to 30%, and feature C to 20%.  
Other features have minimal impact.  
This insight allows us to detect potential biases.  
If the model disproportionately relies on a specific feature,  
it might indicate bias or overfitting.  
A widely used technique for globally explaining complex AI  
models is mimicking the black box model  
using an interpretable surrogate model.  
Deep neural networks and other black box models  
often make highly accurate predictions.  
But their internal decision-making process  
is opaque.  
To make these models more interpretable,  
we can approximate their behavior  
with a simpler, interpretable surrogate model,  
such as a decision tree.  
How does this work?  
First, we train a complex model, such as a deep neural network,  
on the original data set.  
We then use the trained black box  
model to predict outputs for a large set of instances.  
Instead of using the original data set labels,  
we train an interpretable model, such as a decision tree,  
to mimic the black box model's predictions.  
Since decision trees are intrinsically interpretable,  
we can extract decision rules, feature-important scores,  
and decision paths to approximate the black box  
model's behavior.  
Now let's explore how we can leverage surrogate models  
for local interpretation.  
Local interpretation aims to explain  
why a specific instance was given a particular transaction  
by an AI model.  
Unlike global explanations, which  
describe the overall behavior of a model,  
local explanations answer the question,  
why did the model make this specific prediction  
for this particular input?  
By analyzing individual decisions,  
we can understand what features influenced the outcome.  
Imagine a machine learning model is used  
to evaluate loan applications.  
A local explanation might provide insights  
like the loan was rejected mainly  
because of the applicant's low credit score  
and high debt-to-income ratio.  
The part-time employment status also negatively impacted  
the decision.  
This breakdown highlights the most important  
contributing factors, making it easier  
for the applicant and financial regulators  
to understand the decision.  
One very interesting and widely used  
method for extracting post-hoc local explanations is LIME.  
The acronym comes for local interpretable model  
agnostic explanations.  
LIME follows a four-step methodology.  
First, we generate multiple slightly modified versions  
of the original instance by introducing small changes  
to its features, then each perturbed instance  
is passed through the black box models  
to record the changes in its output.  
Once we do this, using the perturbed samples  
and their predictions, we fit a simple interpretable model,  
for example, a linear regression or a small decision tree.  
And finally, we extract explanations  
for the operation of the surrogate model,  
hoping that this allows us to explain why the black box  
model made its decision for this instance.  
Considering the example of the deep neural network classifier  
that recognizes tigers, we can use deep neural network  
inference to generate perturbed instances  
and use them to record the prediction changes.  
Then we can find surrogate models by fitting interpretable  
models like decision trees.  
Using the important features-- for instance, large, golden,  
yellow, or amber-colored eyes with round pupils,  
small rounded ears, bold black stripes on an orange coat,  
muscular body, long and striped tail--  
we can extract explanations like instance  
A was classified as a tiger because it  
has bold black stripes on an orange coat, a muscular body,  
a long and striped tail, small rounded ears,  
large golden yellow or amber-colored eyes with round  
pupils that involve these features.  
Now let's discuss counterfactual explanations,  
a powerful technique for understanding  
AI decisions by exploring what could have been different.  
What are counterfactual explanations?  
Rather than explaining why an AI model made  
the specific decision, counterfactuals  
explai what minimal changes to the input  
would have led to a different outcome.  
Instead of answering, Why was my loan rejected?  
a counterfactual explanation answers,  
What would need to change for my loan to be approved?  
Suppose an AI model rejects a loan application.  
A counterfactual explanation might  
say, if your credit score and your income  
increased a bit, giving some numbers,  
your loan would be approved.  
This explanation provides actionable insight  
into what the applicant can do to improve  
their chances of approval.  
Counterfactuals also apply to computer vision models.  
Suppose an AI system classifies a domestic cat  
as a tiger because of its background.  
A counterfactual explanation might  
say, if the same cat were in a living room,  
the model would classify it as a domestic cat instead of a tiger.  
This means that changing the background  
alters the classification outcome.  
In this case, counterfactuals explain  
how context influences model decisions,  
helping us detect possible biases in AI predictions.  
To generate counterfactual explanations,  
we can use several methodologies.  
For example, there are optimization-based approaches.  
The goal is to find the smallest possible change  
in input features that would result  
in a different prediction.  
This is often done by solving an optimization problem where  
we minimize the changes required to flip the model's decision.  
For instance, instead of suggesting a major salary  
increase, the model identifies that a 5,000 increase in income  
and a 50 point increase in credit score are sufficient  
for loan approval.  
These methods ensure counterfactuals remain realistic  
and minimally disruptive.  
Another approach is to extract prototypes.  
Instead of modifying the original instance,  
this method finds a real-world example  
from a different class that is similar to the given instance.  
Generative models, such as GANs or variational autoencoders,  
can be used to generate realistic counterfactual  
instances.  
For example, if a patient is diagnosed with a disease,  
the system could find a similar patient  
who was classified as healthy, highlighting the key differences  
in their medical profiles.  
This method helps answer, What does  
a real example from the desired class look like?  
making counterfactuals more interpretable.  
So what is the take-home message of this lecture?  
First of all, AI is very useful, but there  
are many considerations to be taken into account.  
In particular, potential risks that  
may be material or immaterial, stemming from biased decision  
making, unfair treatment, security vulnerability, and AI  
system malfunction, among others.  
The lack of transparency in AI models  
contributes to algorithmic aversion,  
where users are reluctant to trust automated decisions.  
Without clear explanations, AI remains a black box,  
making it harder for users to trust AI and adopt it  
in practice.  
Explanations are key to AI transparency.  
To build trustworthy AI, we need transparent and interpretable  
systems.  
This means that we need to extract explanations that  
describe the AI model predictions,  
but also the data collection, pre-processing,  
and training processes.  
To trust the AI system, users should  
be able to understand how a specific instance was classified  
and what factors influenced the outcome.  
On the other hand, providing explanations  
is not an easy task.  
While the need for explainability is clear,  
implementing effective explanations  
remains a major challenge.  
Context is crucial to understand explanations terminology,  
and the form of explanation is important.  
Different applications require different types of explanations.  
For example, a doctor may need a description of the detailed AI  
reasoning in medical terms, while a loan applicant may  
need a simple and intuitive justification  
for the rejection of an application  
or the factors that should be changed for getting acceptance.  
And finally, it is very challenging  
to develop interpretable machine learning models  
with high accuracy as it is to successfully post-hoc interpret  
black box AI models like deep neural networks.  
By addressing these challenges, we  
can build trust moving forward to a more human-centered AI.  
Thank you for your attention.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture showed how explainable AI is essential for building trustworthy AI systems by making data, model behavior, and individual predictions transparent—especially in high-risk domains.

Key Takeaways:  
Trust depends on transparency: AI risks (bias, privacy, safety failures) and algorithmic aversion make clear explanations necessary for adoption and accountability.  
Explain the full lifecycle: Transparency includes training data (source, labeling, size, bias), performance metrics (errors, uncertainty), and instance-level decisions.  
Three core explanation types:  
Global — how the model behaves overall.  
Local — why this specific prediction was made.  
Counterfactual — what minimal change would alter the outcome.  
Model choice shapes interpretability: Interpretable models (e.g., decision trees) provide built-in clarity; complex models require post-hoc tools (surrogates, LIME, counterfactual methods).  
Explanations must be faithful: They should reveal true drivers—including hidden biases—not just produce intuitive but potentially misleading justifications.  
\`\`\`

Lecture 2: AI & Fairness  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: AI & Fairness, taught by Professor Dimitris Bertsimas, Boeing Leaders for Global Operations Professor of Management and Professor of Operations Research at MIT.

What do college admissions, loan approvals, and parole decisions have in common? They all rely on data-driven judgments—ones that can inherit human bias and quietly amplify it. This lecture introduces fairness-aware machine learning:

Spotting systemic bias: Real-world datasets (admissions, hiring, lending, policing) can encode disparities across race, gender, and ethnicity. Simply dropping protected attributes doesn’t fix it—proxies linger.  
Measuring fairness: We formalize bias (α-bias) and define demographic parity, requiring outcome-rate gaps between groups to be within a small threshold ε.  
Understanding feedback loops: Predictive systems can reinforce disparities (e.g., policing), making biased outcomes even more likely over time.  
Fixing bias with optimization: We frame fairness as a mixed-integer optimization problem: jointly learn logistic-regression parameters and optimally flip a limited set of labels to meet ε-parity.  
Interpreting the remedy: An optimal classification tree on “flip / no flip” outcomes reveals when and why adjustments occur—turning a black box into actionable rules.  
Case studies in practice: Bar-exam outcomes and COMPAS recidivism predictions show how ε-parity can substantially narrow group gaps with only slight impact on meritocracy.  
Tuning the trade-off: The “price of diversity” is quantifiable; ε is a dial you set for the problem at hand.  
By the end, you’ll see how optimization and interpretable ML can detect, quantify, and mitigate bias—improving equity while preserving meritocracy as much as possible.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define systemic bias in datasets and distinguish between diversity and meritocracy in decision-making.  
Describe why removing protected attributes does not eliminate bias (proxy leakage).  
Explain α-bias for datasets and ε-demographic parity as a fairness criterion for classifiers.  
Interpret how feedback loops (e.g., predictive policing) can reinforce disparities over time.  
Outline how logistic regression with label flips can be formulated as a mixed-integer optimization problem to enforce ε-parity.  
Show how interpretable audits are performed using optimal classification trees to identify conditions under which labels are flipped.  
Compare fairness–meritocracy trade-offs and quantify the price of diversity when tuning ε.  
\`\`\`

L2.1 Fairness & Bias: Demographic Parity  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In this lecture, we'll discuss fairness and bias  
in machine learning.  
The problem we will be addressing  
is the problem of systemic bias.  
Systemic bias with respect to gender, race, and ethnicity,  
often unconscious, but is prevalent in data sets involving  
choices made by people.  
Some examples include data sets related  
to human choices like college admissions, hiring, lending,  
or parole decisions that discriminate  
against African-Americans or women.  
Let me discuss the definitions of diversity and meritocracy  
that is relevant in this lecture.  
Diversity is defined as the practice of including people  
from a range of different social and ethnic backgrounds,  
and of different genders and sexual orientation.  
Meritocracy is defined as the practice  
of selecting people when a choice is made based  
on achievement, as opposed to wealth or membership  
in a special social class.  
Often in practice, these two goals are in conflict,  
and we observe an inherent trade-off between them.  
Society has found it challenging to alleviate such bias  
and achieve diversity in a way that maintains meritocracy  
in these settings.  
In recent years, due to the growing volume of applications  
in college admission, hiring, lending, et cetera,  
machine learning models are being increasingly employed  
for such classification problems.  
It has been shown that without appropriate intervention  
during training or evaluation, classification models  
train on such data sets can be biased against certain groups  
of individuals.  
Of course, we can apply simple remedies, for example,  
ignoring the protected attributes, for example, gender,  
race, ethnicity, et cetera.  
But such practices are largely ineffective  
due to the other factors being correlated with the protected  
attributes.  
The data can be inherently biased in possibly complex ways,  
thus making it difficult to alleviate bias.  
Of course, there is price on inaction.  
Classification models that are actively trained on such data  
sets become more biased over time  
through feedback loops, wherein the bias  
against a certain subpopulation can be amplified.  
Feedback loops have been observed in predictive policing,  
for example, credit markets, or many other applications.  
Let me give you an example of the notion  
of feedback loop in the context of predictive policing.  
So whenever we encounter more crimes and arrests  
in a particular neighborhood, this  
results in an update of the crime database.  
And of course, based on this updated database,  
we train a predictive model.  
This results in deploying more law enforcement resources  
in these certain neighborhoods.  
This means that there is an encounter more  
crimes and arrests in these neighborhoods,  
and the feedback loop continues.  
Let me illustrate what we'll do today  
using a data set involving law students.  
This data set examines whether the bar exam taken  
by law students in the United States  
is biased against ethnic minorities, especially  
Black students.  
The data set also contains anonymized historical  
information, including age, LSAT scores, law school GPA,  
and undergraduate GPA.  
To mathematize the information we'll present,  
I'm going to use the following notation  
that each of the students is assigned an outcome, minus 1  
or plus 1, representing passing, plus 1, or failing, minus 1,  
of the bar exam taken by the student.  
We define the set w to be the set of white students, the set  
capital B to be the set of Black students,  
and then we denote by nw, the total number of white students  
that have taken the exam, and b, the total number  
of Black students who have taken the exam,  
pw is the total number of white students  
who have passed the exam, and pb,  
the total number of Black students  
who have passed the exam.  
So we need to define what does it mean  
to for a data set to be biased.  
We utilize the notion of alpha bias,  
alpha is a number between 0 and 1\.  
So we call a data set to be alpha  
biased if the difference between the rates  
of positive observation among the group of white students  
and the group of Black students is at least alpha.  
In other words, the percentage of white students  
that have passed the exam minus the percentage of Black students  
that have passed the exam, this difference is above a threshold  
alpha.  
In that case, the data set is alpha biased.  
For example, if it's, let's say, 50%,  
it means that the percentages are 50% apart,  
an undesirable effect.  
Let me define the notion of demographic parity.  
So demographic parity of a classifier,  
this is a system that decides who gets a positive outcome,  
passes the bar exam, versus does not pass.  
The definition is as follows.  
If you take the percentage of white people who  
pass the exam based on this classifier,  
minus the percentage of Black people  
who pass the exam based on this classifier,  
this difference, the absolute value,  
is less than some value epsilon, let's say, 1%, epsilon  
equals 0.01.  
In that case, we have parity, which is a desirable outcome  
so that we have some notion of fairness.  
So let me give you an example of such demographic parity.  
Let's say we have two subpopulations,  
subpopulation A and subpopulation B.  
On the top left, we see that, out of 6 people,  
4 had a positive outcome, passed the exam,  
whereas on the subgroup B, out of the 6, 2 pass the exam.  
So in this case, the data set is alpha equals 1/3 bias, so 1/3,  
the difference is 4/6 minus 2/6, that's 1/3.  
And then on the right, we see 3 out of 6  
on the subgroup A who passed the exam, and 3 out of 6  
on subgroup B that pass the exam.  
So in this case, alpha equals 0\.  
That is demographic parity.  
So now let me go into the key proposed solution.  
So what we do is we allow to flip the outcome  
labels while training the model to achieve parity.  
And in particular, we're going to use optimization  
to flip in an optimal way.  
So we propose a mixed integer optimization  
of the type you have seen in the area of prescriptive AI.  
So we used mixed integer optimization, MIO,  
for short, that introduces a variable Zi, 0 or 1,  
to decide which outcome label to flip.  
For example, a particular student  
who was originally assigned plus 1, meaning passed the exam.  
And if Zi equals 1, we flip.  
So this Yi become minus 1\.  
And similarly, if Yi was minus 1, it did not pass the exam  
and we flip, we make it Yi plus 1,  
meaning the person passed the exam.  
So if we decide to flip the outcome label of the ith  
observation of the ith student, so the new, Yi, let's call it  
Yí, the new Yi, is equal to Yi times 1 minus 2 times Zi.  
In other words, if Zi is 0, we don't flip.  
Then the new Yi is equal to Yi, we then flip it.  
If, on the other hand, Zi is 1, 1 minus 2 Zi is minus 1\.  
So then Yí becomes minus Yi, therefore, we flipped it.  
So of course, we need to be careful  
how many variables we flip.  
So we define the set of variables Zi  
so that we only flip a portion.  
We call it Tw of labels to flip among the white population,  
and T subscript b proportion of labels  
we flip in the b population, in the Black population.  
And in order to achieve demographic parity at the level  
epsilon, recall that this is the number of people  
who pass the exam among the white population  
minus the percentage of people who  
pass the exam in the Black population,  
this difference would be less than epsilon.  
So we select Tw and Tb correctly,  
as shown in the calculation.  
Then we achieve epsilon demographic parity  
if we flip Tw and Tb labels.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.2 Fairness via Logistic Regression: Demographic Parity  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now, let's consider a principal method  
we used in the past for classification,  
namely logistic regression.  
Recall that y equals plus 1, as we have discussed,  
means that passing the bar exam.  
And y equals minus 1 is failing the bar exam.  
So we seek to predict the probability of a success outcome  
for the dependent variable y, passing the exam,  
as a function of independent variables x1, x2, xk.  
Recall that the likelihood of y equals  
plus 1 is given by the formula in the slide, which  
is the classical logistic regression formula.  
So how do we select the beta coefficients,  
the coefficients that multiply the variables to make  
the prediction?  
We optimize over the beta variables  
the likelihood of achieving that.  
But in addition, now, to optimizing over beta,  
over the parameters, we can also optimize--  
you can select which variables to flip.  
So that we flip the variables, as well as  
changing the betas together to optimize the likelihood further.  
So this can be modeled.  
This mathematical model can be modeled as a nonlinear,  
in this case, binary optimization  
problem of the types we have discussed  
in the foundational module on AI prescriptive.  
And this is given here.  
The details are not so important.  
The key here is it can be done easily.  
So in the end of the day, by solving an optimization problem,  
we find the parameters of the logistic regression.  
And at the same time, we find which variables  
to flip in such a way that we achieve a parity,  
namely that the difference of ratios  
between those white students-- the percentage of white students  
who pass the exam minus the percentage of Black students  
that pass the exam is less than epsilon for an epsilon  
being a pre-specified characteristic, which is we  
utilize it to be 1%.  
So let us apply this methodology to the data set that I mentioned  
about passing the bar exam.  
This data set originates from this study in the late '90s that  
examined whether the bar exam taken by the law students  
in the United States is biased against ethnic minorities.  
It contains anonymized historical information,  
including age, LSAT scores, first year law school  
GPA, cumulative law GPA, the GPA in the law school,  
as well as the undergraduate GPA.  
So it has achievement.  
It had, of course, age, and then achievement  
of scores for a variety of characteristics.  
So now, the graph here shows the differences  
between Blacks and whites on various characteristics  
involving the LSAT, the GPA in the law school,  
the undergraduate GPA, and so forth.  
And you see that white students, the ones in blue,  
have overall, on the left, stronger scores  
than their Black counterparts.  
Whereas on the right graph, this is the same thing regarding  
gender, we see that male students, at least in two  
of the three categories, are slightly above the averages  
relative to female students, on the other hand,  
on the law school GPA, the female students are stronger.  
In other words, these data sets are biased with alpha on race  
is 0.3.  
And the alpha, the bias on gender, is much lower, 0.02.  
So in other words, there is very little bias on gender.  
But there is quite a lot of bias for race.  
So the story is similar regarding  
LSAT scores, the undergraduate GPA, and so forth.  
So this is the situation we aim to remedy.  
So we apply for these data sets that exhibit some bias regarding  
race anyway at the level of 0.3 to bring it  
to basically very little bias, epsilon equals 1%, 0.001.  
And what we observe, if you focus  
on the vertical that says LR for Logistic Regression,  
so regarding the white applications,  
you observe that in the data, this is the so-called z-score.  
I remind you that z-score of z-score  
of a person minus the mean divided  
by the standard deviation.  
And we observe that for the white population, if you apply  
this optimization method, we don't materially  
change the scores before what is in the data  
and what is after the optimization.  
However, with the Black population  
there is a slight decrease.  
We make it less meritocratic, so to speak, but very little,  
slight.  
So I repeat again that the z-scores of the attributes,  
the GPA, the LSAT scores for admitted students  
among the white population do not change significantly  
even after employing the mixed integer optimization approach.  
However, the z-scores of attributes for admitted students  
among the Black subpopulation decreases slightly,  
signifying that lowering the threshold for passing the bar  
exam for Black students, but in such a way  
that we help to achieve demographic parity.  
So we very much achieve the getting demographic parity,  
namely the percentages of whites who  
pass minus the percentage of Blacks who pass  
is basically now within 1%, where  
it used to be 30% apart at a very small price on meritocracy.  
So now, of course, this is a machine  
learning quantitative method.  
What we would like now to do is we would like to understand  
in an actionable way, using machine learning again,  
what are the characteristics of these students  
for which the outcome labels are flipped after employing  
the mixed integer optimization approach?  
So what we do on that, we construct  
a new data set based on the results of the optimization  
approach.  
Each observation is labeled as one of the following-- positive,  
this is where the label flipped to a positive label,  
negative, this is where the outcome changed  
to a negative label, or no change.  
So now we have, because the mixed integer optimization  
approach could actually change the label to positive,  
or change the label to negative, or no change,  
so now this is a three class classification problem.  
So we have the attributes, the xi's.  
This is the age, the undergraduate GPA, LSAT,  
and so forth.  
And then the outcome is whether the outcome changed,  
it flipped in the positive way, or in a negative way,  
or no change.  
And then we apply in an optimal classification tree,  
the methodology we used in the foundational module  
on machine learning.  
And what we observe is this tree that  
makes partitions of this data set  
and then outputs when you make a change or not.  
In that way, we have now an interpretable way of deciding  
when we flip or we don't flip.  
Now this particular model, this tree  
has an area under the curve of 0.67, not spectacular.  
But on the other hand, insightful  
in telling us what are the key characteristics of the variables  
that result in flipping.  
So, for example, let us summarize the understanding.  
The logistic regression model identifies the following  
criteria, based on GPA and LSAT scores  
to select the most meritocratic students  
among the Black subpopulation.  
So if the LSAT is above 34.75 and the z-score of the GPA  
is less than minus 0.86, so these are stronger scores,  
or the LSAT is less than 34.75 and the undergraduate GPA  
is above 215, those Black students who  
were assigned to a negative label,  
we flipped them to a positive label.  
So notice that they have either a higher LSAT score or higher  
undergraduate GPA.  
The model also identifies criteria  
for the least meritorious students  
among the white population.  
So in this case, there are two categories.  
This is now among the white population,  
the LSAT is bigger than 3475 and the cumulative GPA z-score  
is less than minus 156\.  
Or the LSAT is less than 3475 and the cumulative z-score  
of the GPA is less than minus 1.08.  
So those white students who were assigned a positive label,  
we now flip them to a negative label.  
So in other words, it identifies the most meritorious Black  
students, we flip.  
And then the least meritorious white students,  
we flip from positive to negative.  
You can go into further analysis.  
These numbers discuss in more detail about the various nodes  
that make no change.  
For example, among the Black population,  
if the LSAT is already greater than 3475  
and the GPA is bigger than minus 0.86, which  
is 93.4% of the students who actually pass the bar exam,  
these are Black students that already have passed the exam,  
they are very qualified, we do not change.  
And similarly, we have Black students who are not  
qualified enough using the criteria that you observe,  
we don't change.  
In other words, we only change the Black students  
that are close to the border.  
And we pass the exam.  
And on the white population, similarly,  
those students that are most qualified, we'd make no change.  
Or white students that are not qualified enough, also,  
we make no change.  
In other words, we holistically look at these variables.  
And we only flip those on the boundary, as I have indicated.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.3 The Price of Diversity: Fairness in Recidivism Prediction  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So the second example I would like to discuss  
is related to the US criminal justice system.  
So the United States has the highest incarceration rate  
in the world, about 0.7% of the population, which  
is a very significant number.  
But unfortunately, incarceration rates  
are not uniform across racial groups, as the graphs indicate.  
So, a key aspect is recidivism.  
So recidivism is the idea that people  
who have been in the jail system and leave the jail system  
commit crimes again and come back to the jail system.  
So recidivism prediction instruments, RPI for short,  
is the assessment of recidivism likelihood  
are guiding pretrial release and parole decisions.  
There is a particular organization, Northpointe,  
it was founded in 1989, to develop software  
for justice, as they call it.  
And a particular system called COMPAS--  
this is the Corrections Offender Management Profiling  
for Alternative Sanctions, makes the recidivism prediction  
from about 137 questions.  
So an organization called ProPublicas, based on this data  
set, try to assess whether such software systems are biased  
or not.  
The particular data set that they used was 7,918 criminal  
defendants in a particular county in Florida in 2013  
and 2014, and the recidivism outcomes through 2016\.  
In other words, this decision was taken in 2013-14,  
and then we observe over the next two or three years whether  
there was recidivism or not.  
So the outcome variable is the risk score, low or high,  
how likely it is the person would exhibit recidivism.  
The variables, the independent variables,  
were gender, age, race, as well as criminal history,  
the date of the offense, the number of prior counts, the type  
of previous offense, the history of revivalism,  
the felony history, and how long the person has been in prison.  
You observe the distribution of the COMPAS scores.  
You observe that there are skewed to the left.  
And you observe also that the incidence of recidivism  
is close to 50%, which is a pretty significant number.  
And you also observe that there is prevalence of recidivism  
by race.  
So you observe, for example, that the percentage  
of Black people that exhibit recidivism  
is higher than all others, all other races.  
And then you also observe, similar to what  
we have done for the low case, you  
look at the distribution of covariates by group.  
You look at the distribution of age, prior counts,  
as well as the decile score for defendants  
who have been assigned a high score by race and gender.  
We observe that these data have, indeed, alpha bias.  
The alpha for age is 0.29 and the alpha for gender is 0.12.  
This means, again, that the percentage  
of people who exhibit the recidivism  
over the white population minus a corresponding percentage  
of the Black population, this difference is 29%.  
In other words, higher percentage of Black people  
by about 29%.  
And similarly for gender, although less, it's only 12%,  
males are more likely than females to exhibit recidivism.  
When we apply the same method, the mixed-integer optimization  
and so forth, to flip, we also find  
an area under the curve of 0.72 is exactly  
the same methodology as before.  
You observe the classification tree here with epsilon  
equals 1%.  
And we observe that the key variables,  
of which to go left or right in the tree,  
is race, age, as well as prior counts.  
So, similar ideas, in other words,  
that the logistic regression model identifies criteria  
based on age and prior counts to select  
the most qualified dependents among the Black population.  
In particular, whenever the age is  
above 36.5 and the prior counts is less than or equal to 3\.  
And these people, Black people, were assigned a negative label,  
meaning parole was not given.  
And we flip, this is the case, they now have a positive label.  
And similarly, the model also identifies  
criteria for the least qualified defendants  
among the white subpopulation, and the criteria  
the model used is that the age is less than 36.5  
and the prior count is at least 1, or the age is less than 26.5,  
and the prior counts also are less than 1\.  
These are defendants-- white defendants  
who are assigned a positive label,  
and we flip to a negative label.  
Similarly, the leaf nodes that predict no change involve  
the most qualified Black population in which we maintain  
no change, and similarly, the least qualified,  
we also exhibit no change, and similarly  
for the white subpopulation.  
This analysis is analogous to what  
we have done in the law data set,  
and it provides insights in which conditions under what  
scenarios we flip the labels or not.  
So if you take a moment and look at the key takeaways  
of the lecture, we have observed that data sets exhibit bias--  
in this particular case, very significant racial bias on two  
examples.  
So problems involving such individual choices  
can be automated using machine learning algorithms--  
this is what we have demonstrated--  
that can alleviate individual biases  
and enhance diversity without significantly compromising  
on meritocracy.  
In practice, the price of diversity can be quantified,  
and consequently, the demographic parity  
can be tuned to the level which is  
appropriate for the problem at hand.  
So this whole area shows the flexibility  
that the techniques we have seen throughout universal AI,  
namely machine learning and optimization,  
can be flexibly adapted to improve diversity  
with decreasing meritocracy only very slightly.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture showed how fairness-aware machine learning can detect and mitigate systemic bias in high-stakes decisions by formalizing fairness metrics and using optimization to balance diversity and meritocracy.

Key Takeaways:  
Systemic bias in data: Datasets from human decisions (admissions, lending, parole) embed racial and gender bias, and feedback loops can amplify disparities over time.  
Formal fairness definitions:  
α-bias measures disparity in outcome rates across groups.  
ε-demographic parity requires group outcome rates to differ by no more than a small threshold ε.  
Optimization-based mitigation: Mixed-integer optimization jointly trains logistic regression and minimally flips labels to satisfy ε-parity while preserving predictive performance.  
Interpretable fairness rules: An optimal classification tree explains when flips occur—typically adjusting borderline cases (e.g., most meritorious minority candidates or least meritorious majority candidates).  
Quantifying the trade-off: The "price of diversity" is measurable—fairness constraints can substantially reduce disparity with only slight impact on meritocracy.  
Real-world validation: Applied to bar exam outcomes and COMPAS recidivism scores, the framework significantly reduced racial gaps while maintaining model effectiveness.  
\`\`\`

Recitation 1: Explainable AI in Practice: Methods Across Data Modalities  
\`\`\`  
Skip to main content  
Recitation Overview  
Welcome to Recitation 1, taught by Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.

In this section, we'll walk through hands-on examples and practice exercises to reinforce the concepts covered in the lectures, focusing on Explainability in AI. The notebook used in this Recitation is available at the following link:

Recitation 1 Notebook

Due to potential memory issues, you are advised to not run this notebook on the server and just review the outputs.

This notebook is complete — all code has already been written and executed — so you will see the outputs from each code cell. Your task is to use these outputs, along with the concepts covered in this module, to answer the questions in this assignment.

If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Lectures covered by this recitation

Lecture 1: Explainable AI  
Let’s dive in and explore the material together\!

Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.  
\`\`\`

R1.1 Preparing Tabular Data  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
Welcome to today's recitation regarding  
interpreting machine learning models  
across different modalities.  
So today, we're going to focus on concepts  
that you came across the explainability lecture  
of this module.  
And we want to emphasize how important an explainable AI is  
for transparency, fairness, et cetera.  
Machine learning models that are used in practice  
should be as interpretable as possible.  
And this is, first and foremost, because we  
are more confident about what the model learns  
and how it behaves.  
And also, it increases the chances  
of higher adherence of people--  
of practitioners, basically, to AI machine learning models,  
in general.  
So we're going to explore interpretability  
across tabular data, images, and language data.  
We're going to first start with tabular data.  
We're going to work with these adult income data set.  
And we're going to see how we can retrieve interpretability  
when we use different machine learning models  
that you have probably already seen in other modules.  
So today, we are not going to explain how these models work.  
We are just going to only focus on the interpretability aspect  
of these models.  
Next, we're going to move on to image interpretability, where  
we're going to see some cool ways of visualizing which parts  
of the images contribute more to the final predictions of images  
models.  
And then, last but not least, we are  
going to go over a language example,  
and we are going to see how attention maps help understand  
which word has-- which words are important for each anchor word.  
And we're going to also explore LIME,  
which is another method that is widely used for explainability.  
So the goal, again, is not to dive into how the models work  
or what's the difference between the tabular, the image  
models, the language models.  
We just want to explore ways of using interpretability.  
So let's start with the first modality, the tabular data.  
We are going to use the Adult Census Income Data Set, which is  
a publicly available data set.  
And we are talking about a classification problem here.  
So we are going to train models that aim to predict whether  
a certain person earns more than $50k per year.  
It's a binary classification problem.  
We have the label 0 if its sample--  
its person has an income of less than $50k.  
And we have the target 1 for the people that have an income above  
$50k.  
We are going to explore a logistic regression  
model, a decision tree, random forest, XGBoost.  
And we're going to use the SHAP explainer inside the--  
we're going to use the SHAP explainer on the XGBoost  
to get some idea about explainability.  
We are going to simplify the features a bit  
because this data set has a lot of categorical features.  
And we think it's more intuitive to just preprocess them and keep  
the most informative and easy-to-parse features.  
First of all, as always, we load our data set  
and the different dependencies, different packages that  
are required for the notebook.  
We are also going to load the Adult Data Set.  
It is available online.  
These here are the names of the different features.  
Income is the final column, the target column.  
And the rest are just our X's, our input features.  
We are removing rows with null values.  
The Adult Data Set is pretty big,  
so we have the luxury to do that.  
And then we are also going to only change  
the features to keep only this.  
We are keeping the age, the sex, the education number,  
hours per week, capital gain, capital loss,  
and marital status.  
And we're going to explain what each of these features  
corresponds to.  
But the idea is that we want to use a simplified  
subset of the features.  
We are encoding the income column as a binary column  
because as we said, we want to solve a binary classification  
problem.  
So if the income is above $50k, then we are encoding this as 1\.  
This is a Boolean evaluation.  
And also, we are simplifying the sex feature.  
We are also simplifying the married feature.  
So if someone is married, regardless  
of other more specific information about the marriage,  
we encode it as 1\.  
If they are unmarried, encoded it as 0\.  
This is how our data set looks like.  
We have the features that we mentioned before.  
And now let's understand what each of these features mean.  
So first, the age, the sex and the marital status  
correspond to demographic and personal attributes.  
So age is, of course, the age of the individual in years.  
Sex is encoded as 1 for males and 0 for females.  
And marital status is encoded as 1 for married and 0  
for unmarried.  
Then we have the education and skill indicators, which  
is basically the education num.  
This is a numeric score representing highest education  
level.  
So the highest the value of this feature,  
the more educated the person is.  
And then we also have work and financial attributes,  
which are the hours per week, which  
is the average number of hours worked per week;  
capital gains, which are investment gains-- for example,  
stocks, real estate.  
For most people, this is 0, but it's still  
an informative factor.  
And capital loss is investment losses used for tax purposes.  
The target variable, as we said earlier, is the income.  
And we have binarized it in a way that we assign 1  
if the income is larger than $50k and 0 otherwise.  
Now, we define our X's and our Y's.  
The Y's the target variable, the income.  
We split into train and test set to avoid data leakage.  
And we have our numerical and our categorical columns.  
And we define these preprocessing pipeline here  
that basically says that, for numerical values,  
use a standard scaler to scale our features.  
And for categorical, which are binary in our case,  
we don't need to do anything.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.2 Explainability in Tabular Data  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We start with logistic regression.  
Logistic regression is a linear model.  
It's quite transparent.  
Because at the end, we get, for each feature,  
a certain coefficient.  
And it's very easy to interpret these coefficients  
because if the coefficient is positive,  
it increases the probability of label 1\.  
So if a feature has a very positive coefficient,  
this means that it contributes a lot to predicting someone  
as having the label 1\.  
If the coefficient is negative, it decreases this chance.  
So we define our logistic regression pipeline here.  
First, we have the preprocess step,  
and then we have the classifier, the logistic regression.  
We fit the model on our training set.  
And then we are going to print the coefficients to basically  
see how each feature contributes to the final prediction.  
We can see we have ranked the features here with in descending  
order, basically.  
And as you can see, the factor, the feature  
with the highest positive coefficient is marital status.  
What does this mean?  
It means that people that are married, according to the model,  
are more likely to have income above 50k.  
Also, if someone has a capital gain,  
this is also a very strong predictor.  
So you would say that these two are the features with the two  
highest coefficients.  
So we can extract the interpretability.  
Like, we can extract basically the information  
that, as far as interpretability is concerned for this model,  
the most important features are the marital status  
and the capital gain.  
And then all factors contribute positively,  
which means that the higher, for example, the education level,  
the more it contributes to a positive income.  
But the two highest ones were these two, the marital status  
and capital gain.  
Another type of classifier is decision trees.  
Decision trees basically produce some logical rules that  
are very easy to visualize.  
And they are extremely interpretable.  
We are defining this preprocessing here.  
Here, we do not need to scale our features  
in the preprocessing because it doesn't affect the model,  
and we want the split to be intuitive.  
So we want the features to have their natural--  
meaning their natural quantities without us altering them.  
So we define the tree pipeline, and we fit on the training set.  
Now we're going to visualize the tree,  
and we are going to see how easy it is to get interpretability  
from tree models.  
We visualize-- we print the tree.  
And it's very easy to read it.  
For example, here, we have the following.  
If the marital status is less than 0.5-- and as I remind you,  
marital status is either 0 or 1\.  
So basically, if the marital status is equal to 0,  
so if someone is unmarried, basically,  
but they have a capital gain that is, say, above 7,000,  
then we end up here in this node,  
which predicts that this person has an income of above 50k.  
I repeat, the way we read the tree is,  
we ask the question in the first row,  
is the marital status less than 0.5?  
If this is true, we go left.  
If this is false, we go right.  
So in the case that we go left, we end up in this node here.  
And then we ask this question.  
Is the capital gain less than 7,000?  
If yes, we go here.  
If no, we go here.  
Here, on the right, if someone is married and, for example,  
if the education number is less than 12.5, we go left.  
But if it's above, which means that they're  
highly educated and married, goes right.  
Here, we predict that the people have an income of above 50k,  
which intuitively makes sense as factors,  
and it's as easy to be completely transparent and see  
what the model decides for each sample.  
For example, for the first point of the test set,  
if we pass it through the tree, we  
can basically see in which nodes the sample falls into,  
which path it follows to reach a final leaf node.  
So we can see the exact path and understand  
why this prediction was made.  
Now, logistic regression and decision trees  
are interpretable models.  
That's why they are still fairly popular.  
They were always easy to use.  
But they are not very powerful in terms of modeling.  
Ensemble models, like random forests and XGBoost,  
that you have probably seen in other modules are more accurate.  
But they are ensemble of decision trees.  
And they work in different ways.  
We're not going to go into details  
about what the differences are between the two.  
But what is important to remember  
is that they are ensembles of many different trees.  
So it's much harder to recover why a prediction was  
made since there are averages or hierarchies of models  
inside each of these ensemble classifiers.  
We define our random forest pipeline,  
and we fit on the training set.  
And we also define our XGBoost pipeline,  
and we also fit on the training set.  
Now let's see how we can get an idea  
about proxies for interpretability  
in these models.  
One way is to extract the feature importances.  
Feature importance ranks variables  
according to how useful and important  
they are for prediction.  
This is a global explanation.  
Global means that it describes the model behavior  
across all samples.  
It is not input specific.  
For example, for the random forest, after we run the model,  
we can access the feature importances  
very easily using this feature importances quantity.  
And we can print a data frame that shows the feature  
name and the importance.  
Roughly, the feature importance is  
computed in the following way.  
For each feature, every time the feature is used in a split,  
we measure how much the split reduces the impurity,  
so how much it improves the prediction in some sense.  
So we sum these impurity reductions  
across all of the trees for each feature.  
And then we normalize the values so they add up to 1\.  
And this results in mean decrease in impurity.  
And of course, the higher the value, the more informative  
the feature is across all of the trees of the model.  
Here, for the random forest, the most important feature  
appears to be age, second, marital status, and third,  
the education number.  
What's interesting is that across all the models,  
we won't get the same top features  
in terms of how informative they are,  
which is interesting because they don't all  
work in the same way.  
So they might reveal different important factors  
based on each model's way of being trained.  
A problem that arises with these feature importances,  
for example, for random forest, is that, OK,  
we show which feature is important.  
But how does this feature contribute  
its important, and what's the direction of influence?  
If the age is large, does this contribute  
to a higher probability of having  
a large income or a lower?  
We assume, based on what we've seen  
with the rest of the models, that it must  
lead to higher probability.  
But feature importances do not show that.  
And, actually, this example is very intuitive,  
so we kind of expect how each feature would contribute.  
But it's not always the case when  
we are dealing with more complex data sets.  
So this is a limitation of the feature importance part.  
Now a very useful explainability tool  
that is used a lot with XGBoost models is the SHAP values.  
SHAP stands for Shapley additive explanations  
and basically assigns each feature  
a value representing how much it contributes  
to a given prediction.  
It's fairly complicated to calculate the SHAP value.  
But the intuition behind it is that for each feature,  
we consider all possible combinations of other features  
and ask how much adding the feature changes the prediction.  
And we average this contribution across all the combinations.  
We are going to see how we visualize the SHAP values  
and how we can read the plot.  
But basically, the idea is that on the y-axis,  
we have the features sorted by importance.  
And in the x-axis, we have the SHAP value.  
A positive SHAP value corresponds  
to pushing the model toward predicting the positive class,  
and the negative SHAP value pushes the model  
towards the negative class.  
And the color is also important here for the original feature  
value.  
Red means that the feature has a high value.  
And blue, it means that it has a low value.  
I know that it sounds a lot, but we're going to see an example,  
and we can explain how this looks like there.  
This is how the subplot looks like.  
Let's try to decode what's happening here.  
On the y-axis, you can see all of  
the features-- marital status, age,  
education number, et cetera.  
They are ranked in decreasing order of importance.  
So the highest is the one with highest importance as well.  
These blue and red dots that you see here actually correspond  
to the actual sample.  
So each bullet point here is one sample of our data set.  
Now, everything that lies on the right side of the x-axis  
contributes to the model having a positive value,  
having a higher probability of predicting the positive value--  
and on the left, the opposite.  
So marital status, for example, has--  
as a feature, there are a lot of points that contribute  
to towards the right side.  
And this happens-- all these features  
that are here have a high value of the feature.  
So red corresponds to the value of marital status.  
And blue corresponds to the value of marital status.  
So this tells us that these samples here  
had a high marital status value because they are red.  
And high marital status value is mapped  
on the right side of the x-axis, which means  
that it contributes positively.  
So a high marital status contributes positively.  
High marital status is equal to 1  
now-- contributes positively to the final prediction being 1,  
being high.  
On the other hand, there are a lot  
of samples that go towards the negative side, towards 0\.  
And all of these samples have a low value of marital status.  
So this means that when marital status is 0,  
this tends to mean that the prediction is going to be 0\.  
Similarly here, for example, education number--  
all the samples that are on the right side  
that push towards the prediction equals 1 have high values.  
So high education number means higher probability  
of predicting 1\.  
Low education number means higher probability  
of predicting class 0\.  
So this is the way of reading this diagram.  
And what's good about SHAP values  
is that you can see not just which feature is most important  
but also what's the direction of contribution,  
unlike the feature importances.  
Because here, we saw not just that the marital status  
is the most important feature, but that the marital status  
leads to higher prediction of class 1\.  
Last thing about SHAP values is that they constitute  
a local explainability method because we are looking  
at each point separately, where exactly it lies,  
and how important each part of this point is.  
But since then we can visualize across all of the points what  
happens, this reveals also some more global sense  
of interpretability, of explainability,  
some global understanding of how features contribute on average  
to the final predictions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.3 Explainability in Image Data  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: This is all for the tabular part of this recitation.  
And now we're moving on to image interpretability.  
So as you might have seen in other modules as well,  
deep learning models for images, like convolutional neural  
networks, learn patterns, such as edges, textures, colors,  
object, shapes.  
But even though they're very accurate and efficient,  
it is not always obvious why a CNN  
makes a particular transaction.  
And it's actually mostly not obvious.  
So we are going to see here different methodologies that  
have been developed that try to explain which  
parts of the images are more important when we want  
to predict a certain value.  
So we're going to explore three different methods.  
The first is saliency maps.  
Saliency maps answer the question,  
which pixels matter most?  
So basically, they highlight the pixels of the original image  
that the model is most sensitive to.  
And how do we do that?  
They basically work by computing the gradient of the model's  
output with respect to each pixel.  
And then, what does this show?  
The gradient, if the gradient is high,  
it means that we get a bright area in the saliency map.  
And this means that small pixel changes strongly  
affect the prediction.  
So these pixels are important.  
When the saliency map is dark, it  
means that the gradient was small.  
So it has little influence.  
So basically, when the output of the model  
has a high gradient with respect to a certain pixel,  
it means that if this pixel changes by a little bit,  
the output will still be significantly impacted.  
And this means that this pixel is important.  
Whereas, if the gradient is low, it  
means that even larger changes in the pixel value  
will not have such a big impact on the model output.  
The second method is called LIME.  
LIME stands for Local Interpretable Model-Agnostic  
Explanations.  
So basically, this can be also used for language,  
and we are going to see that later in this recitation.  
So that's what it means to be model agnostic.  
It's not tailored to a certain architecture.  
Basically, the idea-- and it's the same idea  
that is also applied for language--  
is that here for images, we break the image into what  
we call super pixels that are small connected regions.  
Think about it not as separate individual pixels  
of the image but groups of connected small regions  
of the connected pixels.  
Next, we are randomly hiding or masking these regions,  
and we are seeing how the prediction changes  
when certain regions disappear.  
And then we fit another surrogate model  
to identify which regions were important.  
So basically, we have a relationship  
between the regions that we have hidden  
and how the prediction changes.  
So then we can use these hidden regions as input  
and train a surrogate, a completely different model,  
to learn which features led to the highest  
changes in the output.  
And in that way, we basically use a meta learner  
to get some patterns of which hidden regions were  
the most important and resulted in the biggest difference  
when they were hidden.  
It basically answers the question  
if I remove this region, does the prediction  
change significantly?  
So this eventually produces an intuitive heatmap  
of important image regions or areas of the regions  
that end up being important.  
The third method that we're going to explore  
is called Grad-CAM.  
This stands for Gradient-weighted Class  
Activation Mapping.  
And it is basically answering the question,  
where does the CNN look?  
So you don't need to know how CNN works.  
But basically, what this does is that it  
uses the final convolutional feature maps, which  
means it uses some output of the intermediate outputs of the CNN  
model, internal, let's say, quantize,  
but towards the end of the architecture,  
towards the output of the architecture.  
And it also used their gradients to identify now  
which spatial locations contribute most  
to the predicted class and which regions the model  
pays more attention to when making a decision.  
So now we're not looking at individual pixels  
like we did with the saliency maps,  
but this is a bit different.  
When we have bright red regions, we  
have high importance, blue regions we have low importance.  
But basically, the result is a localized heat map  
that we overlay on the original image.  
And this heat map tells us which parts the model  
gave more attention to based on the final layers of the model  
and their gradients.  
So what we're going to do is that we're  
going to use a pretrained large convolutional neural network.  
It is trained on a specific data set,  
and we are going to classify a dog image.  
And after doing this classification,  
we are going to explore the three interpretability methods  
we talked about, saliency maps on individual pixels,  
LIME score for meaningful regions,  
and Grad-CAM for the model's high-level spatial attention.  
And we're going to see which parts are considered important  
based on each of these three methods  
when the model made the prediction.  
It's a single prediction, single model.  
We're just trying to explain it using three different methods.  
So we are loading the libraries that we  
are going to use for this part.  
We are loading the pretrained ResNet50 model here.  
We load it from the torchvision library.  
This is the model here.  
And then the next thing is that we download the image  
we are going to work on.  
It's a publicly available image.  
It's an image of a dog, as you can see.  
We download it, and then we resize it  
so that it's more manageable.  
And the inference and everything happens fast.  
So it's an easy image.  
It's a dog.  
It's easy to recognize.  
We are going to define this preprocess pipeline here,  
where we basically resize.  
Here we resized for visualization purposes.  
But we are resizing the image.  
And notice that here we resized the NumPy version of the image.  
The input to the preprocess pipeline  
will be this version of the image  
here that we loaded, that we haven't resized.  
So that's why we are resizing it here.  
It's not applied again, basically.  
We transform it to tensor, which is important for the model.  
And then we normalize it so that we  
don't have very high values in our features.  
These are all very standard in computer vision.  
So we are preprocessing the image.  
We're getting the tensor.  
And then we are passing this image, this tensor,  
through our pretrained ResNet model.  
And at the end, we get the probabilities of the classes,  
and we get the output probability.  
We don't care if this is correct or not right now,  
but the predicted class had number 258\.  
Now, let's see how we can calculate the saliency map.  
So for this specific class that the model predicted,  
what was the most important thing on the image that--  
yeah, it was important for the model  
to make the prediction according to the saliency maps.  
We are basically taking the gradients here,  
as we said earlier.  
This is very simple.  
It's just the back propagation gradient.  
We are normalizing between 0 and 1\.  
And we are now going to show the resized image, the saliency map.  
And then we can overlay the saliency map  
on the image to see which parts light up,  
which parts are brighter compared  
to our exact initial image.  
So what do we see?  
We see that, actually, what was the most important  
for the prediction was the shape of our dog.  
See?  
Here you can see the body of our dog on these red dots.  
Red dots means that these had higher gradients,  
so they were more important when we classified.  
The background, the grass here, was not  
important for this classification  
to be made by the model.  
And here in the overlay, you can see  
how nicely the different regions of the dog bright up.  
Now, moving on to the LIME explanation,  
here we are loading the explainer.  
We're creating the explainer.  
We are going to basically use these LIME predict  
function, where we take as input the images.  
We preprocess them.  
We have these batches of all the images.  
And what happens is that basically--  
yeah, all these images will be variations of the original image  
when we hide different parts, when  
we had different parts of the initial image.  
That's why we have a for loop here.  
That's why there are multiple images.  
And then we get the probabilities  
for all these different variations.  
So this is how we use the-- we initialize the explainer,  
use this explain instance function, which takes as input  
the original image.  
The LIME predict function, we are  
taking the top label, the 258\.  
So that's what we're trying to explain.  
We're taking the probabilities with respect to this.  
And we also define how many samples we want it to generate.  
So let's see.  
After applying the LIME score, you  
can see with yellow these closed regions here  
that seem to be the most important.  
And as you can see, these regions  
focus on parts of the body of the dog, this part that  
focuses on the tail.  
There is this part that focuses on the body and the mouth.  
And here we also have the eyes, the ear.  
So again, we can see the parts of the dog  
were the most important for making the classification, which  
intuitively makes sense.  
Finally, we're going to see the Grad-CAM interpretability  
method.  
We don't need to spend too much time on how the code works  
exactly, but the idea is that we get the forward  
and backward, basically, parts in some sense,  
hooks-- we call it hooks-- of the target layer.  
And then we take the activations and the grads and the weights,  
and we compute, eventually, this final score.  
And we can visualize it here.  
That's all you need to remember.  
We can visualize it.  
And as we said, red regions correspond to high importance,  
green to less, and blue to even less.  
So as you can see, especially when  
we overlay this map, that heatmap on our original image,  
all this background, this dark blue, is not important at all.  
Again, the silhouette of the dog seems to get the lighter blue.  
And in the middle, we see that the highest importance  
lies around here.  
That's all for the images.  
So we saw these three methods.  
There's no good or bad method.  
There's just different ways of trying  
to explain which parts were the most important for the model.  
And although the details, for example, this area here,  
was not necessarily found by the other methods, the general idea  
that the silhouette of the dog is the most important  
for reaching the final class, it looks consistent  
and makes sense.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.4 Explainability in Language Data  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now for the third and last section  
of the recitation, we're going to take  
a brief look at how language interpretability looks like.  
So we will take a look at attention heatmaps  
and lime for text.  
We're going to use the DistilBERT model.  
This is a BERT type of model.  
It's small and which we did on purpose for educational reasons  
here.  
And we are going to take this input sentence.  
I absolutely loved the cinematography,  
but the plot was terrible.  
We are going to tokenize this sentence.  
So basically, break this sentence  
into smaller words or subwords that  
maps these parts in certain IDs that are readable by the model.  
We pass the inputs through the model we have already loaded,  
and in the output, we get probabilities  
about the sentiment that we are predicting.  
So basically, after loading the model,  
we want to see-- we will run an example  
sentence through the model.  
And we want to see if it's classified  
as a positive or a negative sentiment.  
The sentence is, I absolutely loved the cinematography,  
but the plot was terrible.  
So we take the sentence.  
We pass it through our tokenizer, which basically  
breaks the sentence into smaller subwords  
and maps them to some IDs that are readable by our model  
that we have already loaded.  
And then at the output of this model,  
we get the probabilities of it being a positive  
or a negative sentiment.  
As we can see, the model is pretty confident,  
and we're going to see where it is exactly confident.  
But for now, we are going to visualize these attention  
maps that basically shows what?  
They show for each anchor word, which  
corresponds to the rows here, which of the other words,  
are the most important.  
For example, let's take this word here, was.  
This word, if we take it horizontally,  
has the highest attention weight in the word but.  
So it looks like the model cares a lot.  
It looks like the word was, its representation is affected  
inside the model a lot by the word  
but, which makes sense because but is what introduces  
the change in the tone.  
The first part is more positive and the second is more negative.  
And in general, all the words of the second sentence  
seem to attend to the word but a lot.  
For the first part of the sentence, most of the words  
seem to attend to the word love.  
So cinematography, it looks like the most important again  
is the word love, which makes sense because what did we love?  
We loved the cinematography.  
So that's how we can read the heatmap.  
The higher the value, the higher the weight  
the anchor word the row gives to a certain other word.  
The last column is very bright because--  
and this is the separator token.  
This is not as intuitive and not good  
for our educational purposes.  
But this is how attention works inside the model.  
We can still do visualize the left part of the table  
and try to get an idea of which parts, which combinations,  
which pairs of words seemed to be kind of connected.  
Was, for example, was connected to but.  
As we said, terrible, also connected to but, et cetera.  
And also, we can visualize this in different layers  
in different parts of the network.  
Here, we visualized a heat map that's around--  
it's internal.  
It's around the middle layer.  
And finally, for lime, we already  
explained how lime works for images.  
For text, we are more or less trying  
to answer the same question, which  
is which words change the prediction if we  
remove or change them.  
So we create many perturbed version of the sentence  
like previously we created many perturbed version of the image.  
So words are randomly removed or masked.  
And then we run the model on these modified sentences,  
and we check how the prediction probability changes.  
Afterwards, we fit a simple surrogate model  
like linear regression.  
The input is which words were kept or removed  
as in the images which parts of the image were kept and removed.  
And the output, what we're trying to learn,  
is how the prediction changed when these words were removed.  
And the coefficients, for example  
of this linear regression model tell us  
which words push the prediction positive or negative.  
And then we're going to display this.  
So basically, we are going to say  
that positive words are shown in orange  
and negative words are shown in blue.  
By positive words, we mean that these words seem  
to be the ones pushing towards a positive classification  
and negative were the ones pushing  
towards a negative classification.  
So we initialize our explainer.  
The class names are negative on the left and positive  
on the right, which, as we remember,  
the first number was extremely high.  
So the model predicted that this is  
negative with high confidence.  
We don't care about how good the prediction is right now.  
We just want to see how each word influenced the prediction  
probability, basically.  
So what does this plot show us?  
Terrible and but were the words that  
had the biggest negative contribution,  
and the words loved and absolutely  
were the words with the highest positive contribution, which  
makes sense.  
So I know it's a bit confusing with the negative and positive  
parts, but if we think about it, what does this mean?  
It means that when we removed the terrible word probably,  
we got a much more positive signal, which  
means that the terrible word, when it existed in the sentence,  
was driving the prediction towards the negative part  
more strongly.  
That's why we draw the conclusion  
that terrible was one of the words that contributed  
to the negative prediction.  
And here, you can see again the full sentence  
with the highlighted words in terms of how positive  
and how negative.  
So a darker color means this word was the most important  
in terms of the negative, and this--  
loved was the word that was most important compared to--  
towards positive, which makes sense.  
OK, so this is all for today's recitation.  
Some key takeaways-- different data types  
need different interpretability tools.  
So for tabular data, we took a look  
at coefficients of the logistic regression model.  
We took a look at decision trees,  
which are highly interpretable.  
But we didn't-- yeah, for decision trees that are  
interpretable and also random forests and XGBoost models that  
are not that interpretable, but we took a look at the feature  
importances and the sub values.  
Images-- for images, we explored the saliency maps, lime scores,  
and Grad-CAM.  
And for text, we explored attention maps and lime scores.  
Linear and tree models are easy to interpret--  
logistic regression through the coefficients, decision  
trees, human readable rules.  
And then samples, they have better accuracy,  
but we need sub values for full explanations.  
Sub provides reads global and local insights as we discussed.  
Image methods provide different levels of detail.  
Saliency maps give us the pixel sensitivity.  
Lime gives us important regions, and Grad-CAM through  
the importance--  
grad-cam, through exploring the gradients  
and the last convolutional layers,  
it emphasizes where the model actually looks.  
The language explanations show relationships  
between words, word to word interactions,  
and, through the lime scores, influence of each word  
on the final prediction.  
And yeah, as a general conclusion,  
we should say that interpretability  
is essential for debugging reasons, for us understanding  
how the models work, and most importantly, for trust  
and transparency when they are employed by practitioners.  
And this is actually a big step towards transparent and fair AI.  
Thank you for watching, and good luck  
with the rest of the module.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this recitation, we explored model interpretability across tabular, image, and language data. The goal was not to study how models work, but how to understand why they make certain predictions and why explainability is essential for transparency and trust.

For tabular data (Adult Income dataset), we examined interpretable models like logistic regression and decision trees, and used feature importances and SHAP values to explain ensemble models such as Random Forest and XGBoost.

For images, we applied saliency maps, LIME, and Grad-CAM to visualize which pixels or regions influenced a CNN’s prediction.

For language, we analyzed attention heatmaps and LIME explanations to understand word-level contributions in a sentiment classification example.

Key takeaways:  
Interpretability methods differ across data modalities.  
Linear models and trees are inherently interpretable; ensembles require post-hoc tools like SHAP.  
Saliency maps, LIME, and Grad-CAM highlight important image regions at different levels.  
Attention maps and LIME reveal word influence in text models.  
Explainability supports debugging, fairness, and practitioner trust.  
Congratulations on completing this recitation\! You now understand how interpretability techniques adapt across modalities and why they are critical for responsible AI.  
\`\`\`

Assignment Overview  
\`\`\`  
Skip to main content  
Overview  
Welcome to Assignment 1\! This assignment builds on what we have learned in this module. In particular, we will deepen our understanding of explainability and ethics in AI.

Questions for Part 1 of this Assignment are based on the notebook:

Assignment 1 Part 1 Notebook

The tabular dataset used in this notebook can be found here.

Due to potential memory issues, you are advised to not run this notebook on the server and just review the outputs.

Lectures covered by this assignment

Lecture 1: Explainable AI  
Lecture 4: AI & Fairness  
Good luck\!  
\`\`\`

Skip to main content  
This part practices the core ideas of Explainable AI in different modalities. You will explore how to get insights in models for tabular, images and notes data.

What you'll do:

Train a few models on a heart disease tabular dataset and compare interpretability tools.  
Load a real Rio photo and compute Grad-CAM.  
Use a pretrained text classifier and compute a LIME-style text explanation.  
For the tabular part, we use a classic heart disease dataset collected from patients who underwent clinical evaluation and angiographic assessment. Each row corresponds to one patient, and the task is to predict whether the patient has clinically significant coronary artery disease.

We first train a logistic regression model. Logistic regression serves as a simple, well-understood baseline that produces probabilistic predictions; it produces a coefficient for each input feature after preprocessing. The coefficients provide a global, model-level view of how each feature influences the model’s predictions under the linear assumptions of logistic regression.

Loading…

AskTIM about this problem

Next, we train a shallow decision tree model. The depth of the tree is intentionally limited to keep the resulting structure interpretable.

The visualization of the tree exposes the sequence of decision rules the model uses, which allows us to reason about how different features influence predictions for different subsets of patients.

Decision tree diagram for heart disease classification, showing splits on features such as thal, age, oldpeak, cholesterol, and chest pain, with leaf nodes predicting “Disease” or “No Disease” along with sample counts and Gini impurity values.

Loading…

AskTIM about this problem

Next, we train a Random Forest model, which combines predictions from many decision trees to capture more complex patterns than a single tree.

After training, we examine the model’s global feature importance scores in the notebook. These scores summarize how useful each feature is across the entire ensemble when making splits, providing a high-level view of which inputs the model tends to rely on overall.

Loading…

AskTIM about this problem

We now train a gradient-boosted tree model using the same input features. We use a SHAP-based explanation method designed specifically for tree-based models. SHAP provides a way to attribute parts of a model’s prediction to individual features in a consistent framework.

We first compute SHAP values for the test set, which quantify how each feature contributes to the model’s output relative to a baseline. We then visualize these values using a global summary plot. This plot aggregates information across many test examples and provides a model-level view of which features tend to influence predictions and how their effects vary.

SHAP summary (beeswarm) plot showing feature impact on heart disease prediction, with features ranked by importance on the y-axis and SHAP values on the x-axis; each dot represents a sample, colored from blue (low feature value) to pink (high feature value), indicating how high or low values push the prediction toward or away from disease.

Loading…

AskTIM about this problem

We now focus on one specific test example and examine how the trained XGBoost model arrived at its prediction for that case.

We display the raw feature values for the selected example in the notebook, along with the model’s predicted probability. We then organize the feature-level contributions by their magnitude, highlighting which features had the largest influence on the model’s output for this individual input.

Loading…

AskTIM about this problem

To examine explainability for image-based models, we load an example image of Rio. We apply the Grad-CAM function to the same image for several different predicted classes. For each class, we generate a class-specific activation map and overlay it on the original image.

By holding the input image fixed and varying only the target class, we can observe how the model's internal focus changes depending on which prediction is being evaluated. These are visualized in the notebook.

Loading…

AskTIM about this problem

In this part, we examine how a trained spam classifier explains individual text predictions using LIME.

We evaluate a small set of short messages that range from clearly benign to borderline or spam-like. For each message, we:

Compute the model’s predicted probabilities for the ham and spam classes.  
Use LIME to generate a local explanation for the spam class.  
Visualize which words most influenced the model’s prediction for that specific sentence.  
LIME (Local Interpretable Model-agnostic Explanations) explains a single prediction at a time by perturbing the input (e.g., removing or masking words) and observing how the model’s output changes. It then fits a simple, interpretable model that approximates the classifier’s behavior around that particular sentence, based on how the prediction changes when words are added, removed, or altered.

Key points to keep in mind:

LIME explanations are local, not global.  
They reflect how the model behaved for this sentence, not how it behaves in general.  
Highlighted words indicate influence on the prediction, not causality or real-world intent.  
Loading…

AskTIM about this problem

Loading…

AskTIM about this problem

Skip to main content  
In this section, we explore AI and ethics, focusing on how bias arises in data and models, and how fairness can be defined, measured, and improved through optimization techniques.

Question 1  
0.0/1.0 point (graded)  
A bar exam dataset is defined to be α-biased if the difference in pass rates between Group W and Group B is at least α \= 0.10. In the data, 60% of Group W pass and 45% of Group B pass. Which statement best describes α-bias?

α-bias can only be determined after training a classifier.

The dataset becomes unbiased if we remove race and sex from the features.

The dataset is α-biased because the pass-rate difference (0.15) is at least α \= 0.10

The dataset is not α-biased because both groups took the same exam.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
1 point possible (graded)  
A city wants to justify its predictive policing system by noting that it does not explicitly use race or neighborhood as input features. Based on Lecture 2, why is this reasoning flawed?

Because arrest data is always unbiased

Because fairness only depends on demographic parity

Because correlated variables and feedback loops can still amplify bias

Because the model must include protected attributes to be fair  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
In fairness-aware logistic regression, labels may be flipped using  
Y  
′  
i  
\=Yi(1−2Zi).  
What happens when Zi=1?

The label is flipped (positive → negative or negative → positive).

The label is set to zero, removing its effect on training.

The observation is downweighted rather than changed.

The label remains unchanged, since Y  
′  
i  
\=Yi.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
1 point possible (graded)  
In Lecture 2, label flips are often described as occurring near the decision boundary, meaning among individuals whose predicted outcomes or scores are close to the cutoff between positive and negative decisions. How would this typically appear in the audit tree?

Early splits on protected attributes, followed by random refinement

Splits on variables such as test scores, prior counts, or age at values close to decision thresholds

Splits that mirror the original classifier’s top-level structure exactly

Splits on variables with the largest overall variance in the dataset  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Two students are discussing the COMPAS example from Lecture 2\.  
Student A says: “The model is fair because Black and white defendants have similar false positive rates.”  
Student B says: “The model is fair because Black and white defendants are labeled ‘high risk’ at similar rates.”  
If ε-demographic parity is the fairness criterion being enforced, which student’s reasoning aligns with the lecture?

Neither student, because ε-demographic parity requires identical feature distributions

Student A, because fairness requires calibration within groups

Student B, because ε-demographic parity constrains the rate of positive predictions across groups

Student A, because ε-demographic parity focuses on error rates  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
In this assignment, you practiced the core ideas of Explainable and Fair AI through different questions. You explored how bias arises in datasets and models, and how fairness can be improved using demographic parity and optimization methods. You also reviewed different forms of explanations, across three different modalities (tabular data, images, language).

Key Takeaways:  
Explainable AI: Interpretability is question- and modality-dependent; we need to use the right tool for each model or modality. Also, explanations describe model behavior, not causality.  
Bias & Fairness: Dataset bias, algorithmic bias, and mitigation are distinct; fairness-aware models can flip labels to reduce disparities while balancing meritocracy.  
Ethics: Feedback loops can amplify bias, demographic parity constrains group-level outcomes, and fairness always involves trade-offs.  
Congratulations on completing this assignment\! You now have practical insight into how AI systems can be explained and made more fair and trustworthy, combining technical methods with ethical considerations.  
\`\`\`

Skip to main content  
Module Summary  
In this module, you explored how explainability and fairness are essential components of trustworthy AI systems, helping ensure that machine learning models are transparent, accountable, and aligned with societal values.

Lecture 1 introduced the foundations of explainable AI, highlighting why transparency is necessary for trust and adoption. You examined how explanations can describe overall model behavior (global), individual predictions (local), and hypothetical changes that would alter outcomes (counterfactual explanations).

Lecture 2 focused on fairness-aware machine learning, showing how datasets derived from human decisions can contain systemic bias. You learned how fairness metrics such as α-bias and ε-demographic parity quantify disparities across groups and how optimization methods can mitigate bias while preserving predictive performance.

Together, these lectures demonstrated how transparency and fairness complement each other in building responsible AI systems.

Key Takeaways:  
Explain why transparency and interpretability are critical for trustworthy AI.  
Distinguish between global, local, and counterfactual explanations.  
Understand how systemic bias can arise from real-world datasets.  
Define fairness metrics used to measure disparities across demographic groups.  
Describe optimization-based approaches for mitigating bias while maintaining predictive accuracy.  
Congratulations on completing this module\! With these foundations, you are prepared to critically evaluate AI systems—not only for their predictive performance, but also for their transparency, fairness, and societal impact.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.  
\`\`\`

