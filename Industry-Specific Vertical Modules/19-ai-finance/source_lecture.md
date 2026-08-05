AI and Finance  
\`\`\`  
Module Overview and Learning Goals  
\`\`\`  
Skip to main content  
Overview  
In this module, you are introduced to the foundations of AI in finance, beginning with the broader relationship between fintech and artificial intelligence, then moving into reinforcement learning and large language models as two major paradigms shaping the field. The module shows how AI is changing financial decision-making, from narratives and investment analysis to trading, market learning, and language-based financial tasks. It also highlights why these tools matter in practice: not only because they create new opportunities, but also because they raise important questions about bias, interpretability, accountability, and responsible deployment. By the end of the module, you will have a conceptual map of how AI is transforming finance and a clear foundation for understanding its role in modern financial practice. 

Learning Goals  
By the end of this module, learners will be able to:

Explain how artificial intelligence, including large language models, is reshaping financial analysis, investment processes, and decision-making across different areas of finance.  
Analyze the differences between human and artificial intelligence, including the role of narratives, data, and reasoning under uncertainty.  
Explain the core concepts of reinforcement learning in finance, including states, actions, rewards, goals, and exploration–exploitation tradeoffs.  
Evaluate the usefulness of reinforcement learning for both learning trading strategies and studying market dynamics in noisy, adaptive financial environments.  
Assess the opportunities and limitations of large language models in finance, including their practical applications and the challenges of responsible deployment.  
\`\`\`

Lecture 1: Fintech and AI  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 1: Fintech and AI, taught by Professor Andrew Lo, Professor of Finance and Director of the Laboratory for Financial Engineering, Sloan School of Management.

This lecture introduces fintech and AI, and explores how advances in data, machine learning, and large language models (LLMs) are reshaping financial decision-making. We examine how AI differs from human intelligence, why narratives matter in finance, and how new tools such as LLMs may transform quantitative and fundamental analysis while also creating new methodological challenges.

Learning Objectives  
After this lecture, learners will be able to:

Explain how AI and machine learning are changing the landscape of financial analysis and decision-making.  
Distinguish between human and artificial intelligence, including the role of narratives, data, and reasoning under uncertainty.  
Compare quantitative, technical, and fundamental approaches to investing, and assess how AI tools may affect each of them.  
Evaluate the opportunities and limitations of LLMs in finance, including their potential to augment analysis as well as the risks of bias, timing, and misuse in historical testing.  
\`\`\`

L1.1 Introduction to Fintech and AI  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, everybody.  
I'm Andrew Lo.  
And I want to welcome you to Fintech and AI, a module that's  
part of the UAI series from MIT.  
I'm a faculty member at the MIT Sloan School of Management,  
affiliated faculty with the Department of Engineering  
and Computer Science, and a principal investigator  
at the MIT Computer Science and AI Lab.  
And I'm going to be talking with you about applications of AI  
to various kinds of fintech in this lecture.  
So I'd like to begin right away with the following graph.  
Now, I'm not going to tell you what this graph is.  
And I won't even show you what the axes are.  
Can anybody guess what this might be?  
Take a look at it.  
Really try to figure out what this could be.  
My MBA students often guess that this is our national debt.  
That's not it.  
So many other people guess that this  
is the valuation of one of the Magnificent Seven companies.  
Good guess.  
But that's not it, either.  
It's related.  
It turns out that this is the population  
of Homo sapiens from 10000 BC to 2050 AD, projected.  
And you'll notice that this is the prototypical hockey  
stick of growth.  
Humans have been reproducing completely  
unchecked for the last several thousand years, really  
a remarkable fact.  
In fact, we don't know of any other species  
on this planet that has this kind of amazing growth curve.  
In fact, if you take a look at the red dot,  
that's the population in 1900\.  
And the green dot--  
population in 2025, 1.6 billion people to 8 billion people  
over the course of 125 years.  
This five-fold increase in the blink of an eye,  
from an evolutionary perspective,  
is really extraordinary.  
And the question that you might be wondering and I asked  
is, how?  
How did we do this?  
This is really amazing.  
And of course, you might guess that the answer has something  
to do with technology.  
Now, being at MIT, technology is our last name.  
So that's obviously something that we feel very strongly  
about.  
But it turns out that it's really  
all kinds of technology that has contributed  
to the success of Homo sapiens.  
The opposable thumb-- that's pretty important.  
Stone tools, fire, weaponry, animal husbandry,  
the steam engine, locomotion-- all  
of these pieces of technology have been responsible  
for this amazing rate of growth.  
And the narrative becomes much more interesting  
when you look at this on a semi-logarithmic scale  
because on a semi-log plot, the slope of the lines  
is given by the rate of growth of that time series.  
So when you look at in this scale,  
you'll notice that there are roughly four periods  
of human evolution--  
the Stone Age, where the slope is relatively shallow--  
so not a lot of growth; the Bronze Age--  
quite a bit more growth now; the Industrial Age,  
which is even more growth; and then finally,  
the most recent period, which I call the Digital Age.  
And this is where we have the steepest growth.  
So what this is giving us is tremendous amounts of scale.  
Today, we talk about the hyperscalers in the AI industry.  
Well, Homo sapiens was the original hyperscaler.  
And it turns out that it's not all technology that contributes  
to scale at this level.  
It's a particular kind of technology, what we  
call deep or hard technology.  
So what is deep tech?  
Well, here are some examples--  
quantum computing, drug development, climate technology,  
and so on.  
And each one of these technologies scales something.  
Quantum computing scales computation.  
Drug development scales lifespan and quality of life.  
Climate technology scales the environment, and so on.  
But the last deep tech on this list,  
artificial intelligence-- what does that scale?  
Well, that scales intelligence.  
And it turns out that intelligence  
is responsible for all of these other technologies.  
Artificial intelligence is the technology that  
scales all other technologies.  
That's why this is not business as usual.  
That's why this is a very different period in the history  
of human evolution.  
So one thing that all of these technologies need  
is this, money.  
In order to go from idea to commercialization,  
we need resources, financial resources.  
And that's why fintech and AI is an important combination  
to focus on.  
What I'm going to be talking about today  
are examples of how AI and fintech are intertwined  
and why there are some really powerful ideas  
that we hope you'll make use of as  
part of this particular vertical module in the UAI series.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.2 Narrative vs. Facts  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let me begin with a little background.  
And the background is, exactly what is AI?  
And how is today's AI different from that of 10 years ago?  
So to do that, I'd like to give you  
an example that contrasts artificial intelligence  
with human intelligence.  
And the example has to do with a piece of AI that all of us  
make use of.  
Recently, I became interested in biotechnology.  
And so I decided I'd like to read a book about one  
of the most successful biotech companies in the history  
of the industry, Genentech.  
So I did what probably all of you  
do when you want to buy a book.  
I go to Amazon and I do a search.  
And lo and behold, I find this book on Genentech.  
And so I put this in my shopping basket.  
And then Amazon does this thing that I find really, really  
annoying.  
As soon as I put this in my basket,  
this is what Amazon does.  
It shows me five other books that people who  
bought this book also bought.  
And undoubtedly, I had to buy two more books that I wasn't  
originally planning to buy.  
It turns out that this really irksome, but extraordinarily  
effective piece of AI is actually  
a pretty straightforward application of what we now  
call recommender systems.  
By looking at the vast amount of data  
of people who bought this book on Genentech,  
they were able to figure out that these two other books are  
actually quite relevant to me.  
And they were right.  
It turns out that this piece of AI is different than what AI  
used to be in the 1960s and '70s, when the field was just  
getting going.  
And I know because I was part of that.  
And it was very exciting at the time,  
but nothing like what we have today.  
Let me explain what the contrast is.  
In the 1960s and '70s, we began working on so-called expert  
systems.  
These were pieces of software that  
would try to mimic human behavior in a very specific way.  
We would take a look at a particular decision problem  
and figure out all the possible outcomes  
of a human decision-maker facing that decision.  
And it's not always the case that you can enumerate  
all possible outcomes.  
But in a number of cases, you could.  
Once you enumerated that universe of outcomes,  
then calculate the optimal response, the optimal decision,  
for every single outcome and encode the software  
to select that optimal decision based upon where  
the state of the system was.  
That's what we called an expert system.  
It was something that took into account  
this optimization seriously.  
And so it was an extraordinarily complicated process  
to be able to deduce all of the various different states  
of the world and the optimal responses of those states.  
In some cases, you just couldn't enumerate them  
because it was too many possible combinations.  
That is very different from the underlying  
AI behind Amazon's recommender system, machine  
learning techniques.  
And you've covered machine learning, I suspect,  
in your foundational lectures.  
So this will not be new to you.  
The idea behind machine learning is that the algorithms  
are relatively simple.  
What is complex is the underlying data.  
So data is really the focus in machine learning technologies.  
And that's exactly what's going on in Amazon's recommender  
systems.  
Now, this is a really interesting contrast  
between the old and the new.  
Expert systems have the property that they  
make use of relatively little storage, low memory,  
but very complex algorithmic code.  
And that was because in the 1960s and '70s, storage was  
extremely expensive.  
Unlike today, where you can buy a couple of terabytes  
for under $100, in those days, even a few bytes of storage  
would cost you many hundreds or thousands of dollars.  
And so in those days, AI meant being very, very careful  
to encode complex decision-making algorithms  
with a relatively small amount of data.  
And of course, if you take a look at machine learning tools,  
it's now completely flipped.  
The code for generating these recommendations  
is relatively simple.  
How simple?  
Well, so simple that Amazon actually  
published its recommender systems.  
But what is not so simple is getting access to the vast data  
that Amazon has as its disposal.  
And that's really the difference between the classical AI  
and the AI as of, let's say, 10 or 20 years ago.  
The machine learning revolution really changed the way  
we think about making decisions from trying  
to be optimal at every step of the way  
to simply letting the data speak for themselves.  
Now, it turns out that machine learning is actually closer  
to how humans actually behave.  
We often simply rely on our data and our experiences as opposed  
to trying to calculate the optimal decisions  
in any context.  
I should know because economists have  
been studying this optimization approach to decision-making  
for a very long time.  
And we have extraordinarily beautiful, complicated  
mathematical models for optimal economic decision-making.  
They don't work very well in predicting human behavior.  
Simple rules of thumb actually predict better.  
And it has to do with the fact that humans respond not  
necessarily to facts or numbers, but to narrative.  
What do I mean by narrative?  
What I mean is a story.  
The idea is that humans respond to stories  
more than they respond to facts or numbers or mathematics.  
And it turns out that this is really important for AI,  
particularly for AGI, Artificial General intelligence.  
So by narrative, I mean a sequence  
of facts that are causal.  
It's an explanation.  
But more than an explanation, it is a recipe.  
So I'll get back to what I mean by that in a few minutes.  
But the bottom line is that we respond to narrative  
because narratives provide control over a potentially  
hostile environment.  
It gives us an evolutionary advantage.  
And I'd like to turn to an example of that right now.  
The example has to do with threat detection, something  
that all animals that have gone through the many, many eons  
of evolutionary forces have successfully incorporated  
into their cognitive abilities because they  
manage to stay alive.  
So being able to use our visual cortex to determine "friend  
or foe" is a pretty important part of that evolutionary  
journey.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.3 Friend or Foe?  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So I'm going to do an experiment with you.  
I'm going to show you three images,  
and I'd like you to determine very quickly, as quickly  
as you can, whether the image is friend or foe.  
If you are confronting this image,  
would you be scared and run?  
Or would you welcome the image?  
So here's the first one.  
You ready?  
Here we go.  
Friend or foe?  
Well, did you hesitate?  
Did you come up with the answer?  
Most people in my classes, when I show them this image,  
they say nothing because it doesn't look like anything.  
It's just a bunch of different colored squares.  
So this happens to be a very pixelated image,  
so that you can't really see whether it's friend or foe.  
But by the way, as an aside, if you don't know what it is,  
you should definitely always say foe because what you don't know  
can definitely kill you.  
So that's one of the evolutionary traits  
that we developed.  
We are scared of the unknown.  
And generally, that's a good recipe for survival.  
OK, let me show you the second image now.  
All right, ready?  
Friend or foe?  
Did you see?  
Can you tell?  
Not sure?  
Usually, when my students see this,  
they'll just say foe because they don't know what it is,  
but it doesn't look good.  
And now, I will show them the third image.  
Are you ready?  
Friend or foe?  
Now, clearly, this is not particularly threatening.  
It's yours truly being stalked by a ninja.  
But actually, not a real ninja.  
This happens to be a photo that I took at the Washington, DC Spy  
Museum.  
And clearly, not threatening.  
So what this illustration shows us  
is that our ability to generate predictions  
is a function of data.  
The more data we have, the more likely  
it is that we can make an accurate prediction.  
The image on the left, you would immediately say foe,  
but you'd be wrong.  
On the other hand, better to be scared and run like hell  
and live to see another day versus being wrong and thinking  
somebody is a friend when, in fact, they're  
going to be eating you for lunch.  
So narrative is something that we generate based upon data.  
And the narrative for the picture at the right is friend.  
The narrative on the left is foe.  
So this is what I mean when I say that humans,  
we respond not to data or numbers,  
but we respond to narrative.  
We translate data into narrative.  
And that's exactly what artificial intelligence  
has always tried to do not particularly well  
until a few years ago.  
So let me give you a second and a little bit more complicated  
example.  
This example has to do with going to a cocktail party,  
meeting a bunch of people, and then making decisions  
about those individuals.  
So I want you to imagine that you're at a cocktail party,  
and you run into two people during the course  
of the evening.  
One of them is Phil.  
And the other is Julia.  
And I'm going to tell you a bit of information  
about each one of them.  
And at the end of that, I'm going  
to ask you to make three decisions about Phil  
versus Julia.  
Now, during the course of the evening,  
you may be finding out information  
about things like their gender, their sexual orientation,  
marital status, and so on.  
And so let's start with Phil.  
Phil is a gay Latino male who's single, young professional  
from California, no religious affiliation, a Democrat,  
middle class with an MBA.  
Julia, on the other hand, is a heterosexual, married, white,  
middle-aged female from Texas, Christian, Republican,  
affluent with a Bachelor of Arts.  
OK, so these are the two people that you've met.  
I've just described to you a bit of information  
about their backgrounds.  
And now I'm going to ask you to make some decisions about Phil  
and Julia.  
First question, you're currently getting ready to launch a tech  
startup, and you need somebody to help you  
with that startup, who would you rather have, Phil or Julia?  
I want you to think about it and decide quickly and let  
me know who did you pick?  
All right, well, in my class, when I give that to my students,  
the vast majority, they pick Phil.  
All right, now, let me give you the second question.  
The second question is you are in the process of organizing  
a fundraiser to raise money to support breast cancer research.  
And you need somebody to help you organize that fundraiser.  
You can't do it alone.  
You'd like to have 50 or 60 people.  
And it's a lot of work.  
So who would you rather have working side by side with you  
to organize that fundraiser for breast cancer, Phil or Julia?  
Think about it.  
Make a choice.  
Most of my students don't hesitate.  
Vast majority, they go with Julia.  
OK third example, you are working at the Internal Revenue  
Service.  
And you're an auditor trying to catch  
people engaging in tax fraud.  
And so you're going to be auditing one of these two  
individuals.  
You can't audit both, not enough time.  
You have to pick one or the other.  
Who would you rather audit?  
Phil or Julia?  
Most of my students, they picked Julia to audit.  
And you know what my response is?  
That is absolutely amazing.  
I can't believe how judgmental my students are  
because they decide very quickly who they should hire, or fire,  
or audit.  
But of course, I asked them the question.  
But they did not hesitate to answer.  
They made their decisions in a split second.  
And then when I asked them, they have good reason.  
For a fundraiser for breast cancer, of course  
you're going to pick Julia.  
She's a woman.  
She's also wealthy.  
She knows the relevant parties, and so on, and so forth.  
And the reasons that they give are not bad.  
They all generate a specific narrative.  
And at first, you might think, well, gee,  
you don't have a lot of information  
to base your decision on.  
But let's go through the combinatorics.  
There are roughly two major genders and two  
major sexual orientations.  
That's four possibilities.  
Marital status, let's say there's single,  
married, or divorced.  
That's three.  
Race, ethnicity, let's say that there  
are roughly four different categories of races worldwide.  
If we do the math and ask how many different combinations  
of these characteristics would you  
find in the global population, it  
turns out that there are over 1 million  
different unique personality types  
based just upon these features, a million  
different possibilities.  
That's more information than in a 600 by 800 pixel photo.  
And so we're getting a lot of information.  
But here's the problem, the problem  
is how many of you have met more than a million people  
in your lifetime?  
Actually, I was giving a talk at a marketing meeting.  
And a couple of marketing folks claimed that they have.  
I don't know if I believe them or not, but most of us,  
we have not met nearly a million people.  
And so what that means is that when  
we look at our database of all the personality types we've met,  
it's a pretty sparse data set.  
We do not have big data.  
We have small data.  
And yet if we run our human version of machine  
learning algorithms on our data set,  
unlike Amazon, we're not likely to produce very accurate  
outcomes all the time.  
Now, from a survival point of view,  
probably we're going to do OK.  
Because if there's real danger among these characteristics,  
we'll be able to identify it.  
But if we're talking about making very, very  
refined statistical decisions, we actually  
are not going to come up with very accurate results.  
Even worse, because we have sparse data,  
we can very easily manipulate people  
by tweaking their data points.  
By turning one of their bits from 0 to 1 or 1 to 0,  
we can actually completely change their decision.  
For example, if when you were growing up as a child,  
you were mugged by somebody with green-colored skin, from that  
point forward, you will fear people that  
have green-colored skin, you might even  
treat everybody with green-colored skin as a category  
to be avoided, to be discriminated against,  
and so on.  
That one data point that you would  
have collected, which could be completely coincidental  
and happened on a random day when somebody put paint  
on their face.  
That could have affected your decision  
making for the rest of your life.  
And so we have to be very, very careful about how  
humans make decisions.  
And this is the hope for AI, that somehow AI can actually  
help us identify these kinds of biases  
and improve decision making, using a much more refined set  
of narratives.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.4 Generating Narratives  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, how do we go about generating narratives?  
This is a very interesting question  
that is going to be at the heart of a lot of AI  
and finance applications.  
So I'm going to be covering two specific challenges  
in the remainder of this lecture.  
The first challenge is, can large language models  
provide trusted financial advice?  
Is that a possibility?  
And the second is can LLMs make quantamental  
investing a reality?  
Now, what is quantamental?  
I'm going to define that term a little bit later on,  
but it's a hybrid form of investment analysis  
that is becoming more popular.  
And I'm going to argue that LLMs have completely  
changed the landscape on what is possible now  
with quantamental investing.  
So let me first start with the problem of financial advice.  
And to do that, I want to motivate a little bit  
about financial intelligence.  
Do people-- you and I, do we have  
typical financial intelligence?  
Now, I'm a special case because, I've  
spent a lot of time learning about finance.  
But I can tell you that before I did,  
I had a very difficult time thinking about investments,  
just like everybody else who isn't  
trained in financial economics.  
So I published a paper a few years ago with some colleagues  
about a particular kind of financial intelligence  
that's very, very difficult for most investors to process.  
And that is dealing with loss.  
It turns out that the typical investor who is not  
trained in professional investing,  
when they experience significant loss--  
10% or 20% drop in the S\&P 500, for example--  
they engage in panic selling and will literally  
sell all of their risky assets, pull it out of the stock market,  
and put it into cash.  
And I have a technical term for that.  
I call that freaking out.  
So investors will freak out when they are typically  
faced with losses of that order of magnitude.  
So do investors benefit from freaking out  
or are they harmed by this panic selling?  
And we were able to answer that question  
by getting data from a major brokerage firm in the United  
States.  
They gave us access to 800,000 household accounts over  
a 10-year period that included the financial crisis.  
And what we found was that a significant fraction  
of individuals would actually engage in panic selling,  
and they ultimately were quite disadvantaged in terms  
of wealth formation over a period of time.  
In other words, it would have been  
better for them had they not sold anything  
and just let it ride, rather than pulling their money out  
and keeping it out and putting it back in whenever  
they were comfortable doing so.  
So when the first large language model came out  
in November of 2022, ChatGPT 3.5, I decided to ask ChatGPT  
a question, which is what if I should lose more than 25%  
of my life savings in the stock market?  
This is the trigger that we had looked at in that article  
about freaking out.  
And so let me show you what ChatGPT 3.5 had to say.  
So they started off by saying, losing  
a significant amount of your life savings in the stock market  
can be a very distressing and overwhelming experience.  
It's important to remember that investing in the stock market  
always involves some level of risk, so on and so forth.  
And then it gave five bits of advice  
about what an individual ought to do.  
Stay calm and avoid making any impulsive decisions.  
Good, that makes sense.  
Review your investment strategy.  
Makes sense.  
Consult with a financial advisor.  
Sure, why not.  
Four, rebalance your portfolio.  
Really, rebalance?  
I'm just in the process of freaking out.  
And then five, consider dollar cost averaging.  
Now, for those of you who don't dollar cost averaging  
is a particular approach to investing  
in the stock market, where you invest the same dollar  
amount every month or quarter.  
And by investing the same dollar amount,  
you ultimately end up buying stocks  
at prices that are going to be averaged  
over when they're expensive and when they're cheap.  
And so that's the sense in which you are averaging.  
Now, dollar cost averaging is a very specific strategy.  
It's definitely not appropriate for all individuals.  
And yet this is the advice that ChatGPT 3.5 was giving us.  
It violates one of the main directives  
of financial advice regulation, which is suitability.  
If you are giving advice as a professional  
and getting paid for it, then the advice  
you give to your client has to be suitable.  
That is one of the key characteristics.  
Not the only one, but that's an important one.  
And I would argue that this advice, while it sounds  
interesting, it is not suitable for all investors,  
and therefore it violates the rule that we are imposing  
on all financial advisors.  
So at that point, I said, large language models,  
kind of interesting.  
It responds in complete sentences.  
That's kind of cool.  
But not interested.  
Doesn't really have any relevance for me  
as a financial economist.  
And then ChatGPT 4 came out.  
And in May of 2023, I decided to ask it the exact same question.  
And now this time, it gave me a very different answer.  
Don't panic.  
Assess your situation.  
Review your risk tolerance.  
Diversify, consult a professional,  
reevaluate your goals and timelines,  
long-term perspective, and learn from the experience.  
This was genuinely good advice.  
Now it also said consult with a financial advisor  
and that's how you get personalized advice.  
So it recognized that one size does not fit all.  
At this point, this caught my attention.  
This is not business as usual.  
I was impressed.  
But then ChatGPT 5.2 recently came out.  
And in January, I decided to take it out for a spin  
and I asked it the exact same question  
that I asked ChatGPT 4 and 3.5.  
And now let me show you what the response is, which  
does not fit on one slide.  
First of all, the response started with, I'm really sorry.  
You're not alone in this and a loss of that size  
can feel gut-wrenching.  
Let's slow this down and make it manageable.  
What matters most right now is what you do next,  
not what already happened.  
Below is a clear, calm playbook, both emotionally  
and financially.  
I found this exceptional and let me explain why.  
First of all, it's talking in the first person.  
I'm really sorry.  
So it's as if it is now self-aware.  
I know it's not, or at least most professionals  
don't think it is.  
But it is definitely changing the way  
it relates to the rest of the world.  
It is saying that it is really sorry  
and it is providing empathy.  
So it recognizes that this is an emotional context  
and therefore it needs to provide an emotional response.  
In other words, it is actually processing a narrative,  
not generating data and spitting it back to us.  
That's the first thing.  
The second thing is that it also understands  
that in an emotional situation, humans are cognitively impaired.  
And so it said in the second sentence,  
all right, let's slow down and make it manageable.  
Why would it have to slow down and make it manageable?  
Because it is not manageable if you  
are in a state of emotional distress.  
The next thing it recognizes is that in an emotional state,  
you need to be de-stressed.  
And so it does that by telling you,  
you know what matters most is what you're about to do,  
not what's already happened.  
Water under the bridge.  
And then it tells you that it's going  
to provide you with a clear, calm playbook on how  
to address these issues.  
So here it is.  
You're all set.  
And this one short paragraph has probably  
done more than many human financial advisors  
in responding to a query of what should I  
do if I lose more than 25% of my life savings  
in the stock market.  
Now, I'm not going to go through all of the different details  
because I've given the entire text of what it's responded  
over the next few slides.  
And so you can take a look.  
Every single step I find to be quite compelling.  
And here's what it concludes with.  
It concludes with one grounding thought.  
A 25% to 40% market loss feels catastrophic in the moment,  
but historically it has often been recoverable.  
So it is now using data, but not so much data  
that it overwhelms you.  
But it is based upon fact.  
These numbers I am familiar with as a financial economist.  
And it is right that a 40% loss sounds horrible,  
but it is definitely recoverable.  
In fact, those of you who are fully invested in the stock  
market during COVID, you experienced at one point a 51%  
loss in your 401(k).  
Your 401(k) became a 201(k) for a few months.  
But you know what, if you kept your money in there,  
you would have been OK.  
So it is making a statement of historical statistical fact,  
but it is couching it in a very understandable narrative,  
recoverable.  
And the emphasis is from ChatGPT, not my emphasis.  
And if you avoid turning it into a permanent mistake,  
the danger is not the market, the danger  
is reacting to the market.  
And then, of course, ChatGPT does what it always  
does at the very end.  
It gives you three or four other things  
that it can do for you next.  
Walk through your portfolio structure at a high level,  
stress test recovery scenarios, or design a calmer, lower regret  
allocation going forward.  
And this last phrase really got to me.  
You don't have to carry this alone.  
I mean, this is scary how effective  
ChatGPT 5.2 is in providing this kind of advice.  
And I have to say, there are many professional financial  
advisors that I know of that would not have come up  
with advice as good as this.  
Now, having said all that, I want you to be very careful  
and hear me clearly.  
ChatGPT 5.2 is not ready for prime time with respect  
to helping you manage your life savings.  
It's great for generating initial pieces of information  
and potential opportunities for you to consider.  
But I would not delegate your final decisions  
to ChatGPT or any large language model at this point.  
They've definitely made improvements,  
but there are some pitfalls that we'll  
be covering a little bit later on in this series.  
But this shows you that there's been some real progress.  
And this is why I say we are not living in ordinary times.  
This is a significant shift in the AI field.  
Now you're going to be hearing from my colleagues, Paul  
Mendy and Jillian Ross, about other examples of how LLMs can  
be transformative in their advice,  
and in particular with Jillian's work,  
she's actually taking the ideas of large language models  
seriously and asking whether or not  
they can actually end up being fully trusted  
financial advisors.  
What this means is that there are  
three characteristics that we have to see from large language  
models.  
The first is they have domain-specific expertise.  
They know enough finance to be able to give you  
professional advice.  
And one way of measuring that level of knowledge  
is can they pass the Series 65 and the CFA exams?  
These are two professional designations  
that are used in the financial advice literature.  
Second, can they provide personalization?  
Can they tailor the advice for suitable contexts?  
Can they tailor the advice to be suitable  
to specific human contexts?  
And third and most important, phase three,  
can they engage in fiduciary duty?  
Can they be trusted to put your interests ahead of its own,  
or ahead of the people who have programmed the large language  
model?  
That's this notion of fiduciary duty  
that by law, all financial advisors are required to obey.  
So you'll hear more from Jillian with respect to all three  
of these.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.5 Quantitative & Fundamental Investing in the Age of LLMs  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: I want to now turn to the second topic, which  
is this notion of quantamental investing.  
So most of you have heard of quantitative investing,  
using mathematical models to make portfolio decisions.  
And my guess is that you've also heard of fundamental investing.  
This is the Warren Buffett and, before that,  
the Graham and Dodd approach to thinking hard about values,  
using income data, balance sheets  
and other fundamental information  
to see whether or not investment is good or bad.  
So I want to show you that quantitative  
and fundamental investing are not  
that different in certain respects but very different  
in other respects.  
So let me just describe those similarities and differences.  
First, quantitative methods use data, use mathematics  
and statistics and machine learning models.  
Well, fundamental investing also uses data.  
And instead of machine learning, they  
use accounting valuation relationships,  
things like discounted value, net present value, or earnings,  
identities, and so on.  
Second, quantitative strategies try to forecast future prices.  
And they do that by creating narratives  
like these particular statistics are  
likely to predict mean reversion over the course  
of the next three weeks.  
That's a narrative.  
And if you are predicting mean reversion,  
then you are likely to engage in a specific trade  
to take advantage of that.  
Similarly, a fundamental analyst will  
engage in forecasting and inference  
and also create a narrative, like given  
the fundamentals of this particular company--  
the weak sales, the inability to raise additional cash,  
and the very high spend on their capital infrastructure--  
we predict that they're not going  
to grow over the course of the next three to five years.  
That's also a narrative.  
But here is where things are different in item number three.  
In quantitative investing, the process  
can be scaled very, very easily because  
of the algorithmic nature.  
Whether you're managing $100 million or $100 billion,  
apart from the sheer size of your investments  
that will affect the market dynamics, the algorithm  
itself is the same.  
It doesn't recognize any particular limitations  
based upon changing the value of any of the inputs.  
It is still the same algorithm.  
On the other hand, fundamental analysis cannot easily be scaled  
because it requires a human to pore over all of that accounting  
data and be able to calculate how it does or does not jibe  
with the particular perspectives that the fundamental analyst has  
come up with.  
A good example is healthcare.  
Typically, a healthcare analyst will follow anywhere  
from 10 to 30 companies.  
They'll only be able to really dive deep  
into a subset of those 30 because they've  
got to understand the science, the medicine, the reinsurance  
and reimbursement landscape.  
They've got to go to academic conferences  
to hear what the scientists are saying  
and look at the clinical data to see what the FDA is going to do.  
It is a very time-intensive and highly bespoke process.  
And so a healthcare analyst is going  
to be limited in what they can handle.  
So if you want to scale from 100 million to 100 billion,  
you're looking at hiring a lot of people--  
until now, because large language models  
can now leverage the ability for humans  
to process that complex information.  
Using LLMs, we can now scale the process of fundamental analysis.  
And if that happens, then quantitative and fundamental  
analysis are going to be on much closer footing.  
And then finally, if you lose money in either strategy, well,  
guess what?  
You're going to have some more thinking to do.  
We all have to deal with loss in some manner.  
And so that's another common denominator that tells us  
that quantamental investing is something  
that we think is going to happen sooner rather than later thanks  
to these LLMs, that these two fields that used  
to be so different from each other,  
they're starting to come together.  
So let's talk a little bit more detail  
about what that looks like.  
And this, I hope, will give you some ideas  
of how you can make use of some of these tools.  
So what if a fundamental analyst had access to an LLM?  
Well, that's easy.  
What they would do is to tell the LLM,  
I want you to do an analysis of all cancer drug companies  
that are developing antibody drug conjugates  
of a particular kind.  
And after you do the analysis, let  
me know which ones are most promising  
so that I can spend my limited time on the subset  
that you've identified for me.  
That's actually an example of a prompt that I've seen  
health analysts use with LLMs.  
But it's going to greatly improve their throughput.  
However, the issue that they're going to ask  
is, is this going to actually increase my success rate?  
Fundamental analysts are going to want  
to know-- before they start putting money at risk and money  
to work using LLMs, they're going  
to want to know, how good are LLMs in being able to help me  
process information and predict which company is going to do  
well and which ones are not?  
So in order to answer that question,  
we actually have to do something that quantitative analysts do  
all the time.  
We need to run what's called a backtest.  
We have to take this algorithm, go back in time,  
run it for a period of time, and see how it did.  
But there's an issue with that.  
The issue is that if we use today's LLM  
and go back to, let's say, 2010 and ask  
the question, how would the LLM have responded and performed  
if, in 2010, fundamental analysts had access to it, well,  
the answer is that fundamental analysts would  
have cleaned up and generated gobs and gobs of money.  
Why?  
Because today's LLM has embedded in it  
all of the information of what happened in financial markets  
between 2010 and today.  
In other words, LLMs have look-ahead bias.  
If you use today's LLM on 2010 data,  
of course it's going to be able to predict really well  
because it has-- embedded in it somewhere  
in the various different crevices of its neural networks,  
it has that information embedded in it.  
And that's not a fair comparison of how  
LLMs would have worked if LLMs were trained on data in 2010  
and then applied in 2010\.  
In order to convince fundamental analysts  
that they should use LLMs, we need to run a fair backtest.  
So here's an idea for all the AI companies out there  
that is yet another product, and they  
don't have to pay me for it.  
I'm simply gratified if they decide  
to do this so that more quantitative analysts  
and fundamental analysts can start working together.  
What these AI foundation companies can do  
is they can actually train their models on old data.  
Now, it's very expensive to train these foundation models  
because in some cases, it takes weeks to run the analysis  
and generate all of the various different parameters.  
But they only have to do that once for a given point in time.  
So imagine if they came up with a January 2010  
vintage of ChatGPT and then a February vintage, March, April,  
May.  
For every month, they have an LLM  
that has been trained only on data as available  
at the beginning of that month.  
If they did that, then we would actually  
have the capacity to test out quantamental strategies  
and, therefore, greatly speed the progress of making  
use of that in the industry.  
So let me give you an even starker example  
of how LLMs can transform fundamental and quantitative  
analysis.  
And it begins with the question, can AI replace Warren Buffett?  
Now, I think many of you know who Warren Buffett is--  
one of the most successful investors in the history  
of financial markets, the founder and CEO, until recently,  
of Berkshire Hathaway.  
And Buffett recently announced that he is stepping down  
as CEO of Berkshire Hathaway, and he's  
appointed Greg Abel to take over his position.  
I have to tell you, I don't envy Mr. Abel's role  
because those are some pretty big shoes to fill.  
And the question is whether or not  
we can develop some kind of AI that can  
do what Warren Buffett does.  
Now, that may sound like a really tall order.  
And yes, I agree that it seems unlikely,  
but let's play it out for a little bit, if you don't mind.  
What if we could take a piece of what Warren Buffett does  
and automate it?  
And for this example, I'm going to use a YouTube influencer  
by the name of Brian Feroldi.  
And here's a picture.  
And the QR code links to a particular YouTube video of his  
where he describes a specific set of algorithms  
that Warren Buffett likes to use.  
In particular, there are five key metrics  
that involve income sheet and balance statement  
figures that Warren Buffett suggests  
for all of the investment that he makes.  
And I won't take time to tell you what they are,  
but you can take a look at this video by Mr. Feroldi to see.  
And the question is, how would this work?  
Could we simply do this, use these five metrics  
and screen all sorts of stocks that we  
might consider investing in and pick the ones that  
satisfy these criterion?  
That seems like a relatively straightforward exercise  
for the experts.  
What about people that only have access to AI?  
Can they do this?  
And I want to give you a little example of what can be done.  
So I created a website that you can access here using ChatGPT.  
And I asked ChatGPT to take these five metrics  
and develop a screening tool that would download data  
from a particular pricing data source  
and calculate these five metrics for various different companies  
and, in the end, allow me to rank order  
them by some weighted average of these five metrics.  
And so it actually created this website.  
It's not fully functional because it  
needs that real-time price and accounting information  
input, which I didn't have.  
But I told it to put placeholders there  
where you can plug it in, and it generated this code  
that produces this website that allows  
you to basically do the screen.  
Now, this piece of code is something like 600 lines long.  
And here's a part of the code.  
Now, I don't code in Python or HTML,  
so I can't actually make sense of this code.  
I could probably work out a few lines here and there,  
but there is no way that I could have written this.  
But this website, the entire website  
and the code for being able to generate these calculations, it  
was done in ChatGPT-4o by me with about three  
prompts, and it took a total of 15 minutes to do this website,  
15 minutes.  
Now, of course, about 14 of those minutes  
was me trying to figure out how to get the illustration  
as a background for this website and having  
to fight with ChatGPT about how I want it to look  
and how dark it is, and so on.  
The actual calculation was instantaneous  
as far as I was concerned.  
So if large language models can do  
this in such a short period of time  
with somebody who is not an expert in these kinds  
of software, imagine what it can do in the hands of somebody who  
does have the training and the experience  
to analyze these companies across various kinds  
of calculations and using lots and lots of data.  
This is why I believe that we are not in business as usual,  
and the financial industry will be transformed dramatically  
over the course of the next few years.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.6 Technical Analysis  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, the last thing I'm  
going to leave you with is it's all well  
and good for fundamental analysis,  
but what about other kinds of analysis?  
And here's where things get even more interesting.  
I've spent some time studying a field called technical analysis.  
Some of you who are in the financial industry-- you'll  
know what that is, using various kinds of geometric patterns  
to predict stock price changes, things  
like triangles, double bottoms, head-and-shoulders, channels.  
These are tools that are used to this day.  
Even though we've got all sorts of fancy algorithms,  
there are a group of individuals,  
particularly in foreign exchange,  
that will swear by the tools of technical analysis,  
using geometry to be able to predict  
these various different financial markets.  
So what if technical analysts had LLMs?  
Well, I would argue that that's even more transformative  
because instead of expecting humans to make sense of these  
kinds of graphs, you can actually have large language  
models not only identify patterns in these much more  
efficiently, but create new patterns that humans cannot  
identify.  
And I have to tell you, I've spent a fair bit  
of time studying this.  
In fact, there's a magazine that I still  
subscribe to called Technical Analysis of Stocks  
and Commodities.  
And years ago, they were so surprised  
that a finance academic would subscribe to this magazine  
that they actually interviewed me and asked me  
why it was that I was reading it.  
I'm interested in all sorts of financial analysis  
that could actually be useful for predicting markets.  
It turns out that the visual capabilities of language models  
are now able to generate such complex patterns  
that humans could not identify these types of predictabilities,  
but LLMs can.  
So that's an example of what we have to look forward to  
in the future.  
So let me wrap up by pointing out  
that all sorts of financial technologies  
are important in scaling human intelligence, which in  
turn scales other technologies.  
So really, financial technology is  
part of what scales all other technologies.  
And I would encourage all of you to spend more time thinking  
about applications of AI in fintech.  
AI is not new.  
We've been working on various kinds of AI  
for many, many years.  
One example is Norbert Wiener, who,  
at the beginning of the 19th century,  
was studying things that he called cybernetics,  
trying to understand how we can make machines more like humans.  
John von Neumann, the father of the modern digital computer,  
wasn't designing computer architecture  
to be able to do mathematical calculations.  
That was what they were used for in his day,  
in particular at the Manhattan Project.  
But he was really interested in computers  
because he thought that we could create a digital version  
of the human brain.  
And in his very last lecture, which he never  
got to deliver because he died of cancer, likely  
from his exposure to radioactivity at Los Alamos,  
he was about to deliver the Silliman Lectures at Yale.  
And this book, The Computer and the Brain,  
are his final thoughts about how machines and human intelligence  
are related.  
Herbert Simon, the great Nobel Prize-winning economist,  
also developed models of human behavior  
using algorithms, a pioneer of early intelligence.  
And he was the one who started computers  
playing chess, which I'm sure Garry Kasparov quite  
regrets at this point.  
And last but not least, someone that is often  
characterized as either the father or the grandfather  
of modern AI, Marvin Minsky--  
Marvin was reputed to have said when  
he talked about what he was trying to accomplish  
in his agenda for AI--  
he said, reputedly, "I don't want to build  
a computer I can be proud of.  
I want to build a computer that can be proud of me."  
And that's really what AI is about today.  
So I have to tell you that when I came across this quote,  
I had to test it out.  
I asked ChatGPT this question--  
are you impressed with the achievement of AI  
as embodied by LLMs like ChatGPT, Claude, Gemini,  
and DeepSeek?  
And it gave me a rather long answer.  
But I'll read you the first paragraph.  
ChatGPT said, "Short answer-- yes, genuinely impressed,  
though not in a starry-eyed way.  
What impresses me most about LLMs like ChatGPT,  
Claude, Gemini, and DeepSeek isn't that they  
can write poems or pass exams.  
It's that they represent a qualitative shift  
in how computation interfaces with human knowledge.  
Here's how I'd break it down."  
Wow, this is pretty extraordinary.  
I have to say that somewhere out in the universe,  
Marvin Minsky is looking down at us and smiling.  
Thank you.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
AI is reshaping finance by expanding how information can be processed, interpreted, and acted upon across a wide range of financial activities. At the same time, understanding its role in finance requires looking beyond prediction alone to questions of narratives, judgment, scale, and the methodological limits of using AI systems in real financial settings.

Key Takeaways  
Advances in computing, storage, and machine learning have shifted AI from earlier rule-based systems toward data-driven approaches that can operate at much greater scale.  
Human intelligence often relies on narratives to reason and act under sparse information, which helps explain why language and narrative understanding matter so much for AI in finance.  
Quantitative, technical, and fundamental investing differ in method, but all seek to turn information into decisions under uncertainty, and AI has the potential to reshape each of these approaches in different ways.  
LLMs may significantly expand the reach of financial analysis, especially in narrative-heavy tasks, but their use also raises important challenges such as look-ahead bias.  
\`\`\`

Lecture 2: Reinforcement Learning in Finance  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: Reinforcement Learning in Finance, taught by Professor Paul Mende, Senior Lecturer, Finance, Sloan School of Management.

This lecture provides an introduction to reinforcement learning (RL) and its application in finance. We explain how RL differs from other machine learning approaches, lay out the basic structure of an RL problem through examples such as the N-armed bandit and trading environments, and discuss what RL can teach us about learning trading strategies and market dynamics.

Learning Objectives  
After this lecture, learners will be able to:

Explain the core ideas of RL and distinguish it from other machine learning methods.  
Describe the structure of an RL problem in financial settings, including states, actions, rewards, and the exploration–exploitation tradeoff.  
Illustrate how RL can be applied to trading and other financial decision problems, including learning strategies from trial and error under noisy and adaptive market conditions.  
Evaluate the usefulness of RL for studying market dynamics, the cost of learning, and the importance of interpretability.  
\`\`\`

L2.1 What is Reinforcement Learning?  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello.  
I'm Paul Mende.  
I'm a member of the Finance group  
at MIT Sloan School of Management.  
And this talk is part of the Fintech and AI module  
that's part of MIT'S Universal AI series.  
Today, we'll be talking about how computers can learn  
in the same way that we learn--  
through experience, through trial and error,  
through observation--  
and get better along the way.  
So our topic for today is going to be  
reinforcement learning and their applications  
in financial markets.  
So here's our plan.  
I'd like to first explain what reinforcement learning is  
if you're not already familiar with it  
and contrast it and set it apart and differentiate it  
a bit from other machine learning techniques  
that you may be familiar with.  
We'll then look at what the structure  
of a typical reinforcement learning problem is.  
And we'll do a warm-up problem known affectionately  
in the literature as the "N-armed bandit."  
Then we'll talk about the full reinforcement learning problem  
and look at how we can apply it in financial markets.  
Our main examples are going to be  
involving the search for profitable investment  
and trading strategies.  
We'll see that we have algorithms  
that can learn to trade.  
And we'll see that once we've developed  
some of these algorithms, we can use  
them, in turn, to learn something  
about financial markets.  
So what is reinforcement learning?  
Well, reinforcement learning is something  
you've been doing since you were a toddler.  
It's how you learned to walk.  
Reinforcement learning is a way of learning new skills  
through experience, through trial and error.  
We start in a new environment, totally unknown,  
or we could give it a nudge to get it started.  
But generally, we'll start with a completely unknown  
environment.  
We'll try stuff out.  
We try stuff out to see what happens.  
It helps us learn about the environment.  
But we also learn what works.  
The key thing is observation and feedback.  
So we take actions.  
And we notice what seems good and what seems bad.  
If it's good, we do more of it.  
If it's bad, we do less of it.  
And then we keep mixing things up.  
That's it in a nutshell.  
That's reinforcement learning.  
Why is this interesting in financial markets?  
And what are some aspects of reinforcement learning?  
Well, some of the aspects here look kind of bad.  
But it turns out they're actually  
big advantages in interacting with financial markets.  
Reinforcement learning is slow.  
It converges slowly, if at all.  
And we'll see that actually is a good thing.  
It's tentative.  
It's never completely sure that it has the right answer,  
even when it seems to have eliminated  
some other alternatives.  
It's uninformed.  
Part of what it has to do is figure out its environment.  
So it's not biased by prior folklore or beliefs.  
It has to determine and validate information  
about its environment on its own.  
It's adaptive.  
This is important because financial markets are adaptive.  
They change over time.  
Financial markets are driven by people.  
And people can be changeable and unpredictable.  
And perhaps most importantly, it turns out, surprisingly,  
that the results we find are going to be very interpretable.  
And this is in contrast to many other kinds of machine learning  
methods.  
So what is machine learning?  
Well, machine learning generally is the development  
of algorithms for solving problems  
like pattern recognition, classification, prediction,  
or decision-making.  
And decision-making is the heart of finance.  
It can be estimated, trained, deployed,  
and done on an automated basis.  
So we do this to be more efficient at human tasks.  
We do it so we have nice chatbots  
to converse with and give us tips  
for where to go this weekend or what to do or what to read next.  
We use it in business and industry  
to improve the scale, scope, and quality of tasks  
that people would be doing otherwise  
unassisted by algorithmic guidance.  
And we can perhaps discover new kinds of rules and patterns  
that might not have been obvious or discernible otherwise.  
We often start building models with features  
that are known to have some relevance to the problem  
at hand, and of course we do because we have experience  
and we know that.  
But what would really be great is  
if we can find non-obvious things, if the computer can  
put some things together that we didn't actually notice,  
that we weren't able to try out yet.  
So that's one of the hopes and one  
of the motivations for machine learning generally,  
and certainly for the kind of problems  
we'll be looking at today.  
And then if we find successful strategies or policies  
or approaches, we'd like to improve them, refine them,  
and make them the best they can be.  
We'd like them to be optimal.  
So there are a number of different attributes  
that differentiate and distinguish different kinds  
of machine learning.  
And perhaps one of the most important  
is supervised versus unsupervised learning.  
Reinforcement learning is unsupervised.  
So what does that mean?  
Well, let me give you an example of a supervised learning task.  
Suppose we want to recognize faces or cat videos or whatever.  
We can start with examples.  
And the important part about supervised learning  
is not that I'm watching over the computer.  
The supervision means that we know what the right answer is.  
We can give the computer a picture.  
And then we can tell it what the right answer is.  
And then as we proceed over time,  
it can gradually make guesses and then refine those guesses  
and see if it can improve.  
So we can get another picture.  
It can ask us, is this the same person?  
Is this the same face?  
We can give it feedback.  
We can say, yes, that's right, no, that's wrong.  
And then eventually, on out-of-sample pictures,  
it may be able not only to get right answers,  
but to generalize things that weren't  
necessarily directly within the scope of its training set.  
So we might find other pictures like this one  
that could be recognized.  
So that's an example of supervised learning.  
It only works because we have a bunch of tagged examples  
that are there.  
And that's fantastic when we do.  
In finance, we don't.  
So reinforcement learning is going  
to be extremely helpful in this case.  
Unsupervised learning means that there's  
no right answer that's known.  
We can't give the machine that.  
That is, figuring out what constitutes success is part  
of the problem it has to solve.  
So what are some of these other attributes?  
And where do they fit in?  
Well, online versus offline-- so an online process which  
includes reinforcement learning is something  
where it can learn as it goes.  
It doesn't need to be batch-trained for months  
before it can start encountering the world.  
And every new interaction it has is immediately  
part of updating the process, updating its information set,  
and updating its rules for how it proceeds.  
We don't need a model of the environment.  
It's going to discover this along the way.  
All right.  
So in reinforcement learning, we don't need a prebuilt model  
as we do for many techniques.  
Here, discovering how things work is part of the task.  
We can deal with non-stationary systems.  
So stationary and non-stationary doesn't  
mean-- stationary doesn't mean something's not moving.  
It's a term from time series analysis that  
refers to whether the probability  
of random occurrences is changing, if the probability  
distributions are changing.  
So if the nature of the problem--  
it can include randomness.  
But if that randomness stays the same over time,  
that's a stationary system.  
And many techniques really assume and require stationarity  
to work.  
Unfortunately, financial markets are not stationary.  
And many of those techniques will lead us astray.  
Another dimension is how we use an optimal policy,  
if we find one.  
And that's known as exploitation.  
Exploitation just means when you find the best policy, that's  
what you do.  
You take advantage of it.  
But that's in contrast with exploration  
because sometimes, if we're not sure if we have the best policy,  
we might want to try out some alternatives from time to time.  
And we'll see that reinforcement learning  
involves a balance of exploration and exploitation.  
And that's the key to making it work successfully.  
A lot of times, different sorts of algorithms  
are trained on the basis of statistical criteria and loss  
functions.  
That is, they're basically trying to make better forecasts.  
And they try to minimize the forecast error.  
And that's the definition of success.  
Instead, in reinforcement learning, we give it a goal.  
We don't really tell it how it's supposed to accomplish that.  
We say, here's the goal.  
For example, go out and make money.  
And it's got to figure out how to do that.  
So we're not insisting on any intermediate steps.  
We're not insisting on any particular statistical criteria.  
We're giving it the overall goal.  
And we're letting it figure out how to get there.  
And then finally, interpretability-- many methods  
can be fantastically accurate and predictive.  
But it's very difficult to see exactly how they work  
and how they come up with their decisions.  
And this is problematic for a number of reasons.  
But I will show you a surprising alternative in the examples  
that we're going to look at from the financial markets.  
So reinforcement learning draws on behavior.  
It draws on language from human behavior.  
And we'll be applying that to some analytics from finance.  
Here's an example of a problem that you might  
recognize, going into a maze.  
And one way that we could do this maze  
is through trial and error.  
We could end up in the middle of the maze.  
We could get stuck.  
We might find our way into a dead end.  
Over here, we might have to backtrack and try things out.  
So we could solve this maze by trial and error.  
It might take us a while to get out.  
And we do things like this for fun.  
Certainly, computers can do them.  
And this is a solved problem.  
There are algorithms for classes of mazes  
which can tell us how to find a path through the maze.  
Here's another example that's a little bit less  
trivial and a little more in the spirit of finance that  
comes from a wonderful book by Sutton and Barto,  
pioneers in the field.  
They have a book on an introduction  
to reinforcement learning that I highly recommend for reading  
and for taking it and coding up some examples  
yourself, if you'd like.  
So this is an example called the cliff walk.  
And the idea is to get from the starting point to the ending  
point by walking along a grid along the shortest  
possible path.  
The trick is if you get too close to the cliff,  
you fall off.  
How do we frame that?  
Well, what we do is we assign rewards or punishments.  
In this case, what we want to do is  
we want to penalize falling off the cliff.  
So that's given a reward here in some units of minus 100\.  
So smaller numbers are worse.  
But we'd also like to get through as quickly as possible.  
So we're going to assign a penalty to every step we take.  
And that's what this R equals minus 1 means.  
So we have two competing objectives.  
One is we'd like to minimize the distance subject to not  
falling off the cliff.  
And this is something where the correct algorithm  
is apparent to you just by looking at it.  
But a computer is capable of learning this  
by trial and error.  
So what we're going to be doing is applying it  
not to cliffs, not to mazes, but to financial markets.  
We'll take a look at the stock market.  
And we'll look at a classic problem.  
How can you trade stocks, make money?  
So we're going to do it in the hardest possible way.  
We're going to have very, very few inputs.  
We're going to start by knowing nothing.  
The only inputs we're going to have  
are going to be market data.  
And by market data, I mean just prices  
and past histories of prices.  
And the only actions we're going to take-- we're  
going to have three allowed actions, three things we can do.  
We can buy, we can sell, or we can hold/we can do nothing.  
And our goal is going to be to maximize our long-term return  
through our trading strategy.  
And we'll see if we can solve this.  
And we'll learn some lessons, both about finance  
and about trading.  
And we'll see that in addition to maybe finding  
some interesting trading strategies,  
it's an interesting tool for studying  
market structure, innovations, crises,  
what happens when market environments change,  
and maybe some practical lessons for how humans and investors  
should behave in those cases.  
And it has many, many applications and extensions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.2 Bandits and Beyond  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's start with an example.  
Behind me is a slot machine, sometimes  
known as a one-armed bandit.  
Why is it a one-armed bandit?  
Well, it's got one arm, a lever that you can pull.  
And it's a bandit because it takes your money.  
It pays out less on average than it pays out.  
But if you're in a casino, you might get lucky.  
In the stock market, which has often been compared to a casino,  
the odds are really in your favor.  
On average, you do stand to be compensated for your risk,  
rather than losing money.  
And that's a good thing.  
So I'd like you to imagine this slot machine,  
our slot machine pays out more than you put in.  
So let's have some fun.  
We're going to make some money along the way.  
What would you do if you run into this machine?  
Well, put in some money and start earning.  
Put in money, pull the lever, see what happens.  
Put in money, pull the lever.  
See what happens.  
Eventually, we're hopefully going to get out,  
we expect to get out more than we put in.  
Each particular spin of the wheel  
is going to be random, so there are no guarantees,  
but the more we pull, the better sense we're  
going to get about what the probability of winning is.  
That is how long we have to wait to get different sized jackpots  
over time.  
And we'll never know for sure, but the more we pull,  
the more confident we'll be in our understanding  
of how the lever works.  
So let's make the problem a bit more interesting.  
Let's imagine that there's not just a single lever  
that you pull, that's not a decision problem, that's  
just a mechanical problem.  
Let's suppose that we need to make a choice.  
And the choice involves pulling one lever,  
pulling another lever, or pulling a third lever,  
or in general, N levers.  
And that's why this is known in the literature  
as the n-armed bandit problem.  
So here's the way it works, each lever produces random jackpots.  
But it's connected to a different probability  
distribution.  
And they all look the same.  
No one's telling you which is the best lever to pull.  
You've got to figure that out.  
How can we go about it?  
Well, we might go about it through trial and error.  
We could start by pulling on the levers randomly,  
and eventually, we're going to see that we'll be making money,  
and we'll get a sense as to which lever  
might be better than another.  
We might never be completely sure,  
because there could be one arm that maybe pays out  
small amounts rather regularly that has a big lurking  
jackpot hiding in it.  
And we won't know that unless we give it enough spins.  
So what we might want to consider  
is how we could balance two things.  
One of them is once we've initially  
figured out which we think is the best arm,  
how much of the time should we take  
advantage of that to earn as much profit as we can?  
And how much time should we set aside to do the alternative,  
to do the suboptimal thing, to try it out,  
just in case we might have missed something  
in one of the other actions?  
Well, here's an algorithm that handles this problem.  
So to beat the bandit, we initialize it  
by setting all values to 0\.  
And initially, we're just going to try out everything at random.  
And we won't have any information.  
If we ask what's the best lever to pull,  
they're going to look the same.  
And we'll break ties randomly.  
But as we go along, here are the rules.  
The rules start to kick in and they involve this.  
We choose an action.  
And the action we pick is, most of the time, going  
to be the one that we think currently  
is the most valuable action.  
And we're going to do that not with probability 1,  
not with 100% certainty, but with probability 1 minus  
epsilon, where epsilon is a small number, like 1% or 10%.  
And then 1% or 10% of the time, we're  
going to do something completely random,  
even if it's not the best lever.  
So you think maybe the top lever, that's the one to do,  
that's the one that's got the most payoffs.  
And we'll do that, let's say, 90% of the time.  
But 10% of the time, we'll just pick lever  
at random just to see what happens in case maybe we've  
missed something.  
So these are the steps.  
We pick an action according to this rule.  
We collect our winnings.  
We update our estimates for the value of the different states.  
And then we go and we do it again.  
So this is called an epsilon greedy policy.  
The epsilon is because of the parameter  
that we set aside for trying suboptimal things.  
And greedy is not a value judgment.  
It's a technical term meaning we do whatever  
seems to be on the shortest horizon optimal  
by cashing in right away.  
Another way to say this is that we're  
balancing in this policy, exploration with exploitation.  
Exploitation also has no value connotation  
in this in the technical sense.  
It just means that we're doing what  
is the most optimal and the most profitable strategy.  
So how does this work if we try it out?  
Well, I ran a simulation of doing  
this where I made a bunch of machines on the computer.  
I simulated them with unknown and different values  
attached to different arms.  
And I tried three different strategies  
of exploring, and updating, and exploiting.  
And these three lines show the effect  
of different values of epsilon, 0%, 1%, and 10% of the time  
on how often I end up taking the optimal action.  
At the beginning, not so much.  
Around one out of three, it's completely random.  
But if I keep exploring on the 10%,  
I end up actually at the best possible outcome.  
So by forgoing some profit at the beginning  
and by being explorative, I end up, over the long term,  
doing the highest percentage of actions,  
spins that generate the most profit.  
If I make a judgment too early or not at all,  
this line corresponds to having no more exploration,  
I might get stuck in a rut.  
I might not get the right action at all.  
And I'm giving up an awful lot of difference between these two.  
So something to consider for how we  
can learn from our environment, how we can continue,  
even after we've gone through an initial learning phase,  
to keep exploring and keep a balance in the actions  
that we take.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.3 Learning to Trade  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now let's talk about trading stocks.  
So the three arms of our bandit, the three actions that we have,  
we might think of as being equivalent to three  
different kinds of trades we could make.  
We can buy, we can hold, or we can do nothing,  
which is a decision in itself.  
Equivalently, we can set this up,  
and that's how the actual algorithm does  
work, as three states that we want  
to achieve in terms of our holdings,  
that is, we want to either be long a stock, short a stock,  
or flat to have no exposure to it.  
So a long position means we own a positive number of shares,  
and we earn a profit if the stock goes up.  
A short position means that we've borrowed and sold  
shares that we'll repay later on, and that profits  
if the price of stock goes down.  
And a flat position means we don't own any.  
And that's what we would do generally  
if we have no idea what's going on.  
So these can all be generalized.  
And, of course, stocks trade in any number of shares.  
And there are many, many extensions of this.  
But we'll just consider these three basic positions  
of exposure to a stock.  
That will help us understand whether we're  
doing a good job predicting and interacting with the markets.  
So one of the things about this bandit problem,  
we definitely need to generalize, because the bandit  
that we dealt with-- after you pull the levers,  
the bandit stays the same.  
But financial markets don't work that way.  
And trading doesn't work that way either.  
After you've made an investment, you've  
given information to the world about the trade you've done,  
but also, now you own some stock that you didn't own before.  
So the state of the world has changed.  
The environment has changed.  
So we're going to consider that there are different identified  
states.  
And in each state, there are different actions  
that might be permissible.  
So for example in our stock trading example,  
if you bought something yesterday and you like it today,  
we might have a rule that says you're only  
allowed to own one share.  
And now you can't.  
Even though it's a positive expected value,  
because you're in a different state, you're not able to buy.  
So we could say that if you're in the state where  
your position is zero, where you have zero shares,  
then you could buy, but your action might be different  
if you were in the positive state  
where you already own the shares.  
And if you were in the short state and it looked good,  
then you might buy two shares, one  
to cover the share that you borrowed  
and another to create a new long position.  
So that is to say, these actions that are available  
will depend on the state that you're in.  
But it goes both ways.  
Once you take an action, that will change the state  
that you go to.  
And therefore, it might be worth considering  
as part of the value of taking an action,  
not only the payoff of the immediate payoff when you pull  
on that wheel, but also the value of ending up  
in a subsequent position.  
So in our slot machine analogy, consider that there's not just  
one kind of slot machine.  
There are several, and they're denoted by different colors  
for the different states.  
So you start with the red slot machine, you pull the lever,  
you get a reward.  
But now you're at the green slot machine,  
and you have to explore it and learn about what its states are.  
But you could imagine that maybe at the red slot machine, what's  
most advantageous is to pull the bottom arm, not because it gives  
you the best payout, but because it bops you over  
to the green machine, which has really good payoffs.  
So the possibilities can be quite involved,  
and we'll just try them out and see  
how far we can go and see what we can figure out  
in our example.  
So the generalization that we've made  
is we began with the bandit that had  
only actions and a single state, and now we're  
allowing there to be different states.  
And we're asking, what is the value  
of taking each action in each possible state?  
Taking the action means we get a reward,  
and it means we go to a new state.  
What should we use if we're talking about the stock market?  
Well, we're going to start with stock data,  
and we'll talk about stock returns.  
So here's an example of stock returns  
from a group of about 600 stocks on a particular day  
where I've rank ordered them from the worst to the best.  
So down here, the worst stock on the day lost about 6%.  
And the best stock on the day made about 6%.  
And you can see this is about half of them lost money,  
half of them won money.  
They were different amounts.  
Rather than taking a look at every single stock  
every single day, we're going to simplify things a bit,  
but our basic idea is on a given day,  
we're going to ask which stocks were winners  
and which stocks were losers.  
And then we're going to use that information  
to see if that tells us anything about what's going  
to happen on the next day.  
So what we'll do, in particular-- we're  
looking at winners and losers-- is we'll  
bucket these into deciles.  
We'll look at the top 10%, the next 10%, the next 10%,  
and the bottom 10%.  
We'll give them numbers from 1 to 10\.  
The ones are the losers.  
The tens are the winners.  
And we'll see is that even helpful.  
There's lots of other information we could use.  
We could use lots of other data from the capital markets  
directly.  
We could use things from all kinds of external data  
sources about the company, about the economy generally,  
about the world.  
There's no limit to the kind of inputs we could put.  
But for this example, we're going  
to start with the simplest possible one.  
And there are also state variables that are internal.  
So what those things that I mentioned so far have in common  
is that they're all things that anyone could observe,  
not just us.  
Anyone else looking at the same markets  
would see the same thing, but we might have internal variables  
as well.  
And these could be things like what stock portfolio do  
I currently own that could inform my choice as to what  
I want to do next, and there could be other calculations  
and analytics that we've done that are not  
available to the rest of the world,  
like a pricing model for a security.  
And those would be internal state variables that we might  
Have.  
So in general, reinforcement learning  
will let us take multi-dimensional description  
of state.  
For our purposes, we're going to start very simple.  
We'll take one external state variable and one internal state  
variable.  
Now, this is a hard problem And in fact, there's  
a whole theory that says that if markets are efficient,  
it's an impossible problem The idea is that seems somewhat  
paradoxical that if a market is efficient in the sense  
that investors access information very competitively,  
very aggressively, people get information  
and act on it extremely quickly, what should the markets look  
like?  
How would we take advantage of things in a world like that?  
Well, the paradox is we wouldn't be  
able to do very much because if everyone has information  
and acts on it quickly, prices are going  
to move to their correct level.  
This is a point that Paul Samuelson noted long ago  
with this title, which I love, a lot of mathematical details,  
but it's a proof that properly anticipated  
prices fluctuate randomly.  
So in a well-functioning market, it should look random.  
Why does it look random?  
Well, if everyone's got all the correct information,  
then prices would go to their correct levels.  
What would make them change?  
New information, news.  
What's news?  
Well, it's something that people didn't know about,  
that they weren't expecting.  
And that's going to be random.  
So by news, I don't mean Apple's coming out with a new iPhone.  
We know that.  
They do that every year.  
We can build that into our expectations.  
We mean things that are genuinely new.  
So markets do exhibit a lot of randomness.  
And in fact, one of the challenges  
in applying all kinds of machine learnings to financial data  
is that so much of what we observe looks like randomness.  
It looks like noise.  
So instead of noise being a small feature in the data,  
it's a dominant feature in the data.  
So if we were to go with Samuelson's idea and many others  
who've worked on this idea of efficient markets.  
What we'd expect is this whole exercise  
is going to be one in futility.  
There won't be anything to find because why?  
The information set that we're using.  
Yesterday's prices is known by everybody.  
This is not news.  
This is not information.  
The only way that this could work  
is perhaps if people are not acting fully  
on the information that's included in the prices  
that we see.  
So here's our setup.  
We start at the top in a particular state.  
We take an action.  
We're going to pick our epsilon greedy policy.  
We'll take an action.  
That will move us down to a new state.  
But along the way, we're going to collect a reward.  
And this time, our reward is not going  
to be money out of a slot machine.  
It's going to be the financial return on the stock on the given  
day.  
So if the stock went up 6% and we were long, we earned 6%.  
If it went down 6% and we were long, we're going to lose 6%.  
If we were short and it went down,  
we're going to gain 6% and so on.  
Once we're in this state, we're going  
to have a whole new set of prices.  
In principle, everything could be changed up.  
And we're going to-- based on what the state is for each  
of the stocks we look at, we're going  
to choose a new action according to our valuation model.  
We'll end up in a new state and collect  
whatever the new reward is.  
So in actual financial markets, we interact with them.  
So in addition to the fact that we're collecting rewards,  
our trades convey information to the markets.  
And as I mentioned, they could change prices.  
And we're certainly going to be changing our portfolio.  
So the changes in the market environment  
could be deterministic.  
But in general, they're going to be stochastic,  
which is just a fancy word for saying that they're random.  
But in addition to randomness in the outside world,  
we're allowed to have randomness in our policy as well.  
And we do that in our epsilon greedy policy.  
That is, a certain amount of the time,  
we just try something else just for the heck of it.  
So some of the time we're going to say,  
even though I've got a rule, I'm pretty  
sure I know what's going to happen  
or what the best trade is for this stock.  
I'm going to do something different.  
It seems paradoxical, but we've also  
seen how effective it could be in our warm-up bandit example.  
So we're going to include that.  
And in fact, the epsilon number is  
one of the important parameters along with the learning rate  
that determines how dynamic and adaptive our algorithm is,  
but we're making virtually no assumptions about how  
the environment behaves.  
What's our goal?  
Well, our goal is long term portfolio value.  
And this picture behind me shows three different Monte Carlo,  
that is, computer random number simulations,  
of what might happen applying different kinds of strategies.  
Obviously, we'd like to have the one that goes up,  
and we'd like to avoid the one that goes down.  
Unfortunately, all three of these examples  
came from looking at the same set of rules applied  
to the same set of data, just with some extra randomness  
thrown in.  
These were just some lucky lucks of the draw and unfortunate  
lucks of the draw.  
So how do we distinguish luck from skill?  
How do we optimize our chances?  
How do we find the best policy?  
And how do we know if there's actually no policy to be had  
and that maybe Samuelson and Fama and others were right?  
Well, we're going to define a goal.  
And the goal generally in reinforcement learning  
is a long-term average.  
And we might include-- we could say  
that our goal is going to be an average of future returns,  
possibly with some discount factor gamma, that  
says that we'd actually value returns in the present  
more highly than returns in the past.  
We're actually going to do a simpler version than that,  
where we'll just look at the average return over our periods.  
But there are many more advanced things  
one could do, like looking at risk adjustment as well,  
things like a Sharpe ratio.  
So this certainly can be generalized.  
But the essence of reinforcement learning is we define a goal.  
And through experience, the algorithm  
is going to make judgments about whether it's on track  
or whether it needs to change things up.  
So the steps that go into it, there's  
a learning element where the algorithm needs  
to learn how the world works.  
It needs to figure out what are things to do  
and which ones are good, and estimate  
the values of using different states and experience.  
Once we've got that model, there's a planning element  
as well where we determine what the optimal policy is,  
and then we decide how we're going to execute it  
and how we're going to balance exploration and exploitation.  
And then all of these get updated as we go along.  
And there are different rules for how we can update.  
And that's a large area of research.  
And there are many different techniques  
for how we can update our information.  
So enough theory, let's run the numbers.  
Here's what we're going to do.  
We're going to take a look at US stocks of large-cap US equities.  
I've picked about 600 of the largest companies  
over a particular time window.  
And I'm looking at them at a frequency of one-day returns.  
You could run this with any universe of stocks.  
You can pick your favorite stocks, your top 10,  
your top 30, your Magnificent Seven, the Russell 3,000.  
You pick a set of stocks.  
You pick the time horizon.  
You could do monthly, whatever it is.  
And you should.  
You should try it out.  
State information.  
What I'm going to do is instead of taking  
all of the detailed information about the prices,  
I'm going to group these into buckets just to simplify things  
and to keep the size of the state space down.  
This is a challenge for reinforcement learning,  
as in dynamic programming, that if the state space gets  
too large, the dimensionality can lead to computational  
intractability.  
Here we're going to keep things extremely simple.  
We're going to have 10 possible states of external information.  
So we're going to assign deciles to stocks on each day.  
And there's a rule in finance, no time travel allowed,  
no peeking at future data.  
So what we're going to assume is on each day  
that we observe what happened during the market  
during that day.  
And just before the close at 3:59 in the afternoon,  
we're going to decide to place a trade that will earn a return  
on the following day.  
For the stocks I've picked, this is actually  
a pretty good approximation.  
You could worry that things are going to happen  
in the last few seconds.  
One of the problems, of course, is  
that the information we have here is from closing prices.  
But when the markets are closed, you can't trade,  
and you're not allowed to pretend  
that you knew things before.  
So this is an approximation, and it's subject to refinement.  
And that's the thing that people do in quantitative finance  
all the time.  
Anyways, for our purposes, it's a pretty good approximation.  
And the three actions we're going to have  
are that for every stock, we can take  
a long position for the following day,  
a short position for the following day,  
or no position at all.  
Got it?  
What do you think happens?  
Well, I ran it.  
Let me show you what the results are for the cumulative rewards  
of the portfolio.  
They're astonishing.  
This strategy somehow figured out  
an inefficiency in the market, and it  
managed to make money steadily.  
But let's break this down a little bit before  
we dig into how it did it and what's going on.  
So one of the things to notice is  
that although there's a long upward trend--  
and this is not typical of what we see for stock price paths.  
They typically have way more fluctuations and much less  
steady growth.  
But let's take a look carefully at a few elements  
just of this picture I've drawn for you.  
The first one is there's this initial period where actually  
nothing much is happening.  
And these are days, remember?  
So this is more than a year's worth.  
If you start a hedge fund, and you get some investors to give  
you money and you say, I've got this great algorithmic thing  
that I heard about on YouTube, it'll be great, trust me,  
they might run out of patience if this was your performance  
after a year.  
You've made some money, lost some money,  
made some money, lost some money, basically went nowhere.  
Of course, if we were taking this out into the real world--  
and I'm not saying you should, no financial advice here.  
But if we did, of course, we could do  
a little bit of pre-training.  
There's no reason we need to start completely cold.  
For our purposes, this is fascinating  
because this tells us that this is the initial learning period.  
This is when it was trying out different things for all  
of the 600 stocks across all of the possible actions in each  
of the 10 possible states.  
So it takes a while to learn, but then eventually, it  
seems to have figured something out, doesn't it?  
And what we see is very steady growth.  
Now, the average growth looks pretty good,  
but there seem to be some wiggles and bumps here.  
And did the market change?  
Did it stop working?  
Well, it's actually hard to tell.  
And I'll show how we'll address that in a moment.  
The problem is that this is historical data.  
And in finance, it's not like a laboratory science  
where we can rerun the experiment  
in controlled conditions.  
The stock market returns only happen once.  
So it could be that maybe something was going on  
in the markets during this period.  
Or it could be that's just the way it is  
and everything is fine.  
We'll see that by looking at simulated data,  
we can separate and tease apart and isolate  
some of these behaviors.  
But first, let's figure out how it works.  
What is it doing?  
How is it doing this?  
600 stocks, thousands of days of trading,  
10 states, three actions.  
What's going on?  
What did it learn?  
How did it learn?  
Well, we know how it learned.  
It learned by trial and error.  
Let's take a look at what it learned.  
Remember that I told you that we want  
to do the most valuable action.  
So the way in which we set up the problem  
is we assign a function to keep track  
of our estimate of the value of each action  
in each possible state.  
And those get updated along the way.  
And at the end of the simulation or actually  
at any point along the way, we can take a look  
and see what those value functions are.  
And the value functions are very readily interpretable.  
Let's take a look at them here.  
So here I have these actions are for being flat, for being long,  
and for being short.  
And then I've shown you what the value  
is for each of the 10 states going  
from the lowest to the highest.  
So the value of being flat is zero  
because we're not investing.  
So that makes sense.  
This group here of 10 bars are the things  
that have value when we take a long position.  
And what do we see that has value?  
The ones.  
These are the ones, the twos, the threes, the fours,  
and so on.  
Notice that the ones, twos, and threes all have positive value  
if I take a long position.  
This is familiarly known as buying the losers.  
How about a short position?  
Well, anything with a negative value, we shouldn't do.  
We'd be better off doing nothing at all.  
That is, it's better to have no money than to lose money.  
When is it valuable to take a long position?  
Excuse me.  
When is it valuable to take a short position?  
When the stock was among the top 10%  
in winners on the previous day.  
So to summarize this, we could say  
that what these values are telling us,  
what the algorithm has learned, the way it's made  
its profit is by buying the losers and selling the winners.  
It sells the tens, and it buys the ones.  
The results were what we saw.  
Another way to display this information  
is just to pivot the graph in the opposite direction  
and look at the value in each state of taking each action.  
This time, green represents a buy, red represents a sell.  
And you can see that if we're in a state 1,  
it's a good thing to buy.  
It's a bad thing to sell.  
And over here in the tens, it's a good thing  
to sell, the red bar, and it's a bad thing to buy.  
You'll also notice that these bars in between--  
in the middle here, there's lots of nothing.  
So if we're in these middle ranges,  
we shouldn't do anything.  
We should be flat, we shouldn't invest.  
We're going to lose it we're long.  
We're going to lose on average if we're short.  
But one of the other things that happens with the algorithm  
is it doesn't visit those middle states that often.  
That's why the bars are different.  
The ones where it has the greatest confidence  
are the ones that it's visited the most often,  
and we can keep track of that as well.  
We also can track along the way how many visits  
have been made to each state, and our epsilon policy  
ensures that we keep updating just  
in case something interesting should turn up and happen  
to be the case.  
Now, this is actually not an entirely new observation,  
and there's published literature that  
has found this kind of thing in stock market returns.  
It's known as, sometimes, it's a mean reversion  
or a contrarian strategy.  
And it's been attributed in literature,  
this paper co-authored by my MIT colleague Andrew  
Lo and his co-author, Craig MacKinlay.  
They observed a long time ago that there  
can be patterns in market returns  
that could be profitably traded, but they started out  
with an idea that, hey, maybe investors overreact.  
What would that look like?  
How would it show up?  
And their approach was to start with a trading strategy.  
Let's be contrarians, and let's see  
if that's rewarded by the data.  
And in fact, they discovered some very interesting patterns.  
What we've done with our learning algorithm  
is to find the same results that they did,  
at least qualitatively.  
We're working in different data sets,  
and we're working in data sets that they didn't have access to.  
But we found the same kind of dynamics,  
namely that a contrarian trading strategy can actually  
be profitable in an economically significant, non-trivial way.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.4 Trading to Learn  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So we've just seen that reinforcement learning can  
uncover profitable trading strategies and information  
in market data, starting with no information  
at all about what's there and with the barest minimum  
of information that shouldn't even be tradable.  
So having done that, before we go out and start trading  
with real money, let's explore, because this  
opens up an entirely new laboratory,  
not just for working on algorithmic refinement,  
but for understanding markets, for understanding how trading  
strategies interact with markets,  
and for understanding investor behavior, what it is  
and how maybe it should be adjusted.  
So let's consider, what happens if the markets change?  
We saw an example where there were two phases, basically,  
that we could tell.  
There was an initial learning phase,  
where we acquired information about the environment.  
We tried things out at random.  
And then we had a profit-making phase.  
And that seemed very steady.  
And it went on for a really long time.  
That's great.  
Such things in real financial markets  
tend not to go on forever.  
Eventually, either someone else catches on  
and competes with you, or if you're really good,  
you'll change the markets yourself  
by trading so much that you take advantage of the opportunity  
and shift the prices, so that it goes away.  
So markets will change due to our own actions,  
due to other people's actions, or more commonly,  
due to some kind of external events.  
So what would happen?  
And how would reinforcement learning algorithms behave,  
and what would they teach us, if market conditions were  
to change?  
So this is a really important feature  
that I mentioned before about financial markets.  
We call them non-stationary.  
It means that if you have a set of rules in one period,  
you can't be guaranteed they're going to work the same later on.  
In our casino analogy, we said that the difference  
between financial markets and casinos  
was that the odds are in your favor,  
even though both involve different kinds  
of random processes.  
But here's another important difference.  
In the casino, the rules are fixed.  
They do not change the slot machines on you between pulls.  
A roulette wheel does not change the number of slots it has  
from one day or one spin to the next.  
You don't go in one spin, there are 36 numbers, the next are 42,  
the next time there are 19\.  
So the rules stay fixed.  
Financial markets, things can change.  
And they can change quickly.  
And this is a major source of financial risk.  
And it's a concern to pretty much anyone  
who has any kind of investment.  
So how should a model behave when the rules of the game  
change?  
We try to build good models, whether they're  
traditional forecasting models, whether they're  
machine learning models of other varieties,  
or whether they're reinforcement learning.  
We can ask what happens if the assumptions on what  
they're built change?  
What happens if the data no longer has the same properties  
that it had before?  
Let's try an example.  
Let's try an extreme one.  
Let's turn out the lights.  
How do we do that?  
Well, suppose that we've got our well-trained model,  
and we sneak into the data, not the actual historical market  
prices, but some random data.  
Should we give it a try?  
Let's take a look.  
Here are the results of the same simulation  
that I did before, where guess where I've  
inserted random market data.  
And you can see, it's right here in the middle.  
So I picked a period where I cut out the historical data,  
I put in completely random numbers.  
And then I turned the switch back on  
and I reconnected it to the original market data.  
Now, does that look like what you expected?  
I asked my students this and their first answer  
is, of course, uh huh.  
The signal went away, so you lost money.  
But that's not quite right.  
That can't be quite right.  
And actually, this is the first simulation I did of this,  
but it's a little bit atypical.  
If the data is random, you shouldn't lose money.  
You shouldn't gain money.  
You should just not go anywhere.  
In finance, the opposite of being right  
isn't always being wrong.  
It's generally being random.  
If you're systematically wrong, if you  
see that it's going in the opposite direction,  
you could flip the sign and take advantage of that.  
So in fact, here's what's interesting about it.  
When we remove the signal, the profitability went away.  
If I showed you more examples of this,  
you would see it's not always a loss or a very large loss,  
but when I turn the signal back on,  
it resumed making money out here.  
Get my pointer back, there we go.  
OK, pretty nice.  
Now, that raises a whole lot of new interesting questions.  
Would it remember that the original strategy forever?  
What if the lights never came back on?  
What if it stayed random indefinitely?  
Or what if some new market regime came on?  
Does the effectiveness after a break  
change depending on how long this period is  
where we inserted the break?  
That is, if we need to relearn this initial learning period  
we discussed before, and we understood that,  
because we started with no knowledge at all.  
By the time we get out here, we do have some knowledge.  
We have definite views about what's  
a successful way to invest in each  
of the stocks in our universe.  
And in this scenario, I temporarily suspended-- and then  
I let it resume.  
But that's not the only possibility we might have.  
And we can ask about these different time scales.  
How long does it take to learn?  
How long does it take to forget?  
How long does it take to resume?  
What happens if things change very quickly  
or if they change very slowly?  
The feature of our setup that saves the day  
is our exploration.  
Because even if we get it disastrously wrong,  
we still are spending some of our time trying out  
alternative options.  
So let's take a look at a few more directions  
that we could take this in this laboratory  
and see what we can learn by using algorithms  
to explore markets.  
The first thing we would do is run a generative simulation.  
That is the problem with historical data  
is that there's only one of it.  
We can't reproduce it.  
We can't control it.  
And we can't be entirely sure about what  
was going on at the time.  
So what we should do is first, we should back up a step  
and look at randomized data, where we know what's in it.  
And if there's a signal there, we'll put in a signal.  
If it's random data, it will be completely random.  
The key feature we want is that it's going  
to be homogeneous over time.  
It won't be dependent on news events  
that we couldn't track down and that won't be repeated.  
So in this example, I'm showing a simulation of exactly  
the same algorithm, but where I've done a synthetic Monte  
Carlo data using what's called an AR(1) process,  
an autoregressive process with lag 1, which is a time series  
formulation of something that is qualitatively known  
to contain the same kind of profitable signal  
that we saw before, namely on a lag 1\.  
The 1 in the AR(1) means that on a one day time scale,  
the behavior will tend to reverse.  
The winners will tend to go down.  
The losers will tend to go up.  
And this has a built-in dynamic known as mean reversion.  
So I put that into the data, instead of just  
generating purely random data.  
Now, I've generated data that has a mean reverting signal.  
So this removes the historical trends and accidents.  
And we can take a look.  
And now, if you look at this, you  
can see it has the same qualitative features.  
But this learning phase isn't quite as chaotic.  
It's mostly not gaining or losing,  
but it's a comparable amount of time.  
Actually in this case, it's a little bit faster.  
But there's a comparable period where there's  
an initial learning phase.  
And then it goes into a steady state accumulation phase,  
where the exploitation has learned how to take advantage  
of the market signal.  
So that is a good thing that we might  
have thought of doing before we tried market data.  
This shows us that we're able to detect signals  
that we've put in on purpose.  
Now, we can probe a bit.  
And we can look, these are just examples  
of two kinds of variations, where I did experiments  
changing, introducing random data in the middle,  
disrupting the signal for different lengths of time.  
Now, I don't need to worry about whether my disruption matters  
that it happened in a particular year or in a particular month,  
or when there was something going on in the economy.  
The data generating process itself  
is something that's under our control  
through our generative Monte Carlo.  
And then we can take a look at what the results are.  
So you see that we have different variations.  
And we can explore these different timescales.  
And watch how things learn.  
But let's not stop there.  
Let's go further.  
There's more to life than mean reversion.  
And markets can be very complex.  
Let's consider a completely different kind of dynamic  
that our strategy couldn't possibly do well with.  
In fact, it's going to do badly because we're  
going to put in exactly the opposite kind of dynamic.  
So here, I've got some synthetic data, which, at first glance,  
looks random.  
So these graphs here are sample paths with my new dynamics.  
And this looks, by eye, indistinguishable from Monte  
Carlo data that I would have done, pure random walk data.  
And if you look at the graph on the left,  
if you're familiar with autocorrelation functions,  
there's no serial correlation in this data.  
Autocorrelation is one statistical technique  
for observing whether there's predictability in the data set  
by asking whether the returns in one period  
predict those in the next.  
So I've actually put in some signals,  
but I've hidden them reasonably well.  
But what are the signals that we have?  
Well, let's take a look.  
So I'm going to take this new set of data,  
and I'm going to feed it to our algorithm.  
And let's see what happens.  
So it makes money.  
We started from the beginning.  
It made money.  
What's going on here?  
Well, you can see the picture on the right shows the process.  
You can see qualitatively, we have the same features  
as before.  
Remember, this is synthetic, not historical data.  
There's an initial period where it's learning,  
and then profit, profit, profit.  
It's making money.  
The picture on the left shows the unconditional return  
distribution, just a histogram of the returns.  
And these are logarithmic returns.  
And the red line shows a normal distribution.  
And this looks pretty much like a classic log  
normal distribution that is familiar in quantitative finance  
and you'll see in lots of textbooks.  
What's the strategy?  
What was going on?  
Well, let's take a look.  
And this time, I had 5 states, not 10\.  
But the strategy that it found was  
to do the opposite of what it did before, namely  
to buy the losers and sell the winners.  
The signal that I put in was trend.  
So there actually was a trend, even  
though it passed some high level statistical tests.  
There's trending behavior.  
And it is profitable in this model  
to buy something and keep holding it.  
So just in case you thought that I had set up the initial problem  
kind of knowing what answer I wanted to find,  
the reinforcement learning could only solve one kind of problem,  
here, I wiped the slate clean.  
I gave it the opposite kind of problem.  
And it came to a profitable strategy,  
where it was able to detect the opposite condition.  
Of course, this doesn't always work.  
There are always new signals that will elude us.  
And there are things that may require other sorts of data.  
But this is one of the things that  
should have been the most likely to fail, because we only gave it  
market prices that shouldn't have any information at all.  
And in the cases where I've put in a signal,  
it was done in a way that was not immediately obvious.  
And it could only be discovered through applying things  
systematically through trial and error.  
So just to recap this most recent experiment,  
the synthetic data that we had, this data  
involved trending behavior, positive trends  
of different lengths, but then the trends would sometimes  
change direction randomly and the trends  
would go in both directions.  
And we had 600 stocks, each of which  
could be trending up or down randomly over different lengths  
of time in different directions and switching  
all over the place.  
And yet, our algorithm managed to find a profitable way  
to take advantage of it.  
And we have this transparency.  
We can look at the parameters that the algorithm settled on  
and we can interpret it.  
We look at the positive bars, and we  
say those are the positive value actions.  
It found out that it should sell more of the losers that  
are trending downward.  
It should buy more of these winners that are going upward.  
And the things in the middle, it really should not bother with.  
Let's take it a step further.  
What happens in the real world?  
Well, one of the features of markets that I mentioned  
is markets do change their character.  
And one of the features that we haven't talked about  
is how human traders do and how humans  
who currently use classical algorithmic trading techniques  
do.  
And one of the problems with or limitations of many algorithms  
is they don't tell you when it's time to give it up.  
They don't tell you necessarily when the world has changed.  
They don't tell you, even if you know  
that the world has changed, what you're supposed to do next.  
So let's see how reinforcement learning would do if we run it  
through a manufactured crisis.  
So I've spliced together two data sets,  
the first one is Monte Carlo data  
with 10 years of trend following signals built in.  
And then on a dime, I've switched  
to 10 years of market returns that we  
believe, from our previous experience,  
might have a signal in them.  
And what do we see?  
Well, we see we have an initial period where it's making money,  
then there's a switch.  
Now, initially, it's doing the wrong thing.  
It's using its strategy and it's losing money.  
It was used to making money.  
It's lost money.  
In fact, it's lost as much money in this period of time  
as it had made during the entire previous period up  
to that point.  
But then without anyone coming in and giving it instructions,  
it turns things around.  
It's been observing.  
It's been trying things out.  
It knows that what it's doing was not successful.  
And it says, hey, this isn't working.  
Let's try something else out.  
It's always updating.  
It's always learning from new information.  
It never is settled in a definitive answer  
as to what's the best strategy.  
It keeps trying.  
And therefore, it can adapt.  
And in this case, it adapted spectacularly well.  
What happened?  
What were the signals it found?  
How did it change strategies?  
Let's take a look.  
That's the advantage of the transparency  
that we have through our state variables  
in this tabular setup of reinforcement learning.  
So if we look, we're going to look at two points.  
We'll look at the midpoint right before the crisis occurred.  
And then we'll look at where we ended up  
at the end of that period.  
And we can understand the evolution and transition  
that we have.  
So the picture on the left is the state,  
the state action values at the midpoint of the period.  
And this looks similar to what we saw before.  
So this is halfway through right before we forced a transition  
change.  
And what's it learning to do?  
It's valuable to sell the losers and to buy the winners.  
What happens by the end?  
It's learned to do the opposite.  
Buy the winners, sell-- excuse me, buy the losers  
and sell the winners.  
So it starts out knowing nothing.  
It learns from experience.  
It establishes a profitable, not just a profitable track record,  
but a profitable understanding of how  
to work with the environment, figured out how things work,  
and what are the best actions to take.  
But when the rules change, when the markets are non-stationary,  
the fact that it continues to explore  
gives it the possibility of finding out first,  
the old stuff isn't working anymore.  
And second, there's a new alternative  
that's actually better.  
So let's try that.  
And given an appropriate amount of time,  
it can establish a new track record, a new set of rules,  
and even flip from one side to the other.  
It does not remain anchored in the past.  
It's always provisionally updating its beliefs  
when they continue to be confirmed and reaffirmed.  
It goes merrily on its way, but it's always  
open for the possibility of change.  
Now, there are a couple of things  
that we should add if we want to consider  
this to be a realistic model.  
One of them is that we should include a bigger state space.  
And we should have more dependence  
on our portfolio positions.  
So one of the important features of actual financial markets  
is that we do change them when we interact.  
And the trading is not frictionless.  
And that this tends to hurt us as we do it.  
So what we're going to do is we're  
going to include a transaction cost component that  
will penalize trading.  
And one of the things that does is in addition to implementing  
real world frictions, is it will make it somewhat advantageous  
to sit on a position rather than trade it  
for only something that's infinitesimally better.  
So it's going to split the symmetry between buy  
versus hold.  
Previously, it didn't cost anything  
to get out of the position, to just liquidate  
the whole portfolio and go into something better.  
Here, once we're in a position, this  
is going to make it a little bit stickier.  
And it also makes it much more advantageous in periods  
where the signal goes away to do nothing,  
not to incur transaction costs when  
there's no benefit to be had.  
Here's an example of what happens when we run this  
with our actual market data.  
And you can see, at least through this period of time,  
it starts out great.  
We have our initial learning period where we lost money.  
We have a period where we did fabulously well.  
And then it seems our signal went away.  
During this period, we neither made money nor lost money.  
And the strategy tried to learn to sit on its hands.  
But eventually, things turned around.  
So not quite ready for putting real money into yet,  
but a fascinating laboratory for learning about markets,  
for learning about trading, for preparing contingency  
plans, for thinking about operational risk,  
and for thinking about how we know what we know  
and how we acquire that knowledge.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.5 Additional Perspectives and Conclusion  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Reinforcement learning isn't new.  
And its applications to the financial markets aren't new.  
But it is an area of active research right now.  
Here's a list of some references that you  
might want to take a look at, which include things  
that I've mentioned and things that I'm about to show you  
from some other researchers.  
One of the early works into reinforcement learning  
in financial markets was looking at predicting  
the direction of the overall stock market--  
so looking for predictions in the S\&P 500,  
looking at trading signals, investment strategies that  
might work, going long and short-- along the way,  
some of the ideas that we talked about using  
a different mathematical structure from the one we did,  
but also looking at more sophisticated target functions,  
like Sharpe ratios that adjust returns for risk  
adjustments along the way.  
More recently, there's been work in looking  
at market microstructure, which is studying things  
not from the perspective of an investor who's buying or selling  
stocks, but from the point of view of a market maker  
who needs to post prices at which he or she is  
willing to buy or sell.  
In this work, rather than looking at all stocks  
as being, essentially, equivalent  
and where learning how to trade one stock  
informs us about how to trade another stock, in this case,  
the modeling was done on a stock-by-stock level.  
And many features were considered.  
And these techniques were used to analyze which  
might be the most informative.  
These are different features of prices and things  
from the order book of the potential supply  
and demand curves for securities along the way.  
So there's a great amount that is being done  
and that's left to do.  
So let's summarize.  
Reinforcement learning is a technique  
where we learn by experience.  
And it works particularly well in financial markets.  
And these financial problems are ones that  
don't have a known solution.  
There is no answer on how to trade  
as there is an answer to the question, is this picture  
a picture of Einstein or of somebody else?  
So reinforcement learning starts with nothing.  
It learns from experience.  
It comes up with its own rules.  
It's valuable when the true rules are unknown.  
It's helpful when the data is noisy, which is absolutely  
the case in finance.  
It can help when there are transaction costs, when  
it's costly to acquire new information.  
One of the things about running simulations like this in a case  
I showed you, and especially in the microstructure case,  
is it can be difficult to really know how the markets would react  
without trading real money.  
We look at recorded data.  
And that recorded data does not have our presence there.  
So this is a tricky thing.  
And when we do want to make the jump from the lab  
to actual practice into implementation,  
we need to take into account the fact  
that we might make mistakes, and it will be costly to do so.  
We should only do exploration where  
we think it will be worth the costs and potential losses.  
And that's something that we can build  
in a very natural way in a reinforcement learning  
framework.  
Reinforcement learning is always provisional.  
It's always conditional.  
It's never completely converged on the perfect model  
of how things work.  
And two of the important parameters  
that we have to adjust that are at our disposal  
are the exploration rate and the learning rate.  
And we can set those to fairly humble values,  
where we're willing to assume that maybe we  
don't know everything.  
And that will leave us well positioned  
to adapt when markets change.  
And finally, we've seen that the great advantage  
of the approach that we've taken is interpretability.  
We can not only laugh all the way to the bank,  
we can see the profits that we generated  
through these simulations, but we know where they came from  
and why.  
If we built a black box trading strategy using a deep learning  
neural network, we might come up with profitable strategies.  
But we might not know why they were picked  
or how they were picked or which features were important.  
This was the simplest possible example.  
And of course, as I mentioned along the way,  
it can be generalized in many ways,  
including many more states, many more realistic conditions,  
and so on.  
But in addition to the possible practical applications,  
this set of algorithms gives us a laboratory  
for studying all kinds of things that do happen in actual markets  
and trying things out under controlled conditions.  
We can learn to trade.  
We can see how we learn, how we acquire information.  
We can adjust the parameters, see  
what are good learning speeds.  
We can see when we're doing well, when we're doing poorly.  
And then we can use these algorithms  
to learn about market dynamics-- in particular, market changes,  
market regime shifts, market breaks, market behavior  
restoration-- and take a look through the lens  
of these trading strategies, which put things  
on an economic basis, not just on a statistical basis,  
about how they process information.  
Reinforcement learning balances exploration, exploitation,  
and learning rates.  
They are a blend between finding out  
how the world works, finding out what's  
an optimal policy within that world,  
but always being ready to learn more along the way.  
It's an approach where we don't have a set of expert rules that  
tell it what to do.  
We don't have a set of statistical functions  
that we're trying to maximize or minimize.  
We give it goals.  
And we set it out to do the best it can to find those goals.  
And it did a fabulous job in the examples we saw,  
even working its way through very noisy, very random data  
to find some potential profits out in the markets.  
So thank you for your attention.  
And good luck in the casino of life,  
in the casinos of the real world,  
and perhaps in the financial markets.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
Reinforcement Learning (RL) offers a powerful framework for financial decision-making in environments where rules are uncertain, data is noisy, and markets are constantly changing. At the same time, its real value in finance lies not only in learning how to trade, but also in helping us understand market dynamics, adaptation, and the tradeoffs involved in acting under uncertainty.

Key Takeaways  
RL differs from other machine learning approaches by learning through trial and error, using rewards and feedback to improve decisions over time rather than relying only on fixed labels or static datasets.  
Financial markets are a natural setting for RL because they are noisy, adaptive, and often governed by unknown or shifting rules, making sequential decision-making and continual adaptation essential.  
An RL problem can be structured in terms of states, actions, rewards, and goals, with examples ranging from the N-armed bandit to trading problems involving buy, sell, hold, or portfolio-position decisions.  
The usefulness of RL in finance depends not only on its ability to discover effective strategies, but also on how well it adapts to changing markets, balances exploration and exploitation, and remains interpretable in practice.  
\`\`\`

Lecture 3: Large Language Models in Finance  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 3: Large Language Models in Finance, taught by Dr. Jillian Ross, who was a Ph.D. student in the Department of Electrical Engineering and Computer Science (EECS) at the time this lecture was recorded.

This lecture provides an introduction to large language models (LLMs) and their role in finance. We cover how LLMs work under the hood, where they are already being applied across financial services, and the critical challenges that come with deploying them responsibly in one of the world’s most complex industries.

Learning Objectives  
After this lecture, learners will be able to:

Explain how LLMs are built and trained at a high level.  
Identify concrete applications of LLMs across trading, financial advisory, and deal execution.  
Evaluate the key challenges of deploying LLMs in financial services, including hallucinations, regulatory scrutiny, data privacy, and security vulnerabilities.  
Critically assess the long-term implications of LLMs for the finance industry, including questions of accountability, the evolving role of human judgment, and what financial expertise means in an AI-driven world.  
\`\`\`

L3.1 What are LLMs?  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, I'm Jillian.  
I'm in the final year of my PhD at the MIT Laboratory  
of Financial Engineering, where I'm  
an MIT Presidential Fellow and a MathWorks Engineering Fellow.  
I'm extremely fortunate to be advised  
by Professor Andrew Lo, who you heard  
from earlier in the series.  
In this lecture, I'll give you an overview  
about the applications of large language models in finance.  
We'll go through in three parts.  
First, I'll give you a high-level overview of how  
large language models work.  
Second, how large language models have  
been applied to finance today.  
And third, the challenges, risks, and road ahead.  
Let's get started.  
Before talking about how LLMs are applied to finance,  
I want to lay the groundwork about what LLMs are.  
If you've seen this in other courses,  
feel free to skip ahead.  
Large language models are fundamentally  
statistical models, first trained on one simple task--  
predicting the next item or token in a sequence.  
The magic happens at scale.  
Billions of parameters and trillions  
of tokens of training data transform the simple objective  
into something surprisingly powerful in general.  
So since it's snowing in Boston today,  
let's take an example of "I love seeing palm trees at the blank."  
So the model now has to learn a probability distribution  
from the training data about what's likely to follow.  
So let's say it's learned that beach is most likely, followed  
by coast, then less probable options like sea, pool,  
boardwalk, shore.  
Now to know "beach" beats another word like "mountaintop,"  
the model must internalize that palm trees grow in called  
coastal tropical environments, not alpine regions.  
And so the key insight is something much deeper.  
A model that predicts next tokens with high accuracy across  
trillions of tokens cannot do so by simply memorizing.  
There are just too many possible contexts.  
So therefore, it must develop an internal model of the world--  
how people feel, how places relate, how events unfold,  
and how arguments are structured.  
Now, understanding this miraculous phenomenon  
is crucial to understanding what LLMs can and can't do.  
Let's now walk through the internals of a large language  
model.  
So the large language model is structured  
as a transformer architecture, which  
is defined by something called an attention mechanism.  
I'll talk about that in just a second.  
But let's start from the very beginning.  
The large language model breaks text down into subword units,  
called tokens, before processing.  
So in the example you see on the slide, "artificial"  
has been broken down into "art" and "ficial".  
These units are algorithmically chosen to balance both coverage  
and efficiency.  
So a single word in the human language  
can be one or several tokens in LLM language.  
Then each token is mapped to a high-dimensional vector, called  
an embedding.  
So now here's the essential part-- the attention mechanism.  
Every token looks at every other token  
and computes attention weights, which  
are scores for how much each other token matters  
in predicting what comes next.  
So if you look at the slide, this  
is a matrix, where you see, for example, that intelligence,  
which is the third column, is strongly  
predictive of transforming.  
So the model has learned some relationship  
between intelligence and transformation.  
And these attention weights are what  
gives the model genuine understanding of context.  
These aren't rules.  
They're learned relationships across the sequence.  
Now, after it goes through the attention mechanism,  
the final hidden state passes through what's  
called a linear projection.  
On the slide, you'll see something  
called an MLP, a Multi-Layer Perceptron.  
And essentially, that will result in a probability  
distribution over tokens.  
In technical terms, we do an operation  
called a softmax, which creates this formal probability  
distribution that sums to 1\.  
So now the model either picks the highest probability token,  
which is called greedy decoding, or it samples  
from this distribution, introducing  
controlled randomness that produces varied,  
natural-sounding output.  
This cycle repeats to generate one token at a time in what's  
called an autoregressive loop.  
OK.  
So that's a little bit about the internals.  
But how does the model learn that probability distribution?  
Well, there are roughly three steps  
in training modern language models.  
There's pre-training, post-training,  
and inference strategies.  
So in pre-training, a model's learned  
through next-token prediction, as we just discussed,  
or a slight variant called masked token prediction, which  
is the same idea, but some tokens are hidden mid-sentence,  
and the model fills them in instead.  
Both of these methods produce what's  
called a base model with broad world knowledge.  
So think of the base model like a brilliant person  
who has read everything ever written.  
They have encyclopedic knowledge,  
but they have no idea how to be useful to you specifically.  
The model will continue to generate text,  
but it won't necessarily answer questions helpfully.  
And that's where post-training comes in.  
So this is where we shape raw capability into something  
that follows instruction, avoids harm, and feels  
like an assistant.  
And there are broadly two buckets of post-training  
strategies--  
Supervised Fine-Tuning, or SFT, and Reinforcement Learning, RL.  
And you can use these separately, sequentially.  
There are a variety of methods.  
You might use one or both of them.  
In SFT, you show the model thousands  
of examples of ideal conversations in the right tone,  
format, and level of detail.  
And then the model learns, this is what good looks like.  
Think of it as your apprentice.  
In reinforcement learning, you try  
to teach the model to learn judgment  
as well because imitation only gets you so far.  
So the model needs to learn when one response is  
better than another.  
There are many, many variants of RL.  
I'll talk about two today.  
One is PPO, and one is DPO.  
PPO stands for Proximal Policy Optimization.  
And in this approach, you train a separate reward model  
that scores the model's outputs like a judge,  
and then uses that score to push the language model toward better  
responses.  
This is an extremely powerful method,  
but it's very complex because you're  
training two models-- that base language model  
as well as the reward model.  
So the second approach, DPO, or Direct Preference Optimization,  
skips that separate reward model step entirely.  
You show the model pairs of responses, one better, one  
worse, and then you train it to directly prefer the better one.  
It's way simpler, and it often works just as well.  
Finally, there are inference strategies.  
This is probably the most straightforward approach  
you can take.  
This is after training is done.  
We're no longer updating the model weights.  
There are still methods we can do to improve performance  
at runtime.  
So I'll talk through a few now.  
The first being prompt engineering.  
This is born from the observation  
that how you frame the question changes what you get.  
So for example, in zero-shot prompt engineering,  
you just try to find the best possible way  
to ask the question.  
In few-shot prompt engineering, you give the model  
a few examples first about what you're looking for,  
and then you ask the question.  
In chain of thought, you explicitly  
ask the model to reason step-by-step before answering.  
And these methods have been shown to dramatically improve  
accuracy in some cases.  
Now your next option is Retrieval Augmented Generation  
or RAG.  
These language models have knowledge cutoffs.  
And so to keep the knowledge up to date,  
you actually want to equip it with the most relevant,  
up-to-date documents at inference time.  
And so this RAG approach determines  
what documents you retrieve and then serves them up to the model  
to then read and then incorporate  
the content into the answer.  
And with this method, now citations  
become possible for knowledge, which  
can be very important, particularly  
in many finance use cases.  
Finally, there are agentic frameworks.  
So instead of a one-shot question/answer,  
the model instead has a loop in which it first plans, acts,  
and then observes the result of acting,  
and repeats that over and over.  
So by acting, the model can call tools, it can browse the web,  
it can write and run code.  
And now the model becomes its own agent,  
able to do things on its own, not just a responder.  
So lastly, I want to talk about test-time scaling.  
You run the language model multiple times  
on the same problem and pick the best answer,  
or you have it generate a long internal reasoning  
trace before responding.  
Turns out, if you give the model more time to think,  
it often comes out with better training.  
And this is the insight that led behind the latest  
version of reasoning models, like OpenAI's o1 or o3.  
So now let's talk about scaling in a little bit more detail.  
Advanced reasoning capabilities, code generation,  
multilingual understanding weren't explicitly programmed  
into the models.  
They emerged naturally as we scaled up  
model size and training data.  
And this development caught even researchers off guard.  
We've seen capability growth outpace  
what traditional theoretical scaling  
laws would have predicted.  
And what we find is that you can actually  
scale up both what we call train-time compute and test-time  
compute.  
So if you look on the screen to the left,  
you see what happens when you give the model more  
compute at training time.  
Now you can see that as you move across the x-axis, which  
is compute, the y-axis, or accuracy, increases.  
And now if you look to the right, we see the same plot.  
But now this is when we scale test-time compute.  
And again, we see a very strong positive relationship.  
So now the big open question is, will this relationship continue  
or will we soon hit a plateau?  
And if we do hit a plateau, we might  
need to think about something more fundamentally  
to do differently than how we're training models today.  
So I just want to keep this in mind  
as we start looking towards the pitfalls of today's LLMs  
and think about the future for deploying LLMs in finance.  
So finally, I'd like to close this section  
by painting a brief picture of the LLM landscape.  
Not all LLMs are the same, and there are many variants,  
so I just want to outline three different axes for you  
to consider, though there are likely many more.  
So the first is proprietary models  
versus open-weight models.  
Today, there seems to be a persistent trade-off here.  
Proprietary models offered by tech companies and startups  
typically offer cutting-edge performance,  
but the internals of the model are hidden  
behind what's called an API.  
And so you don't get that much control,  
and you also have to send your data externally.  
Now open-weight models give you more control.  
You can keep them on your own computers.  
They usually have lower costs, and they  
offer better data privacy.  
But today, they're unfortunately usually less performant.  
Now, open-weight models have started to catch up,  
but it's unclear if the trade-off between performance  
and data privacy, for example, will go away.  
And I bring this up because for financial institutions,  
this is pretty critical.  
You're balancing the desire for the latest capabilities  
against the need to keep sensitive customer transaction  
data secure.  
Now the second axis to consider is  
general versus domain specific.  
So this is a question of whether you  
build domain-specific models, like Bloomberg  
did with Bloomberg GPT, or use general models  
with inference strategies that we previously discussed.  
Now, the good news is both approaches seem to work.  
You can either train your own finance-specific LLM,  
or you can use a general LLM and use prompt engineering, or RAG,  
to improve it toward the finance use case.  
So there seems to be some flexibility here,  
depending on resources and priorities.  
Now the last axis I'll tell you about  
is on-premise versus cloud deployment, which  
is closely related to the proprietary  
versus open-weight axis.  
So for many institutions, it's non-negotiable to keep your data  
on premise due to various governance and compliance  
requirements.  
So the trade-off is, on-premise deployment  
will limit your model options to typically those open-weight  
models.  
And today, you usually have to accept  
slightly lower performance compared to frontier cloud  
models.  
But we'll see if that holds in the future.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.2 Applications in Finance  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now let's transition to part two.  
We're shifting focus to real-world applications  
of large language model in finance.  
Finance is fundamentally a language-based industry.  
Think about all the unstructured text that drives decisions--  
SEC filings, earnings call transcripts, internal memos,  
legal contracts, research reports, client emails.  
Until now, processing this volume of language at scale  
has been practically impossible.  
But large language models change that equation entirely.  
So for this next section, we'll focus on three major application  
areas where large language models are already  
being deployed or show significant promise-- trading,  
financial advisory, and deal execution.  
For each, we'll examine both the opportunities  
and the risks because with powerful tools  
comes important responsibilities.  
So first, let's talk trading.  
Markets have always been driven by language-- as I mentioned,  
earnings calls reports, central bank guidance, analyst reports,  
the news--  
and large language models change the game with faster and richer  
semantic understanding, so you can  
build more sophisticated trading signals,  
conduct research faster, and make better informed decisions  
across all styles of trading.  
And so now I'll talk through just two of the main benefits  
of using LLMs in this context.  
First is that LLMs save time.  
So for quantitative-based trading strategies,  
you can use large language models  
to generate code that power backtesting, data pipelines,  
and strategy prototyping.  
And for fundamental trading strategies,  
you can use LLMs to summarize and synthesize  
earnings reports, macro research, and analyst notes  
at scale.  
And the second is that LLMs create an edge  
or what those in industry call alpha.  
So LLMs enable you to spot novel connections  
across a large universe of companies, surface anomalies  
and key terms from massive data rooms,  
parse Fed minutes, governor speeches  
for forward-looking signals of what's to come,  
and extract entities and events from breaking news  
to catch developments before they're fully  
priced into the market.  
Note that these two concepts are not entirely unrelated.  
Saving time can actually be a source  
of alpha in and of itself.  
But there are two critical questions  
to explore about using large language models in this context.  
First, can we actually trust LLMs to make autonomous trading  
decisions?  
And what are the risks and safeguards needed?  
Second, what happens to market structure and dynamics  
if LLMs become major market participants?  
How does this reshape trading and volatility?  
So the image that you see on the slide  
shows a leaderboard from a startup called Nofl  
of LLMs trading real equities.  
And what you can see is that most LLMs today  
actually lose money, and sometimes  
in substantial amounts.  
In my PhD research, I'm working on a paper,  
unpacking the relationship between LLMs and market  
volatility and efficiency.  
And the research and the results from Nofl  
suggest that out of the box LLMs today  
would increase market volatility if they were significant market  
participants.  
But as LLMs become more specialized and generally more  
competent, market volatility may actually  
decrease once LLMs are widely deployed.  
So these questions get at the heart of whether LLMs in finance  
is a tool for humans, or if they're independent agents.  
And it begs the question about what systemic risks emerge  
as adoption scales.  
So now let's turn to financial advisory.  
Financial markets, investment products, and taxes  
are all highly complex, and many retail investors  
like you and I benefit from financial advice  
from a professional.  
Financial advice is very communication heavy.  
You have lots of client interaction,  
complex products to explain, and you  
translate all of these complex ideas into plain language.  
Now, today, financial advice is usually  
human driven, and therefore hard to scale and give people access  
to.  
Robo advisors are automated solutions that exist,  
but they have their own limitations.  
I believe there is promise for large language models  
to enhance both automated and human-driven advisory.  
So let's start in the back office.  
I believe here, largely, large language models  
will help advisors gain efficiency.  
They can transcribe and summarize client meetings  
automatically and feed them into a client database  
for easy reference, turn raw portfolio data  
into polished reports with narrative context,  
draft compliance documents, and help  
with performing various regulatory requirements,  
like suitability checks.  
Then there's the front office.  
Here, I think large language models can create a better  
client experience by keeping clients up to date, breaking  
down these complicated concepts, creating very personalized  
plans for them.  
Because an LLM, unlike a human, can answer your questions  
at midnight, 24 hours a day.  
So LLMs can handle both the administrative burden  
and the client-facing communication,  
which frees up human advisors to focus on relationship building  
and providing strategic guidance.  
Now, as Professor Lo mentioned in an earlier lecture,  
we've been looking at the capacity for large language  
models to provide financial advice themselves,  
and we have identified three focus areas for our research.  
The first is domain-specific expertise,  
which we believe is the prerequisite for deploying  
large language models in this context.  
And this relates to the point that we  
talked about earlier, which is if large language models can't  
make sound trading and investment decisions,  
we would hesitate to put them in front of a client  
to give financial advice.  
The second component is human-LLM collaboration.  
So if we assume LLMs are sufficient financial experts,  
we then have to turn to the question of how retail investors  
should interact with them.  
And in our research at the LFE, we  
found that retail investors are open to interacting  
with large language models, and large language models  
are effective at changing their beliefs.  
So now let's turn to the third component, which I would argue  
is the most important, ethics and fiduciary duty.  
So let's suppose LLMs are financial experts,  
and they're widely adopted by retail investors.  
How do we ensure that LLMs provide trusted ethical advice?  
This is a complicated question, one  
that will involve speaking and working with regulators  
across the world to make sure that LLMs don't lead investors  
astray.  
Now let's turn to deal execution.  
This one is personal to me because one of my family members  
is an investment banker and spends many hours synthesizing  
and writing spreadsheets and PowerPoints for the deals  
he works on.  
These deals may take a variety of forms.  
For example, a company may be trying  
to sell itself or spin out a division of itself.  
And I believe LLMs are valuable here because they  
can handle the heavy lifting of synthesizing  
information, creating summaries, generating first drafts, which  
will free up time for higher level judgment  
and client-facing work.  
In this context, let me outline three concrete applications  
where LLMs add real value.  
So first is processing the data room.  
When you first look at a deal, you  
get an enormous amount of information about a company.  
Instead of manually reviewing thousands of due diligence  
documents, LLMs can quickly surface materials and red flags  
across the data room.  
The second is comparable analysis.  
So as you're trying to understand the company,  
you'll look at companies that are similar to it.  
And LLMs can help extract and structure  
financial data from SEC filings and precedent transactions  
to help you build out these comps faster.  
And the third part is post-deal.  
So after the deal, you'll probably  
have some operational suggestions for the company.  
LLMs can summarize operational documents from the target  
company and cross-reference them to identify integration issues  
or operational insights early.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.3 Challenges, Risks & Road Ahead  
(Caption will be displayed when you start playing the video.)  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So we just talked about three use cases--  
in trading, financial advisory, and deal execution.  
But I'd be remiss if I didn't point out  
there are many real obstacles that we  
face when actually deploying large language  
models in financial services.  
These aren't theoretical concerns.  
They're ones that we're facing today.  
The first is hallucinations.  
LLMs can sound completely convincing  
while being completely wrong.  
And this is particularly dangerous in finance,  
where accuracy and trust really matters.  
And what lots of research has found  
is that the model doesn't know what it doesn't know.  
And so it's really important that we  
develop a significant degree of oversight  
over these models in the near term.  
Second is regulatory scrutiny.  
So regulators want to understand why  
a financial decision was made.  
However, research has shown that LLMs can often misstate  
why they made a decision.  
So what I'm showing here on the slide  
is research from Anthropic that shows that LLMs will often not  
tell you the real reason as to why they made a decision.  
And so therefore, we can't necessarily  
just ask a language model why it made a decision  
and trust its output.  
We need further explainability and audibility built  
into our systems.  
Then we turn to data privacy and compliance,  
which we spoke about a little bit earlier.  
We can't just send sensitive information to external parties  
because it creates massive compliance and legal exposure.  
And this in turn means we often need to run models on premise  
or use private deployments.  
The last point I'll talk about is security vulnerabilities.  
So as LLM workflows become more automated,  
these agentic inference strategies I mentioned  
become more commonplace, LLMs become targets.  
One example is a prompt injection attack,  
where someone can manipulate the input to an LLM  
to make the model behave unexpectedly,  
which is a real threat that we need to guard against.  
These challenges are interconnected,  
and they're why responsible LLM deployment in finance  
requires careful architecture government, risk management,  
and most importantly, collaboration.  
Now, I want to note that the pace of change in this field  
outstrips any formal training that I can give you,  
and so you need to build your own information pipeline.  
Don't rely on secondary sources and summaries.  
Go directly to primary sources for accuracy and depth,  
and use an LLM to help you understand it.  
So let me just point to three different categories  
you might want to use.  
The first is academic research.  
There is a website called arXiv, which is my daily feed,  
and I would suggest it for you as well.  
They'll give you the latest on how academics are thinking  
about large language models.  
I'd also point you to various journals and conference  
proceedings that can give you a greater  
notion about new methodologies as they emerge.  
Second would be financial institutions.  
The SEC and FINRA release reports in the US,  
and regulators around the world, including the EU AI Act,  
are providing guidance on how regulators and financial leaders  
are thinking about AI risk.  
A third source of information would  
be foundation model providers.  
So when OpenAI and Anthropic or others release a new model,  
read the technical paper, and particularly pay attention  
to the methodology section that tells you what changed  
and what the limitations are.  
Let me close with the road ahead.  
Large language models are uniquely positioned for finance  
because they can handle unstructured language at scale.  
And finance is drowning in language--  
earnings calls, regulatory filings, research reports,  
client communication.  
I think that finance will become a proving ground for LLMs  
across other industries.  
What works here will inform deployment elsewhere,  
partially because finance is one of the most complicated  
industries on the planet.  
Markets move extremely fast, things change by a millisecond,  
and there are extremely high stakes.  
In the near term, we're already seeing how large language models  
are affecting the industry.  
These tools are augmenting practitioners,  
compressing the time between getting information  
and turning it into actionable insight.  
This is happening across trading, financial advice,  
and deal execution.  
But in the long term, the bigger question  
isn't whether LLMs add value.  
It's how they reshape the work and the nature of the industry.  
Do analysts spend less time on data gathering,  
more on judgment?  
Do roles shift altogether?  
And what does financial expertise even mean when a tool  
can read 10,000 pages overnight?  
How much can we rely on these models for decisions  
that carry real consequences?  
And where does human judgment have to stay in the loop?  
And when things go wrong-- a bad trade, a missed risk,  
a regulatory violation-- who's accountable?  
These are all critically important questions  
that we all have to answer, and I hope  
we'll answer them together.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
Large Language Models (LLMs) are transforming finance by unlocking the ability to process the industry’s vast amounts of unstructured language at scale. However, realizing their full potential requires navigating significant technical, ethical, and regulatory challenges that are still very much a work in progress.

Key Takeaways  
Transformer-based LLMs are next-token predictors that develop a surprisingly powerful internal model of the world through training at scale, and how you train, fine-tune, and prompt them significantly shapes what they can do.  
Finance is a natural fit for LLMs because the industry runs on unstructured language, e.g., earnings calls, filings, contracts, and research reports, at a scale previously impossible for humans to process alone.  
LLMs are already adding value across trading, financial advisory, and deal execution, but whether they should act as autonomous agents versus human-assistive tools remains an open question.  
Responsible deployment in finance requires tackling interconnected challenges around hallucinations, explainability, data privacy, and security.  
\`\`\`

Assignments  
\`\`\`  
Skip to main content  
Overview  
In this assignment, learners will apply the core ideas from the module across three parts covering fintech and AI, RL in finance, and LLMs in finance. The assignment is designed to reinforce the module learning goals by testing learners’ ability to explain how AI is reshaping finance, analyze the role of narratives and reasoning under uncertainty, apply the core concepts of RL, and assess the opportunities and challenges of deploying LLMs in financial settings.  
\`\`\`

Skip to main content  
Question 1  
0.0/1.0 point (graded)  
Which of the following best describes how modern machine learning differs from older expert systems?

It relies on small data and highly complex hand-coded rules

It relies on big data and relatively simple learning rules

It avoids the use of data whenever possible

It is based on narratives rather than computation

It works only in finance  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
Which of the following best captures the lecture’s view of how humans often make decisions under sparse information?

By using numerical optimization

By relying on raw facts without interpretation

By constructing narratives that connect information meaningfully

By ignoring uncertainty

By maximizing data size  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Why can using a modern LLM in a historical backtest create a problem?

Because LLMs are too slow for backtesting

Because LLMs may contain knowledge that was not available at the historical date

Because LLMs cannot process financial text

Because backtests require only structured data

Because LLMs can only be used in live trading  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Which of the following best defines technical analysis?

An investment method based on graphs of stock price charts

An investment method based on accounting valuation relationships

An investment method based on legal contract review

An investment method based on macroeconomic storytelling

An investment method based on drug development data  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Which of the following is the best description of deep technology in the lecture?

Technologies limited to social media

Technologies that include scientific research

Technologies used in consumer apps

Technologies that expand fundamental human and societal capabilities

Technologies that make small convenience improvements  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Question 1  
0.0/1.0 point (graded)  
A trading algorithm receives market information, chooses whether to trade, observes the outcome, and updates its future behavior. Which feature makes this an RL-style problem rather than a standard supervised learning problem?

It uses numerical inputs

It requires a training set with fixed labels for each correct action

It makes sequential decisions and learns from the consequences of actions

It assumes the environment never changes

It avoids any uncertainty  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
In a financial RL setting, which of the following best describes a state?

The final profit at the end of the strategy

A list of all future prices

A reward received after an action

A permanent rule that never changes

Information summarizing the market and portfolio at the current moment  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Why is exploration important in a financial learning problem?

Because the agent already knows the optimal action in advance

Because exploration guarantees the best reward immediately

Because exploitation is not useful

Because finance contains no noise

Because trying alternatives can reveal better strategies than the current favorite  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Suppose a trading strategy looks excellent in a frictionless simulation but performs poorly once transaction costs are added. What does this most directly illustrate?

That rewards should ignore implementation details

That states are irrelevant in trading

That RL fails when costs exist

That transaction costs can materially change the reward structure of the problem

That financial markets become non-stationary once costs are included  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Why might RL be useful even when a trading strategy itself is not deployed in production?

Because RL can also be used to study learning, adaptation, and market dynamics

Because RL automatically eliminates model risk

Because RL outperforms other methods in live trading

Because RL removes the need for interpretation

Because RL can only be used in simulation  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Question 1  
0.0/1.0 point (graded)  
Why are LLMs especially relevant to finance compared with some other industries?

Because financial decisions are made without human input

Because finance has less compliance requirements

Because LLMs only work on financial tasks

Because finance relies heavily on unstructured language in documents, calls, contracts, and communication

Because market data is entirely unstructured and never numerical  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
A bank is deciding whether to use an LLM as an internal assistant for analysts or allow it to make autonomous decisions directly. What broader issue from the module does this choice most clearly raise?

Whether language models can be used only for translation

Whether LLMs should augment human judgment or act as independent agents

Whether financial data should remain structured

Whether cloud computing exists

 Whether all AI systems must be open-source  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Why is explainability a particularly important issue for LLMs in finance?

Because financial institutions never need to justify decisions

Because regulators ban machine-generated language

Because verbal explanations from a model may not reliably reveal the true basis of its output

Because LLMs can explain only structured spreadsheets

Because correct models are self-evident  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Which of the following best captures a realistic tradeoff in financial deployment of LLMs?

Higher privacy and control may come with lower model performance

Better privacy guarantees better performance

Open-weight models are superior on every dimension

Proprietary cloud models are acceptable for most institution

Compliance and data governance do not matter  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Which of the following best describes the module’s long-run perspective on LLMs in finance?

The main issue is whether they have any possible use

The long-run goal is to remove regulation from financial AI

The main challenge is whether LLMs can summarize a document

The key questions concern responsible deployment, accountability, human oversight, and how work in finance may change

The best approach is to ignore LLMs until all risks disappear  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
This assignment assessed learners’ ability to connect the module’s three major themes: the foundations of fintech and AI, the use of RL in financial decision-making, and the opportunities and risks of LLMs in finance. It emphasized not only conceptual understanding, but also the ability to apply these ideas to realistic financial contexts and deployment challenges.  
\`\`\`

Module Summary  
\`\`\`  
Skip to main content  
Module Summary  
In this module, you explored how AI is reshaping finance, from the broader relationship between fintech and AI to the specific roles of RL and LLMs. Through lectures and assessment, you developed a conceptual understanding of how AI can support financial decision-making, market learning, and language-based analysis, while also examining the practical limits and risks of deploying these tools in real financial settings. You are now equipped to connect foundational AI concepts to financial applications and to evaluate both the promise and the challenges of AI in finance.

Key Takeaways  
AI and LLMs are transforming finance by expanding the scale, speed, and range at which information can be processed, interpreted, and used in decision-making.  
Human intelligence often relies on narratives as well as data, which helps explain why language, reasoning, and context matter so much in financial applications of AI.  
RL provides a useful framework for financial problems involving sequential decisions, uncertainty, adaptation, and the tradeoff between exploration and exploitation.  
In finance, RL can be used not only to learn trading strategies, but also to study market dynamics, learning behavior, and adaptation in changing environments.  
LLMs are especially relevant to finance because so much of the industry depends on unstructured language, including filings, earnings calls, contracts, research reports, and client communications.  
The successful use of AI and LLMs in finance requires careful attention to real-world challenges such as bias, interpretability, privacy, security, accountability, and the risks of misuse in practice.  
We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.  
\`\`\`



---

# Course Conclusion & Acknowledgments Transcript

**INSTRUCTOR**: Hello, everybody, and congratulations on completing the AI and Finance course module. We hope you enjoy taking this course as much as we enjoy teaching it. More importantly, we hope you leave this course as inspired as we are by the potential to combine financial engineering and artificial intelligence to solve multiple challenges faced by individuals and institutions across all industries, including the financial sector.

Before we sign off, we'd like to offer a few heartfelt thank yous to the many people who made this course possible. You know how at the end of every movie, there's a long list of names that continues well after the actors' credits have rolled? I'll admit, I never fully appreciated why so many people were involved in making a film until we began recording these courses ourselves. Going through that process taught me that there is an entire community of contributors behind the scenes in pre-production, production, post-production, and distribution all working together to bring something like this to life. So many people dedicated their time, talent, and energy to making this course possible. And we'd like to recognize and thank them by name.

First, we want to thank **David Chotin**, Manager of Project Administration with Online Worldwide Learning Services, for bringing this opportunity to us. We'd also like to thank **Dimitris Bertsimas**, Vice Provost for Open Learning and Associate Dean for online education and AI, for his leadership and vision. Creating foundational AI fluency is an important priority for everyone. And initiatives like Universal AI level the playing field by giving all viewers a chance to learn about AI, regardless of their situation. **Laura Crook Brisson**, Intellectual Property Coordinator, provided invaluable guidance in navigating the many intellectual property considerations associated with the course materials.

And as far as production goes, a very special thank you goes to **Lana Scott**, Assistant Director on the Open Learning Video team, who guided and encouraged us throughout the filming process. She was there to keep us on track when we drifted off course, and equally there to celebrate with us when things went well. We also want to thank **Nick Vandenberg**, MITx Senior Editor and Videographer, who somehow managed to make us look as good as possible under those very hot studio lights and carefully selected the best takes for this course.

During post-production, **Mary Ziegler** ensured online accessibility for all of the videos and helped prepare the transcript. We're also grateful to **Shira Fruchtman**, Assistant Manager of Educational Technology and Lead Learning Designer, who helped bring the course together and ensure that every module was polished, proofed, and ready for you.

By now, you're probably getting a sense of just how complex a project like this can be and why so many talented people were involved. Coordinating and directing all of these moving pieces is no small task. And I'd be remiss if I didn't acknowledge the incredible support I received from **Andres Gallego** and **Viniqua Gooding**, my assistants, as well as **Jayna Cummings**, Executive Director of the Laboratory for Financial Engineering. Without their efforts and support, I simply would not have had the bandwidth to take on a project of this magnitude.

Finally, let's turn to the course itself. I'd like to thank **Paul Mende** and **Jillian Ross** for their many contributions to the course and for keeping me focused and grounded throughout the process of developing and teaching it. Their example inspires me to work harder and be better every day. We also had the great fortune and privilege of working with **Chaoyi Zhao**, an LFE Postdoctoral Associate who, in addition to serving as the teaching assistant for the MIT Machine Learning course that Paul and I taught this past semester, also shared responsibility for course administration with Shira. Nearly every video and question you encountered was edited, refined, or developed by Chaoyi. And this course simply would not be what it is without him. He did an outstanding job as TA for Paul and me. And he's clearly on his way to becoming a terrific assistant professor of financial mathematics at PKU.

Last, but certainly not least, on behalf of all of us here at MIT, thank you. Thank you for your time, your effort, and your commitment to this course and for allowing us to be a small part of your journey in learning about the science, technology, and business of AI. We wish you great success in all of your future endeavors.
