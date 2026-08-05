Generative AI, the Future of Work, and Human Creativity  
\`\`\`  
Module Overview and Learning Goals  
\`\`\`  
Skip to main content  
Module Overview  
Welcome to Generative AI, the Future of Work, and Human Creativity\!

This module explores the frontier of generative artificial intelligence and its profound implications on creative problem-solving, decision-making, and multimodal content generation. As GenAI becomes an increasingly integrated part of workflows across industries, understanding how it complements and challenges human cognition is essential. From creative applications like storytelling and design, to decision-support systems in high-stakes environments, and all the way to advanced diffusion models powering text-to-image generation, this module provides a holistic view of how humans and AI can collaborate effectively.

Across these sessions, we will unpack how generative AI tools transform ideation, enable novel forms of expression, and generate high-fidelity visual content from natural language. We will also critically examine the limits of automation in judgment tasks and the risks of over-reliance. Finally, we delve into the technical mechanisms underlying diffusion models, giving students a foundational grasp of how leading systems like DALL·E and Midjourney operate.

Learning Goals  
By the end of this module, learners will be able to:

Understand the landscape of GenAI in creative tasks and identify key GenAI tools and use cases in idea generation, storytelling, design, and content production.  
Evaluate the balance between human judgment and AI outputs and recognize when and why human oversight is critical in AI-assisted decision-making, and assess risks associated with full automation.  
Explain the fundamentals of diffusion models and describe how iterative denoising processes create realistic images from noise, as well as understand the architecture and training behind these models.  
Use embeddings to guide image generation from text and explain how systems like CLIP align text and image embeddings and how they enable controllable text-to-image generation.  
Critically assess real-world applications of generative AI and analyze opportunities and limitations in domains such as entertainment, architecture, healthcare, and science, including ethical and operational considerations.  
\`\`\`

Lecture 1: AI and the Future of Work  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 1: AI and the Future of Work, taught by Professor Léonard Boussioux, Assistant Professor of Information Systems at the University of Washington.

This lecture provides a foundational overview of how artificial intelligence is reshaping the future of work. It explores the spectrum of cognitive tasks—from repetitive and routine to non-routine and creative—and how AI technologies increasingly perform or augment these tasks. Special focus is given to “judgment” as a category of decision-making that blends knowledge, experience, and values. Through real-world examples, learners will examine where AI is most effective, where human input remains essential, and how work is being restructured around this evolving partnership.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define different types of cognitive tasks and evaluate their susceptibility to automation.  
Distinguish between knowledge, prediction, and judgment in the context of work.  
Identify which components of human judgment are difficult to replicate using AI.  
Reflect on the limitations of data-driven systems and the ongoing need for human discretion.  
\`\`\`

L1.1 What is Generative AI?  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, everyone.  
I'm Leo, and I'm super excited today to talk more about AI  
and the future of work.  
We are going to investigate how the technology is impacting  
the world, society, businesses.  
And with this lecture, you'll be able to understand better  
how you can be ready for it.  
So here are the learning outcomes for today.  
We are going to evaluate the business impact of generative AI  
by analyzing its economic potential.  
We'll be able to assess the value creation opportunities  
and the critical risks and limitations  
in organizational deployment.  
We'll also investigate different human-AI collaboration  
perspectives.  
And we'll look into the concept of the jagged frontier  
such that you are ready to know where  
AI can help you or potentially harm your tasks.  
Very importantly as well, we'll assess the ethical and societal  
implications of AI by looking into the sustainability,  
the privacy, the regulatory considerations such  
that you can feel ready also to implement responsible AI  
implementations.  
So you probably heard about generative AI  
because of ChatGPT.  
It's also a big buzzword.  
What was very impressive is that ChatGPT reached 100 million  
users in just two months.  
It's the fastest growing technology ever.  
And then lots of people are also impressed  
by how much money, for instance, OpenAI  
is seeking to accelerate this whole deployment  
and go towards what is called artificial general intelligence.  
And here, you can see Sam Altman, the CEO  
of the famous OpenAI company.  
Also, in the stock market, it's going wild.  
You can see, for instance, Nvidia,  
which is a provider of very important resources for AI.  
They enable the training of the models with special computer  
architectures.  
Everybody is now investing in those  
because lots of big tech companies want those resources.  
And there is a huge demand for this.  
So let's see where we are.  
Remember from the previous lectures  
about the differentiation between AI,  
machine learning, deep learning.  
Remember that large language models and generative AI  
is just a small part of the whole landscape.  
And here, today, we are going to talk  
about how these little parts can impact, in fact, all businesses.  
But in general, we'll also talk about how AI will also  
influence all of it.  
Some people call large language models  
a general-purpose technology because the adoption  
is extremely rapid, and they can tackle so many different areas.  
They can also be compared with humans  
in some famous benchmarks.  
And they reach sometimes superhuman performance.  
It's also looking like the models from generative AI  
may have a huge impact on the world and businesses,  
potentially a $2.6 to $4.4 trillion  
annually in economic contribution.  
And it could also automate lots of tasks.  
Does it mean it will replace you?  
Not necessarily.  
In fact, it can augment our work.  
And this is the whole point of those lectures,  
to show you how you can leverage the technology the best way  
possible.  
End of transcript. Skip to the start.  
\`\`\`

L1.2 AI and the Future of Work  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's look more into the generative AI that  
can impact the future of work.  
Lots of very exciting studies around how having access to AI  
may potentially help you in all sorts of professional tasks.  
So here, for instance, there is this famous paper  
that showed that BCG consultants who had AI  
were able to be much more efficient  
and have higher quality of tasks compared to the people who  
did not use AI.  
And then there is the concept of the jagged frontier of AI.  
What does it mean?  
It means that AI can be good at certain tasks  
and terrible at others, while for humans, those tasks look  
equally difficult. And this is very important for you  
to understand when AI can help you or harm you.  
Because it turns out that in some situations, if you use AI,  
you'll end up being worse than if you did not use it.  
So we'll look more into this in this lecture.  
So let's look at a task inside the frontier.  
For instance, if you ask AI, like ChatGPT,  
to summarize a text or write an email,  
it's extremely easy for the model  
and it will go much faster than you, typically.  
However, if you ask AI to solve some math equations  
or create an infographic that's outside  
of the current realm of the models,  
they can do it, but potentially with lots of mistakes.  
So it's important to understand for you, maybe,  
the simple equation might actually look  
super hard for an AI model.  
And sometimes some tasks are in between.  
The AI can sometimes get it right,  
sometimes get it with a few mistakes.  
So it's important to understand where you are.  
For instance, if you want the model  
to help you write a project proposal,  
you may need to edit this.  
If you want the AI to evaluate the quality of an idea,  
it's unsure if you can really trust the judgment.  
And as models evolve, this frontier is going to move.  
This is why it's important for you to learn where it's moving  
and to quickly onboard with the latest technology,  
such that you can feel ready to use the technology when  
relevant.  
And then that's part of my job constantly,  
to try those models in so many different settings  
to see, OK, now this model can help me  
in this specific situation, or this new model is still not  
good enough to help me in what was already too  
hard for the previous versions.  
In this study, there are lots of very exciting graphs.  
For instance, in this one they show  
that generative AI can boost or hurt performance,  
depending on the type of task.  
For instance, if you use GPT 4 for creative product innovation,  
people really benefited from this.  
However, when it came to business problem solving,  
the consultants who used it ended up  
being a bit worse than if they did not use AI.  
Other interesting graphs-- when generative AI can potentially  
improve the performance of the low-performing employees.  
Indeed, it helps everyone to get upskilled,  
and the experts don't benefit as much because they sort reached  
their top level expertise.  
It depends on the setting, of course,  
but this is really good news because it really provides  
opportunities for everyone to learn new skills  
and potentially perform much better.  
Regarding creativity, also other interesting insights.  
AI can really boost your personal performance.  
However, if you take the whole crowd as a whole,  
it may hurt the collective creativity  
because the ideas generated by AI tend to always be the same.  
While if you reach for the whole crowd,  
you may have many more ideas.  
So we'll investigate this in the next lecture.  
Also, lots of people believe that because of AI, this  
stifles their creativity, meaning  
that they feel like they ask too much from AI  
and they stop using their brain.  
I don't want this to happen for you.  
This is why we have lots of opportunities  
to discover how instead, you can have an even better creativity,  
thanks to generative AI.  
End of transcript. Skip to the start.  
\`\`\`

L1.3 AI Technologies and Their Applications  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now let's talk more about  
how you can work with the technology.  
There is a new form of division of labor,  
meaning new ways of collaborating.  
So now we'll use metaphors about how we can collaborate with AI,  
and I will talk about how you can be  
a centaur with AI or a cyborg.  
Being a centaur is the analogy with this mythical creature,  
where you have someone who is half human and half a horse.  
So you have two identities.  
When it comes to AI, you have, for instance, a specific task.  
Are you going to do it yourself with no AI?  
Or potentially you are just going  
to ask AI to do it entirely.  
So the goal is to figure out when  
you should delegate something to AI  
or when you should just do it yourself.  
And some people, they think, OK, I  
want AI to ghostwrite my content.  
The other analogy is being a cyborg, meaning having  
AI integrated with yourself.  
For instance, you are going to do your task  
by being at the same time yourself  
and asking the AI to help you on the go,  
asking AI to give you feedback.  
And this is called sometimes the "AI in the loop" framework,  
meaning that you start with something, you ask for feedback,  
you iterate on this, and you keep cocreating.  
Those two strategies can be helpful for different tasks.  
For instance, if you want to write a piece of code  
that you know AI can do extremely well,  
you just delegate.  
Some people also use it to do their homework.  
But then the goal is to also learn.  
This is why the cyborg approach can be very helpful.  
For instance, if you want to write a very complicated piece  
of code, you may ask AI to first give you a potential outline.  
You are going to edit manually this outline.  
And then you can ask AI to do the section 1 of your outline.  
Then potentially you make minor corrections,  
and then you go to the section 2\.  
And then on the go you are going to build your content.  
So now let's dive more into how you can leverage also  
tools for the collaboration with AI.  
For instance, lots of Copilot, it's now a big buzzword.  
Potentially, for instance here, as you can see,  
you can have on PowerPoint a prompt  
that would directly create an entire slide deck for you.  
Maybe it can solve lots of time.  
So here is an example where you can use a Copilot to help you  
with a presentation generation.  
You can potentially write some prompts on the site,  
meaning some text, and then immediately you  
get an entire presentation ready.  
So it's a new way of working with the tools  
with natural language interface.  
It can be extremely valuable and save a lot of time.  
Same with spreadsheets.  
You would be able, for instance, to load your data  
and ask for a direct analysis of the whole content.  
It can also save lots of time and enable you to focus directly  
on the value you want to extract and not necessarily onto,  
how do I code this cell?  
Or how do I mix all those informations together?  
Also very valuable, having a Copilot for writing emails.  
This can also save a lot of time because you can potentially  
have the AI draft the first answer because it can also  
look into the previous emails and know the context.  
And then you just add it to your taste.  
And for coding, it's also massive impact.  
Most coders now use all sorts of AI tools to help you,  
where you can potentially edit, solve bugs on the go,  
and there are just so many exciting tools for this.  
I personally use them all the time.  
Other interesting content is about what  
is called assistant models.  
For instance, Sam Altman advertised the custom GPTs  
last year.  
It allows you to take a general model, for instance ChatGPT,  
train it to be specifically targeted to a task.  
For instance, it can be a custom GPT for emails.  
It can be a custom GPT to help you find recipes with a food you  
have in your fridge.  
It can be a custom GPT to help you find the most exciting hikes  
around you.  
So many use cases, and sometimes you  
can build your own custom GPT if you figure out  
that you have a task that happens  
very regularly in your day.  
I personally have created so many of those.  
For instance, I even created one for my students  
where I fed all the content from my course,  
and they can chat with this custom GPT to have,  
for instance, quiz questions, hints for the homeworks,  
or details about how exam and the grades will happen.  
End of transcript. Skip to the start.  
\`\`\`

L1.4 AI and Economic Potential  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, let's talk more  
about the economic potential of generative AI.  
We just covered many exciting use cases  
where technology can help different ways of collaborating,  
which means it will impact the way we work.  
So McKinsey, as I mentioned, thinks that lots of money  
can be added to the economy, in particular,  
for instance, in customer engagement.  
AI brings the ability to scale, answering customers  
on, for instance, any website or social media.  
And having those chatbots could potentially  
save lots of resources from call center agents  
and provide everyone the opportunity  
to get the answer immediately, without having  
to wait for a very long time on the phone.  
Another exciting opportunity is the ability  
to absorb lots of content and make it much more concise,  
such that, instead of having to go through so many web pages, so  
many reports, you get immediately  
the proper information you need, which  
would bring potentially expert knowledge to anyone's hands.  
If you want to do research in a very technical topic,  
let's say, for instance, natural language processing,  
and you have a specific question about it,  
you can leverage the AI technology  
to do the search for you and bring what matters  
for your specific questions.  
Of course, this has ethical questions  
because there is lots of interest  
in doing the search manually, in the old-fashioned way.  
But then, sometimes, you just want  
to be efficient and get the answer you need on the go.  
That's huge value there.  
Another important aspect is creative content.  
You can leverage AI for, for instance, marketing messages,  
press releases, research and development,  
creating images online.  
I, personally, use those AI tools all the time,  
and the images you can see in these presentations  
are mostly all generated with AI, by using multiple tools.  
I used Midjourney, Dall-E, Recraft, other models.  
So I tried to make those lectures  
more entertaining and visually appealing  
by leveraging those AI technologies.  
And, finally, massive impact around coding.  
It's very evident that AI can help  
you code all sorts of different languages,  
even though you don't know how to code in this language.  
And it's already been shown that the productivity  
of professional coders has been massively  
improved thanks to those tools.  
I personally code so much faster by using this.  
You also have risks, though, because the technologies  
have shortcomings.  
For instance, there is what we call confabulation.  
Confabulation is the fact that AI  
can produce inaccurate or biased content  
and it can misinform the people who will use it.  
So methods to change that can include fine  
tuning AI with specific context learning,  
maintaining the human oversight.  
Some people also call this hallucinations,  
meaning the model will totally invent facts.  
And then, I've seen so many of those cases.  
When I know the answer, it's OK.  
I can potentially correct.  
However, sometimes you don't know what's right or wrong.  
In that case, that can be very detrimental to you.  
Here is an example.  
I asked Claude, which is one of the top-performing models,  
a few months ago, who is Leonardo Lucio, so who am I?  
I already know who I am.  
However, what happened is the model started  
to invent things that are completely wrong about me.  
It said that I'm a French businessman-- so we could argue,  
potentially, yes; an entrepreneur, we could argue--  
but also the founder and CEO of Doctolib.  
It's a big startup based in France.  
I am sorry, not this.  
The model completely invented that fact.  
And this can happen all the time,  
when you ask AI to give you some specific facts.  
Sometimes, it won't give you any sources.  
And even if it gives you sources,  
it doesn't mean that the content will actually be correct.  
And some people have talked a lot about the fact  
that one lawyer used ChatGPT in court,  
to figure out some cases for help,  
but the lawyer forgot to check the sources.  
And ChatGPT had made up cases from scratch  
that actually don't exist.  
So, of course, there will be potential sanctions from this.  
But the lesson is, if you use AI for important topics,  
always be careful about the quality of the information.  
So now, let's talk more about consumer reactants.  
It's the fact that the technology may impact  
the way people perceive your company,  
and it can potentially trigger negative reactions, especially  
if you have human really involved in the process.  
So it's sometimes very important to be transparent  
that you used AI.  
For instance, recently, I was looking for an apartment  
in Seattle, where I live most of the time,  
and it turns out that the answers I was getting  
were from an AI.  
And then, the AI looked very human in the way it was writing,  
and so I answered in a very human way myself,  
with a lot of empathy.  
And I realized later it was just an AI.  
So I felt very angry with this situation.  
Why would I spend so much time writing a kind email  
to just an AI, while I could just directly answer directly  
the information?  
So this is an example where your customers may be unhappy,  
depending on how they interact with the technology.  
For instance, Air Canada had a chatbot  
to help answer customer queries.  
It was before the age of ChatGPT,  
so it was another type of AI.  
And it turns out that the bot hallucinated some fake policies  
to a customer.  
So you just provide wrong information  
to a customer, which may lead to detrimental consequences.  
Now, let's talk about copyright.  
The problem with AI-generated content  
is that it's been generated by a model where you don't really  
understand how this model was trained.  
And this model is using information  
from all over the internet, private databases, databases  
where you have no idea where they're from.  
And it's possible the model will just spit out  
some words that are not yours and someone else's, or people  
who did not allow the companies to train on their data.  
For instance, The Times, like The New York Times,  
has sued OpenAI and Microsoft over AI use of copyrighted work.  
So this is still going on today.  
Some people also generate artworks, using, for instance,  
Midjourney, like I do.  
And then, when you do use those images for commercial purposes  
or awards, what's the policy with this?  
Is it OK, knowing that those images are potentially  
influenced with actual artworks from artists  
who disagreed with the use of their art in training?  
And, for instance, in the movie industry,  
it's also causing lots of trouble,  
and potentially lots of lawsuits may happen as well.  
Cybersecurity is also, of course, of concern  
because the fact that you have an AI that  
may have some independent agency and operate and use tools  
may open for new types of cyber attacks.  
Or maybe you ask AI to generate some code,  
but this code has a major fault in it,  
and you did not catch that.  
So it may eventually harm your brand,  
potentially lead to attacks on what you created, and there  
are major challenges at stake.  
For instance, The New York Times has investigated  
that those models, like ChatGPT, sometimes can actually  
generate email addresses that actually exist,  
and it's because they were in the training data.  
So there is lots of studies about how those models actually  
capture information.  
Can we have those models forgetting such information?  
And there is, of course, a lot of work of curation,  
from people training the models, to avoid potential leaks  
of important data.  
So here what's important for you,  
is, don't put important information about you  
or someone else in those models because it goes, potentially,  
in the training data, especially, for instance,  
healthcare information, financial information.  
So maintain awareness of everything you put out there.  
If you're curious and want to play with the model  
and see how it can be vulnerable to different attacks, even  
attacks from just writing the prompt differently,  
you can play this game.  
I use it in my classroom.  
It's multiple levels, where you have  
to trick the model into revealing a password.  
So give it a try.  
End of transcript. Skip to the start.  
\`\`\`

L1.5 Ethical and Practical Considerations  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's talk about, also,  
lots of ethical challenges and debates with AI.  
There is now technology that can recognize potentially  
all the faces in the world by leveraging  
every single photograph on the internet.  
So now imagine that this model in the hands  
of different governments, agencies.  
It's huge power in the hands of whoever  
can leverage such technology.  
Is that something we want, don't want?  
Anyway, the technology is out there.  
You can also use the technology to get lots of information  
for trading, potentially leveraging satellite imagery  
to understand how many boats entered  
that port, how many cars went to Costco or Walmart,  
so you have even an idea of how a stock will perform.  
So hedge funds use such models.  
Is it something that you find a good use of AI or not?  
It's a debate, but the technology is really out there  
and transformed lots of businesses.  
Having AI also allows building new kinds of weapons and drones  
that can potentially kill at the other side  
of the world with no one out there on the field.  
It changes the whole way of doing war,  
and also asks a lot of questions about ethics around this.  
And finally, the models in AI, like many algorithms,  
are very sensitive to biases, racism, sexism,  
and many other things that you do not want with your values.  
For instance, here I generated a few days ago a picture  
using Recraft using the prompt, a room full of CEOs.  
And what you can see is it's only white males  
in the room, no one else.  
I did not ask for anything specific but CEOs,  
but the model immediately put white males.  
It shows that there is biases into the training data  
because this is what the model has learned,  
but it also reproduces those biases.  
There are so many of them to investigate.  
If you're curious, look online.  
Lots of people compiled those and also work  
hard to mitigate this issue.  
And how do you get those fantastic models?  
You actually need human labeling,  
and the people labeling these are typically low-wage workers,  
unfortunately, in low and middle income countries.  
So this is what it takes sometimes  
to get high-quality performance.  
And they had to label very toxic content.  
Is that something that's ethical?  
That's a question again.  
And now, be ready for lots of AI-generated content  
all over the internet.  
All the text you read might have been written by an AI.  
AI avatars are becoming extremely used, even,  
for instance, in politics right now.  
So Ukraine unveiled the first AI-generated military  
spokesperson they use an avatar to display messages  
from the government at scale without having  
to make an actual recording.  
This can be very valuable in wartime.  
Potentially, you have the opportunity  
of displaying messages immediately  
without having the possibility to record this in a clean manner  
because avatars are always looking good  
and can work all the time, never tired  
and always speaking with perfect language.  
So lots of opportunities for this.  
But maybe it will trigger reactions from people.  
And then you live in a world where you never  
know if this was actually said or if it was completely  
invented by an AI.  
People working in the field really  
push for artificial general intelligence,  
and they want to accelerate development at any cost.  
And maybe this is not something you  
want to spend that much money, that much amount of resources  
just to build a better AI model.  
So there is some prior that I can solve all your issues.  
Is it potentially true in the future?  
Or maybe this is just a diversion  
to more important topics.  
So big questions out there.  
So you will listen now to a video by Sam Altman  
where he says that he really wants this technology, whatever  
it costs.  
And so, of course, you may agree or disagree with such situation.  
The technology also leads to collaborations,  
as I mentioned previously.  
And sometimes some people will win prizes for a creation  
that they co-created with an AI.  
Do you agree with the rules?  
It means also that everything has  
to change, potentially, in allowing or not allowing that.  
And for instance, the winner of a prestigious Japanese literary  
award actually used ChatGPT a lot  
and other technologies to generate this.  
And potentially, it's just a smart use of the technology,  
and it still reflects her art and her creation.  
But some people complain that it's not fair.  
It used to be only written by humans.  
And think about all privacy and intellectual property  
implications.  
Data privacy concerns I mentioned  
because the data you use for training  
may include some sensitive information.  
And you may have some information leakage  
in the model outputs.  
The intellectual property issues as well,  
the fact that you can have some copyright  
infringement with the data used, some patents that you leverage,  
but in fact, the content that you discovered  
has been generated by an AI.  
And right now, you cannot copyright anything that has been  
generated with AI.  
Who owns what was AI generated?  
When I create an image, am the owner?  
Is it, for instance, OpenAI, who created  
the model that's the owner?  
Or is it the people who created the data that  
trained the model that's the owner?  
Or maybe multiple people should be the owner.  
It's an open question.  
Lots of biases and fairness, as I mentioned,  
in the training data.  
To regulate all of this is extremely challenging  
because you don't want to stifle innovation,  
but you do want also to regulate enough that it  
won't be a complete mess.  
And so you have many different approaches with this.  
The other big challenges around AI  
is the fact that to train those models and use them,  
it uses a lot of resources, water and electricity,  
for instance.  
To train ChatGPT, this costed a huge amount of energy  
that was potentially equivalent to 120 different US household  
yearly consumption.  
And it really contributes a huge amount  
to the ongoing demand for energy.  
There is lots of research to make those models more energy  
efficient.  
More opportunities to potentially make less--  
more possibilities to make them less expensive with better  
training methods, better mathematical techniques  
for optimizing better model architectures, better hardware.  
But still, it's a huge amount of energy.  
Lots of news about that.  
For instance, there has been disclosed  
that Microsoft and Google had their energy consumption  
in water and electricity increased by 20% to 30%  
in the past few years.  
And this was even before generative AI  
having such a peak.  
So what about now?  
So really think about this.  
It's an overall opportunity for research as well.  
And of course, regulating AI is challenging.  
In Europe, they have already implemented some landmark rules,  
and in the US, for now, it's just in trial.  
And for instance, California wanted  
to implement some specific legislation, but in the end  
it was not adopted.  
So sometimes the Congress is calling  
for some testimonies from the leaders in big tech  
to discover more about that.  
But it goes very slow, much slower  
than the rate of inventions.  
So keep an eye on regulations companies  
do, such that they are ready to tackle,  
for instance, a new way of training models,  
a new way of leveraging data.  
But overall, very active and important topic.  
And I invite you to take some time to pause the lecture  
and also think more about everything  
I just mentioned for yourself and ask yourself the following  
questions.  
How can you ensure that AI is developed and used  
ethically and responsibly?  
What role do you think that government, businesses,  
and individuals should play to regulate and oversee  
AI development?  
How can you address concerns about AI impact  
on jobs, privacy, fairness?  
What steps can we take to mitigate  
the potential risks and unintended consequences of AI?  
Here I just generate one picture to illustrate this slide,  
and you can see that overall it looks pretty good.  
But you can have some typos, for instance,  
if you ask AI models to generate some text.  
That's just an example of a little mistake that AI can do.  
And potentially, it can be harmful in some situations.  
And this is very subtle.  
If you look at the image without looking too much in the details,  
you would not notice that there are, for instance,  
two P's into the ChatGPT on top of this image.  
End of transcript. Skip to the start.  
\`\`\`

L1.6 Deploying AI Models  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's talk also about the fact  
that you have multiple ways for the industry to deploy and share  
their models.  
You have the market of closed-source models  
and open-source models.  
Closed-source models do not disclose much in general  
about how the model was trained, which data was involved,  
and what architecture it is.  
Those models are typically the ones  
from some companies that receive lots of money.  
And you also have the open-source community,  
where everybody can contribute.  
And there is more transparency around this.  
However, as you can see, they don't receive as much funding.  
And it really relies also on the strength  
of the community to build them.  
And they have pros and cons, those models.  
For instance, closed-source models  
typically have slightly better performance as of today.  
They are easier to run out of the box because those companies,  
they want to make money from their models,  
so they work hard on making them very easily accessible,  
even if you don't have necessarily technical skills.  
Open-source models typically have the ability  
to be more customized because you know everything about how  
it was trained, and you have also access to the code  
very often.  
It's also sometimes cheaper to train and deploy  
because you can customize this to your own setting.  
And it's the community that maintains  
the control on the development.  
And if you look at the calendar of releases of models from 2023,  
you can see that so many models were developed.  
Some are top notch and are open source.  
Many are also closed source.  
So you have a variety of opportunities.  
So sometimes you may resort to using a closed-source model  
if you want something that will be always super reliable.  
Or sometimes, because you want to do research and control as  
much as you can, or you look for something cheaper,  
you may go with an open-source model.  
I personally use both types depending on the use case.  
And I want to remind you that AI is not sentient,  
meaning that AI does not have a soul  
or does not experience the world the way we do.  
This is just an algorithm that is able to generate some text.  
And this text may sound extremely human.  
It may sound even like a conversation  
with lots of empathy, a model that can really understand you.  
You can see lots of movies these days  
about sci-fi future where people having relationships with AI.  
Those AI can really have those conversations of this type as  
of now, but they don't have the ability  
to interact with the world the way we do.  
They don't think and love or hate or experience emotions  
and feelings how we do.  
So really remember that those AI models are just  
extremely good at repeating content and writing texts  
that sound like it's human, but it's actually not human.  
And because there was lots of debate  
about this, if you ask an AI model, Are you sentient?  
now there is a precrafted answer from OpenAI, Anthropic,  
or Gemini or whatever top model where  
they make sure that the models say, no, I am not sentient,  
I am just an algorithm.  
And I want to show you a few shortcomings of large language  
models.  
They have the behavior of not reasoning and making  
very terrible mistakes for things that look so obvious.  
If you ask, for instance, ChatGPT to count the number  
of Rs in the word strawberry-- so they are three--  
the model will just tell you there are two Rs.  
And I tell the model, you should count better.  
And that model tell me, oh, you're right,  
there is actually one R, so it's even worse.  
This model is so smart.  
This model, people use it for so many different things,  
and yet it can make such a silly mistake.  
It's because the model does not really think the way we do.  
It's just using probabilities to be  
able to answer to your question.  
And now I ask the model, how many Rs in marionberry?  
And so here, it tells me again there are two Rs,  
while there are actually three.  
And then I tell them, well, no, there is only one again,  
which is, of course, a lie.  
The model tells me, oh, you're absolutely right.  
There is only one R in marionberry.  
Thanks for keeping me on my toes.  
This behavior is called sycophancy,  
the fact that the model will want to agree with you.  
And that's an issue because if you tell the model  
something wrong, or you ask the question in a way that  
would suggest the AI should agree with you,  
you may get really harmful answers  
or wrong answers, potentially.  
And here, I used an even smarter model, according to OpenAI,  
and ask this time, how many Rs in the word strawberry?  
So this time, the model actually thought.  
It's not really thinking.  
It's more like processing for a longer time.  
And then it started to try to figure out a way to count.  
So it spelled the word letter by letter.  
But it turns out that while spelling strawberry,  
it forgot one R. So of course, it gave me a wrong answer,  
there are only two.  
But however, if I ask this time the model  
that, no, there is only one, the model counted again,  
and this time told me, no, I think I counted,  
and there are actually three.  
So there is improvements happening and, of course,  
lots of research to avoid this challenge.  
Remember that those models are also a black box.  
They lack explainability.  
It's hard to interpret their decisions.  
So it means that your good human judgment,  
your critical thinking, are even more important.  
And we just saw some use cases about that.  
And I really believe it's important to maintain  
AI literacy, meaning that you are aware of how  
to use the technology.  
You remain current about the latest correct,  
ethical, effective usage of generative AI and large language  
models.  
And really, I want to insist--  
your critical thinking is so important.  
I don't think AI will replace you.  
I rather think it can augment you,  
but you have to be smart in the way you're going to use it.  
And having a proper human-AI collaboration  
will give you so many impactful creative pathways.  
And we'll have other lectures to look more into this.  
So if we conclude, we can see that mastering  
the art of this jagged frontier is important.  
For you, you have to figure out where  
AI can help you or harm you.  
And how do you figure this out?  
By playing with the AI, by trying multiple times.  
Change the prompt.  
Try different models.  
And whenever you see there is a new release,  
just look for the same previous questions that were too hard  
and try them again with this new model  
to see if it can solve them.  
The goal is to adopt those effective collaboration models.  
Figure out if you can delegate this  
or if you want to co-create.  
There are so many ways to leverage  
the technology for the better.  
I also want you to feel responsible to navigate  
those ethical challenges proactively.  
Look at all the implications if you use a given technology,  
implications of other users on how those models were trained,  
on the resource needed to maintain such models.  
And it's important for all of us to feel responsible for this  
because the technology is here to stay.  
So stay informed.  
Think critically.  
Keep up with all those opportunities and the key risks.  
And I really believe that those AI models,  
although they're extremely good at recognizing patterns,  
figuring out how to best answer this question in their own way,  
your human judgment will be important to shape  
this whole collaboration.  
And we remain the masters of the whole process.  
Thank you for listening to all of this.  
And we'll have lots of other exciting lectures  
to understand better how you do creative problem solving  
with the technology.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
In this lecture, we explored how artificial intelligence is reshaping the nature of work by taking on increasingly complex cognitive tasks. We examined where AI performs well and where human judgment remains essential.

Key Takeaways:  
The distinction between routine, non-routine, and judgment-based work  
How prediction, knowledge, and judgment differ—and why judgment is hard to automate  
The importance of human values, context, and discretion in complex decision-making  
Early real-world examples of AI augmenting but not replacing professionals  
Congratulations on finishing this lecture\! You’ve built a conceptual foundation for thinking critically about where AI fits—and doesn’t—in the evolving landscape of work.  
\`\`\`

Lecture 2: Gen AI and Creative Problem Solving  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: Gen AI and Creative Problem Solving, taught by Professor Léonard Boussioux, Assistant Professor of Information Systems at the University of Washington.

This lecture explores how generative AI tools—like large language models and image generators—can augment and expand human creativity. It delves into specific use cases in brainstorming, visual ideation, and storytelling, analyzing how humans and machines co-create. The lecture encourages learners to think critically about the differences between “associative” creativity (where Gen AI excels) and “evaluative” creativity (where human judgment is key). Learners will also examine examples where Gen AI is used in professional creative domains such as marketing, entertainment, and architecture.

Learning Objectives  
By the end of this lecture, learners will be able to:

Describe how GenAI models contribute to creative tasks such as brainstorming and ideation.  
Distinguish between generative, associative, and evaluative forms of creativity.  
Analyze the role of human oversight in selecting, refining, and integrating AI-generated content.  
Assess the strengths and limitations of GenAI in creative workflows.  
\`\`\`

L2.1 Augmenting Innovation with Generative AI  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, everyone.  
Today, we are going to cover one of my favorite topics--  
generative AI and creative problem-solving.  
I love creativity.  
I consider myself an artist.  
And I really believe that AI combined with your skills,  
your artistry can make such a beautiful impact.  
And problem-solving is so important for the world.  
So many big challenges to solve.  
So combine the two.  
We have a superpower.  
And I want to show you beautiful examples on how to do it today.  
The question that will keep us busy  
is, how can we augment the early stages of the innovation  
process using generative AI?  
Here are two images I generated myself,  
for instance, with Midjourney.  
And I wanted to illustrate a nice analogy  
with having, for instance, the orchid inside the light bulb  
or potentially growing out of the light bulb.  
Two different ideas.  
You will see that all the images in this lecture  
were generated by AI mostly.  
And I generated them using Midjourney, Recraft or Dall-E,  
a variety of models.  
I find this to be a beautiful way to illustrate your content.  
So here are the intended learning outcomes for today.  
We are going to investigate how to design and implement  
some effective human-AI collaborative workflows such  
that you can do creative problem-solving.  
We'll evaluate different prompting strategies  
and techniques such that you can generate creative solutions  
to business problems.  
And we will also analyze and compare the approaches  
from a whole human crowd to a problem and also  
a human-AI approach, where it's just you prompting an AI,  
to see how you can generate novel and valuable solutions  
to challenging topics.  
So the question, as I mentioned is, can we  
augment those early stages of the innovation process  
with generative AI?  
Let's say you start with a challenge, a problem to solve.  
You may want to have lots of possible solutions.  
And potentially, how do you get those solutions?  
You ask a whole crowd of people--  
for instance, all your friends; your parents; me, my students;  
your employees; your colleagues.  
And everybody will try to solve this and give you  
ideas for that.  
But also, some of those solutions could be AI generated.  
For instance, you, if I ask you, find  
an idea for a circular economy challenge,  
meaning find an idea to have a sustainable business idea--  
so let's say, for instance, the challenge to solve  
is, give me ideas around a sustainable business.  
You could potentially ask the AI to give you lots of ideas,  
and then you may select your favorite ones.  
But what you realize is it becomes easier and easier  
to get lots of ideas.  
And then maybe from out of all the solutions you got,  
it became overwhelming for you to figure out, OK,  
what should I do next?  
This is why one of the very important topics,  
as well, is to be able to evaluate and screen  
those solutions to select which ones should be pushed more,  
receive more funding, more money.  
And the goal is to potentially use AI to help us doing this.  
That's the topic of the next two lectures.  
The first lecture, that the one we have today,  
is about how you can generate those solutions  
effectively such that you can complement your expertise  
with AI.  
And then in the next lecture, we'll  
look into how you can evaluate those early-stage innovations  
using AI as well.  
The research I'm going to present today  
is actually my research I've done in the past couple years.  
And I'm super excited that I can transform this  
into a lecture with lots of exciting, actionable insights.  
So I want to thank my team with whom I worked on that--  
Jackie Lane, Miaomiao Zhang, Karim Lakhani,  
and Vladimir Jacimovic.  
It's a collaboration with Harvard Business School.  
And our paper has now been published.  
So you can read this in the following link.  
So here is the summary of the findings in our paper.  
We actually targeted this.  
We want to create good business ideas  
in circular economy in the format of a problem  
and a solution-- your problem you want to solve  
and the solution that could solve it.  
And we asked a whole human crowd to actually  
give us answers for this.  
So we had an open call to human solvers.  
And they could participate to the challenge  
and potentially earn prizes.  
We then took this exact same challenge,  
created a prompt for ChatGPT, and asked the model  
to also give us answers.  
It turns out that after the whole study,  
we figured out that the whole crowd had, in fact,  
the same creativity than me prompting ChatGPT,  
meaning I was able to match so many different people with just  
me and an AI.  
That's very impactful.  
It shows that you can bring to yourself lots of capabilities.  
However, if you look into the details,  
the ideas that I was able to generate with ChatGPT  
were actually more valuable in average  
compared to the ideas of the whole crowd.  
However, the ideas from the whole crowd  
were, in fact, on average, more novel than mine.  
And very importantly, the extreme, highly novel solutions  
were actually from the crowd, not from me and the AI.  
There is so much value you can untap from an AI.  
But the crowd also brings so many different perspectives such  
that they can have such cool, innovative ideas that if you're  
just alone, you may not have.  
So we are going to look more into those details  
in this lecture.  
End of transcript. Skip to the start.  
\`\`\`

L2.2 AI and Creative Problem Solving  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: What's exciting as well  
is that if you are just one human with an AI,  
it can save lots of time.  
Instead of having so many people having to contribute,  
it's just you.  
And it's also quite cheap to interact with the AI.  
So I used the GPT API to be able to do all of this.  
And I was able to get as many solutions  
as I wanted extremely easily.  
However, when you call for a whole crowd,  
you need lots of humans.  
You need to reward them to incentivize them to participate.  
And they all spend lots of time answering the challenge.  
So there is also lots of value in terms of time and money  
to get from a human-AI collaboration.  
So to be more specific, what we call creativity--  
so the quality of an idea--  
is, in fact, the combination of how novel and valuable this idea  
is.  
So it comes from the field of innovation.  
So novelty is defined as the degree to which your idea is  
original and departs from a given set of existing knowledge.  
And value is defined as the degree to which your idea is  
useful and will deliver economic and social returns.  
So we want to evaluate our ideas with respect to those two  
components-- novelty and value.  
So let's start with the motivation,  
with a statistical view of innovation.  
If you look at a whole set of ideas from multiple people,  
in general, those ideas will have this log Gaussian curve,  
where you have a long tail, where the best  
ideas are statistically rare.  
Your goal is to have the highest quality possible.  
We're interested in those very rare ideas.  
But as you can see, they are not that many.  
So there is the technique called crowdsourcing.  
By asking the whole crowd to generate ideas versus just,  
for instance, the employees in a given company or just  
yourself, you are going to increase  
the number of parallel paths, meaning the number of ways  
you could tackle the challenge.  
And this has been shown, with literature,  
that it increases the variance in idea quality,  
meaning it's possible that on average, ideas  
will be a bit worse.  
But you get more of the exceptional, really good ones.  
And this is what matters.  
So crowdsourcing has lots of advantages.  
It brings you access to a diverse set of knowledge  
and perspectives.  
You have higher likelihood of capturing  
those extreme outcomes, the good ones that you really want.  
And in fact, it can be a cost effective and efficient manner  
to get good solutions versus relying only on what  
you have in your own company.  
A famous example is the Netflix competition,  
where there was a $1 million prize  
to enhance the quality of the algorithm  
to recommend movies to users.  
It turns out that this competition was a success.  
And the winning team had invented  
a new algorithm that was actually  
super useful for Netflix.  
That's a good example of real-world crowdsourcing.  
There exists also platforms, like Kaggle  
for data science, where different companies,  
organizations, research groups can create a competition  
with potentially prize money.  
They provide data and a prompt and a challenge.  
And many people can participate, which  
brings so many perspectives for challenging problems.  
So crowdsourcing is actually used in the real world  
and very useful.  
However, it also comes with challenges.  
It's complex to organize potentially.  
You need to figure out how to properly formulate the problem,  
how to decompose everything such that anyone can understand  
this and participate without the domain knowledge of a given  
company.  
You need to incentivize people to participate.  
Otherwise, people won't take the time necessarily  
to do your challenge.  
And then you end up also with lots of low-quality ideas.  
And it's a lot of work to filter out the bad ones.  
So that's something we'll investigate in the next lecture.  
And clearly, here, we're talking about generative AI.  
And large language models have a huge potential  
for idea generation.  
It's actually very scalable.  
You can produce many ideas fast, efficiently,  
and with a very low cost.  
Maybe with different prompting techniques,  
you can emulate a whole crowd.  
This is what we wonder.  
Can I have as much creativity as a whole crowd  
just me prompting an AI, as long as I'm  
potentially creative in the way I'm going to prompt the AI,  
meaning talk to this AI?  
It turns out that AI can be good at recombining ideas.  
So that could be an interesting perspective.  
And we'll look into this.  
So really, the idea is that we can augment the human process  
by having this AI as a collaboration.  
And this can really enhance productivity and creativity.  
But also, as we mentioned in the previous lecture,  
there are drawbacks with using large language models.  
And for creative problem-solving,  
it's possible that the model will hallucinate answers,  
confabulate potential ideas that are not relevant at all  
or not even feasible.  
Also, remember that those models are trained with a specific data  
set.  
Having something novel means that you  
have something outside of an existing set of knowledge.  
It's possible that the model may be trapped,  
stuck in the ideas it already knows,  
and does not know how to get completely new idea.  
And also, those models, they don't  
have as much contextual understanding  
as you do as a human.  
It's possible it does not have enough information to properly  
generate valuable solutions.  
So those challenges might prevent us  
from building successful generation.  
But we'll see how we can circumvent that.  
End of transcript. Skip to the start.  
\`\`\`

L2.3 Evaluating Creativity and Novelty  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now let's look into this,  
can human large-language model collaboration  
match the creativity of a human crowdsourcing?  
So this is the setting that I just mentioned.  
We actually launched a challenge from January to May 2023\.  
We received 125 eligible human solutions  
that we filtered out, such that they  
were all of a higher quality.  
We took this exact same challenge that  
was online and asked ChatGPT to generate lots of solutions,  
using multiple types of prompt engineering,  
meaning multiple ways of talking to the model, using techniques I  
will describe very soon.  
And then we needed to evaluate the quality of those ideas.  
So we actually asked humans, using a platform called  
Prolific, to evaluate the novelty and the value  
of those solutions.  
And thanks to this, every problem solution pair that  
was either given by a human or by a human AI, meaning  
me prompting ChatGPT, was evaluated  
16 times on average, which is enough for statistical studies.  
So let's now look into the prompting techniques  
that I used to guide my search for valuable and novel ideas.  
One simple technique, that we call independent search,  
consists of opening multiple chats  
and always asking the same question.  
Maybe you remarked that when you copy/paste something to ChatGPT  
and try it multiple times, you may end up  
with different answers.  
This is because this model is probabilistic.  
It's going to generate things with a bit of randomness, such  
that it makes them all a bit more creative.  
So we just copy/pasted multiple times the problem,  
and we collected the different answers from ChatGPT.  
And we leveraged the creativity of the model  
of having a bit of randomness in each chat  
to get different ideas.  
Second technique, that we call differentiated search,  
consists in having only one instance of ChatGPT, which  
means I'm going to open one chat and ask the model one  
time after the other to generate one new idea.  
So give me a first idea.  
Great.  
Now I want you to give me a new idea that  
is even better than the previous one.  
OK, I got the second idea.  
Now give me again an even better idea.  
So this is an iterative process.  
And the idea is it's the analogy of having one human that  
is asked to brainstorm, and you push the human more and more  
to think creatively out of the box, ideas that are not evident.  
So the overall analogy is, do you ask 100 people for one idea  
or one person for 100 ideas?  
And we replicated this with ChatGPT.  
So if we look at it in another way,  
with this independent search, you have this initial prompt.  
You ask the same large-language model,  
and you collect as many solutions  
as you want, with as many chats as you want.  
And the other way, the differentiated search, you  
have the large-language model with one instance.  
You get solution one.  
You ask for a better idea.  
You get solution two.  
You ask again for a better idea, and you keep going.  
It turns out that this method may bring more creativity  
from the model because you push the model to think  
harder and differently than the obvious answers.  
Every time we ask for a new idea,  
we also leverage different prompt engineering techniques.  
So prompt engineering means that you  
craft input prompts to achieve a desired output,  
such that you get better answers because you wrote your question  
or your task in a better way.  
It's a very important skill.  
A few techniques-- persona-based prompting, or role playing.  
You can give a personality to your model such that the model  
will emulate this personality.  
You sort of wake up the AI brain to look into everything  
it knows about a given celebrity.  
Very important as well to include context for your model.  
The more context it has, the more  
it can give you an answer that corresponds  
to what you actually want.  
A technique that's super impactful  
is called few-shot prompting.  
If you ask your model to do something,  
but the model has no idea about the exact format you expect,  
it may not generate something you actually want.  
So the secret is give a few examples  
of what you expect to be a good answer or a bad answer,  
such that you can calibrate the quality of your model,  
and the model will be able to imitate something  
that you consider good.  
Chain of thought is one of the most popular methods.  
It consists in asking the model to think step by step.  
Because when you think step by step, instead of giving you  
this intuitive first answer, the model will actually  
take the time of generating a whole simulated reasoning  
process by asking, OK, first, I'm  
analyzing the different problems I have in mind.  
Second, I'm going to rewrite this problem in the best way  
possible.  
Third, I'm going to figure out a few solutions that  
could be possible.  
And fourth, I'm going to select the best solution,  
I think, for this problem.  
So by having such process, the model  
will have a better ability to tackle your task.  
And there are many ways of doing this.  
You can either just say, think step by step.  
It's enough, which is very impressive.  
Or you may actually yourself describe  
what you expect the model to do step by step.  
Finally, it can be so simple as telling the model,  
I want an exceptional, fantastic, amazing, wonderful  
idea.  
By adding those words, you prime the model  
into giving you better answers.  
Why?  
Because during the training process,  
the model has seen lots of examples  
on the internet of what people were qualifying, oh, wow,  
that was so good.  
So the model remembers all those good things.  
So if you remind the model, do something amazing and absolutely  
fantastic, the model will actually do something better  
already.  
So think about including those words.  
It does work.  
So we did implement those different techniques.  
So remember, we have multiple instance and single instance.  
And I'm going to create a multiple levels of ChatGPT.  
For instance, the level 1, I just give the original problem  
descriptions, the exact same one I gave to human solvers.  
But level 2, I'm going to give a personality to ChatGPT,  
and this personality will actually  
be personalities of the real humans who  
participated to the challenge.  
Like this, I give different perspective of ChatGPT.  
It will allow the model to give solutions  
that are more contextualized because the model will think,  
OK, I'm from Asia.  
I experiment food waste.  
I want to generate a solution that  
has a really good level of maturity,  
and I'm a professional businessman.  
With all those details, the model  
may think differently than if you say,  
I'm part of an NGO based in South America  
and I am a secretary.  
Everybody's thinking differently,  
so you want to emulate the different perspectives  
of different humans into the model.  
So you need to prime the model by giving this role playing.  
And finally, we also gave real-world expert personalities  
to the ChatGPT.  
For instance, you are Elon Musk, who  
has expertise in automobiles.  
You are Satya Nadella, the CEO of Microsoft.  
You are the founder of Google, Sergey Brin.  
The model knows about those people  
because it has read so much about them.  
It's read all the Wikipedia pages, for instance.  
So it knows how they think.  
Maybe it knows also their biographies.  
So the idea is leverage what the model knows  
about those famous people such that it will think like them,  
and you may end up with even more creative ideas.  
And this is what actually happened.  
For all those prompts, we made sure to include  
one-shot example, so a little example of what is expected,  
a chain-of-thought process, asking the model  
to think step by step.  
And we also told the model, your idea  
will be evaluated according to novelty, value, feasibility.  
So the model knows what is expected as good criteria.  
And the role playing is what I just mentioned.  
It turns out that research has shown  
that if you do the role playing, you really  
trigger this chain-of-thought mechanism, where  
the model will be more creative and potentially more diverse.  
So let's look at the results.  
Remember, we asked actual humans from the Prolific platform  
to evaluate the quality of all the ideas  
that were either generated by a human or by the human AI,  
meaning me, prompting ChatGPT.  
So here in this plot, you can see every single idea as a dot,  
and we plotted the value with respect to the novelty.  
What you want is to be in the corner on the left,  
in the high part, because it means  
you have a high value and a high novelty.  
So let's take a look at the idea that had the highest  
novelty according to everyone.  
It turns out that this idea was a human idea from the crowd,  
and the idea was to use innovative bricks made  
of foundry dust and waste.  
That would have a LEGO-like structure.  
Like this, you can interlock them and build  
structures extremely fast.  
And on top of this, it's from recyclable materials.  
And like this, you really save lots of resources  
and you build something meaningful for circular economy.  
It turns out that this idea, that was deemed the most novel,  
is actually implemented these days in the industry.  
And so you can see examples of different companies  
working actively on recycling glass or recycling plastic  
or concrete to build structures that  
would leverage such bricks that are very easy to interlock.  
So this is still a novel idea because not everybody  
knows about this idea, but it's actually a good one.  
Companies are building this.  
So now let's look at the most valuable idea.  
It turns out it's a human AI idea,  
an idea I got by asking ChatGPT to perform the problem.  
And the idea is to convert food waste from restaurants  
and households into biogas for electricity,  
and potentially fertilizer through bioenergy centers.  
It turns out that this is also a company that exists.  
And remember, ChatGPT has read so much content on the internet,  
so this is why it's easier for the model  
to generate something valuable because it  
has read which companies are successful and what they did.  
This is why it's a great idea to leverage the power of ChatGPT  
to enhance the quality of your idea  
because the model knows things that you do not.  
But the novelty is something that  
is more from you, the human, because you have this ability  
to figure out something out of the box.  
So humans really inspire novelty,  
and we can see that overall there  
are more novel ideas from the human crowd  
than just me prompting ChatGPT.  
But the value, it's the reverse.  
You have more valuable ideas from the human AI  
than the human crowd.  
So keep in mind that the strengths of a whole crowd  
are not the same strengths as just you prompting ChatGPT.  
However, now that you know this, you  
may be able to prompt better ChatGPT to elicit more novelty.  
Or instead of just asking ChatGPT to directly give you  
the problem and solution, you are  
going to improve the quality yourself as a human.  
So you go through an iterative process.  
This course is about generative AI,  
but remember you've taken lots of lectures about data  
science, potentially also data visualization.  
So my goal is to show you that you can show results  
in so many different ways.  
In the previous slide, I showed you a scatter plot  
so you can visualize every dot.  
Here I'm showing you a distribution,  
so it allows me to derive other types of insights.  
So always think that different types of visualization  
can show different results--  
same data but different results.  
So here my goal, in this plot, is  
to show the distribution of all the different ideas,  
whether they were from the human crowd,  
from the multiple instance, so meaning  
when I open 100 chats, for instance, or only  
one chat, so single instance.  
What we can see is that when it comes to novelty,  
you clearly visualize that only the humans had a bit  
of distribution to the right.  
When it came to value, the AI solutions  
were more to the right.  
But interestingly, having the single instance  
improved the novelty of ideas.  
Remember what it means.  
It means that if I ask ChatGPT in one chat  
to keep generating idea after idea,  
I ended up with a better novelty.  
The intuition is if you push the model to keep thinking and keep  
generating something different, in the end,  
it will exhaust all the common ideas that it has in mind  
and will start to have to think about, OK, what is not obvious?  
What haven't I said already?  
And you push the model to think harder and harder,  
to look into other areas of this AI brain, a bit like you  
as a human.  
If I ask you for 10 ideas, it can be potentially  
a bit challenging.  
But now I ask you for 100 ideas, and suddenly you say, oh my god,  
how am I going to get 100 ideas?  
You're going to think about crazy ideas,  
like things that are not obvious at first sight.  
Same thing with AI.  
So remember, it's great to ask AI to iterate itself  
for better content.  
When it came to value, there was no big difference  
between the two.  
It's because AI, per se, was already  
knowing how to generate something valuable,  
and it's something sort of a default.  
It has really learned very well from the training stage  
how to get value in the answer.  
It's also because companies that are going to release models  
like OpenAI, they spend a good amount  
of time trying to get answers for the users that  
will bring them lots of value.  
I just mentioned that different manners of representing results  
can give different insights.  
Here is another manner.  
We have studied in previous courses and modules  
the concept of a regression, meaning  
you are going to predict a given thing with different features.  
Here it's a super, simple regression.  
But people like to visualize what  
is called a statistical significance, meaning  
how important is a given factor to predict something.  
So here my goal is to predict the creativity of the solutions  
depending on if they are from a human AI,  
meaning me, prompting ChatGPT, or the human crowd.  
And I also wanted to predict the creativity depending  
on if I'm from a multiple instance,  
so meaning multiple chats, or a single chat.  
It turns out that those results are  
showing that there is no difference  
in average creativity, whether it's a human AI or a human crowd  
solution.  
So it means I was really able to match  
the whole creativity of a whole crowd, just me with a model.  
That's very impressive, to be honest.  
And we could also see that having the single instance  
slightly outperformed the creativity of human crowd  
outputs, which means that having the ability to iterate  
with a given model is extremely powerful.  
In this slide, you can see that I  
tried to predict whether a given solution will  
be one of the best in creativity or if they're just part  
of the average or the bad ones.  
So it's a binary classification.  
What we can see is that if the solution comes  
from the human AI, there was actually no difference  
whether it was a top creativity or not compared  
to coming from the human crowd.  
And in fact, there was also no major difference  
whether it came from multiple instances or a single instance  
when it came to top creativity.  
So what does it mean?  
It means the very best solutions, the ones we really  
care about, I as a human prompting ChatGPT  
managed to get as many as the whole human crowd.  
Remember, creativity is the combination  
of value and novelty.  
So overall, I can get super, creative ideas just  
with ChatGPT.  
But remember that the novelty was more of a human thing.  
So now the question I want to engage you with is,  
how do I get AI to give me top, novel ideas?  
That's something that's harder.  
One set of techniques is potentially  
to rely on better AI systems.  
AI capabilities are advancing.  
I did this study in 2023 where the models were already good,  
but now things keep improving constantly.  
So keep an eye on future state-of-the-art,  
large-language models.  
Look into the concept of multimodality  
that we also cover in the course,  
meaning that the models that learn from multiple sources  
may have the ability to think also differently.  
Look into the concept of multiagent systems,  
meaning systems where you have multiple GPTs talking  
to each other.  
So imagine one model gives idea 1\.  
One model gives feedback on idea 1,  
such that model 1 can actually improve on this.  
And you iterate.  
So instead of having me trying to take the best ideas  
or giving feedback, you may have two AIs talking to each other  
to get even better ideas.  
There is also the concept of retrieval-augmented generation.  
It's a system that allows the model  
to know even more than it already  
does by looking for information online  
on the go at inference time.  
So lots of techniques get developed by the community,  
and it means that the models keep  
having better opportunities to bring you novelty as well.  
And second, a whole set of better human-AI interaction.  
In this lecture, I just showed you  
a simple use case where I give a prompt,  
and I collect the answer from ChatGPT.  
And I can, of course iterate.  
But I did not get involved that much as a human.  
I was involved at the first stage of writing a good prompt.  
But that's it.  
I did not try to edit the answer from the AI.  
I could actually take the very valuable idea from AI and think,  
myself as a human, how I can make it more novel.  
Or potentially I can take a very novel idea from a human  
and ask AI to make it more valuable.  
So think about this collaboration aspect.  
Remember that AI is very good at recombining ideas.  
It has seen so much information in the training data  
that it knows how to get potentially novelty out  
of two unrelated ideas.  
So that's already one way of getting innovation.  
However, it's also important to be  
able to go from zero to one, those moonshot ideas,  
those people who can think really out of the box.  
Creativity has something magical,  
this eureka moment that you're able to figure out something  
that nobody else has, this genius instant.  
Can we replicate this with the AI?  
End of transcript. Skip to the start.  
\`\`\`

L2.4 Human AI Collaboration Techniques  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So I want to show you a quick demo of some  
of the latest AI models to illustrate how a human-AI  
collaboration may look like in the future to generate ideas.  
So here, I'm going to ask ChatGPT-4o equipped  
with SearchGPT to figure out if there is any company online that  
did the most novel idea from the human crowd.  
And you can see that it figured out lots of companies.  
And it read all about them.  
So now it can talk about what they do.  
And here, I asked the model to make those solutions much more  
novel and valuable.  
And I tell the model, be very innovative.  
Thanks to this, I get the model to iterate again.  
So it's really a human-AI collaboration.  
I started with a very novel idea.  
I asked the model, figure out who did that.  
And now I tell the model, make it even better.  
And I get potential exciting ones.  
So now I'm telling the model, pick  
the one you find the most creative,  
promising, novel, valuable.  
And I even asked the model to make it even better.  
It's to show you an example of human-AI collaboration.  
And I want the model to expand on it  
and write it in the format of a problem solution.  
So here, you can see it decides to focus  
on environmental pollution and climate change in urban centers.  
And now it gives me an exciting solution  
with biosequestering bricks with CO2 capture and purification.  
Of course, that would be amazing to have such technology.  
So it illustrated how I really get  
to combine prompting with a whole workflow.  
And now I want to know if this is feasible to build,  
because if you have an incredible, fantastic idea,  
but it's impossible to build, that's not that useful.  
So here, the model went online, search every technology that  
might be implementable, and now I have a much better workflow.  
So it's to show you how you can reach high novelty  
with a human-AI collaboration and that the technology keeps  
evolving.  
I now want to illustrate another potential model called  
Perplexity.  
It's also a model that has the ability  
to search online for information.  
And here, I used the exact same prompt as before.  
I asked the model to find if any company has done that bricks  
idea.  
You can see that Perplexity is also  
giving you images, sources of where it figured out  
this information.  
And what's cool is that you can also interact.  
Notice that the model also found out exactly like OpenAI.  
And you can have a whole list of new questions.  
It's exciting because you can explore lots of contents.  
And here, I'm just asking what types of waste materials  
are used in the production of a given brick from one  
of the generated solutions.  
So you can really explore the whole problem space very easily  
with this new type of technology.  
So here, I'm asking the model to propose new ways  
to make this even more novel and creative,  
so exactly what I asked to SearchGPT.  
And it goes online to figure out if anyone has proposed anything.  
So the AI becomes extremely good at recombining information live.  
And it's not stuck with what it just learned from the training.  
It can also enhance the whole generation process  
from online search.  
How does this work?  
I just showed you two examples, where you  
had SearchGPT and Perplexity.  
Those models are able to react to a given prompt  
by looking for information online on the go.  
This is called retrieval-augmented generation.  
Because you retrieve information,  
you augment your generation.  
Here is a workflow.  
I'm the user.  
I'm asking a question to the model.  
You have a mechanism that will create a retrieval query that  
will look for what's important to answer in a given database.  
The database will return the retrieved data.  
Typically, it's texts.  
It goes back to the initial model.  
It is going to create a whole prompt that you do not  
necessarily see yourself.  
This is going to go through the large language model  
and can give you the final answer.  
So it's not only based on the training information  
that the model received, but also  
on these newly retrieved pieces of knowledge.  
That's a cool technology.  
That was just one example of how to enhance  
the human-AI collaboration.  
There is so much we can do.  
So to conclude, the human-guided AI using prompt engineering  
can really produce creative outputs  
that are comparable to human solvers alone.  
In our study that I just showed, the human AI outputs  
were more valuable, which reflects that large language  
models have a huge training, fine-tuning alignment process.  
The human crowd outputs were more innovative,  
in particular top novelty.  
But remember that AI capabilities are advancing.  
Overall, what we want is not the one or the other,  
but rather to combine the two, having an AI in the loop,  
meaning the human is really driving the process,  
and you ask AI to help you, or a human in the loop.  
Maybe I will spend most of the time working,  
and you are just going to drive where it should go next, like,  
for instance, in the previous search  
process with retrieval-augmented generation.  
So you really have amazing opportunities  
to augment any pipelines for evaluation of ideas  
to generate better ideas.  
So think about it, and keep collaborating.  
So really, the future of creative problem solving  
is to leverage those human-AI guided outputs  
for a more cost-effective and scalable approach  
such that you have more parallel paths,  
and you can free up human resources for other processes  
that really matter.  
The goal is to go to this human-AI synergistic future,  
to have a strong synergy between the two.  
And the goal with any AI-in-the-loop  
or human-in-the-loop is to augment,  
in a responsible manner, our processes,  
not replacing our creative thoughts.  
I really believe that AI remains a tool  
and is nowhere to replace, again,  
critical thinking, your curiosity, your growth  
mindset, your mission-driven purpose, your creativity,  
and your humanity.  
Those are things for us humans, but we have better tools  
than ever to make it happen.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
This lecture focused on how generative AI can enhance human creativity by helping us generate ideas, visuals, and narratives. Learners saw examples across design, entertainment, and writing, and discussed where humans remain central in shaping and curating outputs.

Key Takeaways:  
Gen AI excels at associative creativity, such as brainstorming and idea remixing  
Humans are still essential for evaluative creativity—choosing what’s valuable, ethical, or appropriate  
Real-world use cases show how professionals co-create with AI in visual design, storytelling, and architecture  
Effective use of GenAI requires a blend of exploration and judgment  
Congratulations on completing this lecture\! You now understand how GenAI can support and expand creative thinking—when guided by human insight.  
\`\`\`

Lecture 3: Gen AI and Human-AI Balance in Decision Making  
\`\`\`  
Overview  
Welcome to Lecture 3: Gen AI and Human-AI Balance in Decision Making, taught by Professor Léonard Boussioux, Assistant Professor of Information Systems at the University of Washington.

This lecture focuses on how AI systems can support, complement, or potentially replace human decision-making. It emphasizes the importance of striking the right balance between human control and algorithmic automation—especially in domains where decisions have ethical, emotional, or contextual implications. Students will learn frameworks for categorizing decision types and explore when AI enhances accuracy versus when it risks eroding trust, accountability, or nuance. The session includes examples from hiring, medicine, legal systems, and operations management.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain how generative AI is applied in decision-making across domains such as healthcare, creative industries, manufacturing, and early-stage innovation.  
Describe the cognitive, financial, and bias-related challenges of human-only evaluation and how AI can alleviate these burdens.  
Distinguish between objective and subjective evaluation criteria, and analyze how AI influences human decision-making differently across them.  
Compare the effects of black-box versus narrative AI recommendations on judgment, persuasion, and critical thinking.  
Discuss strategies for balancing automation and augmentation in human-AI collaboration, ensuring human oversight in subjective decision-making.  
Recognize how human-AI interaction can enhance creativity, expertise, and the art of curation in decision-making.  
\`\`\`

L3.1 AI Innovation in Decision Making  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, everyone.  
Today, we are going to cover how you can leverage  
the collaborative aspect with generative  
AI for decision-making.  
I really want to emphasize that developing a human-AI expertise  
is extremely important.  
We already discussed in previous lectures  
that it can help for the future of work,  
helping you creating also better ideas.  
But today, it's about making decisions.  
Human-AI collaboration is already happening.  
For instance, in a medical diagnosis,  
doctors can leverage technology, for instance,  
in radiology, helping you to assess if a patient has  
a given condition or not.  
Creative industries-- myself, I use AI lots.  
All those images that you see, I generated them using the model  
called Recraft.  
You can leverage AI, for instance,  
to create music as well.  
Manufacturing-- there are more and more  
robots where they have the ability  
to process visual inputs.  
So it's computer vision.  
And humans can collaborate with such robots.  
It's a very active area of research  
and also for the industry.  
And of course, in scientific research,  
it's becoming more and more prevalent to try  
to do discovery of new materials, new drugs,  
leveraging the technology.  
But to be able to properly collaborate with such technology  
and make decisions, lots is involved.  
And let's talk more about the innovation aspect.  
How do you get to do decision-making and collaborate  
with AI when it comes to creating new startups,  
new products?  
It became so easy to generate content.  
For instance, you can write a business plan with ChatGPT.  
And you can find so many tutorials online or people  
discussing this.  
It became so easy that it's also possible  
that you face challenges and that the content you get  
is actually not that much of a high quality.  
And now you're ending up with so many solutions.  
And you don't know which one is actually meaningful and actually  
has a product behind.  
So there is need for decision-making.  
And having an opportunity to leverage  
GenAI for decision making could really help leverage evaluations  
at scale.  
Think about all those use cases in real life  
where you need to evaluate content.  
For instance, as a researcher and professor,  
I need to write lots of research.  
And every time I'm writing a paper, it goes under review.  
This is very expensive in terms of time and cognitive bandwidth  
to evaluate the quality of a given paper.  
Think also about all those legal documents.  
You need lawyers, attorneys to evaluate and check  
the quality of what was written.  
Maybe AI can help there.  
And lots of startups are already pushing this.  
Think also about all strategic decision-making-- for instance,  
in finance or you're a company, and you  
want to figure out what should be your next product,  
your next strategy, the next idea that your team should  
push further.  
AI may help you making the decision.  
Coding is such a huge prospect for generative AI.  
How can you evaluate the quality of your code?  
So code review.  
Companies like Google, Microsoft already use this a lot.  
In the topic that we are going to cover today--  
and also we already touched upon in the previous lecture--  
the whole concept of having AI helping you for business model  
solutions, products-- so the early stage of innovation  
processes.  
And so many decisions need to happen there.  
And of course, maybe you're a student  
wanting to apply for college, graduate school,  
or a given program.  
Imagine how many of those applications we receive.  
Personally, I receive lots of emails of students  
interested in working with me.  
And I really try to read everything I receive and spend  
time answering.  
But it's also a huge burden and a bandwidth  
that you have to allocate for this.  
Could you automate evaluating applications?  
And maybe you're scared.  
Oh, my god, an AI is going to evaluate me.  
But it does not mean it's bad news.  
Potentially, the AI may even improve  
the quality of the screening.  
So this is what we are going to discuss today.  
As I mentioned, the future of work  
really entails this AI for decision-making.  
And we've seen that AI revolutionizes  
productivity, idea generation, and strategic decision-making.  
The motivation for today is a case study  
in GenAI for innovation.  
It's very important to have access  
to expert evaluation of early-stage innovations,  
because this is what will tell, for instance, investors  
or the founders if they have a chance to make it  
into a successful company.  
But the process of having expert evaluators-- for instance,  
venture capitalists--  
has a lot of financial and cognitive costs,  
a lot of information overload.  
Maybe they have lots of contents to review.  
And they also faced lots of biases themselves.  
Maybe they feel overconfident.  
They over rely on their assessments.  
And then they have lots of heuristics  
that they've learned across the years.  
But it doesn't mean it would necessarily  
apply to your given company.  
So there is an opportunity to leverage generative AI  
to enhance this whole process.  
So remember, this is a slide I showed in the previous lecture.  
You have a challenge, a problem to solve.  
We covered how we can collaborate  
with AI to generate meaningful, valuable, novel solutions.  
And we also discussed crowdsourcing,  
where you can ask a whole crowd for more ideas.  
But we also mentioned that it's so easy  
now to generate those ideas that I'm overwhelmed by figuring out  
which one I should push more.  
This is why the topic for today is  
how generative AI will help you evaluate early-stage innovations  
at scale.  
So these are the learning outcomes.  
We'll look into how you can design AI approaches to assist  
this human decision-making.  
We'll look into multiple ways of asking AI to help you.  
We'll also analyze how your domain and AI expertise level  
and depending also on the subjectivity of the criteria  
to evaluate the solutions.  
We'll look into how this will influence  
the human-AI collaboration process,  
with the specificity of the early-stage innovation scenario.  
So think about the fact that if you're an expert  
and you have an AI to help you, will it benefit you to evaluate?  
Or will it make it worse?  
Or maybe it won't change anything.  
But now let's say you have no expertise in evaluating startup  
ideas.  
Maybe AI will help you getting upskilled.  
That's something we covered in a previous lecture.  
And finally, we'll also discuss strategic human-AI collaborative  
workflows to optimize this division of labor,  
specifically around automation and augmentation  
in the context of idea evaluation.  
End of transcript. Skip to the start.  
\`\`\`

L3.2 Case Study: MIT Solve and AI for Innovation Screening  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The work I'm presenting today  
is real work that I've done with my colleagues.  
And our goal is really to build tools and methodologies that  
will have impact.  
It's not just knowledge we discovered.  
It's actually knowledge that is being implemented  
and already transforms workflows.  
So Solve is based at MIT.  
It's a marketplace for innovation.  
Every year, they have multiple crowdsourcing challenges  
for a better world, around climate, financial inclusion,  
health equity, education for all.  
Their goal is to fund projects from all over the world,  
in particular low- and middle-income countries,  
to help them achieving huge impact.  
They've given more than $70 million  
in funding to those projects which  
impacted millions of lives.  
And they've helped over 800 projects with this funding.  
But how do they do this?  
They have dozens of challenges.  
And for every challenges, they received thousands of solutions  
to evaluate.  
It's a huge burden to go through so much content.  
It's amazing because it means that so many people want to do  
great things for the world.  
But you don't have enough money to fund everyone.  
And it does not mean that every idea you receive  
is worth spending some funding there.  
So they have humans and a whole process  
to figure out how they should allocate the resources.  
Our goal is to help them making better decisions,  
alleviate the cognitive bandwidth  
that they have to allocate there,  
such that the whole process becomes better for everyone.  
Remember, screening is overwhelming.  
Think about having to evaluate hundreds of ideas in a row.  
That's something that can be exhausting, and imagine  
all the biases involved.  
So we want to help the whole process.  
Let me describe in more details how  
MIT Solve is going from an application to selecting  
the best ones and the finalists and finally the winners  
that will receive funding.  
Today, we are going to leverage an actual challenge  
about global health equity.  
And it was from earlier in 2024\.  
They received 531 applications.  
They then asked the staff of the company, MIT Solve,  
to figure out which solutions should be screened out such  
that they obtain about 40% of the solutions being  
semifinalists.  
Then you will have a network of judges and sponsors  
to go through this round of semifinalists  
to select a very small short list of finalists.  
And those ideas are now potentially the very best.  
But they only want to invest in about half of them.  
So they have expert judges, technical vetters to figure out  
who will be the winners.  
And the winners get money, mentoring and support, community  
membership, and potentially a lot of money  
more in additional prizes.  
You can see that there is a whole very long process.  
But the one that is also extremely demanding  
is how to go from 531 to 229\.  
There are so many applications to read.  
Everyone includes lots of pages of content.  
So our goal is to help them specifically  
around the screening process.  
Remember this curve about the idea quality and distribution  
of ideas?  
Overall, the ideas are falling under a log curve or a bell  
curve.  
We really want the very best ones.  
So our goal is to figure out which ones we should eliminate.  
So these are the bad apples or ideas that  
are not well written enough.  
And of course, AI can help in assessing  
the quality of the best ones and potentially  
improving them even better.  
Our partners at Solve told us that since the arrival  
of ChatGPT, the number of solutions  
they received has more than doubled.  
It's great news.  
It means that more people participate.  
But it also means that potentially  
the quality of those solutions is decreasing.  
Why?  
Because it becomes easier to generate a business plan,  
a startup idea.  
But it does not mean you actually have an actual product.  
So they face the cognitive challenge  
of having to go through more content that's  
very well written, because it's from ChatGPT.  
But potentially, the underlying actual quality  
is lower than it appears.  
Really, it shows more than ever that having a generative AI  
pipeline to assist the screening will be helpful.  
So here is our methodology to experiment  
with large language models and idea screening.  
Our goal is to do science.  
So we want to help them and build a tool,  
but we have a principled approach.  
So it's also interesting for you to visualize  
how we do research in such a topic  
and how we derive conclusions that will inform the tools  
and how to build good collaboration prospects.  
We did four steps.  
Step number one, we partnered with MIT Solve  
and developed a large language model screener  
using their historical data.  
Then we took this model and prepared a field experiment,  
which means that we actually built a tool  
and signed some legal documents such  
that we can have human subjects using the tool.  
And we wanted multiple types of subjects-- experts,  
nonexperts-- to have a variety of insights.  
Step number three, we deployed the large language model  
recommendations on actual data.  
And we have a web app that we actually built ourselves  
and tested with real people.  
Thanks to all the data we collected,  
we could identify the optimal form of human-AI collaboration.  
So let's look into the research questions  
we want to answer through the data analysis.  
First of all, we developed two types of AI--  
a black box AI and a narrative AI.  
The black box AI is basically just a large language model  
recommending to pass or fail a given solution--  
no details on why, just the final suggestion from ChatGPT.  
The narrative AI is the recommendation  
from ChatGPT but also with a narrative,  
meaning an explanation from why ChatGPT believes  
this solution should fail or pass each criterion so there is  
more to grasp for the humans.  
So our question was, having those AI-generated narratives,  
will it influence in a good way or a bad way?  
Will it change the way people evaluate,  
meaning having more to grapple with?  
Will it influence how I approach the collaboration?  
The second aspect we investigated  
is the fact that when you evaluate solutions,  
you actually face evaluations in objective criteria,  
meaning that's something that can be fact checked  
and has actual definitions of what is good or bad,  
or potentially something subjective, which  
is more personal, will relate to your intuition, your experience,  
of if you think that this is a good example or a bad example  
but based on your personal intuition.  
And we wanted to figure out how AI will influence you  
potentially differently depending  
on if it helps you for something objective or subjective.  
Finally, we wanted to figure out if your domain expertise will  
actually influence the way you overall use the platform.  
Here are all the results very quickly so  
that you have an idea of where we're going.  
It turns out that having the narratives  
really influenced the human decisions, more than having  
the black box models.  
That could be intuitive in a way,  
because if you have explanations,  
you are going to react with respect to those explanations.  
So you're going to shape the way people should  
look at a solution.  
We also witnessed that subjective criteria amplified  
the effect of the AI narratives more than it  
did for objective criteria.  
And finally, interestingly, the effects  
were consistent across all expertise levels.  
Whether you were evaluating ideas  
for the very first time in your life  
or whether you've done that for years and years,  
people were influenced the same way by the tool.  
So very interesting to know that as well.  
End of transcript. Skip to the start.  
\`\`\`

L3.3 Methodology for AI Assisted Screening  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: And I want to mention something exciting that maybe  
you've heard from a previous module lecture or a course  
that you have explainable AI, which  
is the concept of trying to explain how your AI model makes  
a decision.  
The goal is to make the process more transparent.  
Maybe you analyze the features.  
Maybe you try to get interpretable trees  
to explain how the model actually  
made the final prediction.  
So overall, you end up with an explanation you can verify.  
Here, with those large language model narratives,  
we are talking about something different.  
The way you get the narrative is from a user prompt.  
It's a black-box process to generate the narrative.  
The large language model may generate an explanation  
for its decision.  
But this explanation is not actually  
reflecting the reasoning of the model.  
It just looks like it is a reasoning,  
but it's just a probabilistic, plausible generation  
from ChatGPT.  
So this is really a generated explanation, not  
an actual explanation of how the decision was made.  
Yet it does not mean you should scratch it.  
It could be useful to trigger your critical thinking  
or help you visualize an idea under another perspective.  
So the key difference really is that explainable AI  
will provide a traceable explanation from the model  
mechanics, while the large language models would just  
generate a plausible, probabilistic narrative.  
So keep that in mind.  
Let's go back to our steps.  
The first step was to partner with MIT Solve  
to develop this large language model screener.  
Traditionally, MIT Solve has developed a rubric  
to screen the solutions.  
And in this rubric, you have five criteria.  
Some are objective.  
Some are subjective.  
We prompt engineers with GPT-4 using techniques I already  
covered, like chain of thought and few-shot prompting,  
to actually emulate the screening process  
and have the model go over every criterion  
and give me a screening decisions for each one of them.  
And in the end, thanks to this, I  
can get a recommendation whether AI is telling me  
that I should pass or fail a solution to the next stage.  
And also, remember, my goal is to get those narratives,  
these generated rationales for the decisions  
that I could potentially leverage.  
Just to give you two examples of criteria  
that were actually used, here is an objective criterion.  
Is the solution at least in the prototype stage?  
You want to have solutions that are not just a concept  
but actually made already into a product that  
is being potentially tested.  
That's one of the requirements from MIT Solve.  
And here is a subjective criterion.  
Is the solution good enough that an external reviewer should take  
the time to read and score it?  
So think about that?  
This is such a subjective question.  
How do you know that this is good enough?  
You don't necessarily have the ability to calibrate.  
If you've done this for years and years,  
maybe you have read hundreds of solutions already.  
So you know how to calibrate the given evaluation.  
But I also asked people who've never  
done that ever before to also answer using this criterion.  
And of course, they don't have the same calibration.  
So this is exciting to figure out  
how AI will influence you for such a criterion, for instance.  
Here is the prompt I used.  
And as you can see, lots of elements were involved.  
First of all, to have the model giving me the final screening  
decisions, you start with a system message  
that will give the context.  
I want to tell the model you are a startup solution screener  
and so that it knows what's happening.  
It's important to give context.  
So remember this.  
Now that I gave context, it's time to give instructions.  
I want the model to critically assess the solution.  
So I gave lots of instructions about how to properly assess  
a solution with some sort of critical-thinking advice  
for the model.  
Then I gave again context.  
This time, I want the model to help  
me evaluate the Global Health Equity  
Challenge I just mentioned.  
So the model needs to know what is the actual challenge.  
So I just copy-pasted the actual description  
that humans had received.  
Remember then that my goal is to evaluate multiple criteria.  
So I gave the given criterion and the specific requirements  
described to pass or fail.  
It's also the first time the model is doing this  
with this kind of challenge.  
So it's important to calibrate the model.  
How do you do this?  
Using few-shot prompting, meaning I'm  
going to copy-paste one passing example  
from the previous years and one failing example  
from the previous years.  
Like this, the model has an idea of what  
is considered good or bad for these given criteria.  
This is really the ability of the model  
to pick up on a little bit of content to do a better decision.  
So it's an emerging capability of the model to learn on the go.  
And finally, of course, now that you've  
crafted the whole prompt to have the context, the description,  
the criteria, examples, you give the final solution to evaluate.  
So you copy-paste the entire text  
from the humans who submitted.  
And you ask the model to evaluate it.  
And you tell the model, I want this in this given format.  
I want a reasoning or for why you're going to pass or fail.  
I want you to summarize your reasoning.  
And finally, I want you to give me  
the probability that you think this is passing or failing.  
Remember, even this probability is a probabilistic generation  
from the model.  
It's not something that the model actually thinks.  
It's something that comes out from the process  
of token generation that you could  
study in the previous course.  
So really, we're leveraging the capability of the model  
of reading lots of content.  
And we rely on its best assessment  
and probabilistic assessment of the content.  
So this is here a chain of what we tell the model to think step  
by step and to have a proper rationale before giving  
its decision.  
Step two.  
Now that we have this model, we are  
going to layer the field experiment into the screening  
process.  
So we actually had four different study sessions.  
And we conducted those sometimes in person, sometimes  
through Zoom.  
The way it worked is we first give a 10-minute training  
to the people who are going to screen.  
And they have a 60- to 90-minute screening session,  
where they have to do it in a row.  
Then we have multiple groups of people.  
We did four different field experiments, some of them  
with expert judges from MIT.  
So we literally took the people who  
do that every year, and we gave them the tool that we built.  
But we also enrolled students from different programs  
to participate.  
For instance, in some teaching, often  
at the University of Washington in Seattle,  
I had about 120 students taking my course on AI and generative  
AI.  
And I asked every single one of them to do the studying.  
And it was part of their homework.  
So thanks to all of them and all those participants,  
we are very grateful, because we collected lots of exciting data  
to conduct our study and have interesting conclusions.  
But overall, what's great is that we  
have experts and nonexperts.  
So we can see how they will be influenced differently  
by the tool.  
So remember, we do things with the Global Health Equity  
Challenge.  
We had initially about 500 solutions.  
We only selected 48 for our study.  
And we selected them randomly.  
Then for every single participant involved,  
we randomly assigned them to a sequence  
of potential use of the tool.  
We have six possible sequence, and I'm  
going to describe those more in detail soon.  
They either start with a control condition,  
where they have no AI involved.  
And then they are going to receive potentially  
black-box or narrative AI help.  
Or it's also possible they start with black-box AI,  
and then they move to narrative AI.  
Or maybe they start with narrative AI,  
and then they move to control.  
It's a standard practice when you do field experiments to have  
a controlled setting and also potentially multiple treatments  
such that you can disentangle the effects of having  
the sequence aspect.  
So now that I have those six sequences,  
I will ask the people who participate  
to screen 5 to 15 solutions in each part of the sequence, which  
gives 10 to 30 evaluations in total.  
They all use the tool we built.  
This is how it looks like.  
You can see a platform where you have the whole solution  
application.  
That has multiple aspects and questions.  
Those are the answers from the actual people  
who submitted to the challenge.  
You can see that they have multiple criteria  
they have to pass.  
In particular, you have those five.  
Is the solution application complete, appropriate,  
and intelligible?  
That's a subjective criterion.  
Then you have three objective criteria.  
Is the solution at least in the prototype stage?  
Does the solution address the challenge question?  
Because, of course, you want something  
that is in scope with the challenge.  
Is the solution powered by technology?  
MIT Solve, because it's hosted at MIT,  
really cares about having technology  
as the core of the idea.  
So they really want to check that what you propose  
involves technology.  
And finally, the criterion I already  
mentioned, is the quality good enough  
that an external reviewer should take the time to read  
and score it?  
Those criteria are classified by order of importance.  
You should check the first one, then the second one, et cetera.  
If you fail any single one of them,  
then this solution should fail.  
If you pass, it means you passed everything, which brings us  
to the fact that every participant has  
to read the whole application in just two minutes  
and a half, which is super challenging, because you have  
5 to 15 pages of content on average.  
It's huge.  
So of course, they cannot read everything.  
And then they decide if they should pass or fail.  
And if they fail the solution, they  
have to decide for which criterion, meaning,  
which one was mostly failed?  
Of course, it's a burden to read so much, especially  
if you're not an expert.  
This is why it's exciting to see that having AI to help you  
may enhance the process.  
So remember the treatment one is this black-box AI will just  
provide the recommendation from the large language model.  
And you can see here, it tells you  
that this idea passed the four first criteria  
but failed the last one.  
So it's a fail.  
And the treatment two is narrative AI where you have also  
those recommendations.  
But also, you have the narrative,  
meaning the explanation for why it passes or fail,  
which can help humans making better decisions, potentially.  
Remember that those are generated rationale.  
Those are probabilistic generation from ChatGPT,  
not an actual reasoning but something  
that looks like a reasoning.  
This is why it's exciting to see if it can be helpful.  
Now that we've seen how the platform looks like  
and that everybody participated, we collected tons of data.  
So here is a graph, a histogram showing you how  
people were impacted by the AI.  
We are visualizing right now the passing rate  
depending on the condition.  
So the passing rate is, how many solutions did you pass out  
of all of the ones you've seen?  
AI was the harshest.  
This is because we calibrated the AI in the training stage  
to replicate the historical passing rate of MIT Solve, which  
was around 40%.  
And you can see that the solutions were so well written  
that in the control condition, where people had no AI,  
people were actually quite optimistic about the quality  
of the solutions.  
And they gave a passing rate reaching nearly 70%.  
But the more people have access to AI,  
the more they start failing the solutions,  
probably because they were influenced.  
If you have black-box AI, it's already decreasing.  
If you have narrative AI, it decreases even more.  
So overall, the AI-assisted screeners  
were 9 percentage points more likely to fail a solution.  
This graph is now looking into more details,  
whether people were influenced differently,  
if AI suggested to pass the solution,  
to fail the solution based on something objective,  
or to fail the solution based on something subjective.  
You can see that when AI is telling you to pass,  
people were more convinced to pass the solution.  
But there was no difference whether you  
had black-box or narrative AI.  
If AI recommended to fail the solution based on something  
objective, it turns out that people again  
were not more influenced whether they had the narrative or not.  
But for sure, they were harsher than in the control condition.  
And finally, when you had AI recommending  
to fail on something subjective, the explanations  
were actually highly persuasive.  
The screeners were adhering more to the narrative AI's  
recommendations, 12 percentage points more,  
than if they had just a black-box solution,  
really showing that those narratives really highly  
influence the decision-making.  
End of transcript. Skip to the start.  
\`\`\`

L3.4 Human AI Interaction Expertise  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's dive more into the fact  
that AI is convincing people in subjective criteria.  
We may think that experts or nonexperts  
may be influenced differently.  
But our results show that people were influenced  
the same way, which means that the influence factor matters  
a lot.  
Do you want a system where AI will really influence you?  
Is that the desired process?  
Or is it something you should engage people  
with such that they have more critical thinking?  
It brings us to the fact that it's important  
when you have people using a new type of tool  
to train them properly such that they  
are aware of the behavior that will happen.  
And very excitingly, having assistance from AI  
improved the quality of the screening decisions.  
So for those 48 solutions we had, we actually  
asked an external set of judges to grade them  
according to multiple criteria that  
are used in the other stages, like from semifinalists  
to finalists.  
Thanks to this external validation data,  
we were able to see who was the best at matching those expert  
judges.  
It turns out that having access to the AI,  
whether it was treatment one or treatment two,  
meaning black box or narrative, really helped people  
failing the solutions that should fail and pass  
the solutions that should pass.  
And this is great news that having  
AI can enhance your skill.  
So overall, AI assistance improves quality  
of screening by 2% to 6%.  
Great news.  
However, the effects were a bit different for experts  
and nonexperts.  
For nonexperts, having AI assistants  
really benefited them more.  
It scaled up their expertise.  
They have never done this before, but thanks to the AI,  
they're able to have a better judgment process.  
However, for nonexperts, there is not  
that much of a difference.  
But we figured out that if they have black-box AI,  
they're a bit better than if they use narrative AI.  
That may seem surprising, but think about it.  
If they have a narrative, it means  
I'm going to think for them.  
And then they're going to think shaped already  
by the suggestion from the AI.  
If I don't give them any narrative,  
I give them just a suggestion, they're  
actually going to think harder and look for information  
in the whole solution to validate or override  
the AI decision.  
So I prompted them in a way to be more critical.  
And this is what also we figured out from the interviews  
that we had with those people afterwards.  
We collected lots of feedback about how they used the tool.  
So having the black-box AI may potentially  
be sometimes better than having an AI that gives you  
more information, because this more information is not  
necessarily going to increase your critical thinking,  
or it may push you in worse directions.  
Remember this very well too.  
So in conclusion, we could see from this whole process and data  
analysis that AI can really help evaluators and organizations.  
It can alleviate cognitive and financial burdens.  
You can scale up expertise across the knowledge boundaries.  
And remember that those narratives  
can be highly persuasive.  
It's very easy for generative AI to generate  
convincing, reasonable-sounding narratives that  
may push you into decisions that are not necessarily desirable.  
It's possible it also helps.  
It depends on the use case.  
So it's important to think about this new division of labor--  
automation and standardization potentially  
for objective criteria and augmentation  
with human oversight for subjective criteria.  
From our study and interviews, we really  
figured out that it's important to develop  
a human-AI interaction expertise and to design systems that  
will encourage the critical engagement with the AI  
recommendations.  
You want to see how the humans will be involved.  
And the design will matter so much.  
So the study from today could illustrate this.  
So if we summarize all of these in a graph,  
we can see that if you have human only,  
the value is especially important when  
you want to evaluate something subjective,  
because this is what requires domain expertise and lots  
of experience and intuition.  
If you use AI as a ghost evaluator,  
meaning you just use AI to make a final recommendation,  
it's harder for AI to get this intuition.  
You will need really good prompting.  
And you may need to involve the human in the loop back  
whenever it's very subjective and very important to evaluate.  
However, if you use AI as a sounding board,  
remember this concept of the cyborg, where  
you collaborate with the AI, and you go back and forth.  
There is lots of opportunities for AI interaction expertise  
right there.  
And now I want to conclude this lecture  
by giving you some creative tips about how  
you can enhance your expertise with using those tools.  
It's not like lecturing.  
It's more my personal tips, my personal beliefs  
of how you can become more creative, how  
you can become an artist with AI,  
and develop this expertise in using it.  
I want to thank all my contributors  
on the study I presented today.  
It was joint work with Jackie Lane, Charles Ayoubi,  
my amazing students also from the University of Washington  
who built the app, Amy, Ian, and Camila,  
and our partners at MIT Solve, who were so helpful  
and helped us so much building impactful tools.  
And still today, we collaborate together  
to make more impactful evaluations.  
So, Rebecca and Pooja, thank you.  
As I mentioned, the final thoughts for this lecture  
are about how to develop human-AI interaction expertise.  
Those images you're seeing now are actually  
images I generated over the years with AI.  
And I really believe it's great to be creative.  
I want to encourage you to be an artist.  
I want to encourage you to try the tools in new manners.  
I want you to recover your artistry.  
Whether you think you're an artist already  
or whether you don't think so, every one of us  
can become an artist.  
And using AI is also an art.  
How do I do it?  
I actually interact tons with AI all the time.  
I try so many different questions.  
And I try to question a different manner.  
If it worked, I also try a different way  
to see if it also works.  
And I use many more tools than just chatbots.  
I encourage you to use image generators  
to have a better understanding of how they work.  
Use copilot of all sorts.  
Use AI avatars.  
Explore.  
Explore what you feel is exciting for you.  
I do it all the time.  
This is how I learned so much too.  
Working with AI is really an active process.  
It's not just I'm prompting and I get an answer.  
There is so much involvement from you.  
And the more you get involved, the more you can get out of it.  
And your taste will matter so much.  
So here is an image that I presented earlier as  
an animation, where I wanted to represent  
how I feel when I have to evaluate so much content,  
when I generate so many images and I want to figure out  
which one I really want.  
Here, I have this direction.  
I have this vision.  
But I have so many possibilities around me.  
So your taste will matter to select which  
one is your final decision.  
And curation matters.  
To be able to generate the image right before,  
I actually generate hundreds of images.  
It's so easy and cheap actually now to generate.  
What's hard is to figure out which one to select.  
So your art of curation will become more and more important.  
There is no scarcity in the amount  
of solutions you can generate.  
Really think about that, and leverage AI for not one or two  
ideas, but 10 or 30\.  
And then your curation will be what makes it better.  
I love creativity so much, as you can see.  
And I really believe you should push your creativity out  
of your comfort zone.  
This is a visualization of me with this realm  
of creative imagination.  
This is how I visualize creativity  
in my brain happening.  
And to create this image, I worked hard.  
And it's one of my favorite images and animation  
I've ever done.  
Let me show you how I did it.  
First of all, I started with Dall-E.  
And I generated one image.  
My prompt initially was quite simple.  
It was "imagination in action, pure art."  
I knew that the model reacted in a very interesting manner when I  
put "imagination in action," because it's quite abstract.  
But there is movement with this action,  
and imagination can be extremely broad.  
But I also figured out that the model visualized imagination  
from lots of images it's seen in the training data  
and visualizes it with lots of colors, a bit everywhere.  
I generated hundreds of images, selected my favorite one  
with this silhouette.  
And then there is a tool called Outpainting  
in Dall-E-- you can do that in Dall-E,  
for instance-- where you can take one image  
and keep building around it.  
So it's not one.  
It's now many.  
And I kept doing this to end up with this one, which  
is, in fact, a combination of 30 different prompts and images.  
I kept building all around.  
And every time, I was selecting which one I like most.  
But it means I had my vision of where I wanted to go.  
I was driving the whole process.  
So really, practice iterating and building in multiple steps.  
Don't stop at one little thing.  
It's important for you to build up the initial creation.  
But there is a little issue.  
This character here has short hair.  
As you can see, I have long hair?  
So I actually wanted to refine one more time  
and get my long hair in the silhouette.  
This is how I got something that represented me that illustrates  
how I visualize imagination.  
But here, it's a bit static, while imagination is something  
that is always in movement.  
And I decide, OK, let's combine now another tool.  
Instead of just doing image generation,  
let's create a bit of movement.  
And I just figured out there was an app on the phone where  
I can put a picture.  
And I can decide how different pixels  
should move in my picture.  
So here, the insight for me to you is combine tools.  
Don't stop in only one tool.  
Figure out the strengths and limitations of each one of them.  
And just build this expertise of being a cross-tool person,  
someone who knows fluently the strengths of, for instance,  
ChatGPT or Claude.  
And then use them when one is better than the other.  
This is always evolving.  
So it means you have to play a lot with the tools.  
And then finally, I got this, with all the movement.  
So let's all work together to build a future of human-AI  
collaboration.  
And let's work on pushing our creativity more and more  
for a better world.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
This lecture tackled the nuanced interplay between AI systems and human decision-makers. Learners explored frameworks for when to rely on automation and when to retain human control, especially in high-stakes or ambiguous situations.

Key Takeaways:  
Decision-making tasks vary in how well they can be automated  
AI is strong at prediction, but judgment often requires human context and values  
Over-automation can lead to problems with accountability, transparency, and bias  
Effective systems often use hybrid models where humans interpret or override algorithmic recommendations  
Congratulations on finishing this lecture\! You’ve gained valuable frameworks for evaluating the balance between human and machine judgment in real-world decisions.  
\`\`\`

Lecture 4: Diffusion Models for Text-to-Image Generation  
\`\`\`  
Overview  
Welcome to Lecture 4: Diffusion Models for Text-to-Image Generation, taught by Professor Léonard Boussioux, Assistant Professor of Information Systems at the University of Washington.

This lecture introduces learners to the technical foundations and real-world applications of diffusion models for text-to-image generation. It begins with the core idea of generating images by reversing a noise process, then builds up to key architectural components like U-Nets and the role of language models like CLIP in guiding image outputs. The lecture highlights how diffusion models are used in platforms like DALLE, Stable Diffusion, and Midjourney. Learners gain an understanding of both how the models work and how prompt engineering affects results.

Learning Objectives  
By the end of this lecture, learners will be able to:

Describe the core mechanism of diffusion models: denoising from random noise to generate images.  
Explain the roles of U-Net, the noise scheduler, and text conditioning in model architecture.  
Understand how CLIP-style embeddings guide image generation from text.  
Experiment with and critique the outputs of real-world generative tools based on diffusion models.  
\`\`\`

L4.1 Text to Image Generation  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hi, everyone.  
I'm very excited today to cover one of my favorite topics  
in generative AI, how to create images from text.  
We are going to cover the technology behind and see  
fantastic applications.  
And my goal is also to inspire you to try  
that technology for yourself.  
Here are examples of images I've created in the past few months  
using different models.  
Some of them can look like futuristic cities.  
Some of them can look like fantasy, cute little cats.  
Basically, your imagination is your only limitation  
of what you can generate.  
It doesn't mean that you will get exactly what you want.  
But then you have the opportunity  
to have brand-new creations.  
I love using this for fun but also  
to illustrate my slide decks.  
And as you could see in so many of my slides,  
you have AI-generated pictures.  
And now we are going to uncover how I do this.  
I want to show you a few capabilities from those models.  
For instance, you can also use them  
to blend two images together to combine attributes  
from image one and image two, and sometimes even more images.  
So here, I created two nice logos for MIT.  
And then I merged them.  
And you can see that you have attributes  
from the logo on the left, with all the colors exploding.  
And also you recover the blue from the image on the right.  
And you now have an explosion with more blue appearing  
in the bottom.  
Another example, this time, I'm trying to merge the MIT logo  
I created with an image of a brain that looks like a circuit.  
And as you can see, I recover again attributes from the two.  
So that's an amazing capability of those models.  
They can blend different images together.  
You can also use these models to input a picture  
and ask for a description of that image.  
And now that you have a description,  
you can generate new images from it.  
Of course, you have so many opportunities  
to describe the same image.  
This is why you can obtain different results.  
So here, I used Midjourney to describe  
one of my favorite pictures that we  
covered in a previous lecture.  
And as you can see, I tried to generate images out  
of every possibility.  
They're all kind of similar, but they also  
have little differences.  
So it gives you the opportunity to choose what's your favorite.  
You can also-- out of one initial image  
that it generated here.  
It's that simple, as Mount Rainier, a beautiful volcano  
based in Washington State.  
You can ask for variations.  
And as you can see in the middle, those images,  
they all look super similar.  
But they all are slightly different.  
Look at, for instance, the river or the clouds.  
So you have the opportunity-- if you have an image you really  
like but you want to see different possibilities,  
you can have that as well, with those diffusion models.  
What's cool is that you can also create a zoom out.  
You can try to create everything that's around the initial image.  
And this can be very valuable if you  
want to create a whole landscape for instance.  
Other possibility-- the input will be an image  
and the text at the same time.  
So you can condition the new generation with two modalities.  
And here, I took an actual picture from the MIT campus  
and asked to make it futuristic, cyberpunk, modern, exciting,  
and looking like a smart city.  
And I created one of my favorite futuristic images  
of MIT, where you can see this dome looking  
like a spaceship and the city of Boston  
looking like it's in the next century.  
So this is something you can do from the Midjourney interface.  
So this is what we are going to cover today.  
I just showed you a few examples of what the technology can do.  
And so we are going to explain the principles and capabilities  
of those diffusion models, including  
how you can do some iterative denoising, which  
is the principle of how those images are created.  
And we will describe how high-quality images  
can be generated from that initial noise plus your prompt.  
To be able to generate images from text,  
you also have a special process.  
You need to embed your text to guide the image generation  
process.  
And I'll show you how certain models  
can be used to colearn how an image corresponds  
to a specific text.  
And finally, we'll also discuss different applications  
of diffusion models across different fields.  
And we'll highlight that this has  
a great positive impact for problem-solving and innovation.  
End of transcript. Skip to the start.  
\`\`\`

L4.2 Demonstrations and Examples  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's start with a demo of those generation models,  
such that I can illustrate a few key ideas about how they work.  
First of all, this is what you can  
see if I ask a few different types of models, imagination  
in action.  
That's a prompt I already used in a previous lecture.  
I love that prompt because it's very abstract,  
and it also has some mystery.  
What would I get from imagination which is so broad?  
An action which is something that creates some movement.  
Here is, for instance, what Midjourney visualizes.  
And you can see lots of kids trying to play  
or creating, imagining, while, for instance, DALL-E is more  
about a silhouette with this cloud of colors.  
So those two models visualize and imagine your prompt  
in a different manner.  
This is because those two models, although they're  
based on similar technology, have a different model  
architecture, different training mechanisms, different training  
data, and so many other factors which  
will impact the final way of how they process your image.  
So now next let's look into how the same prompt,  
"Imagination in action," can impact the model differently,  
depending on the version of the model that was developed.  
Those models change all the time.  
They evolve.  
They typically improve, but it also  
means that they will interpret your words  
in a different manner.  
Here is the same model, Midjourney,  
from the same company but at different times,  
meaning different versions of when they were developed.  
For instance, in July 2022, you can  
see that those images look very naive.  
The shapes are unclear, and you don't really  
know what's there when you put this imagination in action.  
A few months later, it already improved.  
You can see that this time the faces of the kids  
look much better-shaped, but the images  
lack granularity and details.  
And, again, if you keep going month after month,  
you can see lots of improvement happen, which  
means that they improve potentially  
the quality of the training data, the quality  
of the architecture, et cetera.  
Fast forward months later and the year after.  
It's already looking super impressive.  
And in my opinion, those models all  
generate things that are equally good.  
But it's about your taste.  
You can see it gets more and more granular with so many  
more details.  
And the models also have their artistic point of view.  
So really remember that the way those generative AI models  
interpret your text will keep changing.  
So you have to constantly update yourself  
about how a prompt could react best according to your desires.  
So now let's take my favorite image out of all the ones I've  
generated with this prompt.  
It's this one.  
I like it a lot because we can see the imagination happening  
with this girl.  
She is currently thinking deep.  
She has lots of colors and flowers around,  
and you can see this cloud of inspiration around.  
I love all of those details, so I  
chose that one to keep exploring what diffusion models can do.  
But now let's look at the few details more precisely.  
Do you notice anything strange or weird in this image?  
Look at the pen that the little girl is handling.  
This is a very long one, longer than usually.  
And maybe it exists in the real world,  
but it's weird to have such a long pencil with two sides  
where you can write with it.  
So now let's look at her left hand.  
You may notice that she only has four fingers.  
It's a typical issue with diffusion models.  
It turns out that they don't perceive the world  
the same way we do as humans.  
They don't know the rules that we know.  
They just learn things based on pattern-matching.  
And very often, when they see pictures,  
maybe people are handling things like this.  
And you don't see actually the four or five  
fingers all the time.  
And so the models learn what may look like a plausible hand,  
but they don't know it has to be five fingers.  
So that's one of those issues.  
And we'll explore more about why this happened.  
I want also to edit this image.  
So, for instance, I can just add a little fish in the picture.  
That's a possibility with the latest tools.  
You just select an area, and you can edit at will.  
Very exciting.  
And you can also, as I mentioned previously, zoom out.  
So now I have more context all around my picture.  
Notice also that the more you start zooming out,  
the more of the details will be challenging for the model  
to process.  
For instance, here the new fish are actually not  
properly shaped.  
And I keep going.  
So here, for instance, I built what's on the side.  
And say you have lots of fish on the left, but some of them  
look kind of strange.  
And if you look on the right, you  
have this little kid or creature.  
It's hard to say.  
And then the arms of this character  
are actually looking very strange again.  
So it shows that the models may have difficulties  
to generate exactly how the real world should look like.  
But overall, if you look at the picture, it all looks great.  
You also know that I love animations and videos.  
And so you can go forward and animate your image.  
And I'm using here a little software again from my phone.  
And it's exciting that it doesn't need to be static.  
It doesn't need to stop at the image level.  
You can push your creation further.  
And now I also take the same image  
and push it into another model called Runway.  
And this is an example of a video  
I could generate out of one image and one little text.  
So it's another possibility with this type of model.  
I'm now going to show you a demo of very impressive video  
generated from a model called Sora from OpenAI.  
It looks extremely real, and sometimes it's even frightening.  
Here you can see dolphins flying, a Jeep driving,  
and even the dust, a festival, people in the train,  
and even the reflections on the windows, robots  
in a futuristic city, someone walking in New York City  
but also with the reflections on the ground, the ocean,  
someone blowing the candles, the snow from the dogs.  
This is incredibly impressive that you  
can have something like this.  
And it looks so real that it may prompt  
us to think, oh, my god-- what is real or not real anymore now?  
This is why those models are not publicly available yet,  
because they want to do a proper release.  
It's also very expensive to run.  
So there is potential, of course,  
for the future of image and video generation.  
And it could transform the whole field of creativity.  
I want to show you another example where,  
although those models may look super impressive,  
they understand even maybe the physics and the world  
is actually not true.  
They don't know the rules of physics the way we do as humans.  
They just try to generate things, again,  
that look very plausible and real.  
Look at this video in detail.  
Look very carefully at what's happening.  
Did you notice anything weird?  
Let's play it again.  
And this time, pay attention to the flag on the boat.  
Pay attention to this red flag on the boat on the right.  
The boat is about to flip.  
And now the flag that was behind is actually  
coming in front of the boat.  
That's not possible in the real world,  
but it's a very subtle thing.  
And it was very plausible from one image to the next one,  
because everything was smooth.  
And you could see that the boat was moving slowly,  
changing sides.  
So the flag also decided to remain on the same side.  
And at the pixel level, it looked all correct.  
That shows you that those models don't understand physics,  
although they generate things that look extremely real.  
And now I want to show you how much the right words can matter.  
Here it's again the same prompt, "Imagination in action."  
And I just add one more word--  
for instance, "Imagination in action and galaxies."  
"Imagination in action and pollen."  
"Imagination in action and pure art."  
All those images are looking similar.  
But they have a different energy, a different feeling,  
emotion, because the one word you add  
will create those subtle cues.  
So remember that the way you talk to this model  
will really impact the final outcome.  
And even if you use the exact same prompt,  
the exact same model, you also have the ability  
to vary the style.  
For instance, in Midjourney, there  
is a parameter called stylize, where  
you can have the model trying to be  
more or less creative out of your prompt.  
So here it's the same prompt, "Imagination in action pollen."  
And you can see that depending on how much stylization I put,  
the model will start taking more liberty  
and trying to have its own artistic point of view.  
End of transcript. Skip to the start.  
\`\`\`

L4.3 Iterative Image Denoising  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So here is the lecture plan  
to cover that content.  
We've covered, in previous courses and modules, what  
is called discriminative AI, when you start with some content  
and you want to classify into, for instance,  
if it's a bird, an insect.  
This is not what we are going to cover today.  
Today, we are going to cover generative AI, where you start  
with a prompt, like bird, and the generator  
will give you new content.  
And we are going to discuss how we are going  
to get those m quality images.  
It's called stable diffusion.  
And, also, how can we control these image generation process?  
And this is done through something called conditioning.  
We are going to use the text to influence the way  
the image shall be generated.  
So here is the motivation.  
We want to generate images with this generative model.  
And there is an infinite possibility of good images.  
How will we get them?  
With the word "bird," those three pictures are actually  
looking all correct.  
They all represent a bird.  
And I did not give any previous detail.  
So the way it works is that we start from a noise image.  
We just start with pure noise, using every pixel  
as a random number.  
And this noise will be what moves into the generative model.  
This is the input of your generative model.  
And then, now that it went through the generative model,  
it's going to get one new image.  
So one specific noise going through the generative model  
gives one new picture.  
Now let's take another noise.  
And I push it through my generative model,  
and I get another bird picture.  
Again, let's take another type of noise,  
push it through the generative model.  
And again, I'm getting a new bird picture.  
So for every different noise, you get a different picture.  
To train the models, we have access  
to so many images on the internet.  
And actually, all those companies  
having image generation models leveraged  
what they can find on public databases, on Google Images,  
and also on private databases.  
It doesn't mean that those images that you  
can find publicly have no copyright in them, which  
is, of course, an issue.  
But this is how they collect so much information  
to train their models, and they also  
leverage the captions associated with each one  
of those images, such that they have  
a data set of caption image.  
This will be useful, and we'll see that later.  
So now that we understood that those images are generated  
from noise, we haven't covered how  
we can train the model to understand  
how they can go from noise to an actual image that looks real.  
This is actually extremely hard if you think about it.  
How can I get and structure noise into something great?  
The secret is to do the reverse.  
Given an image, can you create a noisy image from it?  
That's actually extremely easy.  
You just have to add a little bit of noise  
to your image sequentially.  
So you start adding a bit, then you keep adding,  
and now you obtained, out of a given real picture,  
a whole sequence of noisy pictures.  
So remember that we add sequentially noise to that image  
by adding random numbers.  
Now that we have the sequence of images  
from the actual final image that is desired to the pure noise,  
I can leverage this to train a model.  
So the way it works is you take a noisy version of an image.  
That will be your input.  
And now, because of this data set you just formed,  
you can actually make it less noisy.  
And you know how it would look like in a less noisy version  
because we artificially created this sequence.  
So x1 will be your input image, and y1  
will be your target for this specific one.  
And you can do that in the sequence.  
Again, now I have x2, which is a noisy version,  
and I know how it would look like with a bit less noise.  
So I have, now, y2, the target.  
And I keep doing this all along my sequence.  
I have here a super noisy version on the right.  
And then, on the left, it's a bit less noisy.  
So the relationship between x and y  
is that x will be your input image,  
and y will be the less noisy version of this image.  
And now the question is, how do we use these xy pairs?  
This is what will be very important for our training.  
We are going to run the classic stochastic gradient descent  
algorithm as usual.  
Input is a noisy image.  
You push this through a neural network, a special one,  
and then you have the less noisy version, which is the output.  
But now we know how it should look  
like because we artificially created the noisy versions  
from the initial one, and I can just reverse the process.  
So remember that idea--  
noisy to less noisy.  
And I have training data to make it happen.  
And then the secret is to do it in a sequence over and over.  
You start with very noisy.  
You make it a bit less noisy.  
You take this image as input.  
You pass it again through the exact same network  
so that it makes it a bit less noisy.  
You take this new output, you make it a new input,  
and then you get the final image.  
So it's a process that repeats over and over  
from the pure noise to the final one.  
And because we have the whole training data,  
this is how we can make it happen.  
And to show it in a different manner,  
this is how it looks like from the input to the output.  
And it's really a beautiful loop.  
Of course, that's kind of expensive  
because it means you have to repeatedly denoise an image.  
And this is expensive computationally in particular.  
And it's not immediate to get an image from pure noise.  
And remember, out of different noise,  
I can get different images.  
This denoising neural network is called a diffusion model.  
It's going to diffuse those pixels into a final desired  
outcome.  
So here I can get, for instance, the MIT campus or a cute cat  
out of two different examples of noise.  
Now we need to discuss the details.  
There are lots of variations of how it happens,  
but my goal here is just to illustrate a way  
to go from noisy version to less noisy version.  
And this model is called a U-net because it's shaped like a U.  
You have many variations of the architecture,  
but what matters is that you have the left part that  
will be responsible to take your initial image,  
condense it into a smaller representation  
and, out of this small representation,  
build it back to the initial format.  
So the right half of the U will use a type of convolution layer  
that is a bit different from the one on the left,  
because the one on the left is responsible for compressing  
information, and the one on the right  
is responsible to take a compressed representation  
to build it back into the initial space.  
So there exists architectures to do this.  
To guide this whole reconstruction  
to the initial process, the U-net  
is using what is called a cross-connection.  
So this is going to take information from the left  
and share it in the right part of the network such  
that the reconstruction happens properly.  
So it's a complicated architecture,  
but really the intuition is I take my initial image.  
I'm going to compress it into a space  
where I collect the most important and crucial  
information.  
There I will do a few little tweaks to remove a bit of noise,  
and I build it back into the initial size,  
but this time with less noise, and I guide this regeneration  
thanks to the skip connections in the middle.  
And I'm guiding this thanks to the cross-connections  
in the middle.  
End of transcript. Skip to the start.  
\`\`\`

L4.4 Text Conditioning and Embedding  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now let's see where we are.  
So far, we learned how we can generate images of good quality  
using diffusion.  
We start with pure noise.  
I push it through the generator.  
But then I don't have any way to control the outcome.  
I just get a random image if I put a random noise.  
So we need to learn a next important detail, which  
is how to control this image generation process with a text  
prompt.  
This time, I want pure noise plus some text.  
And this shall give me what I desire.  
This is called conditioning.  
The text is going to condition the generation.  
But it's also a challenging framework.  
How do I really get to generate something out of a text?  
I really want this text prompt to guide the whole generation  
workflow.  
An idea that could work is potentially, OK,  
if I have a rough sketch of what I want,  
then it's possible I would be able to get my final image,  
because this rough sketch will guide the whole generation  
process.  
The problem is I don't have access to a rough sketch at all.  
So we need to work differently.  
The secret is I'm going to use what  
is called an embedding, meaning a representation of my text  
that should capture the essence of what's in the text.  
And this embedding, this vector will inform the image generation  
process.  
So if I use the prompt "large blue-green hummingbird  
in profile view," that's a prompt.  
I'm going to push this into a text encoder,  
meaning an architecture that is a neural network  
responsible to convert these words,  
this prompt into a representation where  
I could encode all the important characters  
and features into numbers.  
I do not understand those numbers personally as a human,  
but the model will.  
The model is responsible to figure out  
by itself how to design numbers that will be useful.  
So here, for instance, one number  
could be about the size of the hummingbird.  
One number could be around the color, one about the angle,  
one about the fact that it's a hummingbird.  
In practice, it's not that interpretable.  
The features are all mixed together.  
And it's the combination of all of them  
that makes the final outcome representation.  
And now that I have this vector to guide the process,  
I could actually denoise my initial noise  
but guided entirely by having access  
to the values from this vector.  
So now the denoising process will happen alongside the text  
representation.  
It will control the generative process  
to make sure that the final image will possess  
all the visual coherence and the meaningful correspondence  
to the input.  
So to give you a bit more intuition about how it works,  
those embeddings are actually in a very large dimension space.  
There are many numbers that operate altogether.  
So here, it's really for an analogy.  
It doesn't really work like size, color, and angle in space.  
It's more like features being combined altogether.  
But it will give you an idea of how  
those models leverage features.  
So here, I put lots of points in my space.  
And depending on where they are located in space,  
it will correspond to one combination of size, color,  
and angle for my hummingbird.  
So for instance, here, if I select this,  
I have a hummingbird looking to the left and looking green blue.  
Now, if I take a point here, you can  
see that the profile of the hummingbird  
has changed a little bit.  
And the color is also a bit different, still with green,  
but this time it has a bit of red as well.  
And I keep going.  
And you can see that depending on where you are in space,  
your hummingbird is turning, has different colors,  
and may have also a different size.  
So I generated all those images myself.  
And you can see that depending on the words I used,  
which means they will be represented  
in a different manner in the space,  
the model will be guided towards giving you what you desire.  
So to come back to the notion of embedding  
that you may have covered in previous modules,  
this is the concept of a representation of complex data  
into a smaller space.  
The goal is to transform complex high-dimensional data  
into a more manageable form.  
So typically, it's a vector.  
And each dimension of this space will represent  
a latent feature of your data.  
That should capture some semantic or syntactic property  
from, for instance, a text.  
What's valuable is that it reduces dimension tremendously.  
So the very key factor from embedding  
is that it's very convenient to leverage them afterwards.  
And on top of this, they're able to relate contents  
from each other because they have a smaller space where  
things that look different initially at the image space  
will now look much more similar in this embedding space.  
So it really allows you and the models  
to understand what are synonyms, what's an analogy,  
and any linguistic relationship.  
They're used by transformers and many other models.  
And as you turn in space, you can  
see that different numbers may be represented similarly.  
Here, this is a representation of the MNIST data  
set with lots of digits.  
And you can see that digits that are the same, like 1, 2,  
or 3, et cetera, they may appear in this space  
to be very close to each other, because the goal  
of those embeddings is to capture  
what's different or similar.  
End of transcript. Skip to the start.  
\`\`\`

L4.5 Text and Image Embedding  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now that we understood  
that it's great to have an embedding of your text,  
we still need to understand exactly how to build  
this embedding and how they should be leveraged to help you  
guide the generation process.  
So the goal to get good embeddings  
is to calculate a text embedding that  
will be close to the embeddings of the image corresponding  
to that prompt.  
So the secret is to have one embedding from the text and one  
embedding from the image.  
And I want those two embeddings to be related to each other.  
So let's take the prompt "a brown Angora cat sleeping  
on the couch."  
So the question is, now that I have this image and caption,  
I want to compute embeddings from them.  
And those two embeddings can be calculated  
with architectures from the computer science fields.  
For instance, for the text encoder,  
there is a famous model called BERT  
that you may have covered in the previous module.  
For the image encoder, you may use  
a convolutional neural network responsible to understand  
that image.  
And now that you have those embeddings,  
they should also satisfy two requirements.  
If the prompt corresponds to the image,  
you want those two embeddings to match.  
You want them to be very close in the embedding space.  
If they do not correspond to each other--  
for instance, here, the prompt "a mountain with snow,  
blue ambience," this does not correspond to this image.  
So you want the embedding from the picture and the embedding  
from the text to be far away in the space.  
And the question is, how do you understand what's far or close?  
Or how do you measure that?  
There is something called the cosine similarity.  
It's a way to compute the distance between two vectors.  
I want to give you a bit more intuition about how it works.  
You have a geometric interpretation.  
Maybe you've studied that in physics in high school,  
for instance.  
When you have two vectors, if they are very similar,  
they will be nearly overlapping.  
If they are very different, they may be perpendicular.  
Or they might be also opposite.  
This is the same intuition, except that now, we  
have extremely large-dimension feature vectors.  
But we are going to do the exact same thing.  
We are going to compute how close or different they are.  
If the product of those two vectors  
gives something around 1, it means  
they are pointing in the same direction,  
meaning they are quite similar.  
If they are 0, it means they have no similarity.  
They are literally going from completely different directions.  
And if it's minus 1, it means they're completely pointing  
in opposite directions.  
So maybe two words might be related.  
For instance, "blue" and "indigo" are two blue colors.  
So they might be very similar.  
"Blue" and "red" may be are unrelated.  
So this is how you leverage the cosine similarity  
to measure how two things are located  
with respect to each other.  
There is the mathematical formula, if you're interested.  
But that's not the point for the lecture of the day.  
It's interesting to see that it's something  
that is very easy to calculate.  
You just leverage the values from your vector.  
You multiply them.  
And you divide by their norm.  
No worries if it looks too complicated for you.  
So now I have this idea that I need text encodings, image  
encodings.  
That should satisfy the two requirements.  
And there exists a method to do this.  
The literature has investigated this.  
And OpenAI has released, at some point, a model called CLIP.  
For the purpose of this lecture, I  
will illustrate how they did it a few years ago, in 2021\.  
But now there exists more modern methods to make it happen.  
So the idea of the CLIP pipeline is you use a transformer.  
That's something we covered.  
You would just initialize that with random weights.  
And you grab a batch of image-caption pairs.  
This you can find easily on the internet.  
You go on Google Images.  
You take images randomly, for instance.  
And you just look at what people wrote about them.  
So like this, you have a data set that associates them  
together.  
Then you are going to run this initial model, the text  
encoder and the image encoder, such  
that you are going to get some embeddings out of them.  
For now, it's all random.  
You haven't trained the model at all.  
But you just get those embeddings  
for all those image-caption pairs.  
And you are going to build a huge matrix.  
Here, I have a cat picture, a bird picture,  
and a mountain picture.  
And I'm getting, from this first model, three embeddings,  
one for each image.  
And I also got different prompts,  
meaning different texts corresponding to those images--  
a brown Angora cat sleeping on a couch, a flying hoopoe--  
that's the name of the bird--  
green background, and a mountain with snow, blue ambience.  
So three texts, three embeddings for each one of those texts.  
And I'm going to compute the distance  
with all the embeddings from the images  
and the embeddings from the texts using  
the dot product I mentioned, the cosine similarity.  
What you want is to maximize the similarity  
between the images and the captions  
that correspond to each other.  
And you want to make sure that every caption that does not  
correspond to the image should be as far as  
possible from the image.  
So it looks like this.  
In green, this is the prompt corresponding to the image.  
And in red, this is a text that does not  
correspond to the image.  
And now that you have some loss function,  
you can leverage what we learned in previous modules about how  
to train a neural network, because you have the ability  
to back-propagate this whole loss function.  
So overall, if you repeat this over and over,  
having prompts embedded, images embedded,  
you compute the loss function.  
You update your neural network.  
And you do it again.  
Again, you embed the images.  
Again, you embed the texts.  
And again, you are going to calculate the loss.  
You keep iterating.  
And you are going to jointly learn  
good embeddings for the images and good embeddings  
for the texts.  
Thanks to this, you are now able to really understand  
how an image should correspond to the initial text.  
And now we really have the ability  
to calculate this closeness score, this dot product,  
for every image caption pair in your data set.  
And as I mentioned, you repeat this training mechanism  
on a huge amount of images and texts.  
And thanks to this, you learn all the concepts,  
all the objects.  
And this is why those models are so good.  
They've seen so many images that they're now  
able to leverage that through the training process.  
So now let's investigate how I can leverage this whole pipeline  
and summarize where we are going.  
I now have the ability to compute  
text embeddings and image embeddings that  
correspond to each other.  
That's very valuable.  
And recall the process that we used to have,  
that we have training pairs from a sequence  
of less noisy to noisier versions of the image.  
What can I do now?  
I can actually include the prompt and the text.  
I can maintain the same sequence of images.  
But this time, I also have the corresponding text.  
And this text can be embedded using the CLIP model.  
So it's great.  
I have my whole data set.  
For every noisier version, I still  
maintain the exact same text.  
And this is how you have your denoising neural network.  
It's the exact same process as before.  
You go from noisy to less noisy version.  
But now, on top of having the image,  
you also have access to an embedding of your caption.  
So this is exactly what we got before.  
Noisy, less noisy.  
You take that, and you keep pushing sequentially.  
Now I also add the text.  
So noisy plus text, less noisy version.  
But this less noisy version will now  
be guided by the text, because we know how the text should help  
you designing the image, because we have an understanding of how  
an image should look like to be close to a given text,  
because we calculated this, thanks  
to the previous framework.  
If you're interested, here are more details  
about how those denoising neural networks work.  
This is very complex.  
And I just want to give you a bit of intuition  
of what's happening there.  
As I mentioned, it uses the U-Net architecture  
for denoising purposes.  
You have the CLIP model that is able to embed the texts.  
This is directly integrated into the U-Net using  
attention mechanisms, something we  
covered in a previous lecture.  
So the attention mechanisms are exactly what  
are in transformers.  
And here, it's also involved such  
that you can properly understand how your text should  
guide the whole process.  
Also, you have to understand that operating with pixel space  
is actually very computationally expensive.  
So the diffusion process will actually  
operate in a space called latent space.  
We are not going to operate in a pixel way.  
It's going to be transformed into a representation that's  
more amenable for neural networks.  
We do not understand this space as humans at all.  
This is really something that the model knows for itself.  
This accelerates computations dramatically.  
So this whole process that you are seeing here  
is how those models operate.  
There are so many variations and constant improvement  
for every single one of those components.  
But here, you have now a better intuition of how all of this  
comes together.  
Remember that to get good models,  
you really need to train for such a long time.  
And I just wanted to illustrate in a fun manner  
that if you only train your model for a little bit,  
like one epoch, you just get very simplistic images.  
If you train longer, you start having better shapes and colors  
and details.  
And finally, you get the proud, fierce tiger  
once you've trained your model for a very long time.  
End of transcript. Skip to the start.  
\`\`\`

L4.6 Conclusion and Future Outlook  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So the conclusion-- this  
is what you need to remember out of this lecture.  
Maybe some details were looking too complicated,  
but, really, I want you to understand that the intuition is  
what matters.  
You have a noisy version of the image.  
You have a way to understand the text with respect to an image.  
You are going to use this embedding  
to guide this whole denoising process.  
And it's a sequential process where  
you denoise little bit by little bit  
until you get your final output image.  
And you have so many applications.  
For instance, in arts and entertainment, education,  
you can develop lots of items for games.  
You can restore and enhance photographs.  
In the film industry, obviously, you  
have many opportunities for visual effects.  
You can generate music with diffusion models as well.  
And then for education, you have the opportunity  
to create simulations and also lots of images.  
For instance, I'm creating lots of them for you  
in those lectures.  
It also helps the field of design, manufacturing,  
and architecture.  
For instance, here, I created a van Gogh dress.  
I love van Gogh as an artist.  
And you can leverage his style in so many  
different perspectives.  
So many industries are already adopting those tools.  
It's very helpful to brainstorm or to co-create.  
To illustrate how it can be useful for architecture,  
I generated this video of how my campus of the University  
of Washington in Seattle may look  
like in a futuristic, sustainable future,  
and I used those diffusion models to make it happen.  
If you play the video again and you  
look at the people who were appearing on the video,  
you can notice that those people are actually  
walking on the water or not walking properly.  
This is, again, one of those issues I mentioned.  
Those models generate things that  
look pretty plausible and looking real,  
but sometimes you have things that are not  
corresponding to reality.  
Those models have learned from lots of training data.  
But in the training data, you don't have  
the physics properly encoded.  
You just have words to understand  
how it corresponds to reality and pixels  
to understand how reality may look like.  
You also have many other opportunities  
beyond art and design.  
It can really help, for instance, in health care,  
in medical imaging.  
You can also generate new drugs with those diffusion models,  
new molecules.  
And there is lots of research around this  
for brand-new molecules and drugs  
that could be implemented through a diffusion process that  
will understand how new, different combinations of atoms  
may give you a new drug to solve a problem that you're facing.  
So this is really enhancing the process.  
It's an open, very active area of research right now.  
Here you see the diffusion process  
happening until you get the final molecule.  
And this is impactful for the field.  
And of course, in science, as well,  
it can help with processing astronomical data, climate  
modeling, material science.  
Imagine all those new materials that could be invented.  
This is one of the key ways to tackle climate change, having  
materials that are more sustainable,  
for instance, that could also capture carbon.  
That's a great way of using diffusion models and satellite  
imagery to potentially forecast the weather by imagining  
a foreseeable future like a hurricane,  
like we've seen in the past, or, for instance, a storm.  
Thank you for listening to this lecture.  
I recognize it was a challenging one.  
It was an advanced topic.  
The idea for you is understanding the capabilities  
of such models.  
They're extremely useful to inspire you to try them  
for yourself, developing your own intuition of how diffusion  
models operate, how the way you prompt  
will influence the final image, and really remembering  
that it's a denoising process, and you can  
denoise all sorts of content.  
You can denoise images, sounds, and potentially even molecules.  
I hope that, in the future, you will  
leverage the technology for the better  
and also explore and keep up to date  
about how those models constantly evolve  
and are becoming more and more powerful.  
Good luck in your journey.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
In this lecture, we dove into the mechanics and applications of diffusion models. From random noise to vivid visual outputs, students learned how text prompts are transformed into images through iterative denoising.

Key Takeaways:  
Diffusion models generate images by reversing a noise process, step by step  
Architectures like U-Net and tools like CLIP guide the generation with text conditioning  
Prompt wording, modifiers, and structure have a major effect on image outcomes  
These models power tools like DALL·E, Midjourney, and Stable Diffusion, used across industries  
Congratulations on completing this lecture\! You now have both a conceptual and technical understanding of how cutting-edge generative models turn language into art.  
\`\`\`

Recitation 1: Using Gen AI in Python  
\`\`\`  
Recitation Overview  
Welcome to Recitation 1: Using Gen AI in Python, taught by Lisa Everest, a PhD candidate at MIT's Operations Research Center.

Generative AI can be applied in multiple ways depending on the tools, infrastructure, and user needs. In this recitation, we explore three practical methods for using GenAI: running local models directly on your machine, accessing models through APIs, and interacting with models via web-based platforms. We’ll compare these approaches on dimensions like setup difficulty, scalability, privacy, and cost. Then, we’ll apply each method to core generative tasks—text-to-image, image-to-text, and text-to-text—to see how capabilities differ across platforms. By working through these hands-on examples, you’ll gain a deeper understanding of how to choose the right method for your goals and constraints.

The notebook covered in this recitation can be found here.

If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Lectures covered by this recitation

Lecture 1: AI and the Future of Work  
Lecture 4: Diffusion Models for Text-to-Image Generation  
Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.  
\`\`\`

R1.1 Three Methods for Generative AI  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
LISA EVEREST: Hi, my name is Lisa Everest,  
and I'm a PhD candidate at MIT's Operations Research Center.  
And welcome to Module 12, Recitation 1\.  
Today, we'll be talking about generative AI application.  
So let's go through a little bit of an overview.  
In this recitation, we will learn  
how to use generative AI in Python and through web  
applications.  
Our learning objectives are as follows.  
We will learn three approaches we  
can take to apply generative AI models and the differences  
between these methods.  
We will be able to generate images  
from text through these approaches,  
something called text to image.  
We will be able to generate text from images  
through these approaches, called image to text.  
And we will be able to perform pure text-based tasks  
with these approaches, called text to text.  
Part 1, three approaches for using generative AI  
models and their differences.  
So there are three possible approaches.  
We will first learn three possible approaches  
we can take to apply generative AI models to the problems we  
want to tackle.  
The first approach is local models.  
Local generative AI models are models  
that are run entirely on a user's own machine,  
without requiring internet access or API  
calls to external servers.  
These models are typically downloaded  
from platforms like Hugging Face and loaded using  
libraries such as Transformers.  
Now, don't worry if some of these terms like Hugging Face  
or Transformers sound a little bit new to you  
or maybe you need a reminder.  
I have a glossary at the end of this Colab notebook  
detailing all of the terms you might want to learn more about.  
The second method is API-based models.  
API-based generative AI models are accessed programmatically  
over the internet through an API,  
or an application programming interface.  
These models run on remote servers, usually in the cloud,  
and can generate text, images, audio, or even code in response  
to input sent via structured requests.  
Users don't need to download the model  
or manage infrastructure, just authenticate with an API key  
and send queries.  
This approach allows seamless integration  
into apps, services, and workflows.  
Examples include OpenAI's GPT via the OpenAI API,  
Anthropic's Claude API, and Stability AI's Image Generation  
APIs.  
The third method is web-based models.  
Web-based generative AI models are accessed through a browser  
interface and require no coding or installation.  
These platforms let users interact  
with powerful models in real time  
by entering prompts or uploading files.  
You may already be familiar with ChatGPT, for example.  
The underlying model still runs on cloud infrastructure,  
but the interaction is simplified for general users.  
Tools like ChatGPT from OpenAI, Meta AI's web assistant  
called Claude.AI, and Gemini by Google fall into this category.  
They're ideal for casual use, prototyping,  
and accessibility, often wrapped in user-friendly features  
like memory, file upload, or chat history.  
So what are the differences between these three methods?  
Well, let's learn more about why you  
might want to use one approach over the others.  
So let's compare each of these three methods  
by the need slash use case.  
So starting with internet access slash offline use.  
So local models are fully offline once you download them.  
So you don't need any internet use, which is great,  
when you want to develop an app, for example,  
or even run pipelines on a data system.  
However, API-based models and web-based models  
require the internet.  
In particular, web-based models are browser based,  
so they're always online.  
Next, storage space.  
So while local models are offline,  
this means that they have to be fully downloaded before use.  
This means that they require a sizeable amount of storage.  
On the other hand, because API-based models and web models  
are online, no storage is required.  
That storage is kind done for you  
by the companies that built and create these models.  
Next, high performance or scalability.  
Because of the storage space, limitations of local models,  
you might be limited by local hardware.  
You can only store as big of a model as you have space.  
On the other hand, API-based models  
scale easily with any cloud infrastructure.  
And then, with web-based models, this  
may be limited to the platform itself, its user  
experience or UI, and any session limits you might have.  
Next, data privacy or sensitive information.  
Now, local models, as they are on your own machine,  
is great for dealing with sensitive data or private data.  
The data stays on your machine.  
It doesn't get sent anywhere or to anyone.  
However, on the other hand, for API-based models  
and for web-based models, this may be different.  
In particular, for web-based models,  
your data has to be sent to whatever  
platform is hosting the model.  
So it's not safe for sensitive information.  
With API-based models, this does vary by provider,  
but typically with especially sensitive information  
like medical data, it is not great practice  
to be using API-based models.  
Next, ease of setup slash if you need code or not.  
So let's start with, actually, the web-based models.  
It is the easiest.  
You just open it in a browser.  
You interact with it kind of face to face.  
And no coding is required.  
In the middle here, we have API-based models,  
where you need some coding, but it's generally  
easy for developers to use.  
You simply know the structure of your query for the API,  
and you'll receive a response.  
Finally, the most difficult is local models.  
You have to load the model yourself,  
technically set it up, load it in,  
submit any requests in there.  
The coding is more complicated.  
However, you will find in this recitation  
that you'll be able to load it yourself.  
The next is integration into custom apps or workflows.  
With local-based models and API-based models,  
it's both flexible and has easy integration to apps.  
However, with web-based models, because you  
have that user interface like a website,  
you can't really integrate it into your own application.  
What about cost after setup?  
So local-based models are free after downloading,  
so that's no cost.  
However, with API-based models and web-based models,  
it's sometimes free, sometimes not.  
It depends on if the company has free tier, paid tiers.  
It depends on how advanced the model is, as well.  
So this sometimes has a cost, sometimes may not have a cost.  
As well as access-- so let's talk about access  
to the latest models or some automatic updates.  
So local models exist on your local machine.  
That means that if you want to update the model to whatever  
is most recent, you have to actually manually update it  
and redownload the latest model.  
On the other hand, with API-based models,  
it's typically the latest version, but not  
necessarily latest model.  
So what do I mean by version and model?  
Let's take GPT-3 and GPT-4.  
Those are, I would say, distinct models or--  
yeah, distinct models of GPT.  
GPT-3 might have some updates made  
by the OpenAI company and maybe some small bug fixes,  
but no fundamental changes, whereas GPT-4  
is fundamentally different from GPT-3.  
So when you use GPT-3, you'll be using  
the latest version, but not necessarily the latest  
model of GPT-4.  
And finally, with web-based models,  
typically it is automatically updated to the latest model.  
So when you go into ChatGPT, it automatically  
will use the latest version of ChatGPT.  
Next is whether it's good for beginners or casual users.  
So as you may guess, the web-based models  
are quite intuitive.  
You have a website.  
You chat with it.  
It's very intuitive to use.  
However, API-based models and local models,  
especially because they require coding  
and some technical experience, it may not be beginner friendly.  
Finally, for research, fine tuning, and experimentation,  
local models are great.  
You have the full model access because the entire model  
is downloaded on your machine.  
On the other hand, API-based models  
have a limited use case for research and fine tuning,  
and for web-based models, it's usually not supported.  
End of transcript. Skip to the start.  
\`\`\`

R1.2 Text to Image  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now that we've learned about these three  
methods for generative AI, let's dive  
into text-to-image, which is generating images  
from text using each of the three methods.  
We will first use a local Stable Diffusion model.  
Recall that you have learned about Stable Diffusion models  
in this module's lectures.  
So as usual, we will need to first install any required  
libraries into the environment and also import  
the required libraries.  
Note that I've already run this installation cell and also  
this importing cell, because it takes some time  
to install and import.  
So now we will locally load the pre-trained Stable Diffusion  
model from Hugging Face.  
For more information on this model,  
you can find the Hugging Face documentation here.  
So this means the model itself is now  
located locally onto this notebook's GPU, not via an API.  
So the first time you run the code below,  
it will download the model from the Hugging Face hub, which  
is about a 4 gigabyte model.  
Now, note that you'll see some output already from here,  
because I've pre-run this cell to load the model,  
as it takes some time, again, to load this model.  
You can see, for example, this step is around four minutes.  
So it takes some time to load these models because they're not  
necessarily small.  
So the ID of our model is called runwayml-stable-diffusion-v1-5.  
And we load it from Hugging Face using this ID and the Stable  
Diffusion pipeline.  
So this is a function, the from\_pretrained,  
that does the model loading.  
And we have the input of that model ID.  
We also specify a few other parameters.  
We specify the torch\_dtype and we set it  
to torch.float16, which tells the model  
to use half precision, float16, instead  
of full precision, float32.  
We use this because float16 uses half the memory  
and speeds up inference, which is important on Colab's limited  
GPUs.  
Note this requires GPU that supports float16 operations,  
and usually Colab provides this.  
We also use the parameter use\_safetensors as true  
because this enables loading the model from dot safetensors  
files instead of dot bin files.  
We use this because dot safetensors format  
is faster, safer, and non-executable,  
which mitigates security risks.  
It is also more compatible with float16 pipelines and Hugging  
Face's optimized loading.  
So though in this case we have loaded the RunwayML model,  
you can also load other text-to-image models  
by changing this model ID variable.  
So some examples include our classic Stable Diffusion model  
here.  
But you can also load Stability AI's Stable Diffusion model  
or another model from Nitrosocke which is called mo-di-diffusion.  
You can see that each of these models specialize in different  
things, such as high resolution or 3D models.  
So we've loaded our model.  
So we can now give our Stable Diffusion model a prompt.  
And using the pipe object from above--  
so we'll call this pipe object--  
we will ask the model to generate  
an image from the prompt.  
And using the plt or plot library,  
we display the image we just generated.  
So let's just run this real quick.  
While it's running, we'll just say that,  
note that we have this axis off just to remove  
any axis from the display, so that our display is prettier.  
So it's generating.  
And here we go.  
Isn't our image cool?  
So you can feel free to play around with these models  
and generate more images from text, use  
different prompts, et cetera.  
So we've prompted a serene mountain lake at sunrise  
with mist and pine trees, so it seems pretty accurate.  
So let's use our second approach for the text-to-image task.  
Our second approach, recall, is this API approach.  
We will use a diffusion model from the company Stability AI.  
So we first need to install the Python client that  
will allow us to interact with stability AI's API service  
and also import all relevant packages.  
Again, I've already installed it and I've  
already imported the packages just to save some time.  
Note that we have a small error/warning here.  
This does not affect our code in this case.  
So let's actually set the API key.  
So we need to tell the API service what our API key is.  
This getpass function right here will  
allow me to input my API key while keeping  
it private or invisible to public view.  
So your API key is something for your eyes only.  
It is a unique key for your own purposes.  
So let's run this quickly.  
So I've inputted the Stability AI API key that I have.  
And that's now registered by the API.  
So just a quick note that if you would  
like to run this code on your own,  
you have to generate your own API key,  
since it's unique for each person, as I mentioned.  
You can do this by following these steps.  
So you can create a free account at Stability AI's website.  
Let's go to the website.  
You'll go to your account here.  
So I'm already logged in.  
You need to create an account, if you don't have one already.  
Go to API Keys and click on this, Create API Key.  
And we have this unique API key here,  
which you can copy to your clipboard  
and then save it to use as an API key in this code.  
Let me delete the one I just made.  
Great.  
OK, so now this following code will actually  
generate the image.  
Let's go through each line of code block-by-block.  
So this first block creates and configures the API client.  
The API client is a piece of software, usually a library  
or object in your code.  
So we kept it as Stability API as the object.  
And it lets you easily interact with an API  
by handling the communication for you.  
We set the following parameters for our API client.  
We have the key, which is that Stability AI API  
key that I just talked about.  
And then we have the engine.  
So this engine is the name of the model you want to use--  
in this case, Stable Diffusion XL 1024 V1.0.  
You can also choose other models in this case.  
This model determines image quality, size,  
and model architecture.  
The second block of code prepares the details  
of our request, which we specify via the following API client's  
parameters in this generate function.  
So the parameters are the prompt,  
which is the text description of the image you want to generate.  
In this case, I put the exact same text  
prompt as we had before.  
Note that it must be a string.  
We also have the steps.  
This is the number of diffusion steps,  
for example 20 through 50\.  
Note that higher values produce more detailed and refined  
images, but take longer.  
Then we have the CFG scale, which  
is the Classifier-Free Guidance scale, which  
controls how closely the image matches the prompt.  
Note that lower values is more creative, divergent.  
Higher is more literal.  
A common range is 6 to 9\.  
The width and height control the width and height, respectively,  
of the output image in pixels.  
So this is 512 pixels width, 512 pixels height.  
Note that it must match the supported sizes of the engine.  
So in particular, this specific model supports output images  
with a 512-by-512 pixel size.  
Finally, samples is the number of images to generate  
for this prompt in one call.  
This is typically set to 1 through 4\.  
And then the answers variable will store the generated image  
response from the API client.  
Finally, the third block of code actually  
displays the generated image.  
More specifically, it loops through the API responses,  
since there may be more than one.  
It finds the image data in the response  
and then converts it into a displayable image object,  
because it needs to convert from bytes into a file-like object  
so that we can ultimately display it.  
So let's run the code.  
And we can see that we do, again,  
have a serene mountain lake at sunrise  
with mist and pine trees.  
But as you can clearly tell, our image  
looks quite different from the local model.  
So we have this one from the API-based model.  
And from our local model, we had this image.  
Which one do you like better?  
All right.  
Last but not least, for this text-to-image section,  
we will explore how to use web-based models  
to generate images.  
In particular, we will see how we can interact with ChatGPT.  
We can ask ChatGPT directly to generate  
an image using a specific prompt and it  
will return back an image.  
So let's see how it looks if we use the same mountain-related  
prompt as previously.  
So for example, we can say, generate an image  
using the following prompt--  
a serene mountain lake at sunrise  
with mist and pine trees.  
Let's actually do it.  
So let's go to ChatGPT.  
And I will say--  
let me copy the prompt.  
Generate.  
Generate an image using the following prompt.  
And hit Enter.  
So it's getting started.  
It's generating.  
Now, I won't let it finish, because it takes quite a while  
for it to generate.  
But the result from one of my other tests  
was this image, which again, is different from the other two  
models' images.  
Now, if you're curious, you can also  
ask ChatGPT what model generated the image and also  
other text-to-image models that you might want to use.  
So I asked it which model generated this image  
and what other models are there.  
So in particular, the one that I requested from ChatGPT  
was generated by OpenAI's DALL-E model,  
which you may have heard of.  
Specifically, the version is DALL-E 3,  
which is integrated already into ChatGPT.  
It produces high quality, coherent, and realistic images  
from text prompts.  
And then ChatGPT has listed out nicely for me  
several other text-to-image models that we could use.  
End of transcript. Skip to the start.  
\`\`\`

R1.3 Image to Text  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Our next set of tasks that I want to explore  
is image to text.  
So we just learned how to generate images from text.  
Now let's go the opposite direction  
and generate text from images.  
We discuss some of the most common use cases of image  
to text below.  
So there is quite a few set of tasks here.  
We have summarization or image summarization.  
The goal is to create a concise textual summary  
of the overall scene or content in an image.  
For example, the input is a photo of people dining out  
at a restaurant.  
The output of this task might be a group of friends enjoying  
a meal at a sidewalk cafe.  
Common uses are in news, photojournalism, image databases  
for tagging purposes.  
Another use case is visual question answering.  
The goal is to answer a natural language  
question based on the visual content of an image.  
For example, let's say the image is a man holding a tennis racket  
and you ask the model, what sport is being played?  
The answer, ideally, should be tennis.  
Some common uses are AI assistants  
and multimodal chatbots like GPT.  
The third use case is image-based reasoning  
or inference.  
The goal is to make logical or common-sense inferences  
from visual input.  
For example, an image could be an umbrella on wet pavement.  
If you ask it to give an inference on what  
may have just happened, hopefully the output  
is it recently rained.  
Some common uses are story understanding, decision support  
systems, and also multimodal large language models.  
The fourth set of tasks is keyword or tag generation.  
The goal is to extract descriptive keywords or tags  
from the image.  
An example output of an image could be sunset, mountains,  
reflection, lake.  
This actually is probably a good set of tags for our image  
from before.  
Some common uses are image search and content  
categorization.  
The fifth set of tasks is OCR and captioning.  
In other words, document understanding.  
The goal is to read and describe the content of image  
with embedded text.  
For example, an output could be a login page with fields  
for username and password.  
Some common uses are business workflows, scan documents,  
and ID verification.  
Finally, there is multimodal prompting/input for other tasks.  
The goal is to use image to text output as input  
to another task--  
for example, translation, summarization or Q\&A.  
An example workflow could be you input an image,  
you get a caption.  
You translate this caption to French  
and use this in a chatbot.  
Common uses are multilingual applications,  
instruction-following agents.  
In this part of the recitation, we  
will focus on the image summarization task.  
In other words, this first task.  
So like before, we'll start with the local model approach.  
We will use the B-L-I-P or BLIP, Bootstrap Language Image  
pretraining model from Hugging Face,  
which is one of the most reliable models for this task.  
We will first install our required packages  
and import the dependencies, which I've done  
so already to save some time.  
Next, we will load our image locally  
into this notebook where we uploaded  
the image into the colab files.  
In this case, let's save our image into our file path.  
So here let's check our files, make sure that it's there.  
So let me upload our appropriate image.  
Then, now that I've uploaded into the colab environment,  
let's actually load it into the notebook.  
Great.  
So now we need to load the BLIP model  
by loading both its processor and the model itself.  
So here, the processor is a preprocessing and postprocessing  
tool.  
You can think of it as a wrapper that  
prepares the input for the model and interprets its output.  
For BLIP and similar vision models,  
it preprocesses the images--  
for example resize, normalize, and convert to tensors.  
So for appropriate input into these models.  
If needed, it also will tokenize some text  
if there's input generation, and also, it  
will decode the model output into human readable text.  
The model is the neural network itself  
that is doing the inference.  
It contains the actual layers, like the encoder and decoder  
layers.  
In the case of BLIP and similar vision models,  
it is responsible for encoding visual features  
and generating language tokens.  
So this code actually loads the BLIP model and the BLIP  
processor, which I've already run this code  
and loaded the models into our notebook  
for some saving of time.  
OK, so let's actually generate some text from our image.  
The code below performs the actual text generation  
from the image.  
Let's go through the code block by block.  
The first block of code uses the processor  
to preprocess the image into model ready tensors.  
This involves resizing and normalizing the image,  
converting it into a PyTorch tensor, which is this return  
tensors argument, and moving the tensor to the same device, CPU  
or GPU--  
in our case, GPU--  
as the model is using, using two BLIP model dot device.  
This is important because the model  
expects a tensor with the right shape, data type, and device.  
This line prepares the input correctly.  
The second block of code runs the model decoder  
to generate a caption by using the process image as input--  
so here's our input--  
and limiting the generated caption to 50 tokens,  
with max length of 50\.  
Note that this is the actual caption generation step.  
It outputs a sequence of token IDs  
representing the predicted text and saves it  
into the variable output.  
The final block of code takes the generated token IDs, output,  
and converts them back into human readable text.  
The parameter skip special tokens equals true  
removes any special tokens.  
This effectively transforms the raw model output token IDs  
into a clean caption you can read and understand.  
This then gets printed out for display in the notebook.  
So we have run it here.  
And after running the code, we have the summary of the image  
is a dog sitting on top of a mountain,  
and we can recall what our image looked like.  
And in fact, it looks like a dog sitting on a mountain.  
So it's a short and simple caption, but accurate.  
Now, I tried to find a free API-based model for image  
to text, but if you recall that pro-cons chart write,  
sometimes API-based models may not be free.  
So we will skip the API-based model for this set of tasks,  
and we will next show how we can generate text from image using  
the web-based model ChatGPT.  
So using the same image, we can ask  
ChatGPT to summarize the image.  
So let's do it ourselves.  
ChatGPT, please summarize what's going on in this image.  
And let's upload the picture.  
Upload.  
We'll take a second to process, and it's  
given us quite a descriptive description.  
A golden brown dog stands on a rocky outcrop.  
Et cetera.  
Et cetera.  
Let's see if I want a simpler one.  
Please summarize in one sentence.  
So, because ChatGPT is a more complicated, complex model,  
it gives us a very nice description  
of what's going on in this picture as  
compared to this very simple summary.  
Now, we can also ask what model it used to summarize the image  
and ask about other image to text models that are available.  
In this case, it used GPT 4.0, which  
has strong vision capabilities and allows  
it to understand and describe images in natural language.  
Other models include BLIP, which is what we just used;  
OFA, which is one for all for Microsoft;  
and GIT, Generative Image to Text Transformer.  
End of transcript. Skip to the start.  
\`\`\`

R1.4 Text to Text  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Our last set of tasks is text-to-text.  
More specifically, text-to-text models take one text input  
and generate another text output.  
These tasks are central to Natural Language Processing,  
or NLP, and cover a wide range of applications,  
which we'll discuss now.  
The first set of applications is translation.  
The task is to translate text from one language to another.  
The input may be to translate English to French.  
The cat is sleeping.  
The output is something that I don't know how to pronounce.  
\[FRENCH\] maybe.  
Sorry for those French that are watching this video.  
The second set of task is summarization.  
The task is to generate a concise summary of a longer  
text.  
Input, summarize-- the company reported record earnings  
this quarter.  
I'm imagining a long paragraph here.  
And the output could be, the company had record earnings.  
The third set of tasks is sentence completion,  
the task being to predict or complete  
the next part of the sentence.  
Maybe the input is, she walked into the room and saw.  
And then the model would finish the sentence and output,  
a group of people waiting to surprise her.  
The fourth set of tasks is question answering.  
The task is to answer a question based on context  
or general knowledge.  
For example, the input could be, what is the capital of Japan?  
And the output is hopefully Tokyo.  
The fifth set of tasks would be paraphrasing.  
For example, you could ask a model  
to rewrite a sentence with different words but having  
the same meaning.  
The input would be paraphrase, he is very intelligent.  
Output, he is highly smart.  
The sixth set of tasks is grammar correction.  
The task is to fix grammatical mistakes in a sentence.  
For example, the input could be fix grammar--  
she no went to school.  
Output, she did not go to school.  
The seventh set of tasks is text classification  
as text generation.  
The task is to predict a label or category in text form.  
For example, classify the sentiment, I love this movie.  
The output would be, positive.  
The eighth set of tasks is dialogue and chat box.  
So the task would be to generate conversational responses.  
For example, as input, it would say user, what's your name?  
And then this backslash n is next line,  
prompting the model as AI and asking what would it say.  
The output would be, I'm your AI assistant, how can I help you?  
The ninth set of tasks is instruction following.  
For example, the task would be to perform  
a task based on a natural language instruction.  
The input could be write a tweet about climate change.  
The output would be climate change is real and urgent.  
Let's act now.  
\# Emoji fire sign, world emoji, hashtag \#ClimateAction.  
So kind of tweet-like.  
The last set of tasks is text simplification.  
And the task is to rewrite text to make it easier to understand.  
Input, simplify-- photosynthesis is the process  
by which green plants and some other organisms  
use sunlight to synthesize foods from carbon dioxide and water.  
Long sentence, right?  
So the output could be, photosynthesis is how plants  
make food using sunlight.  
So as you can see, this world of NLP text-to-text is quite huge.  
And there's a lot of work being done in each of these tasks.  
For our discussion and learning, we  
will focus on sentence completion and summarization.  
So let's start with using the first approach, local models.  
We will use a few models to showcase  
how the responses differ, including GPT-2  
and Google's Pegasus model.  
We will first install and import the required libraries, as  
always.  
Here I've pre-installed the required library  
and also pre-imported the libraries  
in order to save some time.  
Next, we will create a text generation  
pipeline using the GPT-2 model.  
Pipeline is a high-level Hugging Face  
function that loads models and tokenizers behind the scenes.  
The argument text generation specifies the task.  
Here, we want to generate text continuations.  
The argument model equals GPT-2 tells the pipeline  
to use OpenAI's GPT-2, a pre-trained language model.  
This code block therefore results  
in the generator object, which can auto complete or continue  
a given prompt.  
The below code block right here actually generates the text  
from GPT-2.  
Let's go through it block-by-block.  
So the first code block defines the text  
prompt we want to give to GPT-2, in this case, a sentence  
about the MIT Sloan School of Management  
that we want the model to finish.  
So we want the model to finish the sentence for us,  
since it's unfinished sentence.  
This next line then calls the GPT-2 generator  
with the provided prompt and generation settings.  
The following parameters are used.  
We give it the text prompt, which is the starting input  
to complete.  
We specify that the max length is  
30, which limits the total number of tokens  
in the generated output-- kind of how long the output is.  
And then the number of return sequences  
is 1, so we ask it only to return one generated result.  
The final line of code will simply  
print the generated result from GPT-2.  
Let's run this and see what happens.  
It's giving us just some reminders.  
So it's given us quite a long response now.  
So as you can see, the initial text prompt is here.  
So we can see this here.  
The mission of the MIT Sloan School of Management  
is to develop principled, innovative leaders who--  
yeah?  
And then it finishes.  
Can work to transform the culture of the business world  
in the 21st century in a way that makes it possible  
for businesses to succeed in the 21st century.  
And it keeps going.  
But this is a quite, I guess, accurate mission, maybe,  
that it's learned from how the model has been trained.  
We can also perform a summarization task in this way.  
So previously was text finishing or continuation.  
And let's also look at summarization.  
So we can create another pipeline object.  
But this time, instead of using--  
let's see.  
Instead of using text generation as the task,  
we will use summarization as a task.  
And this will tell the pipeline we  
want to perform the summarization task.  
Note that here, I did not specify a model,  
which means that it's going to default to the model  
sshleifer/distilbart-cnn-12-6, is a small, simple model.  
Now, I'll let you know how I knew that it defaulted to this.  
But for now, we will create this default summarization pipeline.  
So now the pipeline has been loaded.  
It's been a few minutes.  
Next, let's define the text that we want to summarize.  
We will store this text in the variable article.  
So here's our text.  
And it's an interesting piece of text.  
The only thing crazier than a guy in snowbound Massachusetts  
boxing up the powdery white stuff and offering for sale  
online, people are actually buying it.  
So someone is selling snow for some reason.  
Now, similar to before, with our text continuation task,  
we will generate and then print the summarization  
from our model output.  
This time, we will allow our model  
to return a response of at most 50 tokens.  
So we take our default summarizer  
that we created before, we input the article,  
we give it a max length of 50, a min  
length of output response of 30, and only request  
to return one answer.  
And then we will print the result. So let's see.  
The article is not defined.  
Run this article and then run this.  
So for $89, you can buy 6 pounds of snow  
in an insulated Styrofoam box for $19.99.  
The website says it has filled more than 133 orders this week  
alone.  
Pretty good summary.  
I would say, yeah, for $89 you can sell.  
Yes.  
Then $19.99 is the box.  
So it's a little bit off with how the text is, but the text  
itself is kind of quirky.  
So we'll roll with it.  
Now, summarization overall, though, I  
wouldn't say it's necessarily top tier.  
So let's try a different model.  
This time, let's try using Google's Pegasus  
model for summarization.  
You can also try changing it to other models  
if you would like to experiment further.  
So as before, we will do the same steps.  
We will create our Pegasus summarizer object  
using the pipeline function, telling  
it to perform summarization.  
And the model has this ID google/pegasus-xsum.  
I have loaded it beforehand just to save some time.  
We can take the same code and ask for some results.  
And it will say, it's the stuff of dreams for many--  
snow that can be shipped to your front door for as little as $89,  
or more if you live in colder states.  
So you can tell that it's kind of in some ways  
a better response.  
I think it's more accurate.  
But it's also got a lot more personality in this response.  
So it's quite interesting to see how different models produce  
different results.  
So when thinking about your task,  
it's important, therefore, to think about which model  
you want to use depending on which task you're doing.  
So next, let's use an API-based model  
to perform text summarization on our snow article.  
We will first need to import the necessary libraries.  
So here we do this.  
And then we will set our API token, endpoint, and headers.  
So let's see.  
We set our API token, like our previous example  
of using an API-based model with text-to-image tasks,  
and we also defined the endpoint like a URL  
for the summarization model.  
We will use Facebook's BART model for this.  
So let me just run this.  
And let me run this first as well.  
So we have our token, or API key set.  
So I input my token here and accept it.  
So let me just talk briefly about these headers  
and what I mean by endpoint.  
So the endpoint is the URL of our API.  
So it's kind of like where we make our request to.  
The headers are special lines or sections  
that indicate structure, context, or metadata.  
These are useful for our API-based models  
and they help with the requests and responses.  
So this is setting the API token here  
and then setting the endpoint here  
and setting the headers here.  
OK.  
Moving on, the below code makes the actual request  
to the API-based model using that API endpoint we defined.  
So here are the requests.  
We are going to send the request with a POST function.  
And we use the API endpoint we defined.  
We use the headers we defined, as well as the snow article  
that we defined previously.  
And this will make the request and save the response  
into the variable, respond.  
Then this line extracts the actual text  
from the API's response and prints it.  
So let's see.  
So it gives us a longer response.  
And it says, for $89, you can buy 6 pounds of Boston-area snow  
in an insulated Styrofoam box.  
With more than 45 inches of snow,  
Boston set a record for the snowiest month in its history.  
The website and social media accounts  
claim to have filled more than 133 orders Tuesday.  
I kind think this has been the best summary so far.  
It's the most accurate, maybe, and more technical, and a more  
standard answer compared to Google's Pegasus model, which  
had a bit more flavor to it, maybe.  
So finally, we will discuss text-to-text  
using the web-based model ChatGPT.  
Essentially, anything you do with ChatGPT  
is text-to-text, as it is a conversation-based application.  
Anything related to images, videos, or audio,  
though, just keep in mind, would not  
be included in these text-to-text tasks.  
So just for ease of this recitation,  
let's just see via this screenshot what ChatGPT does  
with our snow-related text.  
I'll make it a bit bigger.  
So I asked it to summarize the following text, which  
I pasted in here.  
And it gives us a summary that's almost as long  
as the original text itself.  
So I asked to limit the summary to 50 tokens, which  
it understands, and it gives us a more concise response.  
And this one is, I would say, also the best so far.  
So with each model, we've gotten a little bit better  
with our summarization.  
So congratulations, this concludes recitation one  
of module 12\.  
And again, just as a reminder, we  
have a glossary of terms of anything  
you might find you want to look up here.  
Thank you.  
End of transcript. Skip to the start.  
\`\`\`

Recitation Summary  
\`\`\`  
In this recitation, we explored three main methods for applying generative AI—local models, API-based services, and web-based platforms. We compared their strengths and limitations, from offline privacy to cloud scalability. We then applied each method to core tasks: generating images from text, creating text from images, and transforming text with text-to-text models.

Key takeaways:  
Local models offer privacy and full control but require storage, setup, and strong hardware.  
API-based models provide scalability and integration but may raise privacy and cost concerns.  
Web-based models are the easiest to use but limited in customization and integration.  
Core GenAI tasks—text-to-image, image-to-text, and text-to-text—are accessible through all three methods, though results and usability differ.  
Congratulations on completing this recitation\! You’ve gained hands-on experience with three distinct ways of applying GenAI and learned how to select the right approach depending on your context.  
\`\`\`

Recitation 2: Explorations in Gen AI  
\`\`\`  
Recitation Overview  
Welcome to Recitation 2: Explorations in Gen AI, taught by Professor Léonard Boussioux, Assistant Professor of Information Systems at the University of Washington.

Generative AI is not only about producing outputs—it is about blending human creativity with powerful tools to achieve meaningful results. In this recitation, we dive into real-world creative workflows where AI is used as a collaborator in design, art, and software building. You’ll see how diffusion models supported the design of the MIT Generative AI Conference logo and tote bag, and how multiple AI tools can be orchestrated together to create a website with images, animations, and even video content. By examining these case studies, you’ll gain insight into the challenges, iterations, and opportunities that emerge when humans and AI work side by side.

Lectures covered in this recitation

Lecture 2: Gen AI and Creative Problem Solving  
Lecture 4: Diffusion Models for Text-to-Image Generation  
\`\`\`

R2.1 Website Creation Demo  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now it's time for a fun story.  
We covered diffusion models.  
And I want to illustrate how I've used them for a real world  
situation as an artist.  
And what you're seeing now is the logo  
I created for the Generative AI Conference at MIT in 2023,  
one of the first conferences ever reuniting so many people  
around generative AI.  
And I was the one creating the logo for them.  
And let's look into how this happened.  
So this is the event.  
Lots of people attended, hundreds of people,  
and also online as well.  
My goal was to create a logo and merch for all the attendees.  
And it was such an amazing opportunity  
that also opened a door for me afterwards  
to present at TEDx MIT about let art be your superpower.  
I consider myself an artist.  
And I also consider that everyone can be an artist.  
And I really insist on this.  
And AI is also one possible tool to help you  
being the best artist you want.  
And I keep presenting a lot around my artworks.  
You will recognize here that I've presented  
you this in some lectures.  
I love also projecting that in large walls  
and explaining to people both the artistic part  
but also the technical part.  
I believe art can bring more people together and spread  
messages in a very different way.  
So the idea is let's take a few minutes to look  
into how I created logos and merch for the conference  
as my mission.  
And I use diffusion models for this.  
The whole process may look wild because I  
combined so many techniques.  
I did not always know if it was the right way of doing it,  
but it was a whole artistic workflow.  
And I want to bring you along in my journey.  
Let's start.  
\[MUSIC PLAYING\]  
The story started when one of my students of my deep learning  
course told me, hey Leo, I remember you told us in class  
you're doing a lot of AI art.  
Could you help us design a graphic for a cool conference  
we are organizing?  
And I said, yeah, of course.  
I'm excited.  
And she told me we would like it to be  
MIT related with an AI vibe, or neural network, or brain.  
But we trust you.  
Anything is fine.  
It just has to be cool.  
So I thought, wow, that's the first commission I ever  
received.  
I had just told my students, 2023  
is the year where I will kickstart my AI artist career.  
And here was my first opportunity.  
So I decided, OK, let's do something really cool for that.  
So I started my inspiration by looking online through pictures  
of MIT and also of AI.  
Of course I know and I have this in my mind.  
But I just wanted to have lots of inspiration  
and see overall how those ideas would combine.  
And I thought, OK, it is time now  
to start creating images with those image generative models.  
And I tried this with Midjourney,  
which was my favorite model.  
It hosted on the platform Discord,  
and you can type a prompt and get some results.  
Remember this is 2023\.  
The models were not as good as they are today.  
And I first started with a prompt that looked promising--  
"MIT in Boston shaped like a neural network AI neurons."  
That's kind of ambitious.  
I really already put the concept of MIT, neurons,  
and then I got this.  
If you know Boston, you may see a bit of the shape of Boston  
but it's not very obvious.  
And the pictures don't look that great, to be honest.  
So I tried the same thing in DALL-E, which  
is another model from OpenAI.  
And this time, honestly, it was too bad.  
I had overall a neural network.  
In one of them, I had the dome but nothing like MIT.  
It was very disappointing.  
And I realized this DALL-E model won't be the one helping me  
this time.  
And in fact, I wondered MIT is a concept that those models maybe  
they don't know.  
And I typed just MIT and this is what I got.  
As you can see, OpenAI had a brief idea of that campus  
at MIT.  
And Midjourney had simply absolutely no idea.  
It just put some random buildings and does not know  
at all how it's shaped, which means I cannot prompt the models  
with MIT to get an MIT dome at any time because the model just  
don't know how it looks like.  
So I have to find another way.  
So I decided to branch out and look for other ideas.  
So I just thought, OK, let's look at the incarnation of AI  
into a student, Boston shaped like a neural network,  
realistic design futuristic.  
And I got some scary faces with some awkward neurons  
and cyborgs.  
I also tried to vary the adjectives.  
And it always looked bad and way too scary.  
Notice that when I write a prompt,  
I include different parts.  
I include overall what I want.  
I include some context about the background and some adjectives  
to qualify how I want the overall vibe of the picture  
to be.  
So I kept my exploration going.  
I thought, let's get something a bit more cute.  
So I asked for a robot holding an AI brain in the hand.  
It did not work that well.  
Again, it's not that nice.  
I want a design that will appeal to people.  
And I thought that by including something the most  
beautiful and cute, I would get something fantastic.  
And indeed, it was kind of cute.  
But I thought, after all, we are MIT.  
It's serious.  
We have so many people from all over the world who will come.  
Is it the energy we want to give just a cute little robot?  
I think we need another type of ambience in the picture.  
So I kept my exploration going.  
I looked for other styles like watercolor or 3D style design.  
It looked interesting but I did not  
have any emotional connection with the content.  
It just looked nice.  
I don't want something to just look nice.  
I want my public to feel an emotion,  
to remember something when I see my picture.  
So I had to move on from that.  
And then because I was talking about emotions,  
I just asked Midjourney to give me emotions  
with love, or self-introspection,  
or observing and feeling enriched.  
And I got those images.  
They started looking great.  
But again, it looks very design but it does not  
connect with what makes us MIT.  
It did not connect with who we are on campus and what we do.  
So I had to move on.  
And I thought, let's try something fun  
and let's try some gimmicks.  
For instance, Mona Lisa and a robot and maybe gods and a human  
touching the fingers with each other  
and replacing God with an AI potentially.  
It looked great, but I also knew that this  
was limited by the abilities of the current models.  
I was expecting that, in a few years,  
I may get some beautiful, groundbreaking pictures.  
It was just fun here.  
And since I was very limited on time,  
like I had a very short deadline,  
I knew it's too complex to get something  
satisfying I can just put all over the internet and campus.  
So again, I moved on.  
I was a bit desperate.  
I tried other things.  
It looked so scary.  
I don't like this at all.  
And then I was really desperate.  
And I thought, you know what, with everything I generated,  
this image of Boston and a neural network  
that spreads was maybe my favorite  
because it does look like a bit like Boston  
with the Charles River.  
And then you have the building.  
And you do have a neural network.  
But honestly, it was still scary and looked like Stranger Things.  
I was unsatisfied.  
And I thought, let's move on from just using purely  
the diffusion models and let's use Photoshop to merge the two  
images together and bring back MIT because, so far, my MIT  
dome is nowhere to be seen.  
So I tried very quickly to make this happen.  
And it felt incredibly scary.  
Oh no, I absolutely don't want to see this feeling of an AI  
crawling or something strange saying,  
oh no, I need to move on from that.  
And at that point, I had no idea where to proceed.  
And I thought, what I really want is a shape of MIT.  
And I feel if I could just start with how MIT actually is and I  
just apply a bit of a different style, it would work.  
So I read online.  
And I discovered that, in fact, Midjourney  
has the ability to upload a picture  
and ask to see this picture under a different way.  
And I thought, oh my God, I'm back in business.  
I can take this beautiful picture  
and ask the model to make it as futuristic, cyberpunk, modern,  
exciting, smart city.  
Those words were precisely chosen.  
I knew that cyberpunk always gives something fun and fancy.  
And I knew that by putting modern,  
I would get something that would project MIT in the future.  
By putting exciting, I add a bit of an energy  
because the model has learned through all its training  
that when something is exciting, it  
has a specific style and vibe.  
And I was blown away.  
I got so many incredible images.  
And I felt, wow, it's looking much more like MIT.  
I have this futuristic feeling.  
It looks modern and cool.  
And in fact, I kept generating so many images  
I didn't realize the very first one I got  
was actually my favorite.  
I absolutely can recognize the dome of MIT.  
It's now shaped like a spaceship.  
I can see a drone in the air and Boston in the background, even  
the Prudential Center, and the city looking  
like it's in the next century.  
I was so delighted.  
And it turns out that was my final picture  
I gave to the organizers of the conference.  
They printed this everywhere.  
And then everybody was actually really liking the picture.  
The picture got a lot of success.  
And quickly, two of our organizers of the conference  
came back to me and said, oh my God, we love the poster.  
In fact, we are thinking of using one of your designs  
as a tote bag.  
We just got some funds.  
And every attendee will receive a tote bag.  
Could you design some other cool thing  
so that we can print it on the tote bag?  
However, the only thing is we need it by tonight.  
So \[GASP\] it's 5:00 PM already.  
You need this by tonight?  
I have lots of work today.  
I am about to prepare a recitation for my students  
at MIT.  
And I felt but it's so cool, in fact,  
that my art will be printed and given to everyone.  
So I said, OK, I'll do it but I think that will be all right  
because, in fact, if I type on Midjourney tote bag, and mind,  
and face, it works.  
I already have some cool designs.  
And I felt, OK, I have this under control.  
I should be able to do it.  
And then you can get some AI.  
It looks super cool.  
So I felt I think I'll have great ideas.  
However, they just told me quickly  
after that it's looking good, but could you  
make it quite simple with a generative vibe  
and, if possible, featuring MIT, and also the manufacturer  
only allows for six colors and a format of 12 by 13 inches.  
That's already much harder than I thought.  
And there are more things to think about.  
But I felt I'll make it happen.  
And this time I had my experience  
from the previous picture I generated.  
So I felt I will immediately start with the MIT dome.  
I took this picture.  
And I started at 10:00 PM.  
I was exhausted.  
So you know when you haven't started your job, it's 10:00 PM,  
you just ask ChatGPT for help.  
So I asked ChatGPT, hey, this is a bit what I want.  
Just give me ideas for prompts of how I can transform my image.  
I literally copy-pasted those prompts.  
And this is what I started getting.  
That looked pretty all right.  
It was looking like a futuristic version.  
I ask only with six colors, neural network pattern.  
That was all right, nothing special,  
but things were still under control.  
And I started going wild.  
I started to put faces to try other colors.  
And I started to have ideas.  
But none of them were really that catchy.  
It just looked nice.  
And nice is not enough once again.  
And I thought, OK, I'm going to create lots of variations.  
I think it's getting there.  
Sometimes I know that my prompts, ultimately,  
if I keep generating, I may get something very cool.  
So it's something I developed an intuition of how  
a prompt can ultimately work randomly once for something  
sweet.  
And there I got one image I liked very much, that one,  
because I could see the MIT dome and all those colors going out.  
And I felt I loved this energy.  
It looks very pop and energetic.  
And there is an ambience going out of it,  
like all this creativity going out of MIT.  
So I felt, let's keep pushing this.  
Let's create variations.  
Midjourney can generate lots of variations  
so I just generate many of those variations.  
The differences are very subtle but I want lots of choices  
to select my favorite one.  
This one was my favorite.  
So I thought I'm done.  
That's a cool logo.  
Let's print it now.  
So I sent that to my friends and they told me,  
mm, it looks fantastic, but can you remove the blue  
so that the printing is easier?  
And in fact, can see that there are some trees and people.  
Can you remove them?  
And I thought, yeah, OK, I think I can do that.  
And I totally know how to do this with Photoshop,  
for instance.  
But I also know that models like DALL-E,  
they allow you to change and modify  
little parts of the picture.  
So this is what I did.  
I actually this time went away from Midjourney, went to DALL-E,  
uploaded my picture, removed all the areas  
that they asked me to change.  
So I removed the trees.  
I removed the people.  
And I just asked the model to generate this.  
So that looked great.  
Now no more trees, no more people, and my picture  
is indeed looking much cleaner.  
I was very satisfied.  
But then the next step is I need to remove the blue.  
So how did I do this?  
I went to Photoshop, clicked on the blue, removed it  
and it looked like that.  
Honestly, that's now looking ugly  
because you have all these sort of greenish transition  
between the yellow and the blue.  
This is hard to remove.  
And I felt, how can I do now?  
Should I spend probably an hour or two cleaning all of this  
but it's not even guaranteed it will look that nice  
or can I try something else?  
And I felt maybe I can just ask DALL-E to do it for me.  
And I tried and I got this.  
Oh wow.  
That's looking beautiful.  
But it's absolutely not what I wanted.  
Now it's looking way too fancy and I  
wanted something that is simpler and then  
it changed too much my initial picture so it doesn't work.  
And then I'm back to this.  
I spent 30 minutes cleaning in Photoshop.  
And I was kind of desperate because although I  
tried so hard, it still looked not professional.  
This is going to be printed.  
Everybody will receive it.  
I don't allow myself to deliver something  
of just average quality.  
I needed to do something better.  
And again, I was feeling desperate at that point.  
And then I just started feeling, you know what, remember  
that you can upload a picture and then get variations  
by adding some text.  
It worked for the previous design  
so I felt, OK, this picture that is overall  
all right but not perfect quality,  
let's get some new pictures out of it.  
So this is what I did.  
It was 11:00 PM now.  
And then I got some new variations.  
They looked fancy.  
And I kept trying and trying in so many ways  
with so many different words.  
And I was on this generation frenzy.  
And I was getting happy.  
It looked like there were some promising ones.  
I even tried to include a little mascot of MIT, our beaver Tim.  
And then it was so cute and so cool.  
But I felt, OK, no, I don't want something cute here.  
I want something that looks like creative, brings energy,  
so let's try other ideas as well.  
And at that point, I did not really  
know how to prompt to get something  
that corresponds to my vision.  
And one of the techniques I use is let's  
see how other people generate.  
Let's get inspired by the words they use.  
So I went on the search bar of Midjourney  
to see how people were prompting with AI.  
And sometimes people use super simple prompts--  
AI logo make art.  
That simple and you get something cool.  
Sometimes people use tons of words,  
but I also know that if you use the very right words,  
you don't need that many.  
And I realized, what do I really want?  
I want my logo with just a clean white background, nothing more.  
Just a clean white background.  
And I felt, you know what, let's take my picture,  
upload it to Midjourney, and ask for a clean white background.  
And wow, I was getting so much closer  
from what I wanted, including this super cool picture up  
there.  
I said, wow, this is looking like something that really  
triggers something in me.  
It's exactly how I feel.  
This whole energy, this painting, this artistry,  
just exploding all of it and all the colors.  
I felt incredibly happy.  
So this one, I liked it so much.  
And I felt maybe I can create variations out of it too again.  
What if I blend two images together?  
What if I take this new image that I created from the one  
on the right and blend it with the first one  
in the first place?  
And let's see what I got.  
I got, again, other cool variations.  
It looked a bit different so it was more choice.  
And I tried even the first images  
from the very beginning, the one that  
was the parent of all those following images.  
And I got, again, some very cool ones.  
And I kept going, trying also maybe  
blending with some neural network.  
I was not as satisfied.  
And I just tried over and over so many different opportunities.  
I don't go cheap when it comes to generating.  
I just go with whatever I can feel  
and I just try over and over such  
that I have lots of choices.  
So ultimately, it was time to stop.  
It was already past midnight.  
So I had five pictures that I selected myself, reminding us  
that curation matters.  
So I selected all my favorites and I  
sent at that time to many of my friends, hey,  
I need to print a logo that will appear on a tote bag.  
Which one do you prefer?  
So I wanted also other people to give me their favorite opinion.  
Turns out that when I woke up in the morning,  
this one was the favorite of people, in fact,  
the first one I got with the white background.  
I was satisfied.  
It was looking great and it really  
corresponded also to my vision.  
I had to handle the color vibrance and the balance  
with Lightroom.  
So it's another software I use to handle pictures.  
I wanted to put the colors a bit more punchy because I knew  
that I needed only six colors.  
And then I tried to convert with six colors  
with random online software.  
Turns out it was not looking great.  
It looked too dull and too dark.  
So I said, oh, I need to do it manually.  
I don't know how to do it.  
I quickly read a tutorial online and started doing it.  
And I ended up with this version in only six colors  
using Photoshop.  
That was perfect.  
That was a satisfying logo with different colors.  
We can recognize the dome of MIT.  
I was incredibly satisfied.  
But we also needed a slogan.  
I asked punch lines and ideas from just ChatGPT.  
And in the end, we just went with something simple.  
"Powered by human and AI."  
It really felt like this.  
It was an entire collaboration with the tools,  
a whole blend of creativity and methods, a whole journey.  
And sometimes, you go one direction.  
It doesn't work and you move back to where you were before.  
So it's a whole tree of exploration.  
Overall, to get those two pictures,  
it was more than 200 different prompts I've tried,  
a total of two AI image generators,  
Midjourney and Dall-E, three image processing software--  
I use Lightroom, Photoshop, and Illustrator  
to create the final version in SVG format.  
It was me, the artist, three brainstormers with me giving me  
feedback, and more than 10 friends giving their opinion,  
really showing that this process of collaboration is so rich.  
I did not abandon my decision making to AI,  
but AI also enriched my serendipity  
and it was a beautiful journey.  
I hope this story gave you a lot of ideas  
and also inspiration for trying yourself.  
And you can see now it's being printed  
and people really loved it and kept the tote bag.  
I still have one today.  
And I feel so proud to work with the art I created myself.  
End of transcript. Skip to the start.  
\`\`\`

R2.2 Diffusion and GenAI Fireworks  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We are going to cover an exciting demonstration  
live of how we can leverage multiple generative AI  
tools all together to create an amazing web  
page in just a few minutes.  
The goal of this demo is to engage you  
into combining those tools, being  
creative in how one tool can kick  
start your journey with another one,  
and see also how multiple capabilities can be merged  
towards a final creation.  
I will use a combination of text models like Claude and ChatGPT,  
image models like Recraft, Midjourney or Dall-E,  
code interpreters and software generator like Replit,  
and even video generator like Runway.  
I'm going to show all of these so that we  
get a final beautiful creation.  
Let's get started.  
First of all, I'm going to use one of my favorite models called  
Claude.  
It's built by Anthropic, and it has some cool capability  
that you can get some code but also  
getting the code immediately visualized on the side.  
So let's start with a simple prompt.  
Create a fantastic website to advertise my course  
on universal AI.  
Use HTML and CSS.  
So those are two languages.  
And give me the most incredible visual aesthetics.  
What's important is to include those incredible, fantastic,  
beautiful words, because the model is suggested  
to look into how it can be really nice because when it was  
trained, those words were often associated  
with content of high quality.  
So I want to remind the model with my words  
of creating something that would be similar.  
Let's just get started with this simple prompt  
and let's see what's happening.  
Right now, the model has been processing this.  
And what's interesting with Claude is that on the side,  
it will now give you the code.  
And you can see that it generates the code token  
by token and goes very fast.  
Notice that it's indeed in HTML and CSS.  
Whether you know or don't know about that, what will matter  
is your ability to interact with the AI  
and to visualize the outcomes.  
If you're satisfied, you can guide the AI towards something  
you can judge.  
Maybe you cannot judge the quality of the code,  
but you can judge the quality of how it renders ultimately.  
So here, I have my web page, and it's already  
looking pretty cool.  
For instance, I have the nice text and font.  
I have little movement when I hover the mouse, 50 plus hours  
of content, and even a button where I can click and enroll  
now.  
If I click, nothing happens.  
It's because the model has only created the first page.  
So let's say now I want to change the color.  
I want something more in the colors of MIT.  
The model is so well-trained that it  
does know that MIT is typically using red and gray.  
We shall see if it works.  
And make it even better and more incredible and fantastic.  
Nothing too sophisticated in my prompt,  
but here, the idea is to work iteratively with the tool.  
By just asking the model to make it much better,  
the model will start to think, hey,  
what's possible for something that will look great?  
Again, it says, OK, I'm going to redesign and use  
MIT's iconic color, red and gray.  
So it does know about it.  
And now it's going to regenerate.  
Notice that the flow was you get something started  
and you can give specific feedback on what you want.  
Here, I was quite vague, but you would  
be able to feel free to tell the model, OK, I want more logos.  
I want to include a picture at the top, et cetera.  
So it's generating.  
You can see that the code is getting a bit longer.  
It's probably because it's trying to be more aesthetic.  
So it needs to code those aesthetics.  
In the meantime, let's create some visual design.  
So I'm now going to GPT, and I want to use the image generation  
from ChatGPT.  
It's called Dall-E.  
So let's start a chat.  
And I will say create amazing visuals  
for my course on universal AI.  
And here, I can put the ratio 16 by 9\.  
And I'm starting this.  
Notice that the way Dall-E operates  
is taking what you want, internally figuring out  
a good prompt for the diffusion models that we have covered,  
and then giving you some outcomes.  
So let's look at it.  
It's looking fancy indeed.  
You have a robot and colors like galaxies.  
It took the idea of universal into an actual universe.  
So that's an interesting take.  
Here, you have a robot meditating and AI even written.  
So those images look nice.  
Let's take this one to download it  
because I'm going to reuse it somewhere else.  
But I also want to know what prompt did you use.  
And my goal is to see how other models are going  
to react with the same prompt.  
It turns out that this is valuable for me  
to have a prompt already crafted with Dall-E  
because I don't have to make any effort for my own prompt now.  
I'm not telling you that you should never make effort  
to craft your prompt but that if you  
don't have anything specific in mind,  
that can be useful to kickstart your journey if you are  
in your learning process with prompting so that you don't feel  
overwhelmed.  
So I'm now going to Recraft, which is  
one of my favorite models too.  
I'm going to create a new project, an image,  
and I'm going to paste the prompt.  
You can choose the style.  
For instance, you want something photorealistic, illustration.  
So let's say I want something illustration.  
You can also choose the format.  
So let's say I also want something in 16 by 9\.  
And I'm going to click on Recraft.  
In the meantime, I'm also going to Midjourney,  
and I'm going to create images as well.  
Midjourney operates on the platform Discord,  
and you type image in plus your prompt.  
And I also want something in 16 by 9\.  
Notice that those three tools all use diffusion models,  
but they have different interfaces and also  
different capabilities.  
But the technology operates on similar principles  
to what we covered previously.  
While those models are creating, let's look at our web page.  
And I can even publish this.  
I'm going to copy the link, create a new web page,  
open a new web page.  
And now this is what I see.  
I do have the colors of MIT.  
I have more things, and it's even more design.  
When I hover the mouse, I can see things moving.  
You can see that things are even jumping a little bit.  
The course curriculum, notice that the model invented,  
hallucinated, the course content.  
It's because I did not give anything,  
and you can totally adapt that.  
But it's real example of AI trying  
to go ahead of what you will include in such website  
because I was so vague.  
And you can click on Begin Your Journey.  
Notice a little bug that the universal AI at the very top  
is overlapping with the banner.  
So that's a little issue, and the model  
does not know about that.  
So what I will do is that I will take a screenshot of how  
it looks like.  
I'm going back to Cloud, and I'm going to upload a screenshot.  
And I'm going to tell the model the universal AI text is not  
well visible.  
Update website.  
It's that simple.  
But because the model cannot see, just knows the code,  
it helps the model to guide it with a picture because you can  
see this with your eyes, but the model cannot.  
By including a screenshot, you help  
the model recovering vision.  
So now the model is generating and updating everything.  
And indeed, it's already a bit better.  
It's still not solved completely.  
I would say not solved completely.  
Re-update.  
While this happens, let's look into our images.  
Let's look into what I got from Recraft.  
And then you see it's another take to universal AI.  
It's a robot that looks more like cyberpunk vibe  
and the planet in the background--  
a bit scarier also than what I got  
with Dall-E. I'm going to save the image because I may reuse it  
later.  
And now let's look at Midjourney.  
Midjourney also operates under a similar type,  
but this time it's more like a futuristic Android  
with lots of stars behind.  
You can see that those models reacted more or less similarly  
to the prompt, and it depends on how  
they were curated by the founders of those models.  
I'm also going to select one of my favorite here.  
I think I like maybe the fourth one better,  
so I'm going to ask for upscaling the fourth one  
to the maximum quality.  
Notice you can also ask for a zoom out.  
So I'm going to zoom out.  
And in the meantime, I also want to create a little movie.  
So I'm going back to Dall-E. I want to download this.  
I'm now going to Runway Machine Learning, which  
is a video generator, and I'm going to upload a picture.  
So I'm going to upload the picture created by Recraft,  
and I'm going to say animate lots of movement,  
super \[INAUDIBLE\], stars everywhere, future universe.  
I do this for fun.  
Maybe it's not professional enough  
for the web page you would want to create,  
but my goal here is to illustrate  
how I use those models.  
And I can ask for five seconds of video  
with this image as an input as well.  
So it's image plus text prompting to get a video.  
And I can also decide that this picture, instead  
of being the first one in my sequence,  
should be the last one.  
And I'm also going to generate five seconds of that.  
Let's look into also my zooming out from Midjourney.  
They're all very similar, as you can see, very small variations.  
It's your style to choose which one you prefer.  
Me, it's the third one for very little reason.  
I don't even think it's more about how my intuition feels.  
I'm going to save this image as well.  
Going back now to Runway, I'm going to select,  
and I'm going to upload that image.  
And I'm going to use the exact same prompt just  
to see what I get out of it.  
And I'm going to do this one more time, this time  
with my Dall-E picture.  
So, same thing.  
First one, five seconds.  
So now, let's look at our videos.  
That's the one from my Recraft picture.  
And you can see that it created sort of a boomerang effect,  
interestingly.  
It zoomed in and zoomed out.  
And honestly, it's quite smooth.  
Few errors, and you can see a 3D aspect so that can be  
to your liking.  
Let's look at the other version where this time,  
I want this to be the last frame.  
The model made just a tiny bit of movement,  
but it created sort of an effect around the planet Earth.  
Now let's look at the one I got from the Midjourney picture.  
Oh, this one has much more interesting effects.  
You can see there is a whole effect of light  
coming all around.  
So I actually this one.  
It's quite fancy.  
And let's look at the one from Dall-E. Interesting  
as well because there is a change of perspective  
and things are blending.  
And overall, what's the conclusion here?  
Those models get even more complicated because now, you  
want to generate a video.  
And it lacks the proper capability  
to really create the video the way I would want.  
I haven't given a lot of details, of course, here,  
but those models are still limited in their ability  
to really stick to the advice, and they  
make a lot of sort of editing choices on their own.  
The way I try to leverage this is I  
know which image will probably already  
give me a pretty good video.  
I know this in advance.  
So when I choose an image I will input,  
I try to take that into account.  
I include the words that I think will be helpful,  
and then I just try over and over  
until I get a satisfying result.  
So this is really a trial and error process,  
an intuition you're building, and the involvement  
of prompt engineering.  
Interest of time, I won't keep exploring,  
but Runway has lots of cool features.  
Let's go back to our website, and now the problem  
has been solved.  
I have my universal AI appearing completely  
and the whole nice website.  
Notice that all of these is code,  
and you can leverage that code.  
Now you can tell the model I want  
to include a picture as the background behind universal AI.  
Named image1.pn.  
Below, include a video named video.mp4.  
Redo the whole code.  
So here, I just created a nice content, images.  
And I want to include it into my web page.  
The problem with Claude is that it's not a capability  
that the model currently has to be able to incorporate directly  
content you would upload.  
It can give you the code, but it cannot execute if you upload  
your own things.  
This is why I need to move on into another tool--  
for instance, a tool called Replit.  
So I will go to Replit.  
My goal here is not to teach you about this tool specifically,  
but just to illustrate that you can visualize how a code will  
appear ultimately, which will help  
you debug if there is any issue even  
though you don't even necessarily have  
skills in CSS or HTML.  
But because you know how to talk to AI,  
you have a vision of what you want,  
you'd be able still to perform very well.  
So I have my whole code here.  
I'm going to copy paste that code.  
I'm now going to Replit, and I'm going  
to create a new website here.  
So it's just going to be empty.  
Don't mind all the details about how should files be organized.  
Just remember that my idea is I want to see how it appears.  
And I'm going to use a software that can render that.  
So here, I uploaded the code in the index.html, which  
is the base file for a website.  
And I need to upload some content.  
So I'm going to click here, upload file.  
And maybe I want to upload the picture here.  
I need to rename it because I said it would be image1.png.  
And I need to get a video.  
This one was my favorite.  
So I'm going to download the video.  
I'm going back over there, and I'm going to upload it as well  
and renaming it video.mp4.  
So now is the moment of truth.  
Is it looking nice?  
So I will ask the model to execute my index.html file.  
OK, let's look at it.  
I indeed have my picture now appearing,  
and honestly, it blends very well.  
And below, I have the video.  
You can see that the video does not appear perfectly.  
Is it because of a bug that I don't know about?  
It looks like there is something to solve.  
It's possible it would have worked immediately  
and I would have been lucky.  
But very often, I have little bugs involved.  
The picture looked very good.  
Now, honestly, this web page looks already fantastic.  
Now I do want to solve this video problem.  
So what can I do again?  
I can take a screenshot.  
So I'm going to upload my screenshot  
showing that it doesn't work.  
I will say the video doesn't work.  
And let's see what the model tells me.  
In the meantime, in fact, I do know why it doesn't work.  
It's because I did not properly named my file.  
Here, this should be named video.mp4, and I bet that now,  
it will work--  
I mean, hopefully.  
Yes, you can see that the video works.  
It was because I did not name the file properly.  
That's a very naive, innocent bug  
that may happen a lot of times.  
And here, you have two ways of figuring it out.  
I mean, it's a classic mistake.  
And here, I happen to check.  
It's also possible that your code did not  
leverage the file as video.mp4 but maybe video1.mp4.  
So you just have to check.  
But this is where you need to do a bit of investigation.  
And here I'm checking, OK, where, is video.mp4  
appearing in the code?  
Maybe the name was not set properly.  
Here, let's look at what was the advice of the Claude.  
Claude does not necessarily know what  
mistake could have happened.  
So they proposed to include a YouTube video instead.  
That could be a good way if you have some trouble figuring it  
out.  
But now the beautiful news is that I have a working website.  
Notice, however, that when I jump on my website,  
the video does not play automatically.  
So that's also something you can tell the model.  
The video does not play automatically when I start.  
Can you make sure that it works in a loop and plays  
automatically?  
I won't necessarily do it in interest of time,  
but that's the kind of exercises that I  
encourage you to do to end up with a beautiful, nice web page.  
To conclude this, I also want to show you  
how the future of software engineering may look like.  
AI can, of course, help you code so many things.  
And there exist so many tools already  
to assist you as copilots.  
But you can even ask from scratch to, for instance,  
this Replit agent framework, to create a web page  
without even having you to be involved in the whole coding  
process.  
This is called an agentic workflow.  
You have multiple AI working together orchestrated  
and planned such that they can collaborate and each  
be responsible for different pages of your website  
or potentially different components of the code.  
Multi-agent systems are one of the most exciting areas  
these days in large language models because they  
enhance the capabilities and opportunities you can tackle.  
Think really about having a team of AI agents  
that can all be specialized in different domains.  
You make sure that they collaborate properly  
and they can give you valuable outputs.  
So expect a lot of exciting content coming from the big tech  
groups in the next few years.  
So here, I asked a Replit agent to build this web page,  
and it tells me, what do you want to include?  
OK, I want to include a course preview, testimonials, carousel,  
and interactive course curriculum.  
Sounds good.  
Here, the model does not really know what I really wanted  
because I was very vague.  
So it asks, OK, do you want these, these, or that?  
And now it gets to the creation.  
It's creating the skeleton of the whole code  
in multiple languages.  
So it was a Python file.  
Now I have an HTML file, and it keeps going.  
And you can see the model knows exactly how to orchestrate  
this whole package of files, which is incredibly powerful  
and will happen more and more in the near future.  
So it will be a new way again to collaborate  
because you have so many files involved,  
and it's hard to keep track of everything.  
So the debugging is becoming more challenging, especially  
because you abandoned a lot of your decision making while it's  
being built. But what you can still do  
is evaluating the final outcome.  
So now everything gets created.  
Here, we see a file for animations  
because we want something that's modern and will move.  
Here, it's a JavaScript file to properly handle  
the whole organization and design aesthetic.  
Here, you have an SVG file to have a little logo that  
will happen to--  
that will come to your page, another one.  
Now it's installing lots of packages.  
The model, to be able to build all of this,  
needs packages pre-implemented, and it  
needs to install them so it also knows exactly what needs  
to be installed.  
Now it's configuring everything.  
Now it's taking a screenshot to check how it looks like.  
That's a new feature because the model does not  
know if it appears good.  
So it takes a screenshot such that it recovers vision.  
And then now from the vision, it can keep going by itself.  
And I indeed have an amazing web page now  
that looks, indeed, very professional.  
You can click on Enroll now.  
Things are moving nicely, and you can even enroll.  
So even let's start to click to see if it happens.  
It does work.  
It brings me to Enroll Now.  
If I click on Features, it brings me here,  
and it's responsive to my mouse.  
And you can go to contacts.  
Still a few things to solve potentially.  
Here, the colors don't match that well.  
It's not that visible.  
But that's totally something you can  
arrange by telling the model.  
So look at what we built in about half an hour--  
an incredible amount of content, a web page  
using multiple techniques.  
We created videos and images.  
This is so exciting.  
Keep exploring all those capabilities,  
and I think we're up for an incredible future all together.  
Keep exploring.  
That's my final word to you.  
End of transcript. Skip to the start.  
\`\`\`

Recitation Summary  
\`\`\`  
In this recitation, we saw how generative AI supports creative work through two demonstrations:

AI-assisted design of the MIT Generative AI Conference logo and tote bag—an iterative process of prompting, revising, and curating outputs across multiple models and tools, where AI enriched but did not replace human decision-making.  
A live demo of building a website with AI—using Claude for coding, ChatGPT and DALL·E for imagery, Midjourney and Recraft for alternate visuals, and Runway for video generation, all integrated into a working webpage.  
Key takeaways:  
Creative workflows with AI are highly iterative—hundreds of prompts and multiple tools may be needed before reaching a satisfying result.  
Different platforms excel at different tasks: Midjourney for stylized images, DALL·E for inpainting and edits, Claude for structured code, and Runway for video motion.  
Human judgment, feedback, and curation remain essential; AI expands possibilities but does not dictate final outcomes.  
Combining multiple AI systems enables richer and more polished creations, from branding to functional websites.  
Congratulations on completing this recitation\! You’ve learned how AI can act as a creative partner across media types and how to integrate diverse tools into a single artistic or technical vision.  
\`\`\`

Assignments  
\`\`\`  
Skip to main content  
Overview  
Welcome to Assignment 1: Generative AI with Diffusion Models\!

This assignment explores what we have learned in Module 12, and in particular, we will learn more about diffusion models, CLIP text embeddings, and prompt-based image generation using Stable Diffusion. Questions in this assignment are based on this notebook. This notebook is complete, meaning that all code has been written and run for you, so that you see all the outputs from each code cell. The goal is to use these cell outputs, along with what you have learned in Module 12, to answer the questions in this assignment. 

This assignment consists of four parts:

Part 1 Text-to-Image Generation  
Part 2 CLIP Embeddings and Similarity  
Part 3 Prompt Style Comparison  
Part 4 Modifying inference steps  
Lectures covered in this assignment

Lecture 4: Diffusion Models for Text-to-Image Generation  
If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.

Learning Objectives  
By the end of this assignment, learners will be able to:

Generate images from text prompts using pretrained Stable Diffusion models.  
Identify how model choices, parameters, and hardware configurations (e.g., precision, GPU usage) affect performance and outputs.  
Use CLIP to embed images and text into a shared vector space and measure their similarity.  
Interpret cosine similarity scores to assess alignment between visual content and textual descriptions.  
Apply prompt engineering and model selection to create outputs in different artistic or stylistic domains.  
\`\`\`

Skip to main content  
This is the first part of this assignment, consisting of four questions. Please use the code and outputs in Part 1 of the notebook to answer the questions here.

Question 1  
1 point possible (graded)  
In the code generating the hummingbird image, which of the following would most likely affect the final output image?

Saving the image in grayscale

Modifying the text prompt

Reducing the model size after training

Changing the seed image format  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
1 point possible (graded)  
If we wanted to use another model to generate the hummingbird image, what part of the code could we change to most easily achieve that?

Import a pipeline model different from 'StableDiffusionPipeline'

Move the model from GPU onto CPU

Change the 'model\_id'

Change the 'torch\_dtype' to be 'torch.float32', which contains full precision  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
1 point possible (graded)  
Why is torch\_dtype=torch.float16 specified when loading the model, rather than after image generation?

To reduce the size of the output image file

To modify the tokenizer behavior

To ensure model weights are stored and computed in half precision during inference

To change how matplotlib displays images  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Suppose you want a general-purpose artistic model commonly used for creative prompt exploration, rather than a very specific animation studio style. Which model fits this role?

Linaqruf/anime-detailer-xl-lora

nitrosocke/mo-di-diffusion

nitrosocke/Ghibli-Diffusion

prompthero/openjourney-v4  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
This is the second part of this assignment, consisting of two questions. Please use the code and outputs in Part 2 of the  notebook to answer the questions here.

Question 1  
0.0/1.0 point (graded)  
What is the numerical gap between the cosine similarity of the two text prompts: "A brown angora cat sleeping on a couch", "A mountain with snow, blue ambiance"? and perfect semantic alignment (cosine similarity \= 1.0)? Please give 4 significant digits.  
  unanswered   
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)

Suppose we compare the following prompt pair to Question 1:

“A snowy mountain landscape” and “A mountain with snow, blue ambiance.”

Which statement is most accurate?

We cannot infer anything

The similarity is higher than in Question 1

The similarity is the same as in Question 1

The similarity is lower than in Question 1  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
This is the third part of this assignment, consisting of three questions. Please use the code and outputs in Part 3 of the notebook to answer the questions here.

Question 1  
1 point possible (graded)  
What is the effect of changing 'cyberpunk' to 'watercolor' in a prompt?

Applies post-processing filters

Alters the visual style in generation

Increases pixel resolution

Changes the model architecture  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
1 point possible (graded)  
Which conclusion about prompt conditioning is directly supported by the outputs in Part 3?

Prompt conditioning guarantees high-quality images

Prompt conditioning reduces noise during sampling

Prompt conditioning influences what the generated image represents

Prompt conditioning improves training efficiency  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
1 point possible (graded)  
Which of the following claims about the three generated images cannot be verified from the outputs shown in Part 3?

The same model was used for all images

The images differ visually

The numerical values of the internal text embeddings

Each image corresponds to a different prompt  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
This is the fourth and final part in this assignment, consisting of five questions. Please use the code and outputs in Part 4 of the notebook to answer the questions here.

Question 1  
1 point possible (graded)  
Which configuration in Part 4 of the notebook would most reasonably be chosen if fast iteration is more important than final image quality?

A smaller value of num\_inference\_steps

A higher-resolution output

A larger value of num\_inference\_step

A larger model with more parameters  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
1 point possible (graded)  
What happens when we increase 'num\_inference\_steps' from 10 to 100 in Stable Diffusion?

The image takes longer to generate and should seem to lower quality

The image takes shorter to generate and should seem to higher quality

The image takes longer to generate but the quality should seem to be the same

The image takes shorter to generate and should seem to lower quality

The image takes shorter to generate but the quality should seem to be the same

The image takes longer to generate and should seem to have higher quality  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
1 point possible (graded)  
In Part 4, which change directly explains why lowering num\_inference\_steps reduces total runtime?

The output image is generated at lower resolution

The latent space has lower dimensionality

The text encoder runs fewer times

The model performs fewer sequential refinement iterations  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
If two images are generated with 20 and 80 'num\_inference\_steps' respectively, which is most likely true?

Both images will take the same time if run on GPU

The 80-step image will always be sharper

The 80-step image may have more detail but takes longer to generate

The 20-step image will always be sharper  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
0.0/1.0 point (graded)  
Based on the runtime pattern observed in Part 4, which estimate would be most reasonable for the runtime at 200 inference steps?

Impossible to estimate from the data

Roughly the same as at 100 steps

Slightly less than twice the 100-step runtime

Approximately twice the runtime at 100 steps  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
In this assignment, we applied diffusion models and CLIP to understand how generative AI connects language and imagery.

Key takeaways:  
Stable Diffusion can generate diverse outputs from text prompts, and results vary with prompt design and model selection.  
Model parameters such as precision (float16 vs float32) and hardware acceleration significantly influence memory usage and inference speed.  
CLIP embeddings place images and text into a shared space, allowing direct comparison of their semantic similarity.  
Cosine similarity provides a simple but effective metric to evaluate how well an image matches a text prompt.  
Prompt engineering and thoughtful model selection are critical for achieving both creative and accurate outputs.  
Congratulations on completing this assignment\! You’ve gained hands-on experience with core diffusion and embedding techniques, strengthening your ability to use and critically evaluate generative AI models.

\`\`\`

Module Summary  
\`\`\`  
Skip to main content  
Module Summary  
In this module, we explored how generative AI is reshaping work, creativity, and decision-making. We examined its role in routine tasks, creative ideation, and high-stakes judgment, focusing on both its opportunities and limitations. In particular, We learned why judgment is harder to automate than knowledge or prediction, how GenAI supports associative creativity but still relies on human evaluative judgment, and how AI can enhance screening while raising risks of bias or over-reliance. The module concluded with a technical foundation in diffusion models, showing how they generate images from text through iterative denoising and text embeddings.

Key takeaways:  
AI and work: Automation excels at prediction and routine tasks, but human discretion and values are critical for judgment-based work.  
Creativity: Generative AI is powerful for associative creativity (brainstorming, idea remixing, rapid prototyping), but humans remain essential for evaluative creativity, ethical judgment, and curation.  
Decision-making: AI can improve accuracy and efficiency in screening and evaluation, especially for non-experts, but narrative AI may bias decisions while black-box recommendations can encourage more critical thinking.  
Technical foundation: Diffusion models generate images by iteratively denoising, guided by architectures like U-Nets and text-image alignment models like CLIP. Prompt design strongly influences outcomes.  
Human–AI balance: The most effective systems combine automation for scale and efficiency with human oversight for subjectivity, ethics, and accountability.  
Congratulations on completing this module\! You now have a conceptual and technical foundation for critically engaging with generative AI—understanding where it enhances human creativity and decision-making, where its limitations demand human judgment, and how to responsibly integrate it across creative, analytical, and operational contexts.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.

\`\`\`

