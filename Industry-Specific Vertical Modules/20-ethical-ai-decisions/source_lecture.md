Ethical AI for Decisions in Today’s World  
\`\`\`  
Introduction  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
My name is Swati Gupta, and I'm a faculty  
in the Operations Research and Statistics department at the MIT  
Sloan School of Management.  
Today, I'm very excited to talk to you about ethical AI  
for decisions in today's world.  
And to understand a lot of these concepts,  
we need to take the perspective of data models and decisions  
to unpack why ethical AI concerns arise in applications  
in today's world and how can we get ahead of them  
and build systems that are for everybody.  
So as we start, I would like to point out  
that AI is all around us.  
It's in recommendation platforms.  
It's in pricing algorithms, routing algorithms,  
matching algorithms that match drivers  
to riders that need a ride.  
It's in music recommendations.  
It's even in logistics and planning all around the world.  
However, with great power comes great responsibility.  
And so AI is all around us.  
It's amazing for increasing efficiency, increasing  
the scale of applications, increasing  
the access to automated pipelines  
through LLMs and GPT models.  
But it can also amplify disparities and have  
unintended consequences.  
And as we go through this module,  
I would like you to pay attention  
to what are the different conceptual frameworks you can  
keep in mind for understanding how these systems work  
but also to understand how to get ahead  
of unintended consequences and mitigate  
the impact that AI can have.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Lecture 1: Data, Models and Decisions in Ethical AI  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 1: Data, Models and Decisions in Ethical AI, taught by Professor Swati Gupta, Associate Professor, Operations Research and Statistics, MIT Sloan School of Management.

In the first lecture, we motivate why ethical considerations matter in AI and algorithmic decision-making, and introduce the data–model–decision pipeline as a framework for locating where harms can arise. We consider feedback loops, where model-driven decisions reshape future data and can amplify disparities over time. We close with a discussion of the meaning of “ethical” in this setting and by examining examples where missing these considerations led to unintended consequences.

Learning Objectives  
After these sessions, learners are able to:

Explain why ethical considerations are essential in AI and algorithmic decision-making, particularly in high-stakes contexts.  
Describe the data–model–decision pipeline.  
Recognize and analyze feedback loops in deployed systems and articulate how they can amplify negative impacts over time.  
Apply basic ethical lenses (e.g., fairness, accountability, transparency) to evaluate AI-enabled decision scenarios.  
Identify common sources of unintended consequences (e.g., underspecified goals, missing context) in real-world examples.  
\`\`\`

L1.1 What are Data, Models, and Decisions: Introduction  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Here is an example to perhaps start our discussion.  
So wildfires across the world have various causes.  
For example, in California, in US, 9.4%  
are due to electrical power line ignitions.  
California's Pacific Gas and Electrical Company  
introduced plant power shutoffs to reduce wildfire risk,  
cutting electricity across large areas.  
But these public safety power shutoff events  
can have various unintended consequences,  
even though they are very well meaning.  
The safety interventions can in fact  
shift the burden onto population with the least ability  
to absorb it.  
For example, on the slide, you see an LA Times article  
that talks about how PG\&E's power outages bring  
darkness, stress, and death to California's poor and elderly.  
So let's talk about why do unintended consequences  
happen in a lot of societal systems  
and especially which are enhanced due to the augmentation  
with AI.  
So this is a model that I want you to keep in mind.  
So think about the data that is being generated.  
And we'll specifically define what data is in this module.  
This data is then fed into the models that  
use AI, machine learning, and optimization to make  
data-driven decisions on a set of users  
that can be very diverse, that can have very different needs.  
And these decisions often interact with law and policy.  
When we make decisions in such a pipeline,  
then these can also create feedback loops  
and go and change the data that we are learning on.  
So the question I want to ask in this lecture is, how can we  
make ethical decisions for a complex demographic of users?  
Of course, to get to that question,  
we need to first understand what makes up  
data, models, and decisions, and what creates feedback loops.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.2 What are Data, Models, and Decisions: Data  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's start with data.  
Data is any recorded information that systems can  
use to learn or make decisions.  
So you've seen a lot of data around you.  
There's various types of data, like structured data,  
which incorporates tables, spreadsheets, for example loan  
data on who was given loan, what was  
the income of that person, what was the default rate, what  
was the risk associated with that person.  
That could be a historic data set  
that is being used to learn something else in the future.  
Data could be unstructured, for example, text data, audio data,  
images, like MRI scans.  
We are generating data in every aspect of our life.  
When we go and interact with a recommendation platform,  
the way our cursor moves on the screen creates a data.  
The news articles that we hover for longer on, that  
creates data.  
Other examples are environmental data,  
for example, the temperature, the rain, the amount of sunshine  
that an area received historically.  
We have a lot of health care data  
that's are immensely important for downstream health care  
decisions that we're going to talk  
a lot about in this segment.  
So health data can have things like vitals of a person,  
or labs that are run on a patient  
to measure various things.  
The lab visits, how often was this patient likely  
to adhere to doctor's advice, how  
much did they wait in a hospital waiting room, and so on.  
So there's various aspects of the health system  
that build on the health data that we generate around us.  
So data is great.  
It allows us to learn and make decisions in the future,  
but data also comes with problems.  
Data can be missing.  
It can be noisy.  
It can be incomplete.  
A lot of the data that we would like we may not have.  
So we might only have proxy data of what we actually  
want to measure.  
For example, for those of you in sales,  
you might know that we would like data  
about the demand of a product, but if we only have sales data,  
it gives us a partial picture because we  
don't capture missed sales due to the stock out of that item.  
So that item might actually run out in the store.  
Even though there was demand for that,  
we never see that demand because there's  
no sales when there's no inventory for the item.  
So the data that we might actually  
have to learn or make decisions for a particular task  
might be different, related, but different from the data  
that we would actually to have.  
Can you think of other examples of data  
that you would like to measure, but you only  
see a proxy of that?  
So let's go back to our power example.  
Here, the data used to make decisions  
of where to have a public safety shut-off event  
would involve the transmission network, weather data,  
so temperature, risk of wildfires in the past,  
and so on, and historical demand data.  
So where did people actually use more power during the day?  
How did the power consumption change over time?  
Which industrial nodes had more demand and so on?  
So all of this, you can see there  
are different types of data that we're using to make decisions  
in this setting.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.3 What are Data, Models, and Decisions: Models  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Next up, let's talk about models.  
What do we mean about models?  
So a model is a mathematical or computational representation  
that maps inputs to predictions or prescriptive decisions.  
That's a lot of words, so let's explain by examples.  
There's various types of models.  
So there could be a predictive model,  
which is trying to look at past data and predict something.  
For example, I could look at the past temperature data  
and try to predict the demand of heating oil in cold regions,  
like Boston.  
Or we could think about predicting a classification  
outcome.  
So think of these as 0-1 decisions.  
And so one could think about predicting perhaps hospital  
readmission.  
For a person who just received care at a hospital,  
what's the likelihood, what's the probability, what's  
a future potential outcome that this person might have  
a hospital readmission again?  
You can think about predictive models  
like recommendation systems.  
So based on what the user has liked in the past  
and how they've interacted with the system,  
a recommendation model would predict what kind of content,  
what kind of items, what kind of jobs would  
the user like to see again.  
There's other types of models like generative models, which  
include LLMs or diffusion models.  
For example, ChatGPT, it has a generative aspect to it.  
You can have a conversation.  
It's creating more data.  
So generative models are another class  
that might try to map inputs to something  
that we want to see as a decision or a prediction  
or a prescription.  
My favorite ones are the decision support models.  
So these are grounded in a lot of mathematics  
and very nice structure, for example, using optimization  
models, which take in the structure of decisions that  
are needed and use the data to make intelligent decisions that  
are more structured.  
So, for example, you could think about scheduling patients  
based on the predictions of risk.  
Now, I want you to pay attention to this example.  
It's a bit involved, because we have predictions of risk that's  
coming from a model that's predictive,  
and now we are layering it on another optimization module that  
says, now take the predictions of risk and schedule patients  
so that higher risk patients get care faster or sooner.  
They are prioritized.  
So in this sense models can be layered  
and they can interact in complex ways.  
They can generate data for other models that might use that data.  
So let's see an example of this.  
In our plant power outages example,  
the question that we would like the model to answer  
is, how can we allocate a given budget  
for undergrounding power lines to reduce the risk of wildfires?  
So it's an allocation problem where  
there is an amount of money that's available,  
and some infrastructure can be improved so that power lines are  
not overground and they don't run  
the risk of starting or igniting a wildfire due to overheating.  
So in this case, as we spoke before,  
there is some historical data that's on demand.  
There's some transmission data.  
There's some historical weather data.  
All of this data can be used to first predict  
the future demand in a region.  
It can be used to predict temperature and risk  
forecasts in that region, and these  
can be taken into account to now feed into an optimization  
system that tries to minimize load shedding, which  
is the amount of power cuts that happen using  
the predicted demand, so it's planning for the future  
so that wildfire risk is tolerable.  
The operating point of the system  
is below the wildfire risk that's considered unsafe.  
And the cost of undergrounding lines, so these transmission  
lines, one can underground them, and the cost of undergrounding  
is a few million per mile, so the cost  
of undergrounding these lines has to be within budget.  
Now, from our modeling perspective,  
we call this entire block as a model.  
It has a predictive part.  
It has some optimization part.  
Well, and that optimization can, again,  
lead to a prediction in the future.  
So models can be complex.  
They can be layered.  
They can interact with each other.  
They can generate data for other models downstream.  
And ultimately, all of this is used  
to make predictions or decisions.  
So these decisions of where the load will be shared  
is something that now the model will  
create as we move to the third part of our pipeline.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.4 What are Data, Models, and Decisions: Decisions  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let me close the loop on data driven decisions.  
So these decisions have been made  
by using data and models that try  
to capture the state of the world, that try to optimize  
various things, that try to predict things based  
on the past states of the world, that  
try to generate new data in interesting ways using diffusion  
models.  
And the decisions to guide who gets what, which resources,  
where resources go, how systems operate,  
those all form a part of the decisions one could take.  
So as we go through this module, I  
would like you to think about various high stake examples  
where decisions are made using automated pipelines with data  
models and decisions.  
For example, you could think about resource allocation,  
which is where and when to do load  
shedding of electric demand.  
We are allocating resources of undergrounding lines.  
In a health care setting, you can  
think about where to place donor organs.  
This is the most life critical resource there is in the world.  
You can think about who gets loans.  
That's also a resource allocation problem.  
Each of these problems impact critical aspects of our life,  
and therefore, it is really important  
to think about how to make ethical decisions  
in these domains.  
The decisions could be about people.  
They could be about who to hire, who to convict,  
who to admit in schools.  
Who do we want to provide educational and job  
opportunities to?  
The decisions can be about infrastructure planning,  
where to place facilities or warehouses, how  
to district cities.  
In these societal systems, decisions  
don't happen in a vacuum.  
They interact with not only people,  
but also with laws, societal expectations,  
and existing social systems.  
And as a result, these model driven choices and decisions  
can shape opportunity, access, and service at scale.  
We already see an unprecedented growth of AI in various sectors,  
and this is only going to increase exponentially  
in the future.  
So going back to our power outages example  
and understanding the impact of decisions.  
I want to highlight that often the consequence  
of these automated pipelines can fall on vulnerable populations.  
The burden on them can be higher.  
For example, if power is load shed in a particular community  
that is already facing a high wildfire risk,  
the hospitals in that area will also face power loss,  
access to fresh food will be reduced,  
and infrastructure can also impact how heat  
prepared different areas are.  
The problem is that low income households cannot invest  
in resilience as much as higher income households.  
For example, they may not have access  
to batteries or electric cars or generators,  
or home care for the elderly.  
And a lot of recent work, recent research  
highlights some of these unintended consequences that  
happen due to the automation of decisions  
due to pipelines that start with the goal of perhaps reducing  
wildfire risk, reducing load shedding,  
but ultimately, can have an unintended consequence because  
of the interaction of societal data,  
interaction of inequalities that exist in the society.  
And given the scale of AI, this can also cause disparate impact  
at scale.  
So as we end this segment, I would  
like you to reflect back on decisions  
taken by AI and automated pipelines in applications  
that you are interested in, that you have interacted with,  
that can perhaps create uneven impacts on people.  
This is a good muscle to develop,  
because as I've worked in this area for the last eight  
to nine years, I've realized that once you start  
paying attention to causes of disparate impacts on people,  
you can already start anticipating how AI applications  
might exacerbate these impacts.  
Keep these in mind as we move onwards to studying feedback  
loops in the next segment.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.5 What are Data, Models, and Decisions: Feedback Loops  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: All right.  
So we are now ready to talk about feedback loops.  
Feedback loops are basically a situation  
where the data-driven decision has now created more data,  
or it's changed the distribution of existing data.  
So let's formalize this a little bit.  
A feedback loop is when a system's output influences  
the future data it learns from, reinforcing patterns over time.  
So a common thing that can happen  
is model decisions, let's say, about who  
gets shown an ad, who is selected for a job,  
will impact outcomes and service on people,  
so who's even being measured for how good they are at a job  
and so on.  
And this generates new data due to changes in engagement.  
For example, if you are shown a particular set of jobs  
and you only interact with that, the model  
may not know or even generate the data  
of how you might interact with jobs  
that are a higher-pay packet or a higher range.  
So the models that we interact with  
can create outcomes and data that other models are also  
learning on, and feedback loops can create shifts  
in the data distribution.  
They can take the system to a better, longer-term outcome  
or worsen the system dynamics.  
And from an ethical AI perspective,  
it often helps us to think about long-term consequences  
of decisions which in a single time step or a single iteration  
may not seem as consequential, but if this continued  
over a long period of time, then they  
can be extremely influential.  
So let's start with a small example of Uber ratings,  
where the drivers' ratings data is  
taken in by matching models that match drivers to riders.  
The match that is actually realized then  
affects the right allocation and visibility of a driver,  
and this in turn can affect future ratings of drivers.  
So as a simple example, let's say,  
a driver has a car that is clean, but it's not fancy.  
And this driver's ratings data is  
being used to match drivers to different riders.  
And let's assume that the matching is always  
done to riders that perhaps expect a free water  
bottle in the car.  
Then this might start impacting this driver's rating  
in the future and lead to lower-quality matches.  
And this becomes a concern when the data from the decisions  
is feeding back and changing the distributions of data  
that we see and learn for in the future iterations.  
If you remember the previous example  
that we developed about load shedding,  
let's think about what kind of feedback loops  
can be expected in this planned power outages example.  
So one feedback that could happen  
is that this can impact the housing prices.  
And if the decisions of where to load shed  
are concentrated on certain areas,  
then this definitely impacts the housing prices.  
Areas that are more prone to load shedding  
will see a decline in the housing prices,  
which might then impact the historical demand data as well.  
So this creates a feedback loop that is perhaps not  
as straightforward as the driver ratings in the Uber example,  
but this is a very consequential feedback loop.  
In fact, there's been recent articles in LA Times,  
for example, where people have observed  
that moving to a climate disaster zone  
just to afford a home might be an unintended consequence  
of these societal systems that we might  
want to avoid in the future.  
So we don't want amplification of disparity,  
and to not sound like a broken record,  
at times these AI systems and automated decisions  
can compound poverty.  
And this really gets us to thinking about other feedback  
loops in automated systems around you.  
Can you think about consequences that recommendation systems can  
have or a job recommendation platform can have  
or shopping platforms can have on the revenue generated  
for various restaurants and vendors  
and how that might change the distribution of the data?  
So I feel like we are really getting to the key question,  
how can we make ethical decisions  
for a complex demographic of users?  
What does it mean to be ethical?  
And what's next?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.6 What does Ethical Mean?  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So far, we've discussed data  
for the data models decision pipeline,  
how do AI and optimization modules  
interact within that segment that's models,  
and what we mean by data-driven decisions.  
We've also talked about what are feedback loops  
and how they can change the distribution of data  
that future iterations of the algorithm are interacting with.  
So let's now get to the question of how can we  
make ethical decisions for a complex demographic of users,  
and what does it even mean to be ethical.  
There are various axes of ethics that we like to think about.  
For example, one could ask for systems to be fair.  
One could ask for systems to be robust, resilient, and reliable.  
One could ask for transparency, explainability, accountability,  
yada, yada, yada.  
There's a lot of things one could ask for.  
So let's start defining these one by one  
to give you a sense of what we are asking for.  
Bias, as a first, is when resulting technology privileges  
certain groups and harms others.  
As an example, we've already talked about the load shedding,  
the power outages, where the resulting technology  
that allocates budget for undergrounding,  
that load sheds in different areas  
can compound poverty in certain groups and privilege others.  
There's another cool example about this app  
that was actually developed in collaboration with MIT.  
It collects data on potholes in the roads.  
As users drive cars in the city, the app will use its algorithms  
and detect a pothole and send that information to the state  
government so they can schedule repairs.  
The problem with such technology is that people  
who were not aware of this app, who did not  
stay in neighborhoods where they could download  
this app on their iPhones, they missed the opportunity  
of using and automating this collection of where  
potholes exist.  
And so it seemed like there was no data on potholes  
in these neighborhoods, and no repairs were scheduled.  
So in relation to bias, fairness is  
ensuring that groups and individuals are not  
systematically disadvantaged.  
And so this would mean that we find ways of load shedding  
power in different areas so that the load shedding,  
the outages are not concentrated on certain areas,  
but we try to protect and help people  
build more resilience in the hospitals  
through generators and so on.  
Next up, let's talk about robustness and reliability.  
So robustness is ensuring that decisions from these systems  
are reasonable, even under noisy,  
unexpected, and adversarial situations.  
Reliability is in a similar vein, asking for systems  
to work as expected, even under unexpected conditions,  
like noisy data or data that has not ever been  
seen by an application before.  
So, for example, a vision model might fail  
because there's a sticker placed on a stop sign,  
and a lot of recent research tries to build this robustness  
into vision models so that stickers or stop signs are not  
misinterpreted as "go" signs by the cars.  
As we have more and more automated systems  
in self-driving cars, issues like this  
become even more important.  
The next example is about hiring people.  
Even though we might only have a noisy or imperfect signal on how  
qualified a person is for a job, then robustness  
would mean we still hired high quality people,  
and reliability would mean that we still  
hire people that are sufficiently qualified  
for a job so that the system doesn't fail in some sense.  
Let me next talk about transparency, explainability,  
and accountability.  
Transparency is asking systems to give some visibility  
to the stakeholders into how the system works.  
For example, think about an organ transplantation system.  
Patients and families of patients  
who interact with the system would  
like to know exactly how the process works so that, first  
of all, they can ensure that the way organs are allocated  
to various people who need them is fair, it is efficient,  
it is not creating a disparate impact.  
And transparency is also important to build trust  
that the people have into the system.  
Explainability in itself can mean different things  
to different people.  
Definitionally, we can say it is the degree to which humans  
can understand a model's internal logic  
or reasons for predictions, but it's slightly  
different from transparency.  
So for those of you who've heard about neural networks,  
for example, transparency could be  
about exactly telling you what are the weights on the edges,  
but explainability could say, well,  
if you input the data about humans that  
have a GPA of at least 3.5, that have a work  
experience of at least five years,  
for them the model will always make decisions that  
are high probability for interviewing them.  
So explainability, in some sense,  
is a set of rules or a set of interpretable ways of how  
a model or an automated decision-making system  
behaves, and transparency is more about how it was created,  
the process, maybe the internal variables it uses, and so on.  
And both of these definitions feed into accountability, first,  
asking the question on who is responsible for model outcomes.  
Is it the organization that has decided to use a specific model?  
Is it the programmer?  
Is it the people who generate the data and interact with that?  
Who's accountable?  
And accountability is a notion that  
also interacts with the law.  
So it includes mechanism for assigning responsibility  
from a legal perspective.  
So as you can see, these different ethical criteria  
are interconnected.  
Some of these can be addressed by algorithm design.  
Some of these have to be addressed  
by incorporating new laws or even  
asking the right questions on whether we should  
be using AI to make decisions in various life  
critical applications.  
So here is a rough partition.  
There are some ethics issues that  
talk about alignment of values, inclusivity  
of different populations, sustainability of technology  
and accessibility, so different people  
can interact with the technology if they would like.  
There are technological challenges,  
like ensuring robustness and reliability and usability  
of systems, even under noisy, missing, and errored data,  
for example.  
And there are legal concerns, like responsibility, process  
fairness, and accountability.  
But this is not all.  
There are many concerns that appear  
at the intersection of these three ways of thinking  
about the problem, like transparency and explainability  
is at an intersection of ethics and technological challenges.  
Human oversight and contestability  
are at the intersection of law and ethics.  
Data quality, integrity, auditability, security,  
and privacy talks about who owns the data.  
Can this data actually be used for the application  
it is intended for?  
Do users have rights for data?  
So for those of you who are sitting in the EU,  
you might have an insight into this with the GDPR.  
And there's also a lot of issues that  
sit in the intersection of all three  
of these areas, which is bias and fairness.  
How do we build systems that are fair?  
How do we build systems that are not biased?  
It's a technological question, but it's also  
a question that builds on laws.  
It's also a question that builds on what  
our societal expectations and ethics surrounding  
an application.  
So I would like you to take a moment  
at the end of this segment and think about,  
what happens if we build technology  
without these considerations?  
Have you come across unintended consequences of AI  
that perhaps was due to not having an eye  
towards ethical considerations in its design?  
And can you think about ways that we  
might avoid these concerns and consequences?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.7 Examples of Unintended Consequences  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: All right, so far, we've  
looked into the data model's decisions and feedback-loops  
pipeline.  
And we've talked about what makes different axes  
of ethical decision-making.  
So what happens if we build technology  
without these considerations?  
Let's go over a few examples in today's world,  
where we see unintended consequences of AI.  
This is by no means a complete list.  
But this will just give you a sneak preview  
of what are the things we are concerned about.  
So first example is bias in optimized decisions.  
So here is an example where Amazon  
was providing same-day delivery to all neighborhoods  
in various predominant cities in the US except predominantly  
African-American neighborhoods.  
This decision might have been taken due to optimized outcomes  
and costs that Amazon was considering in this decision.  
However, on the face of it, it looked  
like a discriminatory outcome.  
And so there was an outcry.  
A lot of mayors of different cities complained.  
They called Amazon and asked them  
to revert their same-day delivery policies.  
Next up, we see some issues due to robustness and resilience  
blind spots in various supply chain systems,  
like the national baby formula shortage talks  
about the inequitable US food system  
and how noise and disruptions to supply chains impact  
different groups differently.  
And we see also a resilient system  
where there was a fatal autopilot crash.  
And Tesla was ordered by a Florida jury to pay $2.3 million  
in compensation.  
The issues are not just about robust and resilience  
and optimized outcomes.  
There's many concerns that are raised because of historic data  
collection practices, for example  
the predictive policing algorithms  
that we're going to talk about in more detail in the upcoming  
lectures.  
There's issues due to bias in data that is generated  
and feedback loops.  
For example, some research found that fewer women than men  
were shown online ads related to higher-paying jobs.  
These are especially concerns because these recommendation  
systems are our gateway to opportunity.  
And if there are systemic, disparate impacts caused  
by these systems, then that can curtail opportunity  
for a wide set of a demographic.  
At times, there is a lack of data privacy and transparency,  
where legal sanctions require more transparency of processes  
used by organizations and explain  
the data sets that have been used  
in development of the systems.  
For example, on this slide, you see two articles, one about Uber  
being hit with legal sanctions to halt  
the use of AI-driven based systems,  
asking for greater transparency of process  
on how they're doing dynamic pricing when matching drivers  
to riders, and another complaint against Clearview AI,  
asking for data sources that they've  
used to develop their technology,  
and claiming that they've illegally  
scrubbed a massive facial recognition data set by taking  
online photos and videos.  
So these issues can lead to growing public governance  
concerns due to lack of human oversight and contestability  
of various systems that impact real lives.  
On this slide, for example, you see  
algorithms across UK, Brazil, and France  
that wrongfully flagged a large fraction of the population  
for possible fraud and error due to errors in data recording,  
due to errors in simple things that their name was recorded  
wrong.  
And they've wrongfully rejected a lot of claims in these Social  
Security applications.  
There is also a growing concern for economies  
that are moving to digital governance  
because for people who don't have experience  
with digital platforms, they can have more data errors.  
They can, for example, be wrongfully marked  
as not being alive anymore, for elders in this article,  
and create a set of digitally invisible populations  
that we have to be very careful about when  
we are making decisions through these systems.  
I also want to highlight feedback issues due to emerging  
technologies and rapidly growing technologies  
like LLMs and chatbots that rapidly interact with humans  
and grow and learn with the data that's generated.  
There is robustness and resilience issues.  
For example, Microsoft had to shut down an AI chatbot  
after it turned into a Nazi.  
And this was maybe even 10 years back now.  
More recently, Air Canada ordered  
to pay a customer who was misled by an airline's chatbot.  
These assistants can spread widespread errors,  
according to some new research.  
And chatbots can systematically violate mental health ethics  
standards.  
With growing reliance of humans on chatbots asking  
about their worries and their hopes and dreams,  
there is a concern on how these chatbots will effectively  
shape the mental health of the future generations.  
And in that respect, there is an important ask  
or a need, a critical need, to align goals,  
to have transparent goals that go  
into the design of these systems through organizations.  
Here is an example where Meta's AI rules have  
let bots hold sensual chats with kids  
and offer false medical information.  
This is a huge concern because it has conflicting objectives.  
An objective of a recommendation platform or a platform that  
wants retention of users is to engage them  
in a conversation that will keep them hooked into that platform.  
However, there is a competing goal,  
and that is of safety of that conversation, that perhaps,  
if overlooked, can cause concerns  
where there is wrong information,  
but also to a very vulnerable group of our population,  
that is kids.  
Further, with the large number of LLMs and models  
that are being developed across various organizations  
in the world, there is a concern that we are heading  
into algorithmic monoculture.  
This is a feedback loop.  
This is a longer-term concern.  
When many decision-makers, when they rely on the same scoring  
models, on the same algorithms to make decisions,  
generate data that feeds into their prescriptive  
and predictive models, errors can start becoming correlated  
and can worsen outcomes at the system level,  
even if the model is optimal for each user individually.  
As an example, there was a case in Walmart  
where a candidate contested that this person was rejected  
by all applicant-screening methods for an entry-level job  
at Walmart, Home Depot, and organizations like that.  
In this plot, what you see is, in a monoculture environment,  
when the algorithms are making same decisions  
or same predictions, you see a lot of people who are actually  
qualified are systematically rejected from the system because  
of similar types of errors.  
In contrast, if we had more diversity of algorithms  
and outcomes, we could see a system  
that balances even under noise.  
So monoculture is a growing concern.  
And people are rapidly developing techniques  
to inject more model heterogeneity and more model  
coverage across populations so that we are not  
making the same types of mistakes over and over again.  
Finally, as AI is proliferating every aspect of our life  
and every decision that's made around us,  
I would like to draw our attention to the real carbon  
footprint that AI has.  
The global electricity we use from data centers  
is around 415 terawatt hours, and that's the number from 2024\.  
And it is expected-- it is projected  
to rise to 945 terawatt hours by 2030, with AI as the biggest  
driver.  
Imagine the impact it will have not only on our electricity  
prices, but also on the needs of the electricity consumption  
that we will have in the world.  
Just to put this in context, 945 terawatt hours  
is around twice Germany's consumption, which  
is a major industrial economy.  
Data centers not just use electricity,  
they also use water for cooling purposes.  
So they are also water intensive.  
And there are massive efforts to understand  
how to build efficient hardware and algorithms  
and have smarter operations that can reduce the energy  
demands of AI data centers.  
In an effort to do this, Google has released data  
on how much energy an AI prompt uses.  
There's also a lot of work that's  
going on as we speak on the land and water impacts of the AI  
boom, and solutions that are being researched and proposed  
every minute.  
So with this, I would like us to think about all  
of the issues we've talked about, the issues due to missing  
and noisy data, issues due to models that don't align  
objectives, and organizations that might prioritize retention  
more than safety, for example, the impact of decisions that  
are built with automated systems that can compound poverty  
effects, that can have disparate impacts,  
and the feedback loops that make it possible that we never  
correct the distributional problems that we  
have in these data sets.  
Again, with AI and data, think about the data  
privacy concerns, the contestability concerns,  
the needs for transparency and auditability  
in various economies, and the growing concerns  
of algorithmic monoculture, AI being a cause of smaller data  
sets in some applications.  
And think about AI's sustainability impact  
on the world.  
With all of this, the urgent question that we need to address  
is, how can we get ahead of these concerns?  
How can we build ethical AI for decisions in today's world?  
We know that AI is extremely important.  
It has its massive advantages.  
It's helped us discover new compounds, new medicines.  
It's helped us find patterns in criminal cases, helped  
us solve crimes.  
The impact of AI is unprecedented.  
It's massive.  
It's critical for the growth and sustainability in today's world.  
But how can we ensure that the decisions we build  
are also ethical?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this lecture, we framed ethical AI as a practical discipline focused on real-world impacts, grounded in many real-world examples. We saw how harms can emerge across the full pipeline, from data collection and labeling, to training and evaluation, to how predictions are translated into institutional decisions. We discussed feedback loops, where decisions change behavior and future data, causing bias or exclusion to compound over time—especially when objectives are underspecified and trade-offs aren’t made explicit.

Key Takeaways  
End-to-end perspective: Algorithmic harm can originate in data, modelling choices, evaluation, or downstream decision processes.  
Feedback loops: Deployment can reshape the world the model observes, which can reinforce disparities and amplify errors over time.  
Objective specification: Even “reasonable” systems can produce unintended consequences when the problem is poorly specified or the target metric is misaligned with human values.  
Explicit trade-offs: Ethical decision-making often requires choosing among competing criteria (e.g., different fairness notions), rather than assuming a single correct metric.  
Wrap-up  
You should now be able to analyze an AI system as a socio-technical pipeline, identify where harms and feedback loops can arise, and articulate which ethical criteria and trade-offs must be made explicit before deployment.  
\`\`\`

Lecture 2: Causes of Unintended Consequences  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: Causes of Unintended Decisions, taught by Professor Swati Gupta, Associate Professor, Operations Research and Statistics, MIT Sloan School of Management.

Lecture 2 examines why bias and harm can emerge in AI-enabled decision systems even when models are technically well-built. Data is collected from a society with existing inequities, which means that datasets often encode bias through missingness, historical proxies and subjective measurements influenced by implicit bias. The session expands the lens from standalone models to end-to-end pipelines, emphasizing how prediction and optimization components can interact downstream and how layered systems may produce unintended disparate outcomes. A core focus is on objective design: when objectives are underspecified or misaligned with organizational values, systems can optimize proxy metrics in ways that look successful while driving undesirable outcomes. The lecture concludes by highlighting that high-stakes deployments require explicit choices about trade-offs and responsibilities, connecting these questions to classic ethical dilemmas such as the trolley problem.

Learning Objectives  
After these sessions, learners are able to…

Explain how societal bias can be reflected in data and why this makes bias in AI systems a pipeline-level concern.  
Identify common data problems (missingness, historical proxies, subjective evaluations).  
Describe the interplay of prediction and optimization in real deployments and recognize risks from layered or interacting models.  
\`\`\`

L2.1 Noise and Uncertainty in Data: Introduction  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Welcome back to the module on ethical AI  
for decisions in today's world.  
This is lecture 2 on causes of unintended consequences.  
In lecture 1, we discussed various ways  
of thinking about data models and decisions  
pipeline that create feedback loops in the data,  
and access of ethical decision making  
that's important to keep in mind when building AI for decisions  
in today's world.  
Before I can talk to you about solutions,  
we need to first understand the causes for these effects when  
we use AI pipelines.  
There are many ways in which I can have unethical or unintended  
consequences, and we've seen some examples  
in the previous slides.  
In this segment, I'm going to talk to you  
about how noisy and imperfect data can  
cause some of these issues.  
We know that data is not observed perfectly.  
It can be missing or incomplete in ways  
that cause downstream consequences on groups  
of people.  
We may not actually observe the data we would like,  
and in fact, our models might rely on certain proxies that  
capture similar signals that we would like our data to have,  
but types of errors and biases in these proxies  
can have noise in ways that impact some groups more  
than others.  
There are various other reasons of unintended consequences.  
For example, the interplay of optimization and prediction,  
or underspecified and misaligned objectives, and we  
are going to talk about these in segments that are coming up.  
So back to noisy and imperfect data.  
Let's consider the application of predictive policing  
through a software that's called PredPol.  
PredPol is an application of analytics techniques  
to identify likely targets for police intervention  
and prevent crime, or solve past crimes by making  
statistical predictions.  
So this tool uses no personal information  
about individuals or groups of individuals,  
eliminating any personal liberties or profiling concerns,  
as stated on their website.  
The variables they use for prediction  
are what we call independent variables.  
That's the data they're using to predict  
where crime is likely to occur.  
Historically, they have data on the type of crime  
that occurred in the past, the time of crime  
that occurred in the past, and the location  
of where it occurred.  
They are using this data in a predictive model  
to predict the probability of drug use-related crimes  
occurring in various parts of the city.  
And in particular, if you stare at the figure on the slide,  
you can see there is a lot of past arrests in the Auckland  
region that's circled, and it has around 200 arrests.  
That has a much higher density of past crimes  
that occurred there.  
And there is a much lighter density, much fewer crimes,  
much fewer past arrests that had happened in the region that is  
called International Boulevard.  
So let's see what happens when the system makes predictions  
about future arrests that should happen.  
We found out predictive policing algorithms  
can cause overpolicing of Black and Brown communities.  
So this is a huge concern because now it  
seems like the police are not really at areas where crimes  
is likely to occur, but they're overpolicing certain areas,  
certain communities much more than other communities.  
Let's put on our analytics hat and think  
about why this might happen.  
The data that the software used did not  
have any race information.  
It only had location information, the type of crime  
that occurred in the past, and the location and time  
of when the arrest was made.  
It does not use demographic information.  
So what might be the causes for overpolicing  
of these communities?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Lecture 2: Causes of Unintended Consequences  
\`\`\`  
L2.2 Noise and Uncertainty in Data: "Biased" Proxies & Missing Data  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So the thing to understand about AI and ML  
is that these techniques are amazingly good at finding  
patterns in data.  
Here is a plot in two dimensions, as we call it.  
This is a trend of line of points.  
And let's say I asked you to tell me what is the trend.  
If I see another point pop up from this data,  
where would you likely see it?  
You might end up drawing a line like this.  
And this is what we call a regression line or a regression  
function.  
So typically one would fit a straight line to it.  
This is not very straight because I drew it by hand,  
so ignore that.  
But the point I'm trying to make is  
that we can only find this pattern if this  
is given the data that we have.  
So if you are missing most of the data in the system,  
we might find the completely wrong pattern  
when the right patterns showed a very different trend.  
So this is what's happening in this situation.  
And to uncover that this was happening,  
Christian Lamb and William Isaac in 2016  
wrote a paper where they combined and contrasted  
the arrests data with a health care data  
on a heat map of drug related health incidents in this area.  
They saw that actually, International Boulevard also  
has a huge incidence of drug related health incidents,  
and therefore the arrest data perhaps  
doesn't capture the reality.  
Why might this happen?  
It's because of the use of a proxy.  
We actually wanted data on where past crime occurred,  
but the data we had access to was only  
where past arrests were made.  
And if there was a process by which arrests  
were made more frequently in certain neighborhoods  
where we even did not have enough data collected  
in the International Boulevard region,  
we could end up creating a completely wrong model  
of how drug incidence varies across different groups  
of people.  
And so what this work showed was that drug use by race  
seems quite comparable across different groups  
if you look at health data sets, and drug use by arrest records  
gives a very different trend, potentially  
because the way the arrests were made  
was not as uniformly spread, so the data had blind spots.  
We did not have a true reflection,  
we do not have a true representative data  
set that gave us a good proxy see for where crime occurs.  
So I would like you to pause here  
and think about various data that you interact with,  
and try to hypothesize what data are you actually missing.  
Are you really capturing the ground truth,  
or could you be missing a lot of data?  
Another thing that is a growing concern  
is that AI can lead to more missing data.  
As an example, here, you see a plot  
of how the interactions on Stack Overflow  
have gone down since 2016, with more and more people relying  
on ChatGPT to find bugs in their codes,  
to ask questions about different ways  
to code up different functionalities.  
There is a steady decline on Stack Overflow  
in the number of posts.  
The posts are low quality.  
They're suggesting that valuable knowledge creation is being  
displaced to private chats.  
Now, this creates a concern that already our societal processes,  
for example, in the predictive policing application led to data  
not being collected uniformly.  
There were data gaps.  
There were representation issues.  
But now large language models might actually  
start becoming a threat to digital public goods.  
As we keep interacting with these systems  
and they can train on our data, are public sources of data  
that we can build algorithms on, that we can build more AI on,  
this will grow smaller.  
And so not only will data become a very important commodity  
in the future, these models might also  
create more missing data and leading concerns because  
of that.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.3 Noise and Uncertainty in Data: Examples for Problems with Missing or Noisy Data  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So to wrap up this segment,  
I would like us to think about, how  
can we make reliable AI driven decisions  
by creating practices that account  
for data collection and systemic practices in the past?  
How can we detect irrelevant patterns in AI models  
that may not reflect the ground truth, that may not  
reflect the state of the world, where AI might be picking up  
a wrong trend, in some sense?  
And can we reduce the impact of these in AI  
based decision making?  
Some other examples that I want to remind us of  
are, the first one is mapping potholes by phone.  
This was the app where, because of tech adoption and engagement,  
we did not have enough data collected in neighborhoods where  
people did not adopt this app or did not have  
the means to download this app.  
We also see missing data when we have missing demand information  
because of lost sales, when the item stocks out  
and we don't know if there was a demand above that.  
There's also a lot of data concerns  
when we are building predictive systems  
to understand which organs are likely to be accepted by which  
patients.  
In this case, for some organs and some types of transplants,  
if we have very few data points, if we  
have very few historic cases where  
organs of a particular quality had been transplanted,  
then it's harder to learn accurately  
on how to match organs where we have small amount of data.  
So missing data is a huge concern.  
Missing data can often lead to unintended consequences.  
But it's not just this.  
Even when we do have data, we could have noisy and imperfect  
information.  
Think back about the Uber drivers example,  
where their pricing strategies, their matching  
is based on ratings that drivers obtain.  
The ratings about a driver may not accurately  
reflect the true driving quality but might reflect also  
the societal biases that we all have as riders.  
Similarly, there's a lot of work,  
a lot of research where people have done controlled experiments  
to show that the way humans evaluate other humans for a job  
can be biased with respect to gender, nationality  
for different types of jobs.  
The pricing, the rate of accepting a person  
to stay in their home on the Airbnb platform  
could also reflect biases.  
So as humans, when we all generate  
data that might have our own implicit bias in it,  
then the question is, can we still make  
reliable and robust decisions that ensure consistency  
so our decisions are fair in the sense  
that similarly qualified people for a job  
should get similar opportunities?  
Or similarly, sick patients should  
be identified ahead of time and get the right treatment  
and the right diagnosis.  
And this is a question that impacts hiring.  
It impacts opportunity.  
It impacts the jobs, the career transitions we might have.  
It is also something that we have  
to keep in mind with growing algorithmic monoculture,  
so that the same types of errors are not  
compounded by these systems.  
And also we have to recognize that data can be noisier  
depending on who we are collecting the data about  
and who is collecting the data.  
An example of that is the limitations  
of the mini mental state examinations, where researchers  
found that actually, if we collect data about Alzheimer's  
and Parkinson's through a bedside survey, then  
it is likely to be more errored if the patients are much older.  
There's other concerns that if you have a human collecting  
data about, let's say the propensity of a sale in a call  
center, it is likely to also incorporate  
how the human was an expert at making the sales or not.  
So our data can be noisy.  
It can be missing.  
It can be imperfect.  
It can depend on the mechanism used to collect the data.  
It can depend on who we are collecting the data about.  
And the goal will be to make sure  
that our decisions are robust, fair, unbiased,  
and ethical overall.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.4 Interplay of Optimization and Prediction: Introduction  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We've already discussed  
how noisy and imperfect data can lead to patterns,  
can lead to decisions that have different impacts  
and disparate impacts on different groups of people.  
Let's now talk about the second set of causes  
of these unintended decisions.  
These are caused specifically due  
to the interplay of optimization and AI.  
We discussed in the first lecture  
that models can be layered and interact in complex ways.  
The issue is that small errors in predictive models  
can get amplified by optimization  
in downstream decisions.  
Let's see how.  
So consider the example of recommendations  
using predictive algorithms that try  
to estimate whether a particular user is likely to click  
on the recommendation or not.  
So to contextualize it, the data that we really want from users  
is whether they're interested in a recommendation.  
But the proxy we have for it is whether they  
click on some link that's provided,  
or they hover on some news article for a longer time, where  
their mouse, the cursor moves as they're  
navigating the page, a web page of a platform like Facebook.  
Those are proxies we can create to assess  
whether somebody likes the content they're being shown.  
We also mentioned in the last lecture  
that some unintended consequences  
led to female gendered users seeing  
fewer instances of job ads related to high paying  
jobs than male gendered users.  
This was an experiment done by researchers at CMU,  
and it's a pretty cool finding.  
Let us think about why something like this might happen.  
Because nobody goes to their workplace thinking that,  
today we are going to write the code for a recommendation system  
that discriminates based on the demographics of users.  
It's really due to interaction of data  
in the models and the optimization  
that we see these disparate impacts happening.  
So the key question is, can it be because of historical data?  
Perhaps some groups don't like seeing high paying job ads.  
Perhaps they've not clicked on many high  
paying job ads in the historic data  
so it gave us a signal that maybe they  
don't want to apply to those.  
Or could there be another reason?  
And so in this slide, I would like  
to make a simple illustrative example  
to highlight the effect of AI deployments  
that are often highly interconnected.  
This is an image I got from Google Images.  
And these deployments can create something  
like a bullwhip effect.  
Small perturbations earlier in the pipeline  
can cause larger and larger effects  
that can amplify in downstream decisions.  
These can destabilize entire systems  
if I was speaking in a hyperbole,  
but they can have real impacts on these critical domains  
that we care about.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.5 Interplay of Optimization and Prediction: Predictive Analytics plus Optimization Examples  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's see an illustrative example of how  
predictive parts of a decision making system  
can interact with the prescriptive parts of it that  
could potentially entail optimization.  
So imagine that you are going on a search platform and you search  
for the word "suits."  
Now, this platform is trying to assess.  
It's a recommendation platform.  
So as it shows you relevant links for suits,  
it also has slots to show advertisements  
from various organizations that might  
want you to click and explore the offerings that organization  
has.  
So think about searching on Google  
and you see some ads pop up.  
Now, we are really focused in this example on how the ads that  
are shown to users selected.  
And so in this case, Google will not only  
decide based on the attributes that the user has,  
based on the data that the user has on the platform.  
It will decide that is it more likely that this user clicks  
on Hugo and Boss, the retail ad, or is it more likely that they  
click on the job ad, which is from Gordon and Gordon,  
the law firm in Boston?  
So let's say the platform that is Google  
has some predictive algorithms that  
predict the click-through rate, the likelihood that a user will  
click on these ads.  
These are just made-up numbers for illustrative purposes.  
The important thing to note here is  
that given these probabilities that the user might click,  
or a thousand users in that group might click  
on that ad, the retailer, the company whose ad is shown,  
they place a bid on the display ad.  
They say that, well, if you display our ad  
and we get a click on it, we play  
the platform, which is Google, so much amount of money.  
And more importantly, as a female user  
comes to this platform, if they were to click on the Hugo Boss  
ad, they would actually generate more expected revenue--  
that is $0.062 on the slide--  
compared to if a male was shown the Hugo Boss ad.  
That's only $0.04.  
And therefore, if the platform that is Google  
is trying to optimize for the revenue,  
they would end up showing the female the retail ad, which  
is more lucrative from Google's perspective,  
and show the male the job ad, which  
is an optimized outcome, because they can only show  
these ads for so many slots.  
So as you can see in this example, there is a trade-off.  
There is a constrained resource of how many ads  
can be shown to the different users  
with the different demographics.  
And there is a competing objective  
of how this translates to the job opportunities  
that the users are seeing.  
And so if an organization is focused on the revenue rather  
than the opportunity, then this can create  
these unintended consequences.  
Let's look at another example that's illustrative  
and it amplifies distributional errors  
across groups and different types of errors across groups.  
So let's consider an AI model that  
predicts the risk of a serious complication in the hospital,  
the emergency room.  
Here, high-risk patients get extra tests  
and preventative care, and low-risk patients,  
as labeled by AI, are not tested as often  
or not monitored as often.  
An insurer uses this model's risk classification  
as high risk or low risk to set premiums and optimize prices  
to hit a profitable strategy.  
So let's take an example where the number of people that  
are predicted as low risk across men and women are 82 out  
of 100, and the number of people who  
are predicted as low risk are 9 out of 10 for non-binary people.  
The false negatives by these model outcomes are imbalanced.  
They are four out of an 82, which is around 4.9%  
for men and women patients, but it's a staggering 22.2%  
for non-binary patients.  
This could be due to a lot of reasons.  
And specifically in this example,  
it might be due to data imbalance as well.  
We don't have enough data on non-binary patients.  
In such a case, because of mislabeling through AI,  
low high-risk patients as low risk, the costs to the insurance  
companies are quite high for non-binary patients.  
And as a result, this can cause higher premiums  
for many healthy non-binary people,  
even though the increase is driven by model error, and not  
really individual risk.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.6 Interplay of Optimization and Prediction: Supply Chain Examples  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: All right, so to wrap up,  
I hope these two examples have exemplified  
how the interaction of optimization and AI  
can exacerbate small errors in predictive models that are then  
taken up by optimized decisions, or even if there were no errors,  
the optimization can in itself exacerbate disparities.  
The key questions we are interested in  
are, can we make optimized decisions that do not  
enhance disparities due to suboptimal estimates,  
and if we can make optimized decisions that  
don't induce high costs on the same group of people.  
For those of you who work in supply chains,  
perhaps it might be helpful to think about areas that are often  
underestimated from a demand perspective, that often end up  
facing a stockout of commodities,  
and think about how can we make decisions  
that are robust to the noise in our estimates.  
Here is an example that simply plots the census data in Atlanta  
and shows how southern regions of Atlanta  
have a lot of socioeconomic inequalities.  
The northern region of Atlanta house mostly wealthier census  
tracts, and an inventory routing problem in this situation  
can cause smaller number of stockouts  
in the wealthier regions, because they just  
have more robustness baked into the inventory routing decisions.  
And so we have some recent research  
where we are trying to mitigate the impact of demand shocks  
and noise in such applications.  
Other areas and other applications  
where we've seen the compounding effects of optimization and AI  
are in Amazon same-day delivery, as we discussed  
before, the national baby formula shortage, because  
of demand inequalities and resilience that  
is missing in the supply chain system,  
and the use of electricity rates that  
might impact vulnerable groups more,  
which don't have the flexibility of charging their batteries,  
minimizing their use of power during peak demand times.  
So with all of this, we are coming  
towards the end of this segment, and I look forward  
to discussing more causes of unintended consequences of AI,  
specifically due to misalignment of objectives and values  
in the next segment.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.7 Underspecified and Misaligned Objectives: Optimization Criteria  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So far, we have discussed  
two major causes of unintended consequences  
due to automated decisions.  
The first major one was making decisions  
using noisy and imperfect data that only reflect  
proxies of what we actually want the data to be about,  
or can have major blind spots and gaps in the data  
we have collected.  
We've also talked about how the interplay of optimization and AI  
can exacerbate the types of errors in predictive models  
that our pipeline builds upon.  
In this module, I would like to discuss  
how underspecified and misaligned outcomes may not  
reflect the organizational values that these  
should have been built upon.  
First of all, it may not be clear on how  
to translate organizational values into the design of AI.  
A lot of organizations today like NIST, IEEE,  
have been working on design standards and principles  
of incorporating ethics into the design of automated systems.  
It's clearly challenging because, for example,  
if I were to ask you how much robustness should be baked  
into an inventory routing management problem to cater  
to equal service to all users, you  
might ask, what does it mean to bake robustness?  
Is it increasing the number of trucks that  
are being used for delivering?  
Is it increasing the number of drivers?  
How much resilience do we want in a system,  
and how much should we actually optimize the revenue?  
The two considerations we have here  
is building ethical systems, but also for organizations  
that can sustain in this world.  
To start thinking about objectives,  
let me draw from a real world example that  
happened a few years back in Alameda County.  
So in 2017, Sutter Health announced  
closure of the only emergency room in Berkeley  
due to seismic unfitness and cost of retrofitting.  
Now, this was a huge concern, and a lot of people  
protested because this emergency room  
was the primary center for service  
for a huge fraction of population  
that was poor, uninsured, and people of color.  
And based on this protest and concerns  
raised to the mayor's office, the hospital chain  
announced that Alta Bates Medical  
Center will stay open for at least another decade.  
So imagine an organization that's  
trying to make a decision of where should we  
place an emergency room.  
Of course, there's a lot of ways to go about it,  
but here my question is just about access.  
Let's say the goal is to place an emergency  
room or a COVID testing site or pharmacies  
so that different populations have equitable access  
to that room.  
Now, in this picture, I draw certain circles  
with different colors, and so they reflect one group of people  
and another group of people.  
So we have a diverse demographic that we want to have equitable  
access for.  
The problem is, how do we define equitable access?  
So let's say we have two groups of people.  
Is equitable access attained by a solution  
which minimizes the total distance traveled by any group?  
Well, it's unclear because in this example,  
the person in group A is really far off from the facility  
and it has unequal access.  
They're really disadvantaged.  
So person from group A could hypothesize, well,  
why don't we minimize the average distance instead?  
But now consider this spread of population.  
In this case, for that minority community  
or one person who is in group A and really  
far from the city center, there, because of them,  
to equalize average distance faced by that community,  
a large fraction of people in group B are being penalized.  
In just this simple example, I would  
like to emphasize that in any application,  
it's not clear on what are the right objectives  
from a mathematical perspective, from a modeling perspective,  
from design of the AI system perspective.  
As we try to model, as we try to convert values that  
are specified in English, that are specified in intention,  
and converting them into models that  
require precise rules or guidelines or objectives,  
or an evaluation function or a scoring  
function to tell us that this solution is  
better than that solution.  
In the case of facility location, in 1993 itself,  
two researchers, Marsh and Schilling,  
gave a list of 24 different mathematical ways  
of trading off efficiency and fairness in placing facilities.  
And so if we don't know how to solve this ourselves  
or finalize our criteria ourselves as humans,  
it's hard to inject these values into the development of AI  
systems.  
And what we really need are systems  
that can trade off these various criteria,  
give us a way of democratizing the system,  
taking the input of the various stakeholders that interact  
with these systems, and align them to organizational values.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.8 Underspecified and Misaligned Objectives: Moral Dilemmas  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, when you're trying  
to think about aligning AI systems  
to organizational values, we could have values  
that are aligned together.  
And we could have values that contradict and compete  
with each other.  
From that perspective, let me tell you  
about the trolley problem.  
It was coined by the philosopher Philippa Foot in 1960s.  
And it talked about how we should decide  
which decision is ethical.  
In the trolley problem specifically,  
the hypothetical situation is that a train is coming.  
And a person could either intervene and change  
the track of the train or may not intervene.  
If the train continues on its course on the trajectory it's  
planned for itself, it can end up  
killing the five people who are on their first track.  
But if the person intervenes, it can end up  
killing the one unsuspecting person on the train track  
because the system deviated from how it was supposed to operate.  
Now, this might seem hypothetical.  
But a couple of years back, MIT ran a massive experiment with  
70,000 participants across the globe.  
And they asked that as we are designing self-driving cars,  
how should we prioritize what route to take?  
As humans, when we are driving a car,  
we don't have the time to really consider  
the consequences of swerving the car one way or the other  
when an emergency arises.  
Imagine a self-driving car that has these predictive systems  
on various trajectories and how safe the different trajectories  
are.  
And it has goals of trying to protect  
the passengers of the car.  
In designing such a system, there  
are many decisions that can be taken algorithmically now  
because the speed of AI, which as humans, we've never  
had to think about consciously as they happen in a split second  
before we can think about these decisions.  
So what the MIT researchers did was  
that they asked a bunch of participants  
if there was a potential accident that could occur  
and the car, had to take one of the two routes, in this example,  
route or route B, where A would end up impacting the baby  
and B would end up impacting the old woman, who's  
crossing the street, then which one would people prefer?  
It seems like a pretty odd question, a question  
we don't want to think about.  
We don't want to trade off lives.  
But with the speed of AI and automated decisions,  
maybe these are becoming more important for us to address.  
So in this experiment, they asked, well,  
would one prioritize a person who  
prioritized saving a person who's  
a nurse or a doctor in the medical system  
versus prioritizing saving somebody who is breaking  
societal rules, and laws, and is potentially a criminal  
and so on.  
So in this experiment, what they found was pretty fascinating.  
Our sense of morality, our sense of prioritizing different  
people, whether it be lawful versus unlawful or old  
versus young, it varies by societal expectations,  
the cultures in different countries, by what  
they place a higher value on.  
And the debate that this gave rise to is now,  
should we decide as a country of what are our priorities, when  
developing self-driving cars, how should we  
align these objectives?  
How should we find the right metrics  
to optimize for as we are making decisions  
for a very diverse set of stakeholders  
as we build systems that interact with populations  
across the world?  
But I think the first step is even  
to lay out all the factors we should  
want considered in the design of today's systems.  
Often these decisions are made without an explicit discussion  
with the stakeholders at the table.  
Understanding what are the trade-offs  
for the different communities will already  
help us align AI systems better.  
So I will end this segment by asking the question  
of how can we make decisions when system priorities affect  
stakeholders in different ways.  
So you can already think about a family that's deciding  
to go for hiking, let's say.  
And every member of the family wants a different hiking route.  
How might you come up with a decision that  
is aligned with everybody, whether it  
be the natural beauty of the hike,  
or the hardness of the hike, or the distance of the hike  
from your home?  
There could be different things, different people in the family  
you want to prioritize.  
And how can you make a decision that's aligned  
with the values of the family?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.9 Causes of Unintended Consequences: Summary  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Before we end this segment,  
I would like to summarize what we've seen so far.  
The first takeaway is that we live in a society as humans,  
which we have our own biases.  
So it is inevitable that the data  
that we collect about the society  
will also reflect these biases.  
Moreover, there are various issues  
with data that might be missing.  
It could reflect historical practices,  
like the arrest records data.  
It could reflect implicit biases,  
like evaluations and ratings on drivers and people  
we want to hire.  
Data problems might be picked up by models that  
are trying to learn patterns.  
The models could have errors in their predictive parts  
that might be differently typed across different populations.  
Interaction with optimization systems  
might introduce further unintended disparate impact  
and outcomes, like the ad display optimization  
or the insurance pricing.  
And moreover, it might be unclear  
how to align organizational values with specific objectives  
that can train models and align models that  
are AI and optimization based to be value aligned  
with the organization.  
This is just a starting point.  
There are many more causes for unintended consequences.  
But the key point is that we don't want such biases  
to propagate into systems that make  
high-stakes decisions and important decisions  
across policing and health care, loans and housing  
and accommodation and access to jobs and education and so on.  
So our next focus is going to be to talk  
about techniques that can help us build ethical AI systems.  
And I hope to provide a starting point  
for thinking about some solutions  
to these unintended consequences.  
And I hope that your research and further education  
can build on this in the future.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this lecture, we examined why biased outcomes in AI often reflect biased social systems and imperfect data, and how these issues can be amplified by multi-stage decision pipelines. We saw that missing or skewed data, the use of historical or subjective proxies, and underspecified objectives can push systems to optimize the wrong outcomes. This makes value alignment a core design problem.

Key Takeaways  
Noisy and incomplete data: Data can be missing, censored, or measured imperfectly, and these gaps often disproportionately affect minority groups. Issues can sneak in when we rely on proxies instead of direct measurements.  
Prediction \+ optimization interaction: Small predictive errors can be amplified by optimization, decision thresholds, and downstream policies, therefore “good accuracy” does not guarantee good outcomes. Miscalibration or bias at one stage can cascade and compound across later stages.  
Underspecified or misaligned objectives: If organizational values aren’t translated into explicit objectives and constraints, the system will reliably optimize a metric that may conflict with what stakeholders actually care about.  
Wrap-up  
You should now be able to diagnose where bias can enter a data-driven decision-making pipeline (data, proxies, objectives, or pipeline interactions) and explain why high-stakes AI needs principled design criteria.  
\`\`\`

Lecture 3: Strategies for Ethical Decision-Making  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 3: Strategies for Ethical Decision-Making, taught by Professor Swati Gupta, Associate Professor, Operations Research and Statistics, MIT Sloan School of Management.

Lecture 3 introduces a practical toolkit for responsible AI decision-making. It motivates methods to diagnose blind spots (e.g., selective labels in parole data), evaluate and balance errors (false positives/negatives, including group disparities), and apply guardrails such as deferral or warnings when evidence is weak. The lecture then surveys tools for handling missing/noisy data, incorporating domain knowledge, quantifying uncertainty (e.g., calibrated intervals), and navigating multi-objective trade-offs using constraints, regularization, and Pareto frontiers.

Learning Objectives  
After this session, learners are able to…

Diagnose selective-label and missing-outcome settings and explain why they undermine both learning and evaluation.  
Interpret false positives/false negatives and assess why different stakeholders may prioritize different error trade-offs.  
Evaluate group-wise performance and articulate what an error disparity implies for harm and accountability.  
Apply principled approaches to imperfect data and justify when domain knowledge should constrain or correct the dataset.  
Use uncertainty-aware reasoning to decide when to act, when to defer, and how to support robust downstream decisions.  
Frame value alignment as a multi-objective design problem and interpret trade-offs using constraints/regularization and Pareto reasoning.  
Formulate and interpret value-aligned trade-offs using constraints/regularization and Pareto frontiers in multi-objective problems.  
\`\`\`

L3.1 Detecting and Diagnosing Problems: Implementing Detection in our Data-Model Decision Pipeline  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Welcome back.  
In lecture 3, we are going to talk about strategies  
for ethical decision making.  
So far, we've talked about the goals we aspire to achieve,  
for example, fairness, accountability, transparency,  
explainability, and many other axes of ethical decision making.  
We would like to achieve these goals  
within the context of the ecosystem  
that we interact in, obeying the laws in our society,  
following the policy perspectives, the expectations  
that people have.  
For example, the antidiscrimination law doctrine  
in the US is Title VII, the privacy laws  
that protect the privacy of the data of the citizens.  
We would like to understand, how can we  
make these decisions, even though we  
have noisy socioeconomic data?  
And we would like to develop AI-based models and mechanisms  
so that the voice of various stakeholder perspectives  
is reflected in this design while ensuring  
that the system is still operational,  
we are still able to use and benefit  
from the scale and the massive compute possibilities of AI.  
So in terms of strategies for ethical AI,  
this is by no means an exhaustive list,  
but some big ideas in this space have  
to do with first detecting and diagnosing  
the problem, which is what we're going  
to focus on in this segment.  
We're going to ask about, why are we getting  
unexpected outcomes, and why are some populations getting  
higher errors?  
And we're really going to walk through an example on how  
we can be a detective observing the data, models, and decisions  
pipeline and detecting and diagnosing  
the problems it incorporates.  
Next up, we'll talk about two other big ideas  
on handling noisy and missing data  
while mitigating its impacts on downstream decisions  
and navigating the interaction of optimization and AI.  
So let's talk about detecting and diagnosing  
the data-driven decisions-making pipeline.  
The first step in building a model  
is to understand, what is the right problem to solve?  
How do we formulate that right problem?  
What is the real-world goal we are after?  
How is the real-world mechanism operating?  
Is there enough data for us to actually make use and benefit  
from the use of AI?  
Can we help scale decisions?  
Are there some inefficiencies in the process  
that we can alleviate by the use of AI and optimization?  
Once we've identified that, we have to think about,  
are there patterns of inequality and discrimination  
that exist in the real-world practices  
that we have to keep in mind while designing our systems?  
Next up, we have to think about, how is data collected?  
Which data can we use?  
Is the data that we have representative?  
Does it look like it's missing a lot of data about people because  
of the collection mechanisms?  
Is the data discriminatory in some sense  
because it's not reflecting the true nature of society,  
it's not evaluating the true performance of candidates  
and so on?  
What can we know about the data before we even  
start thinking about building the AI and optimization models?  
So as you can expect, the next step is the design of the model,  
understanding, what is the type of models we want to build?  
Are these supervised?  
Are these unsupervised models?  
What are the layers we want to build in?  
Are there some optimization components?  
Are there some generative AI components?  
Is there a chat interface that we  
would like to query the model?  
What should be the design of that pipeline?  
And this is often an iterative step  
that happens across multiple teams in an organization.  
Things we want to look out for-- are there  
biases already encoded in that in the way  
that we are designing the system?  
Is there a power imbalance in who is designing  
and who it's impacting?  
And how can we capture the voice of the stakeholders,  
for example?  
The next step is, of course, developing the model,  
training the model, and actually making the AI  
and optimization do what we intend for it to do.  
The model can then be validated on what  
we call as a test data, the data that the model has never seen.  
And we can test the model's performance on this data  
before actually deploying it in practice.  
Things to look out for in the model development and validation  
steps is if there is some injustice,  
if there are some objectives that  
are misaligned with the values of the organization,  
if we are using proxies that have an unintended consequence  
at this step.  
Are we actually getting data that is passing all the fairness  
checks in the validation stage?  
If it is not, then we have to go back  
to formulating the problem, data collection, model  
design, and rethink about what we missed in this pipeline.  
And if it does pass all the checks  
and all the ethics frameworks that we have in our mind,  
then we can go ahead and deploy that.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.2 Detecting and Diagnosing Problems: Detecting Issues in Algorithmic Parole Decisions  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's build this out step by step  
with the example of parole decisions.  
So let's talk about formulating the problem.  
So what's parole?  
It's the release of a prison inmate before the completion  
of their sentence on the promise and anticipation  
of good behavior.  
So imagine a problem formulation where  
we look at the factors and the data  
that we have on inmates in a prison.  
And we are trying to assess whether we can develop an AI  
system that can even predict whether somebody  
is likely to reoffend or not by seeing  
through past patterns of past inmates  
and their criminal histories.  
The factors that we really want the system to obey  
is that we should be able to grant parole  
to inmates who are likely to adhere to parole terms,  
and we should not be granting parole  
to inmates who are likely to violate the terms of parole.  
So now there are two types of errors  
that such a system could have.  
It could mistakenly predict that a person will violate parole  
when the person is actually not going to violate parole.  
And so this is an error that we call false positive,  
not granting parole to an inmate who had  
adhered to the terms of parole.  
The other type of error is granting parole  
to somebody who will violate the terms of parole.  
And such an error is called a false negative.  
Now, you can imagine that from such an AI that's  
making these decisions, we would like  
to keep the number of false negatives  
and the number of false positives to a minimum.  
Both of these decisions, both of these types of errors,  
have different costs to the society  
and cause different unfairness outcomes in the system.  
So now, coming back to data collection,  
let's see what data we have on this example.  
So parole decisions are made by a parole board.  
And typical factors in the decision  
include an inmate interview that's  
conducted in the prison, a psychological exam evaluation.  
And there's a lot of available data  
on who's the violator, what's the gender of this person,  
what's the age, how much time they've already served,  
how much time did they have to serve, their offense class,  
if they had multiple offenses or not, where did they offend,  
and the ethnicity of the person.  
Having this data, for example, from New York state from 2012  
to 2015, this had data on 6,000-plus parolees.  
But importantly, it is censored in a way  
that we have to be very careful about when  
developing such a system.  
We only have data on people who would have been eligible  
for parole and were granted parole.  
And we can observe, from those who were granted parole,  
how many went ahead and violated the terms  
and how many went ahead and did not violate the terms of parole.  
We don't have data on people who did not get parole.  
So there could be a set of people in this data  
which did not get parole.  
And we have no way to learn about whether they would have  
violated the terms or whether they would have not  
violated the terms.  
And one way to protect against this blind spot in the data  
is that we need to provide context to model predictions.  
Imagine a data-driven decision making  
pipeline which uses AI optimization  
and different types of models.  
If, when making its decision, it could also  
have an asterisk to say that, well,  
for this set of decisions on these set of profiles,  
I actually don't have enough data.  
So take my prediction with a pinch of salt.  
Or I would rather differ from making predictions  
on this group of people because they are not  
represented in my data.  
A lot of research is happening in this area  
on how we can have disclaimers with model predictions  
be made available to decision makers  
so that we are able to address the blind spots in our data.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.3 Detecting and Diagnosing Problems: Auditing Model Design & Development in Algorithmic Parole Decisions  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Next, let's talk about the model design.  
So we have our data.  
We have a problem in our mind of how we want to formulate it.  
The relevant questions about model design have to do with,  
which AI models?  
What objectives should we prioritize?  
So first of all, which data are we allowed to use?  
Should we use race data?  
Should we maximize the accuracy of the models?  
We are going to talk a lot about that  
in the alignment of models with organizational values as well.  
Do we prefer accuracy or explainability of models?  
This is an important question.  
If you want the most accurate model,  
it might turn out to be not the most explainable model.  
So we have to address this question in the model design.  
We have to think about ways in which humans  
will interact with the system.  
So for example, do judges need information  
about why the model is predicting a yes or a no?  
Do we need to bake that into the model design?  
And more importantly, how can we incorporate mechanisms  
for human oversight and protect against algorithmic monoculture?  
With these considerations, let's say  
we go into the model development stage  
where we've decided to use a CART model because it's  
explainable, we don't use race, and we just  
want the most accurate model.  
Here is the CART model that you can fit on this data  
from New York State.  
The way to read this is almost like a decision flow diagram.  
So you start with the node at the top.  
The time served is less than 1.94.  
If that's true, then yes, you will predict a 0\.  
The model is most likely to predict a 0 in this case.  
What the 0 means is this person is not  
likely to violate terms of the parole,  
and they can be granted parole.  
If the time served is more than 1.94,  
you have to then trace the righthand side, the no branch  
of the model, and check whether the crime class is A, B, C, D,  
or E. This models the severity of the crime.  
And so as you can see, the model is  
predicting 0's and 1's of whether a person is going  
to recommit a crime or not.  
And it really depends on the type of the crime  
and the amount of time that they've served.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.4 Detecting and Diagnosing Problems: Model Evaluation  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, if one looks at this model,  
we are likely to hypothesize that perhaps this has  
no unintended consequences because it does not even  
use race.  
So that's how we are now getting into the model validation step.  
So let's check on the test data on how this model performs  
across different groups.  
And I'm specifically looking at the false positive rate.  
So this is where a model falsely marked somebody  
as they would reoffend the crime, whereas the actual data  
we have on people who were granted parole did not go ahead  
and reoffend the crime.  
And what you see here is that the false positive rate is very  
different across two groups--  
the African-American defendants in this group  
and the white defendants in this group.  
The false positive rates are almost twice  
as high in one group compared to another,  
and that can be a cause for ethical concern.  
So at this point, because the false positive disparity  
is very high, we have to go back and rethink our model  
formulation, what we have potentially missed,  
and try to have mitigation and checks and balances in the model  
development design, the data collection, and the problem  
formulation before we can end up deploying the system.  
So we have to go back, reassess the goals of the problem.  
We decided that we wanted an explainable model.  
Let's say we decide that now we want  
errors across different groups as small as possible.  
Perhaps we also suggest that false positives should  
be balanced across all groups and race, gender, age,  
ethnicity, whatever groups you could think about.  
Suppose we also ask that the false negatives have to be  
balanced across all groups.  
So we sit together.  
We look at the problem formulation again.  
We add a list of requirements that we want from the model  
before actually deploying it.  
But this might actually render the model to be infeasible.  
Let's see why, and this is just an intuitive example.  
So there is a certain level of interaction of these objectives.  
At a high level, if an AI system is trying to classify certain  
people as yeses-- so in this case,  
yes they will reoffend a crime, or no,  
they will not reoffend a crime--  
in this case, you can see that effectively using  
a linear classifier, or really in this intuitive example,  
using a line to separate these two groups of people is easy.  
However, let's see now that different types  
of data distributions present in that data set, which is really  
how the real world is.  
You don't get very clean separation  
in predicting outcomes.  
Now, since the data distribution between the triangles  
and the squares is different, as we  
try to change the placement of this line,  
we will see different outcomes and different impacts  
on these two groups of squares and triangle shapes.  
For example, if we keep the same line,  
we are seeing that we are making false negative errors  
on all of the squares.  
There's no false negatives on the triangles,  
so it looks like we are discriminating  
against the squares.  
If we actually move the line a little bit,  
now we are making false positive errors only  
on the triangles, which might seem, again, discriminatory  
because we are not making any false positive errors  
on the squares.  
Let's try to find the most accurate classifier.  
In this example, you can test it out by drawing your own lines,  
but this turns out to be the most accurate classifier here.  
In this case, we see that the error rates are now disparate.  
On one group, we are making more false positive errors.  
On the other group, we are making  
more false negative errors.  
And so this comes back to the alignment of systems.  
Should our goal really be to achieve balance  
in false negative rate, balance in false positive rate, best  
accuracy?  
What should be the goal?  
Because there are different stakeholders involved,  
these decisions impact different people  
in the system differently.  
And so this trade-off has to be carefully reached at.  
So as we go into understanding trade-offs,  
perhaps this is a good time to revisit the trolley problem.  
One choice impacts certain people.  
Another choice impacts some other people.  
So what I'm trying to say is that different criteria that we  
might desire in a system may not be aligned,  
and one might need to consider explicit trade-offs  
across different objectives.  
And this is what we'll talk about in the next segment.  
So just to wrap up, it's important to revisit different  
paths of developing an AI/ML-driven pipeline that makes  
data-driven decisions.  
And it's important to really think about every component  
and do an iterative design so we can catch problems  
with our problem formulation in the context.  
We can catch problems with missing and types of noisy data.  
We can understand and make conscious moral choices.  
And we can identify metrics we care about  
and make a plan to either deploy the system if everything works  
as expected or continue iterating on this process  
until we've identified the right data-driven decision  
pipeline to deploy.  
And now, I would like you to take a minute  
and think about what is similar analysis  
in the data-driven decisions pipeline that you care about,  
that you interact with.  
reveal, would it reveal problems with the problem formulation,  
the type of data that's being used, the model choices?  
Do you even know what the model choices are in these pipelines?  
How are the models trained?  
How were they developed?  
And does deployment or do model metrics reveal something  
that we should really rethink and fix in the pipeline?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.5 Handling Noise: Handling Missing and Erroneous Data  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now talk about some strategies  
for handling noisy data and model predictions.  
The key questions we are interested in this segment  
are how can we complete the data that might be missing,  
maybe at random, maybe not at random;  
and how can we correct bias in existing data.  
And I'll make that precise in a little bit.  
We are also interested in answering,  
can we still make ethical decisions, even with noisy data,  
and what such solutions might look like.  
So one view I want you to remember  
is that data is only a partial picture of the real world.  
The real world is, of course, much more complex, much  
more nuanced.  
And the data that we have and the models  
that we build only help us view the world, only  
help AI view the world from a very small lens.  
And so if we can make this lens more precise,  
then we can aim to have better models.  
Let me first give you an overview of techniques  
for handling missing and errored data.  
One practice that I've seen a lot of organizations  
do is simply drop the data points which  
have so much missingness that they end up just adding noise  
to their data sets.  
This is not great because dropping rows  
means that now you're working with even smaller information.  
But sometimes this becomes necessary to be  
able to get enough signal that our AI and machine learning  
models can pick up.  
The next practice is data imputation.  
There are various ways of doing that.  
For example, if you have no information in a time series  
data set about a particular variable,  
then one might impute it by the mean value across the other data  
points.  
In this example, for instance, you  
see a trajectory of heart rate changing over time,  
where the green dots are the data that's available to us,  
and the red dots are data that is imputed.  
So this was missing data, but we imputed  
it using what is known as linear interpolation  
or linear imputation.  
One can also use techniques that involve  
connecting to the nearest neighboring data, learning  
from the nearest neighboring data,  
et cetera, and more advanced methods that  
regress the missing variable.  
For example, learning a composite measure  
like the kidney donor profile index using other donor data,  
or using techniques like mice which  
incorporate multiple imputation with missing variables,  
or techniques like low rank matrix completion that  
is used by a lot of collaborative filtering  
engines like Netflix, which try to assess what  
is the rating that a user might provide to a movie,  
even if they've not seen that movie.  
However, a key difference that makes these techniques even more  
powerful is if we can incorporate the domain  
knowledge, doing which can significantly  
improve the signal the information that our data has.  
Let's see an example how.  
I want you to remember that AI and machine learning  
algorithms see the world through the lens-- that  
is, the models and the data provided by us.  
And so if we can make this lens even sharper,  
we can improve efficiency and fairness in the system.  
We can get ahead of a lot of unintended consequences  
that these models have because they  
don't have the full picture of how the data interconnects  
and depends on various factors.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.6 Handling Noise: Incorporating Domain Knowledge by Understanding Interdependencies in Data  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let me first talk about incorporating  
domain knowledge.  
There are various ways one can do this.  
The first is collecting data by understanding interdependencies  
across various variables.  
The second is collecting data labels  
when decisions are generated by a biased process.  
And the third is using the power of the foundation models  
by embedding finding data relationships  
that word embeddings encode.  
It is in fact true that the power of these methods  
can be unlocked even further by incorporating domain expertise  
within a technology team.  
Let's talk about how can we collect data  
by understanding interdependencies  
that the data has.  
We'll talk through this with an example.  
And here, we consider the problem  
of detecting critical health conditions.  
So we are interested in predicting  
whether a patient who is in an ICU  
might be likely to develop sepsis  
in the next couple of hours.  
Sepsis is a condition that is essentially a multiorgan  
failure, and it's a leading cause of morbidity globally.  
It's also the leading cause of deaths in ICUs in the US.  
Sepsis has been estimated to cost a huge amount of money.  
For example, back in 2013, sepsis  
accounted for more than $24 billion in hospital expenses,  
representing around 13% of total hospital costs in the US,  
but nearly only 3.6% of hospital stays.  
And these percentages have relatively stayed  
stable in these years.  
So for this application, we have to rely on available data  
that we have about the patient in the ICU.  
This data is called the patient's electronic health  
records data.  
And there is a lot of work that shows  
that this data can be missing, errored, and incomplete.  
For example, a physician orders labs for a patient  
assessing their condition, and these labs  
measure different levels of bloodwork.  
However, if a physician does not order some labs for a patient,  
we will never see those values in EHR data.  
The data can be collected using instruments  
that have different errors on different demographics.  
Different people can have different sensitivity  
to certain tests, and that can be reflected in the data.  
Of course, there can also be human error  
in recording the data.  
There can also be errors in the instruments that is being used.  
And therefore, the task of detecting sepsis  
is much more challenging.  
The data set we are working with is not pristine.  
It does not give us an accurate signal  
of how sick the patient is.  
So let me draw your attention to this lab that's  
called pulse oximetry.  
It's really called the fifth vital sign  
after temperature, pulse rate, respiration rate,  
and blood pressure.  
Pulse oximetry uses a quick, noninvasive monitoring technique  
that shines the light through the fingernail of a person  
to detect the changes in the color of the fingernail.  
And using that, it measures the oxygen saturation in the blood.  
However, since this vital is based on a technology that  
is more errored for darker skin tones,  
we see these errors percolate in the data that is recorded.  
Now, when we think about collecting a data set that's  
been generated through these different labs  
with different sensitivities, we see clinicians and ICU doctors  
operating with ease.  
They can read a patient's chart, and they  
have mental models that they can already correct  
for conflicting labs and data.  
Thinking back at the lens that we provide to the AI,  
we thought it would be really good  
if we could develop a mental model for AI  
as well, in the same sense as clinicians  
and ICU doctors review patient labs that change over time.  
To do this, we spoke to a lot of clinicians  
and we understood that, for them, they follow certain rules.  
They use their experience to know  
that if lactate, for instance, is more than 6,  
then bicarbonate labs should be less than 0\.  
Or if pH is more than 7, then the partial pressure of carbon  
dioxide should be less than 35 or bicarbonate  
should be less than 10\.  
They have these data interdependencies  
that are already encoded in the way  
that they read the labs data.  
So our question is, from a technological perspective,  
how can we correct the data using the clinical domain  
expertise so that it matches clinical intuition so  
that doctors can query the system  
and ask, why did the system correct  
the data in a particular way?  
And how can we find the closest possible correction  
to the recorded potentially-errored data  
that we can use in our downstream prediction  
task of sepsis?  
So one technique that has been emerging in the recent years  
is to use high-dimensional mathematical constraints  
to do this.  
We can compute what are known as projections  
onto this set of physical feasible data,  
and this provides us the most likely corrected data point.  
So imagine you have a ball, and you're trying to see what is--  
your ball is suspended in the air,  
and you're trying to see what is the closest  
point on the floor to which your projection maps to.  
It will likely be the shadow on the floor of the ball  
if the light source is placed directly on top of the ball.  
Let me give you another picture.  
So what you see here is a new patient data appears,  
but it is not in the space of physically possible data  
that a patient could generate if this was a living patient.  
This is the information that we got from clinicians.  
We can find the closest point from the error patient data  
to what is feasible.  
Let's call this the corrected data.  
We can take this process one step more further  
and we can ask for what do not so sick patients look like?  
Medically speaking, this is the set of homeostasis constraints.  
What do patients who are not as critical look like?  
And now we can use the distance of the corrected data  
from this set again from the homeostasis constraint  
to identify how sick a patient is.  
This technology in itself can help  
us collect data while incorporating  
domain constraints.  
We can push the techniques of data imputation data completion  
even further by incorporating domain knowledge.  
Can you imagine other ways of collecting data using domain  
knowledge, in the applications that you work in,  
in the systems that you are thinking of developing?  
So our research shows that data collection using projections  
can help increase AI performance on downstream tasks.  
For example, this step alone can improve the precision  
of detecting sepsis in critical patients  
six hours before onset of sepsis.  
And the edge that we get is really this cohort of patients  
who we were not able to label that they are going  
to get sepsis, in the pipeline that did not  
use trust maps, which is the projection stuff,  
but we are able to detect that on a huge set of patients  
and do preventative care.  
And, potentially, if we had this technology in place earlier,  
we would have prevented certain cases of sepsis.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.7 Handling Noise: Correcting Labels in Biased Data Sets  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now talk about how  
we can attempt to correct data labels in a system that perhaps  
collected the data through a biased process.  
The example I want you to keep in mind  
is perhaps an evaluations example,  
where there is implicit bias in evaluating people.  
And what we see are model outcomes from this process.  
Our goal will be to try and get ahead of the bias labels,  
if possible, and already make corrections in the data  
before we even use the data in model training.  
So imagine if the domain experts in a hiring  
system or an admissions system have a sense  
that a person's group information should not really  
correlate with the person's outcome--  
for example, if you've already accounted for a person's  
computer programming scores, a person's  
GPA, their work experience, how well they did in an interview,  
and so on, then the outcome should only  
be dependent on these features, but not on the person's group  
information, for example, if they're  
left-handed or right-handed.  
And if we have a sense of this from the domain experts,  
then we can use mathematical techniques  
to transform the data in a way that the group of the person  
doesn't contain information about the person's outcome.  
For example, if you know that the person is left-handed  
or right handed, you should not be  
able to predict whether this person would  
be accepted for the job.  
But while we are transforming the data,  
we want to be very true to most of the data  
that we've collected.  
So we want to enforce conditions like if two data points were  
close to each other initially, then  
they should remain close to each other after the transformation.  
And we should not lose the predictive power of AI.  
We are trying to assess who's qualified, per se,  
and we don't want to modify the data  
so much that we are not able to make this decision anymore.  
So this can be done with some very cool  
recent pre-processing techniques using optimization.  
Let's give you an intuitive explanation of what is possible.  
So here are a set of six people--  
Al, Bo, Cal, Dan, Ess, and Fu.  
And really, as mathematicians, we  
like to name our things A, B, C, D, E, F.  
And that's what I've done here.  
So for all of these people, let's say  
we have some data on what their GPA was, some data on what  
their work experience was, and we  
have an outcomes from a process which said,  
should we hire this candidate?  
Should we not hire this candidate?  
The domain expertise will answer the first question.  
Is it possible that Fu's outcome in this data set is biased?  
Domain expertise can tell us if we are missing some data,  
like there was an interview where perhaps Fu did not  
do as well.  
There was a recommendation letter, perhaps  
Fu did not do as well.  
So we can get a signal of whether we should get more data  
to make this decision.  
Otherwise, domain experts can verify,  
and they can audit these decisions.  
They can verify that perhaps this was an incorrect decision  
because a candidate who had a lower GPA--  
that is, Cal-- was accepted.  
A candidate that had a lower work experience than Fu--  
that is, Bo-- was also accepted.  
And so it's not clear why Fu was not offered the position.  
Now, the question, once we identify  
that there are some data points where this happens,  
can we use advanced techniques to automatically identify  
such cases and potentially also add  
this signal to the lens of AI that this may be a biased label,  
or this label might require some correction?  
And so there are ways to actually mathematically solve  
this problem.  
And here is what happens.  
The data is transformed in a way that it preserves  
most of its structure.  
But the label for Fu has changed from 0 to 0.7,  
indicating that it's not a perfect hiring  
outcome, but perhaps something in between that  
reduces the potential bias of that decision.  
This technique can have a huge impact on model outcomes.  
Let's see an example that's related to parole.  
So COMPAS is a system that's been  
used in a lot of states in the US  
to predict whether somebody might re-offend a crime  
or not when they're released from the prison system.  
This system was developed by Northpointe,  
and it was analyzed by ProPublica in 2016  
to show examples and classes of defendants  
where low priors were labeled as high risk,  
high priors were labeled as low risk,  
so these were types of errors in the system.  
More importantly, they showed that the type of error  
was correlated by the group of the person, the ethnicity,  
the gender, and so on.  
Now, this was a huge cause for concern  
because these decisions impact lives.  
And Kalman, et al In 2017 showed that  
the pre-processing technique that we just looked at  
can be used to reduce the unfairness in such systems.  
They used this to modify the data labels  
so that the data that the AI model is being trained on  
does not reflect extreme biases.  
And in this way, they were actually  
able to reduce the unfairness by doing a pre-processing  
of the data set.  
It would be super interesting to think  
about what other data-driven decision making pipelines can  
benefit from a pre-processing that tries to automatically  
flag data points that might have a biased label  
and try to correct these labels so that biases don't propagate  
further in AI/ML training pipelines.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.8 Handling Noise: Embedding Data with Foundational Models  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Next, let's talk about the use  
of foundation models in bringing in domain expertise  
through embeddings.  
A foundation model is a large, general purpose machine  
learning model that's trained on broad and diverse data  
so that it learns general representations and skills  
that can be adapted to many downstream tasks.  
Some examples include large language models  
like GPT 3, BERT, Claude, image and vision models like DALL-E 2,  
multimodal models that can handle combinations  
of different data types.  
These large language models are rapidly  
proliferating various applications in the society.  
Let's talk about how these models  
can be useful in incorporating domain knowledge in a very  
organic way.  
To do this, I would like you to think about word embeddings.  
Imagine that every word that we know in a language  
can be mapped to a high-dimensional mathematical  
space.  
In this example, it's just a space with two dimensions.  
Let's say I place summer at this point here on the slide.  
If I were to ask you where to place winter,  
where would you place it?  
Potentially, you would place it at a mirrored point that  
reflects its two different seasons-- one is hot,  
one is cold, and so on.  
Let's try to place another word-- fall.  
Perhaps this should be somewhere in between winter and summer.  
Let's place it there.  
How about tree?  
Well, tree is related to fall.  
Maybe we place it here.  
What about leaves?  
Leaves are much closer to trees.  
But fall also has leaves falling.  
So we place leaves there, and so on.  
Let's now think about ski.  
Well, you fall while skiing, so I guess I would place it here,  
and so on and so forth.  
What I would like you to understand  
is that word embeddings give us a way to translate concepts  
into mathematical placement.  
Concepts that are close to each other  
will reflect in an embedding as two vectors  
in a high dimensional mathematical space that  
are close to each other.  
And instead of doing this process manually,  
we would like an automatic system  
that, for different words, can tell us  
a good embedding, a good mathematical representation  
of these concepts.  
So it captures the property that similar concepts  
appear mathematically as similar vectors.  
This is where foundation models can help us.  
An emerging technique from foundation models  
is what is called tap text.  
So the idea is to incorporate the context of applications,  
we download a foundation model, fine-tune this  
with the application context.  
Interestingly, convert tabular data into natural language  
descriptions and ask the foundation model  
to give us mathematical representations  
of these natural language descriptions of the data, where  
the embeddings hopefully give us more context than we  
could have captured from the tabular form of the data itself.  
This technique can help us make use  
of all of the millions of documents that  
exist on a particular topic.  
We can fine-tune foundational models  
to the specific application and use case in our organization.  
And we can produce task dependent embeddings  
that hopefully capture the domain context better.  
Once we have these embeddings, they  
can be used across many prediction platforms.  
Here is an example of how this could look  
like in a healthcare setting.  
So imagine you have tabular data on a patient's vitals.  
This data can then be converted using simple natural language  
processing into text.  
And this text can now be fed in as a summary  
to the large language model.  
This summary may include just the tabular data.  
It could also include doctor's notes, for example.  
And then it could be used to fine-tune a large language  
model that is built specifically for this domain of healthcare,  
but not specifically for this context.  
So specifically, this work that I'm highlighting  
uses the clinical long form model,  
and it fine-tunes this, generates text embeddings that  
capture more domain information, and uses it  
in conjunction with the tabular data  
to feed into further downstream machine learning models.  
The success of this pipeline really  
depends on the information that is captured in the embeddings,  
and this is where a lot of the skill and the model development  
can happen.  
So with these techniques of data collection, data  
label correction, and embeddings that capture  
more and more domain expertise, I would like you to think about,  
do they completely solve problems with noisy error  
and missing data?  
Can we also use them to handle predictive errors  
within model pipelines?  
And how can we use these techniques  
in various application contexts that we care about?  
Of course, continuous monitoring is needed.  
We have to revisit the data development  
deployment validation pipeline.  
And these are important cutting edge problems  
that we are trying to solve in industry and academia  
so that downstream impacts of these issues can be mitigated.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.9 Handling Noise: Data and Model Uncertainty  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We now move on to data model and uncertainty.  
In this segment, let's talk about how  
to think about model uncertainty.  
As the AI and machine-learning modules in our model  
are making predictions, can we also  
assign uncertainty to these predictions  
and account for them in the future layers of the pipeline  
so the uncertainty doesn't compound  
unintended consequences?  
AI does not have a 20/20 vision.  
It doesn't see the real world with the same granularity  
as we are able to observe it.  
AI sees the world through the data and the models  
that we've provided it, through the documents that it learns on,  
through the internal representations that it  
has, through the embeddings that it's able to train and create.  
So we really need to sharpen that lens  
if we want to have an outcome that's ethical and fair.  
Let's go back to the example of evaluations data.  
We talked about how ratings might include biases  
that people have and rating systems  
might end up discriminating against Uber drivers or workers  
in the gig economy by proliferating  
the impact of those biases.  
We've also talked about various evaluation studies  
where people have changed their evaluation on a candidate based  
on their different group characteristics,  
which were not really correlated with the job preparedness.  
And as AI is training on all of this data,  
it can also make errors on people.  
It can pick up these trends and amplify them.  
So how can we estimate what are the errors in AI predictions?  
This is really crucial.  
Think back at our detective mindset  
in trying to understand, why is the pipeline making  
these unintended consequences?  
And this is an important part of it.  
So, for example, we could compute  
counterfactual predictions.  
We could ask, well, if we changed  
some aspects of a person's data, would the prediction  
on that data completely change?  
For example, in an application, we  
found that changing the nationality  
of a person in a hiring recommendation platform  
changed their fit score to a job by 150%.  
This is something that we really had  
to inspect and detect and find solutions  
to mitigate its impact, because the nationality of your person  
should not really have an impact on how good a fit  
they are to a job like waitressing, gardening,  
and so on.  
Second, it's important to estimate regions of data  
where our predictive models make more error.  
This is something that you might have seen in real life as well.  
It's really easy to reject bad ideas.  
It's very easy to accept groundbreaking ideas.  
It's really in the middle of both of these  
that we don't know whether an idea is worth pursuing or not.  
Similarly, in regions of data where  
models can make more errors, we see this happen very frequently  
in healthcare settings.  
For example, if the quality of a donor kidney is very high,  
that means the KDPI is very low.  
It's an easy decision.  
This kidney is likely to have good outcomes.  
It should be transplanted.  
If the KDPI of the donor kidney is very high,  
which effectively translates to it's a very low-quality kidney,  
it's very easy to predict that this kidney should not  
be transplanted from the data that  
is generated through the organ transplantation system.  
It's really in the center part of the data,  
when the kidney quality is medium-- this  
is where a lot of the medical expertise  
is used to identify which is a good kidney to transplant  
and which is not.  
Here, the model can make higher errors.  
And knowing this, we can be more careful in deploying AI models  
for downstream decision making.  
An emerging technique is conformal prediction,  
which tries to estimate how much the model prediction changes  
on the calibration data and uses these intervals to estimate  
errors.  
So there are many ways in which you can think  
about errors in AI predictions.  
And calibrating these errors can help us make better decisions.  
Let's see how.  
So here is your hiring outcomes data set that we have access to.  
It has features related to gender,  
the 10th class percentage, the 12th class percentage,  
the college tier, the GPA, the city tier,  
and so on, and various tests that the candidates have taken.  
We asked if we can build an AI model that predicts the computer  
science score as a proxy of how hireable this candidate could  
be for a programming task.  
When we trained this model, we realized that the accuracy of AI  
can be very contextual.  
AI could make more errors on people  
with certain characteristics and less errors on people  
with other characteristics.  
In this example, specifically, a metric  
of performance used for a simple linear regression model  
is R squared.  
And we found the model had an R squared of 0.56 on male data  
and 0.62 on female data.  
So the model was actually making somewhat less errors  
on female data.  
But something interesting happened here.  
In the data that was the training data set,  
we did not see any skew in the male performance  
compared to the female performance.  
However, in the data that was the best fit for this very  
simple and explainable linear regression model  
that you see on the slide with its coefficients published,  
this model created a positive skew for male candidates.  
So even if the model was more accurate on females,  
the error on males was giving them  
more of a benefit of the doubt and adding a higher score--  
if I am to be precise, a 16.95 points  
changed if you changed the gender  
of the candidate in this data from female to male.  
And of course, this is a simple linear regression model,  
and you could fix this by various techniques.  
But I wanted to showcase this as a pedagogical point--  
that we could have distributions of errors on different groups  
and used by our AI models that try to predict various aspects.  
And these error distributions could be very different.  
So an emerging technique in this area is to use calibrated errors  
and make decisions with the error intervals instead.  
What you see on the slide is errors  
that are estimated for the different candidates.  
And based on the error in our estimate of how  
qualified the candidate is, we are  
able to find a set of candidates whose  
data, whose performance, could potentially intersect  
with the highlighted box.  
This gives us a subset of candidates  
that we should interview, we should gather more data on.  
We should potentially consider them for the next round.  
But more importantly, it is a very transparent way  
of incorporating and acknowledging  
the measurement error we have in our AI predictions.  
To highlight this point further, we  
considered an online selection algorithm  
where we wanted to select 25 candidates  
from a pool of around 600 candidates in the test data.  
And we report selection rates over 10,000 runs.  
The main takeaway from this is, if we simply  
used the ML predictions without having an eye towards the error  
intervals, we would end up selecting many more  
male candidates than females.  
If we used quotas, we would end up  
overcorrecting the selection in a way that did not  
reflect the data distribution.  
However, accounting for errors that  
are calibrated for the AI model, we  
were able to show that now the selection rates tracked  
the trends that we saw in the data  
and did not exacerbate the disparity due to the predictions  
incorporating an error.  
Finally, I would like to emphasize  
that the use of these intervals and error calibration  
to account for errors in our model pipeline, the model  
predictions, can improve selection ratios,  
can improve decisions downstream,  
without resorting to practices like enforcing quotas.  
And from US perspective, we also discussed  
that this approach is compatible with Title VII  
and provides a way for organizations  
to navigate disparate impact and treatment.  
To summarize, I strongly believe that human AI collaborative  
pipelines that account for uncertainty in the data,  
account for domain expertise, and calibrate  
the noise in AI models are much more fairer and robust.  
We need to have strategies like data completion and correction  
using domain constraints, data label processing,  
by combining knowledge from auditors and domain experts.  
Finding if we can get more bang for the buck using word  
embeddings from foundation models  
as well as calibrating noise in AI  
can really help mitigate the impacts on downstream decisions  
and help us build collaborative pipelines that  
are transparent about the error and uncertainty  
in various places of the pipeline  
and ultimately lead to fairer and robust decisions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.10 Aligning Goals: Encoding Values in Objectives  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So last but not the least, in this segment,  
I would like to discuss how we can navigate the interaction  
of AI and optimization.  
The key questions we would like to think about here  
are, how do we encode model choices that  
are aligned with our values?  
How can we make decisions, even when  
these values might be competing, when  
we have competing objectives?  
And are there ways to reduce compounding effects,  
algorithmic monoculture, feedback loops, et cetera?  
So let's start with encoding values in models.  
Let's think back about the data models and decision pipeline.  
And here we are really trying to understand,  
how can we develop our models that  
reflect the values or fairness that we would like  
in our decisions, and how can we build that into the model  
development itself?  
One way to do this is to regularize the model.  
It's a way that we use to trade off various objectives.  
For example, model efficiency with model sparsity  
will give you regularized machine-learning models that  
don't use a lot of variables.  
In this case, I want you to think about regularization  
as a pull of the solution by two directions.  
One is signified by the left team that  
cares about efficiency, the other  
by the right-side team that cares about fairness.  
And if we can formulate this mathematically,  
then we can try to get solutions that are not  
to the left extreme or the right extreme  
but perhaps at an operating point  
that the stakeholders and the decision makers like.  
Mathematically, we think about this  
as some sort of a maximization problem  
that tries to maximize the efficiency plus some strength  
to incorporating fairness.  
And as we change lambda, which controls the relative strength  
of the fairness objective, you can  
imagine that the team on the right-hand side  
is becoming stronger.  
So your model's operating point is  
pushed more towards a fairer strategy versus more  
towards an efficiency strategy.  
Let's make this a little bit more precise.  
So imagine that we want to train our models with fairness  
built into the objectives.  
Here we can ask for an efficient model that  
minimizes a least-squares loss, the errors that the model makes  
in the decisions.  
Or we could ask for a model that minimizes the cost of operation  
or maximizes the profit, et cetera.  
We could think about quantifying unfairness  
and ask to minimize unfairness in multiple ways--  
for example, minimizing false positive rates  
across different groups.  
So think about the parole and the COMPAS examples again--  
minimizing the maximum false positive rate across any group,  
or minimizing some combination of maximum false positive rate  
across any group, maximum false negative rate across any group.  
So you can think about various ways to quantify fairness.  
And a key question is, how can we select lambda?  
Another question is, what should be the notion of fairness?  
And the third is, what is the operating point that we  
should decide for our model?  
Note that injecting even a small amount of fairness  
really helps move away from solutions  
that might prioritize certain groups simply  
because of the data interactions.  
Let's go back to the COMPAS data again,  
where we saw the impact of data preprocessing techniques.  
In this case, let's see what model training with fairness  
objectives can get us.  
The operating point in this model  
gave us a false positive rate of 0.29  
using a simple logistic regression model  
that we trained ourselves, and the false positive rate again  
had a disparity between the two populations,  
as I highlighted before.  
It was really high for African Americans  
and much lower for Caucasians only.  
Let's try retraining the model with the fairness objective  
baked in with a regularization penalty of 0.5, I think.  
So in this data set, we modeled our fairness objective  
as minimizing the false positive rate disparity across the two  
groups.  
And as you can see, as we change lambda slowly,  
the AUC, which models the accuracy of the model,  
it doesn't fall too much.  
This is the area under the curve,  
but you can effectively think of it  
as a metric to understand model performance.  
That metric is more or less stable.  
However, at lambda 0.10 already, we can see that the disparity  
of false positive rates across these groups has significantly  
reduced.  
And this is why I say injecting a small amount of fairness  
in your efficiency objective can really  
help move model decisions that are much more fair  
and cause much less disparate impact.  
In this specific case, you can see  
that the false positive rate across the two groups  
and overall is now at a 0.18.  
One could imagine that this might seem fair  
from the fairness notion we have defined,  
but it does induce a higher false positive rate  
for the Caucasian-only population,  
and this is something that we need  
to be cognizant of when using this technique.  
We need to go back to what our model was doing originally  
and see that we don't worsen the outcomes  
for different groups of people.  
Here is a mental model that I would  
like you to keep in mind when thinking about trade-offs  
between various objectives.  
Imagine that we are in a system where  
we are trying to maximize fairness,  
so we want to move as much on the x-axis as possible.  
And we want to minimize the cost,  
so you want to keep the y-axis as low as possible.  
We could have two solutions.  
If you were just maximizing fairness, the cost of operations  
could be really high.  
If we were minimizing cost, unfairness could be really high,  
or fairness in the system could be very low.  
What we can do is we can think about trade-offs  
between these two and optimize a set of objectives  
that trade off cost and fairness differently.  
And this is what generates what is known  
as a Pareto-optimal frontier.  
This is a very well-studied area in operations research,  
and I would urge you to think about Pareto-optimal solutions  
in various applications.  
These solutions for a given cost of operations  
will maximize fairness and, for a given level of fairness,  
will minimize the cost.  
Every other solution is suboptimal,  
and it is dominated by something in the Pareto frontier.  
And now the decision is really about which operating point  
we would like in the model from Pareto frontier.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.11 Aligning Goals: Navigating Competing Objectives  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: What we discussed in the last segment  
is how to align the values that we would like in a system  
within the model training itself,  
how we can regularize model objectives to balance  
between efficiency and fairness.  
In this segment, I would like to discuss  
how can we navigate multiple criteria requirements?  
For example, here is a table from Marsh and Schelling  
in '93 that already proposed 24 different notions of fairness  
for planning in a facility location.  
In this segment, I would like to reflect about situations where  
we don't have any consensus on which notion of fairness  
we should have.  
If we don't have consensus on how to trade off  
across robustness, resilience, efficiency, operating  
costs, retention factors, and so on,  
then how can we still make decisions in such situations  
that align with our organizational values?  
Here is a hypothetical example now  
in a similar vein as opening pharmacies and opening hospitals  
that we talked about earlier.  
So imagine we have a set of objectives where we can really  
have a lever that helps US trade off  
between efficiency and fairness of various thoughts.  
As we trade this off, the optimum solution  
of where to place the hospital will  
change, creating for every point that's  
continuous on that lever that gives us a different operating  
point.  
And as we change these solutions,  
we might get an infinite set of optimal solutions, which  
is very hard to navigate.  
So ideally, what we would like is small set  
of representative solutions that are enough  
and that capture every possible objective that people could have  
on the decision-making table.  
Of course, there's a huge problem.  
Our objectives are underspecified.  
We don't know exactly various trade-offs  
between different criteria.  
And we would like to capture all of these  
with a small set of solutions.  
So here is a big idea.  
When we face a big decision, like where to build a hospital,  
who gets a scarce resource, or how to recover after a disaster,  
there isn't just one right answer.  
There's a whole landscape of possible solutions shaped  
by competing values and trade-offs and the voices  
of different stakeholders.  
But here's where AI can help us summarize and navigate  
this complex landscape.  
Let me tell you how this happens with some more  
intuitive examples.  
Our goal is to create a small portfolio of decisions using  
the following information.  
Let's suppose we are given a characterization of decisions  
that we want to open facilities, or we  
want to find a schedule for jobs on a cluster,  
or we want to optimize over roads and routes in the city.  
We want to find matchings of students to schools, et cetera.  
And let's say we have a large set  
of structured, under-specified set of objectives.  
For example, we could say I want a trade-off between all  
of these notions of fairness and efficiency  
with all types of weights in between them,  
but I don't know how this model choice is really  
going to affect my outcomes.  
And I would like to have a smaller set of solutions  
so that each potential choice of these weights and trade-offs  
is well-represented in the set.  
Then, as a decision-making group,  
we could sit around the table, we  
could focus on the properties of these three to five decisions,  
and we can consider carefully and we  
can find the right operating point for the organization.  
So how can we build something like this?  
Here is the mathematical intuition for this.  
Let's suppose this is my space of possible decisions.  
It's what we call a polyhedron.  
And let's say there are about four simple linear objectives  
that I want to maximize.  
So I'm trying to walk in these directions  
and find the furthest point along these directions  
in this decision space X. So can we  
find a portfolio that satisfies all of these objectives?  
And the answer is yes.  
Let's see how.  
For the green objective, we can have  
this set of solutions that lie towards the right side  
of this green line.  
For the pink objective, we can, again,  
draw a set of reasonable solutions  
that capture how far we can move along that direction.  
For the blue objective, again, we can do the same thing.  
And for the brown one, we can do the same thing.  
And you will realize that if I take the optimal operating  
point for the brown objective, and I  
can take the red point that's highlighted for the other three,  
I reasonably capture the two possible operating  
points, two possible decisions that capture all four  
of these objectives.  
There are various mathematical techniques and AI systems  
that we can build that help us navigate and summarize  
the set of possible decisions.  
Let me give you an example of how this set can change  
as you relax the criteria.  
If you don't want every objective  
to be perfectly represented, then we  
can actually make do with a smaller portfolio.  
So think about this.  
If you want the best possible solution for every objective  
to be in the portfolio of solutions,  
we have to have a much larger set.  
If you're satisfied with a good enough solution  
for the various objectives, then we  
can make do with a smaller set of solutions.  
And there is a lot of recent work  
that tries to characterize this trade-off.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.12 Aligning Goals: Competing Objectives in Resource Allocation  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's ground this in the data models and decisions  
pipeline.  
So we talked about how there's noisy data, how  
we have model choices, and how we can use these models to make  
data driven decisions.  
What happens in many applications  
is that there is no one way to encode the values  
and align the models with the values of our organization.  
So perhaps there are many different ways to do that.  
And this can be identified by humans in the loop, humans that  
are involved in making these decisions  
and choices for the types of models we should be considering  
to encode the voice of various stakeholders.  
Where AI can help us is really summarize  
the impact of all of these large set of models  
into a much smaller set of decisions  
so that we can iterate and find the right operating  
point in the organization.  
As concrete examples, let's look at this article  
from New York Times in October of 2024,  
which depicts the pharmacies that were closed since 2015\.  
There's a large number of pharmacies  
that have been closed in the US, and the key question  
is, how can we increase access to medical facilities  
and pharmacies in the US by planning infrastructure  
in the right locations?  
In this case, there could be many ways  
to look at the problem.  
And here is an application that we developed  
that showcases where medical deserts appear where people  
don't have access to pharmacies within a specified radius  
and have a specified fraction of the population below poverty  
line.  
Analyzing the census tracts, we can construct a portfolio  
of solutions of where pharmacies can be placed and identify  
what's the impact of these solutions on different groups  
of people, what's the impact of these solutions in the cost  
of opening these, what's the induced distances, and so on.  
This is really powerful because it  
helps us be very intentional about aligning values  
in our model operations, aligning organizational values  
in the model decisions.  
As another example, I would like to highlight a reinforcement  
learning environment where multiple stakeholders can have  
different rewards or different actions  
that they would like to be prioritized.  
In such an example, again, it's unclear on whose voice should  
be prioritized, as prioritizing different groups  
and different voices in the system  
can give us a very different set of reinforcement learning  
policies.  
As an example, I want you to think about a resource  
allocation setting, where every population that gets a resource  
will have a different value for the resource.  
They will have a different expectation of what the resource  
allocation policy can be.  
Let's think about a call center.  
And as an example I will draw from this NGO  
in India which is called ARMMAN.  
ARMMAN partners with hospitals and it  
operates across various states in India  
to provide information about prenatal care  
to expecting mothers.  
ARMMAN faces a challenge.  
Should they have automated calls to expecting mothers  
to provide the information?  
Or should they have human callers call their beneficiaries  
with information?  
Calls by humans are restricted in number.  
However, these calls can engage mothers better.  
So imagine a call center agent that asks a language model  
that you should give me a policy that prioritizes low income  
beneficiaries and minimizes reward shift in the education  
feature.  
I want our operating call center policy  
to be close to having the same impact at different levels  
of education, but I would like to prioritize low income  
beneficiaries through the allocation of calls.  
The large language model in itself  
can now act as a generating process  
and generate a large number of potential objectives and rewards  
that are aligned with the human's preferences.  
We can, again ask a similar question  
of how can we design a small set of policies that capture what  
the human decision maker is intending,  
without giving them a large space of potential outcomes  
and overwhelming the decision making process.  
So here is an example where we show  
that there are three policies that the call center could  
operate on in a particular month or a week,  
and the impact that these policies can  
have on the different features.  
We have to remember that the data that we have about people  
does not cleanly divide into different groups.  
The impact on education will also  
have an impact on mothers or various ages.  
It will also have an impact on mothers with different income  
levels.  
And finding portfolios of decisions,  
and understanding their interdependence  
of the impact induced by these decisions  
is very important in making ethical decisions  
from an automated pipeline.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.13 Other Strategies for Building Ethical Systems  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: With this, I would like  
to wrap up by summarizing and highlighting  
a few different ideas in building ethical systems.  
So far, we've talked about ways of handling noisy data.  
We've talked about model calibration,  
aligning values in the model training  
through objectives and regularization,  
and constructing portfolios when we are not  
clear about various parameters ourselves  
and we would like to see the space of induced decisions.  
There are many other ways in which  
we can mitigate the impact of feedback loops, in which we can  
get around algorithmic monoculture  
and think about translating policy with data driven decision  
pipelines.  
And I will just give you a quick intuition  
of some of these ideas.  
So for feedback loops, it helps to provide better protection  
to vulnerable communities, assuming  
that decisions might not be very robust for these  
if we can already think about building that robustness  
in the pipeline.  
We can also constrain the AI system  
from moving too far from previous operating  
points due to data changes.  
We can ask the AI system to not deviate too much  
from the previous data distribution that it saw,  
so we can get ahead of unintended consequences  
with feedback loops.  
Secondly, to understand algorithmic monoculture,  
it will help to understand which data most of the algorithms  
make errors on and then be transparent about this data,  
defer decisions when we are operating with this data,  
try to find better models for this  
and build strategic portfolios that cover all of the data.  
Prioritizing model diversity and creativity  
will help in reducing algorithmic monoculture.  
And this is where I see a huge impact humans can have.  
Lastly, translating policy is not easy.  
Translating policy into objectives  
that are specific for model training is not easy.  
It is important to keep updating the data driven decisions  
pipeline so we can protect against interactions  
between data, the network, the society, the socioeconomic data  
that we have that interacts at so many levels  
so that the intended policies can actually be implemented.  
To end, I would like to highlight a vision  
that our future relies on careful, calibrated, and  
knowledgeable human AI systems where humans know  
the right questions to probe, the right questions to ask,  
the right ways to modify and constrain  
these automated decision making systems.  
And AI has a sharper view on the context in which we  
are generating data, in the constraints that our real model,  
real world operates in, and societal expectations where  
AI knows how to align values, and AI  
knows how to help humans navigate  
the set of complex possibilities and the decision space.  
I believe together, we can really  
build ethical systems that scale and provide equal opportunity  
to everyone in the society.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this lecture, we argued that many ethical failures in AI are caused by predictable, diagnosable pipeline failures: partial observability, imperfect measurement, noisy labels, and unmanaged trade-offs. The parole example makes this vivid: because outcomes are only observed for people who were granted parole, a model can look strong on standard evaluation while remaining effectively untested on the population that was denied parole. That blind spot motivates a more disciplined practice of ethical AI: treat error analysis as a first-class diagnostic (FPR vs. FNR), introduce guardrails when evidence is weak and reduce overconfidence by making uncertainty explicit.

A second theme of this lecture was that progress often comes less from more complex algorithms and more from better data work. We can use domain knowledge to correct inconsistencies, constrain what counts as plausible data, or repair biased labels. We also discussed multi-objective design, where values must be encoded operationally through objectives and constraints, and trade-offs should be surfaced transparently (e.g., via a Pareto frontier or a portfolio of policies) rather than just looking at a single metric like accuracy.

Key Takeaways  
Standard training and validation can give a distorted picture when outcomes are observed only for a selected subset of cases (e.g granted parole). The model has no grounding in a substantial part of cases.  
Ethical evaluation cannot stop at overall accuracy. Various error types must be considered: look at false positive and false negative rates, who is exposed to each kind of error, and whether error rates differ across groups.  
In many systems, the highest-leverage intervention is in the data itself. Domain knowledge can improve robustness by correcting data through known interdependencies, repairing biased labels, and constraining or completing records so they remain consistent with real-world relationships.  
Uncertainty should inform action: calibrated uncertainty estimates help determine when to act and when to defer, and prevent downstream decision layers from treating weak evidence as certainty. Useful tools include counterfactual-style sensitivity checks, identifying regions of the feature space where errors cluster, and distribution-aware calibration methods such as conformal prediction intervals.  
Values like fairness, accountability, transparency, and explainability must become explicit objectives, constraints, and monitoring rules. They must also guide accountable trade-off decisions, for example, via Pareto frontiers or portfolios of policies.  
Deployment can create risks over time: feedback loops and algorithmic monoculture can gradually worsen outcomes. Systems must therefore include safeguards against drift across iterations. Do not rely on a single dominant system, but encourage model diversity.  
Wrap-up  
You should now be able to (i) identify when evaluation is unreliable due to selective observation, (ii) audit systems via group-conditional error analysis and uncertainty-aware guardrails, (iii) see when data/label repair and domain constraints are the highest-return interventions, and (iv) frame ethical deployment as a multi-objective, socio-technical design problem rather than a single-metric optimization.  
\`\`\`

Recitation 1: Hiring Experiments on Noisy Data  
\`\`\`  
Skip to main content  
Recitation Overview  
Welcome to Recitation 1: Hiring Experiments on Noisy Data, taught by Catherine Oellig, Visiting Student Researcher at Massachusetts Institute of Technology. This recitation emphasizes material discussed in L2.1 Noise and Uncertainty in Data: Introduction, L3.7 Handling Noise: Correcting Labels in Biased Data Sets, and L3.9 Handling Noise: Data and Model Uncertainty. It builds on research done in Salem and Gupta (2019).

In many labor markets, hiring screenings are one of the highest-impact decision systems ran at scale. Who gets invited to interview affects income, access to healthcare, continuing education, and long-run mobility, not only for an individual, but for families and communities over time. At the same time, employers face a practical constraint: modern applicant pools so big that some form of automated screening or ranking must be used simply to manage volume.

This creates a core tension. Employers may want processes that are both effective and defensible (i.e. finding strong candidates consistently, tailored to a target job and fair across protected groups), but these decisions have to be made with only inaccurate scores or proxy predictors.

This recitation exemplifies how a prediction layer trained on noisy data can lead to uneven downstream outcomes and how to overcome error asymmetries with conformal intervals.

The recitations focus on applying the theory from the lecture to a concrete case study. The experiments, visualizations, and much of the discussion will take place through an accompanying Jupyter notebook, which is intended to make the material more interactive and hands-on. We encourage you to open, download, and explore the notebook yourself, and to play around with the code and outputs as you work through the recitation.  
\`\`\`

R1.1 Overview  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, I'm Catherine Oellig  
and I will be your TA for this lecture series.  
I will walk you through two recitations,  
so let's kick off with recitation one.  
The background for this recitation  
is that we will be looking at hiring experiments.  
In many labor markets, the hiring pipeline  
is one of the highest impact decision  
systems we run at scale.  
Who gets invited to an interview affects  
income, access to healthcare, continuing education,  
and long-run mobility, not only for an individual,  
but for families and communities over time.  
At the same time, employers face a practical constraint.  
Modern applicant pools are so big that they  
need some kind of automated screening or ranking  
just to simply manage the volume.  
This creates a core tension.  
Employers want to process applicants  
so that it both feels effective, so they find strong candidates,  
and defensible at the same time.  
So they want to make consistent decisions.  
They want to have job-related decisions,  
and they want to be fair across protected groups.  
But these decisions have to be made with only inaccurate scores  
or predictors.  
Now, this is the key modeling point for today's recitation.  
Even if we optimize or implement any explicit fairness  
constraint, the prediction layer can already  
generate uneven downstream outcomes.  
So in an applicant screening, we rarely  
observe the true quality of a candidate.  
Instead, we observe some kind of proxy outcome,  
such as a standardized programming  
score or historical features, which  
we can then use to predict new candidate scores with.  
But prediction error is not uniform,  
and different groups can experience different error  
patterns, even when the overall accuracy looks reasonable.  
And this matters because ranking decisions  
amplify error asymmetries.  
If we take point predictions and select the top 10%  
for interviews, we may systematically  
favor the group for which predictions  
are more optimistic or less noisy,  
even if the true top candidates are more balanced.  
In other words, small differences in error structure  
can translate into large differences  
in who gets selected for a job interview.  
That's why this recitation focuses  
on uncertainty aware selection, which  
was developed in Salem and Gupta's work  
on hiring individuals under a partially ordered information  
due to noisy candidate evaluation.  
The core idea is to make uncertainty explicit  
and then make decisions that respect that.  
Rather than treating a predicted score as the ground truth,  
we will compute an interval that likely contains that score.  
These intervals then induce a partial order called a posit.  
Just using point predictions to estimate  
a candidate's skill level can be unfair  
if uncertainty is different across candidates.  
Therefore, we will zoom in on this dynamic.  
We will start with linear regression.  
We will look at a linear regression  
with and without gender and summarize bias and standard  
deviations of errors by gender group,  
and then evaluate what happens when we select the top 10%  
by point predictions.  
When we see that this ranking does not  
align with the ground truth across genders,  
we introduce conformal prediction intervals  
to calibrate uncertainty.  
We will then use a posit-style selection rule  
that prioritizes candidates who are  
in the top set with high probability,  
rather than those who merely have point estimates.  
The goal here is not to force a demographic outcome  
but to prevent an error structure from becoming  
a hidden mechanism that distorts outcomes.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.2 Data Loading and Score Distributions  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: OK, let's move on to loading the data  
and looking at the initial score distributions.  
For our hiring experiment, we will  
use a subset of the Aspiring Minds Employability Outcomes  
from 2015\.  
AMEO combines candidate profile information  
with early employment outcomes for engineering graduates.  
In addition to outcomes such as first job salary, title,  
and location, it includes standardized assessment scores  
spanning cognitive skills, domain skills, and personality  
assessments, along with basic demographic and educational  
background variables.  
In this recitation, we will treat  
the data set as a stylized example of a historic hiring  
pipeline, and we will observe the candidate features  
available at screening time and as a proxy target  
for job-relevant skills.  
Concretely, our target label is the candidate's  
standardized programming score, which  
we will interpret as a proxy for the underlying programming  
abilities.  
We start by loading a clean subset of the AMEO data set  
and select candidates that have a valid programming score,  
which ends up being the 2,212 candidates that you see here.  
We then want to construct two feature sets,  
so one that includes 20 screening variables  
and the other that includes 21 because one includes gender  
and one excludes it.  
We want to make sure to exclude features  
that could leak into our desired goal of predicting a computer  
programming score.  
So we leave out features such as computer science class grades,  
programming grades, programming scores,  
anything that is too similar to our computer science scores.  
And at the same time, we try to include predictive features  
such as experience, GPA, courses in college,  
that nevertheless kind of line up with what you would expect  
to see in a hiring pipeline.  
At this point, we already see that the data set is somewhat  
unbalanced, so we have three times as many male candidates  
as female candidates.  
If we then go on to plot the score distributions by gender--  
so the true scores that they have achieved historically--  
we already see two patterns.  
So on the one hand, we see that there's a mean shift.  
The male distribution is shifted to the right.  
And the mean score for women is about 20 points higher  
than for women.  
At the same time, we also see that there's dispersion.  
So there's a larger standard deviation for men.  
And this is visible in a higher spread, and a bit more mass  
on both of the extreme sides of the scores.  
We also see here in this boxplot how much more  
the standard deviation deviates between the two genders.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.3 Train / Calibration / Test Split  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We then move on to creating a training,  
calibration, and testing split.  
So later on, for formal prediction,  
we will need a separate calibration set.  
And so we split the data into training data, so 60%  
that we will use to fit the model and estimate bias.  
And another 20% will be calibration,  
which we will use later on to compute the conformal quantiles,  
and then the remaining 20% we will  
use to evaluate our selections.  
So once we have run this, we see that our data splits  
are the following, and we use the function stratify  
up here that ensures that our distribution of gender  
stays the same along the different sub data sets.  
We can then move on to model training.  
So we will train a linear regression model  
to learn a mapping from the applicant features, so  
all of the background variables, the test components, GPA, et  
cetera, and try to score a continuous outcome variable  
y, the programming score.  
A trained regression model outputs a point prediction,  
which we interpret as the model's best estimate  
for a score of a candidate.  
At this point, we deliberately train two models.  
So one will be trained on all of the features, except for gender,  
and the other one will include gender.  
Before diving into group-specific error patterns,  
we take a first look at the overall predictive performance  
using R-squared, also called the coefficient of determination.  
R-squared measures how much of variation in true score,  
the model explains, compared to a simple baseline that  
predicts the same constant value, the historic mean,  
for everyone.  
An R-squared mean near 0 means that the model is not  
doing better than a predicted average score  
for every candidate in the training data,  
and R-squared near 1 means it has perfect predictions,  
but this could also mean overfitting.  
An R-squared that's negative is the worst  
in predicting the mean.  
So let's look at an R-squared for our models.  
So we see that the model trained with gender  
has a slightly higher R2 than the model without gender.  
That means that it reduces the squared error by about 60%  
relative to the predicted mean baseline.  
That means we have a slight gain in prediction accuracy  
by including gender.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.4 Bias and Standard Deviation Analysis  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: But if we now look at the bias  
and the standard deviations of these models.  
So as a little refresher, the prediction error  
is defined as the difference between the underlying true  
score and the predicted score.  
We can then look at this prediction error across groups.  
So in our case, we will look at female versus male candidates.  
And then compute the bias as the average over the prediction  
error.  
To interpret this, you must know that bias that is larger  
than c is 0 means that a model over predicts for groups  
on average, a bias smaller than 0  
means that model under-predicts for groups on average,  
and around 0 means that the model would  
be approximately unbiased on average for said group.  
If one group is systematically under-predicted,  
fewer members of that group will appear in the top tail.  
And in a hiring setting, that means  
that the top tail are those candidates that will  
be selected for interviews.  
So even if their true scores are high, if there's this shift,  
then these people won't be selected for interviews.  
We then also will look at the standard deviation  
of the prediction error calculated as such,  
and a larger standard deviation per group  
means that the model is less reliable for a group,  
so there's more spread in the errors,  
and a smaller standard deviation means that predictions  
are more consistent for group.  
But even if a bias for a group is near 0,  
a group with a larger standard deviation  
can have surprisingly large errors.  
So if we compute these predictions and errors  
on the training set, we see that the linear regression  
with gender has a bias for both groups at around 0,  
and relatively similar standard deviations for both models.  
Linear regression without gender slightly under-predicts  
male candidates and slightly over-predicts female candidates.  
So on average it scores, women, female candidates  
10 points higher than male candidates.  
We can then look at the coefficients  
of the linear regression, and I will standardize these  
so that we see the scores as normalized.  
Otherwise, since GPA or a programming score  
can be on different axes, we would see a big shift.  
So by standardizing these, we see a proportional impact  
of these different features.  
And if we compare, then we see that both of these models  
use same--  
assert value to the same features.  
For example, domain, logical skills, quantitative skills,  
and your college GPA are both very, very important.  
Your mechanical engineering skills  
are important for achieving a high score.  
But in the model with gender, even though women on average  
score higher, the male feature vector  
has an impact of 6.5 points.  
That means that even though we do not see bias,  
there is a shift, depending on your gender.  
So if we now use these models to rank the top candidates  
in the test set, as we do here, we  
see that in the true data set, 15.6% of all candidates  
in the top 10% would be female.  
In our predicted data sets for our prediction,  
including gender, we only get 13.3% female candidates.  
So there's a 2.2% drop, which kind of translates  
to actually one candidate less between  
female and male candidates.  
We also see that our hit rate is relatively poor,  
so we only get 25 candidates that we  
predict to have a high programming score that actually  
have a high programming score.  
But this is just due to the fact that we  
are using linear regression as an abstracted example.  
If we were to use a model like XGBoost,  
we could expect higher hit rates.  
We see that the linear regression without gender  
has a slightly higher hit rate, but over-predicts  
female candidates.  
So we see that there's a 4.4% lift in percentage  
of female candidates selected for the top 10% of candidates,  
and those would be the candidates that would  
be invited for a job interview.  
So we see that there is a prediction  
gap between how many women and men would  
have been selected in the top 10%  
depending on what kind of model we use.  
And it also differs from the true programming scores  
or the true candidates that we would  
have liked to have selected.  
Is there a way we can fix this?  
So with this, we see that including gender  
can improve the fit, but it also directly uses  
a protected attribute to make a prediction.  
Dropping gender does not automatically  
remove gender effects, as we have  
seen, because other features could act as proxies.  
So no gender is not the same as fair.  
This motivates moving from point estimates  
to calibrating uncertainty across groups using  
conformal predictions, and then we  
will later on use a posit-based uncertainty-aware selection  
mechanism.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.5 Bias-Corrected Conformal Prediction Intervals  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So how do we calculate bias graded  
conformal prediction intervals?  
We first will recenter our distribution.  
So we estimate the average prediction error for each group,  
and then we shift the distribution  
to account for this bias.  
After the step, Intuitively, the model  
is no longer systematically over or under predicting for a group,  
at least on the training data.  
Then, to calculate our conformal quantiles,  
we will look at a separate calibration set.  
So the first step was on the training set.  
And now we will look at the calibration set  
and compute absolute residuals, so absolute prediction error  
after bias correction.  
For each group, we then choose a quantile,  
which is the 1 minus alpha quantile of these residuals  
within a group.  
So intuitively, this means that this quantile  
captures how noisy predictions are for a group.  
And the noisier groups get larger  
and thus get a larger quantile point and thus wider intervals.  
So you can imagine that we look at where the probability mass  
of these distributions sit.  
And if we have larger tails for one group,  
then we know that the quantile will be larger.  
So if a group's predictions are noisier,  
larger errors occur more often, and the threshold  
will be larger.  
If a group's predictions are tighter,  
then the interval will be smaller.  
This interval width then becomes a group's uncertainty radius.  
So for every new candidate, we can then  
output an interval centered at the bias-corrected prediction  
with an half width equal to the group's calibrated uncertainty  
radius.  
Concretely, this interval then says,  
given what we saw in calibration,  
the true score is likely to fall within this range  
around our prediction.  
And since we use these conformal quantiles for the width  
calculation of the intervals for this certainty,  
we call these intervals conformal intervals.  
In our setting, we will use 40% coverage  
to keep these intervals relatively narrow.  
This trades off statistic reliability for sharper ranking.  
So higher coverage, smaller alpha  
would produce wider intervals and a more conservative  
selection, while lower coverage produces narrow intervals  
but more misses.  
So we set our target coverage, and we set our alpha.  
And then we compute predictions on calibration and test sets.  
So here, we compute the conformal quantiles first.  
And we see that, for the linear regression with gender,  
the quantile threshold is a lot higher  
for the male candidates than for the female candidates.  
That means that the width of the uncertainty  
interval for male candidates will be larger  
than the width for female candidates.  
We can also look at this for the no gender regression  
and see a similar behavior.  
So the width will also be larger for the male candidates.  
This just means that in the predictions,  
we have on average more error.  
So we want to account on average for this error.  
When we then build these bias-corrected conformal  
intervals on the test set, we see--  
we can look at our coverage.  
And so this coverage means that of all predictions across all  
predictions that we make, we want at least--  
this was our target--  
40% to actually be inside these intervals.  
And we see that we achieved this.  
And for the no gender linear regression,  
we even see that the male coverage  
is slightly higher due to them being larger and due to there  
being more prediction errors.  
So all of this leads to the male candidate predictions  
to be slightly more conservative than the female candidate  
predictions, accounting for this large standard deviation  
in the errors that we saw previously.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.6 Poset Selection  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: After having calculated our bias corrected  
conformal predictions, each candidate now no longer  
is just a single score.  
So instead, each candidate has a prediction interval,  
a plausible range for their true programming score.  
And it reflects the uncertainty that we have for their group.  
This naturally leads to a key decision point.  
If a model is uncertain about the exact ordering  
of the candidates near the cutoff,  
how should we make the top 10% interview decision  
without pretending that the point predictions are precise?  
These intervals induce a partial ordering among candidates,  
so if candidate A's entire interval  
sits above candidate B's interval, then  
clearly candidate A would be a stronger candidate.  
If the intervals overlap, then the ordering between A and B is  
ambiguous, so the model cannot confidently say who is better.  
This is why this approach is often described as posit-based.  
So we are no longer forcing a complete ranking  
of every candidate, but rather some candidates  
whose intervals overlap are allowed to be incomparable.  
Similarly, this idea in the screening pipeline, we  
translate each interval into a conservative score.  
And we'll look at the lower end of the interval.  
So in this notebook we use that lower  
bound to select the candidates and we choose a lower bound  
cutoff so that exactly 10% of all of the candidates  
lie above it.  
And then we select everyone above the cutoff.  
So this is what we do here.  
We want the top 10%.  
In our ground truth, we see that this  
is the gender distribution in the top 10%  
And now we try to find posits.  
Now we try to find thresholds for the genders  
to accommodate this.  
Conceptually, this means that we're  
selecting candidates who look stronger,  
even under cautious uncertainty-aware estimates  
rather than those that merely have a high point prediction.  
The lower bound rule reduces the chance  
of over-selecting candidates whose high point prediction  
is mostly an artifact of noise.  
It is important to understand that a posit selection does not  
force parity, and it does not guarantee equal selection rates  
across gender.  
Instead, it reduces imbalance that  
is introduced by prediction and ranking itself.  
So by requiring the candidates to be  
strong under conservative uncertainty-aware score,  
we bring more fairness into our ranking.  
If the true top 10% in the data set is imbalanced,  
a well-calibrated conservative rule  
will tend to match that reality rather than equalize it.  
So if we now look at our top 10% selections  
and compare the raw top 10% selection  
to the posit selection, we see that the posit selection  
rule has lifted our gender distributions.  
So now we see that even though our hits have stayed the same,  
so how many of our predicted candidates would have actually  
been in the selected candidate pool  
if we had known their true programming score  
stays around the same.  
But we see that now our gender distribution  
matches because of this group-based positive approach  
that we used.  
We can also visualize these posit intervals  
and actually see the ranking.  
So what I want you to pay attention to  
is that the red line is our top 10% cut off.  
And so we see that this female candidate is the last candidate  
that was selected.  
The other candidates below this, because they are slightly grayed  
out, have not been selected.  
The other two lines that I've plotted  
are one in green, the true programming score.  
So if a candidate had a programming score above this,  
they would have been in the top 10%  
depending on this true programming score.  
And the blue line is our predicted programming score  
before we did all of these conformal interval shifts.  
Then I've also plotted our predictions  
for blue for male candidates and pink for female candidates,  
and their true scores in green.  
A green circle means that they were selected in the ground  
truth, a X means that they would have  
not have been selected in the ground truth, which we can see  
because this is the cutoff off and so all  
of the candidates with a true score beneath this cutoff  
would not have been selected.  
So here we actually see the posit shift in action.  
Rather than just looking at this point prediction,  
we have these intervals that reflect the uncertainty  
around our estimates.  
And we see that the uncertainty around the male candidates  
is slightly larger due to a higher standard deviation.  
We also see that the main difference here  
is whether or not we would have included this candidate  
or this candidate.  
Due to the lower bound selection,  
we would select the female candidate.  
We can also output the detailed selection.  
So for example, for the linear regression with gender,  
we see their true programming score,  
their predicted programming score,  
and the lower and upper bounds that we have calculated  
with the conformal intervals.  
We then see our top 20 candidates,  
and we see if they are actually also in the ground truth or not.  
So here we see which ones we included in the top 10%  
even though they wouldn't have been.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.7 Key Takeaways  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's talk about the key takeaways.  
On the one hand, prediction bias is group dependent,  
so even when overall fit looks reasonable,  
the model can systematically overpredict for one gender  
and under-predict for the other.  
These small directional shifts m because ranking amplifies  
the most near the cutoff.  
Bias-corrected conformal interval separates shift  
from uncertainty.  
So we first recenter predictions using a group-level bias  
estimate from the training set, and then we  
calibrate interval widths using residual quantiles  
from a separate calibration set.  
These resulting intervals are both less  
shifted on average and calibrated to achieve a chosen  
coverage level.  
Then I showed you how to make a posit-style selection, which  
then changed the decision rule, but not the underlying model.  
So selecting candidates by the lower  
end of their calibrated interval prioritizes  
candidates who look stronger even under uncertainty.  
This can materially change who gets  
shortlisted compared to ranking by point predictions.  
If you want to check out the references  
that I used to build this recitation,  
I've included them down here.  
And they also give you more background information  
on fairness in hiring and how to use conformal intervals  
for different problems.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Recitation Summary  
\`\`\`  
Skip to main content  
Key Takeaways  
Prediction bias can be group dependent.  
Even when overall fit looks reasonable, the models can systematically overpredict for one gender and underpredict for the other.  
Bias-corrected conformal intervals allow us to include uncertainty in ranking.  
We calculate these intervals by first recentering predictions using a group-level bias estimate from the training set, followed by calibrating interval widths using residual quantiles from a separate calibration set. The resulting intervals are both less shifted on average and calibrated to achieve a certain “goodness of prediction” score, called coverage.  
Poset-style selection changes the decision rule, not the model.  
Poset-style selection of candidates means ranking candidates based on some partial order on their calibrated intervals. This prioritizes candidates who look strong even under uncertainty. Poset-style selection can materially change who gets shortlisted compared to ranking by point predictions.  
\`\`\`

Recitation 2: Finding a Portfolio of "Fair" Solutions in the Facility Location Problem  
\`\`\`  
Skip to main content  
Recitation Overview  
Welcome to Recitation 2: Finding a Portfolio of "Fair" Solutions in the Facility Location Problem, taught by Catherine Oellig, Visiting Student Researcher at Massachusetts Institute of Technology. This recitation emphasizes material presented in L2.7 Underspecified and Misaligned Objectives: Optimization Criteria, L3.10 Aligning Goals: Encoding Values in Objectives, L3.11 Aligning Goals: Navigating Competing Objectives, and L3.12 Aligning Goals: Competing Objectives in Resource Allocation. It is motivated by research done by Gupta, Moondra, and Singh (2025).

In Recitation 2, we study the facility location problem: how to place new facilities, here, pharmacies, to improve access in a setting with existing “medical deserts.” Using U.S. Census block-group data for Alabama, we quantify which communities lack adequate access and then search for placements that are not only effective, but also fair in how they distribute improvements.

A key lesson is that “good placement” is not purely a technical outcome of optimization—it is a values choice. If we add a fixed number of new facilities, should we prioritize efficiency (= maximizing total system-wide improvement in access) or equity (= protecting the worst-off groups, even if total gains are smaller)? This efficiency–equity tension is unavoidable whenever a single policy changes outcomes for different stakeholders in different ways.

Because there is rarely an agreement on a single, correct definition of fairness, we take a portfolio approach: we generate a small set of representative, high-quality solutions across different trade-off settings and compare their distributional impacts. This creates a structured basis for a stakeholder discussion.

In the course of this, we will look at and compare different optimization strategies.

The recitations focus on applying the theory from the lecture to a concrete case study. The experiments, visualizations, and much of the discussion will take place through an accompanying Jupyter notebook, which is intended to make the material more interactive and hands-on. We encourage you to open, download, and explore the notebook yourself, and to play around with the code and outputs as you work through the recitation.  
\`\`\`

R2.1 Setup  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now move on to recitation 2\.  
In this recitation, we will formulate a facility location  
problem as a mixed integer program.  
We will then start off by using a distance minimization  
objective and observe how the objective choice can create  
blind spots in our results.  
We will generate a Pareto frontier  
by varying the weight parameter between the L1 norm  
and the L-infinity norm.  
What that is, I will explain later.  
And we will then diagnose distributional effects  
by comparing group outcomes across the different solutions.  
We will then introduce a coverage space objective  
as a mitigation and repeat the same analysis,  
and then have a small policy discussion.  
By the end of this recitation, I hope  
that you are able to analyze and compare  
solutions at different points across the Pareto frontier,  
and discuss what this means for actual policy.  
The background for this recitation  
is that it builds on work by Gupta, Moondra, and Singh,  
who use US census data to identify  
medical deserts across states and then apply optimization  
to study where new health facilities could be placed.  
A key contribution of that line of work  
is not just producing one best plan,  
but constructing a portfolio of high-quality solutions  
that would present different societal priorities.  
A medical desert is a geographic area  
where residents lack adequate access to health services  
and supporting infrastructure, such as pharmacies, hospitals,  
and clinics.  
There is no single universal definition for medical deserts.  
They could be operationalized using travel distance or travel  
time, provider capacity, service availability, insurance  
acceptance, or any combination of these.  
Industry citation, we want to use a distance-based definition  
to keep the core ideas transparent and measurable.  
But this leads to the main problem.  
If we want to reduce medical deserts,  
we typically need to open new facilities.  
But good placement is not a purely technical question.  
It's a values question.  
Do we want to minimize the total system-wide burden  
so that the overall access improves as much as possible?  
Or do we want to protect the worse off groups,  
even if that reduces the total improvement we can achieve?  
This is a central tension between efficiency and equity,  
and it shows up whenever one decision affects  
stakeholders in different ways.  
In our setting, each demand group,  
which we will classify in ethnic groups, income groups, and urban  
versus rural groups, has an average access burden  
measured via travel distance.  
We consider two complementary objectives.  
The one objective will be capturing efficiency,  
so that means minimizing the total burden aggregated  
across groups.  
Intuitively, L1 rewards large overall improvements.  
So if we can reduce distances substantially for many groups,  
the objective improves, even if one group  
remains relatively worse off.  
This corresponds to maximizing total welfare.  
Equity, on the other hand, corresponds  
to the mathematical L-infinity objective,  
which corresponds to minimizing the burden  
of the worst off group.  
Intuitively, L-infinity is dominated by the maximum group  
burden.  
If any group has high average distance,  
that group defines objective value,  
so the optimizer is forced to address it.  
This corresponds to a no group left behind kind of lens.  
More generally, LP norms encode different value judgments  
about how we aggregate costs like travel distance  
across stakeholders.  
As the p increases, the model becomes  
increasingly sensitive to the high burden groups.  
That's why we choose L1 and L-infinity  
as the two polar opposites.  
To see how solutions change as we move from efficiency  
to equity, we will introduce a trade-off parameter  
that we call lambda.  
Conceptually, lambda controls how strongly we  
penalize inequity relative to overall burden.  
It lets us continuously shift from solutions  
that prioritize efficiency and total  
improvement toward solutions that prioritize equity  
and reduce the worse off group burden.  
Because there's rarely a consensus on the right notion  
of fairness, it is often more useful to generate  
a small set of representative, high-quality solutions  
across lambda values, called a portfolio of solutions,  
and then we can compare them.  
This creates a structured way to have a stakeholder conversation.  
Instead of debating abstracted principles,  
we can inspect concrete plans and  
their distributional impacts.  
So to see this, we will first minimize raw travel distances  
for block groups, and then we will  
see that this objective can be misaligned with medical desert  
definitions, depending on how we use it, and can systematically  
neglect some groups, especially urban groups.  
We will then present a second optimization approach  
by switching to a coverage objective that is directly  
tied to whether a block group is in a medical desert or not.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.2 Load and Understand the Data  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's start off by setting up our recitation.  
As in the last recitation, we will  
be using different Python libraries  
throughout this script.  
So if you do not have the following Python libraries,  
you first will have to install them using pip,  
as I did in this command line.  
You can do this by just running the cell.  
Importantly, we also need to include an optimizer.  
We will be using the SciPy optimizer  
from the library called Scientific Python, which  
you can also read up on, and this  
dictates which solver we use for our mixed integer  
linear program.  
Once you've set up all of these libraries,  
you will get the message that SEV is complete.  
Let's now load and understand the data.  
So for this recitation, we will be  
importing the data of Alabama.  
We then need to sometimes flip the distances from kilometers  
to miles, since the census data sometimes has kilometer values.  
If we print the number of census groups,  
we see that we have around 4,000 census block groups for Alabama.  
A block group is a small geographic unit used by the US  
Census Bureau, which typically contains roughly 600 to 3,000  
residents.  
It is designed to capture the neighborhoods  
at a granular level, while being large enough  
for statistical analysis.  
So we can first print the census data frame head  
and inspect the data that we have.  
We see that we have different kinds of block groups.  
We have geographical IDs.  
We know the population of the different block groups,  
and we see the demographic percentages,  
So how many of the people in this block group are white,  
how many are Black, how many are Asian.  
We also get different metrics on how close the nearest  
child care centers are, so this data set is very rich.  
We will then filter through demographic groups  
to simplify this recitation.  
So I want to look at 18 different groups,  
and I want to group the groups by either majority white,  
majority Black, or majority other, which will  
be any other demographic group.  
I then also want to group by income  
level, so medium, high, and low income levels.  
And we will look at different geographic locations,  
so we will discriminate between rural and urban neighborhoods.  
If we now output all of these block groups that we have found,  
we see that the biggest block group  
is the white, medium, rural block group, which  
we have 668 groups of.  
So 17% of all block groups are white,  
medium, rural block groups in Alabama.  
We then see that the fourth highest block group  
is the Black, low, urban block group, which makes up  
11% of all block groups.  
Next, I will compute a desert flag.  
So as I talked about earlier in the introduction,  
we want to look at medical deserts in this data sets,  
and we will simplify this definition of a medical desert  
by looking at the travel distance of populations  
within this block group.  
So we will count a block group as a medical desert  
if it's in a rural area, if people  
have to travel more than five miles to reach a pharmacy,  
and we will call a urban area a medical desert,  
if people have to travel more than one mile to a pharmacy,  
since people often go by foot in cities.  
We will then also cut off by income level,  
so if more than 25% of a block group's population  
is below the poverty line, then we  
will include them in the medical desert subset,  
because otherwise we can assume that maybe they have a car  
and better access to health care than others.  
So if we then look at this desert rate  
within the different groups, so for the desert rate,  
we're asking within a demographic group what fraction  
lives in a desert, and we can also output desert distribution.  
So of all deserts what fraction belongs to a group.  
And we see that 50% of all Black, low, urban block groups  
live in medical deserts.  
Of the white, low-income, rural block group,  
40% live in desert in medical deserts.  
This means that there is a distributional shift,  
so between the percentage of total block groups  
that these groups make up and the percentage  
of block groups that they make up in the desert data set  
is a big shift.  
So for the Black, low-income, urban group,  
they only were 11% of all the block groups,  
but they are 40% of all the desert groups.  
So this motivates looking at group-wise optimization moving  
forward.  
We can also visualize this in a chart.  
So here we see our different block groups  
by race, income, and location in Alabama,  
and we see that these big white, high-income,  
and medium-income groups make up the largest distribution,  
and here's the Black, low-income, urban group.  
And then if we look at the desert composition,  
as we saw before in the data set output,  
that the Black, low, urban proportion of medical deserts  
is the largest.  
So now the whole data set has around 4,000 demand points,  
as we saw, and for the sake of this recitation, however,  
I just want to reduce the data set to all of the groups that  
are in medical deserts.  
So we will flag all of these groups  
here and ignore the other groups,  
since we need to help those people the most.  
Then we can pre-compute a distance matrix.  
So since later on we will be using a mathematical solver,  
we need to give some kind of input  
on how far away each block group on average is to a pharmacy.  
This takes a while to compute, so it's easier  
to store this information, since we  
need to access this information again and again in a distance  
matrix.  
This is a very standard approach for any solver.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.3 Mathematical Formulation  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We can then move on to the mathematical formulation  
of this problem.  
So we have different sets.  
One set contains the demand points.  
Another contains all the candidate facility locations.  
Then we have our demographic groups  
and the demand points within the group.  
We will look at different parameters, so the distance  
from a demand point J, a group, and to a nearest existing  
pharmacy, and the existence--  
the distance between a candidate facility site  
and different demand points.  
We'll then define the number of facilities that we want to open.  
We then also define decision variables,  
which we set to 1 if we open a facility at location I,  
and if a demand point is served, then we can also set it to 1\.  
We then add different mathematical constraints.  
So we want to open exactly K facilities, for example,  
10 or 25\.  
And we only assign demand points to open facilities.  
There's no reason to assign a demand point to a facility  
that we're not planning on opening.  
And we assign most one facility per demand point  
to help as much people as possible.  
We then calculate the distance and try  
to minimize the group average distance in the one objective  
for the L1 norm.  
So we look at all of the average distances  
over the separate groups.  
And in the L infinity norm, we look at the maximum distance  
for each group.  
Our objective then becomes this trade-off between the L infinity  
norm and minimization and the L1 infinity-- the L1 minimization.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.4 Implementation the Optimization  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: I hear it and implemented the optimization,  
which you should feel free to click through and understand.  
It's just a mathematical programming formulation  
of exactly these constraints that we just discussed.  
So we can now output the existing pharmacy distances.  
So the mean is around 4 miles whereas the median  
is around 1.8 miles.  
This is because there's more people probably living  
in urban areas.  
And the maximum traveling distance is 28 miles.  
We can now also look at these means and medians  
per demographic block group.  
So we see that on average, the black low-income rule block  
group has to travel most, followed by the rural groups.  
And then also, in the urban and medical \[INAUDIBLE\] definition,  
the black low-income urban groups  
are the most disadvantaged.  
So now we can test the optimization.  
And I set k to 25\.  
So we want to open 25 facilities.  
And I'll just set the test lambda to 0.5.  
So that means that we have a middle trade-off between the L1  
and the L infinity norm.  
This now outputs an average group distance for us.  
So the white low rural group has been reduced  
to 6.3 miles in average.  
So if we compare this to the previous average distance  
that they had to travel-- was 11.7.  
So this is a substantial reduction.  
We see similar reductions for all of the groups.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.5 Generate the Pareto Frontier  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We can then generate a Pareto frontier.  
So we do this by sweeping lambda from 0, so pure equity,  
to 1, which is a pure efficiency objective,  
and then collect the corresponding solutions.  
We can then compare these solutions  
and see what it does to different groups, which groups  
are disadvantaged, which groups are helped more  
in different solutions.  
So we sweep these values, and we can visualize the Pareto  
frontier, which is this swoop.  
For each value of lambda, you here  
see these two summary metrics.  
So on the one hand, the L1, the sum of the group burns  
and which then represent the systemwide efficiency, and L  
infinity, so the maximum group burn,  
which represents the worst-off group performance.  
So here, for lambda 0, where we are in the pure equity case,  
we see that we have the largest L1 sum of group distances,  
whereas here, for lambda equal to 1,  
we have the smallest L1 sum of group distances.  
At the same time, L infinity here is the largest,  
and here, it is the smallest, which  
visualizes this trade-off that we  
see between the different solutions.  
To understand the Pareto frontier plot,  
you have to see that these are all of the optimal solutions.  
So any solution that would be underneath this Pareto frontier  
would be like a free lunch because you can improve the L  
infinity norm, and you can improve the L1 norm  
by finding a better solution.  
So this is the boundary of the optimal solutions  
that we can find.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.6 Compare Group Distances Across Solutions  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We can then compare our group distances  
across solutions by building a table of distances  
for each lambda.  
So here, we see the different lambdas.  
And here, we see the averages for  
the different demographic block groups that we have created.  
Let's visualize this.  
So we see here how the travel distances change from lambda 0  
to lambda 1\.  
So here, in the equity case, we see  
that the solver forces the worse-off groups  
to be close to each other.  
So we try to minimize the worse-off groups  
as much as possible, which ends up being  
this l-infinity shrinkage here.  
So the worst-off group here is less bad off  
than it would be than it is over here.  
Then moving from lambda equal to 0 to lambda equal to 1,  
we see how this shift affects different groups.  
So as before, the Black low-income rural group  
and the white low-income rural group  
were similarly in similar positions  
and had similar group distances.  
If we then shift over to an efficiency objective,  
we see that the white low-income rural group  
sees more of a distance impact than the Black  
low-income rural group.  
This can be because there is just easier quick wins  
for the Black low-rural group, or there's maybe  
some groups that have an extremely high average distance.  
So already, by helping those, we can  
lower the average a lot easier than  
in the white low-income rural group.  
But we can see how this impacts different groups  
in different ways, shifting from one objective to the other.  
We also see that the other race low-income rural group benefits  
very strongly from the efficiency criteria.  
And this is because we do a group-wise optimization.  
Since we divide by each group, that  
means that for a small group, it's relatively easy  
to get efficiency gains.  
And this impacts the minimization  
of the objective in a bigger way than for a bigger block group.  
For a bigger block group, you have  
to improve the distances for much more block groups  
for there to be an impact.  
So this is why the rural here sees the most gains.  
We can also look at the change in medical deserts.  
So we use the same medical desert definition as previously.  
We want to only consider groups that  
have a rural threshold of 5 miles  
and an urban threshold of 1 mile.  
And the poverty threshold should be that more than 25%  
of the people living in this block group  
are below the poverty line.  
So let's look at this.  
We see that the baseline was here  
at about 583 medical deserts.  
That's how many medical deserts we had to begin with.  
And we see that for lambda equal to 1,  
so for the equity objective, the number of medical deserts  
has dropped to 547, whereas all the way over here,  
for the efficiency objective, the overall number  
of medical deserts has dropped to 548\.  
So relatively similar numbers of medical deserts-- but let's  
see if that affects different block groups.  
So we can zoom in on a solution portfolio  
by choosing some lambdas that we want to look at.  
So for example, I chose lambda equal to 0, so the equity only,  
and lambda equal to 1, efficiency only, and then  
a couple of lambdas in between.  
And if we first look at the group distances  
for these different solutions, we  
can see that in the beginning, as lambda goes towards 1,  
the other race low rural block group sees more of a benefit  
since they are weighted much more  
into the objective function.  
We also see that the white low-income rural group  
has a slight disadvantage of the efficiency in the efficiency  
objective.  
If we then look at the medical desert reductions per block  
group, we see that the biggest reduction  
for all of the medical deserts happen in the rural areas.  
So the black low-income rural group  
sees the biggest reduction in medical deserts in the equity  
objective.  
If we move over to efficiency, again, because  
of the weighting of the different groups,  
we see a big gain in the other race of low-income rural group  
because of the way we formulated the objective  
and because, again, it's a small group,  
so small improvements make a big improvement  
in the objective function.  
So we just have a lot of bang for buck.  
Now, this motivates asking ourselves,  
was distance the right thing to minimize?  
So maybe we minimize average distance.  
But maybe that meant that we minimize  
the distance for groups that already weren't off better.  
So the average was very near to no longer being  
a medical desert.  
And we only shifted this distance a little bit  
beneath the threshold, but maybe we didn't help groups  
as much that were further away.  
Or maybe for groups where the average distance was very far  
away, we brought it closer to the threshold  
but not necessarily beneath the threshold.  
So this distance formulation might not actually  
be doing what we want if our goal is to actually just reduce  
medical deserts.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.7 Fair Facility Location with Coverage  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So this kind of motivates  
the second part of this recitation,  
where instead of looking at a optimization scheme  
that minimizes the distances, we instead maximize the coverage.  
So what does that mean?  
We can define coverage of a group  
by saying that a group is covered if they are not  
a medical desert.  
So we can consider a block group as served  
if it lies within a prescribed distance of any pharmacy,  
and this naturally leads to a coverage objective.  
So we maximize the number of block groups  
that are not medical deserts after opening new facilities.  
So again, we look at different demand locations  
and different candidate facility sites.  
And we, again, need the distances.  
But the most important difference  
here is that each demand point has this threshold  
that we calculate.  
So as we try to minimize the distances,  
we always check if the new distance falls  
beneath this new threshold.  
We have the same decision variables as previously,  
so opening a new facility at site I,  
and then introduce this new decision  
variable that decides if a demand point is covered or not.  
So if it fits the medical desert definition or not.  
Our constraints are then similar to above,  
that we have a facility budget, so we can't open more than,  
say, 25 facilities, and we have these coverage  
limiting constraints.  
So when does a group count as covered?  
Our objective is then maximizing coverage,  
which is equivalent to minimizing the deserts.  
If we now want to bring the L1 norm and the L infinity norm  
into coverage, we need to switch from minimizing distances  
to maximizing coverage.  
And by doing that, we can say, OK,  
so L1 efficiency then becomes optimizing the average group  
outcome.  
So in the coverage setting, L1 means  
you care about the overall performance of average  
across groups.  
We then weigh groups equally and the mean  
is the desert rate, so how many of our block groups  
within this ethnic group--  
this ethnic and demographic group, are medical deserts.  
And then we try to minimize the average desert  
rate across the groups.  
The infinity case then is equal to optimizing  
for equity or robustness.  
So we tried to optimize the worst group outcome.  
So overall the optimization points and overall  
the facilities that we allocate, we  
try to minimize the group that's worst off.  
This means that we care about the worst served group the most  
and we're trying to reduce the maximum desert  
rate of any block--  
of any demographic group.  
We can now do the same Pareto sweep as we did previously  
for the distance optimization, and we again  
look at setting up 25 new facilities.  
Let's now visualize the Pareto frontier.  
So we see a very different Pareto frontier line  
than before.  
We also see that here, again, these  
are the groups that have the worst L1 norm  
and these are the solutions where  
we have the smallest L1 norm, but therefore,  
the highest L infinity norm.  
So the highest maximum group distance.  
We can now use this to choose some groups to look  
at in particular.  
So later on, let's maybe look again at lambda equal to 0,  
lambda equal to 0.2, because this  
seems to be a medium trade-off point,  
and corresponds to the knee of the Pareto frontier.  
And then let's also look at lambda equal to 0  
and maybe lambda equal to 0.5.  
But first, let's look at the change in medical deserts.  
So we can now plot the overall amount of medical deserts.  
And for reference, this is our initial distance reduction  
optimization.  
And this is now the coverage reduction optimization.  
So we have reduced the number of medical deserts  
to 505 medical deserts rather than 583 medical deserts  
by just setting up 25 new pharmacy facilities.  
For the infinity norm, this corresponds  
to 509 medical deserts.  
So we see a substantial reduction in medical deserts  
in using this coverage optimization.  
If we then zoom into our solution portfolio,  
we can also look at which demographic groups does  
this benefit and which demographic groups might  
this harm more than the other solution.  
We see that for lambda equal to 0, so in the equity case,  
there's the largest reduction for the Black low income  
urban group.  
If we then shift over to lambda equal to 1,  
so the efficiency objective, again, we  
see that the other low rural group is--  
but if it's the most, again, because of the way  
we weight the groups.  
But we also see that the white low urban group  
benefits from this too.  
So we can now compare these two desert count ratios  
between the two optimizations.  
So when we look at the coverage optimization  
overall, as we saw previously, there's  
a reduction overall in total count of medical deserts.  
We also see that by formulating this with the coverage function,  
so considering a group covered for different thresholds  
depending on the rural and on the urban location  
of demographic block groups, this kind of shifts  
the burden of medical deserts.  
Before, we saw that there was only  
a reduction for rural groups because we were just  
minimizing overall distances.  
Now that we're maximizing coverage,  
we also see that we're benefiting urban groups just as  
much as rural groups on average.  
So overall, we see that when trying to find solutions  
to problems like this, it's not only  
about mathematical implementation.  
It also comes down to what stakeholders  
define as their values for improving access.  
Do you want to improve the distance traveled  
on average by groups?  
Would you like to improve the overall medical desert rate?  
Do you want to make sure that the worse off group is the least  
bad off, or do you want to make sure that on average we've  
minimized distances?  
These are all discussions to be had and depend  
on the values of the people sitting at the table making  
this decision.  
But this can give you a good framework on how  
to discuss different solutions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R2.8 Key Takeaways  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So the key takeaways from this recitation  
are, on the one hand, scalarization.  
So you can convert a multi-objective problem  
into a single objective problem using this lambda.  
And the lambda can be used to trade off different objectives,  
therefore generating a portfolio of different solutions  
that you can compare.  
A Pareto frontier then shows all non-dominated solutions  
versus the dominated solutions.  
The dominated solutions are the ones  
that you can't improve without worsening another.  
So that was the Pareto frontier line.  
Then we also saw that the trade-off is real.  
So pure efficiency, lambda equal to 1,  
leaves some groups behind while lambda equal to 0  
can sacrifice total welfare.  
This is what we saw in the different radar charts.  
And then we also saw and stressed in the end  
that it all comes down to a policy choice.  
So the best solution depends on values and priorities.  
And the optimization allows you to see different options.  
But at the end of the day, the humans  
have to make their decision.  
If you found this interesting to follow,  
I can recommend looking into the paper  
by Gupta, Moondra, and Singh on provably small portfolios  
for multi-objective optimization, which  
is the paper that inspired this recitation.  
I can also recommend checking out the interactive tool built  
during this research that kind of lets  
you do the same analysis for different definitions  
of medical deserts.  
So in this case, we looked at pharmacies,  
but you can also include more sites, such as hospitals  
or different care facilities.  
You can look at different states.  
And it's just interesting to see how different objectives trade  
off the location of new facilities.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Recitation Summary  
\`\`\`  
Skip to main content  
Key Takeaways  
Efficiency–equity trade-offs can be formalized using L1 versus L-infinity norms in the optimization objective. Different norms encode different value metrics.  
The Pareto frontier identifies non-dominated solutions. It shows where trade-offs are unavoidable and where some solutions are simply worse than others.  
Objective choice matters. We saw how minimizing raw distance can be misaligned with threshold-based policy goals and can produce systematic neglect of certain contexts, such as urban deserts in this case. This emphasizes the importance of a well-aligned objective.  
Optimization can produce options. Governance determines which trade-offs are acceptable and which definition of “fairness” and “improvements” should drive the objective.  
\`\`\`

Assignments  
\`\`\`  
Skip to main content  
Overview  
Welcome to Assignment 1\! In this assignment, you will use what you have learned in the course of the module to act as a consultant analyzing a city’s AI-based triage system for scheduling housing inspections. Using a short scenario, you will 

Identify where bias enters the pipeline and what bias types are most relevant,  
Explain how those biases can translate into concrete real-world harms,  
Define how the decision system could be redesigned to reduce those harms.  
Lectures covered by this assignment

Lecture 3.1 — Detecting and Diagnosing the Problems: Implementing Detection in our Data-Model Decision Pipeline  
Lecture 3.7— Handling Noise: Correcting Labels in Biased Data Sets  
Lecture 3.9 — Handling Noise: Data and Model Uncertainty  
Lecture 3.10 — Aligning Goals: Encoding Values in Objectives  
Lecture 3.12 — Aligning Goals: Competing Objectives in Resource Allocation  
Lecture 3.13 — Other Strategies for Building Ethical Systems  
Lecture 2.7 — Underspecified and Misaligned Objectives: Optimization Criteria

Skip to main content  
A city uses an AI triage tool to schedule housing inspections. It is trained on the last five years of inspection outcomes to predict “risk of serious code violations,” and the city inspects the highest-risk buildings next month.

You learn two facts:

Inspectors historically focused more on neighborhoods with higher complaint volume and stronger advocacy, so those areas were inspected more often.  
“Serious violation” labels come from inspector write-ups, and inspector teams apply different thresholds for what they record as “serious.”  
Keeping this in mind, answer the following multiple-choice questions:

Question 1  
0.0/1.0 point (graded)  
Which answer best identifies the most relevant bias types and where they enter the pipeline?

Uneven inspection coverage creates selection bias, and inconsistent “serious violation” write-ups create label bias; both enter during data collection and labeling.

Complaint volume is a biased proxy, so the main problem enters through feature design when complaints are used as an input.

Neighborhoods differ in housing conditions, so the main problem enters through model choice when one citywide model is used for all areas.

Inspection capacity is limited, so the main problem enters at deployment when the city must prioritize some buildings over others.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
Why can a strong validation score still be misleading in this setting?

The model predicts violations rather than repairs, so good performance may not match city goals.

The model is trained on too few years of data, so good performance may not hold in future years.

The model uses neighborhood information, so good performance may just reflect overfitting to location.

The model is only tested on buildings the city chose to inspect, so good performance can still reflect biased observation.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Which harm is most directly caused by the rule “inspect the highest-risk buildings next month”?

Inspectors begin to rely less on their own judgment, so reports become less detailed over time.

Frequently inspected neighborhoods become safer, so the model starts ignoring truly risky buildings elsewhere.

Frequently inspected neighborhoods generate more recorded violations, so they keep being prioritized over time.

Residents in low-priority areas stop filing complaints, so the city loses an important input signal.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Which change most directly weakens the feedback loop and improves representativeness?

Reserve some inspections for random or stratified coverage, and use model scores for the rest.

Remove complaint-related features, and keep inspections fully score-based.

Retrain the model more often, and keep the same inspection rule.

Add more building features, and keep inspections fully score-based.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Which intervention best addresses inconsistent “serious violation” labels across inspector teams?

Add more building covariates so the model can statistically “smooth” label differences.

Use a shared severity rubric and regularly check agreement across teams.

Reweight neighborhoods so low-complaint areas count more in training.

Replace the supervised model with an unsupervised anomaly score.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Assignment Summary  
Skip to main content  
Summary  
In this case study, the core issue was biased data generation that resulted in negative feedback loops.

The training data reflected where inspectors went and how they labeled outcomes, so the model learned patterns that partly encode historic inspection priorities and inconsistent severity thresholds. When deployed with an “inspect top-risk” rule, the system can reinforce itself: areas that were historically inspected more will continue to generate more recorded violations, staying “high risk,” while under-inspected areas remain less visible and are deprioritized. This leads to asymmetric burden.

The strongest redesigns, therefore

Force representative measurement via randomized/stratified inspections,  
Improve label governance via standardized rubrics and inter-rater reliability checks.  
\`\`\`

Skip to main content  
Overview  
Welcome to Assignment 2\! In this assignment, you will use what you have learned in this module to solve a case study. You will act as a consultant by advising a city on where to place two new urgent-care clinics using an optimization-based planning tool. 

To complete this task, you will need to 

Define a fitting objective function,  
Characterize trade-offs between competing objectives,  
Propose guardrails to align decision-making with efficiency and equity goals.  
Lectures covered by this assignment

Lecture 3.10 — Aligning Goals: Encoding Values in Objectives  
Lecture 3.11— Aligning Goals: Navigating Competing Objectives  
Lecture 3.12— Aligning Goals: Competing Objectives in Resource Allocation  
Lecture 2.7 — Underspecified and Misaligned Objectives: Optimization Criteria

Skip to main content  
You are advising a city on where to place two new urgent-care clinics. The city is considering an optimization-based approach to choose clinic locations, but leadership is concerned about both efficiency (overall access) and equity (avoiding very poor access for any one group). Your task is to select an objective function that best matches a stated equity priority and to reason through how changing the objective shifts outcomes across neighborhoods.

The city has three areas:

Downtown: high population density, good public transit, higher average income  
Northside: moderate population, many elderly residents, limited transit  
Riverside: lower population density, lower average income, longer travel times today  
The current plan is to choose clinic locations by optimizing one objective function. City leadership states the priority as: “Reduce the risk that any one group faces very poor access.”

Please answer the following questions, staying in the above described scenario.

Question 1  
0.0/1.0 point (graded)  
Which objective best matches: “Reduce the risk that any one group faces very poor access”?

Minimize operating cost to free resources for other equity programs.

Maximize expected utilization to place clinics where demand is highest.

 Minimize average travel time to maximize total access gains.

Minimize the maximum travel time to limit worst-case access outcomes.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
If the city switches from minimizing maximum travel time to minimizing average travel time, what is most likely?

Riverside improves because any clinic increases total access, especially where baseline travel is long.

Northside improves most because limited transit makes marginal gains larger than Downtown’s.

Downtown is more likely to benefit while Riverside is more likely to lose relative to minimax, because dense areas dominate average improvements.

Outcomes converge across neighborhoods because two clinics eliminate most long-travel outliers.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Which policy best operationalizes the equity priority while preserving efficiency trade-offs?

Require one clinic in Riverside regardless of travel-time impacts.

Impose a maximum travel-time cap per neighborhood (or subgroup), then minimize average travel time subject to that cap.

Optimize average travel time, then run an equity audit and adjust only if disparities are extreme.

Use utilization maximization and publish results to ensure accountability.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
If the city uses “minimize average travel time \+ λ × inequity penalty,” what does increasing λ typically do?

Makes the solution random because the penalty dominates the objective.

Improves demand forecasting accuracy, indirectly improving equity.

Forces clinics away from Downtown regardless of access outcomes.

Places more weight on reducing disparities/worst-served outcomes, often trading off some average efficiency.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
This assignment exemplifies encoding values and highlights the trade-off between competing equity objectives.

If the city minimizes average travel time, which seems like a good goal, the solution will place Downtown at an advantage. A high density neighbourhood with strong transit allows the optimizer to reduce average travel time a lot by placing clinics downtown, even though many people in this area already have relatively good baseline access. When deployed, this could reinforce itself politically and operationally: resources flow to places where improvements are easily seen in aggregate metrics, while Riverside (and potentially mobility-constrained residents in Northside) remains less protected from very poor access. The result is asymmetric burden: some groups face persistently long travel times even though the system appears “efficient” on average.

Instead, the city should implement policies that

Explicitly protect the worst-served by using a minimax objective, minimizing maximum travel time or by imposing travel-time caps per neighborhood/subgroup,  
Preserve efficiency within guardrails by optimizing average access only after minimum-access floors are met (or by using a weighted objective with λ as a transparent trade-off knob plus ongoing monitoring of worst-case access).  
\`\`\`

Skip to main content  
Overview  
Welcome to Assignment 3\! In this assignment, you will analyze a bank’s AI-supported loan approval system and evaluate whether its offline performance results can actually be trusted. Using a short scenario, you will

Identify the key blind spot that makes historical evaluation potentially misleading,  
Explain how selective outcome observation and inconsistent default labels can translate into concrete harms,  
Assess why policy changes can make past metrics unreliable for future deployment, and  
Propose a redesign of the decision system that improves validity, reduces compounding errors, and strengthens accountability.  
Lectures covered by this assignment

Lecture 3.1 — Detecting and Diagnosing Problems: Implementing Detection in our Data-Model Decision Pipeline  
Lecture 3.7 — Handling Noise: Correcting Labels in Biased Data Sets  
Lecture 3.9 — Handling Noise: Data and Model Uncertainty  
Lecture 3.10 — Aligning Goals: Encoding Values in Objectives

Skip to main content  
In this assignment, you will analyze a bank’s AI supported loan approval system and assess whether its evaluation results can be trusted. Using a short scenario, you will (1) identify the most important blind spot that makes offline performance metrics potentially misleading, and (2) explain how noisy labels and policy changes can translate into concrete harms. You will then propose a decision system change that improves validity, reduces compounding errors, and increases accountability.

A bank uses a model trained on the last four years of personal loan outcomes to predict “probability of default”. The bank plans to use the score next quarter to decide approvals and set interest rates.

You learn two facts:

Historical approvals were not uniform: applicants from certain neighborhoods were rejected more often due to branch coverage and documentation gaps. As a result, default outcomes are observed mainly for people who were approved in the past.  
The “default” label comes from collections workflows. Different regional teams apply different thresholds for when an account is recorded as default (for example, restructuring vs charge off timing), and these differences are correlated with borrower location.  
Use the provided information to answer the following questions:

Question 1  
0.0/1.0 point (graded)  
Which answer best identifies the most relevant issues and where they enter the pipeline?

High-dimensional features cause overfitting; the main remedy is regularization and stronger cross-validation.

Defaults are rare, so class imbalance is the dominant issue; the main remedy is reweighting the loss.

Outcomes are observed mainly for historically approved applicants and defaults are inconsistently defined across regions; the issues arise in data collection

Neighborhood features act as proxies; the issue arises in feature engineering and is mainly solved by removing location signals.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
Why is this evaluation problem especially serious if the bank changes its approval policy next quarter?

Because the model may now be used on applicants whose outcomes were rarely observed under the old approval policy, so past validation may not say much about performance on the newly approved group.

Because any change in approval policy automatically changes the statistical relationship between features and repayment, so historical validation results can no longer be used at all.

Because next quarter’s applicants may differ somewhat from past applicants in income, employment, or debt levels, so the bank should assume that time variation is the main reason offline metrics may fail.

Because regional differences in collections workflows mainly matter once the bank starts adjusting interest rates with the model, since pricing decisions create the label inconsistency problem.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
If some regions record “default” earlier or more strictly than others, what harm is most likely?

Similar borrowers across all regions receive slightly worse pricing because the model becomes more conservative overall when labels are inconsistent.

Borrowers in lenient-label regions receive worse pricing and more denials because the model treats their fewer recorded defaults as hidden risk.

Borrowers in stricter-label regions receive higher predicted risk and worse pricing or denial outcomes even when repayment behavior is similar.

Borrowers in stricter-label regions mainly face less accurate scores, but not systematically worse loan terms, because the noise averages out in a national model.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Which mitigation pair most directly addresses (i) selective outcome gaps and (ii) inconsistent default definitions?

Stratified auditing approvals \+ standardized default rubric across regions

Counterfactual/off-policy evaluation \+ ongoing monitoring with triggers

Uncertainty-aware deferral \+ appeals/recourse process

Reweighting for imbalance \+ stronger regularization  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Which threshold policy best reduces harm when model confidence is uneven and stakes are high?

Use a single approval cutoff for all applicants, but require manual review for the highest-risk cases so denials with the largest expected losses receive additional scrutiny before a final decision.

Adjust approval cutoffs by region so that decisions better reflect local repayment patterns and operational differences, while allowing the bank to maintain stable approval volumes across branches.

Auto-approve and auto-deny only at high-confidence extremes, and send applicants in the uncertain middle range to a second-look review with an opportunity to provide missing documentation or context.

Use a single bank-wide median score threshold for approvals and denials, since a fixed central cutoff is easier to explain, easier to monitor, and avoids case-by-case discretion in borderline cases.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 6  
0.0/1.0 point (graded)  
Which monitoring plan best matches the scenario’s risks?

Monitor overall AUC monthly; if it stays high, the system is safe.

Monitor profit and default rate; if both improve, the system is justified.

Monitor training loss and feature importance drift; if stable, deployment is safe.

Monitor approvals, APRs, and stability/calibration proxies by neighborhood/region with predefined triggers to pause/rollback on shifts.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Assignment Summary  
In this case study, the central problem is that the bank’s historical data does not cleanly represent the population on which the model will be used.

Default outcomes are observed mainly among people who were previously approved, so the model is evaluated on a selectively observed sample rather than the full applicant population. That means strong offline metrics may reflect past approval patterns and share/perpetuate past bias. On top of that, the target label itself is noisy: different regional teams use different default thresholds, so the model may learn regional workflow differences rather than genuine default risk.

These issues can translate into concrete harms: Applicants from under-observed neighborhoods may be scored using patterns that were never properly validated for people like them, and at the same time, borrowers in stricter-label regions may be assigned higher predicted risk, denied credit more often, or charged worse interest rates even when their repayment behavior is similar. Once such scores are fed into approvals and pricing, the system can compound past inequities and make them look data-driven.

The strongest redesigns therefore do three things:

Address selective outcome gaps through auditing, uncertainty-aware review, and cautious deployment where coverage is weak,  
Improve label governance by standardizing the default definition across regions and checking consistency in how labels are assigned, and  
Add monitoring and intervention rules so the bank can track approval rates, APRs, and calibration stability across neighborhoods and regions, with clear triggers for pause, rollback, or human second-look review.  
\`\`\`

Module Summary  
\`\`\`  
Wrap Up  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Finally, let's review  
and wrap up our discussion on ethical AI  
for decisions in today's world.  
I believe that ethical AI is, in fact, a societal need.  
AI is all around us.  
We see it in recommendations, transportation, power systems,  
education, hygiene, health care, et cetera.  
And these applications are going to continue to grow.  
We have to build systems that ensure  
that we don't compound poverty, we don't compound disparities.  
We are able to get ahead of the unintended consequences.  
We talked a lot about various examples from supply chains,  
from chatbots with misaligned objectives, with data errors,  
and impact on outcomes.  
We talked about various axes of decision  
making on how to build responsible AI.  
And there are many priorities, like reliability, transparency,  
fairness, robustness.  
We really have to think from an organizational perspective  
and make a conscious choice on which priorities  
we want to emphasize in the design of our systems.  
There's various ways of thinking about responsible AI  
and ethical design, be it from an ethics  
perspective, a technological perspective,  
a legal perspective.  
There are many issues that we have to think about  
in an application context.  
We discussed various causes of unintended consequences  
in decisions, going from noisy and imperfect data  
to the interplay of optimization and AI  
and underspecified and misaligned  
objectives that don't reflect organizational values.  
We then spoke about strategies for building ethical AI,  
from detecting and diagnosing problems.  
We talked about the pipeline that has to have a careful look  
and evaluate whether we are injecting bias  
at different places and try to build conscious models that  
are well-validated before deployment.  
We talked about various ways of handling noisy errors  
and missing data.  
Specifically, ways that incorporate domain  
knowledge and can build much better and fairer models.  
We further talked about handling model uncertainty through better  
calibration and understanding that AI error is contextual.  
Finally, we spoke about aligning optimization and AI,  
changing model training, using regularization, and using  
AI to help us navigate a broad set of potential models  
and solutions using portfolios.  
Overall, in order to build ethical AI,  
I believe it has to be a collective decision that we need  
to consciously reach for after a deeper  
dive into various applications.  
It's not a one size fits all, and different application  
contexts require different perspectives.  
We need lawyers on the table.  
We need statisticians, analytics experts, AI and ML experts,  
and social scientists, to name a few,  
to point out to different mechanisms, different places  
where these systems interconnect and interface with each other.  
I believe that the future of AI is proactive.  
With intentional human-AI collaboration,  
we really can get ahead of the ethical challenges  
and build societal systems that are for everyone.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Module Summary  
In this module, we analyzed Ethical AI for decision-making along a data–model–decision pipeline. We started with examples on how AI is already shaping real outcomes around us, across hiring, transportation, energy access, education, and healthcare. We discussed recent news headlines, motivating responsible algorithmic decision-making as a practical and societal need.

A central theme was that even well-intended systems can produce disparate impact when they learn from imperfect data and operationalize decisions through automated rules and optimization. We then discussed what it means to evaluate and implement AI responsibly.

Key Takeaways  
Unintended harms can have systematic causes.  
Noisy and Imperfect Data: As data can be missing or incomplete, we often only have proxy features, as the “true” underlying variables are often not directly observable. Proxy features can also encode bias and noise, which can disproportionately impact some groups, as we saw in Recitation 1\.  
Interplay of Optimization and AI: Predictive models and optimization layers interact in complex, hard-to-anticipate ways. Small prediction errors can be amplified through this interplay.  
Objectives can be underspecified or misaligned, as values are often hard to translate into measurable AI objectives, as we saw in Recitation 2\.  
We can introduce fairness through optimization design. One can encode values through regularization terms, explicit fairness constraints, or multi-objective formulations. Different formulations implement different ethical values, so the choice of system objectives is a governance decision, not a purely technical one.  
Solution portfolios can help visualize ethical trade-offs and guide decision-makers through different “fairness” notions.  
We need to account for Feedback loops. Deployed systems can change behavior and impact data over time, which can amplify disparities or degrade performance, especially for vulnerable communities. We need to constrain the system, so that it does not multiply these disparities over time.  
We need humans in the loop: Many reliable decision systems treat model outputs as decision support, and combine automated scale with human judgement, domain expertise, and escalation paths. This means  
Uncertainty should have a direct modeling impact. Calibration, prediction intervals, and uncertainty scores need to trigger review actions and incorporate meaningfully in decision-pipelines.  
Embedding domain expertise and data relationships can mitigate uncertainty. Subject-matter knowledge can help inform how to mitigate noise in data, which proxies make sense and how uncertainty in data can be factored into decisions.  
Congratulations on completing this module. You now have a conceptual and technical foundation for building, auditing, and improving algorithmic decision pipelines in ways that better align system behavior with ethics, accountability, and stakeholder values.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.

