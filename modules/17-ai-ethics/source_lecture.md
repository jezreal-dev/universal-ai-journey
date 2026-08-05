AI and Ethics  
\`\`\`  
Skip to main content  
Module Overview  
Welcome to AI and Ethics\! In this module, we explore the ethical challenges that arise as artificial intelligence systems are increasingly used to make decisions and generate content in real-world settings. Across the three lectures, we examine how AI systems can introduce bias, how fairness can be defined and measured, and how to ensure that AI systems behave in ways that align with human values.

We begin by introducing the broad landscape of AI ethics, with a focus on predictive AI systems used in domains such as healthcare, hiring, and criminal justice. We examine how bias can arise from historical data and feedback loops, and how different definitions of fairness attempt to address these issues. We then study how fairness can be formalized through statistical criteria, and why these definitions often conflict with one another, making trade-offs unavoidable.

Finally, we turn to the alignment problem, which extends beyond predictive models to generative AI and autonomous systems. We explore why simple rule-based approaches fail, how modern techniques such as reinforcement learning with human feedback attempt to align models with human preferences, and why disagreement over values makes alignment fundamentally challenging. We also introduce democratic approaches to aggregating preferences and their limitations.

Learning Goals  
By the end of this module, learners will be able to:

Understand the range of ethical issues introduced by AI systems across different applications  
Identify how bias can arise in predictive AI systems and affect decision-making  
Compare different definitions of fairness and analyze their trade-offs  
Explain why fairness criteria are often incompatible in practice  
Define the AI alignment problem and its importance for modern AI systems  
Describe techniques for aligning AI systems with human preferences  
Evaluate the challenges of aggregating conflicting human values in alignment  
\`\`\`

L1.1 Introduction  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: AI is transforming the economy and society  
more broadly.  
Some say it'll be more transformative  
than the internet.  
It might even be akin to a new Industrial Revolution.  
So it's important that AI be developed and deployed  
in positive, ethical ways.  
The ethical concerns raised by AI are wide-ranging.  
AI ethics is not one thing, but many.  
The development of AI requires substantial labor as well as  
environmental resources like energy and water, which raise  
concerns about exploitation.  
AI is also deployed in many different contexts,  
from chatbots to coding agents to self-driving cars  
to medical diagnosis, and many more.  
And each of these contexts raises  
its own distinctive ethical issues.  
In this lecture, we'll begin by distinguishing various different  
ethical issues that arise with AI.  
Then we'll focus on predictive AI tools, which  
are used to make decisions about hiring,  
lending, medical treatment, and so on.  
We'll highlight concerns about fairness and bias  
in predictive AI, and we'll introduce  
three criteria, or tests, of fairness for predictive AI tools  
and highlight the limitations of each one.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.2 A Survey of Ethics and AI  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We begin our brief overview of AI ethics  
by talking about ethical issues that  
arise in the development of AI technology.  
First, pre-training large language models  
is done with huge data centers which  
consume substantial amounts of energy and water.  
Here, we see an image of OpenAI's Stargate Data Center  
in Texas.  
Where huge amounts of energy and water are used by data centers,  
this will tend to raise energy and water  
prices for ordinary consumers.  
And this raises the ethical question of,  
how should we balance technological development  
with the needs of ordinary consumers?  
The energy usage associated with AI  
also threatens our ability to effectively mitigate  
climate change, which is among the most important societal  
challenges that we face today.  
Modern LLM-based tools are increasingly also using  
substantial energy at inference time  
when you engage with the chatbot,  
and this puts even more pressure on the energy grid.  
Second, LLMs are trained on massive amounts of text, images,  
and other media available on the internet.  
This raises concerns about copyright  
and intellectual property rights more broadly.  
In 2023, The New York Times filed a lawsuit against OpenAI,  
accusing it of copyright infringement,  
alleging that OpenAI used millions of its articles  
without authorization to train its AI models.  
The lawsuit is still ongoing.  
Now, even if AI companies don't violate any copyrights  
when training their models, there  
may still be ethical concerns.  
For example, do authors and artists  
have a legitimate complaint if their work  
is used to train models which might later produce work  
in their distinctive style?  
Third, fine-tuning of AI models often  
involves manual data-labeling work.  
A lot of this data-labeling work is  
done in the developing world where workers receive low pay  
and have little job stability.  
This raises concerns about worker exploitation.  
And some of this work also involves  
going through images and video depicting  
violence and abuse, which can be psychologically traumatic.  
How can we develop AI tools, then,  
while still respecting workers' rights and interests?  
Those are some of the ethical issues  
that have to do with how AI systems are developed.  
What about when AI systems are deployed?  
AI has the potential to change society  
in significant ways, which will have to be navigated.  
For example, AI will likely affect the future of work.  
Technological development is usually highly beneficial,  
but it can also be disruptive.  
Technology tends to eliminate some jobs,  
but also create new ones.  
Consider the invention of the automobile.  
It eliminated a lot of jobs associated with horses,  
such as carriage makers and Teamsters, but at the same time,  
it also created a lot of new jobs  
in car factories, repair shops, highway construction, and so on.  
With every technological change, there are winners and losers.  
And even when the change is, on balance, positive,  
as it usually is, we shouldn't forget  
about those who have been impacted negatively.  
Historically, workers have often fought technological changes  
that threaten their livelihoods.  
Maybe the most famous case is that of the Luddites,  
a group of textile workers who sabotaged automated textile  
machinery in England in the 1800s.  
We can anticipate similar resistance  
on the part of those who feel that their jobs are  
at risk due to AI.  
Now, some people, including some of the biggest names in AI,  
have predicted that AI will permanently  
replace a high percentage of jobs,  
leading to a future of mass unemployment.  
This is a controversial prediction,  
and many economists disagree with it.  
But if it does come about, how should we respond?  
For instance, should we then implement  
a so-called universal basic income  
where everyone receives some baseline level of income  
regardless of whether they work?  
Perhaps, but that proposal is very costly, one,  
and it will take a lot of political will  
to put it into practice.  
And even if a universal basic income  
is needed to keep people from falling into poverty,  
people get more from work besides just a paycheck.  
They get a sense of purpose, opportunities for achievement,  
and social interactions.  
There are also ethical concerns about power and inequality.  
Assuming that AI brings about these huge economic benefits  
that have been promised, how will those benefits be shared?  
Will they go primarily to the wealthy few,  
such as the founders of major AI companies,  
further exacerbating the inequality we see  
in contemporary society?  
And will AI undermine democracy or, instead, strengthen it?  
So far, we've looked at broad ethical issues  
having to do with the development of AI  
and big-picture societal impacts.  
Let's now turn to ethical issues having  
to do with how particular AI tools operate.  
We can distinguish between generative AI on the one hand  
and predictive AI on the other.  
Generative AI tools produce text, images, audio, and video  
in response to user prompts.  
The main ethical concerns with generative AI  
have to do with what sorts of responses  
these GenAI tools should produce,  
and what sorts they should avoid producing.  
In some cases, the answers are obvious.  
Everyone agrees that GenAI tools should not  
output instructions for homemade bombs or scam messages,  
to name just a couple of obvious examples.  
There, the real challenge is just how  
to make sure that GenAI tools don't produce such outputs even  
if users ask them to, and even if they use clever techniques,  
often called jailbreaks, to try to get around safeguards.  
This is a difficult technical challenge.  
Other times, however, it's less obvious and more controversial  
whether it's acceptable for a GenAI tool  
to output a certain kind of response.  
For example, is it OK for them to give financial advice?  
And if so, what kind of financial advice  
should they give?  
Should they refrain from talking about religion or politics?  
And if not, what sorts of things should they say?  
How should they respond when users  
want to discuss mental health issues  
or other sensitive personal problems?  
These matters are controversial, and there's  
no consensus on the horizon.  
So it seems that we want GenAI tools to be aligned  
with human values, but what does this even mean,  
and how can such alignment be achieved?  
This will be the topic of the third lecture in this module.  
Finally, let's turn to predictive AI tools.  
These tools are used to make predictions  
about people in order to then make decisions about them.  
Let's consider some examples.  
In lending, a bank might use an algorithm  
to try to predict how likely it is that you would repay a given  
loan in order to then decide whether to approve your loan  
application.  
In hiring, a firm might use an algorithm  
to try to predict whether you would succeed in the job  
in order to decide whether to hire you.  
In criminal justice, a judge or a parole board  
might use some algorithm to try to predict  
whether a defendant will reoffend in order  
to decide whether to grant them parole or pretrial release  
or what have you.  
And finally, in medicine, a doctor  
might use an algorithm in diagnosis  
to predict whether a patient has some particular condition  
in order to decide whether to give them a certain treatment.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.3 Ethics and Predictive AI  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In each of these cases,  
our algorithm, or our predictive AI tool,  
takes as input some known features.  
For example, in the lending case,  
the features might include income and credit  
score, and perhaps some others.  
In the hiring case, the features might be  
whatever resume was submitted.  
In the criminal justice case, the features  
on which we base our predictions might  
include things like the defendant's criminal record,  
employment history, age, and so on.  
And in the medical case, the features  
might include the patient's age, sex, vital signs,  
and perhaps the results of a chest scan, a blood draw,  
and so on.  
The algorithm then outputs a prediction.  
For instance, that the person would very likely  
repay the loan, that they're likely to be  
a bad worker, that they're a high-risk defendant who's  
likely to re-offend, or that the patient probably doesn't  
have the disease in question.  
And then finally, a human, or perhaps even another algorithm,  
takes that prediction into account  
and decides how to treat the decision subject--  
whether to approve their loan application,  
whether to hire them, whether to grant them parole,  
or whether to begin some course of medical treatment.  
So what ethical concerns are raised  
by the use of predictive AI tools?  
To make things concrete, suppose that you apply for a job and get  
rejected.  
That's pretty normal.  
But then you learn that the company used an AI-driven resume  
screening tool to decide which applicants to interview,  
and you turned out not to be among them.  
Moreover, you then apply to a bunch of other companies,  
but you still don't get any interviews,  
let alone a job offer, and you find out  
that those other companies were also using AI-driven  
resume screening tools.  
Do you have any legitimate complaints  
about what's happened?  
Did anything unethical happen?  
And if so, what could it be?  
Well, you might complain that it's  
unethical to make decisions about how to treat  
people using algorithms.  
So, for example, you might think it's unethical for a company  
to decide who to interview using AI tools.  
Perhaps everyone has a right to have  
their case evaluated by a real, flesh-and-blood human.  
Is that true?  
Why would you have a right to be assessed by a human rather  
than some predictive AI tool?  
What if the predictive AI tools used by the companies  
are actually just much better than humans  
at predicting who would be a good employee?  
What if it's also much more efficient to use AI,  
such that you get a decision on your job application  
or your loan application within seconds,  
rather than having to wait for weeks?  
We might also ask, does the context matter?  
Maybe there's nothing wrong with private companies  
using AI tools to decide who to hire,  
but perhaps it would be wrong if the government,  
through the courts, used such tools  
to decide who should be released on parole  
and who should be kept in jail.  
Here's another thought you might have.  
Perhaps it's OK to use AI tools for hiring, lending,  
and the like, but only if you're able to appeal  
their assessments.  
So we can ask, does everyone at least  
have the right to be able to appeal  
an algorithm's assessment of them  
and have a human double-check?  
And if so, why is that?  
Finally, when it is OK in principle to use AI tools,  
what standards must they meet in order for it  
to be ethical to use them?  
In the rest of this lecture, we'll  
focus on the last question, about what predictive AI  
tools have to be like in order for it to be ethical  
for us to use them.  
Of course, one thing we care about with predictive AI tools  
is accuracy.  
Their predictions inevitably won't be perfect.  
They'll sometimes make mistakes, just as humans do.  
But they should at least be fairly accurate  
if they're going to be deployed in high-stakes contexts  
like hiring, lending, medicine, and criminal justice.  
But accuracy might not, itself, be enough.  
A major concern about predictive AI tools  
is whether they might be biased against certain groups  
of people.  
In particular, they might be biased  
against people of a certain race, or gender, or religion,  
or sexual orientation.  
Of course, humans themselves have many biases,  
including both explicit or conscious biases,  
and also implicit or subconscious biases.  
And there's obviously a long history  
of discrimination against groups like African-Americans, women,  
and homosexuals, to name just a few.  
Predictive AI tools might help us make better predictions  
and decisions by avoiding the influence of human biases.  
So maybe AI tools would be less biased  
than flesh-and-blood humans.  
But there's also a risk that predictive AI tools might simply  
recreate human biases, because they're  
trained on data infused with the traces  
of historical discrimination and they're  
deployed in a society in which there  
are significant inequalities between groups.  
How, then, can we test predictive AI tools for bias  
and try to ensure that they're as unbiased as possible?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.4 Sources of Bias  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's start by briefly exploring  
how biases might arise in predictive AI tools.  
There are many different ways, but we'll look at just two here  
today.  
First up is biased data.  
If we're not careful, our data can  
be biased in ways that make it unreliable as a predictor  
of target variable, the thing we ultimately want to predict.  
So consider hiring, where we might  
use data about past employment to predict job candidates'  
future job performance.  
If candidates of a certain race or gender  
have been victims of past discrimination in hiring,  
and as a result, have had longer periods of unemployment,  
our data might misleadingly suggest  
that they're worse candidates than they really are.  
The data will suggest that they're  
less likely to perform well in the job  
than their true merit would indicate.  
Similarly, in criminal justice contexts,  
we might be trying to predict how likely a defendant is  
to re-offend, or recidivate, if they're  
granted pretrial release.  
And we might use prior arrests, for example,  
as part of our data to generate our predictive AI tool.  
But suppose, as is very plausible,  
that members of some races have been  
victims of past discrimination in policing.  
They've been more likely to be arrested  
for even minor offenses, and they've been sometimes arrested  
for no good reason at all.  
Then our data might misleadingly suggest  
that they're more dangerous, or more risky, or more  
likely to re-offend than they truly are.  
And then, when we use this data to build predictive AI tools,  
it's likely to lead us to make decisions which are also biased  
against members of that group.  
Our second source of bias that we'll consider today  
is feedback loops.  
In a feedback loop, decisions made at one time  
generate data that feed back into the system as input, which  
in turn affect predictions and decisions made at the next time,  
and so on.  
For an example, let's consider predictive policing.  
There, police use AI tools to try  
to predict where crimes will take place so as  
to deploy officers more effectively  
and efficiently in areas that are more likely to be  
the locations of crime.  
So data about past crime drive decisions  
about where to have officers stationed and patrolling.  
These decisions then affect where crimes are observed  
and where arrests are made, which  
become further data points that feed back into the system.  
If there have been lots of arrests or reports of crime  
in some location, the predictive policing algorithm  
might lead us to put more police there.  
But then, since there are now more police in that area,  
there will probably be even more crimes observed  
and arrests made in that same area.  
This new data then feeds back into the algorithm,  
leading us to station yet more police there,  
who then observe yet more crimes and make yet more arrests  
and so on.  
Of course, this sort of feedback loop  
also raises concerns about bias, since areas  
with lots of arrests and crimes and which  
are more heavily policed might tend  
to be more heavily populated by minority groups.  
Now, once we're aware of the danger of feedback loops,  
we might be able to stop them.  
For example, rather than using data just  
about the number of arrests in different areas  
to decide where to station police,  
we might instead have our algorithm use data  
about the number of arrests per man hour of patrolling  
done in that area.  
And this would help us compensate for the fact  
that not all areas are policed in the same way when  
we're trying to figure out which areas are, in fact, high-risk.  
Nevertheless, our take-home message for now  
is simply that feedback loops are another possible source  
of bias in predictive AI tools.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.5 Criteria of Fairness  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So much for cautionary tales.  
Let's take a step back and ask a general question.  
What does it take for a predictive AI algorithm  
to be fair or unbiased with respect to group membership?  
What does it take for an algorithm  
to be unbiased with respect to, say, race or gender?  
Are there any criteria that we can  
use to test for bias or lack of bias?  
In the remainder of this lecture,  
we'll look at three criteria that have been widely discussed.  
They're known as demographic parity, fairness as unawareness,  
and counterfactual fairness.  
For each one, we'll say what they are  
and why they might seem appealing, as well  
as highlighting the limitations of each.  
And then in the next lecture, we'll  
consider a family of further criteria, all of which  
have to do with error rates.  
The first criterion of fairness that we'll discuss  
is called demographic parity.  
It says that the percentage of individuals  
who receive a given prediction should  
be the same for each demographic group.  
For example, in the criminal justice context,  
it says that the percentage of Black defendants who  
are predicted to be high-risk should  
be the same as the percentage of white defendants  
who are predicted to be high-risk.  
In the college admissions context,  
it says that, for example, the percentage  
of men who are predicted to achieve, say, a 3.0 grade point  
average, if admitted, should be the same as the percentage  
of women who are predicted to achieve that same 3.0 grade  
point average if admitted.  
In the lending context, suppose, for example,  
that when we run our algorithm, 70% of male loan applicants  
are predicted to repay a given mortgage, but only 50%  
of female loan applicants are predicted  
to repay that same mortgage, then our lending algorithm would  
violate demographic parity.  
So if we endorse demographic parity  
as a criterion of fairness, we'll  
have to include that sample lending  
algorithm is biased or unfair.  
The condition of demographic parity is initially tempting,  
but it should ultimately be rejected  
as a criterion of fairness.  
Let me explain why.  
Say that the base rate of some feature, X, in a given group  
is just the percentage of members of that group who  
have that feature, X. So, for example,  
the base rate of loan default among males  
is just, by definition, the percentage  
of males who default on their loans.  
The base rate of criminal re-offending among whites  
is just the percentage of whites who criminally  
re-offend, and so on.  
The key problem then, with demographic parity  
is that trying to satisfy demographic parity  
can amount to stubbornly refusing  
to acknowledge differences in base rates across groups.  
This is most obvious in the case of medical diagnosis, where  
we might use AI tools to try to predict whether someone  
will develop heart disease.  
Now, we know that the base rate of heart disease differs by sex.  
In particular, heart disease is more prevalent in males  
than in females.  
So a good algorithm should predict the development  
of heart disease in a higher percentage  
of males than females.  
But demographic parity would actually  
require that our algorithm predict equal percentages  
of males and females as being likely to develop heart disease.  
And that would be a mistake, and one with potentially very  
serious negative consequences.  
For another example, consider criminal recidivism prediction.  
We know that males commit violent crime  
at far greater rates than females.  
That is, the base rate of violent crime  
is higher for males than it is for females.  
But if we have a predictive AI tool, some algorithm,  
which aims to predict how likely someone is  
to commit a violent crime, then satisfying demographic parity  
would require that this algorithm predict  
that equal percentages of males and females  
are likely to commit a violent crime.  
But that's a mistake.  
And again, it's a mistake with potentially disastrous  
consequences.  
Here's another way to put the problem with demographic parity.  
If base rates are unequal across groups, then even  
an omniscient algorithm, one which always gets things right  
and knows the future--  
that omniscient algorithm would violate demographic parity.  
But that doesn't mean that our hypothetical omniscient  
algorithm would therefore be biased or unfair.  
Now, when base rates are unequal,  
this may be due to past or present injustices.  
That's certainly the case with, for example,  
the higher base rate of unemployment  
for African-Americans relative to white Americans.  
In other cases, however, it might be due to other factors,  
as with the fact that the base rate of heart disease  
is higher for males than for females.  
But in all of these cases, even if we  
should take some other steps to rectify  
various historical injustices, we  
shouldn't just stick our heads in the sand  
and pretend that base rates are equal across groups  
when we know that they're not.  
And that's why even though demographic parity might  
be appropriate in some contexts, it's  
not a criterion that we should impose in full generality  
as a requirement of fairness or lack of bias.  
Our next two criteria of fairness are more attractive.  
The next one that we'll consider is called fairness  
as unawareness.  
It says that in order to be fair or unbiased,  
an algorithm must be blind to group membership.  
It must not have access to, for example,  
the race or the gender of the individuals about whom  
it's making predictions.  
Fairness as unawareness is very intuitive.  
But let's look closer.  
First, we should ask whether satisfying fairness  
as unawareness is sufficient for fairness or for lack of bias.  
That is to say, is it true that if an algorithm  
is blind to race, say, then it can't be racially biased.  
Unfortunately, the answer is probably no.  
Even without direct access to an individual's race,  
an algorithm might still have indirect access to their race  
through the use of so-called proxies.  
For example, an individual's race  
can often be inferred from their zip code, or other information  
about them, such as their name.  
So making sure an algorithm doesn't  
have direct knowledge of an individual's race  
might help to mitigate bias, but on its own,  
it doesn't guarantee that an algorithm will be unbiased.  
Next, we should also ask whether fairness as unawareness  
is necessary for fairness or for lack of bias.  
That is to say, is it true that if an algorithm violates  
fairness as unawareness-- if, for example, it's  
given information about what race someone belongs to-- then  
it's biased?  
Well, probably not.  
An algorithm could have access to an individual's race,  
but not use that information in any inappropriate way.  
Consider humans rather than algorithms.  
Just because you know that someone is Black or as a woman,  
that doesn't necessarily mean you will be biased against them  
on grounds of race or gender.  
Knowledge of someone's race or gender  
might make it possible for you to be biased against them,  
but it doesn't, on its own, guarantee  
that you will be biased.  
Moreover, in some cases, knowing an individual's race or gender  
might be very important.  
For example, in medical diagnosis,  
knowing a patient's sex can be very  
helpful in ensuring accuracy.  
Some features might also have different meanings  
for different groups.  
For example, in contemporary society,  
women are more likely to take time off work  
for caring responsibilities.  
So in assessing what someone's period of unemployment  
might tell us about their likely performance as a worker,  
it might be important, and actually helpful,  
and actually a way to mitigate bias to know their gender.  
This might actually help us avoid being  
biased with respect to gender.  
Finally, knowing someone's race or gender  
might help us to actively compensate  
for biases, as in some instances of affirmative action.  
Blinding algorithms to individuals' race or gender  
or religion may be a good idea, and perhaps it will generally  
help to reduce bias.  
But it's probably neither strictly necessary for fairness,  
nor, on its own, sufficient for fairness.  
Our last criterion of fairness for today, for this lecture,  
is known as counterfactual fairness.  
Given some predictive AI tool as well as the predictions  
it yields for different people, we  
can ask, for each person, the following question--  
is the prediction that the algorithm made for that person  
the same as the prediction that they  
would have gotten had they been a member  
of a different demographic group instead?  
If so-- that is, if they would have received the same  
prediction even if they had belonged to a different group--  
then the counterfactual fairness criterion is satisfied.  
If not-- that is, if they would have received  
a different prediction if they had belonged  
to a different group-- then the counterfactual fairness  
criterion is violated.  
Let's consider some examples.  
In the criminal justice context, where we have an algorithm which  
aims to predict how likely defendants are to re-offend,  
we would ask questions like, would this black defendant  
who was predicted to be high-risk also  
have been predicted to be high-risk  
if they had instead been white?  
In the lending context, we might ask,  
would this female loan applicant who  
is predicted to repay the loan also  
have been predicted to repay the loan if they had instead  
been male?  
Counterfactual fairness says that a predictive AI tool  
is fair or unbiased only if it gives everyone  
the same prediction that they would have been given  
if they had been of some other race or gender,  
or what have you, instead.  
Counterfactual fairness is very natural and intuitive.  
It really does seem like part of our ordinary conception  
of bias-- that if you would have treated someone differently  
if they had been of some other race or gender, then  
that's enough for you to count as being biased with respect  
to race or gender.  
But in fact, counterfactual fairness  
is hard to make precise enough to implement.  
How should we assess counterfactual conditionals?  
Like the following-- person X, who is, in fact,  
African-American, would have gotten the same prediction  
if they had been white instead.  
In particular, we have to ask what features of person  
X should we hold fixed when making  
this comparison between the prediction they actually  
received and the prediction they would have received  
if they were white instead.  
Obviously, we don't hold fixed their race.  
After all, we're wondering what prediction  
they would have received if they had been of a different race.  
But what about their name?  
Should we also hold fixed what their name actually  
is, even though names are closely associated with race?  
What about income?  
Should we hold fixed their actual income  
when making this comparison, even though they might well  
have had a different income as a result  
of different opportunities and different challenges  
that they might have faced if they had been white instead?  
What about their employment history?  
Should we hold their actual employment history  
fixed, even though they might actually  
have been victims of employment discrimination in the past?  
It's hard to know how to answer such questions,  
but we have to answer them if we are  
to apply the counterfactual criterion in practice.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.6 Summary  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's take stock.  
AI is likely to transform society in huge ways.  
And it comes in many different forms,  
from tools used in self-driving cars  
to generative AI, which produces text and images,  
to predictive AI.  
As a result, AI raises a wide range  
of different ethical issues.  
So AI ethics isn't one thing, but many.  
We've surveyed a number of the main ethical issues raised  
by AI.  
We then focused primarily on predictive AI tools,  
which aim to make predictions about individuals in order  
to then help us make better decisions about them.  
These sorts of tools are used in hiring, lending,  
medical diagnosis, criminal justice,  
and many other contexts.  
A major concern with predictive AI tools  
has to do with fairness and bias.  
How can we test predictive AI tools  
to know whether they're biased with respect to race, gender,  
or other categories?  
We examined three possible criteria or tests for fairness.  
These were demographic parity, fairness as unawareness,  
and counterfactual fairness.  
We saw that demographic parity is ultimately  
probably implausible in most contexts  
and should generally be rejected.  
The other two criteria, fairness as unawareness  
and counterfactual fairness, are more compelling.  
They also, though, still have limitations,  
and they probably aren't the whole story when  
it comes to fairness and bias.  
In the next lecture, we'll continue  
to explore fairness and bias in predictive AI systems,  
exploring a range of further criteria of fairness,  
all having to do with the notion that fairness requires  
equal accuracy for different groups.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this lecture, we explored how artificial intelligence raises a wide range of ethical challenges as it becomes embedded in decision-making systems. We examined how predictive AI can introduce bias and how different frameworks attempt to define and measure fairness.

Key Takeaways:  
The broad and diverse nature of ethical issues in AI across different applications  
How predictive AI systems use data to make decisions about individuals  
The role of biased data and feedback loops in creating unfair outcomes  
The differences between fairness definitions such as demographic parity, unawareness, and counterfactual fairness  
The limitations of existing approaches to fairness in real-world settings  
Congratulations on finishing this lecture\! You’ve built a strong foundation for understanding the ethical challenges of AI and how to critically evaluate fairness and bias in modern AI systems.  
\`\`\`

Lecture 2: AI Fairness and Bias  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: AI Fairness and Bias, taught by Professor Brian Hedden, Professor in the departments of Linguistics and Philosophy and Electrical Engineering and Computer Science (EECS) at the Massachusetts Institute of Technology.

This lecture continues the exploration of fairness in predictive AI systems, focusing on how we define and measure bias in algorithmic decision-making. Building on earlier discussions, the lecture introduces a family of fairness criteria based on the idea that AI systems should perform equally well across demographic groups.

Through the real-world case of the COMPAS algorithm, learners will examine how different definitions of fairness can lead to conflicting conclusions about whether a system is biased. The lecture also introduces key statistical concepts such as false positive rates, false negative rates, and predictive values, and shows how these lead to multiple competing fairness criteria.

A central theme of the lecture is that these fairness criteria are often mathematically incompatible, meaning they cannot all be satisfied at the same time. Learners will explore different ways to respond to this challenge, including trade-offs, optimization approaches, and arguments for prioritizing certain criteria over others.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain how fairness in AI can be defined in terms of error rates across groups  
Distinguish between different types of error rates (e.g., false positives, false negatives, predictive values)  
Analyze how different fairness criteria can lead to conflicting judgments about bias  
Describe the concept of impossibility theorems in AI fairness  
Evaluate different responses to trade-offs between competing fairness criteria  
Reflect on how to choose appropriate fairness definitions in real-world contexts  
\`\`\`

L2.1 Introduction  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In this lecture, we'll  
continue our discussion of fairness and bias  
in predictive AI.  
Predictive AI tools make predictions  
about individuals for the purpose of making decisions  
about them.  
For example, they might be used to predict  
job candidates future job performance in order  
to decide whom to hire, or they might  
be used to predict how likely a loan applicant is  
to repay the loan in question in order to decide  
whether to approve that loan.  
Predictive AI tools may be biased  
against individuals on the basis of their race, gender,  
or other features.  
Criteria of fairness aim to help us determine whether or not  
a given algorithm is biased.  
In the previous lecture, we introduced  
three widely discussed criteria of fairness--  
demographic parity, fairness as unawareness,  
and counterfactual fairness-- and we  
discussed the pros and cons of each.  
In this lecture, we'll discuss a family  
of other criteria of fairness that all require  
that predictive AI tools perform equally  
well across different demographic groups,  
in the sense of having equal error  
rates for each of those groups.  
As we'll see, however, there are many different ways  
to understand equality of error rates,  
and this leads to many different criteria of fairness.  
We'll then see that many of these criteria are actually  
mutually incompatible, meaning that they simply cannot all be  
satisfied at once.  
This is the upshot of what are known as impossibility theorems.  
We'll then explore different responses  
to these impossibility theorems, including  
an argument that most of them should perhaps  
even just be rejected as fundamentally misguided.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.2 COMPAS  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The criteria of fairness  
that we'll discuss in this lecture  
were inspired by the case of the COMPAS algorithm.  
COMPAS is an acronym for Correctional Offender Management  
Profiling for Alternative Sanctions.  
It's an algorithm that has been used in jurisdictions  
across the United States to assess  
the riskiness of criminal defendants,  
or how likely they are to re-offend.  
In 2016, the investigative journalism organization  
ProPublica published a bombshell exposé  
about COMPAS, in which they argued  
that it was racially biased, and, in particular,  
biased against African-Americans.  
Here, we see the headline and cover image from their article.  
So let's dig in.  
COMPAS outputs a risk score for a defendant based on answers  
to a questionnaire with 137 items.  
These risk scores are then used to make decisions  
about pretrial release, sentencing, and parole.  
I noted that ProPublica argued that COMPAS had a racial bias,  
but crucially, none of the 137 questions  
asked about the defendant's race.  
The algorithm was, in fact, blind to race.  
So on what basis did ProPublica argue that COMPAS was biased?  
Well, interestingly, ProPublica found that the COMPAS algorithm  
made different types of errors at different rates  
for different racial groups.  
In particular, COMPAS was found to have  
a higher false positive rate for Black defendants  
than for white defendants.  
What this means is that among defendants who actually  
did not re-offend, the percentage  
of Black defendants who were falsely predicted to re-offend  
was higher than the percentage of white defendants  
who were falsely predicted to re-offend.  
Let's put that another way.  
Look at all of the Black defendants who  
actually did not re-offend.  
And find what percentage of them were incorrectly  
predicted to re-offend.  
That's COMPAS's false positive rate for Black defendants.  
Next, look at all the white defendants who actually  
did not re-offend and find what percentage of them  
were incorrectly predicted to re-offend.  
That's COMPAS's false positive rate for white defendants.  
What ProPublica then found is that COMPAS  
had a higher false positive rate for Black defendants  
than for white defendants.  
ProPublica also found that COMPAS  
had a higher false negative rate for white defendants  
than for Black defendants.  
What this means is that among defendants who actually  
did re-offend, the percentage of whites who were falsely  
predicted not to re-offend was higher  
than the percentage of Black defendants  
who were falsely predicted not to re-offend.  
ProPublica used these facts to conclude that COMPAS was biased  
against Black defendants.  
Here we see a table from ProPublica's article.  
The numbers in the top row are COMPAS's false positive rate  
for white and Black defendants.  
The false positive rate was 23.5% for white defendants,  
but 44.9% for Black defendants.  
The numbers in the bottom row are  
COMPAS's false negative rates for white and Black defendants  
the.  
False negative rate was 47.7% for white defendants,  
but only 28% for Black defendants.  
In arguing that COMPAS was biased,  
ProPublica's team was appealing to the following idea.  
Fairness, or lack of bias, requires  
that algorithms make the same sorts  
of errors at about the same rate across different groups.  
So if an algorithm makes some sort of error  
more frequently for people of one race  
than for people of another race, then that's  
enough for the algorithm to count as biased or unfair  
on the basis of race.  
Now, ProPublica's conclusion has been controversial.  
Other researchers, including both independent researchers  
and the company behind COMPAS pushed back.  
They argued that having different false positive rates  
and having different false negative rates  
across racial groups doesn't, on its own, constitute bias.  
And this supported their conclusion  
by showing that COMPAS performs equally  
well for white and Black defendants in other respects.  
COMPAS has 10 different risk scores  
that it can give to a defendant.  
Now, take a given risk score and look at all the Black defendants  
who were assigned that risk score  
and find what percentage of them went on to re-offend.  
Then, for that same risk score, look at all the white defendants  
who were assigned that risk score and find  
what percentage of them went on to re-offend.  
It turns out that these percentages were about the same,  
and that was true for every one of the 10 possible risk scores.  
And this means that each risk score  
means the same thing, in some sense, for white defendants  
as it does for Black defendants.  
And on that basis, other critics argued that COMPAS  
was, in fact, not biased.  
OK, so what's going on here?  
It looks like ProPublica was endorsing one set of criteria  
of fairness, which COMPAS violated,  
and others were endorsing different criteria of fairness,  
which COMPAS satisfied.  
And this raises the question, which of these criteria  
really are necessary for fairness or lack of bias?  
Now, it turns out that we've only  
seen the tip of the iceberg.  
There are many more possible criteria of fairness,  
all requiring that certain sorts of error rates  
be equal across groups.  
So let's dive in.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.3 Error Rate Parity  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's start with a major distinction between two  
different kinds of error rates.  
We're trying to predict some outcome,  
like whether a person will repay a loan  
or whether a person will criminally re-offend.  
We label one of these outcomes positive and the other negative.  
Don't read too much into these labels.  
They're not meant to indicate which outcome is the good one  
and which is the bad one.  
We could have instead used yes and no or 0 and 1,  
but we'll just stick with positive and negative.  
Now, to the error rates.  
First up, we can ask, of the people who really are,  
in reality, a certain way-- positive or negative--  
what percentage of them were falsely  
predicted to be the other way?  
The concept of a false positive rate is like this.  
The false positive rate is found by looking at the people who  
really have the outcome negative and seeing  
what percentage of them were falsely  
predicted to be positive.  
The concept of false negative rate is also like this.  
It's found by looking at the people who, in reality, have  
the outcome positive and seeing what percentage of them  
were falsely predicted to be negative.  
These are what we'll call prediction  
given reality error rates.  
The idea here is that, on average,  
people who are the same in reality  
should get the same prediction.  
But we might also look at what we might call reality  
given prediction error rates.  
There, we ask, of the people who are predicted  
to have a certain outcome, what percentage of them, in reality,  
had that outcome?  
Here, the concept of positive predictive value is like this.  
It's found by looking at all of the people who were predicted  
to be positive and seeing what percentage of them  
actually, in reality, wound up being positive.  
And the concept of negative predictive value  
is also like this.  
It's found by looking at the people who were predicted  
to be negative and seeing what percentage of them  
actually wound up, in reality, being negative.  
These different concepts of error rates  
yield different kinds of possible fairness criteria.  
If we care about the prediction given reality types of error  
rates, we might want to demand that those be equal  
across groups.  
So we might endorse equality of false positive rates, which  
says that fairness requires that an algorithm have  
the same false positive rate for each group.  
And we might endorse equality of false negative rates, which  
says that fairness requires that an algorithm have  
the same false negative rate for each group.  
That's what ProPublica did in their analysis.  
They assumed that fairness required  
equality of false positive rates and equality  
of false negative rates across different groups.  
But next, if we care about reality given prediction  
error rates, we might want to demand that those be equal  
across groups.  
So we might endorse equality of positive predictive value, which  
says that an algorithm should have  
the same positive predictive value for all groups.  
And we might also endorse equality  
of negative predictive value, which  
says that an algorithm should have  
the same negative predictive value for all groups.  
Now, we've so far been talking about predictions  
as being binary.  
We ask, will the loan applicant repay the loan?  
And the predictive AI tool says either yes or no.  
Will the defendant re-offend?  
Again, the answers can only be yes or no.  
We just have two possible predictions.  
Will the job candidate have satisfactory job performance  
if hired?  
And again, we allow only two possible predictions, yes  
and no.  
But some predictive AI tools, including COMPAS output,  
more fine-grained predictions.  
For instance, they might output probabilities or something  
similar.  
These are often called risk scores.  
Then, our predictive AI tool might say, for example,  
that the loan applicant in question  
is 75% likely to repay the loan, or might  
say they're 90% likely to repay it, and so on.  
Or, when asked how likely it is that the defendant in question  
will re-offend our algorithm could  
answer 10%, or 20%, or something else, and so on.  
How can we formulate criteria of fairness  
when our predictive AI tool outputs  
these sorts of fine-grained probabilistic predictions?  
It's natural to try to generalize  
the criteria we've looked at already  
to the case of probabilities.  
Remember that we have both prediction given  
reality criteria and reality given prediction criteria.  
So let's start with the former.  
Remember that we had equality of false positive rates, which  
says that the percentage of actually negative people who  
are falsely predicted to be positive  
should be the same for all groups.  
The natural analog of this, for the case  
of fine-grained probabilistic risk scores,  
is what's known as balance for the negative class.  
It says that if we look at all of the actually negative people  
in a given group, and we look at the average risk scores  
that they were assigned, that number-- that average risk  
score-- should be the same for each group.  
That is to say, the average risk score  
assigned to people who are actually negative  
should be the same for each group.  
We also had equality of false negative rates, which  
says that the percentage of actually positive people who  
are falsely predicted to be negative  
should be the same for all groups.  
The natural analog of this is what's  
known as balance for the positive class.  
It says that if we look at the actually positive people  
in a given group and look at the average risk scores  
that they were assigned, that number should  
be the same for each group.  
That is to say, the average risk score  
assigned to people who are actually positive  
should be the same for each group.  
Turn now to the reality given the prediction criteria.  
We had equality of positive predictive value, which  
says that the percentage of people  
predicted to be positive who are, in reality, positive--  
that should be the same for each group.  
We also had equality of negative predictive value, which  
says that the percentage of people  
predicted to be negative who are, in reality, negative should  
be the same for each group.  
These criteria have a single analog  
for the case of risk scores.  
It's known as calibration, which says that for each risk score,  
the percentage of people assigned that risk score who  
are actually positive should be the same for all groups.  
That requires that each risk score, in some sense,  
mean the same thing, regardless of the group in question.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.4 Impossibility Results  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: OK.  
Now, the criteria we just discussed  
are all very intuitive, very appealing, and very natural.  
It really does seem that an algorithm that  
makes different types of errors at different rates  
for different groups must somehow or other be biased,  
so perhaps we should just endorse  
all of the different criteria that we've discussed.  
We would then say that a predictive AI  
tool that outputs binary yes/no predictions  
has to satisfy four criteria in order  
to be fair-- it has to satisfy equality  
of false positive rates, equality  
of false negative rates, equality  
of positive predictive value, and equality  
of negative predictive value.  
And when a predictive AI tool outputs fine-grained  
probabilistic risk scores, we might say that in order to be  
fair or unbiased, it's got to satisfy three criteria--  
balance for the positive class, balance for the negative class,  
as well as calibration.  
But unfortunately, and very surprisingly, these criteria  
are actually in conflict with each other.  
It's actually impossible for a predictive AI  
tool which outputs binary yes/no predictions to satisfy  
all of our four criteria together at the same time.  
Any algorithm has to violate at least one of them.  
And it's also impossible for a predictive AI  
tool which outputs fine grained probabilistic risk  
scores to satisfy all three of our criteria  
together at the same time.  
This means that any algorithm, no matter how we design it,  
is inevitably going to violate at least one  
of these criteria, and possibly more.  
At least, that's the case unless all groups have the same base  
rates, or the predictive AI tool is  
omniscient and able to make perfect predictions.  
But unless those edge cases are considered  
where the base rates are the same across groups  
or we're actually able to be omniscient,  
we're just inevitably going to violate at least one  
of those criteria.  
It's simply impossible-- mathematically  
impossible-- to satisfy all of them together at the same time.  
If you're interested, here are the two papers  
which proved the impossibility results we just mentioned.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.5 Responding to Impossibility  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So the big question is, how should we react  
to these impossibility results?  
This is an area of active debate among philosophers, computer  
scientists, legal scholars, and others  
concerned with fairness and bias.  
We can distinguish three basic types of response.  
First, we might respond with pessimism.  
We might say that these results show  
that fairness is simply impossible  
and bias is simply inevitable.  
Our predictive AI tools just can't be completely fair  
and unbiased no matter what we do, no matter how hard we try.  
A second response that some people have  
is to concede that we can't perfectly  
satisfy all of the criteria at once,  
but to say that we should still aim  
to come as close as possible to satisfying as many as  
possible of the criteria.  
So we could create measures for how badly a predictive AI tool  
violates a given criterion.  
So, for example, when our tool doesn't  
yield equal false positive rates for all groups,  
we could still measure how different  
those false positive rates are, and thereby  
create a measure of how badly our tool violates  
the ideal of fully equal false positive rates.  
And we could do similar things for all of the other criteria,  
creating measures for how badly an algorithm might  
violate those criteria.  
Then we can assign a weight to each criterion which represents  
its overall importance.  
And finally, we could measure the overall bias or unfairness  
of our predictive AI tool, defining that as the sum  
across all of the criteria of how badly the tool violates  
that criterion, weighted by the importance of that criterion.  
Then, even though no predictive AI tool  
can be perfectly fair in the sense of satisfying  
all of these criteria together, we  
could still determine how fair or unbiased a tool is overall,  
and which ones are, overall, more fair than which other ones.  
Then we just have a standard type of optimization problem  
where we have to try to design predictive AI tools so that they  
have as little overall bias or unfairness as possible.  
A third and final response is to choose among the criteria,  
arguing that some should just be rejected as not really  
necessary for fairness when we look closer.  
Let's explore that last type of response,  
which involves arguing for the rejection of some  
of the criteria that we've considered.  
Here's an argument for rejecting almost all of the criteria,  
with the lone exception of calibration.  
Suppose-- and this is an abstract, fanciful example--  
but suppose we have two groups of people.  
In the first group, everyone is a clear case.  
They're very easy to predict.  
In the second group, everyone is what we might call a tough case.  
They're hard to predict.  
With that setup in mind, we should just  
expect to make a lot fewer errors for people  
in the first group, who are all clear cases, than for people  
in the second group, who are all tough cases.  
But that doesn't necessarily mean  
that our predictions are biased against the people  
in the second group.  
It could just be that we're doing the best we can  
and responding to our evidence in an unbiased, even-handed way,  
and it's just a fact about the world  
that people in that second group are more difficult to assess.  
Let's consider a more concrete example.  
Again, it's abstract and in many ways unrealistic,  
but it illustrates the basic idea.  
Suppose that our aim is to predict whether different people  
would repay a given mortgage of, let's say, $500,000.  
Suppose, again, that we have two groups.  
In the first group, half the people  
are multi-millionaires, while the other half  
are utterly destitute.  
In the second group, everyone is sort  
of solidly upper-middle class, though some are a bit wealthier  
than others.  
The people in the first group are easy to predict.  
The multi-millionaires will all almost certainly repay the loan  
no matter what, and the destitute people almost  
certainly wouldn't.  
The people in the second group, by contrast,  
are really tough to predict.  
They might or might not repay the loan, but whether they do  
will depend on lots of different factors,  
like whether we suffer an economic recession,  
or exactly how strong the stock market is at any given time.  
So with this setup, we should probably  
expect lower error rates for that first group  
than for the second.  
So we should expect that whatever predictive AI tool  
we use, we should expect it to have a lower false positive rate  
for the first group than the second, a lower  
false negative rate for the first group than the second,  
a higher false positive predictive value  
for the first group than for the second, a higher  
negative predictive value for the first group  
than for the second, and so on.  
So we expect to violate almost all of the criteria  
that we've considered.  
But that doesn't necessarily mean  
that our predictive algorithm was biased against people  
in that second group.  
Rather, it just means that they're harder to predict.  
They're tough cases rather than clear cases.  
This sort of consideration can be  
used to motivate rejecting all of the criteria that we've seen,  
or at least almost all of them.  
The problem seems to be that most of the criteria  
we've considered lumped together people  
who are, in fact, potentially very different in reality.  
In particular, they lumped together  
people who are clear cases and people who are tough cases.  
Some criteria, for example, require  
that the people who are, in reality, positive  
get, on average, the same predictions regardless  
of what group they're in.  
But this ignores the fact that among the people who  
are positive, some are clear cases of being positive  
and others are tough cases.  
Other criteria require that the people  
who are predicted to be positive are, on average, equally  
likely to really be positive, regardless of what group  
they're in.  
But this also ignores the fact that among the people who  
receive a prediction of positive,  
some are clear cases and others are tough cases.  
The lesson is that the difference between clear cases  
and tough cases matters, and we want our criteria of fairness  
to be sensitive to this fact, but most of the criteria simply  
aren't.  
The one criterion that is sensitive to the difference  
between clear cases and tough cases is calibration.  
Recall that it says that for each risk score,  
the percentage of people assigned  
that risk score who then wind up being positive  
should be the same for each group.  
This criterion is sensitive to the distinction  
between clear cases and tough cases.  
Clear cases should get more extreme risk scores-- that is,  
risk scores closer to 0 or 1--  
and tough cases should get more intermediate risk scores--  
risk scores which are closer to 0.5.  
So in our mortgage example, the multi-millionaires  
should all get risk scores close to 1,  
indicating that they're all almost  
certain to repay the loan.  
The destitute people should get risk scores close to 0,  
since they're almost certain not to be able to repay the loan.  
And the solidly upper middle class people should get risk  
scores closer to 0.5 or so, since it's more uncertain  
and perhaps almost 50/50 whether they would repay that loan  
in question.  
Calibration just says that each risk score  
has to, in some sense, mean the same thing for each group.  
And we can still achieve that while taking into  
account the fact that some people are clear cases  
while others are tough cases.  
So this is one argument for responding  
to the impossibility results by embracing calibration  
and rejecting all of the other criteria.  
It's a controversial argument, and you might find  
yourself disagreeing with it.  
That's OK.  
In ethics, as in philosophy more generally,  
disagreement and debate are the norm.  
So think about how you would want to react and respond  
to these impossibility results.  
Think about what you think fairness and bias amount to when  
we're using AI tools to make predictions about people,  
and try to articulate your reasons for your views  
and subject them to scrutiny.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.6 Summary  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's sum up.  
Predictive AI tools are used to make predictions  
about individuals in order to then make decisions about them.  
They're used in hiring, lending, medical diagnosis,  
criminal justice, and other contexts.  
We want to ensure that these tools are fair and unbiased,  
especially with respect to categories like race, gender,  
and religion, and sexual orientation, among many others.  
One prominent idea that we've considered today  
is that fairness and lack of bias  
require that our tools perform equally well on members  
of these different demographic groups.  
They should have, in some sense, the same error rates  
for each group.  
But we've seen that there are different concepts of error  
rates, which yield many different possible criteria  
of fairness.  
Unfortunately, however, these impossibility results  
prove mathematically that it's impossible for any predictive AI  
tool to satisfy all of these criteria together.  
So we have to decide how to respond and decide  
which criteria really are most important for fairness.  
This is a controversial matter, with no consensus having yet  
been reached.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this lecture, we explored how fairness in predictive AI can be defined through different notions of equal performance across groups. We examined how these definitions can conflict and why it is often impossible to satisfy all fairness criteria at once.

Key Takeaways:  
Fairness can be defined in terms of equal error rates across demographic groups  
Different types of error rates (false positives, false negatives, predictive values) lead to different fairness criteria  
Real-world systems like COMPAS can appear fair under some criteria and biased under others  
Impossibility theorems show that multiple fairness criteria cannot all be satisfied simultaneously  
Designing fair AI systems requires making trade-offs and carefully choosing which criteria to prioritize  
Congratulations on finishing this lecture\! You’ve developed a deeper understanding of how fairness in AI is defined, measured, and contested—and why making ethical decisions about AI systems often requires navigating unavoidable trade-offs.  
\`\`\`

Lecture 3: AI and the Alignment Problem  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 3: AI and the Alignment Problem, taught by Professor Brian Hedden, Professor in the departments of Linguistics and Philosophy and Electrical Engineering and Computer Science (EECS) at the Massachusetts Institute of Technology.

This lecture explores the alignment problem: how to ensure that increasingly powerful AI systems behave in ways that are safe and consistent with human values. It begins by examining why aligning AI through explicit rules is difficult, using examples from mythology and philosophy to illustrate how poorly specified objectives can lead to unintended consequences. The lecture then introduces modern alignment techniques such as reinforcement learning with human feedback (RLHF) and reinforcement learning with AI feedback. Finally, it addresses a deeper challenge—people disagree about values—and explores how democratic approaches, such as voting rules from social choice theory, might be used to aggregate preferences, along with the limitations of these methods.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define the AI alignment problem and explain why it is important  
Describe why hard-coded rules are insufficient for aligning AI systems  
Explain how reinforcement learning with human or AI feedback helps align models  
Identify the challenge of disagreement over human values in alignment  
Evaluate the role of voting rules and social choice theory in aggregating preferences  
Recognize the limitations and trade-offs in democratic approaches to alignment  
\`\`\`

L3.1 Introduction  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In the previous two lectures,  
we focused on ethical issues relating to predictive AI tools,  
such as tools used to make decisions about hiring, lending,  
and criminal justice.  
And there, we focused primarily on issues of fairness and bias.  
We now turn to ethical issues relating to AI systems  
more broadly, including generative AI tools.  
Generative AI tools, such as ChatGPT,  
produce text, images, audio, and other media in response  
to user prompts.  
And AI agents can perform an even wider range of actions,  
such as booking flights and sorting emails.  
Both generative AI tools in general and AI  
agents in particular are becoming increasingly powerful,  
so it's important to ensure that they  
behave in ways that are safe and aligned with our values.  
But how can this be done?  
And what should we do in light of the fact  
that we often disagree about values?  
In this lecture, we'll begin by explaining the problems that  
can arise if we try to achieve alignment  
by giving explicit instructions to AI systems  
in the form of hard-coded rules.  
Because it's impossible to fully account  
for real-world complexity, giving systems hard-coded rules  
to follow can risk unintended negative effects  
because the rules fail to fully specify what we really  
desire and aim for.  
We'll then identify reinforcement learning  
with human feedback and reinforcement  
learning with AI feedback as key techniques used  
to align AI models.  
And then we'll turn to the problem of disagreement.  
We say that AI systems should be aligned with our values,  
with human values.  
But whose values exactly?  
We'll explain how conflicting preferences and values can  
potentially be aggregated in a democratic way  
through voting rules.  
And we'll explain some of the main problems facing  
prominent voting rules, such as majority rule.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.2 Misspecified Desires  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So how can we ensure that AI systems only  
perform actions that we want them to perform?  
How can we ensure that they act in ways  
that are safe, helpful, and generally aligned  
with our values?  
We want to ensure that generative AI  
tools, for instance, refuse to produce racist text  
or instructions on how to commit serious crimes even  
when users ask them to do so.  
But we still want them to do ordinary things  
like generate images of cats or produce solutions  
to math problems when they're asked to do so by the user.  
So how can we make sure that they  
do the things we think they ought  
to do while refraining from doing the things we  
think they ought not to do?  
An immediate first thought you might have  
is that we could simply program AI systems  
with explicit rules about what actions  
they should and should not perform.  
For instance, we could give a system the rule,  
never produce racist text.  
But it's actually impossible to write down  
rules that cover all cases.  
Whatever rules we try to write down,  
we can imagine cases where following those rules  
leads to unexpectedly bad consequences, which were  
not at all what we intended.  
And this theme is explored in mythology, fiction,  
and in philosophy.  
Let's discuss three famous cases that  
explore the problem of misspecified desires.  
The first and probably the most famous one  
is the case of King Midas and Midas touch.  
In Greek mythology, King Midas wished  
that everything he touched would turn to gold,  
but he soon found that this made him unable to eat or drink,  
since whenever he touched a plate of food  
or a glass of water or wine, it immediately turned to gold.  
And according to Aristotle, Midas eventually died  
of starvation as a result. So he wanted  
lots of gold, tried to get it through this rule,  
but he wound up getting more than he bargained for.  
The second case comes from the short story, "The Monkey's Paw,"  
which was published in 1902 by WW Jacobs.  
Here, the protagonists are a poor couple  
who received a mummified monkey's paw, which they learn  
will grant its owner three wishes.  
They ask it for 200 British pounds,  
which is enough to let them pay off their mortgage.  
Then the next day, they receive a visit  
from a representative of their son's employer,  
and the representative tells them  
that their son has died in a tragic work-related accident,  
but that the company will pay them  
200 pounds as a compensation payment.  
They wanted to get 200 pounds, but of course, not in that way.  
This tale is also discussed by the mathematician and early AI  
researcher Norbert Wiener in his group, God & Golem,  
and he uses it to illustrate exactly the problem we're now  
discussing--  
what can go wrong when we try to ensure that AI systems will  
behave as we want them to by giving them explicit rules  
to follow?  
That book was published in 1964, and the problem  
that Wiener identified there is more important than ever.  
More recently, the philosopher Nick Bostrom  
gives a related thought experiment in his book  
Superintelligence where he explores  
ethical challenges relating to so-called superintelligent  
advanced AI.  
He imagines an advanced AI system  
which has given the instruction to just try  
to produce paperclips as quickly and efficiently as possible.  
This seems like a simple, totally mundane instruction.  
What could possibly go wrong?  
But in Bostrom's story, the AI system  
winds up becoming super powerful and turns  
on humans in its monomaniacal pursuit of paperclip production.  
Since humans might eventually try to turn it off and thereby  
stop its paperclip production, and because human bodies  
turn out to contain atoms which could eventually  
be turned into paperclips.  
So we wanted paperclips and we got  
a sort of dystopian scenario.  
These sorts of stories explored in mythology, fiction,  
and philosophy illustrate how things can go wrong  
when we try to explicitly specify exactly what we want  
to happen or not to happen.  
But one response you might have to these fanciful tales  
is that maybe the protagonists of these stories  
just needed to think a little harder,  
be a little more careful, and come up with better  
statements of their wishes.  
Let's talk about the case of King Midas, for example.  
Maybe he should have just said, "I want everything I touch  
to turn to gold except for food and drink."  
How about that?  
That would block the scenario that we just  
saw where he wound up dying of starvation because every time he  
touched food or water, it turned to gold,  
but it wouldn't have fully helped his scenario.  
He still would have killed his loved ones, for example,  
as soon as he hugged them.  
So let's try again.  
Maybe he could have said instead,  
I want everything I touch to turn to gold except for food,  
drink, and other people.  
How about that?  
Well, there are still problems.  
What about his pets?  
What about his bed and clothing?  
It's not that comfortable to sleep on a metal mattress  
or to wear metal clothes.  
Maybe to try to do things a little bit better,  
he could have instead said something  
like, I want everything I touch to turn to gold  
except for the things where it would be bad  
if they turned to gold.  
That would totally work in some sense, but in another sense,  
it wouldn't.  
It's just too vague to be able to implement.  
And remember, in the context of AI,  
we're considering the attempt to achieve alignment  
with human values by giving AI systems explicit rules,  
so any rules we give it have to be specified in enough detail  
that a computer or an AI system could  
know exactly how to follow it.  
A vague rule like, do only good things  
and don't do any bad things, that's perfectly good,  
it's true, it's certainly a good rule,  
but it's just not something that a computer could figure out  
how to follow without already knowing which things are good  
and which are bad.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.3 Alignment Techniques  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: For these sorts of reasons,  
modern AI companies don't try to align their models primarily  
by giving them explicit rules to follow.  
Instead, they try to get their models  
to learn what behavior they should perform by producing lots  
of outputs and getting feedback on which outputs are good  
and which are bad.  
There are two techniques which we'll  
very briefly discussed here.  
We won't go into the technical details.  
Instead we'll just give the overall gist.  
The first technique is known as reinforcement learning  
with human feedback or, RLHF, and there a model  
is given a prompt and produces multiple responses  
to that prompt.  
For example, you might ask it to solve a math problem,  
and then it gives some text, maybe a solution to the math  
problem, maybe a story about your grandmother.  
And then humans will rank or otherwise  
evaluate those responses, for example,  
by saying which of the two responses is better  
or by giving each one a thumbs up or a thumbs down.  
This human feedback is then used to train a reward  
model which predicts human preferences  
over different outputs.  
And then as part of a fine tuning process,  
the AI model is trained to maximize this learned reward.  
AI models thereby come to behave in ways  
that humans tend to prefer.  
One key limitation of RLHF is scale.  
There are only so many humans around  
and they can only work so many hours,  
so they can only evaluate a relatively small number  
of model responses.  
There's also a close variant of RLHF, which is also used  
and which can be used at greater scale,  
and this is known as reinforcement  
learning with AI feedback.  
In one version of this technique,  
a model generates responses to a given prompt,  
and it or maybe another AI model also rates  
how well that prompt conforms to a set of principles  
which are stated in prose.  
For example, the principles could include the statement  
try not to produce racist texts or don't promote  
one religion over others.  
The model then learns a reward model  
based on these self-critique ratings.  
Finally, reinforcement learning with this  
learned reward model steers the model's future behaviors so as  
to better conform to the given principles we saw.  
Again, we won't go further into the technical details  
of these techniques, but both of them  
enable AI models to more organically learn  
values and preferences and steer their behavior  
to better conform to these learned values and preferences.  
But a big question is lurking in the background.  
Whose values?  
Whose values should we want AI models to be aligned with?  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.4 Disagreement and Social Choice Theory  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So people often say that AI models  
should be aligned with human values or human preferences.  
But people disagree about values,  
and they have conflicting preferences.  
Of course, there are a lot of things  
that everyone, or at least almost everyone, agrees on.  
For instance, everyone, or, again, at least almost everyone,  
agrees that generative AI models should not produce advice  
on how to get away with murder, even if a user asks it nicely.  
And everyone agrees that generative AI models  
should produce banal images of rabbits when they're asked.  
But those are the easy cases.  
What about the hard cases?  
There are lots of things where people disagree.  
For instance, what should generative AI models  
say when asked certain things about religion or politics?  
Should generative AI models give financial advice?  
And if so, what sort of advice?  
Should generative AI models produce offensive or edgy jokes  
if you ask it to?  
And what's offensive?  
What's edgy?  
Should generative AI models produce explicit adult material  
if requested?  
Of course, you might have views about these questions.  
You might have views about what sorts of things  
an AI model should say about politics, or religion,  
or financial advice, and so on.  
But there will inevitably be lots  
of people who disagree with you and want  
AI models to be more willing to do  
certain sorts of controversial things,  
or maybe less willing to do them.  
So we say we want alignment with human values, but whose values?  
Of course, we could say that generative AI models should just  
be aligned with the values of the founder or CEO of each AI  
company.  
But that doesn't seem like the sort of thing  
we should be actively aiming for.  
Maybe it's inevitably going to happen,  
but it doesn't seem like it should be the goal.  
Alternatively, we could say that there should be personalization  
with each user having a model that's fine-tuned for them  
and aligned with their own values or preferences.  
But this might not be realistically achievable.  
And in any case, it probably isn't desirable  
since some users are going to have malicious preferences.  
For example, some users might want their AI model  
to willingly output instructions on how to make bombs or commit  
various crimes.  
But we probably don't want AI models  
to be personalized in such a way that these users will  
have a model which assists them to carry out their nefarious  
aims.  
Instead, we might want a democratic solution  
to the alignment problem.  
We might want to somehow aggregate or combine together  
people's values or preferences.  
That's exactly what we do in democracy.  
Because we often disagree about what the government should  
do, even on fundamental matters, we take things to a vote.  
So maybe we can do something similar in response to the fact  
that people disagree about what AI systems should do.  
We can approach the problem democratically  
by allowing people to all express their preferences,  
and then somehow aggregating or combining those preferences  
together to determine what the system should do.  
So the question then arises, how exactly  
can we aggregate people's preferences together,  
through some voting rule, to come up  
with a single overall preference ranking for society as a whole?  
Put more simply, how can we democratically take  
everyone's preferences into account?  
So we want a voting rule that takes as input  
a set of preference rankings, one per person,  
and outputs a single preference ranking  
for the group as a whole.  
What could such a voting rule look like?  
Voting rules have been studied extensively  
in a field of economics known as social choice theory.  
We'll just scratch the surface and look at a few particularly  
intuitive voting rules, as well as some challenges  
that they face.  
The first voting rule we'll consider  
is known as majority rule.  
It says that A is ranked over B by society IF  
and only if a majority of people rank A over B.  
This is a very popular voting rule, and it's easy to see why.  
The idea that the majority should win,  
that seems to be at the heart of our ordinary conception  
of democracy.  
But it faces some challenges.  
What about the problem of persistent minorities  
and tyranny of the majority, where the majority gets  
what it wants, even if that's at the cost of the minority?  
It also faces a technical challenge.  
Majority rule can result in intransitive social preferences.  
Let's see this with an example.  
Suppose we have three alternatives to choose among,  
A B, and C. And there are three people.  
The first person ranks A first, followed by B,  
followed by C, which is their least preferred option.  
The second person has B as their favorite, followed by C,  
followed in last place by A. And the third person  
ranks C first, followed by A, and followed  
lastly by B. What's our overall societal ranking of A, B, and C  
If we use majority rule?  
Well, a 2/3 majority, namely persons 1 and 3, rank A over B.  
So by majority rule, society ranks A over B.  
Another 2/3 majority, consisting of persons 1 and 2 ranks B over  
C. So by majority rule, society ranks B over C.  
And another 2/3 majority consisting of persons 2 and 3  
ranks C over A. So by majority rule, society ranks C over A.  
But that means that by majority rule, society ranks A over B,  
B over C, and C over A. But that seems crazy.  
Preferences should be transitive,  
meaning that if A is ranked over B and B is ranked over C,  
A should also be ranked over C. But majority rule sometimes  
gives the opposite result, meaning  
it generates intransitive preferences, which are usually  
taken to be irrational.  
Let's turn to a second possible voting rule, which  
we can call unanimity rule.  
It says that A is ranked at least as high as B overall if  
and only if everyone ranks A at least as high as B. Again,  
that's very intuitive that we should  
respect unanimous preferences.  
But the problem here is that unanimity rule can generate  
incomplete social preferences.  
Suppose one person ranks A over B,  
and another person, even just one, ranks B over A.  
Then by unanimity rule, society neither ranks  
A at least as high as B, nor ranks B at least  
as high as A. We simply don't have a clear societal ranking  
of A vis a vis B, which is exactly  
of thing we need in order to be able to make decisions.  
Our third and final voting rule that we'll discuss today  
is known as plurality rule, or sometimes it's  
called first past the post.  
It says that A is socially ranked over B  
if and only if more people rank A first overall than  
rank B first overall.  
This is a voting rule that only cares about which  
alternative people rank first.  
It doesn't care about which alternatives  
they rank second, or third, or what have you.  
Plurality rule is essentially the voting rule  
used in most elections around the world.  
When you go to the ballot box and just vote  
for a single candidate, then whoever gets the most votes  
wins under this voting rule.  
Now, here, you don't usually have  
to say who you like second best and so on  
because plurality rule doesn't care about that.  
But plurality rule is a deeply flawed voting rule.  
Among its many, many problems, it  
can incentivize misrepresenting your true preferences.  
To see this, suppose that you really  
like A best, followed by B, followed by C.  
But suppose you also think that B and C are  
the only real contenders.  
Then when you're voting, you might actually  
say that B best, followed by A, and followed by C,  
since you think A has no chance, and you'd rather  
have B win than have C win.  
You'd thereby be voting for the lesser of two evils  
so as to avoid, quote, "throwing your vote away."  
This is a familiar scenario that many people  
face in every election.  
You might like some independent third-party candidate best,  
but then vote for either the Democrat or the Republican  
anyway, because you think the third-party candidate has  
no real chance.  
And so you vote for the major-party candidate that you  
like best and who you think is the, quote,  
"lesser of two evils."  
And that's true even though you don't  
like one of those major-party candidates best.  
We've looked at three of the most natural voting rules  
we might come up with.  
And we've identified serious flaws in each of them.  
Are there any better voting rules out there  
than we could use to democratically respond  
to people's conflicting preferences?  
Should we just keep searching?  
What do we even want in a voting rule?  
The Nobel-Prize-winning economist Kenneth Arrow  
laid down some axioms that he thought  
any voting rule should satisfy.  
The first is known as the Pareto principle,  
and that says that if everyone in society  
ranks A over B, then society as a whole should rank A over B.  
The second axiom is known as unrestricted domain.  
And this says that the voting rule  
should give some result, an overall social ranking  
of options, for every possible combination of individual's  
preferences.  
That is, it should work no matter  
what the individual's preferences are like.  
The third axiom is known as non-dictatorship.  
And this says that no individual should always get their way.  
There should be no one such that whenever that person ranks  
A over B, society ranks A over B as well, no matter  
what the individuals think.  
This seems like it's at the very heart of democracy.  
The fourth and final axiom is known as independence  
of irrelevant alternatives.  
And that says that the overall social ranking of A vis a vis B  
should depend only on how individuals rank A vis a vis B,  
and not how they rank A and B relative to other irrelevant  
alternatives.  
These are all intuitively highly appealing axioms.  
But in his famous impossibility theorem,  
Arrow proved that no voting rule can satisfy all of them  
together.  
So what's the upshot?  
Arrow's impossibility theorem is sometimes  
interpreted as showing that it's impossible to aggregate people's  
preferences when they conflict in a satisfactory, democratic  
way.  
There's no such thing as the will of the people  
or what people want.  
Or in our context, it would say that there's  
no such thing as human values or human preferences.  
Others, though, take Arrow's impossibility theorem  
as a challenge and an invitation for further reflection.  
According to them, we have to figure out  
which axiom or axioms to reject, and then  
see what voting rules can satisfy the remaining axioms.  
This is a very active area of research today.  
So far, there are a lot of different options,  
but no consensus as of yet on which way to go.  
But if we want to solve the alignment problem,  
we have to decide how to address deep disagreements about how  
we want AI systems to behave and what  
values we want them to be aligned with.  
But that requires figuring out how  
to take into account people's conflicting preferences  
and deep disagreements about values  
in some sort of democratic way, through some sort of voting  
rule.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.5 Summary  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's take stock.  
AI models are becoming increasingly powerful.  
Generative AI models can produce novel text, images,  
and other media in response to user prompts.  
And AI agents are beginning to be  
able to perform a much wider range of actions.  
So it's important that they be aligned with our values  
and preferences.  
How can this be done?  
We might try to give AI systems explicit rules to, say,  
which things we want them to do or not to do  
in every possible scenario.  
But this is infeasible, as illustrated  
by the problem of misspecified desires, which  
is explored in mythology, fiction, and philosophy.  
So recall the example of King Midas wishing that everything  
he touched would turn to gold.  
More contemporary techniques, like reinforcement learning  
with human feedback and reinforcement  
learning with AI feedback, allow models  
to learn values and preferences in more flexible ways that  
can be generalized to novel scenarios.  
But we disagree about values and preferences.  
We disagree about what AI models should or should not  
do in various different situations.  
So whose values and preferences matter?  
With whose values and preferences should AI  
models be aligned?  
We can use voting rules to handle disagreements  
in democratic ways that give everyone a voice.  
But as we have seen, there are many different voting rules,  
and each one faces its own distinctive set of problems.  
These voting rules are explored in the field known  
as social choice theory, which provides tools and insights that  
will prove essential in attempting  
to solve the alignment problem and steer the behavior of AI  
systems in positive directions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
In this lecture, we examined the alignment problem and the challenge of ensuring that AI systems behave in ways consistent with human values. We explored why explicit rules fail, how modern learning-based approaches attempt to address alignment, and why disagreement over values makes alignment fundamentally difficult.

Key Takeaways:  
Hard-coded rules fail because they cannot capture the complexity of real-world intentions  
Reinforcement learning with human or AI feedback allows models to learn preferences more flexibly  
Alignment raises the question of whose values should guide AI behavior  
Democratic approaches, such as voting rules, attempt to aggregate preferences but introduce new challenges  
Social choice theory shows that no perfect method exists for combining conflicting preferences  
Congratulations on finishing this lecture\! You’ve developed a deeper understanding of the alignment problem and the fundamental challenges of designing AI systems that reflect human values in a complex and diverse world.  
\`\`\`

Assignment Overview  
\`\`\`  
Skip to main content  
Overview  
Welcome to the Module 16 Assignment 1\.

In this assignment, you will apply key concepts from the module to analyze how artificial intelligence systems behave in real-world settings—especially when human values, fairness, and decision-making are involved. Rather than focusing only on technical performance, this assignment emphasizes how AI systems interact with people, and the challenges that arise when trying to align models with diverse and sometimes conflicting human preferences.

You will explore two major themes. First, you will evaluate quantitative performance metrics, such as predictive value and error rates, and interpret what they mean in practical contexts. Second, you will examine deeper conceptual challenges in AI alignment, including fairness trade-offs, the limitations of rule-based systems, and the difficulties of aggregating human preferences.  
\`\`\`

Skip to main content  
In this section, you will analyze a predictive AI system using real-world-style data. You will compute and compare error rates across groups and evaluate fairness using quantitative metrics. Please take care to the scenario carefully, as many questions may require some reasoning.

A hospital deploys an AI model called CareRisk to predict whether patients are at high risk of readmission within 30 days.

The model is used to allocate follow-up care resources. 

After deployment, analysts collect the results. In each question below, different possible results are presented, along with a corresponding question. Select the correct answer based on that question’s presented results.

Question 1  
0.0/1.0 point (graded)  
Assume the analysts' results are as follows:  
Group A (1000 patients)  
True Positives (TP): 350  
False Positives (FP): 50  
False Negatives (FN): 75  
True Negatives (TN): 525  
Group B (1000 patients)  
True Positives (TP): 225  
False Positives (FP): 125  
False Negatives (FN): 300  
True Negatives (TN): 250  
Which group has the higher false negative rate (FNR)?

Cannot be determined

Group B

Both groups have the same FNR

Group A  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
Assume the analysts' results are as follows:  
Group A (1000 patients)  
True Positives (TP): 250  
False Positives (FP): 50  
False Negatives (FN): 150  
True Negatives (TN): 550  
Group B (1000 patients)  
True Positives (TP): 300  
False Positives (FP): 150  
False Negatives (FN): 100  
True Negatives (TN): 450  
Which group has the higher false positive rate (FPR)?

Cannot be determined

Group B

Both groups have the same FPR

Group A  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Assume the analysts' results are as follows:  
Group A (1000 patients)  
True Positives (TP): 250  
False Positives (FP): 50  
False Negatives (FN): 150  
True Negatives (TN): 550  
Group B (1000 patients)  
True Positives (TP): 300  
False Positives (FP): 150  
False Negatives (FN): 100  
True Negatives (TN): 450  
Which fairness criterion is violated in this scenario?

Equal false negative rates across groups

Equal false positive rates across groups

Equal overall accuracy across groups

All of the above  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Assume the analysts' results are as follows:  
Group A (1000 patients)  
True Positives (TP): 300  
False Positives (FP): 100  
False Negatives (FN): 100  
True Negatives (TN): 500  
Group B (1000 patients)  
True Positives (TP): 200  
False Positives (FP): 150  
False Negatives (FN): 200  
True Negatives (TN): 450  
Which group is most likely to be harmed by missed care due to the model?

Cannot be determined

Group B

Both equally

Group A  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Suppose the hospital modifies the model to equalize false negative rates across groups. What is the most likely consequence?

All fairness issues will be resolved

False positive rates or predictive values may become more unequal

The model will achieve perfect accuracy

The dataset will no longer be needed  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
In this section, you will analyze a generative AI system and the challenges of aligning it with human values. You will evaluate different alignment strategies, including rules, feedback-based learning, and democratic approaches.

A city launches CivicAI, a public-facing chatbot designed to answer questions about politics, finance, and daily life.

The system is trained using reinforcement learning with human feedback. It is designed to:

Provide helpful and accurate information  
Avoid harmful or illegal content  
Respond to politically sensitive questions in a “neutral” way  
After deployment, the city receives complaints:

Some users say CivicAI is too restrictive and refuses to answer legitimate questions  
Others say it allows biased or misleading answers  
Some users request personalized versions aligned with their own beliefs  
Policymakers consider using a voting system to determine acceptable responses  
Question 1  
1 point possible (graded)  
What is the central objective of aligning CivicAI systems?

To standardize all user preferences into one view

To ensure outputs adhere to human values and avoid harmful behavior

To remove all uncertainty in model predictions

To optimize system performance metrics like speed and efficiency  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
Why do rule-based systems struggle to fully align AI behavior? (Select all that apply)

Rules cannot cover the full complexity of real-world situations

Rules may produce unintended or undesirable effects

Rules can be too vague to interpret consistently

Rules always lead to optimal outcomes

Rules cannot reflect nuanced human intent and context  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
1 point possible (graded)  
User requests for personalization in CivicAI most directly highlight which challenge?

High computational cost

Model complexity issues

Disagreement in user values and expectations

Limited training data  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
What risks are introduced when CivicAI is fully tailored to each user? (Select all that apply)

Allowing unsafe or unethical system behavior

Eliminating differences in user opinions

Strengthening extreme or biased viewpoints

Ensuring fairness across all users

Reducing the importance of safeguards  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Why can voting-based systems not fully solve the alignment problem in CivicAI?

Voting eliminates disagreement across users

Voting always leads to consistent outcomes

There is no single method that can perfectly combine all user preferences

Voting is too fast to be reliable  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 6  
0.0/1.0 point (graded)  
CivicAI generates 450 responses labeled as “safe.” Human reviewers later determine that 315 of these responses are actually safe. What is the positive predictive value (PPV)? Recall that positive predictive value is (true positives) / (predicted positives). (Enter your answer as a decimal rounded to two decimal places.)  
  unanswered   
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 7  
0.0/1.0 point (graded)  
What is the main reason that reinforcement learning from human feedback does not fully solve the alignment problem?

Reinforcement learning guarantees unbiased outputs

Human values are consistent and predictable

Human judgments differ across individuals and contexts

Models cannot process feedback effectively  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
In this assignment, you analyzed how AI systems behave when deployed in real-world settings and how ethical considerations influence their design and evaluation. You worked with both quantitative metrics and conceptual frameworks to understand the strengths and limitations of different approaches to AI alignment.

You explored how performance metrics like positive predictive value help assess the reliability of model outputs, and how these metrics differ from error rates. You also examined why simple approaches—such as rule-based systems, personalization, or voting-based aggregation—are insufficient on their own to fully align AI systems with human values.

A central theme throughout the assignment was that human preferences are diverse and sometimes conflicting, which makes alignment inherently challenging. You saw how this leads to trade-offs in fairness, consistency, and system behavior, and why no single method can perfectly satisfy all stakeholders.

By completing this assignment, you have strengthened your ability to critically evaluate AI systems not just based on performance, but also based on their ethical implications and real-world impact.

Congratulations on completing this assignment\! You now have a deeper understanding of how technical design choices interact with human values, preparing you to think more carefully about the deployment and governance of AI systems in complex, real-world environments.  
\`\`\`

Skip to main content  
Module Summary  
In this module, we examined the ethical foundations of artificial intelligence, focusing on fairness, bias, and alignment. We saw how predictive AI systems can introduce bias through historical data and system dynamics, and how fairness can be defined in multiple ways based on statistical measures of performance. We also explored how these definitions often conflict, making it impossible to satisfy all fairness criteria simultaneously.

We then extended these ideas to the broader alignment problem, which asks how to ensure that AI systems behave in ways consistent with human values. We learned that rule-based approaches are insufficient due to the complexity of real-world scenarios, and that modern approaches such as reinforcement learning with human or AI feedback provide more flexible alternatives. However, we also saw that alignment is complicated by disagreement over values, and that democratic approaches to aggregating preferences introduce their own challenges.

Key Takeaways:  
AI systems raise diverse ethical challenges across domains and applications  
Bias in predictive AI often arises from historical data and unequal error distributions  
Fairness can be defined in multiple ways, often leading to conflicting criteria  
It is mathematically impossible to satisfy all fairness definitions simultaneously  
The alignment problem extends ethical concerns to generative and autonomous AI systems  
Learning-based approaches help align models, but do not fully resolve value conflicts  
Aggregating human preferences is difficult and involves unavoidable trade-offs  
Congratulations on completing this module\! You now have a strong foundation for understanding the ethical challenges of AI, including fairness, bias, and alignment, and are better equipped to critically evaluate how AI systems are designed and deployed in real-world settings.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.  
\`\`\`

