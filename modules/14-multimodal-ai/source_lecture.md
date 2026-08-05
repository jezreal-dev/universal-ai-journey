Multimodal AI  
\`\`\`  
Module Overview  
Similarly, there's been great progress in AI for health care.  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
And welcome to this four-part lecture series on multimodal AI  
taught by myself, Paul Liang and Dimitris Bertsimas.  
The world around us is multimodal.  
And despite great progress in artificial intelligence,  
most of our best AI systems today  
still only perceive a very narrow slice  
of this full multimodal world.  
For example, ChatGPT and these large language models  
are great at understanding the words that we speak  
or type onto a computer.  
But these systems don't also understand  
our vocal expressions, such as shouting or laughing.  
Our facial expressions, such as smiling.  
And our body language, as we communicate  
with other people around us.  
Similarly, there's been great progress in AI for health care.  
These AI systems are able to look at X-ray images  
and help doctors diagnose the type of diseases  
the patients may have from looking at these X-ray images.  
However, we know that doctors use a wealth of information  
to make predictions.  
They might call for more detailed lab  
tests about a certain organ in the patient's body.  
They might put these patients under various forms  
of medical sensors to track their ratings across time.  
And, of course, they use all sorts  
of wearables and mobile data to track their patients  
on a day-to-day basis outside a doctor's office.  
Multimodal AI is all about learning and processing  
all these diverse forms of data in the world,  
fusing them to make more accurate predictions.  
Multimodal AI can have many great benefits.  
In the physical world, for example,  
there are so many sensory modalities  
that can inform an agent how they should  
behave within this world.  
Let me give an example for robotics.  
There are lots of people, including  
some of my collaborators, who are  
working on robot arms that have multiple sensors attached  
to them.  
This robot could have a force sensor  
and that tells you the force of grasping and picking up  
an object.  
At the same time, robots often have camera sensors  
that allow them to see the world through different colors  
and orientations.  
The good thing about having multiple sensors on robots  
is that now these robots are more  
robust in the face of imperfections in either sensor.  
You could start pushing these robot arms,  
messing up their force to simulate something  
like an earthquake.  
And the robot should rely on their cameras to solve the task.  
Likewise, you can occlude the robot's cameras with a folder  
to simulate rain or fog and other occlusions  
and the robot should then rely on force to solve the task.  
Therefore, having multiple modalities on a robot  
can make them much more robust in the face of imperfections  
in either sensor.  
Some of the research in our group  
is also extending the sensors that these AI  
systems can currently take in.  
Smell is a particularly interesting and important sensor  
for us humans.  
It allows us to smell things that taste good and also smell  
the presence of dangers.  
Can we imbue this same sense of smell  
into AI systems to make them more multimodal in nature?  
In this video on the right, we're  
showing an example of a chip that  
is able to capture gases in the atmosphere, therefore,  
enabling, these AI systems to smell  
via the gases released by different foods and beverages.  
We've programmed the system, for example,  
to smell the presence of peanuts.  
If this sensor is brought close to a chocolate  
bar or a jar of peanut butter, it  
can actually smell from the gases released by the food.  
Whether there are peanuts within this substance,  
which can be very beneficial when  
someone who is allergic to peanuts  
is detecting whether there's peanuts in their food.  
Another great application of multimodal AI  
is in the medical world.  
There are so many sensory modalities  
that holistically come together to indicate a person's health  
and well-being.  
In the area of physical health, various indicators,  
like computer vision, can be used  
to track the status of patients in the ICU,  
whether these patients are lying down,  
whether they're standing up, whether they're actually  
getting the assistance that they need from doctors and nurses.  
This kind of computer vision, along with other sensors that  
are attached to these ICU patients,  
can really relieve the stress and attention that doctors  
and nurses have to track the patients 24/7.  
Another big application of multimodal AI  
is in understanding the emotional well-being  
of patients.  
Mental health is becoming a disaster nowadays  
in the United States.  
And there's various modalities that  
can be used to track the daily mood of patients,  
especially those who are at risk of depression  
or going into mental health disorders.  
These modalities can include many things,  
such as those on the smartphone, including  
what applications that people are using, whether they're  
being where they're bringing the smartphones to,  
and whether typing on these the smartphones.  
And, finally, multimodal AI is also a great indicator  
of our social wellness, enabling us to understand  
how will we interact socially with other people  
through the words that we say, our vocal expressions,  
and our facial expressions, and body language that we're  
using communicating in groups.  
So in this four part lecture series,  
the goal is to really appreciate that multimodal problems are  
everywhere.  
They're in understanding human communication  
through, both verbal and nonverbal communication.  
There's lots of multimodal systems being  
used to control physical systems, such as robots  
and manufacturing pipelines across multiple sensors.  
They're used in analyzing all forms of medical data  
to make more robust and accurate predictions.  
And they can even be used to monitor the climate  
and environment through all sorts of weather  
and environmental sensors.  
In this first lecture, we're going to dive  
into introduction on the basics of multimodal data models  
and core challenges.  
We're going to look at what makes multimodal data unique as  
compared to machine learning problems  
that only look at a single data source, a single modality.  
We're going to cover at a high level overview, different forms  
of multimodal models and core challenges in multimodal AI  
that need to be tackled in the future.  
In the second lecture, we're going to dive deep  
into multimodal fusion for health care applications.  
We're going to look at how various medical indicators can  
be brought together using AI systems to help doctors  
make more accurate predictions on their patients.  
In lecture 3, we're going to again look at multimodal fusion  
through a lens of a different applications  
by looking at the climate and the environment,  
looking at what sensory indicators there are,  
and, again, how these can be brought together  
to better track the environment and potentially  
even tackle climate change.  
And finally, in the fourth lecture,  
we're going to cover some recent advances  
in building large multimodal models and large generative  
models of multimodal data.  
End of transcript. Skip to the start.  
\`\`\`

Overview  
\`\`\`  
Welcome to Multimodal AI\!

In this module, you’ll learn how combining data types — images, text, time series, audio, and more — enables AI systems to capture richer patterns and make stronger predictions.

You’ll start with the foundations: what counts as a modality, why multimodal data is unique, and the six core challenges of representation, alignment, reasoning, generation, transference, and quantification.

From there, you’ll explore applications. In healthcare, you’ll see how the HAIM framework unites electronic health records (EHRs), notes, labs, and images to improve predictions, and how multimodal multitask learning leverages shared signals across outcomes with structured attention for interpretability. You’ll also study large multimodal models, which extend language models to handle vision, audio, and video, powering text-to-image generation and retrieval-augmented reasoning.

Beyond medicine, you’ll see multimodal AI applied to hurricane forecasting, where satellite, radar, and tabular features are fused to enhance storm prediction.

By the end, you’ll see how multimodal AI generalizes across domains — from hospitals to hurricanes — wherever diverse data must be understood together.

Learning Goals  
By the end of this module, learners will be able to:

Define what a modality is and describe the unique properties of multimodal data, including heterogeneity, connections, and interactions.  
Describehow embeddings transform diverse inputs (EHRs, text, images, time series) into numerical representations and how fusion combines them.  
Compare traditional single-task models with multitask approaches and explain how shared signals across outcomes improve predictions.  
Interpret structured attention as a way to balance knowledge sharing and interpretability across tasks.  
Analyze how large multimodal models extend language models with adapters, cross-attention, and generative methods to handle images, audio, and video.  
Evaluate real-world applications of multimodal AI in healthcare, climate forecasting, and beyond, and discuss their broader societal and operational impact.  
\`\`\`

Lecture 1: Introduction to Multimodal AI  
\`\`\`  
Overview and Learning Objectives  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 1: Introduction to Multimodal AI, taught by Professor Paul Pu Liang, Assistant Professor at the MIT Media Lab and the Department of Electrical Engineering and Computer Science.

What do reading lips in a noisy café, diagnosing disease from scans and notes, and making a meme with text and images all have in common? They all rely on multimodal AI — systems that learn from multiple kinds of data at once.

This unit introduces the foundations of multimodal AI:

From psychology to deep learning: Research evolved from studying gestures and speech together, through computational and interaction eras, to today’s large-scale deep learning models.  
What is a modality? A way of expressing or sensing the world — from raw signals like audio or pixels, to abstract features like sentiment or object labels.  
Three key ideas: Heterogeneity (modalities differ), connections (they overlap), and interactions (they combine in unique ways like redundancy, complementarity, or sarcasm).  
Six core challenges: Representation, alignment, reasoning, generation, transference, and quantification.  
Why it matters: Tackling these challenges powers advances in healthcare, climate science, and generative AI, bringing us closer to systems that understand the world as humans do.  
The impact? Multimodal AI transforms diverse data into intelligence — making AI more natural, versatile, and powerful.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define a modality and explain the difference between raw and abstract modalities.  
Describe what makes multimodal b unique through the ideas of heterogeneity, connections, and interactions.  
Summarize the historical eras of multimodal AI: behavioral, computational, interaction, and deep learning.  
Identify the six core challenges of multimodal AI: representation, alignment, reasoning, generation, transference, and quantification.  
Recognize real-world applications where multimodal AI provides advantages, such as healthcare, climate analysis, and generative AI.  
\`\`\`

L1.1 The History of Multimodal AI  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let me first start  
with a historical perspective on multimodal AI.  
The rise of multimodal AI really started in the 1970s with  
seminal work by psychologists, in particular,  
and a psychologist called David McNeill at the University  
of Chicago.  
David McNeill was the first person  
to study how language and gestures come together  
to bring about higher order understanding  
of human communication.  
So David McNeill "gestures are in effect the speaker's thought  
in action, and an integral component of speech,  
not merely just an accompaniment or addition to speech."  
To illustrate this phenomena, let me show you two short video  
clips.  
I want you to take a look at these two video clips  
carefully and tell me what is the difference between them.  
So here's the first video clip.  
\[VIDEO PLAYBACK\]  
\- Ba, ba, ba.  
Ba, ba, ba.  
\[END PLAYBACK\]  
PAUL LIANG: OK.  
And here's the second video clip.  
\[VIDEO PLAYBACK\]  
\- Ba, ba, ba.  
Ba, ba, ba.  
\[END PLAYBACK\]  
PAUL LIANG: So what is interesting between these two  
video clips?  
Well, most of you should be able to realize  
that, in fact, in these two video clips,  
the audio was exactly the same.  
And the only thing that changed across these two video clips  
was the movement of the speaker's mouth.  
In the first video clip, the speaker  
was making ba, ba, ba, with a B. And in the second video clip,  
the speaker was making fa, fa, fa, with an F.  
Given the exact same audio clip, just  
by looking at how the speaker's mouth changed,  
we actually perceive them as having two different sounds.  
And this was really seminal at that time.  
A ton of people were working on speech recognition,  
trying to give audio of speech to a computer  
and asking the computer to recognize what the person was  
saying in the speech.  
And this experiment demonstrated that instead of approaching  
speech recognition from a speech- and audio-only problem,  
we should be approaching it from an audio-visual problem, where  
you contextualize the speech of what the person is  
saying with how their mouth is moving from computer vision.  
And this really kickstarted an era of methods  
on audio-visual speech recognition.  
One of the earliest demonstrations  
of multimodal machine learning in action.  
And that was the first era of multimodal research,  
the behavioral era, where a lot of studies in multimodal AI  
were inspired by how humans communicate and interact  
with each other through multiple modalities.  
After the behavioral era came the computational era.  
From the late 1980s to the early 2000s,  
there was lots of attempts to build AI systems that could  
replicate the behavioral multimodal demonstrations  
in humans.  
After the computational era came the interaction era.  
Now that we've built a single computer system that  
could understand humans and their multimodal behaviors,  
can we build interactive systems that could actually  
go back and forth--  
communicate with humans, understand  
humans, and back and forth.  
And, finally, in the 2010s until now is a deep learning era,  
enabled by massive data sets, large models,  
and efficient GPU compute, allowing people to train  
extremely large multimodal models that are much more  
performant in nature.  
And especially since the 2010s we've come into this foundation  
model era where these deep learning models can be trained  
in a general purpose manner across massive data sets before  
fine-tuning and specialized for individual tasks.  
Now, most of this lecture is going  
to focus on the deep learning era, looking at recent advances  
and revolutions in multimodal AI through the lens  
of deep learning.  
Now, a lot of this course is based on his recent survey  
paper and this full course that we teach CMU  
and now that I'm teaching at MIT.  
This survey paper is called "Foundations and Recent Trends  
in Multimodal Machine Learning" and really dives deep  
into the individual models and challenges referenced in this  
course.  
End of transcript. Skip to the start.  
\`\`\`

L1.2 What is Multimodal AI?  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's start with an introduction  
to multimodal AI.  
And if we're talking about multimodal AI,  
let me explain what a modality is.  
So modality refers to a way in which something is expressed  
or perceived in the world.  
And usually, when we look at modalities,  
there is often a sensor that captures this modality  
and digitizes it onto our computers.  
We can think of modalities as a spectrum,  
from raw modalities that are closer to a sensor,  
to abstract modalities that are further away,  
that have undergone more processing from the raw data  
collected from a sensor.  
Raw modalities include the speech signal that is currently  
being picked up on the microphone,  
or images that are taken from a camera.  
From a speech signal, we can extract the specific words  
that I'm saying by using speech recognition.  
And this language, therefore, becomes a more abstract  
modality, capturing the most important words  
while removing other speech artifacts.  
From images, we can start detecting objects in the image.  
And again, that's one level of abstraction  
away from the raw image.  
And finally, from the language, you  
can even detect the sentiment-- how happy or sad  
I might be when speaking.  
From these detected objects, we can  
extract the specific categories of what objects  
they are in the image.  
And these are now more abstract modalities because now you're  
just looking at a particular value,  
such as positive or negative sentiment,  
instead of the raw speech signal itself.  
So modality refers to a way in which something is expressed  
or perceived in the world.  
Multimodal, therefore, refers to problems  
involving multiple modalities.  
And something really interesting happens when multiple modalities  
are brought together.  
When different modalities are brought together,  
they're often heterogeneous in nature.  
The modalities are all very different from each other,  
each having their own unique characteristics  
and representations.  
And at the same time, these modalities,  
despite being very different, they're often interconnected.  
They share some connected and interacting information.  
And this is what makes multimodal unique--  
the fact that we are bringing very heterogeneous data while,  
at the same time, data that shows connections  
and interactions with each other.  
So I'm going to dive into these three terms in detail.  
And these three terms are what makes multimodal AI  
unique and special.  
Firstly, the idea of heterogeneity.  
If I have two modalities, I often  
want to think of them as a spectrum,  
describing how the information in these different modalities  
are diverse in their qualities, structures, and representations.  
So this spectrum will span from homogeneous modalities that  
are more similar in nature to heterogeneous modalities that  
are very diverse in nature.  
Homogeneous modalities might be images  
from two different cameras, one from the front  
and one from the side.  
At a high level, they're both imaging modalities.  
They contain the same qualities of images,  
but they capture slightly different information  
because they give you different orientations  
of the object of interest.  
Something that is more heterogeneous  
could be text from two different languages,  
such as English and French.  
Different languages have their own structure and grammar,  
but at the same time, they can often  
be translated back and forth with each other,  
so they capture roughly the same information.  
Something that could be even more different  
could be language and vision, such as words  
describing an image.  
Now we have fundamentally different modalities  
with fundamentally different information.  
And you could go even more heterogeneous,  
such as language and a GPS sensor,  
becoming very different in nature.  
One key idea is that abstract modalities are  
more likely to be homogeneous.  
Whereas if you have raw data, the data  
is very different in nature, if you  
start abstracting and learning representations and learning  
meaning from these modalities, you now  
have an opportunity to bring them more homogeneous and more  
closer together with each other.  
So that's the first key idea of multimodal-- the fact  
that data from different modalities  
are different and show different qualities, structures,  
and representations.  
Despite these differences, the second key idea  
of multimodal data is that they often show some connections.  
This describes a shared information  
that relates modalities with each other.  
So this idea of shared information  
is in contrast to unique information  
that is only present in one modality  
and not present in the other.  
And again, you want to think of connections as a spectrum.  
There are pairs of modalities which  
are stronger in connections, there  
are modalities which are weaker, and there are also  
pairs of modalities that are unconnected, completely  
distinct from each other.  
So again, you're going to use a very simple example  
to demonstrate this.  
You might have this image.  
And oftentimes, images that you see on the internet  
come with some caption.  
This caption could be "A blue book on top of a table beside  
a sofa."  
Of course, these two modalities are pretty connected  
with each other.  
Purpose of the caption is to describe the image.  
But at the same time, there's a ton  
of information in the image that is not described in the caption.  
The fact that the table is round,  
that it has multiple legs at a weird angle,  
and the fact that there's a glass of flowers  
on top of the table.  
So the second key idea is the fact  
that modalities are connected.  
There is some shared information that  
relates them with each other.  
And finally, the third key idea for multimodal data  
is the fact that they interact with each other.  
Interactions describes the process  
of how modalities combine to provide information for a task.  
So different from connections, which  
just looked at two modalities relating with each other  
without a task, interactions looks  
at the presence of two modalities  
with some task Y they are trying to predict.  
And just to give some examples of interactions,  
one example is redundancy, where there is some common information  
between these two modalities, and it's  
the common information that is also  
critical for predicting the task.  
So one example could be a person saying, "This movie is great\!"  
with a huge smile on their face.  
Both of these indicate that the person likes the movie.  
And together, you're very confident that the person really  
loved the movie.  
Another example of interactions is  
that of uniqueness, where there's  
some unique information in one modality that  
is critical for the task and it isn't present in the other.  
One example could be a person saying,  
"The movie does a good job of developing the characters"  
with mostly neutral facial expressions.  
And out of these, the first modality, language,  
contains the unique information that the person felt slightly  
positive about the movie.  
And the third type of interaction,  
the one that I find the coolest, is  
synergy, where there's some emerging information that  
only arises when you combine the two modalities together.  
One example I'd like to give is when a person says something  
positive, like "Wowwww" but with anger or frustration  
on their face.  
And together, the difference in meaning between these two  
modalities actually indicates that a person  
is being sarcastic.  
So that's an example of synergy, where both modalities must  
be taken together into context to make  
a prediction on the task.  
So that summarizes part 1\.  
The key idea of multimodal AI is the study of heterogeneous  
and interconnected data--  
heterogeneous, because different modalities  
are going to be very different from each other; connections,  
because these two modalities often share some connecting  
and overlapping information; and finally, interactions, the fact  
that these two modalities combine in different ways  
when making some prediction on a downstream task.  
End of transcript. Skip to the start.  
\`\`\`

L1.3 Core Challenges in Multimodal AI  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So in part two of this lecture,  
we're going to look at several basic multimodal models  
and challenges these multimodal models tackle.  
Here's a very high-level schematic for multimodal AI.  
You often have many modalities.  
I'm showing three modalities--  
A, B, and C in this case--  
all of them being heterogeneous.  
So they are different from each other,  
so representing them through different shapes and colors.  
And oftentimes, modalities can have multiple subelements  
to them.  
If modality A is language, for example,  
there might be multiple words that I'm saying in a sentence.  
If modality B is a video, there might be  
multiple frames in the video.  
And likewise for other data modalities  
like audio and time series.  
And we can often represent multimodal AI as a big building  
block that combines all these modalities  
through some processing to output  
either a representation or some label that we're  
trying to predict.  
Now let's open up the black box of multimodal AI.  
I like to think of multimodal AI as consisting  
of six fundamental challenges.  
And different models each tackle different challenges.  
One first challenge and the most basic challenge  
is that of learning representations.  
How can I take data and learn semantic representations that  
reflect the fact that different modalities interact  
with each other?  
Representation is a core building block  
for most multimodal problems.  
So given two modalities A and B, each with multiple elements,  
such as words that you're saying in a sentence or different parts  
of the image, the challenge of representation  
just looks at single elements, one from each modality.  
I'm going to simplify the problem  
and just look at one element in each modality.  
And given these two elements, there  
are several ways of doing representation.  
One way is what we call fusion, where you have these two  
elements, and you're trying to bring them together  
to combine the information between them  
into one representation.  
Another way of doing representation  
is coordination, where given these two elements,  
you learn one representation from each  
and you coordinate them with a similarity function.  
For example, coordinating that a word that I'm saying  
represents some particular object in the image.  
And the third type of representation  
is fission, where you start with two elements, one  
from each modality, and you learn more representations  
than a number of modalities that came in.  
Fission is often useful to discover different subparts  
in your modality, perhaps parts that have common information,  
and also parts that have unique information  
in the first and second modality.  
So that's the first challenge, a basic building block  
of how you represent multimodal data, either by fusing them  
together, by coordinating two separate representations,  
or even doing fission, where you factorize your data into more  
representations.  
So whereas with representation, we just looked at one element  
in each modality, the second challenge  
is alignment, where now we're going  
to look at multiple elements across your modalities.  
The goal of alignment, the second challenge,  
is to identify and model all the connections  
between multiple elements across your different modalities.  
Modeling this alignment is very important  
because most modalities have some internal structure that  
tells you how these multiple elements correspond  
with each other.  
In the image domain, for example, most of this structure  
is spatial.  
We often describe images by saying a book on top of a table  
to the right of a sofa.  
And sometimes in other modalities  
the structure could be hierarchical,  
for example, a tree or a graph.  
The goal of alignment is to capture, for example,  
how this particular book is referenced  
in language through words.  
There are several subchallenges here.  
One subchallenge is the case where your data modalities are  
discrete, in which case can clearly partition your elements  
into discrete steps.  
For example, each word is discrete  
and each object region is also a discrete set.  
In this case, the problem of alignment  
boils down to finding out the matching  
between the different discrete words that you're saying  
and the discrete object regions in the image.  
This is also commonly known as the language grounding problem  
in natural language processing.  
A second challenge extends the first one  
and goes to the continuous space.  
There are often times when we have  
data modalities that are not so clearly partitioned  
into discrete steps.  
This can include continuous data, such as high frequency  
sensors, or audio data.  
So in this case, we have to develop  
methods for continuous alignment that  
enables you to learn the segmentation boundaries that  
converge your continuous data into some discrete boundaries  
before performing alignment with other modalities.  
And finally, while in these two subchallenges,  
the alignment was the end goal in itself,  
a third subchallenge uses alignment to learn  
better representations.  
We call this contextualized representations.  
For example, how can I learn better representations  
of what a person is saying by taking  
into account the alignment between the individual words  
that they're saying with the different facial expressions  
that they're making while saying those words?  
In this case, alignment is implicit.  
It is an intermediate step to learn  
better representations that use the alignment to make  
better predictions.  
Now that we have learned how to represent individual elements  
across modalities and capture their alignment  
between multiple elements across modalities,  
the third challenge is reasoning.  
The goal of reasoning is to combine knowledge, usually  
through multiple inferential steps,  
to exploit the structure of the problem.  
When we think of combining information  
through multiple steps, we often think  
of multiple layers of deep neural networks,  
different layers that progressively  
capture increasingly higher order  
and semantic representations.  
But in many times, reasoning tries  
to do this in a more transparent and understandable way,  
often exploiting the structure of the problem.  
For example, the structure of the problem  
could be something that is a tree structure, where  
certain elements have to be combined first  
before combining other elements later down in the stage.  
The problem might also help if we use explicit representations  
at each layer of reasoning, such as using  
attention maps to focus on different parts of the image.  
And nowadays, with the progress of large language model  
reasoning, there is also an opportunity  
for discrete words and natural language  
to be involved in the reasoning process,  
just like how humans think step-by-step and stage-by-stage.  
And oftentimes, reasoning is impossible without  
some external knowledge.  
External knowledge of the data modalities,  
of the structure of the problem, or the tasks at hand.  
And oftentimes, this external knowledge  
comes from either a human or larger databases  
on the internet.  
Several subchallenges in reasoning.  
One of them is to model the structure of the problem.  
Is the reasoning structure step-by-step or hierarchical?  
Whether I have to fuse certain modalities before  
fusing the other, or perhaps even interactive,  
such as in reinforcement learning.  
What intermediate concepts do I use  
to represent the intermediate stages of reasoning?  
Whether I use neural network representations,  
attention maps, or even use natural language.  
What is the inference paradigm?  
How do I take two elements and infer higher order structures,  
including even using causal reasoning or logical reasoning  
as an intermediate step?  
And finally, what type of external knowledge  
and how I obtain it in an efficient way  
to drive the reasoning structure.  
The fourth challenge is generation.  
Whereas previously we looked at making predictions on a task,  
generation aims to learn a generative process  
to actually produce new raw modalities that reflect  
interactions and structure.  
There are several subchallenges here.  
It's often very important to take  
large amounts of multimodal data and summarize it  
into the most salient parts.  
There's also lots of demand for methods  
that can translate from one data modality to the other.  
For example, taking in a caption that I say  
and generating an image that most  
closely represents that caption.  
And finally, creation.  
How do I take smaller amounts of data,  
such as perhaps the first frame in an image,  
and generate more frames, perhaps even  
generate a whole video based on that starting frame?  
That's creation.  
Challenge five is transference, the idea  
of transferring knowledge between modalities, usually  
to help some target modality which may be noisy  
or with limited resources.  
For example, a doctor might be trying  
to build an AI system that can better  
help them process x-ray images.  
However, we often don't have access to too many x-ray images.  
That's because they're difficult to collect from patients,  
and there often is privacy concerns  
when sharing x-ray images across different hospitals.  
However, we can use different types  
of images, such as those available on the internet,  
to supplement the visual modality.  
In this case, we could develop a system  
that leverages the large amounts of data  
of natural images in modality B to enrich modality  
A, which are x-ray images.  
Several subchallenges here, the first one being  
transfer learning.  
There's lots of demand nowadays for building  
large pre-trained models, for example, of natural images  
or of natural language, and transferring these large models  
to specific downstream tasks which have less data,  
such as medical images or medical text.  
A second way to tackle transference  
is through co-learning.  
In this paradigm, an additional modality  
could be introduced either during training on the input  
side or on the output side.  
In the input side, we call this co-learning via fission.  
And on the output side, we call it co-learning via translation.  
We are trying to additionally predict this other modality  
during training.  
The good thing about co-learning is  
that after this additional modality is introduced  
during training, you can remove it and only  
have inference using the target modality during testing.  
And finally, model induction.  
In this case, you can train two separate models, one  
for the target modality with limited data  
and one for the source modality with lots of data,  
and enforce some constraint between them  
so that information can transfer from the model with more data  
to the model with less.  
The sixth and final challenge is quantification.  
The whole goal of quantification is  
to build a deeper empirical and theoretical study  
to better understand heterogeneity, interactions,  
and the whole multimodal learning process.  
For example, how can we better measure the fact  
that different data modalities are different from each other  
and come up with better methods to learn from very  
different data sources?  
How can we also measure which modalities  
interact with each other in which ways,  
and design better fusion methods to capture these interactions?  
And finally, multimodal learning is not without its challenges.  
There are often challenges where different data modalities  
can learn or overfit at different times.  
How do you build new optimization strategies  
so that we can balance the learning  
from different modalities and keep all the benefits,  
while reducing any drawbacks?  
End of transcript. Skip to the start.  
\`\`\`

L1.4 Multimodal Data, Models, and Challenges  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So these six challenges all come together.  
Given any multi-modal problem, we always  
have to decide how to represent the individual elements  
in your data.  
Am I bringing things together by fusing them?  
Am I aiming to learn separate representations  
but coordinate them together, or am I  
even trying to factorize and learn more representations  
from the data modalities that I started with?  
After representation of these individual  
elements in your modalities comes alignment.  
How do I now account for the fact  
that different modalities often have multiple elements according  
to some structure, such as words that I'm  
saying in a temporal sequence, different image  
regions of an image with some spatial structure?  
And how do I learn the mappings between elements  
from one modality with elements from the other?  
That's the challenge of alignment.  
Given representation and alignment,  
how can we combine this information,  
usually through some principled, multi-step structure,  
to learn predictions for some downstream task?  
This idea of combining information  
through some structure across multiple steps  
is often known as reasoning.  
And the whole goal of reasoning is  
to make this structure more robust and interpretable  
to outside people.  
Sometimes, I don't care about making a prediction on a task,  
and instead, I care about generating  
more data, such as summarizing large amounts of data  
into smaller ones, translating between one data  
modality and the other, or going from smaller data  
to generate more data in a coherent manner.  
And that's the challenge of generation.  
Sometimes, I might also care about making  
predictions in one data modality, but with limited data.  
So how can different data sources that  
have more abundant data help?  
That's the idea of transference.  
And finally, all of this comes together  
with the sixth and final challenge of quantification.  
It is a magnifying glass so that we can better  
empirically and theoretically understand all these properties  
of multimodal data and the models  
that we're building to learn from multimodal data.  
So that summarizes the first lecture.  
There are several key takeaways here.  
Firstly, I want everyone to appreciate  
that multimodal problems are everywhere  
in understanding human communication  
through both verbal and non-verbal channels,  
in analyzing the vast amounts of medical data  
to help doctors make more accurate diagnosis,  
and to track different physical indicators of the climate  
and environment.  
What makes multimodal data unique  
is the fact that they're often heterogeneous,  
and different modalities are different from each other  
in their structures and representations.  
Despite these differences, these data modalities  
often share some connections.  
There's some overlapping shared information between them.  
And these data modalities combine in certain ways  
to bring about more accurate predictions  
when making some prediction for a task.  
A multimodal AI introduces six main challenges--  
the idea of representing your data,  
aligning multiple elements across modalities, reasoning  
in a multi-step and multi-stage manner, generating more data,  
transferring information from high-resource modalities  
to data modalities with less data, and quantification,  
really understanding the multimodal modeling process.  
Identifying the appropriate multimodal challenge  
and the right model to use is critical  
in all multimodal problems.  
And in the next three lectures, we're  
going to dive deep into multimodal fusion for health  
care and climate applications and also  
look at recent advances in large multimodal models  
and generative AI.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
This lecture introduced multimodal AI, tracing its evolution from early behavioral studies of speech and gesture to today's deep learning foundation models, and explained why combining multiple data modalities creates unique modeling challenges and opportunities.

Key Takeaways:  
Historical evolution: Multimodal research moved from the behavioral era (human communication studies like audio-visual speech perception) to computational and interaction systems, and now to the deep learning and foundation model era.  
What is a modality? A modality is a way information is expressed or sensed (e.g., audio, vision, text), ranging from raw signals (pixels, waveforms) to abstract features (objects, sentiment).  
Three defining properties:  
Heterogeneity: Modalities differ in structure and representation.  
Connections: They share overlapping information.  
Interactions: They combine in task-specific ways (redundancy, uniqueness, synergy).  
Six core challenges: Multimodal AI problems revolve around  
Representation (fusion, coordination, fission),  
Alignment (mapping elements across modalities),  
Reasoning (structured multi-step inference),  
Generation (translation, summarization, creation),  
Transference (leveraging high-resource modalities), and  
Quantification (measuring and understanding multimodal learning).  
Central insight: Multimodal AI is powerful because it integrates diverse but interconnected signals—enabling richer understanding and prediction than any single modality alone.  
\`\`\`

Lecture 2: HAIM: Holistic AI for Medicine: An Application of Multimodal AI  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: HAIM: Holistic AI for Medicine: An Application of Multimodal AI, taught by Professor Dimitris Bertsimas, Boeing Leaders for Global Operations Professor of Management and Professor of Operations Research at MIT.

What do reading a chest X-ray, analyzing lab results, and interpreting a doctor’s notes all have in common? They’re all part of the complex decision-making process in medicine — and they can all be brought together through multimodal AI.

This lecture introduces Holistic Artificial Intelligence for Medicine (HAIM):

Why multimodality matters: Just as doctors use scans, notes, labs, and monitoring data together, AI can also combine diverse inputs to make better medical predictions.  
From data to embeddings: Each modality — tabular records, time series, language, and images — is transformed into numerical features or embeddings that can be used in machine learning.  
The power of fusion: By merging these representations, traditional ML models like XGBoost can predict outcomes such as mortality, diagnoses, and length of stay with far greater accuracy.  
Real-world impact: Applied on large datasets like MIMIC-IV and deployed at Hartford HealthCare, HAIM has improved performance by 6–33%, reduced patient stays, and increased hospital efficiency.  
Beyond prediction: HAIM supports diverse applications, from risk of deterioration and ICU admission to emerging use cases like detecting domestic abuse or providing AI clinical companions.  
The impact? By uniting medicine’s many data streams, HAIM demonstrates how multimodal AI can drive better care, smarter resource use, and life-saving insights.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain the motivation for using multimodal AI in medicine and how it mirrors the way doctors integrate multiple data sources.  
Describe the HAIM framework and its approach of transforming diverse inputs (tabular data, time series, language, and images) into numerical embeddings.  
Define the concept of fusion and explain how embeddings from different modalities can be combined for prediction tasks.  
Compare the performance of HAIM with classical models that rely only on electronic health records (EHRs).  
Identify real-world applications of HAIM, including mortality prediction, disease classification, length of stay, and broader healthcare deployments.  
\`\`\`

L2.1 HAIM: Holistic AI for Medicine: An Application of Multimodal AI  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In this lecture, we present  
Holistic Artificial Intelligence for Medicine, or HAIM for short.  
Haim is the Jewish word for life.  
It represents an application of multimodal AI in medicine.  
The outline of the lecture is as follows.  
We first give motivation for using multimodal AI.  
We then present HAIM and apply it  
in a realworld environment at Hartford HealthCare system.  
And finally, we conclude with applications of HAIM  
in several other areas of medicine.  
In order to motivate multimodality,  
let us think how medical doctors make decisions.  
They utilize scans, MRIs, CTs, X-rays, et cetera; language,  
radiology reports, doctors' or nurses' notes;  
tabular data, electronic medical records, for instance;  
time series; and genomic information.  
Given that human doctors use multimodal data,  
it is natural to ask whether machines  
can use multimodal data to make medical diagnoses and decisions.  
Consider the sensors that humans use to understand the world.  
People use the five basic human senses--  
touch, sight, hearing, smell, and taste.  
In other words, multimodality is a fundamental characteristic  
of human life.  
It is therefore natural to consider the question  
whether machines should also be used for multimodal data.  
In this lecture, we present HAIM from the principal findings  
of a 2022 paper entitled, "Integrated Multimodal  
Artificial Intelligence Framework for Healthcare  
Applications that Appeared in Nature Digital Medicine,"  
September 2022 by myself and members of my research group.  
I would like to tell you a bit of the history  
of the conception of HAIM.  
In 2013, IBM created Watson, a computer program that  
could compete in Jeopardy, a game  
that a contestant is given a statement  
and she needs to express the answer  
in the form of a question.  
For example, if the answer is "he developed the theory  
of relativity," the contestant needs to say for a correct  
answer, "who is Albert Einstein?"  
IBM Watson competed with the best human players in history  
over two days, and it won very decisively.  
I remembered an excitement on this event,  
as I knew at the time that this was  
the beginning of an era of propelling machine  
intelligence to the next level.  
IBM proceeded to apply Watson in medicine,  
unfortunately unsuccessfully.  
In the intervening 12 years, artificial intelligence  
has advanced significantly, especially generative AI  
and large language models.  
HAIM shows how to combine various modalities  
to achieve significantly improved performance.  
HAIM presents a holistic perspective of AI--  
computer vision, natural language processing,  
machine learning-- to improve the ability of models  
to make predictions and prescriptions,  
especially in medicine.  
The traditional machine learning paradigm  
is to use tabular data for making predictions.  
When multiple modalities are present,  
like computer vision or language,  
this paradigm does not apply and we  
need to discover different ways of combining data.  
In the next slides, we outline how  
to combine different modalities of data.  
When electronic health data are present,  
like the one shown in the slide, we keep the records as they are,  
as they are in the traditional machine learning format,  
where traditional methods apply.  
When there are time series available,  
we use software like tsfresh--  
you will see now in the recitation--  
to extract features of the time series,  
like the maximum value, the minimum value, the median,  
the mean, the number of peaks, among many others.  
In this way, the time series is summarized in numbers  
that are inputs in a traditional machine learning format.  
When the input are doctor or nurse  
notes or a radiology report, that is language,  
we use a foundational model like ClinicalBERT.  
This summarizes the language information in the format  
of an embedding, a 768-element vector.  
This vector summarizes the information  
in the numerical format that can be combined  
with other numerical features.  
Note that we can use generative AI  
models like OpenAI 4.0 or Llama instead of ClinicalBERT.  
When the input is in an electronic cardiogram,  
we use the language information included in the EKG,  
like language, and then use a foundation model like  
ClinicalBERT, we have seen earlier,  
that summarizes the language information in the format  
of an embedding of a 768-element vector in a numerical format,  
as before.  
When the input is an image like an X-ray,  
we use convolutional neural networks to extract an embedding  
of a 768-element vector in a numerical format.  
Note that we can use embeddings from a generative AI model,  
instead of using images from a CNN model as an alternative.  
This is the critical idea of the lecture.  
We use the numerical features we developed, either directly  
from electronic health care records  
or extracted features from time series or embeddings  
using unstructured data.  
This idea is called fusion.  
We now have a traditional machine learning task.  
We want to predict, say, for example, mortality using  
as inputs the numerical features we extracted,  
as indicated earlier.  
We use a traditional ML model like XGBoost or random forest  
to perform this prediction task.  
Note that the method is very general,  
as we treat each modality independently,  
so that if we add new modalities,  
we just add the additional embeddings.  
Note that we do not train the modalities in combination.  
Note also that the embeddings do not depend  
on the task we want to perform.  
The embeddings just summarize the data  
of each modality independently of the task we want to perform.  
Let us now apply HAIM for various prediction tasks using  
MIMIC-IV data set from the Beth Israel Deaconess Medical  
Center, a hospital system in Boston, Massachusetts.  
The data set of 34,537 patient records are coming from  
the emergency ICU rooms.  
The records include a chest X-ray,  
electronic medical records, radiology notes, and EKG.  
That is, it includes vision, language, and tabular data.  
Our target diagnosis include 12 targets--  
mortality prediction, that is, we  
aim to predict if a patient is deceased or sent to hospice  
or the patient is alive at the hospital discharge; one  
of 10 diagnoses, that is, we want to predict if a patient has  
a certain disease, like fracture, lung lesion, enlarge  
CM, consolidation, pneumonia, \[INAUDIBLE\] classes, lung  
capacity, pneumothorax, edema, cardiomegaly; and finally,  
the length of stay, that is, we want  
to predict if a patient exits the hospital in 48 hours.  
We have compared the performance of HAIM  
and the performance of a classical machine learning model  
that is only based on electronic medical records,  
the classical approach.  
On mortality, HAIM improves the accuracy by 11% to 33%  
compared to electronic medical records.  
That is only based on classical machine learning models.  
On disease classification, HAIM improves the accuracy  
by 6% to 22% compared to electronic records.  
On length of stay, HAIM improves the accuracy by 8% to 20%  
compared to electronic medical records  
and more classical machine learning model.  
In all cases, the use of multimodality  
results in a significant improvement of performance.  
In this slide, we present subanalyses in order  
to understand the relative contribution of each modality  
to the prediction for disease classification.  
The vision input, in this case, the X-ray,  
was the dominant modality.  
For length of stay and mortality,  
the time series and the electronic medical records  
was the dominant modality.  
We next present an application of the HAIM methodology  
to predict length of stay at Hartford Health Care system,  
HHC for short, the largest hospital system in Connecticut,  
with operating revenues above $5 billion a year,  
seven diverse hospitals, ranging from an academic urban hospital  
to a community hospital, and from large to small hospitals.  
Altogether, HHC has a total of 2,500 beds.  
It is representative of a high-quality, typical US  
hospital network.  
We have implemented some of the algorithms we presented  
in a company called Holistic Hospital Optimization,  
H2O for short.  
This is an indication of the connections  
with the fundamental aspect of life, water.  
We discuss in detail the length-of-stay application.  
We have implemented other applications,  
like a deterioration index, that includes mortality risk, ICU  
risk, scheduling nurses, and scheduling operating rooms.  
The software is used by hundreds of users--  
physicians, nurses, administrators.  
It works in all seven hospitals of HHC,  
and has led to an annual revenue uplift in the tens of millions  
of dollars.  
We have implemented these solutions  
to several other hospital systems around the world.  
The applications include predicting  
discharge in the next 24 or 48 hours, which  
is important for identifying and prioritizing patients,  
reduce the length of stay, and save costs,  
prepare for treatment and disposition plans.  
It also predicts the final destination  
after discharge, the mortality risk,  
as well as the risk of needing admission to the intensive care  
unit.  
These predictions help warn of patients' deterioration,  
as well as allocating more effectively hospital resources.  
The table depicts the AUC, the Area Under the Curve,  
for mortality, destination, 24- and 48-hour discharge,  
predicting entering ICU or leaving ICU for all seven  
hospitals at HHC.  
The results are reliably strong across all predictions  
and all hospitals.  
We next demonstrate that the calibration plots are also  
very accurate.  
Specifically, on the left plot in the horizontal axis,  
we plot the proportion of patients that have probability  
of 48-hours discharge between, say, 0.5 and 0.6,  
in increments of 10%, and then plot the proportion of patients  
among those that are discharged within 48 hours in the vertical  
axis.  
The line is very close to the 45-degree angle,  
illustrating that the predicted probabilities closely match  
empirical evidence.  
On the right plot, we saw the calibration plot for mortality.  
Again, calibration is very accurate.  
The figure shows the software that  
has been implemented at HHC.  
The colors demonstrate the following information.  
Green suggests that the patient needs  
to be prioritized for discharge.  
Yellow also indicates that hospital personnel  
needs to prepare, but not with the same level of intensity.  
Red indicates that the patient is deteriorating.  
Note that we assign a green alert  
if the discharge probability in the next 24 hours or 48 hours  
is over 50%.  
The yellow alert happens if the 48-hour discharge probability is  
between 35% and 50%, and the probability increases by over  
10% from the day before.  
The software also plots a subplot  
that shows how different factors affect length of stay.  
This way, the predictions are far more interpretable.  
Compared with human doctors, the artificial intelligence approach  
has significantly higher AUC, identify  
more patients who can be discharged,  
and make more accurate predictions.  
Clearly, the AI edge is significant.  
We have performed a test in which certain wards at HHC  
have used the software and compared it with others  
that did not use it.  
We have found that the average patient  
length of stay for the units that use the software  
reduced by 0.67 days, from 565 to 498 days.  
This suggests that we reduce length  
of stay approximately 15%, and thus we  
can increase the throughput by a corresponding amount,  
thus increasing the overall revenue of the hospital  
by tens of millions annually.  
HAIM is widely applicable in a variety of applications.  
Examples of current work include detecting domestic abuse  
at the Brigham and Women's Hospital, automatic detection  
of data from nodes, scans, and laboratories  
at Mass General Brigham, unified diagnostics for EKG at Hartford  
Hospital, detection of subdural hematoma,  
as well as what is called AI companion.  
We utilize HAIM to give advice to doctors and nurses regarding  
diagnosis.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture introduced Holistic Artificial Intelligence for Medicine (HAIM), a multimodal framework that integrates images, clinical text, time series, and tabular records into a unified prediction system deployed in real hospitals.

Key Takeaways:  
Why multimodal in medicine: Doctors combine scans, notes, labs, and vitals when making decisions—HAIM mirrors this by integrating multiple data modalities instead of relying only on EHR tables.  
Core idea (modular embeddings):  
Tabular data → used directly  
Time series → summarized into statistical features  
Clinical text → foundation-model embeddings (e.g., ClinicalBERT)  
Images (e.g., X-rays) → CNN embeddings. Each modality is converted into numerical features independently.  
Fusion \+ classical ML: All embeddings are concatenated and fed into models like XGBoost or Random Forest. The system is modular and task-agnostic—new modalities can be added easily.  
Empirical gains (MIMIC-IV): Multimodal HAIM significantly outperformed single-modality baselines in mortality prediction, disease classification, and length-of-stay prediction.  
Real-world impact (Hartford HealthCare): Deployment across seven hospitals improved discharge prioritization and deterioration prediction, reduced length of stay, and increased operational efficiency.  
Central insight: Converting heterogeneous medical data into unified embeddings and fusing them into a single predictive pipeline enables measurable clinical and operational improvements at scale.  
\`\`\`

Lecture 3: Multimodal Generative AI  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 3: Multimodal Generative AI, taught by Professor Paul Pu Liang, Assistant Professor at the MIT Media Lab and the Department of Electrical Engineering and Computer Science.

Imagine watching a video where someone rolls their eyes while saying “what a privilege,” diagnosing a tumor from both scans and reports, or asking a computer to draw a bowl of soup that is a portal to another dimension. What do these have in common? They all rely on multimodal AI — systems that combine text, images, audio, and video to capture richer meaning than any single input alone.

This module introduces the foundations of multimodal generative AI:

From single streams to fusion: Just as a neural network stacks perceptrons, multimodal models align words with visual frames, audio tones, or sensor readings, building shared representations across modalities.  
Why cross-attention matters: Like ReLU gave perceptrons new power, cross-attention layers let models contextualize words with eye-rolls or emphasis, capturing subtleties such as sarcasm.  
Teaching old models new tricks: Instead of retraining billions of parameters, adapters and prefix tuning act like small plug-ins that let frozen language models take in images or video, expanding their abilities without starting from scratch.  
Scaling up: From Flamingo to LLaMA-Adapter, researchers extend this idea across languages, vision, and even 3D data, unlocking powerful multimodal capabilities.  
From words to worlds: Text-to-image generation, first with autoencoders and now with diffusion, turns prompts like “a bowl of soup that is a portal to another dimension” into vivid pictures.  
Putting it all together: Modern systems can now take photos of cookies, answer “How should I display these at the market?”, and generate not just advice but actual images of possible layouts.  
The impact? Multimodal AI enables healthcare support, climate monitoring, creative design, and richer human–AI interaction. By the end, you’ll see how today’s breakthroughs in large multimodal models rest on three pillars: fusing different streams of data, teaching frozen LLMs new tricks, and extending them into true multimodal generators.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define multimodal models and explain why combining text, images, audio, video gives richer understanding.  
Describe how cross-attention links modalities (e.g., words \+ expressions) for context such as sarcasm.  
Explain how prefix tuning and adapters extend frozen LLMs to multimodal tasks.  
Summarize large-scale models like Flamingo, MiniGPT-4, LLaMA-Adapter and their alignment \+ instruction tuning.  
Interpret text-to-image generation from autoencoders → diffusion models, turning prompts into images.  
Compare retrieval vs. generation strategies for multimodal outputs, noting trade-offs in realism and flexibility.  
\`\`\`

L3.1 Large Multimodal Models and Multimodal Generation  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Today we're going to be talking  
about multimodal generative AI on large multimodal models  
and multimodal generation.  
So let's recap what we've learned so far  
in this four-part course.  
In the first lecture, we motivated  
how multimodal problems are everywhere  
in understanding human communication  
through both verbal and nonverbal channels,  
in controlling physical systems, and analyzing  
vast amounts of medical data, and monitoring  
different sensors in the climate and the environment.  
In the first lecture, we covered the basics of multimodal data,  
different types of models, and the core challenges  
in multimodal AI.  
We then looked at several applications  
of multimodal fusion, in particular for health  
and also for climate.  
In today's lecture 4, we're going  
to cover recent advances in large multimodal models  
and generative AI.  
So large language models need no introduction.  
Models like ChatGPT train on vast amounts of data  
on the internet and fine-tuned for various downstream natural  
language processing tasks have completely revolutionized AI.  
Given a particular prompt, these models  
are capable of question answering.  
For example, recite the first law of robotics and answering--  
"A robot may not injure a human" and so on.  
These models are also capable of open-ended dialogue.  
You can sustain a conversation with these models  
for a long time and it can still remember things  
that they've said at the beginning of conversations.  
These models are capable of translating languages  
to other languages.  
By augmenting these models with search engines,  
They're able to retrieve real time news  
and commentary on these news.  
They're able to solve math problems and even write code.  
And they're getting increasingly capable in all forms  
of mathematical and advanced reasoning.  
But we're here today to talk about large multimodal models.  
So what are large multimodal models?  
I'm going to give a very simple example to illustrate.  
So this might be a video that I'm interested in.  
\[VIDEO PLAYBACK\]  
\[LAUGHTER\]  
\- It's just a privilege to watch your mind at work.  
\[END PLAYBACK\]  
PAUL LIANG: "It's just a privilege to watch your mind  
at work."  
So, given this video, I might want  
to build a large language model that can both understand words  
and questions that I ask as well as this video, using  
both the content spoken in the video,  
the visual frames in the video, and the audio dialogue  
in the video.  
So I might want to ask this large multimodal model  
a question like, what is the tone  
of the man in the gray shirt?  
He's being sarcastic.  
Describe the relationship between these two people.  
Tell me a story inspired by this short video clip.  
And perhaps even retrieve and play the next episode  
of this TV show.  
Or this jacket that a person is wearing  
looks nice, show me what I would look like if I wore it.  
So as you can see, these large multimodal models  
have to do several things.  
They have to understand the question that you're  
asking these models.  
They have to understand all forms of multimodal data,  
in this case, the language, video,  
and audio in this video clip.  
They have to answer these questions in natural language.  
And sometimes they might even require to generate videos,  
for example, retrieving and playing  
the next episode of these TV show.  
So in this lecture, we're going to learn  
how these large multimodal models are built.  
In the first part, we're going to cover  
how we can learn multimodal temporal representations  
of text, images, video, and audio.  
The predominant modalities that are  
on the internet-- we call them digital modalities  
that today's large multimodal models primarily handle.  
So how do you take in language, that's usually  
spoken in a sequence of words, videos, which is often  
a frame of individual images, and learning  
these temporal representations.  
We call them temporal because we're often  
trying to look at sequences of multiple modalities  
and how these sequential information relates  
with each other.  
How should I represent my language  
by taking into account the frames in the video?  
And, likewise, how can I better represent these videos  
by taking into account the dialogue that these people  
in the videos are speaking.  
So that's part 1\.  
How do you take in lots of multimodal data  
that are temporal in nature and learn  
multimodal representations.  
In part 2, we're going to look at how  
we can use these multimodal representations to adapt  
large language models so that these large language models can  
generate text conditioned on this multimodal data.  
So this enables your model to look at these videos and answer  
questions such as this person is being sarcastic  
or they seem to be close friends,  
given questions from the user.  
And, finally, part 3, we're going  
to go beyond just completing text and answering  
in natural language.  
We'll look at how these systems can also generate data  
in different modalities, how they  
can generate images or generate videos,  
such as retrieving the next episode in this TV show.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.2 Learning Multimodal Temporal Representations  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So, firstly, learning  
multimodal temporal representations  
of various forms of sequential data,  
such as text, images, video, and audio.  
Now, we've already seen that transformers  
and these self-attention in transformers  
are really great at learning representations of language,  
specifically temporal representations of languages  
across multiple sequences.  
And these transformers are basically  
the backbones of many large language models today.  
So a natural way to learn multimodal temporal  
representations is to extend these transformers  
for only language to the multimodal setting.  
In this setting, we now have multiple temporal modalities.  
And the goal is to use transformers  
and their self-attention to learn all the pairwise context  
between one modality and the other.  
Let me show you a very simple example using just two  
modalities and a short context.  
So using again the video that we saw previously,  
person was saying some words like, it's just a privilege  
to watch your mind at work.  
and it might be three words.  
I'm just highlighting "privilege" and "mind,"  
for example.  
The person might also be showing several facial expressions  
and doing vocal emphasis.  
So what these transformers do is that they essentially take  
your sequence of three words, that I've illustrated here,  
and your sequence of four nonverbal expressions, including  
vocal emphasis and eye rolling, and learns what we  
call a cross-attention matrix.  
This cross-attention is vision to language attention  
because the two modalities involved  
are vision and language.  
And this attention matrix is going to be 3 by 4\.  
3 for every 1 of your three words and 4 for every 1  
of your 4 nonverbal expressions.  
What this 3 by 4 matrix captures is a matrix of attention,  
telling you which of these two pairs of modalities  
should interact with each other.  
In this case, it might learn that privilege,  
while taking into account emphasis like privilege,  
is a very important interaction with a weight of 0.7.  
And, likewise, the word privilege with eye rolling  
is also another very important interaction  
that a model should look at with a weight of 0.3 and so on.  
This vision-to-language attention matrix essentially  
tells you how all of the words in your sentence  
should interact with all of your four nonverbal expressions.  
This matrix can then be used to contextualize  
the actual features of nonverbal expressions.  
So this 3 by 4 matrix multiplied by a four-dimensional vector  
will give you a three-dimensional vector.  
What this output three dimensional vector  
represents is for every one of your three words--  
for example, privilege-- looking at the attention with your four  
nonverbal expressions and multiplying it  
by those four nonverbal expressions,  
That gives you a new representation  
of the word privilege while taking into account  
the context from your nonverbal expressions.  
And, likewise, I'm going to repeat that with the next word  
mind by looking at, again, the four nonverbal expressions  
and the attention to them multiplied by those actual four  
features, that gives you a new representation of the word mind  
contextualized with vision.  
So this repeats until we've contextualized all the words  
that a person is speaking on their nonverbal expressions.  
And this representation is very useful.  
We've now realized that this privilege  
is spoken in the context of vocal emphasis  
and an eye roll at the end.  
And that allows you to predict that a person is actually  
being sarcastic about the other person.  
So that is, at a high level, what  
we call multimodal cross-attention transformers.  
It learns these pairwise interactions  
from one modality to the other that tells you  
how those two modalities attend and contextualize each other.  
Now, oftentimes, these cross-attentions are repeated.  
I've shown you the cross-attention  
from vision to language.  
And, oftentimes, there's also the cross-attention  
in the other direction from language to vision.  
And after cross-attention, people have usually found that  
it helps to put several self-attention layers--  
so those are unimodal transformers--  
to further contextualize data within the same modality.  
And these models are very performant.  
Vilbert, for example, that applies  
this pairwise cross-attention from vision to language  
and the cross-attention from language to vision,  
followed by unimodal transformers,  
was one of the first demonstrations  
of learning representations from sequential image and text data.  
So now that we've learned these multimodal representations  
through cross-attention, how the vision relates to language  
and how the language relates to vision,  
how do we train these representations?  
Well, several strategies have been explored.  
I'm going to highlight three of the most common strategies.  
One of the most common strategies  
is to perform masked language modeling.  
So given, for example, images of, in this case, man and a dog,  
in the image, and several words man with his mask.  
Can we take in both of these modalities  
and predict what is the next word in the sequence?  
So, in this case, the model has to understand the image  
and realize that there's dogs in the image.  
And, likewise, the model has to understand the previous words  
in the sentence and grammatically  
fill in the next word being dog.  
So we call that masked language modeling,  
masking out words in the caption and using  
both the images and the remaining words  
to predict the word that was masked out.  
A natural second type of objective  
is masked region modeling, basically, the other direction.  
I'm going to keep all the words in the caption  
and I'm going to mask out a certain part of the image.  
And given the remaining image and the caption,  
I'm going to try to predict the part of the image that  
was masked out.  
So that was masking images and recreating it.  
Again, that requires the model to have spatial understanding  
of the remaining parts of the image  
to predict what was missing and, again, understanding the caption  
to help infill the objects that were missing in the image.  
And, finally, another common objective  
is an alignment objective.  
Given a particular caption and a particular image,  
I'm going to try to predict whether those actually belong  
and match with each other.  
So images and their corresponding captions  
should match with each other and images  
with other random captions should not  
match with each other.  
So does the sentence match the image?  
So these are just some training objectives  
that can be used to train the representations learned  
from these large multimodal transformers.  
So that's part 1, how we can take in temporal data from  
different modalities-- such as words, images, video,  
and audio--  
and learn temporal representations  
of how each modality becomes contextualized  
in a sequence of other modalities.  
In part 2, we're going to look at how  
these multimodal temporal representations can  
be used to adapt large language models to become multimodal.  
This will allow you to ask questions and retrieve answers  
about these multimodal representations  
in a flexible manner.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.3 Adapting Large Language Models with Prefix Tuning  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So we're going to cover a common way of adapting  
large language models.  
And this method is called prefix tuning.  
Now, the whole idea of prefix tuning  
is that we often have large pretrained language models  
that I've shown here.  
It takes in a caption--  
for example, a small red boat on the water--  
as individual tokens into the model  
and it essentially models the probability  
of this text sequence.  
Now, the goal of adapting large language models  
to look at multimodal data is the idea instead of just looking  
at the probability of this text sequence,  
I want to model the probability of this text sequence  
given some image, condition on some image that I also see.  
So we call this prefix tuning because as the prefix  
to this text sequence I'm going to add  
an image, an image that corresponds  
to this particular caption--  
so an actual small red boat on the water.  
Given this particular prefix that I've  
appended to the beginning of this caption,  
I'm going to extract some visual features that  
are shown in red triangles.  
And I'm going to learn what we call an adapter.  
An adapter is essentially a transformation  
that transforms the visual representations of this image  
into something that can be input into the large language model  
input token space.  
Given this adapter, we can now define a new model  
that takes in both the adapter representations of the image  
and the tokens in language sequentially.  
First, the adapter representation  
as a prefix and the representations of the words  
into the language model.  
Now, this language model is now an adapted representation  
because in our models the probability of text, given image  
that we have appended at the beginning of this sequence.  
This model can then be trained to, again,  
autoregressively output the specific caption.  
Autoregressively, meaning first taking the image and predicting  
the word "a" then taking the image and the word that  
you've predicted "a" to predict "small."  
Taking the image and "a small" to predict the next word "red,"  
"boat," "on," "the," "water," and so on.  
Now, another key benefit that I have-- of this model  
is the fact that this pretrained model can be frozen.  
And the only thing that we need to train  
is the adapter layer that transforms  
the visual representations into the input space  
of these large language models.  
This is a critical benefit because most  
of these pretrained large language models  
are extremely huge, so you don't want to continue training them  
once they've been pretrained.  
And the only thing that we need to train  
is this small adapter transformation  
that transforms the images and the representations  
into the space of these frozen large language models.  
So this very simple framework can enable many applications.  
Once you've trained it in this way, you can give it a new image  
and you can ask the frozen language  
model what color is the car.  
And, again, by taking this image and its visual representations  
and prepending it as a prefix to this question,  
you can now learn a representation  
that captures the next word given  
the previous question and the images  
that you want me to look at.  
And these models can correctly answer blue.  
Here's another example.  
This example is a bit more involved  
because it requires models to extract some external knowledge.  
So over here I'm giving a model an image of an airplane.  
I'm going to extract features and, again, adapt it  
into the large language model and put it  
as a prefix to the frozen large language model.  
And then I'm going to ask a question, who invented this?  
and give the model one demonstration of the answer  
that I'm looking for-- in this case, the Wright brothers.  
So we call this one-shot learning  
because you're giving the model one example  
of the format of the question and the answer  
that you're looking for.  
Given one example, I'm then going  
to add to the next time you prompt the model a new image--  
in this case, a person holding an iPhone--  
and basically ask it the same question, who invented this?  
Answer, with a blank.  
Now, the goal of the model is then  
to learn from this first demonstration example  
and try to answer this next question.  
And, again, using this adapting pretrained large language model  
method, the model is able to answer that Steve Jobs, answer,  
who invented this iPhone.  
Here's a slightly more involved example.  
I'm going to give it an example of an apple.  
And its visual representations adapt it  
as a prefix to the frozen large language model.  
And I'm going to tell the model that this is a dax, where dax  
is basically a made up word.  
I'm going to give it an orange and tell the model  
that this is a blicket, where blicket is again a made up word.  
Now, given a new apple in some different orientation,  
I'm going to ask the model, what is this?  
Now, the model, by learning from these few examples,  
is able to successfully solve this binding problem,  
where the goal is to bind this new concept dax  
and blicket to these images of apples and oranges.  
So given this new apple, the model  
can correctly answer this is a dax.  
So these are just some examples of the power of adapting  
pretrained and frozen large language models,  
where you can keep the bulk of the parameters-- the huge,  
large language model frozen--  
and the only thing that you need to train  
is this very simple adapter layer  
that takes in these visual representations  
and transforms it into something that the frozen large language  
models can understand.  
And this allows you to quickly turn large language models  
into multimodal counterparts, enabling  
you to answer questions, do symbol binding, and so on.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.4 Scaling Multimodal Models with Adapters  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So since the original paper on adapting  
large language models was released in 2021,  
these methods have really been scaled up.  
Here's one example of a very large multimodal model that  
was essentially trained using this idea of adapting  
frozen large language models into a large multimodal model.  
It's called the Flamingo model from Google DeepMind  
that can look at images and hold free-form conversation with it.  
So I love the example on the right  
because it's a picture of an Apple with an iPod pasted on it,  
which is actually a reference to a common failure  
mode in the previous generation of multimodal models,  
where they recognize this image as an actual Apple iPod instead  
of a literal apple with an iPod sticker on top of it.  
So you can start giving this image to this Flamingo model  
and you can ask it questions like, what does the sticker say?  
The sticker says it's an iPod and the model correctly  
recognizes that it is a literal apple  
with a sticker on top of it.  
There's several other good examples  
of adapting large language models.  
This MiniGPT-4 model is a good example  
that is completely open source.  
It is an attempt to replicate the capabilities  
of GPT-4 by taking a frozen large language  
model, in this case Vicuna, freezing it, taking in images,  
and putting them through a frozen vision transformer.  
So that's a model that is able to encode images  
into representations.  
And the only thing that is trained in this model  
is this orange linear layer block in the middle.  
This orange linear layer takes in the image representations  
from the frozen vision transformer  
and transforms it into a representation  
that can be input into the frozen Vicuna language model.  
And there are several stages of training.  
The first stage is alignment.  
Using paired image and text data,  
you're going to give it some images  
and you're going to tell the model what these images are.  
So this is an image of a person, this  
is an image of many people having a conversation,  
and so on.  
That's the alignment stage.  
And the second stage is instruction tuning.  
So this stage involves giving it images and giving it  
certain instructions.  
For example, what do you think of this logo design?  
Act like you're a personal assistant  
and essentially having humans write out  
what a good answer should be-- the fact that this logo  
design is simple and minimalistic,  
with a pink drawing of a flamingo standing on one  
leg in the water and so on.  
So just by these two stages and just  
by training this small linear layer that maps the vision  
transformer outputs into the space of large language models,  
you can get a ton of great capabilities that almost,  
at some surface level, matches GPT-4 performance.  
LLaMA-Adapter is another example that  
has really scaled up the diversity of these adapter  
models.  
Whereas previously we just gave the example  
of a frozen large language model in English being adapted  
by images, LLaMA-Adapter has essentially  
scaled this up to, firstly, multiple languages.  
You can use English language models, Chinese language models,  
French language models, and so on.  
And you can also adapt other modalities beyond just image.  
In this case, you can adapt 3D point cloud representations  
into the space of these large language models.  
That allows the model to achieve capabilities like giving in some  
particular point cloud of a car, in this case,  
giving an instruction, like generate an image from the 3D  
point cloud, and actually being able to generate these images  
representing cars that map to the 3D point cloud.  
And the bottom example is just showing the same capability  
but in a different language, Chinese.  
So LLaMA-Adapter is also another great resource  
where all the code is open source because the LLaMA  
language model is open source.  
And all these adapter models, from 3D point clouds, to images,  
to audio, video that they adapt into the LLaMA model are all  
open source.  
So that wraps up part 2\.  
So you recall in part 1-- we looked  
at how we have sequences of images, text, video, audio,  
and how we can learn multimodal temporal representations  
of each modality, interacting and contextualized  
with a sequence of other modalities.  
In part 2, we looked at how these multimodal representations  
can be adapted into large language models  
so that you can keep the large language model frozen  
while still having the capabilities of it  
conditioned on the prefix of these adapted multimodal  
representations.  
In this third part, we're going to finally complete  
the schematic and add image generation capabilities.  
Beyond just generating text, can I also output more data  
from other modalities.  
And this enables true multimodal interaction  
because you have multimodal inputs and multimodal outputs  
potentially across multiple steps of interaction.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.5 How Text-to-Image Models Work  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So part three, text-to-image generation.  
I'm sure all of you have seen amazing capabilities  
of text-to-image generation.  
Nowadays, for these AI models, you can put in a prompt that  
sounds really unrealistic-- for example,  
an astronaut riding a horse in the style of Andy Warhol--  
and these models are able to generate  
pretty realistic images that follow  
the captions to a large extent.  
You give it a caption that says a bowl of soup that  
is a portal to another dimension as digital art.  
And again, these AI models can generate  
pretty fantastic and realistic images  
following those instructions.  
So how do these text-to-image generative models work?  
At a high level, you can first take a lot of images  
from the internet.  
And given a ton of images, the first step  
these models typically take is to train  
some form of autoencoder.  
An autoencoder is a pretty generic term  
that essentially means you're going to take in this raw image,  
learn an encoder, an image encoder,  
into some set of features.  
And given this set of features, I'm  
going to learn an image decoder that maps these features back  
to the original image.  
So any method with an encoder-decoder  
can be seen as an autoencoder because your autoencoding  
and trying to recreate yourself, recreate the original image.  
And the good thing about these autoencoders  
is that it can be trained with tons of data.  
All you need is to download tons of images on the internet.  
You don't need any text captions for them.  
You don't need any labels for them.  
You don't need to filter them in any way.  
Just take as many images as you can, and train this autoencoder.  
The next step is to learn a transformer that actually  
brings text into images.  
So you could take in some text, for example,  
an armchair in the shape of an avocado, learn a text encoder--  
nowadays, these text encoders are done  
using large language models--  
which gives you an output feature for these texts.  
And then the goal is to map the text to the corresponding image  
representations.  
Now this part is harder because now this part  
requires you to have paired data of the text  
with the corresponding image.  
So this amount of paired data is going  
to be substantially limited as compared to just image or just  
text data.  
But assuming if you can obtain such paired data,  
you can essentially learn this mapping that takes in text,  
learn an encoder into text features,  
and use that to predict the image features.  
And finally, the third step is generation.  
Given a new prompt that is different from the one  
in the training set is going to pass through the text encoder,  
learn features, map into the image features,  
and then decode into a raw image.  
That's the generation process for text-to-image generation.  
So how are some of these modules actually implemented?  
Well, when this model first came out, the Dall-E 2 model,  
they used a discrete variational autoencoder.  
So what discrete variational autoencoder means  
is that you can take in tons of images,  
and your goal is to learn an image encoder into some image  
features and an image decoder that maps the features back  
to the image.  
This can be trained using tons of data,  
as long as you have lots of images  
that you can take, encode, and decode  
to recreate the original image.  
Now the key here is that this autoencoder  
has a discrete latent space.  
That's why I've drawn these intermediate features as bracket  
98, bracket 3, bracket 990, for example.  
Each of these features is discrete,  
so it belongs into a list of digits.  
In this case, between 0 and 8,192.  
You can think of these discrete tokens  
as a visual token, some token that represents  
some part of the image.  
And likewise, if I give you another image,  
I can apply the same encoder.  
To learn these features, it's going  
to be a different set of discrete tokens.  
For example, bracket 46, bracket 390, bracket 6\.  
That can be decoded back to the original image.  
I'm going to first start by training  
this discrete autoencoder.  
Now in the process of recreating the original image  
through the image encoder and decoder,  
this reconstruction process is not going to be perfect.  
So that's why you see the images on the right  
are going to be a slightly blurred version  
of the original input image.  
So now that we've learned an encoder and decoder that  
maps images into these discrete tokens and discrete tokens  
back into an approximate version of the original image,  
the second step is to translate text  
to these discrete image tokens.  
So this can be done using an autoregressive transformer,  
such as a large language model, that  
takes in the caption, an armchair  
in the shape of an avocado, and predicts the first token, 56\.  
This first predicted token will then be given as the input  
to the next step, where you have an armchair  
in the shape of an avocado, token 56,  
to predict the next token, 73\.  
This next token would then be put back into the input  
and predict the next token, 67, and so on.  
So this autoregressive decoding process essentially  
transforms all this text into a set of predicted image tokens,  
which can then be used by the decoder  
to predict the raw image in some approximate form.  
So at a high level, that's how the first generation  
of these really powerful text-to-image generative models,  
the Dall-E 2 family of models, worked.  
Of course, nowadays, these models  
have become much more high resolution  
than just VAEs, which create a slightly blurred reconstruction  
of the input.  
And the key idea behind some of these new models  
is to replace the autoencoder that  
does one step of encoding and decoding with a diffusion model.  
Now the internals of diffusion models are a bit complex.  
But at a high level, the key takeaway  
is that this diffusion model does encoding and decoding  
not in one step, but across multiple steps.  
So you have multiple steps of encoding your images  
into some latent feature, and you  
have multiple steps of decoding the latent feature back  
into the original image.  
This sequence of encoding and decoding through multiple steps,  
alongside the significantly scaled-up versions of today's  
models using large amounts of data  
and large numbers of parameters, really  
allow these diffusion models to generate super-realistic images.  
So here are some examples from modern diffusion models.  
This is a Stable Diffusion model released in 2022\.  
Very popular today.  
You can give it a text instruction  
that says a street sign that reads latent diffusion.  
It can actually generate pretty realistic images.  
These models still have some problem  
with generating words that are exactly without spelling errors,  
but on the whole, they look pretty realistic.  
The second example, a zombie in the style of Picasso.  
Again, pretty realistic images.  
They are really high resolution.  
Beyond text-to-image generation, these models  
can also be conditioned on other modalities.  
So over here, you can give the model  
what we call a semantic map.  
On the left, the semantic map essentially shades the regions  
in one consistent color where you want those regions to be  
the same semantic object.  
So I might shade in red something  
where I want the model to generate a sky.  
I might shade in consistent green someplace  
where I want the model to generate the ground.  
So given this semantic map and given instructions  
of generating an image following the semantic map,  
these models can actually generate and fill  
in the details in the specific regions that a user requests.  
Here's another example, where instead of conditioning  
on semantic maps, you're conditioning  
on object bounding boxes.  
So you can give these layouts where you want a certain object  
to be here and a certain object to be here  
in the form of bounding boxes.  
And it can generate images that pretty consistently follow  
where the objects should be and what these objects are.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.6 Large Multimodal Models with Image Generation  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now let's bring everything together  
by demonstrating a recent example  
of a large multimodal model with image generation capabilities.  
So over here, as input, we have both images and text.  
You might have several cookies that you just baked and you've  
taken a photo of.  
And you might have a question, for example.  
How should I display these at the farmer's market?  
Now again, we're going to use the adapter layer from part two  
to start this model, where you take in the image,  
you put it through a visual encoder,  
and you learn a linear mapping from the output  
of the visual encoder to the input of your large language  
model token space.  
This is, again, the adapter that is used as a prefix to the text.  
And given the caption, I can, again,  
tokenize that using a text tokenizer  
into the large language model input space.  
Together, the large language model  
ingests both the prefix of the visual token and the actual text  
tokens after the prefix, and it starts generating more text.  
For example, large language model might generate,  
I think you should place it in this way.  
But of course, placing it this way  
is not descriptive without actually  
generating an image of how these cookies should be placed.  
So these models are able to plug a Stable Diffusion model that  
takes as input the text that the large language model generates,  
and actually generate a realistic image showing  
how these cookies should be laid out.  
And so that's the generation model  
that we discussed in part three.  
In fact, this model goes a step further  
by having a decision node that either generates  
new images pixel by pixel, shown on the right,  
or retrieves images that are similar to the text prompt.  
Sometimes, retrieval is better, and sometimes, generation  
is better.  
So retrieval gives you the guarantees  
of images that are from the internet that are realistic,  
but you're limited in the number of images that you can retrieve.  
Generation is good because now you're unbounded.  
You can generate any pixel by any pixel,  
and generate any image.  
But of course, you're at risk of images  
that are hallucinated or has incorrect properties.  
And finally, the model will output both text and images.  
I think they look best when they are  
on a tray with a little bit of space between them.  
So that's the text.  
It also generates a corresponding image  
through this text-to-image generation  
model that shows what such a layout could look like.  
And here are just more examples from this model  
that enables pretty good multimodal interaction.  
You can take in images and texts,  
for example, an image of a ramen and how should  
I make it more nutritious.  
It can give you several tips of adding different vegetables  
and recipes.  
And it can also include an image of what  
an outcome could look like.  
In the second example, you can give it an image of a tattoo,  
and you're trying to brainstorm what kind of tattoo  
would look best.  
And it can ideate with you, generate potential examples  
of tattoos that might look nice for the particular person.  
In the third example, you might be baking cupcakes.  
And you might say, how should I best publicize it at a market?  
It can give you several suggestions,  
and also generate an image of what  
a nice signboard in front of these cupcakes  
could look like to publicize it.  
So these models are really at a frontier.  
They enable very flexible, multimodal interaction  
with images' text as input from the user, image and text  
output by the model, and potentially  
across multiple steps, like having a real conversation  
with a person.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.7 Wrap-Up  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So to summarize, we saw three parts  
of building large multimodal models and multimodal generative  
models.  
In the first part, we looked at how  
various forms of sequential data,  
like words, images, videos, and audios,  
can come together through these multimodal temporal  
representations that learns how each modality should  
be contextualized with a sequence of other modalities.  
In the second part, we saw how these multimodal representations  
could be used to adapt large language models so that you can  
have flexible text generation on the output,  
while looking and conditioning on all forms of multimodal data.  
And finally, in part three, we added the capability  
for text-to-image generation so that we can also  
have multimodal input and multimodal outputs,  
generating more images, videos that supplement the text  
response from a model.  
And this concludes this lecture.  
In summary, we've seen that large language models have  
enabled new capabilities for free-form question  
answering, dialogue, and advanced reasoning.  
Naturally, it's very critical to extend these large language  
models into large multimodal models  
so that you can jointly process vision and language  
to learn multimodal temporal representations.  
These representations can be used to adapt large language  
models to generate text while looking  
at various forms of multimodal data,  
such as text, conditional images, video, and audio.  
And finally, we have the other direction, too.  
You can augment these large language models  
with generation capabilities so the text that you're generating  
can be supplemented by generating images, video,  
and audio for true multimodal interaction.  
And that's the end of this lecture,  
and also, the end of this four-part course.  
I want to summarize the main takeaways.  
Firstly, I want everyone to have an appreciation  
that multimodal problems are everywhere  
in understanding human communication  
through both verbal and non-verbal channels,  
in controlling physical systems using a wider range of sensors,  
and analyzing diverse forms of medical data  
to help doctors make treatments, and to monitor the climate  
and the environment.  
In lecture 1, we looked at the basics of multimodal data,  
various types of multimodal models,  
and different challenges that makes  
multimodal AI difficult as compared to single modality AI.  
In lecture two, we dive deep into building multimodal fusion  
architectures for healthcare applications.  
In lecture three, we looked at how these multimodal fusion  
architectures could be used to aggregate  
all of these indicators of your climate  
to track the climate and the environment.  
And finally, in lecture four, we just  
covered recent advances in large multimodal models and generative  
AI, building this new generation of systems  
that are capable of multimodal interaction as input  
and generating multimodal outputs.  
Thank you, everyone, and I hope you enjoyed this course.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture introduced large multimodal models (LMMs) and multimodal generative AI, explaining how large language models are extended to jointly process text, images, video, and audio—and to generate multimodal outputs for interactive systems.

Key Takeaways:  
From LLMs to LMMs: Large language models transformed text generation; large multimodal models extend them to reason jointly over vision, audio, and video alongside language.  
Multimodal temporal representations: Transformers with cross-attention learn how sequences of words, frames, and sounds contextualize each other, capturing cross-modal interactions (e.g., tone, sarcasm).  
Adapting frozen LLMs: Small adapter/prefix layers map visual or other modality features into the token space of a frozen language model, enabling multimodal conditioning without retraining the full model.  
Scaling to real systems: Models like Flamingo and MiniGPT-4 combine alignment and instruction tuning to support multimodal dialogue and few-shot reasoning.  
Text-to-image generation: Modern generative pipelines evolved from token-based autoencoders to diffusion models, enabling high-resolution image synthesis from text prompts.  
Multimodal input and output: By combining LLM reasoning with generative models (e.g., Stable Diffusion), systems can both interpret multimodal inputs and generate images—enabling true multimodal interaction.  
Central insight: Integrating cross-modal representation learning, lightweight LLM adaptation, and generative modeling creates systems that both understand and create across modalities.  
\`\`\`

Lecture 4: A Case Study with Hurricane Forecasting  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 4: A Case Study with Hurricane Forecasting, taught by Professor Leonard Boussioux, Assistant Professor at the University of Washington, Foster School of Business.

What do forecasting a hurricane, diagnosing a patient, and guiding a self-driving car all have in common? They all rely on multimodal AI — models that combine different types of data to see the bigger picture.

This lecture introduces the foundations of multimodal machine learning:

From storms to sensors: Hurricanes are fueled by warm oceans and chaotic winds. To predict their paths and intensity, scientists collect many data sources — satellite images, radar time series, pressure tables, even aircraft flying into storms.

Why multiple modalities matter: Just like a doctor checks vitals, scans, and patient notes before making a diagnosis, multimodal AI integrates images, text, tables, and signals. Alone, each source tells part of the story; together, they can transform predictions.

Training across formats: Convolutional neural networks extract patterns from images, while transformers capture sequential context. Time series and tabular features join the mix. By aligning and encoding them into vectors, we can fuse these diverse signals into a single predictive pipeline.

Keeping models practical: Feature extraction and fusion make the data manageable. Gradient-boosted trees and other ML models then turn these multimodal embeddings into accurate forecasts. Sometimes end-to-end learning is enough, but often a hybrid approach adds power.

The impact? AI models are already matching — and even enhancing — the performance of traditional physics-based weather forecasts, complementing decades of meteorological expertise. The same principles extend beyond storms, powering advances in health care, ecology, and beyond.

By the end, you’ll see how today’s AI breakthroughs in forecasting and decision-making rest on these core building blocks (collect, extract, and combine) simple steps that, when applied across modalities, unlock insights from the world’s most complex problems.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explore how multimodality applies to hurricane forecasting, and explain why combining data sources (e.g., images, time series, tables) improves predictive performance.  
Describe feature extraction techniques (CNNs, transformers) and explain how they convert raw data into usable vector representations.  
Explain how different modalities are aligned and fused into a single representation for machine learning models.  
Interpret the role of gradient-boosted trees and neural networks in making predictions from multimodal embeddings.  
Compare forecasting approaches (statistical, dynamical, consensus, and AI-based) and evaluate their strengths and limitations in hurricane prediction.  
\`\`\`

L4.1 What is Multimodality?  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The topic for today is the concept of multimodality.  
I love this concept because I spent my entire PhD  
studying this and how it can impact so many different fields.  
The idea of multimodality is that we  
can combine multiple data sources together  
to solve a challenging problem, for instance,  
in health care or weather.  
I will illustrate the concept with a case study  
from my own research when I was a PhD student with my advisor,  
Professor Dimitris Bertsimas.  
So the results I will show you are really  
results on which I worked for years.  
And I'm so happy I can make it into a lecture for you today.  
So let's get started.  
We are going to cover multiple important topics  
around multimodality.  
First of all, we'll describe the foundational principles  
and potential architectures for multimodal machine learning,  
including concepts of modality fusion and feature extraction.  
I will explain multimodal machine learning techniques  
to analyze and predict outcomes in real world  
scenarios such as hurricane forecasting  
and will evaluate advantages and limitations  
of multimodal approaches and suggest  
ways to improve this such that accuracy can be  
perfect for your application.  
I want to start with mentioning how  
ubiquitous the technology of multimodality is all around us.  
The idea of multimodality is really  
to have components, robots, software devices, algorithms  
that can process all sorts of data at the same time.  
For instance, robots need to be able to operate  
with the real world.  
And they may receive information from cameras, LiDAR cameras.  
And they have mechanics involved for how to move.  
Self-driving cars may have access to vision from cameras  
but also LiDAR again.  
And they have to be able to operate with all  
the mechanics of a car.  
All the smart home devices that can understand  
your voice and then have sensors also at the same time,  
they also involve all sorts of data.  
If you are using video conferencing,  
you may notice that sometimes you  
have some AI features that are able to understand  
in real time what you're saying to caption and also give you  
a summary of all the discussion points.  
That's also multimodality because such technology  
can understand your voice and potentially transcribe  
this into a text.  
Platforms for online streaming and social media  
are also able to process images, videos, caption these.  
There is such a wealth of data right there.  
The wearables, like the smartwatch, those devices for VR  
and augmented reality, they're able to process also  
different types of data.  
And finally, your smartphones, they  
are handling so much data at any time.  
All those technologies that you're seeing here  
are multimodal.  
And they're all around us.  
The multimodality is really the ability  
to combine the data sources together.  
Those modalities that you want to process/relate  
can be, for instance, tables of features.  
For instance, your age, your weight, your ethnicity,  
your demographic data.  
It can also be a time series, which is a type of table where  
you have time involved.  
For instance, the temperature across time,  
the price of a stock market.  
That's something that has this temporal component that  
is important.  
You also have images, of course, texts, sound.  
Those are modalities.  
They are sources of data.  
Combining them is the concept of multimodality.  
You as a human, you do this constantly, every day.  
Even now, listening to my lecture,  
because you can listen to what I'm saying and see the slides,  
and on the slides you have images and also text,  
those are all different modalities.  
Humans are so good at doing this.  
This is how you drive.  
This is how you order food at a restaurant.  
This is how you make decisions.  
This is how you hike.  
We need multimodality to operate in this world.  
So the big question is, how can I  
replicate this natural cognitive process into a computer  
to assist my decision making?  
That's the topic for today.  
If you look more into your multimodal experiences that,  
for instance, shape your memories,  
you have so many things involved-- the sound, the taste,  
the touch, the appearance, and the smell.  
This is how we form our understanding of the world.  
And machines can potentially have access to this information  
as well through sensors.  
And now that you have this information,  
you need algorithms to be able to process it.  
We have our brain, and animals, and plants also  
have equivalents of brains or ways to process data.  
But machines need algorithms.  
For weather forecasting, it's extremely important.  
You want to build models that are as accurate as possible,  
utilizing all available data because it probably can help.  
So to predict, for instance, the temperature tomorrow  
or to predict how a hurricane will move next,  
I need to analyze images, for instance from satellite imagery.  
It can be pure pictures, but also  
infrared pictures or UV pictures;  
time series that you can obtain from radar stations.  
For instance, it can be the temperature  
at the nearest airport; and tables of extra side data,  
for instance from a buoy in the middle of the ocean.  
Sometimes the National Hurricane Center  
is even sending aircrafts in the middle of a hurricane  
to collect important information to make predictions.  
But now you have so much data in so many different formats,  
it's a big challenge to combine all of it.  
Health care is also another very good example.  
How are doctors, nurses, practitioners making decisions?  
They ask you questions.  
What's your age?  
What did you eat?  
Are you taking any drugs right now?  
This is a set of features that can make it into a table.  
Maybe they will ask for an electrocardiogram.  
They want to measure your breathing.  
They want to measure your heart pulse  
across time and potentially many other factors.  
This is making into a time series.  
They may request for images--  
an MRI, a CAT scan, a radio X-ray.  
All sorts of images can help doctors.  
And finally, they also write notes.  
Nurses and doctors can write a lot of notes about you.  
Those notes can be helpful if multiple people  
are trying to help you.  
And if you already visited a hospital in the past,  
typically your data can be stored in the database  
so it's possible that using data from previous stays  
in the hospital can help you for this new situation.  
Can we have algorithms that can process all of this?  
The answer is yes.  
And we're working on that.  
Today, we are going to cover some methods around this.  
Before we get going, I want you to think more  
about those concepts for yourself and for your interest.  
So my first question for you is, can you  
think in your field, your major, your minor, your hobby what  
are things you could predict?  
For instance, it can be predicting the winning  
team in the next game.  
It could be predicting the stock market.  
It could be analyzing how the wind is flowing.  
So many things.  
So think about what you could predict using algorithms.  
And next, those prediction tasks.  
Are they multimodal?  
Would you benefit from multiple data sources  
to make your decision?  
And what kind of data sources would be useful?  
So let's take just a random example, sports.  
If you want to predict who is the winning team,  
maybe you want data about all the players  
involved in your team and the team  
that you're going to compete with.  
And maybe you want to know also the previous performance.  
So think about those two questions  
such that you have even more understanding of the concept.  
And now let's talk about multimodal machine learning.  
It's the study of all those computer algorithms that  
can learn and improve through the use of these data sources  
from multiple modalities.  
Multimodal AI is the overarching principle  
of how do we build those computer agents that  
can understand, reason, and plan through those multimodal  
experiences.  
Today, we are going to look into multimodal machine learning,  
a subset of multimodal AI specifically  
responsible for figuring out good algorithms for this.  
If you look at this video right now,  
you are having multiple sequences of information.  
You have the language.  
So this is what I'm saying.  
Maybe you have access to a transcript.  
Maybe you have captions.  
Those are texts.  
You have the images.  
So it's a sequence of images.  
It's like a video.  
And you have the sound.  
Right now, it's already being multimodal.  
And you have multiple data sources working all together  
in a sequence.  
If I want to build an algorithm that can understand videos,  
I need an algorithm that can potentially  
understand all of that.  
A modality to be more specific can be raw or abstract.  
For instance, a speech and an image  
is very close to the sensor.  
You just have a sensor that can measure something  
and you immediately get the data.  
But sometimes it's also a bit more sophisticated.  
Speech can be transformed into language  
because you transcribe the sound that you just  
heard into the actual words.  
Out of your image, maybe you have  
objects that you could detect.  
Those can also be considered modalities.  
And then if you keep moving to more abstract modalities,  
you may have a sentiment intensity.  
Out of those words that I just said,  
can you feel if I'm happy, or angry, or just neutral?  
You can understand the sentiment as a more abstract modality  
out of the initial content.  
And out of the detected objects, you  
may detect them and then figure out in which categories  
they fall.  
So you have a more abstract type of modality.  
So really modalities can happen all around you.  
And the algorithms may be able to process  
maybe just the raw modality or maybe some more abstract kinds.  
And then modalities can be more or less different.  
If you have images from two different cameras,  
those two modalities are quite similar because it's  
images of the same situations, just two cameras.  
Maybe you can have also text from two different languages.  
Those texts are both language but they  
may use a different alphabet.  
Now you may have also language and vision.  
So this time it's more different.  
You have, for instance, a caption describing an image.  
So those two modalities correspond to each other  
but they are very different in their format.  
And finally, you have data that can be extremely different.  
For instance, you have some financial market data and lots  
of social media information.  
Still, you could forecast maybe the stock market  
better if you know the sentiment analysis from social media.  
So you need to be able to combine  
things that are very different.  
There exist techniques for every single combination  
of modalities.  
And it's a very active area of research.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L4.2 Multimodal AI for Hurricane Forecasting: Motivation and Challenges  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Today, we'll focus on multimodal AI for hurricane  
forecasting.  
This is the topic I investigated in my thesis  
during my PhD at MIT, and I want to show you  
how I managed to forecast hurricanes using  
multimodal machine learning.  
Let's look into a brief video so that you  
have a better idea of how hurricanes work  
and why it matters to forecast them.  
Climate change, wildlife preservation, healthcare, these  
are some of the most pressing questions in the world  
but with little in common.  
It takes humans years to specialize in each field.  
Now, what if we could find solutions  
to all these questions using only one universal methodology?  
Recently, artificial intelligence  
has been successful in various topics.  
So I asked myself, could we build artificial intelligence  
for hurricane forecasting, insect identification,  
medical diagnosis using the same underlying methodology?  
The answer is yes.  
My research addresses these questions in a unified way.  
How does it work?  
I get my inspiration from the way we as humans make decisions.  
For example, a doctor can take the blood pressure,  
listen to the heart pulse, request a radio picture,  
and read a patient file before recommending a treatment.  
These are data sources in different formats, text, images,  
sound, tables.  
The natural cognitive process of understanding and utilizing  
all this data is called multi-modality.  
My goal is to replicate this mechanism in computer models.  
As an example, in a COVID-like pandemic,  
timely professional assessments are critical in saving lives.  
If our AI models can analyze patient data in real time  
and make accurate, fast suggestions,  
medical resources can be distributed more intelligently.  
To build an AI like this, I need three steps.  
First, I gather all available data sources  
about the target problem.  
Second, I transformed and extract information  
from the data using AI models.  
Finally, I combine all these process data together  
and make predictions with a machine learning model.  
My three-step recipe, gather, extract, predict,  
can be applied to any problem.  
The American Meteorological Society  
accepted my hurricane forecasting models  
for publication.  
Several museums deployed my insect identification tools.  
My health care models are now tested in several hospitals  
to assist doctors.  
I built all these models with this exact recipe.  
In conclusion, multimodality is the art of solving problems  
by using all data sources.  
This is also how the human brain works.  
Now, with the help of artificial intelligence,  
we can use computer models to mimic this cognitive process.  
With multimodality, I have one methodology to rule them all.  
Multimodality was really my thesis specialty,  
and I did more than just hurricane forecasting.  
I also worked on multimodality for health care  
and ecosystem conservation.  
I was really passionate into the combination of data  
because I believe that it allows me to tackle  
so many different challenges.  
I love the idea of combining, and I  
love the idea of having to resort to multiple types of AI  
to do this.  
And you could see from the previous lectures  
that we already studied multiple types of neural networks.  
Those can be adapted depending on the type of data.  
That's a very exciting area of research.  
So this is how we will operate in this lecture.  
I will introduce you to hurricanes, about the physics  
and why it matters to forecast them.  
I will show you a few opportunities with AI  
and why it can really help improve the overall field.  
And finally, how do we get this multimodal hurricane  
forecasting?  
The research I developed has been already quite successful.  
I was invited, for instance, in 2024  
to present in a nationwide conference about hurricanes  
how AI can really help join forces  
with the more traditional fields of weather forecasting.  
And I was absolutely delighted to see  
that the work I've done from MIT made its way into the hands  
of the forecasters.  
And they really want to leverage the technology for the better  
and build new kinds of models that can really  
help us in the future to predict those storms so much better.  
And it's important for all of us.  
AI is already making the news in weather forecasting.  
And there exist models that can already  
outperform the methods currently used by the National Hurricane  
Center, while those methods were developed for decades  
of research in physics.  
So it's really promising to include  
AI in more traditional topics.  
So Google DeepMind have worked a lot around this.  
AI in weather forecasting is still a work in progress.  
Clearly, the methods can help, but they  
have to convince the researchers in that field.  
The most successful application right now  
that's already being used and implemented  
by companies and governments is about rain nowcasting.  
The idea is to predict what's going  
to happen with respect to rain in the next few hours.  
The power of AI when it comes to weather forecasting,  
is that AI can ingest content extremely fast  
and give you answers extremely fast.  
Physics-based models are behind.  
They receive data about what's happening now,  
and then they need to compute with very large physics  
models, a whole simulation of what is going to happen next.  
This can take multiple hours, while AI can just give you  
a super fast inference.  
This is why it's such an important technique to help  
the weather forecasting field.  
Remember, AI is so fast.  
Look at how fast it can solve this little Rubik's cube.  
\[AUDIO PLAYBACK\]  
\- Oh, yeah.  
\- \[INAUDIBLE\]  
\[WHIRRING\]  
PRESENTER: This is work done at MIT.  
\[END PLAYBACK\]  
PRESENTER: Here it's robotics and AI,  
but AI is able to process all of it extremely well.  
Another important aspect of forecasting the weather  
is that you don't use a single model.  
You use a combination of top models  
because sometimes one of your model may underperform,  
and one of your model may be extremely  
good in this specific situation.  
The idea is to build a consensus among multiple models of what  
they think overall would be a proper answer.  
This is used in practice by the National Hurricane Center,  
and sometimes people call this the spaghetti models  
because you can see every model is telling you  
where the hurricane is going to hit,  
and they look like spaghettis all together.  
One technique to build a consensus  
is just to take the average model.  
The idea by including AI is not to replace  
all those incredible physics-based models but to have  
one more model that will look at weather forecasting  
under a different angle, a data-driven angle that leverages  
multiple modalities of information  
and include it into the consensus to potentially  
have an even better consensus now  
that there is a bit more information  
to make a good final decision.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L4.3 Case Study: Multimodal Hurricane Forecasting in Practice  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So the work I'm going to present now  
is based on the research I've done with my friend  
Cynthia, and Theo, and advisor Professor Dimitris Bertsimas.  
This work has been published in a really good weather journal.  
And this was impactful for the field  
so I'm delighted to transform it into a lecture for you  
because I learned so much while doing the research.  
And I also believe it can teach you  
lots of important components.  
Let's get started with hurricane forecasting.  
Recently, in the US, there was a massive hurricane called Helene.  
This hurricane caused 233 fatalities  
and has also involved losses than more than $80 billion.  
About every year or every year, you  
have some of those massive hurricanes  
all over the world that kill a lot of people  
and also destroy lots of things.  
The reason why they kill a lot of people  
is that sometimes they can intensify extremely rapidly,  
meaning they go from being a simple little storm  
into a massive hurricane, sometimes overnight.  
It's very hard to predict when a hurricane is going to intensify.  
And we need good models for this.  
Other big challenge-- a hurricane is not only big winds.  
It's also a lot of rain.  
And this rain will flood all the areas that are coastal.  
And those floods can be flash floods  
and also potentially take people who are trying to escape.  
This is why it's very important to evacuate and listen  
to the advice from the local government.  
But sometimes the evacuation orders  
are not prepared well enough in advance  
and some people decide to not evacuate.  
Also, falling trees, wind damage, infrastructure failures,  
tornadoes, and secondary hazards--  
hurricanes go along with so many other things.  
All of that needs forecasting and good planning.  
Let's get into the challenge of hurricane forecasting.  
First of all, we need to understand the concept  
of a tropical cyclone.  
A tropical cyclone is the scientific denomination  
of a hurricane.  
A hurricane is the last stage of a tropical cyclone.  
Before that, it would be a tropical storm  
and a tropical depression.  
Our goal is to figure out if a tropical depression, which  
is the beginning of the storm, is  
going to evolve into a larger one and, in fact,  
become at the very end this hurricane.  
They're called tropical because they  
form in the warm waters in the tropics.  
This water, because it's warm, is  
going to give energy to a disturbance that will  
evolve into the depression.  
And there is some movement of turning.  
And it keeps accumulating energy that goes into the clouds.  
And sometimes an eye is formed at the center of the hurricane.  
This is what is creating those monster  
storms that can wreak havoc.  
Our goal is to be able to forecast the track of such  
a storm because we want to know who should get ready to evacuate  
or prepare the infrastructure to resist  
the hurricanes and the winds.  
And you also want to forecast the intensity of the hurricane,  
meaning how strong the winds will be.  
Strong winds also means that it can destroy a lot  
but it also means that there will  
be lots of water involved and lots of floods.  
And to give you an idea of why predicting properly  
the intensity so the speed of the wind is important,  
let's look at the difference in storm surge flooding depending  
if you have a hurricane of category 3  
or category 4 in Florida.  
There is so much of a difference of how much water can go inland.  
And you really want to know in advance if it's  
going to be a huge intensity.  
It turns out most hurricane deaths are due to storm surge.  
So that's very important to figure it out.  
The current way it works for the National Hurricane Center  
is to use a combination of multiple types of model.  
Some of them are called statistical.  
They use historical data from different features  
acquired to make predictions.  
It's easy to understand potential hurricane behavior  
because the features are very explainable, typically.  
The problem is it's not necessarily  
very complex into the way it can model the data.  
And it does not adapt very well to new types of situation,  
for instance, because of climate change or a specific rare type  
of hurricane.  
The most successful models are typically dynamical models.  
They use sophisticated mathematical equations  
to simulate the physical processes underlying the storm.  
We can use the wind, the temperature, the pressure,  
the humidity.  
They use all of these at the same time.  
Simulate what will happen next.  
It's very powerful to predict but it also  
takes a huge amount of time to run, multiple hours,  
so you always lag behind what's happening.  
And on top of this, it's also very sensitive to the input  
conditions.  
To simulate the world properly, you  
need to know exactly what's happening right now.  
And getting the clean, proper, not noisy input conditions  
is challenging.  
There exist models that combine both,  
meaning the statistical and dynamical methods,  
and it creates a balanced approach.  
They can have the best of both worlds.  
But it's still typically not as precise  
as pure dynamical models.  
And getting a good balance is also challenging.  
And finally, using all these combination of models,  
we have what I called the consensus model,  
those spaghettis I mentioned.  
The idea is to do this at the very last stage.  
You look into the strengths and weaknesses of each model.  
And you try to combine them into one strong predictor.  
But of course, it depends on the quality of the underlying models  
to know which one should be included in your ensemble.  
Our goal is to contribute a new method that will be statistical.  
We want to leverage this data-driven approach  
to forecast hurricanes.  
Our goal is to predict the track and the intensity  
using the data that we have publicly available.  
There is lots of data involved.  
And then we have access to all the hurricanes  
all over the world in different basins.  
For instance, you have hurricanes for the North  
Atlantic basin like this.  
So this is the Eastern part of the US,  
Mexico, the Gulf of Mexico, all the islands, Caribbean,  
for instance.  
We also have the Eastern Pacific Basin,  
where this is about the eastern part of the ocean so the West  
Coast of the US, Mexico, and other islands.  
Lots of hurricanes as well in Asia.  
Around Japan, for instance, they regularly face challenging ones.  
So all this data, we use it.  
We don't stop only for US hurricanes.  
We use all over the world.  
And every hurricane can be also before a tropical depression  
or a tropical storm that evolves into this hurricane phenomenon,  
as I mentioned previously.  
So we leverage all this data.  
This data consists of multiple modalities.  
That's the subject of the day, multimodality.  
So we have access to time series data.  
So those are historical storm features.  
It can be the latitude and the longitude,  
so the position of the hurricane,  
the speed of the storm, the direction of the storm.  
We have many of such features.  
And we also use the satellite imagery using public data sets.  
It turns out that you can have access, for instance,  
to the winds at different altitude levels.  
You can have access to the pressure at different altitude  
levels.  
So we use such features all around the area  
where various tropical cyclone.  
And we look into the data at different altitudes  
because the phenomenon is informed by how each altitude  
level behaves.  
And on top of this, we want to compare the performance  
of our AI method with the models from the National Hurricane  
Center.  
So we also collect what were the historical forecasts made  
by the government at the time.  
We center our images at the center of the hurricane.  
And we take a huge area all around, for instance,  
1,000 kilometers of data all around the hurricane.  
And then as the hurricane moves, we also  
move the map accordingly.  
The challenge is we have access to time series data  
that is stored in the table and images.  
How do we combine the two of them?  
That's what I will show you very soon.  
The key results from our study is  
that the multimodal machine learning framework we developed  
was leveraging a method of feature extraction.  
Out of each modality available, I  
tried to extract features that were summarizing  
the relevant information.  
And this method brought new perspectives  
to the field of meteorology.  
It turns out that our top models had comparable performance  
with the best models from the National Hurricane Center  
in the US for forecasting 24 hours ahead.  
And what's also fantastic is if we include  
our model into an operational consensus with actual model  
currently used, we can even improve the performance better.  
It shows that having an AI model in the middle  
of other traditional models can enhance the performance  
because it looks at other aspects of the storm  
and uses different principles.  
So I really believe in the future of this technology.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L4.4 Building a Multimodal Forecasting Pipeline  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's dive into the framework  
of how we build a multimodal machine learning pipeline  
to forecast the intensity, so the wind speed and the track,  
so where the hurricane will go next, 24 hours ahead.  
Remember, we start with data.  
The framework I'm going to describe works in three steps.  
First, you collect the data, and you align the data,  
such that everything has the same timestamp.  
Now that you aligned all your data,  
you want to extract features from each data source.  
The idea of extracting features is converting your initial data  
format into the format of a vector.  
A vector is just a series, a sequence of numbers,  
and you know that those numbers are actually  
very easy to process with traditional machine learning  
frameworks that you have covered in previous lectures,  
like a simple linear regression, or logistic regression,  
or decision tree, or random forest.  
Those traditional machine learning methods  
operate with tables.  
So the goal of the extracting step  
is to convert initial data formats that are not tables  
into tables.  
And finally, now that I have all those features together,  
I'm going to make a prediction.  
So let's do it.  
First of all, I need to extract features out of my images.  
So I'm going to do some deep feature  
extraction using deep learning.  
In particular, I used convolutional neural networks  
and transformers to extract features  
from my initial sequence of images.  
Notice that it's challenging to handle a sequence of images.  
First of all, they're images.  
But on top of this, you have multiple altitude levels.  
And on top of this, it's also a sequence  
of images across multiple hours.  
So it's sort of a four-dimensional data.  
The goal is really to extract valuable information out  
of it in a simple format.  
I want to do the same thing with my time series.  
Although it's in the format of a table, as you can see,  
you need to figure out that there  
is some timestamps involved.  
And then the time, the sequential aspect of this data,  
matters.  
You have to understand that every sample of information  
comes next to each other.  
And you want the model to figure that out.  
So the idea is, I will process that to transform it again  
in a table of a simple vector of features.  
And now what's magical is that I have some vision embeddings,  
meaning some features extracted from the time series data.  
And then I'm going to take the vector that  
corresponds to the image, the vector that  
correspond to the time series.  
And then I'm concatenating them, meaning  
I stick them to each other.  
By sticking the two vectors to each other.  
You just obtain a larger vector, but it's still  
a vector of numbers, so you can actually  
make your prediction using all your favorite machine learning  
algorithms.  
In particular, in this scenario, we  
use what is called a gradient-boosted tree.  
You may have covered this in a previous lecture.  
If not, the intuition of a gradient-boosted tree  
is that it's an ensemble of multiple trees together  
that are specifically trained to help each other,  
where the trees that you're building in a sequence  
will try to correct the mistakes made by the previous ones.  
So you have a very strong ensemble of trees.  
This overall pipeline gives you some final forecasts.  
So I repeat, it's a three-step approach.  
You align your database according  
to the time and location.  
You extract features from each modality.  
You combine the modalities that are now  
vectors into one final vector.  
You feed these as input data to a traditional machine  
learning framework, like a gradient-boosted tree.  
And then you make your predictions.  
The overall pipeline works similarly,  
like in machine learning.  
You are going to train this gradient-boosted tree using  
a training data set.  
You are going to validate using validation data  
and also test on test data.  
So we did all of this.  
But still, there is a big challenge,  
which is how to extract the features  
with the deep neural network.  
How do I get the proper vision embeddings?  
So let's look into it.  
This is how it works.  
We want to build an end-to-end architecture for multimodality.  
This means that I want to start with some input data, my images,  
and end up with a vector representation, an embedding  
of this initial data.  
How do I do this?  
I'm going to structure the data as a sequence.  
I have my visual features, the satellite imagery  
from 21 hours ago, from 18 hours ago,  
and then you go in steps of three hours until the data  
that you can observe right now.  
And then you want to encode this data in a given format.  
To encode the data, I'm going to use  
a convolutional neural network.  
It's something we studied previously  
that is well suited for images.  
So here instead of having three channels of color,  
I actually have different altitude levels as input.  
I push this through a convolutional neural network  
that is the exact same one for every part of the sequence.  
And this CNN will be responsible to output  
some transformation of my data.  
Then what happens at that point?  
I now have a sequence of transformed data,  
one for each initial time step.  
So the CNN is responsible for converting my images  
into a vector.  
Now, I have one vector for T minus 21 hours, one vector for T  
minus 18 hours, one vector for every subsequent step,  
until I reach to one vector for now.  
I take those vectors, and I fit them into a transformer.  
Remember what we studied about transformers-- they process  
tokens, for instance, of texts.  
But here, instead of having a token of text,  
I basically have vectors of information  
about my initial images.  
So the transformer can be adapted  
to process this, for sure.  
Remember that transformers are very  
good at having a contextual understanding  
of your whole sequence.  
My goal is to have the transformer paying attention  
to different parts, such that it can  
predict how the hurricane will happen in the future.  
I want to leverage the strength of that method  
also for the hurricane.  
And now that I encoded the whole data in those vectors,  
it is time to decode.  
The transformer will be responsible to transform  
those vector representations into features I want to extract.  
However, we haven't studied so far in any lecture  
how do you get to predict features.  
We have learned how to predict, for instance, a text,  
how to predict a target, like it can be a classification  
or regression.  
But we have no idea on how to predict features.  
So we need to figure out a method  
to go from the transformer to those features extracted.  
So first of all, let's add into this whole process  
a fully connected layer.  
This fully connected layer is what  
we studied in the first lecture of the module, which is  
a normal simple neural network.  
The idea is out of my transformer,  
I will get some outputs.  
I just want to feed this into a simple network  
because it can be useful.  
Remember also when we covered the convolutional neural  
networks that at the end, we flattened everything,  
meaning we transformed everything  
into one super long vector.  
And this final vector is processed through a series  
of fully connected layers.  
We do the exact same process right here.  
So I have my fully connected layer.  
But still we haven't solved the problem  
that we don't know how to get the right features.  
So we have a technique to make it happen.  
The technique is I actually know how  
the hurricane will be in the future from my historical data.  
So let's focus this entire architecture  
into predicting the intensity and the track forecast,  
which is, in fact, what you want to do ultimately.  
Let's train this architecture so that it really  
knows where it should go.  
And now, I have signal to back propagate and use  
gradient descent exactly as we have  
covered in previous sessions.  
Same thing will happen here.  
And the idea is, if I train a model successfully  
to predict the intensity and the track  
in an end-to-end manner With this supervised learning,  
since I have the labels, it turns out  
that you can extract features from the representations that  
happened in previous layers in your network.  
So for instance, what the transformer will  
feed into the fully connected layer,  
this final vector, if this final vector  
can be used for a final high quality forecast,  
it also means that this vector contains  
lots of precious information.  
How could you forecast properly if this vector is not  
encoding precious information?  
So instead of feeding this precious information  
into this final fully connected layer, I just take it for me.  
I store it somewhere.  
And I'm going to reuse it in a later step.  
So I repeat the overall idea.  
I'm training this entire architecture  
to forecast something.  
I know my target is intensity and track.  
While it's training, the model is learning  
some internal features.  
Maybe you remember in convolutional neural networks  
where I mentioned that the deeper you go,  
the more the model is going to combine edges and parts to make  
the final prediction.  
Exact same thing is happening right now.  
My transformer is understanding for itself  
some interesting features that we do not understand as humans,  
but make a lot of sense for computer algorithms.  
I want to reuse those features that  
are compressed representations of the entire initial data.  
And I'm going to take them to feed them  
in the rest of my pipeline that I showed you previously  
with the gradient-boosted trees.  
We can make this even more complex, in fact.  
You can also include extra information  
in this overall network.  
The beauty of neural networks is that you can  
have them being very modular.  
You can adapt the architecture to your liking.  
And I can decide to give even more hints for my predictions  
by including the statistical data that I know.  
Remember that I have a whole time series of information  
with weather features, and I have  
the information of the location of the hurricane,  
the storm features.  
I can take those and give them to the transformer  
as well for every single step involved.  
So this is exactly what I'm doing right now.  
On top of the vector of information extracted  
from the convolutional neural network,  
I'm going to append the statistical data that correspond  
to this exact time step.  
So now my transformer has even more information and context  
to properly make the final prediction, which  
means the features extracted by the transformer  
will be even better.  
So the idea of end-to-end learning  
is you have a specific target, and while you train,  
you're able to get good features.  
You can just take those features and reuse them  
in a later stage with other methods.  
So now we completed, in fact, the step  
of getting my vision embeddings.  
I was able, using the transformer and CNN,  
to transform my sequence of initial images into one vector  
that I could extract after training completely the model.  
The idea is you train the model.  
You freeze this entire model.  
It's now fixed.  
It won't move anymore.  
And you just use that as your feature extractor  
by taking the values that happen at the very end  
of your architecture.  
The good thing about this method is that it's very modular.  
You can add more modalities if you need  
and have any feature extraction technique you want.  
Let's say that the state of the art has changed around CNN  
and transformers.  
Instead of using my previous method that I showed,  
you can adapt and choose an entirely different  
neural network and still maintain  
this overall mechanism of collecting, extracting,  
and predicting.  
I also want to mention that it's still quite of an art  
to figure out how to extract the best features possible.  
And then I iterated a lot for months,  
in fact, to figure out what would  
be the appropriate transformer and CNN combination  
to get good features.  
So there is lots of research and work involved.  
But then if you use the proper combination  
and you look into how good those features were  
into this new pipeline that you're seeing,  
collect, extract, predict, it's a back and forth  
and looping process.  
So of course, there is lots of research involved there.  
I just mentioned it's modular.  
Here you can just add whatever new modality  
you have, for instance, a new type of satellite imagery.  
You are going to use another type of feature extractor.  
And you will get additional embeddings,  
meaning additional vectors, that you can just combine all of them  
together by concatenating them.  
So you fuse this information.  
You use whatever machine learning model of your choice  
to make the final forecast.  
And you can train this final machine learning model.  
And you can tune the different parameters involved.  
I want to show you just a few results.  
What matters is to understand why we really wanted  
to do this feature extraction.  
After all, I already trained a model  
that is a transformer and CNN to directly forecast  
the final intensity and track.  
But why did I really need to extract those features?  
In fact, it made it even better because  
the gradient-boosted tree is able to look  
at these features extracted in a different manner  
than a neural network.  
Gradient-boosted trees are very good.  
On top of this, don't forget that I  
combined some vision embeddings with, again,  
the statistical data.  
So I was able to have all those features coming along  
into a model that is very good at that.  
So there is value in extracting features and recombining them.  
Sometimes an end-to-end architecture  
is just doing as good.  
In this specific scenario for hurricanes,  
that was valuable to use the feature extraction.  
And now if we compare the performance  
with some of the best models from the National Hurricane  
Center, we can see that we are really  
at par with how well they perform,  
which is really good news.  
It shows that having an AI pipeline  
could potentially really transform the meteorology field.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L4.5 AI Opportunities in Weather Forecasting and Beyond  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: And I want to repeat this,  
that this is an ongoing field and companies like Google  
are really pushing that forward.  
There is so much interest into predicting the weather properly.  
We need good weather forecasts all the time.  
And as you know, people talk about weather also all the time.  
You want to know how to prepare.  
You want to know how agriculture should function, if planes  
can fly properly, how to evacuate  
if you have natural disasters.  
You have so many reasons why weather is so important.  
So Google has investigating a method  
around graph neural networks.  
That's something we do not cover in this module  
but it's also very exciting.  
It's looking at the data in the shape of a graph.  
And you can use that for weather forecasting.  
It works extremely well.  
So to summarize what we covered around multimodality,  
we have identified a mechanism of collecting data,  
extracting relevant features.  
And there are so many methods to do this I gave one of them  
with CNN and transformers.  
Now that you have those features,  
you push them through a machine learning or operations research  
model to predict or prescribe something.  
This is very modular.  
You can adapt this for tropical cyclone forecasting  
but also for other topics like ecosystem conservation, which  
I've done, or health care operations.  
The idea is really you have multiple modalities.  
You push them into different architectures  
to get valuable features.  
You combine those valuable features  
you extracted into a final outcome.  
Notice that there exists so many modern methodologies  
to not even need to extract features anymore  
and have some end-to-end architecture, meaning you  
start from the input and you get the output immediately.  
I would really say that all those approaches may  
work sometimes and may fail in others.  
So keep in mind the overall panel of opportunity  
that you have.  
Sometimes end-to-end is enough.  
Sometimes a feature extraction has valuable reasons  
to be implemented.  
For instance, when you have very different  
modalities and it becomes way too challenging  
to have an end-to-end mechanism.  
Keep looking into this topic.  
There are so many applications of multimodal machine learning  
involved with satellite imagery.  
You can help people facing earthquakes, wildfires, floods,  
identifying climate change, getting a precise agriculture,  
having a better understanding of reforestation or deforestation.  
So much data lies out there publicly available for free.  
And using methods, combining multimodality  
could really help us tackle some of the most pressing issues  
of our world.  
When it comes to opportunities with AI and meteorology,  
here are a few takeaways for you.  
First of all, realize that AI is leveraging decades  
of historical data to make the predictions so it's  
a data-driven approach.  
AI can be multimodal and can leverage data  
from so many different formats.  
It can be sparse data and very structured data like tables  
but also it can be images and completely unstructured--  
language.  
AI models are also trained to identify patterns  
and relationships in this data.  
And traditional machine learning models  
may not have the complexity and capability  
to identify the patterns.  
So that's the beauty of neural networks.  
And it's very important to realize that AI is not using  
physics to make predictions.  
AI is making its own rules.  
And it tries to discover its own physical rules of the world.  
But sometimes it understands the world  
in a way that looks like it is how it operates.  
But in fact, it's not exactly the truth.  
So always be aware that it's a power and a strength  
that it can extract its rules on its own but also sometimes  
a challenge because it can make out rules that are not correct.  
AI is super fast at predicting so it's  
a great value for the weather field.  
And the technology is getting more and more mature  
and accurate.  
One big takeaway that I want to transmit overall  
with this entire module is that we need more multidisciplinary  
approaches, more collaborations with people in the fields.  
This is one of the reasons why we are  
building this entire course.  
We want you to come along, to talk to each other,  
to figure out how all together we'll find new solutions,  
because we have more concepts involved  
and we can really tackle more pressing challenges.  
If you do those collaborations, we'll  
be able to have models that can adapt and improve better.  
And AI is very promising in weather forecasting  
and could even leverage physics-based knowledge.  
It doesn't mean we need to stop at just pure data-driven.  
We can combine the two worlds.  
AI won't replace us.  
It will really complement, augment, and enhance  
all our existing methods.  
And your creativity and your collaboration  
with all your friends and colleagues  
will matter and make the big change.  
I just want to finish with one fun  
little thing that it turns out that some birds are  
some of the best predictors of hurricanes in the world.  
Birds have an internal mechanism that we don't understand well  
in their brain that allows them to know exactly when they should  
migrate to avoid the hurricanes.  
It's such a mystery.  
And it also means that there is so much more we can discover.  
So different types of data--  
I don't really know what the birds are able to perceive.  
Is it electromagnetism?  
Is it a really good understanding of the pressure?  
No idea.  
But this is so mysterious.  
So keep pushing your creativity, thinking  
outside of the boundaries, and looking  
into so many different fields.  
I wish you the very best in your endeavors.  
And I hope all the content we covered can help you.  
I really encourage you to keep exploring, reading online,  
and taking more modules.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture introduced multimodality—combining multiple data sources to make better predictions—and showed it through a hurricane forecasting case study.

Key Takeaways:  
Multimodality is everywhere: real systems (weather, healthcare, robotics) need to fuse tables, time series, images, and text—like humans do.  
Hurricane forecasting is naturally multimodal: combine satellite imagery (across space, time, altitude) with storm time-series/tabular features.  
Core pipeline: collect → align → extract → predict  
Align modalities by time/location  
Extract embeddings (CNN \+ transformer for imagery sequences)  
Fuse by concatenating vectors  
Predict with models like gradient-boosted trees  
Main result/insight: multimodal AI can match strong forecasters and works best as an extra model in an ensemble, complementing physics-based methods.  
\`\`\`

Lecture 5: Multimodal Multitask Learning  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 5: Multimodal Multitask Learning, taught by Professor Yu Ma, Assistant Professor at the University of Wisconsin.

What do diagnosing heart disease, predicting hospital length of stay, and spotting a tumor in a scan all have in common?

They all rely on multimodal, multitask machine learning — models that combine different kinds of medical data and make multiple predictions at once.

This lecture introduces the foundations of this new paradigm:

From single-task to multitask: Traditional models predict one outcome at a time. But in healthcare, conditions are interdependent. Multitask learning trains models to capture shared signals — like irregular heart rhythms or genetic biomarkers — that matter across outcomes.  
Why multimodality matters: Patients generate many data types: images, time series, notes, labs. Each holds complementary information. Combining them helps build a fuller clinical picture.  
Training smarter models: Shared representations allow knowledge transfer across tasks, while task-specific branches specialize for classification, regression, or even clustering.  
Keeping models interpretable: Attention mechanisms let models decide how much to share across tasks — transparent enough for clinicians to trust, but still powerful enough to converge.  
The impact? Multimodal, multitask models like M3H don’t just boost predictive accuracy by double digits. They also support real-world hospital operations — unifying deterioration prediction, discharge planning, and resource allocation under one predictive umbrella.  
By the end, you’ll see how healthcare AI is moving beyond isolated models toward holistic systems that mirror how clinicians actually think: integrating diverse signals, balancing multiple goals, and powering smarter, more coordinated decisions.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain why traditional single-task models in healthcare are limited, and how multitask learning leverages shared signals across outcomes.  
Describe multimodal data sources in medicine (images, time series, EHR, clinical notes) and explain how combining them improves prediction.  
Interpret how shared representations and task-specific heads work together to support classification, regression, and clustering tasks.  
Discuss why clustering is challenging in deep learning and how methods like autoencoders with k-means or surrogate losses address this.  
Analyze the role of structured attention mechanisms in selectively sharing information across tasks while maintaining interpretability.  
Evaluate the impact of multimodal, multitask models like M3H on predictive accuracy, generalization, and real-world hospital operations.  
\`\`\`

L5.1 Why Multimodal Multitask Learning Matters in Healthcare  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, my name is Yu Ma.  
I'm a PhD candidate here at MIT, and I'll  
be guiding you through this lecture  
on multimodal, multitask machine learning in health care.  
In this lecture, we'll explore how  
combining different types of medical data, as you have seen  
in previous lectures, such as images  
and clinical notes, along with a new concept,  
multitask learning, which makes multiple clinical predictions  
simultaneously, can be integrated  
to make better predictions.  
To understand why multimodal, multitask  
machine learning matters today, it's  
useful to take a step back and look  
at where we are with existing clinical support tools.  
This chart that you see here lays out  
several very well-known clinical models in terms of their two  
key axes.  
On the y-axis, we consider how general the data sources  
are, from very simple demographic features  
to rich high-dimensional modalities,  
like images, language, and multisource data.  
On the x-axis, we measure how general  
the tasks are from a single clinical prediction  
in a specific setting, to more ambitious models that  
aim to make many predictions across multiple clinical  
domains.  
Every single reference here corresponds  
to a landmark paper or system, and you'll  
notice that most existing tools actually  
cluster around the bottom left, which kind of correspond  
to the single-task models that rely on very limited data types.  
And even some of the more advanced models,  
like those using general EHR data, image data, language data,  
still actually operate within one clinical setting  
or a problem class.  
But more recent works, marked here in blue,  
aims to actually push that boundary a little bit more,  
which implies can we possibly learn across multiple data  
sources and across multiple clinical tasks  
at once and simultaneously.  
In this module, we'll talk about how this paradigm shift, which  
tours multimodal multitask machine learning,  
can really help us build smarter models for healthcare decision  
support.  
To begin, let's take a look at how model selection is actually  
traditionally done in health care machine learning.  
Suppose we're trying to solve one clinical problem.  
We would typically split the data set into training  
and testing sets, run cross-validation  
over several model types, and then select the model  
with the best average performance  
on that particular task.  
And after verifying it performs well on a test set,  
we'll deploy it in practice.  
So this is a very solid and very widely adopted  
approach, both in academia as well as in industry.  
But here's a small catch.  
It only treats each clinical task in isolation.  
For instance, we might separately build models  
for deterioration prediction, procedure scheduling,  
surgical planning, or even domestic violence prevention.  
And each of them gets its own model  
being trained completely independently,  
optimized independently, and being deployed independently.  
But what are we really leaving on the table  
with this in-silo approach?  
In many cases, these tasks are not really truly independent,  
but rather patterns that help predict  
deterioration could potentially signal a longer length of stay.  
So think about this patient's condition simply  
not being very healthy and they deteriorated,  
which will prolong the entire stay of their hospital  
admission.  
Information being very useful for procedure scheduling  
might also overlap with insights from surgical planning.  
So the question becomes, if I stick with the classical model  
selection, one task, one model at a time,  
what are some of the shared signals that we are discarding?  
Can we potentially do better by learning across these tasks  
jointly?  
So let's try to dive into one very concrete example,  
cardiology.  
Traditionally, as we have said, AI models  
are very much built to predict a single cardiac condition.  
For instance, we might train a model  
to predict ejection fraction based  
on some EKG data or a separate model  
to predict sudden cardiac death.  
So these are very powerful tools in isolation.  
And as we see in literature, as well as in practice,  
a lot of their performances are very, very strong.  
But they are missing something critical,  
which are these clinical context doesn't always happen in silo.  
They think about in terms of the patient  
and how these risks actually interact with each other.  
So instead of building a single model per outcome,  
we actually aim to build models that can simultaneously  
predict multiple cardiac endpoints  
and in this case, a single model that jointly predicts ejection  
fraction and sudden cardiac death  
from the same time series and EKG data.  
So why does this matter?  
Because shared physiological signals,  
like irregular rhythms, waveform patterns, or vital sign shift,  
may be relevant across multiple conditions.  
And by training on these tasks together,  
the model can learn shared representations  
and become more clinically insightful.  
We also see a very similar opportunity in oncology,  
where most existing AI models in cancer care  
are really designed to predict a single endpoint.  
For example, one model might classify  
whether a tumor is malignant or benign,  
while the other model estimates the stage of cancer  
once it's been diagnosed.  
And these models tend to work completely independently,  
even though both predictions rely on overlapping patient  
data, like genetics, pathology reports, or EHR information.  
But again, from a clinical perspective,  
these outcomes are very much deeply connected to each other.  
You don't just want to know if someone has cancer.  
You also want to know how far it has already progressed  
and how aggressively it should be treated.  
And that's why our goal is to move towards models that, again,  
jointly predict multiple oncology  
endpoints, like classification and staging,  
at the exact same time.  
And in this particular case, we'll  
be using genetics and structure EHR data  
to drive these predictions.  
And the hope is that, again, some  
shared biological signals, either genetic mutations,  
biomarkers, treatment response patterns,  
can potentially enrich both tasks  
while being learned together.  
And this type of multitask setup really  
allows us to make diagnostic tools that  
feel closer to how oncologists actually think.  
So in both cardiology and oncology,  
we saw that clinical tasks don't happen in isolation.  
Conditions co-occur.  
Diagnostics are interconnected.  
And treatment decisions often depend  
on multiple, simultaneous diagnostic predictions.  
So a natural question becomes, how  
can we potentially design models that actually learn  
all of these outcomes together?  
And instead of treating each one on its own problem,  
the core idea is this, rather than  
training a single model per outcome,  
let's train a single model that can learn multiple clinically  
relevant tasks at once.  
And mathematically speaking, we are given an input x.  
This is precisely the exact same as a single task problem  
that we have seen up until this point.  
But instead of building m--  
think about this as m different types of endpoints, conditions  
that we're considering.  
Instead of building m separate models  
to predict different types of outcome,  
y1, y2 all the way to ym, let's try to learn a joint function  
f that outputs all of them simultaneously.  
The way which we can accomplish this  
is through multitask learning, which  
is a branch of technique from the computer science community,  
recently explored across a lot of different areas.  
And the core idea is the availability  
of a shared learning component.  
But what exactly is the intuition of this setup?  
And why would it actually improve performance?  
This particular slide that you see next  
illustrates precisely the core intuition.  
On the left, we have a standard approach  
to separate models trained independently  
to predict two outcomes A and B. Every single model you see  
receives the same input embedding, which  
is a fixed-length, numerical representation of the data,  
in this case a patient.  
But because there are no shared learning,  
the two tasks cannot benefit from each other.  
Maybe model A learns something useful about comorbidities  
or lab values that could have helped model B,  
but that information never gets transferred.  
On the right, however, we have a shared learning network  
for multitask learning.  
And remember, this really is the key for multitask learning.  
Now, the same input goes through this shared layers,  
whose parameters are being jointly optimized and jointly  
learned from both tasks.  
And what happens here is very important.  
The model begins to learn more generalizable patterns that are  
useful across both outcomes.  
And it can focus on commonalities, for example,  
elevated inflammation or shared risk markers,  
and refine them jointly together,  
which is precisely what leads to these more accurate and stable  
predictions.  
And let's try and go one layer slightly deeper  
into the training, as well as inference process.  
In multitask learning, we're not just  
sharing these model parameters.  
We're actually augmenting the data implicitly  
by exposing every single task to information from others.  
During training, when we are computing the loss for task A,  
that loss back propagates through the shared network,  
updating the parameters.  
But later, when we're trying to train task B,  
it benefits from that trained, updated shared network,  
meaning that task A's signal has now indirectly helped  
with task B's learning.  
So even though we don't directly feed task A's outcome  
into task B's input, it is as if task B  
has access to the hidden representation of information  
regarding task A's outcome.  
And you can think about this as a very subtle form  
or implicit form of data augmentation,  
where we are enriching every training  
example by letting related outcomes inform one another.  
And during inference, we don't need  
both labels or both outcomes, really just the input.  
But the model already carries these shared representation  
during training, which can then lead to stronger generalization.  
So when the tasks are related, multitask learning  
creates a kind of implicit collaboration,  
where each task becomes a teacher for the others.  
And this is exactly what we mean when  
we say multitask models are more than the sum of their parts.  
Before we move on, let's clarify how multitask learning differs  
from another very common strategy, transfer learning.  
On the left, we see transfer learning in action.  
And this is a sequential approach,  
where first a model is trained on task A, typically  
a large or general purpose task.  
Then that trained model, or some part of it, is transferred  
and fine tuned on task B. This works  
very well when you don't have much data for the second task,  
and the first task is similar enough  
to provide a meaningful head start.  
But notice that learning is one directional,  
where task A informs task B, but not the other way around.  
Now contrast with multitask learning, shown on the right.  
Here you see multiple tasks, say tasks A, B, and C,  
are being trained together simultaneously through a shared  
learning representation.  
And every single task both teaches as well as  
learns from the others.  
And these shared layers are being updated jointly  
so that every gradient step is informed by multiple objectives.  
And this two-way communication is what gives multitask learning  
its power where especially in domains  
like health, where outcomes are naturally interrelated.  
So while both methods aim to reuse knowledge,  
multitask learning is a more collaborative process, not just  
a handoff from one task to another.  
And that collaboration often leads to better generalization,  
faster learning, and also deeper representation  
of the original information.  
So far, we've talked about why multitask learning is  
powerful on its own, but in health care,  
we often have another challenge, but also  
from another angle, opportunity, which  
is the presence of multiple data modalities.  
So think about a typical hospital setting.  
You have images like X-ray MRIs, tabular data, like demographics  
and lab values, time series, like vitals,  
as well as monitoring of your heart rate,  
language data from clinical notes and EKG reports.  
Each of these data types really carries  
complementary information about the patient,  
but integrating them into a single model is nontrivial.  
And this brings us to the key idea of our framework.  
So first we'll extract features from each modality using  
finetuned models, like a CNN from images or transformers  
for clinical notes.  
Then we align these features into a shared-learning embedding  
space, using contrastive learning,  
to make sure that the representations  
from different modalities are compatible.  
Once we have that unified representation,  
we pass it into a shared learning network,  
often with task-specific branches  
and shared attention blocks to really support  
multitask prediction.  
And finally, we produce a task-specific output,  
like prediction of heart failure, which  
is a binary classification problem;  
chest pathology identification, a multiclass classification  
problem; length of stay, a regression problem;  
or patient subgroupings, an unsupervised cluster.  
And a nice property of this framework  
is that it's very modular, where if you  
have a new modality of data or a new task  
that you're interested in learning more about,  
you can add them without redesigning the entire pipeline.  
It is also scalable because everything  
is trained end to end.  
This is what makes it truly multimodal and multitask,  
a single model that pulls insights  
from a diverse clinical data modalities to try  
and power through a wide range of medical predictions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L5.2 Advancing Multimodal Multitask Learning: Architecture and Applications  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: After learning a shared representation  
across all data modalities, we now route  
that embedding into task specific networks,  
where each is being customized to its prediction type.  
You can see the structure of these branches here.  
We have a binary classification head for tasks,  
like heart failure prediction, multi-class classification,  
for example, identifying specific chest pathologies.  
Each task specific head starts with a wide expansion,  
larger hidden dimensions that help the model capture  
generalizable patterns and subtle variations in the shared  
embedding.  
Then we progressively shrink the layers,  
as we move closer to the final prediction,  
essentially distilling the general signal  
into task specific outputs.  
These branches are optimized jointly with the shared layers,  
but they're free to learn task relevant features that  
may not be shared.  
This balance between shared learning and task specialization  
is what allows the framework to scale  
across a wide range of medical tasks,  
from classification to regression  
to unsupervised clustering.  
Among all the tasks specific networks that we showed earlier,  
clustering stands out as one of the most difficult to implement  
in deep learning.  
And why is that the case?  
Because clustering centroids are not naturally  
being learned in a typical neural network training.  
Unlike classification or regression,  
there is no ground truth label or gradient  
path that cleanly defines what makes a very good cluster.  
So instead, to achieve the two goals of homogeneity  
within the cluster and, second, separability between clusters,  
we adopt a two-step approach, where in step number one,  
we train an autoencoder, which learns  
to compress and reconstruct the input,  
forcing the model to create a meaningful latent space.  
The better the reconstruction, the more  
structure we have captured.  
In step number two, we perform k-means clustering directly  
on that latent space.  
This allows us to assign samples to clusters  
that are separable and interpretable, as you  
can see in the TSNN visualization  
plot on the bottom left.  
But there's more.  
We have two design options as well.  
So one approach is I can treat cluster centroid  
as learnable parameters and try to optimize them jointly  
with the autoencoder.  
The other is to build a deep clustering network that  
uses a surrogate loss.  
So for example, think about a soft cluster assignments  
with KL divergence or entropy regularization  
to guide the network toward clean separations.  
Both methods can actually work very well in practice,  
and the choice really depends on the complexity of the data,  
as well as the downstream user case.  
So even in unsupervised tasks, like phenotyping,  
we apply the same principle, use shared learning representations.  
But let the head specialize and adapt  
to the tasks unique structure.  
So far, we've talked about the power of shared learning, using  
a common backbone to jointly learn multiple tasks.  
But there is one very important question  
that remains, just exactly, how can we  
make this shared component more interesting and more  
intelligent, which gives us better performance?  
Now, first of all, not every single task  
benefit equally from every part of the input,  
and some features might be highly relevant for prediction  
of deterioration, but not so useful  
for the forecasting of length of stay.  
So instead of sharing everything blindly,  
we asked a simple question, can we potentially design  
a mechanism that can selectively share knowledge based on what's  
relevant for every single task?  
And that brings us to attention mechanism,  
and the very first step is to generate  
what's called task specific versions of the input embedding.  
And, so here, you can see that the same input embedding, say  
from EHR or images, is being passed through different task  
specific subnetworks.  
One tailors the features for deterioration prediction,  
and the other modifies them for a length of stay.  
And these embeddings are now task aware.  
Even though they came from the same original input,  
they've been tuned to reflect what's  
most useful for each prediction, and this sets us up  
for the next piece, which is designing an attention  
mechanism that lets us decide what to share, how much,  
and with who.  
Now that we've created these task  
specific embeddings, the next challenge is simple,  
how do we actually combine them in a very meaningful way?  
We want the model to not just share information,  
but rather to really learn how much to share  
between these particular tasks.  
And this is precisely where the attention mechanism comes in.  
On the left, you see these modified embeddings  
for two tasks, let's say, deterioration and length  
of stay.  
In the middle, we introduce a learned attention weight matrix,  
where each row represents a target task,  
and every single column represents a source task.  
So the value in row D and column LOS  
tells us how much the deterioration model should  
pay attention to the length of stays' models representation,  
and vice versa.  
In this case, we see something interesting,  
and the deterioration task places approximately 60%  
of the weight on length of stay.  
But the length of stay task relies more on itself.  
This means that there is a asymmetry inside this weight  
matrix, and it's very important, because it reflects  
that the task relationships are often directional and not  
symmetric.  
Finally, we apply these attention weights  
to the task specific embeddings, producing  
an attended representation for every single task.  
This allows the model to integrate useful information  
across tasks in a way that is learned and optimized  
during training.  
So we've moved on from share layers to task specific inputs  
to task aware, attention driven collaborations, which  
is especially valuable in very complex clinical settings, where  
relationships between outcomes can be very subtle and very  
dynamic.  
In theory, the attention mechanism we just described  
should work very well.  
But actually, in practice, especially in large multitask  
models, convergence actually becomes a huge challenge.  
In traditional deep learning setups,  
the common solution is overparameterization,  
which, basically, means let me stack multiple attention layers,  
add some different types skip connections,  
and repeat this process many, many times.  
And this helps with convergence.  
But in clinical settings, this particular approach actually  
creates a new, very significant problem,  
which is these deep attention stacks becomes  
way too complex to be interpreted  
by the physicians who are actually using these models.  
And clinicians cannot usually reason just exactly why one task  
relies on another or how much information is being flowed  
across different predictions.  
So let's try and take a different path.  
Instead of many attention layers,  
we'll just use a single layer, where  
it's one matrix of learned attention weights across tasks.  
And the benefit, it's transparent,  
interpretable, and we can visualize it completely  
directly.  
But here's a trade off.  
So instead, in this case, in order  
to encourage the convergence behavior, while still  
retaining interpretability, we'll  
impose a simple structure on the attention weight.  
Specifically, we'll try to emphasize  
the original task itself, or what  
we call the source task in the attention matrix, as follows.  
In the example, we see that the deterioration tasks now  
places 90% of the attention on itself and only 10%  
on length of stay.  
Meanwhile, the length of stay task  
allocates 80% of the attention to itself  
with 20% to deterioration, and these constraints  
guides the learning process by ensuring  
that the model doesn't lose focus on its primary objective.  
But again, it still allows for some space  
for a measured and cross-task information flow.  
And the result is an attention mechanism  
that is, first, clinically a lot more interpretable  
and intuitive, a lot more easier to debug,  
as well, and still able to converge with just a single pass  
of the attention layer.  
And the result is an attention mechanism  
that is, first, clinically a lot more interpretable  
and intuitive, a lot more easier to debug,  
as well, and still able to converge with just a single pass  
of the attention layer.  
So what happens when we put this entire framework,  
multimodal inputs, multitask output, share attention  
mechanism into practice?  
We'll try to evaluate our model, M3H, on the mimic four data set,  
which are drawn from patients at MGH,  
as well as Beth Israel Hospital.  
This data set includes over 12,000 patient day samples  
spanning over a rich combination of data types,  
including tabular, time series, clinical notes,  
as well as medical images.  
And we didn't just test it on a few benchmarks.  
We actually evaluated it across 44 distinct health tasks,  
including 39 diagnostic prediction tasks covering  
16 clinical departments, three operational forecasting tasks,  
such as length of stay and discharge prediction,  
one unsupervised patient phenotyping task  
using our clustering head, and one large scale chest  
pathology classification task.  
As you can see in the result on the right,  
M3H consistently outperforms traditional single task  
learning models, where on average, we  
observed a 11.4% performance improvement being measured  
across task appropriate metrics, such as AUC  
for binary classification problems,  
R squared for regression problem,  
and the silhouette score for clustering.  
This includes improvements in high impact areas,  
like heart failure, ischemic heart disease, diabetes,  
and obesity, some of the most widely studied diseases  
in clinical literature.  
By learning from multiple data types  
and coordinating across tasks, M3H  
delivers meaningful improvements in both accuracy  
and clinical relevance.  
To further evaluate how generalizable M3H is,  
we looked at its performance across the four most  
commonly seen machine learning problem types in health care.  
In each subplot here, you see a direct comparison  
between single task learning on the left and multitask learning  
on the right.  
And let's try to take a step back and reflect  
on what these results really mean beyond model performances.  
In health care system, predictive tools  
are really rarely used in isolation.  
Clinical outcomes, such as deterioration, discharge volume,  
and length of stay are all tightly  
interdependent with each other.  
So, for example, instead of separate models run in silo,  
ICU prediction of predicting deterioration, the word  
managers trying to forecast a length of stay, the discharge  
planners trying to estimate the daily volumes,  
we can now actually bring all of these tasks  
under a single predictive umbrella  
and allow them to try and make decisions altogether.  
This naturally supports a more collaborative care planning  
and delivery across the hospital system.  
And the implication for hospital operations  
is also simple, but powerful, that instead  
of moving from reactive staffing and bat  
allocation towards a more proactive  
and cross-departmental planning informed by a unified prediction  
and unified knowledge, this is exactly  
the kind of systematic coordination  
that modern health systems are striving for.  
And, so as we close, we see that multimodal, multitask models,  
like M3H, don't just offer technical improvements,  
but really allow for a more organizational improvement  
in how care is being planned, delivered, and being optimized.  
While this talk has focused on health care, the framework we  
developed, multimodal, multitask machine  
learning with structured attention,  
isn't just limited to medicine.  
In fact, this setup applies very naturally  
to a wide range of domains, where, first, multiple data  
types are available, second, several interrelated outcomes  
need to be predicted, and third, where interpretability  
and coordination really matter.  
For instance, in sustainability, researchers  
have already used multitask learning  
to improve biomolecular production  
and estimate greenhouse gas emission, where data comes  
from molecular simulation, sensor logs, and production  
records.  
In manufacturing, as well, it's being  
used for quality control and inspection  
automation, combining sensor data, images and operator  
reports.  
And in online platforms, multitask setups  
have powered a recommendation engines  
as auction optimization and sentiment analysis, each drawing  
from behavioral data, text and interaction graphs.  
And the core insight is wherever multiple outcomes share  
a signal and a diverse data types exist,  
multimodal, multitask machine learning, like frameworks,  
can really offer a way to learn more holistically.  
So while we designed this model for health care,  
the underlying principles are a lot more broadly applicable  
and can really help push the different boundaries  
of a wide range of socially and economically critical domains.  
In this lecture, in conclusion, we  
explored how multitask learning can  
be used to build more generalizable and clinically  
useful machine learning models.  
We also saw how combining data from multiple modalities,  
like images, time series, and clinical notes,  
can predict multiple outcomes simultaneously, can really  
improve performance, and allow coordination across tasks  
better reflect how clinicians actually reason  
in real world care settings.  
We also walked through our proposed structured attention  
mechanism, which brings more interpretability  
and measured knowledge sharing into multitask models,  
making them not only effective, but also easier to trust  
and deploy in clinical workflows.  
These ideas extend beyond just health.  
Whether you are working on hospital operations,  
sustainability, manufacturing, or online platforms,  
multimodal multitask models can really  
help you unify fragmented data and align multiple decision  
goals.  
Thank you so much for being here today,  
and I hope this gives you new tools and new ideas  
for how we can build a smarter and more integrated AI system  
for the real world in health.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture introduced multimodal, multitask machine learning in healthcare, showing how jointly learning from multiple medical data types and predicting multiple clinical outcomes at once can produce more accurate, coordinated, and clinically useful AI systems.

Key Takeaways:  
Beyond single-task models: Traditional healthcare AI trains one model per outcome. Multitask learning instead trains a single model to predict multiple related outcomes simultaneously, capturing shared clinical signals.  
Why multitask works: Shared layers allow tasks to learn from each other through joint optimization, creating stronger, more generalizable representations than siloed models.  
Multimodal integration: Combine images, time series, structured EHR data, and clinical notes by extracting modality-specific embeddings and aligning them into a shared representation space.  
Structured attention for selective sharing: A learned attention matrix controls how much each task borrows from others—balancing performance, convergence, and interpretability for clinicians.  
M3H framework results: On MIMIC-IV (44 tasks), the multimodal multitask model outperformed single-task baselines, improving diagnostic prediction, operational forecasting, and patient phenotyping.  
System-level impact: Joint models better reflect real clinical workflows, enabling coordinated decisions across deterioration prediction, length of stay, discharge planning, and beyond.  
Broader insight: Wherever multiple related outcomes and diverse data types coexist, multimodal multitask learning offers a unified, scalable, and interpretable approach to AI design.  
\`\`\`

Recitation 1: Multimodal Learning: HAIM  
\`\`\`  
Skip to main content  
Recitation Overview  
Welcome to Recitation 1, taught by Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.

In this session, we’ll work through hands-on examples and practice exercises to reinforce the concepts covered in the lectures, focusing on Multimodal Learning with tabular, text, and image data. The notebook used in this Recitation is available at the following link:

Recitation 1 Notebook

For data agreement reasons, the data used to run this notebook are not provided. Although you cannot run the notebook, you can still explore the code and the outputs\!

If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Lectures covered by this recitation

Lecture 2: HAIM: Holistic AI for Medicine: An Application of Multimodal AI  
Let’s dive in and explore the material together\!

Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.  
\`\`\`

R1.1 Introduction to Multimodal Learning with MIMIC  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
Welcome.  
So today's focus is on multimodality.  
And as you've seen in the lectures of this module,  
multimodal learning involves combining information  
from different sources, especially,  
for example, text, like clinical notes  
or any other form of text that is available,  
tabular data, like, for example, demographics, medical images,  
for example, chest x-rays, and time series,  
like lab measurements, events that changed over time,  
vitals, et cetera.  
These examples are not random.  
We picked them because they reflect  
the data set we are going to work with today.  
In this module, you have mainly discussed  
a form of applying multimodal machine learning, which  
is fusion.  
Fusion refers to a way of combining the modalities  
in order to potentially get better  
predictive performance compared to just using them individually.  
Today, we are going to work with the MIMIC data set.  
MIMIC data set is a publicly available, de-identified data  
set from patients that were in the ICU of the Beth Israel  
Medical Center.  
It includes, as we kind of mentioned  
earlier in the example, demographics, clinical notes,  
different imaging data, and different time series data,  
namely labs, vitals, and medications.  
Although MIMIC is a publicly available data set,  
there are data agreements that prevent us  
from displaying or showing any raw patient data  
in order to maintain privacy.  
For this reason, we are not going to visualize all the data  
that we have.  
So we are going to run the code on the data,  
but we're not going to visualize the raw information that  
corresponds to each patient.  
The goal of today's recitation is  
to see how we can perform multimodal machine learning  
in order to predict the existence of pleural effusion  
in different patient's lungs, for patients, as we discussed,  
that are already admitted to the ICU.  
Each row of our data corresponds to a specific patient,  
and the goal is to train separate XGBoost models  
to predict pleural effusion.  
And we want to compare how these XGBoost models perform  
when we train them on each modality separately,  
and when we also train one combined fusion model  
and explore how combining these modalities improves performance.  
We are going to evaluate the models using the AUC  
metric that you've already seen in the introductory modules.  
So let's start, as usual, and we are  
going to first import the packages in the libraries  
we are going to use in the rest of the notebook.  
There is one package that is not already included  
in Google Colab, TorchXrayVision.  
That is why we have to install it separately,  
and then after installing it, import it  
as the rest of the packages.  
For time efficiency reasons, we are not  
going to run the notebook live, it is already run,  
and we are going to explain the code  
and also interpret the results without running  
the cells simultaneously.  
As I mentioned earlier, for data agreement purposes,  
we cannot display the raw data from MIMIC.  
However, we can briefly explore some of the information  
they contain.  
The data are already saved in my Google Drive main folder.  
And after I connect the Google Colab, the notebook,  
to my Google Drive, I can actually load the data.  
And you can see here that we first have the tabular data,  
then we have time series, we have nodes,  
and we also have the images.  
And as you can see here, we load two separate files  
for the images because the first file just contains information  
about the image identifiers, the specific images  
that we want to load.  
And the second I am loading, the images variable  
corresponds to the actual arrays that  
contain the information about the different pixels.  
Basically the arrays that contain the images themselves.  
And this is in the form of a dictionary  
where each key can also be found in the CSV file,  
the df img csv file that we load right above.  
So after we load our data, let's just do a very brief exploration  
to have a general idea of how the data looks like.  
First of all, for the tabular data,  
we observe that there are different demographics that  
are included in the data frame.  
This information is static.  
It does not change over time for each patient.  
And that is why we consider this data static tabular and not  
time series.  
So we first print the number of rows our data frame has.  
And this is roughly the same for all  
of the rest of the data frames.  
In case one of them has fewer rows,  
this means that there is not available data in this modality  
for this specific patient.  
As you can see, we roughly have 10,000 different rows.  
Each row corresponds to a certain patient  
and a certain admission to the ICU.  
And the tabular data, the tabular data frame,  
contains these specific columns that we have printed here.  
Apart from identifiers, like the subject ID, the admission ID,  
and this identifier that combines information  
about the subject and the state, and this  
is the identifier we will use throughout this recitation,  
we can see that the tabular data frame contains information  
about the patient's age, gender, ethnicity, marital status,  
language, and insurance.  
So these six columns here correspond  
to the actual information about the demographics.  
Now, in order to encode this information  
in a way that can be processed by our machine learning models,  
we encode this, we have already encoded this,  
into integer values, and each of the integer  
values correspond to a specific value  
from the initial column that has a natural meaning.  
The last column of our data frame  
is called pleural effusion, and as you might guess,  
it corresponds to the target, to the label, that we will  
want to predict eventually.  
Now moving on to the time series,  
we can see examples of different measurements  
that are contained in this data frame  
and change over time, for example, lab values.  
The time series data frame has this label column  
that contains information about each of what type of time series  
event each row corresponds to.  
And if we print the unique values, all the set  
of the unique values of this column,  
we can see that we have, for example, heart rate,  
respiratory rate, the oxygen saturation,  
and other measurements, like the platelet count, glucose,  
hemoglobin, et cetera.  
These can change throughout each patient's stay in the ICU.  
So that is why we consider them varying and not static  
as the demographics.  
And that is why we treat them as a separate modality  
and we are going to process them in a different way,  
as we'll see shortly.  
Now the next modality that we loaded was nodes.  
We have three types of nodes available.  
This information is located in the node category column.  
And the different types of nodes we have  
are echoes, radiology reports, and ECGs.  
And as far as the images are concerned,  
we have the df img data frame that we loaded earlier.  
As we briefly discussed, this mainly  
contains the image IDs we want to focus on for each patient.  
The actual images are located in the images dictionary.  
We note that each patient might have multiple images,  
might have multiple instances of nodes, and of course,  
multiple measurements of time series data.  
And aggregating these different instances across the modalities  
is not necessarily straightforward.  
And there are multiple ways that can be done based on our needs  
and the specifics of the data set.  
Here we're going to explore one of these ways.  
We're going to discuss this a bit later.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.2 Embedding Tabular and Time Series Data  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, let's move on to the second step of our pipeline.  
After loading the data, we need to extract embeddings.  
What do we mean by embeddings?  
As you have already seen in different modules,  
embeddings can be thought of as summaries  
of the information that is contained in the raw data.  
Let's start from the tabular data.  
Tabular embeddings are more or less  
the information that we already have on the demographics.  
As we said earlier, we want the encoded information  
so that it is usable by a machine learning model.  
So we keep the age as is.  
And then for the rest of the columns that  
were all non-numerical, we actually  
keep the encoded numerical version.  
We also keep our target variable, pleural effusion,  
that we are going to use when we move to the prediction task  
later on.  
So more or less, as you can see for tabular data,  
embeddings is just the raw tabular data themselves.  
There's not much that is done because they are already  
encoded in a way where each row corresponds to a patient  
and has static information about this patient  
in a numerical form.  
Moving on to the time series, for each  
of the signals that we have or each of the events that we have,  
we extract summary statistics because we  
don't want to have multiple rows for each of the patients,  
because if each row corresponds to a different timestamp  
where these values were calculated,  
we will end up with a bigger data frame that will not  
have a one-to-one correspondence between one  
identifier and a single row.  
So we want to have a single row for each identifier.  
And to achieve that, we calculate these summary  
statistics.  
Here, we calculate the max, which  
is the maximum value in the time series for a specific traffic  
signal, lab value, and event.  
We have the minimum.  
We have the average.  
We have the variance, which encodes the variability,  
of course, of the value.  
We also calculate what we call meandiff, which is basically  
the mean of the differences between consecutive values.  
Maxdiff encodes the largest absolute jump  
between two consecutive values.  
And basically this helps detect how smooth our data are.  
Then we have the mean abs diff, which  
corresponds to the average of the absolute differences  
between consecutive values.  
And then we have the sum abs diff,  
which encodes the total variation over time  
because it actually corresponds to the sum of all  
the absolute differences.  
We also calculate the difference,  
the change in value between the first and the last time point,  
the number of peaks--  
and by the number of peaks, we mean  
the number of local peaks, which helps us assess how many  
oscillations we have in the data.  
So it kind of encodes the form of the data  
if we plotted the signal over time.  
And last but not least, we also calculate the trend.  
The trend corresponds to the slope of a line that  
fits best through the values.  
For example, a positive trend indicates an increasing pattern.  
A negative trend indicates, of course,  
the opposite-- a decreasing pattern.  
All these values summarizes how our time-varying signal  
changes over time.  
And by calculating all of them for each of the signals  
or events we want to encode, we have  
captured the full information for each  
of the different variables we want to use.  
These variables or events are contained in this list here  
called "Event list."  
For example, we saw some examples earlier too.  
We have glucose, potassium, sodium,  
different kinds of measurements, et cetera.  
These are the events we want to focus on.  
Then we have defined this \[? get time series ds, ?\]  
standing for time series embeddings function, where  
basically we calculate all of these metrics and statistics  
that we already talked about.  
Here, you can see that we filter our data to only focus  
on the event of interest.  
We sort our values based on the chart time of each measurement.  
And then we have defined functions  
that calculate the number of local peaks and the trend.  
And we have this dictionary that basically,  
for each of the statistics that we want to measure,  
that we want to calculate, we have  
defined the corresponding function  
that will be applied to each of the features.  
So here we group our data frame by our identifier,  
so by patient, and by label, where  
label is each of the events.  
We keep the value of each of these measurements.  
And we apply all these functions that we have  
defined in this dictionary.  
And by performing this line, we basically  
make sure that for each of the features that we want to use,  
we have calculated all of the different statistics  
that we want to keep.  
In order to have one column per statistic and per feature,  
we apply this pivot function, which  
basically turns the data frame and flips  
the rows and the columns of the data frame.  
In case we have missing values, we  
can choose to fill them with this fillna function here.  
In case we want to use these as tensors,  
which is not something that we are going to do today--  
but for completeness, we have included it--  
we can use these two lines to convert basically  
our data to tensors.  
After applying this function to our time series data,  
we end up with a data frame, where each row corresponds  
to a single identifier, to a single patient,  
and contains all the extracted statistics for each  
of the events in the events list that we specified.  
This data frame contains roughly 452 columns.  
An example of this column is max glucose,  
where, for example, for all of the patients  
vertically-- for each of the rows,  
we have their maximum value of glucose.  
Then we might have mean glucose that  
corresponds to the minimum value of glucose, et cetera.  
This is the same for all of the variables  
that are included in this event.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.3 Embedding Clinical Notes and Images  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Moving on to the nodes modality,  
we are going to focus on how to extract numerical embeddings  
from raw clinical notes using the pre-trained ClinicalBERT  
model.  
Basically, what this model does is that it converts the raw text  
to meaningful representations, which,  
as you know from previous modules, we call embeddings.  
We note here that BERT has a maximum input  
length of 512 tokens.  
So in case the nodes that we have in hand  
are larger than that, we need to split them into smaller  
overlapping chunks.  
We want to make sure that the chunks are overlapping to ensure  
that, in case there is information that is related  
to the core of the chunk, we don't miss it  
because it's cut at the edges.  
Each chunk is then tokenized, padded, and passed  
through the model in batches.  
From each chunk, we are going to extract  
the embedding of a specific CLS token, which  
captures its overall meaning.  
It's not important to remember the specific token,  
but it comes from a spot in the architecture of the model that  
basically makes sure that this embedding captures  
the meaning of the input node.  
We then group the resulting embeddings by  
node because we have one embedding per chunk.  
So then we group them by node so that each clinical node  
is represented as a list of embeddings, one per chunk,  
which can then be used in general downstream machine  
learning models and in our specific case for the prediction  
of pleural effusion.  
We note here that each patient might have multiple nodes  
instances.  
And as we said earlier, each node instance  
can consist of multiple chunks.  
So in order to get a single embedding per patient,  
because this is exactly what we want  
to have at the end of the day, we need to aggregate in some way  
the embeddings that correspond to each chunk and also  
each node.  
Here, what we're going to do is we're going to average  
the embeddings that correspond to each node and also across  
nodes to extract a single 768-dimensional embedding that  
will summarize all the node information for each patient.  
And we're going to see how this is performed  
in more detail in the code.  
Moving on to the images, we want to extract visual embeddings  
from chest X-ray images that we have available for our data set.  
In order to do that, we use a pre-trained DenseNet model,  
and each image is first pre-processed.  
It's converted to grayscale.  
It's resized and normalized.  
And then we pass this image through the model  
again in batches.  
For each image, the model returns both prediction logits  
and intermediate deep features, basically representations,  
which are combined into a single embedding.  
These embeddings are then saved in a data frame.  
And we can choose again how we are going to combine them.  
We can average them.  
We can keep only the first.  
We can concatenate the first with the average.  
Again, there are different ways of combining them.  
We select to use the average approach  
here too, as with the node case, as we'll see very briefly.  
get\_chest-x-ray\_embeddings is the function  
that actually takes as input the images, a list of images,  
and passes the images through our DenseNet model  
that we load here.  
We do this per batch, as we just mentioned.  
And before we pass each image through the model,  
we perform a bit of pre-processing.  
We normalize the image between 0 and 1\.  
We convert to a single channel in case there are more channels.  
And we append each processed image in the processed images  
list that we have already defined.  
Then we get our final batch tensor  
after we convert the NumPy images to tensors.  
And we pass the batch tensor through the model.  
These lines here are used to extract the dense features,  
these representations that can be thought  
about as the embeddings we got from the language model  
that we used earlier for the nodes.  
And then eventually, if we just pass the batch tensor  
through our model, in the end, we get the prediction logits.  
So for each combination of dense features and predictions,  
we save them.  
We create a combined embedding, and we save them together.  
Now, to build the data frame for the embeddings,  
we first call the get\_chest\_x-ray\_embeddings here.  
And then we select the aggregation function  
based on the aggregation method we want to use.  
And then eventually we just group the embeddings  
using the aggregation function that we have defined.  
In our specific case, we first convert our dictionary of images  
to a list of images.  
And then we use the build\_chest\_x-ray\_feature\_df  
function that we just went over to basically extract  
the embeddings.  
Again, its row corresponds to a certain patient.  
And we have a single column that has the tensor  
of the full embedding.  
This is why we again use this code snippet here,  
as we did with the node embeddings,  
to basically expand this to a data frame  
with a full set of columns, where each column corresponds  
to a single element of the embedding.  
We end up with 1,024 columns, because this is the output  
dimension of the model combined with the predictions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.4 Single-Modality vs. Multimodal Models  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed1.50xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: For the last part of our recitation,  
we are going to use the embeddings we extracted from all  
these modalities to train XGBoost models in order  
to predict pleural effusion, as we discussed in the beginning.  
We have four modalities.  
We have our tabular data.  
We have our chest X-rays, our clinical notes,  
and our time series.  
And we are first going to train one model per modality.  
And then we are going to combine the different modalities  
by concatenating their embeddings, their features,  
to train a model on the full information we  
have on the patient.  
Here we define our training function,  
where basically, we perform a train-test split of our data.  
We define our XGBoost classifier and some parameters here.  
We also have the fit function that fits the classifier.  
And then we have the probabilities  
that we get at the output and then  
the AUC score that we calculate at the end on our tests.  
First of all, we want to make sure  
that all the data frames have the same identifier  
as their index.  
And we also want to make sure that all  
the entries of the pleural effusion labels are valid.  
So we filter here our tabular embeddings data  
frame to keep only the rows where the pleural effusion  
values are either 0 or 1 to exclude any minus 1 values  
that we might have, which encode uncertainty  
about the actual label, about the ground truth.  
And then we have all the different embeddings.  
We set the index to the identifier column.  
We want to make sure that we have  
the exact same set of patients across all of the modalities.  
So in case there is missing information  
about a patient in one modality, in this very specific code,  
we exclude this patient.  
But in general, we can deal with it in different ways.  
We can add zeros instead of values for this modality.  
We can do different things.  
We can impute in different ways.  
Here we choose to just exclude these patients  
since they are not many.  
So we find the common IDs, the common identifiers.  
For each of the modalities, we only  
keep this set of patients in our final data set.  
Then we extract our labels from our tabular data  
frame, the pleural effusion.  
And then we get our X's, which are pretty much  
the exact same thing as the original data frames  
apart from the tabular data frame,  
where we have to drop the pleural effusion  
column because it is our target column.  
The second step here is to train models per modality.  
Using this syntax, we combine the tab name  
to the X tab data, the image, the X image, et cetera.  
And using the train XGB function,  
we basically train separate models  
using each of the modalities.  
And we save the probabilities and the resulting AUCs.  
Finally, we combine all of our data in a single data frame  
by performing this horizontal stack operation here.  
So we stack all of the X's for the different modalities.  
And we train our XGBoost model using all  
of the available embeddings.  
After we train all of these models, we display our results.  
And we can see that our model that was trained only  
on the tabular data had a very low performance of only 62.6%,  
which makes sense because we cannot really infer whether  
a patient has pleural effusion by just looking  
at their demographics.  
Of course, age might play a role.  
But it is not straightforward.  
Then we have a very good performance  
from the images where we achieve an 83% AUC,  
notes achieved a 79.3% AUC, and time series a 72.7%, roughly.  
Now, if we combine all of these modalities,  
we end up with 85% AUC, which is improved over each  
of the single modalities.  
As we can see here, we can also plot these values in a bar plot.  
And we can see clearly that the combined model, the model  
trained using the combined embeddings, is better than all  
of them.  
It is close to the image modality.  
It is close to the highest available modality.  
But even two percentage points increase  
can be very, very important for individual patients.  
So we, more or less, demonstrate that multimodality helps.  
It helps us improve our performance.  
The performance improvement sometimes can be more,  
sometimes can be less.  
We cannot know a priori how much combining the different  
modalities will help us.  
But it is definitely worth trying  
combining different modalities because we, basically,  
combine different sources of information.  
And this can lead to improved downstream performance.  
So this is all for today.  
We're going to briefly mention some key takeaways  
from today's recitation.  
What did we learn?  
We show that multimodal learning integrates different data types.  
We had structured data, tabular, clinical notes, imaging,  
the chest X-rays, and time series.  
And it combines and integrates all these data types  
in order to potentially improve predictive performance  
in health care, as we saw today, but also in other domains.  
We have domain-specific embeddings.  
And by domain here, we mean we have different embeddings  
for the nodes, different embeddings for the images, which  
capture modality-specific information.  
And this is important for the performance  
of the downstream predictive models  
at the end of the pipeline.  
We also saw that the models we trained on each modality  
separately can provide insight into how  
each of the data sources performs  
and how powerful each modality is.  
Then we also saw, and that was the most important part  
of today's recitation, that actually combining  
the modalities leads to better performance  
in the downstream task.  
We performed fusion, which is simple concatenation  
of the different embeddings we extracted.  
Even this simple operation highlights the importance  
of combining information that comes from different sources.  
\[? Mimic ?\] data are not synthetic.  
So they are real-world.  
And they enable a realistic evaluation of our models  
on complex tasks, like diagnosing pleural effusion.  
There are also other pathologies one  
can work with, like pneumonia or other potential conditions.  
And it enables us to basically explore  
how multimodality works in a variety  
of different downstream tasks.  
But of course, today we chose one of them  
to discuss in this recitation.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Recitation Summary  
In this recitation, we applied multimodal machine learning to the MIMIC ICU dataset to predict pleural effusion. We worked with four data types: tabular demographics, time series labs and vitals, clinical notes, and chest X-rays. For each modality, we extracted embeddings—summary statistics for time series, ClinicalBERT embeddings for notes, DenseNet features for images, and encoded values for tabular data. We then trained XGBoost models separately on each modality and finally combined them into a fusion model by concatenating embeddings.

Key takeaways:  
Each modality captures different aspects of patient information: demographics (basic context), time series (dynamic changes), notes (clinical insights), and images (visual evidence).  
Performance varied by modality, with images and notes outperforming tabular data.  
Fusion consistently improved performance beyond single modalities, demonstrating the power of multimodality in healthcare prediction tasks.  
Congratulations on completing this recitation\! You now have hands-on experience in building and comparing unimodal and multimodal models, showing how integrating diverse data sources can lead to better clinical predictions.  
\`\`\`

Assignments  
\`\`\`  
Skip to main content  
Overview  
Welcome to Assignment 1\! This assignment builds on what we have learned in this module. In particular, we will deepen our understanding of data exploration, embeddings from different modalities (tabular, text, and images), and fusion strategies (early vs. late fusion) for prediction tasks.

Questions in this assignment are based on the following notebook:

Assignment 1 Notebook

Due to potential memory issues, you are advised to not run this notebook on the server and just review the outputs.

This notebook is complete — all code has already been written and executed — so you will see the outputs from each code cell. Your task is to use these outputs, along with the concepts covered in this module, to answer the questions in this assignment.

Lectures covered by this assignment

Lecture 2: HAIM: Holistic AI for Medicine: An Application of Multimodal AI  
If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Good luck\!  
\`\`\`

Skip to main content  
The Problem

Every year, thousands of pets are listed online for adoption. Some are adopted quickly, while others take much longer. Predicting how fast a pet will be adopted can help shelters write better descriptions, prioritize resources, and improve adoption chances.

This is a multimodal prediction problem because each pet has multiple kinds of data:

Tabular data (e.g., age, breed, color, sterilization status).  
Text descriptions (free-form text written by the shelter).  
Images (photos uploaded with the listing).  
Our goal is to combine these different data sources and build a model that predicts the Adoption Speed of each pet.

The Dataset: PetFinder.my Adoption Data

We will use the PetFinder.my dataset, which was originally part of a Kaggle competition.

Size: \~12,000 training examples.

Inputs:

Tabular: structured features about each pet.  
Text: a short description provided by the shelter.  
Images: at least one photo per pet.  
Target: AdoptionSpeed (0 \= same day, 4 \= not adopted after 100+ days).  
After visualizing the first rows of the training dataframe, we focus on the columns of our dataset:

PetID \- Unique hash ID of pet profile  
AdoptionSpeed \- Categorical speed of adoption. Lower is faster. This is the value to predict. See below section for more info.  
Type \- Type of animal (1 \= Dog, 2 \= Cat)  
Name \- Name of pet (Empty if not named)  
Age \- Age of pet when listed, in months  
Breed1 \- Primary breed of pet (Refer to BreedLabels dictionary)  
Breed2 \- Secondary breed of pet, if pet is of mixed breed (Refer to BreedLabels dictionary)  
Gender \- Gender of pet (1 \= Male, 2 \= Female, 3 \= Mixed, if profile represents group of pets)  
Color1 \- Color 1 of pet (Refer to ColorLabels dictionary)  
Color2 \- Color 2 of pet (Refer to ColorLabels dictionary)  
Color3 \- Color 3 of pet (Refer to ColorLabels dictionary)  
MaturitySize \- Size at maturity (1 \= Small, 2 \= Medium, 3 \= Large, 4 \= Extra Large, 0 \= Not Specified)  
FurLength \- Fur length (1 \= Short, 2 \= Medium, 3 \= Long, 0 \= Not Specified)  
Vaccinated \- Pet has been vaccinated (1 \= Yes, 2 \= No, 3 \= Not Sure)  
Dewormed \- Pet has been dewormed (1 \= Yes, 2 \= No, 3 \= Not Sure)  
Sterilized \- Pet has been spayed / neutered (1 \= Yes, 2 \= No, 3 \= Not Sure)  
Health \- Health Condition (1 \= Healthy, 2 \= Minor Injury, 3 \= Serious Injury, 0 \= Not Specified)  
Quantity \- Number of pets represented in profile  
Fee \- Adoption fee (0 \= Free)  
State \- State location in Malaysia (Refer to StateLabels dictionary)  
RescuerID \- Unique hash ID of rescuer  
VideoAmt \- Total uploaded videos for this pet  
PhotoAmt \- Total uploaded photos for this pet  
Description \- Profile write-up for this pet.  
Question 1  
0.0/1.0 point (graded)  
Which of the following columns are useful features to keep in our model? (Select all that apply.)

PetID

Age

Breed1

Gender

MaturitySize

FurLength

AdoptionSpeed

Vaccinated

Sterilized

Health

Fee

RescuerID

State  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 4 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

We now plot the distribution of AdoptionSpeed.

Bar chart showing the distribution of adoption speed categories (0 \= fastest, 4 \= not adopted), with most observations in categories 2 and 4 and very few in category 0\.

Question 2  
0.0/1.0 point (graded)  
What does the distribution of AdoptionSpeed in our dataset look like? (Select all that apply.)

Pets that were never adopted are the largest group.

Most pets are adopted extremely quickly (category 0 dominates).

The categories are perfectly balanced.

Very fast adoptions are rare.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Why do we convert the 5-category AdoptionSpeed target into a binary variable? (Select all that apply.)

To guarantee perfectly balanced classes.

To simplify the prediction problem into two outcomes.

To reduce sparsity across categories.

Because machine learning models cannot handle multiple classes.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
1 point possible (graded)  
Which of the following challenges is most specific to modeling the Description text compared to tabular features?

Text data does not require any preprocessing.

Text descriptions are always shorter than tabular feature vectors.

Text data requires converting variable-length inputs into fixed-size representations.

Text features cannot be combined with tabular features in a single model.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
1 point possible (graded)  
Why might adding image features hurt model performance if they are not handled carefully?

Image embeddings are typically high-dimensional and can lead to overfitting when data or regularization is insufficient.

Image features prevent the model from learning linear relationships in tabular data.

Image-based models cannot be trained jointly with text and tabular features.

Images introduce label noise because visual content is weakly correlated with adoption outcomes.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
In this part, we are going to extract embeddings from each of the different modalities — tabular, text, and images.

For tabular data, we transform categorical and numeric features into a structured embedding space.  
For text descriptions, we use a pre-trained language model to capture the semantic meaning of each pet’s profile.  
For images, we use a convolutional neural network (ResNet18) to generate feature vectors that represent visual characteristics of the pets.  
These embeddings provide a unified numerical representation across modalities, making it possible to train models that combine heterogeneous inputs.

Question 1  
0.0/1.0 point (graded)  
When preparing the tabular features, we noticed that there are no missing values in the dataset. Why is this useful information for model training? (Select all that apply.)

It means we don’t need extra preprocessing to handle NaNs.

It guarantees that the dataset has no errors or inconsistencies.

It simplifies training because every feature column already contains valid entries.

It ensures that the model will automatically perform better.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
Why do we convert pet descriptions into embeddings using a pre-trained language model such as all-MiniLM-L6-v2? (Select all that apply.)

To map variable-length text descriptions into fixed-length numeric vectors suitable for downstream models.

To assign a unique integer ID to each word appearing in the description.

To encode semantic information that reflects meaning, context, and similarity between descriptions.

To simply count how often each word appears in the text (bag-of-words).  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
1 point possible (graded)  
From a modeling perspective, why is it useful that text embeddings have a fixed dimensionality?

It allows them to be concatenated with tabular and image embeddings

It ensures faster adoption predictions

It removes the need for feature scaling

It guarantees the embeddings are unbiased  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
1 point possible (graded)  
Why is normalization especially important when comparing embeddings across different images?

It reduces variability caused by lighting or intensity differences

It guarantees semantic similarity is perfectly preserved

It removes all background information from the image

It ensures that all embeddings have exactly the same norm  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
1 point possible (graded)  
What is a key advantage of using a pretrained image encoder rather than training an image model from scratch in this setting?

It makes image embeddings perfectly interpretable

It reduces the risk of overfitting when the available dataset is relatively small

It guarantees that image embeddings will dominate other modalities

It eliminates the need for labeled data entirely  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 6  
0.0/1.0 point (graded)

A shelter wants to update its adoption model weekly as new pet listings arrive. The team considers fine-tuning ResNet18 each week using the newly collected data instead of keeping it frozen.

Which concern is most relevant in this scenario?

Weekly fine-tuning may cause the image embeddings to drift over time, making model behavior harder to compare across weeks

The CNN will stop producing fixed-length embeddings

Fine-tuning forces the task to become unsupervised

Fine-tuning will prevent the model from using tabular and text features  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
In this part, we tackle a binary classification task: predicting whether each pet will be adopted quickly. We begin by training models on each individual modality (tabular, text, and image) to evaluate their standalone predictive power. Afterward, we explore how to combine modalities using two common strategies — early fusion (merging feature representations before training) and late fusion (ensembling predictions from separate models).

Question 1  
1 point possible (graded)  
Why might a simple binary classifier still struggle even after aligning all modalities correctly?

Binary labels eliminate the need for regularization

The adoption outcome may depend on complex, nonlinear interactions between features

Alignment removes too much data to train a classifier

Binary classification always leads to underfitting  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
You notice that all three single-modality models achieve AUCs above 0.60 but none exceed 0.70. Which interpretation is most appropriate at this stage?

The models are severely underfitting and cannot learn meaningful patterns

The predictions are random

Each modality contains some predictive signal, but none is sufficient alone

The task is impossible to solve reliably  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
A practitioner skips unimodal evaluation and directly trains an early-fusion model. What risks does this introduce? (Select all that apply.)

Improvements or failures may be incorrectly attributed to fusion rather than to a single strong or weak modality

The fused model will necessarily perform worse than all unimodal models

It becomes difficult to diagnose which modality is helping or hurting performance

The learning problem implicitly changes from supervised to unsupervised  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

So far, we trained models on each modality separately (tabular, text, image). However, each modality captures different aspects of the adoption process — structured attributes, textual descriptions, and visual appearance. Early fusion means we simply concatenate the embeddings from all modalities into a single feature vector and train a model on top.

This way, the model can learn interactions across modalities (e.g., certain breeds in certain images with certain textual cues), potentially improving predictive power.

Question 4  
1 point possible (graded)  
What is the core idea behind early fusion in multimodal learning?

Randomly selecting one modality per sample to reduce bias

Using a neural network to alternate training between modalities in different epochs.

Combining feature representations from all modalities before model training

Training separate models for each modality and averaging their predictions  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

We plot the Early Fusion AUC results across modalities. Bar chart comparing AUC scores by modality on the PetFinder dataset, showing that the combined multimodal model achieves a slightly higher performance compared with tabular, text, and image modalities individually.

Question 5  
1 point possible (graded)  
Based on the AUC results shown (tabular ≈ 0.67, text ≈ 0.61, image ≈ 0.63, combined ≈ 0.69), what best explains why early fusion improves performance?

Because the strongest unimodal signal dominates the fused model

Because concatenation removes noise from weaker modalities

Because combining modalities allows the model to exploit complementary information

Because adding more features always increases test AUC  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 6  
1 point possible (graded)  
Given the unimodal and fused AUC results, which modeling decision is best supported by the evidence?

Replace early fusion with late fusion immediately

Use tabular features only, since they dominate performance

Keep all modalities but monitor overfitting and marginal gains

Drop text and image modalities to simplify the model  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

With late fusion, you don’t concatenate features. Instead, you train a separate model per modality (tabular, text, image) and then combine their predictions at the end—e.g., by averaging/weighting the predicted probabilities or training a small meta-model on those probabilities.

Question 7  
1 point possible (graded)  
Which scenario would most strongly favor late fusion over early fusion?

The task is unsupervised

All modalities are extremely low-dimensional

Only one modality is available at inference time

Modalities have very different feature scales and distributions  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 8  
0.0/1.0 point (graded)  
In this task, late fusion outperforms early fusion. Which of the following reasons best explain why this can happen? (Select all that apply.)

Each unimodal model can focus on learning patterns specific to its data type before combining predictions

Late fusion avoids creating a very high-dimensional joint feature space that may overfit

Combining predictions allows the model to balance strengths and weaknesses across modalities

Late fusion guarantees better performance than early fusion for any dataset  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 9  
1 point possible (graded)  
A team wants to deploy a fused model but must minimize retraining cost when one modality changes. Which fusion strategy is preferable?

Feature normalization

Late fusion

Dimensionality reduction

Early fusion  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
In this assignment, you explored how multimodal machine learning can be applied to predict pet adoption speed using the PetFinder.my dataset. You examined different data types — tabular features (age, breed, health, etc.), text descriptions, and images — and saw how each contributes unique information. You also learned how to extract embeddings from these modalities, evaluate their predictive power separately, and then combine them through early fusion (feature concatenation) and late fusion (ensembling predictions).

Key takeaways:  
Different modalities capture complementary signals: tabular features gave the strongest baseline, but text and images added valuable context.  
Embeddings transform raw data (structured, text, image) into numerical representations suitable for models.  
Early fusion can improve performance by combining features directly, while late fusion often performs best by leveraging modality specialization.  
Preprocessing (alignment of PetIDs, normalization, handling multiple inputs per pet) is crucial for fair comparison across modalities.  
Congratulations on completing this assignment\! You now understand how multimodal learning can integrate structured, textual, and visual data to improve real-world prediction tasks.  
\`\`\`

Module Summary  
\`\`\`  
Skip to main content  
Module Summary  
In this module, you explored how multimodal AI builds intelligence by combining diverse data types and addressing the unique challenges of representation, alignment, and reasoning across modalities.

Lecture 1 introduced the concept of modalities and traced the evolution of multimodal AI, highlighting its unique properties and six core challenges.  
Lecture 2 applied multimodal methods to healthcare through the HAIM framework, showing how integrating EHRs, labs, images, and notes improves predictive accuracy and decision support.  
Lecture 3 extended the discussion to large multimodal models, demonstrating how language models can be adapted with cross-attention, adapters, and diffusion techniques to handle vision, audio, and beyond.  
Lecture 4 showcased multimodal forecasting in climate science, where fusing satellite imagery, radar data, and tabular storm features improved hurricane prediction.  
Lecture 5 advanced to multimodal multitask learning, introducing structured attention for interpretability and showing how models like M3H support coordinated decision-making across dozens of healthcare tasks.  
Key Takeaways:  
Define what makes multimodal data unique and explain the six core challenges of multimodal AI.  
Describe how embeddings and fusion unify diverse modalities into shared representations.  
Compare single-task and multitask learning, and interpret how shared signals improve performance.  
Discuss how large multimodal models extend LLMs to richer inputs and outputs, including images, audio, and video.  
Evaluate real-world applications of multimodal AI in healthcare, climate forecasting, and other domains.  
Congratulations on completing this module\! With these foundations, you are ready to critically understand multimodal AI — not just as a technical framework, but as a way to unify fragmented data and support complex, interconnected decisions across medicine, science, and society.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.  
\`\`\`

