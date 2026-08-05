Large Language Models  
\`\`\`  
Module Overview  
Welcome to Large Language Models\!

In this module, we will explore Large Language Models (LLMs), which have rapidly become one of the most transformative advances in artificial intelligence. Built on massive datasets and powered by transformer architectures, they generate fluent text and multimodal content, enabling applications ranging from conversational agents to scientific discovery. This module provides a comprehensive overview of LLMs: how they are designed, how they function, and how we can interact with them effectively.

We begin by introducing the foundations of LLMs, including tokenization, autoregressive prediction, and scaling. We then move to understanding their architecture, with a focus on attention and transformers, and how these innovations changed the way models are trained and used. Finally, we explore prompting—how users guide LLMs through carefully crafted instructions to unlock reasoning, enhance outputs, and reduce common pitfalls.

Learning Goals  
By the end of this module, learners will be able to:

Explain the foundations of LLMs, including tokenization, autoregressive text generation, and the role of scaling in performance  
Understand the architecture of transformers, particularly attention mechanisms and their ability to model long-range dependencies  
Describe the paradigm shift in AI practice from training models from scratch to prompting pre-trained LLMs  
Apply prompting strategies—such as zero-shot, few-shot, and chain-of-thought—to guide model behavior and improve reasoning  
Recognize the strengths and limitations of LLMs, including their emergent abilities, biases, and tendency to hallucinate  
Evaluate practical and ethical challenges in deploying LLMs, including cost, efficiency, alignment, and responsible use  
\`\`\`

Lecture 1: Foundations of Large Language Models  
\`\`\`  
Overview  
Welcome to Lecture 1: Foundations of Large Language Models, taught by Professor Léonard Boussioux, Assistant Professor of Information Systems at the University of Washington. 

In this lecture, we will explore the fundamentals of large language models (LLMs), which represent one of the most transformative advances in artificial intelligence. Built on the foundation of transformers and trained on vast amounts of text data, these models have demonstrated remarkable capabilities in generating text, answering questions, summarizing content, and even reasoning through complex problems.

In this lecture, we explore what makes LLMs powerful, why scaling laws have been central to their development, and the challenges of data, compute, and evaluation that come with them. We will also examine recent innovations—like models that "think" internally before responding—and the ethical concerns of bias, misuse, and responsible deployment.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain the scaling laws and why they drove the rapid growth of LLMs  
Describe how transformers and attention mechanisms enable contextual understanding in text  
Discuss the tradeoffs between model size, efficiency, and accessibility, and how techniques like distillation address these  
Understand the limitations of LLMs in reasoning, their tendency toward noisy or probabilistic outputs, and why human oversight remains essential  
Recognize the ethical challenges of bias, misinformation, and benchmark leakage in evaluating model quality  
Appreciate the wide range of applications of LLMs, from text generation to summarization and beyond  
\`\`\`

L1.1 What are Large Language Models?  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The topic of the day is a very ambitious one.  
You probably heard of large language models.  
You probably use ChatGPT.  
Now is the day where we uncover the mysteries behind.  
I'm saying it's ambitious because I'm  
going to cover lots of concepts and content,  
in fact, as much as I can in the short time  
frame of this lecture.  
My motivation for you is to uncover the mysteries such  
that you feel more confident when you use the technology,  
you have a better understanding of what neural networks are  
involved, and you feel ready to push your journey forward  
in the domain.  
So let's get started.  
The learning outcomes for the day are the following.  
I want you to be able to define the foundational principles  
of large language models, including the fact it's  
a data-driven learning process.  
What is tokenization, and what is this principle  
of autoregressive text generation, which  
is, in fact, how large language models can generate text?  
We'll explain the architecture and functioning  
of large language models, focusing  
on some key concepts, so this autoregressive text  
generation, the self-attention mechanisms, and also  
multi-head attention.  
Lots of new words--  
I know it's complicated, but I want you to have a better  
intuition very soon.  
And also, we will describe the performance, the applications,  
and the limitations of large language models  
and how we can leverage some techniques to adapt,  
refine, align those models and figure out some trade-offs  
with some of those methods.  
Let's dive into it.  
We covered in previous modules discriminative AI,  
when, out of some data and labels,  
you can use, for instance, a decision  
tree, a linear regression, a logistic regression  
to output something.  
For instance, it can be the temperature tomorrow,  
the price of the stock market, if a given  
person has a given disease.  
The idea is, this discriminative model,  
we learn relationships between the data and the labels.  
What's different with generative AI  
is that you start with an input that is not necessarily well  
structured, and you want an output that will be new content.  
Large language models are such technology.  
They can generate new content.  
The way they operate is by learning patterns  
in unstructured content.  
So the very important principle for you  
is that the large language models  
are no different from all those AI  
models that we studied so far.  
They learn from data, and they will  
use complex pattern-matching to generate text.  
And here is how it works.  
The principal of a language model  
is that it can calculate the conditional probability  
of a word appearing next in a sequence based on the preceding  
context.  
So if you start with the sentence "The cat sat on the"--  
the language model will output the probability  
that every possible word in its dictionary will be the next one.  
So it gives you a probability that the next word is  
aardvark, chair, mat, or zebra.  
If you don't know what is an aardvark,  
this is this interesting animal, and it's actually a word  
in the dictionary of ChatGPT.  
A likely word is maybe "the mat."  
The cat sat on the mat.  
So the model will give you a higher probability  
that the cat sat on the mat, but it's also possible  
that the cat sat on the chair.  
So there is a decent probability.  
But it's very unlikely that the cat would sit on a zebra.  
So this is why you have a probability of 0\.  
So that's the first key principle.  
A language model can understand what's before  
and tell you what's the likelihood that a given  
word will be the next one in a sentence.  
This is great because we can leverage that mechanism  
to generate text sequentially.  
So given a prompt, so a text as an input,  
the large language model can pick the most likely next word  
or sample a word from the possible words  
to be the next one.  
So let's take a famous soliloquy from Hamlet,  
"To be or not to be."  
You give this to the large language model,  
and you want to see what's the next word.  
So the large language model will tell you,  
this is the word "that."  
So you take that word, you put it in the prompt,  
"to be or not to be, that," you push that into the large  
language model again, and you get the next word, "is."  
You take the word "is."  
You put it in the sentence again, "to be or not to be,  
that is," and you keep going.  
You obtain "the."  
And you do it over and over.  
That's the principle of ChatGPT and all  
those famous large language models.  
They generate the words one by one.  
And then every time they generate a new word, they  
take it, put it in the initial sentence,  
and reproduce the process until it reaches a stopping condition.  
So here, for instance, is the first paragraph  
of the soliloquy of Hamlet.  
So that's the first key word.  
Text generation is an autoregressive process.  
You can understand that as the intuition of your autocomplete  
on your phone.  
When you're texting, you have a few words that are suggested.  
That's the same thing that happens with large language  
models.  
They just pick one of the next possible words,  
and they keep repeating.  
That's the magic.  
It's also very impressive that models like ChatGPT  
can be so powerful, while, in fact, what they just do  
is generating words one by one.  
Of course, there is lots of mechanisms happening  
to be able to figure out how to generate words one by one, such  
that overall, they make sense.  
And now we are going to uncover all of these.  
End of transcript. Skip to the start.  
\`\`\`

L1.2 Architecture and Functioning  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: What makes large language models special?  
A few different things about them.  
First of all, they have a special architecture  
called the transformers.  
Those transformers have access to a self-attention mechanism  
that gives them a contextual understanding of the content.  
And then they can be trained in a good way  
thanks to parallel processing.  
Those are new keywords for you.  
We will explain them later.  
Next, they also operate using a neural network  
that I just mentioned is a transformer but a very  
large one, very often more than 1 billion weights.  
It's huge and very hard to train,  
which means if you want to train such a model,  
you also need lots of data.  
So the large language models are able to learn from gigantic data  
sets scraped from text on the internet and private databases.  
By the way, the GPT of ChatGPT actually  
means Generative Pretrained Transformer.  
Generative because it generates.  
Pretrained because it's been pretrained  
on this massive amount of data.  
And transformer because this is the architecture used  
by the model, and I will explain that very soon.  
Other important concepts-- foundation model.  
ChatGPT is a foundation model.  
It means it was trained on such a huge amount of data  
that it's like a foundation, a model that  
can be adapted to downstream tasks, that  
is so good from everything it has learned,  
that can easily do a few different things from now on,  
because it has learned this ability to adapt.  
This is a key slide--  
the whole pipeline of the large language model.  
And I will go through it step by step.  
The way it works is the following.  
You have this text that you input.  
That's the prompt.  
Sometimes you ask questions.  
Sometimes you just iterate on some content.  
But basically, you input text.  
The problem is that text is not what the computers can process.  
They can process numbers.  
So we need a way to convert your text into a sequence of numbers.  
This is called tokenization.  
So I'm going to take for instance,  
the sentence "What's the most delicious fruit?"  
And I'm going to convert that into tokens,  
meaning little parts.  
And every little word or subword will be represented as a number.  
Now that I have this series of numbers,  
I can give that to the large language model,  
which is a big transformer.  
And this is similar to what we covered before  
with feedforward neural networks or convolutional neural  
networks.  
They just receive numbers as the entry, the input.  
The large language model is going to do lots of things,  
but finally, it gives you an output.  
And this output will be a probability distribution of what  
is the most likely next word.  
So for instance, it can be mango, strawberry, pineapple,  
cherry.  
But you don't want a probability distribution as the user.  
You just want one output, the final decision from the model.  
So there is some technical details  
where you take this final probability  
distribution to select one final choice of a word.  
And here, maybe it will be mango,  
which is one of the most popular fruits.  
My personal favorite is cherry, but it turns out  
from what you find online, that mango is a favorite of people.  
I actually asked the question to several popular models, what's  
the most delicious fruit?  
And ChatGPT gave me a series of potential fruits.  
And mango came first.  
I asked Claude, another popular model.  
It also told me that mango is its personal favorite.  
So if you look at the answer of Claude,  
the model even says that it's a personal favorite.  
Gemini, which is the large language model  
version of Google, also goes with mango.  
But interestingly, when I asked Google,  
they have now implemented a new feature  
called AI overview that's trying to give you  
an answer from the first few websites.  
And the answer I got was very unusual.  
It was gooseberry.  
And maybe some of you have never heard of the gooseberry.  
It turns out that Google Overview looked into a YouTube  
video where someone was saying this is the most delicious fruit  
that nobody has heard about.  
And the model has just leveraged that  
content to give you the answer.  
So it works a bit differently than the other three,  
where it just operates based on the previous knowledge.  
The Google version of the AI Overview  
is looking through answers online  
of what people say and just give you the final answer.  
But just for the curiosity, I wanted to mention this.  
End of transcript. Skip to the start.  
\`\`\`

L1.3 Tokenization in Detail  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So now going back to our pipeline,  
I mentioned that to be able to process the initial text,  
you need to convert that into tokens.  
A token is a key mechanism to figure out  
how words can be represented as numbers,  
because if you think about vocabulary,  
you have so many variations of the same word.  
Some words can be written as a verb, as an adjective.  
And the past are different.  
For instance, "I am," "you are," "he is" is the same verb,  
"to be."  
Some words can be represented in different manners  
depending on if they are in the plural form,  
if you use them in a given context.  
So this is why there is a need for a common set of vocabulary  
to not have too much struggle for word representations.  
For instance, take the word "unbreakable."  
Do you want a token for the word "unbreakable"?  
Or do you want rather to decompose this word  
into "un-break-able"?  
This is a more general way of doing it,  
which would enable you to scale to more potential words.  
And then some sentences might be so common--  
or some group of words-- so common  
that it's valuable to have a token just for this.  
For instance, "what's" is so common that it can be--  
instead of just "what" apostrophe S as three tokens,  
it can be just one token.  
And finally, all sorts of punctuation.  
If you have an interrogation mark, two dots,  
maybe they should be represented with one token as well.  
Just to show you a fun way of visualizing tokens,  
I took my name.  
And I wrote it in many different ways.  
I wrote it the English way.  
I wrote it the French way and also  
with no capitalization in the first letter.  
And notice that, for instance, for GPT-4o,  
depending on how I wrote my name,  
it's actually tokenized in such different manners.  
And even the same way it's written,  
depending if there is a space before my name or not,  
it's going to be tokenized differently.  
For instance, at first it's "Leon-ard."  
Then there is a space and then my name completely, "Leonard."  
So space plus "Leonard" is actually one token.  
But if there is no space at the beginning,  
the model does not have a token for my name anymore and is  
actually decomposing into "Leon" and "ard."  
There is no token for my name in French.  
So the model actually used L, the E with the accent,  
"on" and "ard."  
And if you have the space before,  
it has token with space and "Le" with the accent.  
And if I don't use the capitalization,  
it's also a different token.  
You can also see that I wrote my name  
in multiple other languages.  
And you also have tokens for different languages--  
for instance Hebrew, Arabic, Mandarin, Japanese,  
Korean, and Sanskrit.  
And if you notice, into Sanskrit,  
some tokens appear with an interrogation mark.  
It means that the OpenAI model does not  
have a token for every Sanskrit character  
and instead is going to use some minuscule decompositions  
of multiple tokens that we do not  
understand as humans to be able to recompose every Sanskrit  
character.  
And then the way models are tokenized is changing over time.  
Now, at the time of recording, GPT-4o  
is one of the most advanced versions of ChatGPT.  
Before, you had 3.5 and 4 and GPT-3.  
You can see that the more you move forward with modern models,  
the more you try to have fewer tokens, meaning  
tokens that encompass more of the content of your words,  
because it means the model has more understanding  
of the vocabulary.  
It's quite complex to understand what's happening.  
But I encourage you into diving into this if you're curious.  
And you can also notice that OpenAI  
decided to have tokens for more languages as time passed.  
For instance, you can see that from no tokens for Mandarin,  
there is now tokens for common Pinyin characters.  
All right.  
So now we could see that I have a set of tokens  
that are numbers.  
This is great.  
And I'm going to bring this into the transformer architecture.  
That's also a very complex moment.  
I believe it's OK if you don't understand all the details.  
My goal here is just to give you an understanding of how  
it's structured such that you can read more  
about it if you're curious.  
Basically, the transformers were invented a few years ago  
and released in this super famous paper now,  
"Attention Is All You Need."  
The way it works is that when you have your tokenized prompt,  
it's going to be embedded, which means going to be transformed  
by a few layers.  
It's going then to go through multiple GPT blocks.  
Those GPT blocks will process your information.  
And you have a stack of them.  
Finally, as you arrive at the very end,  
you are going to flatten all of these,  
as we've seen with the convolutional neural network,  
meaning you take the representation  
in multiple spaces.  
And you just make it a vector.  
And you just get your final probability  
for every possible word in your vocabulary.  
The key idea for you is this is different blocks.  
Those blocks are quite complicated.  
But my goal is just to tell you, hey,  
you have your tokenized prompt.  
It's going to go through multiple types of neural network  
layers.  
And in the end, after all this processing, you get your output.  
That's the key idea to remember.  
And the large language models can exist  
in so many different formats.  
And as time passes, you have so many variations.  
So keep following the updates.  
It's very hard to keep track of everything.  
The literature is going all over the place.  
It's such an active and booming topic.  
End of transcript. Skip to the start.  
\`\`\`

L1.4 Contextual Understanding  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now it's time to understand  
how the magic of large language models happens.  
Because we want to predict the words properly,  
it also means we need to be able to understand  
the context of everything that happens in your sentence.  
We call this contextual understanding.  
That's one of the key powers of neural networks used  
for transformers.  
They're able to figure out how different words relate  
to each other.  
So let's take the sentence "The cat sat on the mat because it  
was tired."  
You want to know if "it" refers to the cat, to the mat,  
or any other word.  
The contextual understanding would tell you that "it"  
refers to the cat, because "tired"  
is not an adjective that typically goes with a mat.  
It rather goes with the cat.  
For us humans, it's quite evident that "tired"  
would be for the cat.  
But imagine for a neural network,  
it could be quite challenging.  
So that's one of the things that the model needs to learn.  
Now let's take the same sentence with one variation.  
Instead of "tired," I'll put the word "warm."  
And if you take the word "warm," it means that this time "warm"  
refers to the mat, not to the cat.  
It could be potentially, because the cat was warm.  
But it's rather more likely to be the mat.  
So you want the model to be able to understand  
this contextual understanding.  
And to make this happen.  
There is a key technology called attention mechanism.  
It's a very complex concept, in my opinion.  
But I want to give you an analogy to understand it better.  
We need three more words of vocabulary-- query, key,  
and value.  
Let's say that I want to do research  
about the impact of technology on society.  
That will be what we call the query.  
I have a question.  
So I'm going to the library.  
And I want to find information about that  
so that I can write my essay.  
How do I figure out which information is valuable for me?  
I'm going to go through the different books.  
And I will read their title and the subject tags.  
Those are the keys.  
They indicate what's in the different books.  
Now that I have my query, I have my question.  
I know which books are useful.  
I want to figure out what's in the book,  
the relevant information for me.  
So this is what we call the value.  
That's the actual content of the book.  
What happens in neural networks, called transformers,  
is the same thing.  
Lots of queries mean lots of questions, lots of things  
to understand.  
You need to look at all the content that can  
help you understanding things.  
And now that you figured out what can help you understand,  
you need to extract the value, meaning the actual content.  
I'm going to repeat it in another way.  
The idea is to figure out how much attention you should  
pay to other parts of your sentence  
when you are going to generate the next word.  
So this is implemented with math and different components.  
The whole point is to figure out how I can gather  
the relevant information.  
And then the words that you have in your input  
will help you doing this.  
So the query that I just mentioned  
will represent the current word token  
that will look for relevant information in the process.  
The key will represent the different components  
you can get from all the other words around you.  
And then the values will represent  
what's actually in those other words around you.  
This whole process will allow every word  
to know how much attention they should pay to others  
and what information you can get as more understanding for you.  
And then let's now illustrate how it works.  
This is, for instance, a sentence--  
"I love AI."  
And I have embeddings from it, meaning  
I have a representation of every word as a vector,  
after I did the tokenization.  
I will now use the query weights, the key weights,  
and the value weights in the process.  
Those are weights that you need to learn, a bit like the filters  
we covered in convolutional neural networks.  
So those are values that will be trained during the process.  
So you have three matrices.  
You multiply this matrix that you  
learn with the input embeddings, for each one of them.  
And you end up with your query, your key, and your value.  
So I repeat-- you take your query weights, your key weights,  
and your value weights that you've  
learned through the process, what you're learning right now.  
You multiply with the input embeddings,  
and you get those three matrices.  
Now, remember that we want to figure out  
how much attention every word should  
pay to the other words in the sentence.  
How do you do this?  
You compute what we call the attention  
scores, which is just a multiplication  
of your query and your key.  
And then you apply the softmax function  
to make sure that everything is more soft, more smooth.  
Now that I have those attention scores,  
it means that I know exactly which  
words give me relevant information to understand  
what's happening overall.  
And now that I know where I should pay attention,  
I will take those attention scores  
and multiply them with the value.  
And like this, I get my attention outputs,  
which will give me some context-aware embeddings.  
So out of my iLog AI input embeddings,  
I am getting what information is right there for me  
with all the words in the context.  
That's how the model builds contextual understanding  
between all the words altogether.  
If we put it all together, it's also challenging, I recognize.  
But the idea is I'm going to do that not a one  
time but many, many times.  
It's a bit like we did for convolutional neural networks,  
when they had multiple filters.  
I'm actually going to have multiple query matrices,  
key matrices, and value matrices such  
that I can look at my sentence through so  
many different angles.  
To give you a little bit of an analogy,  
it's a bit like you take one sentence  
and you give it to 100 students.  
And every one of these students is  
going to look at the sentence in a bit different manner.  
That's the exact same thing for the network.  
We are going to pay attention to the different words  
in different ways.  
Like this, your model will be able to learn  
very interesting parameters.  
That's how the model becomes intelligent-- by looking  
at every sentence under every possible angle.  
And the cool thing is you can make this very parallel when  
you train it, because the architecture is  
properly formatted.  
So going back to our whole pipeline, you have your prompt.  
You tokenize it into numbers.  
Those numbers, you fit them into the large language model  
that you will use this attention mechanism  
to figure out which words should pay attention to which  
other words.  
You do this so many times in so many different ways  
that you end up understanding really much  
what's happening right there.  
And it allows you to go to the next stage, which  
is the output of the next word.  
Final question is, OK, I have my probability distribution.  
How do I get the--  
my final choice out of all of them?  
You have multiple ways of doing it.  
One way is you take all the different words  
and you just pick the most probable.  
This is called greedy decoding.  
You just take the highest scoring token.  
Second technique-- top-k.  
You are going to consider the k most likely tokens.  
And you are just going to sample them based on their likelihood  
scores.  
So you just readjust their probabilities,  
now knowing that you only have two possibilities.  
So if I take only two, I have mango  
with a 62% possibility and strawberry  
with a 38% possibility.  
This is why if you take your text in ChatGPT  
and you open multiple chats, you may end up  
with different answers, but it's the exact same question.  
It's because you actually select the words with some randomness.  
And the other possibility is top-p, where this time,  
you're going to select the top 25% words.  
So you will take as many words as it  
needs to get into the threshold of 25% probability  
if you sum up their likelihood.  
So if I take top 25% here, I have mango, strawberry,  
and pineapple.  
And I'm just going to sample out of those three.  
In practice, with ChatGPT, they just take all the words  
as possible outcomes.  
That's something you can change.  
But in the ChatGPT interface that most people use,  
it's a default value, which means  
that potentially any weird word could actually come next.  
But they trained the model so well  
that naturally, the model knows what are the top possibilities.  
But it reflects back to what I just  
said, that this is why the same question can have  
different answers if you open different chats,  
because in practice, they really try to maintain the fact  
that there is randomness.  
One way to monitor the randomness  
is to include a parameter called the temperature, which  
allows you to reweigh the weights differently.  
So for instance, you may want to be not that creative.  
You want really to say OK, mango is the number one.  
I still want to allow every word to potentially be the next one.  
But I want mango to be way more probable than just 52%.  
So I'm going to push mango much more  
by having a low temperature that will refocus the network on what  
is the most likely.  
If you put a higher temperature, it  
means you want your model to be more creative, to potentially  
choose things that are more random and more unexpected.  
So in practice, the temperature is set to 1 with ChatGPT,  
as of now.  
And that's something that you can choose if you are a coder  
and use the API interface.  
End of transcript. Skip to the start.  
\`\`\`

L1.5 Applications  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now that I covered a lot of interesting concepts,  
I want to replace us in the history  
so that we have an idea of what were key inventions  
to make sure we get ChatGPT, because it's  
more than what I just covered.  
There is also some other important aspects.  
GPT2 to GPT3 was already a big leap  
because GPT3 had more training data,  
and then the architecture used was also much bigger.  
You can see on the right the number of parameters.  
GPT3 had 175 billion versus only 1.5 billion for GPT2.  
But the secret to go from GPT3 to ChatGPT  
was to go beyond the initial training of the model  
and to fine tune the model even more.  
But what was also magical is that when you scaled  
the amount of training data and the size of the architecture,  
the model started to be smarter, started  
to have some emergent properties to be  
able to adapt while they were not  
trained on some specific tasks.  
This is why ChatGPT took over the world.  
The model can help you with so many different tasks.  
Even if the model was not trained on that specifically,  
it can generalize because it learned so many concepts.  
So now let's look into how do you get a GPT3 into a ChatGPT.  
GPT3 by default will be racist, sexist,  
won't answer your question very well,  
and we want the model to be useful  
and agrees with our values, so we need some other methods.  
One important method is to fine-tune the model  
with some specifically well-curated examples  
of question and relevant answer.  
With those well-curated data sets,  
I can therefore have a model that will  
be more tuned to what I like.  
But that's still not enough.  
I need also to help the model understanding our values  
and what is a good answer or a bad answer.  
So there exist multiple methods, like reinforcement  
learning with human feedback or constitutional AI.  
The idea is that you have a reward model that you train  
that will be able to tell ChatGPT,  
OK, you're doing a great job right now.  
Or no, this is a bad answer.  
And now that ChatGPT has some feedback,  
you can retrain the model such that next time  
it won't output those tokens as much  
and will start doing other types of answers.  
The idea is really to guide the model  
to being better and more aligned to your desires  
because you give feedback regularly.  
And we can use techniques like reinforcement  
learning, that I do not cover, to get this.  
So if we take an example, which type of optimization model  
is most suitable for the traveling salesman problem.  
Maybe you have heard of that problem, maybe you did not.  
Maybe ChatGPT has never heard of this,  
and it tells you a linear optimization model.  
That's an OK answer.  
In fact, it's a mixed integer linear optimization model  
typically.  
So you give a small reward to the model.  
And now that the models say, OK, I just have an OK answer,  
I could do a better job, you're going  
to update the weights of your neural network  
such that next time it outputs a better answer.  
And you do this with so many different techniques.  
And how do we get from ChatGPT 3.5 to GPT4?  
And again, people say, wow, this model is even better.  
There is the method of having a mixture of experts.  
The principle is that when you have an input,  
you have a network called a gating network that  
will understand the type of question you just  
asked and will route your question to submodules  
of ChatGPT.  
Instead of going through the whole network,  
you go through a specialized submodule.  
Imagine if I ask all my students,  
OK, questions about soccer, questions about how to cook,  
questions about traveling.  
Maybe some students have different hobbies,  
different specialties.  
So some students may have better answers than others  
because they're more informed.  
Here is the same idea.  
You have one big ChatGPT with many submodules,  
and some of those submodules are specialized into coding,  
into summarizing texts.  
And then the gating network understands what type of query  
you're asking and will route that properly such  
that you get the best answer possible.  
This is how we got an even better model out of GPT 3.5  
by sort of specializing multiple sub GPTs.  
I want to mention that now all those techniques are implemented  
in so many different ways.  
Meta recently released Llama 3.2, open-source,  
and you can visualize that they involve so much pretraining,  
fine-tuning, other things like distillation.  
You have so many concepts involved.  
So the idea for me in this lecture  
is to equip you with some intuition of how it works,  
and then you can keep your journey  
going by exploring all those amazing technologies.  
End of transcript. Skip to the start.  
\`\`\`

L1.6 Practical Challenges  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: I want also to give a few comments.  
First of all, the fact that OpenAI did a big bet.  
They bet that if they spent lots of money  
in training a huge neural network using  
a huge amount of data, they will have something  
very smart and intelligent.  
This is because there is some research in the past few years  
called the scaling laws.  
People have observed that the more compute, the more training  
data, and the larger architecture you go,  
the better your model becomes.  
And so far, it's called a law because it's  
been verified empirically.  
So this is why you may hear that we need more data,  
we need more compute--  
because companies think, OK, I need  
to increase the capacity because I will get smarter models.  
The challenge is at some point, you run out of data available.  
It's also extremely computationally expensive,  
so lots of technologies need to be involved  
to solve that challenge.  
A recent model from OpenAI is called O1.  
This is also a new mechanism that operates.  
Instead of giving you the final answer word by word,  
the model is going to think first internally such  
that it won't output the best guess as of now,  
but is going to iterate and do some draft.  
And when it's satisfied with the draft it has,  
it will give you the final answer.  
It helps improving the performance a lot.  
Here is a demo of how it works.  
I'm going to select all one on ChatGPT,  
and I'm going to paste a very challenging problem  
about scheduling operations in a farm to pick apples.  
As you can see, it's very complicated,  
lots of decisions involved.  
And what's happening is that before giving me an answer,  
the model is currently building a form of a reasoning process.  
And here, you can visualize this reasoning process.  
It's only a summary of the reasoning process.  
OpenAI does not make it public exactly what the model is doing,  
but you can see that the model is doing all sorts of things--  
calculating profits, modeling the strategy,  
defining variables.  
And you can see how many steps are involved  
in a hidden manner for you.  
And after it's completed generating  
all those internal steps of how it should approach your task,  
it will finally give you the answer.  
This is a way to scale the capabilities of your model  
beyond just the training stage, but also  
at the inference stage, meaning the moment when you predict.  
It's a great, interesting paradigm  
that we may see arise more and more in the next few years.  
Now that the model finished thinking,  
it's finally giving you the answer.  
And as you can see, it's giving me mathematical answers.  
It's hard for you to figure out it's even correct.  
There is so much involved.  
But my goal is to visualize the way  
the model can think or process information  
and is able to do math.  
It's possible subtle mistakes are hidden a bit everywhere,  
and this is why you need the human oversight  
to verify what's happening and if it's even  
going in the right direction.  
So keep thinking about this debate.  
Are large language models able to reason,  
to have an actual rationale?  
That's something we will explore in the generative AI  
module a bit more, because large language models can potentially  
think and give you answers using multiple principles.  
First of all, they are good at memorizing information  
because they're so huge.  
Sometimes they give you an answer  
that is about probability.  
For instance, what's the best fruit  
is something that they collected from huge amount of data  
by reading lots of forums.  
They output that mango is very probable.  
If you ask, for instance, what's the national day of France,  
the model has read lots of Wikipedia pages and memorized  
its July the 14th.  
Now, if you do math and you ask the model to do math for you,  
you don't necessarily have the answer,  
and you don't really know what's probable or not probable.  
So the model will start to do some form of a noisy reasoning.  
It will try to imitate how humans would approach the task,  
but it will have lots of noise and potential mistakes  
in the flow, because the real goal is  
to have some symbolic reasoning, an actual reasoning  
with specific rules that if you follow, you will get it right.  
But large language models struggle with this.  
It's an ongoing debate.  
It's unclear how models actually give you answers and reason.  
So get excited about this and look more into it.  
That's one of my areas of research.  
Evaluating the quality of your model is also very important.  
You need to figure out if you can release  
this version of ChatGPT, or if you should keep training  
a bit more.  
So there is a whole process of evaluation.  
So it's a big topic as well, and there exist lots of benchmarks.  
The problem with those benchmarks  
is that lots of the data has leaked online,  
and so the models may learn directly from the testing set.  
And they look very good, but actually, it's  
because they cheated.  
They already learned the answer perfectly.  
So this is why you don't have to necessarily trust  
those benchmarks.  
You just give an idea.  
And then, for instance, there is Dr. Jim Fan  
who's working in big tech, who is saying it could even  
be a homework for students to try to break the testing set  
and get your models to outperform in the benchmarks.  
So keep an eye on these that don't necessarily  
trust what those big tech companies are telling you are  
we are now the best at this.  
Also wanted to mention that having a large language model  
is expensive to run, and maybe it  
won't be able to be stored on your phone.  
This is why there is the technology of distillation.  
The idea is to have small language models that  
will train thanks to the strengths of the larger ones,  
but you are going to distill this knowledge into a smaller  
version.  
You transfer knowledge, a bit like  
transfer learning that we've seen earlier.  
And you can use the outputs from the large language  
model as some guidance.  
It's like a teacher model, and you're a student, a smaller  
student model.  
And thanks to this, you are able to maintain a smaller size.  
To conclude, we've covered lots of important content.  
What I suggest to remember is that the large language  
models learn from vast amounts of data taken from the internet.  
Some of these data may be high quality.  
Some of these data might be very low quality.  
And the more we learn all of this--  
including, for instance, content you don't  
want, like racism or sexism--  
but that's behaviors you can find online or social media,  
so the model by itself will replicate this  
because it's what it has seen.  
This is why you need methods to alleviate that--  
for instance, fine-tuning or reinforcement  
learning with human feedback.  
Remember that the models generate tokens one  
by one, which means it may limit its reasoning process,  
yet it's still super powerful because they  
have great architectures based on the transformer.  
We have attention mechanisms that  
are able to understand the contextual meaning  
of every word in your sentence.  
It has lots of applications.  
You can have text generation, summaries,  
and many other exciting use cases  
we'll cover in the next module.  
So looking ahead, those large language models  
are really transforming the capabilities  
of so many industries, but it's important for us  
to verify how they can be efficient, scalable,  
and ethical.  
We really need to all work hard to maintain  
a responsible deployment.  
This is why we have also other lectures around this.  
Thank you for listening, and keep  
exploring the amazing opportunities from those models.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
In this lecture, we explored the foundations of large language models, how scaling laws and transformers fuel their capabilities, and the ongoing challenges of data, compute, evaluation, and ethics. We also examined cutting-edge advances such as reasoning-oriented inference strategies and knowledge distillation.

Key takeaways:  
Scaling up data, compute, and architecture drives LLM performance, but introduces practical and ethical challenges.  
LLMs are powerful text generators that rely on probabilistic prediction, not guaranteed reasoning.  
Evaluation requires caution due to benchmark leakage and bias in training data.  
Techniques like distillation help balance performance with efficiency, making LLMs more practical for real-world use.  
Congratulations on completing this lecture\! You’ve gained a foundation for understanding how LLMs are built, why they work, and the opportunities and challenges they create for AI applications.  
\`\`\`

Lecture 2: Understanding LLMs  
\`\`\`  
Overview  
Welcome to Lecture 2: Understanding LLMs, taught by Professor Georgios Stamou, Professor at the School of Electrical and Computer Engineering at the National Technical University of Athens, Greece, and Visiting Professor at MIT. In this lecture, we will dive deeper into Large Language Models (LLMs).

LLMs are not just powerful text generators; they are complex systems built upon massive datasets, sophisticated architectures, and nuanced training processes. In this lecture, we take a deeper look at what makes these models work. We’ll explore how their scale, pretraining, and fine-tuning contribute to their capabilities, as well as the limitations that arise from their design. This foundation will help you critically evaluate LLMs—understanding both their strengths and the potential pitfalls when applying them to real-world tasks.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explainthe principles behind pretraining and fine-tuning in LLMs  
Describe how scale (data, parameters, and compute) impacts LLM performance  
Understandhow LLMs capture patterns in language through statistical learning  
Identifycommon limitations and challenges in interpreting and controlling LLM outputs  
Recognizethe trade-offs between predictive accuracy, efficiency, and reliability when deploying LLMs  
\`\`\`

L2.1 How Can We Best Use LLMs?  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In the past few years,  
LLMs have demonstrated some seriously impressive results.  
Modern LLMs can not only generate highly-fluent text,  
but also produce compelling images, music, sound, and video.  
And they can do so in milliseconds.  
This renders them a major component of almost any AI  
system used in practice today, especially when communication  
with humans is key.  
It almost gives the sense that the content they output  
is original and ready to use.  
This is why optimizing the use of LLMs  
is really important whenever AI is involved.  
In a previous lecture, we saw an introduction to LLMs.  
The goal was to understand their architecture  
and their functioning as machine learning models.  
In this lecture, we describe the key characteristics of LLMs  
that drive their impact and will likely  
shape their future development, at least until we experience  
a new AI paradigm shift.  
We will continue to try to view LLMs not as black boxes, but as  
machine learning models that are complex yet still  
understandable.  
Keep in mind that the better we understand  
their functional characteristics,  
the better we can use them.  
This is especially true, because the optimal way  
we use them while prompting them changes significantly  
as the models improve.  
So we need to continuously adapt the prompting techniques  
we use every day.  
There are no universal prompting recipes  
that work for every model and every problem.  
There are prompting techniques that we should know,  
but we must always adapt them, using  
our knowledge of the problem at hand  
and our understanding of how the AI models work.  
We begin this lecture with an explanation  
of how transformers, the technology behind LLMs,  
revolutionized AI by enabling the training of very deep neural  
networks.  
We also explain why the same ideas and technology  
can be applied not only to text, but also to images, video,  
and other modalities.  
Finally, we explain how the increasing size of models  
has changed the way we use them in practice,  
shifting from collecting data and training models to prompting  
pretrained models.  
End of transcript. Skip to the start.  
\`\`\`

L2.2 Attention  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Since the early 2010s,  
it has become increasingly clear that deep learning models can  
achieve very strong results.  
In image analysis especially, convolutional neural networks  
greatly improved model accuracy when  
it comes to object recognition and classification.  
Nevertheless, certain limitations remained.  
We could still not significantly increase  
the number of parameters by adding many hidden layers  
without making the learning algorithms much  
harder to converge.  
The concept of attention and the introduction of transformers  
offered a radical solution in this regard.  
This is the reason for the LLMs we came to know today.  
Transformers are highly efficient from  
a computational perspective.  
Moreover, they are much easier to train.  
Today, we can develop transformers  
with a practically unlimited number of parameters that are  
feasible to train in practice.  
The title of the paper that first  
introduced these technologies is quite telling  
and marks a landmark in the field--  
Attention is All You Need.  
Let's go through this idea step by step.  
We begin by exploring the motivation behind attention  
through a challenging problem in the area known  
as visual question answering.  
We are given an image in an outdoor setting depicting  
animals, trees, mountains, and other elements.  
And we are asked the question, is there  
any animal represented by more than one individual?  
If we examine the image carefully,  
the answer could be yes.  
Elephants appear more than once.  
There are three of them.  
The other animals appear to be represented  
by just one individual each.  
Indeed, this problem might be more challenging  
than we realize, since answering it requires a reasoning that  
goes beyond locality and taking multiple parts of the image  
into account.  
To answer the question, we first need  
to recognize different animals, such as elephants,  
appearing various locations, sizes, orientation, and colors.  
After recognizing that some of these objects,  
despite their differences, are similar enough  
to belong to the same species, we then need to count them.  
CNNs are not well suited for global information aggregation.  
A certain level of aggregation can  
be achieved by increasing the kernel size  
or by stacking multiple layers to expand the receptive  
field of deeper neurons.  
However, it has been proved that this is not  
enough for difficult problems, like visual question answering.  
We started our discussion with images,  
but similar principles also apply to questions about text.  
In our example, we are provided with a piece of text  
that describes how elephants live together.  
The question may request simple pieces of information  
or may require reasoning to answer.  
Words are the building blocks of texts.  
This text consists of 41 words, while others may contain  
hundreds or even thousands.  
Word relationships depend on syntax,  
where proximity plays a role, as in images,  
but this is not always the case.  
For example, what do the words "they" and "their" refer to?  
Moreover, words connect to each other,  
and the strength or importance of these connections  
varies depending on the specific words  
and their contextual relevance.  
To fully capture meaning and context,  
word-level connections need to extend across extensive portions  
of text, enabling the model to handle long-range dependencies.  
So there are no obvious methods for converting text  
into a structured representation that fully captures  
its meaning in a form suitable for neural network processing.  
This is also how human perception appears to operate.  
When asked a question about animals in a scene,  
we instinctively focus our attention  
on objects identified as animals,  
actively seeking relevant information  
rather than passively observing the entire scene.  
Given the specific image and asked the question,  
is there any animal represented with more than one individual?  
We focus on finding the answer to the question  
without processing all visual information simultaneously.  
Instead, our eyes shift between points of interest,  
focusing on the most relevant features.  
Moreover, we use contextual information and integrated with  
information we are given to understand the text,  
the words "they" and "their" should ideally be linked  
to the word elephant.  
For more complex problems that require reasoning,  
we can use context as background knowledge to guide the attention  
or to be involved in the reasoning process.  
In our example, if we know that elephants often appear  
in groups, as the text mentioned,  
we would look for multiple elephants in the image,  
as they are strong candidates for appearing  
with more than one individual.  
In summary, here's how these concepts translate  
to the field of deep learning.  
A set of neurons in a layer of the neural network  
can attend to a set of neurons in the previous layer, which  
serves as the context, to determine  
their activations based on the relevant contextual information.  
For example, if asked to count the number of elephants,  
the neurons should attend to those  
in the previous layer that represent  
information about elephants.  
If we assign a set of neurons the task of identifying  
information about the elephant, they  
should focus their attention on the neurons  
in the previous layer that encode  
information about the elephant.  
This idea is, in a way, similar to  
how convolutional layers work, where  
each neuron focuses on the local region of the input.  
In convolutional networks, attention  
is fixed and restricted to a small local neighborhood.  
This is a strong inductive bias that works extremely well  
for some problems.  
On the other hand, to solve more complex problems,  
we need more flexibility.  
We need more extensive attention mechanisms  
that can flexibly focus on any part of the input,  
even if it is not near the object.  
Somebody could say that we also do  
this with the receptive fields in convolutional networks.  
However, receptive fields in convolutional networks  
are fixed.  
It seems that we need attention mechanisms that  
are learned during training, allowing  
the model to dynamically determine  
which parts of the input are most  
relevant for the specific task.  
The key question now is how can we  
carefully and dynamically select information from a vast context?  
The solution comes from the field of databases.  
The actual information is stored in the values.  
Values represent the content of each item.  
The criteria for the selection process  
are stored in the queries.  
And the keys store the information about an item's  
relevance to a given query.  
So the keys are matched against this criteria, the queries,  
to retrieve the values.  
End of transcript. Skip to the start.  
\`\`\`

L2.3 From Attention to Transformers  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now examine how transformers use attention  
to extract the needed information from preceding  
layers to pass on to the following layers.  
In fully connected layers, the weight matrices  
map the input information to each output token,  
treating all tokens as potentially relevant.  
Learning becomes very challenging  
because the model has to figure out  
which tokens are relevant purely from the data,  
without any built-in inductive bias to guide it.  
In the elephant example, this means we cannot know in advance  
which part of the image will be relevant to our task,  
for example, recognizing elephants.  
In contrast, convolutional layers  
are built with a strong inductive bias.  
We assume that neighboring neurons are important  
and that all other neurons should be ignored.  
This idea works well for object recognition  
since neighboring pixels are, indeed, the most important.  
However, when a broader view is needed,  
such as counting the elephants in an image,  
this approach is less effective.  
Transformer layers also incorporate a strong inductive  
bias, but unlike convolutional layers,  
it is flexible and adjustable rather than being  
tied to neighboring positions.  
The way transformers adapt relies  
on the queries/keys/values mechanism, where  
each token generates a query to ask, what am I looking for,  
keys that represent what information are contained,  
and values that carry the actual information  
to be shared to the next layer.  
So values hold the actual information from the input  
tokens, the content that will be passed to the next layer's.  
Keys are learnable representations  
that capture features like numbers, colors, or attitudes  
that queries can match against, and queries  
score how well each token's content matches  
what we are looking for.  
Its output token is a weighted sum  
of all tokens, weighted by attention scores.  
The more similar the query and key are,  
the higher the attention score, and therefore, the greater  
the attention weight.  
This captures the intuition behind the computation performed  
by the attention mechanisms.  
Through this computation, we are able to bring together  
all the relevant information.  
This is a standard component of the transformer layer.  
To organize attention, we must define the information blocks  
it will process.  
For example, consider a text which  
is a sequence of characters.  
If our unit is a single character,  
the entire process would rely on the similarity between letters,  
which is not very useful.  
Of course, it's the words, not the letters,  
that convey the actual meaning.  
We must split inputs, text, images, audio, video  
into discrete meaningful units, word, subwords, image patches,  
or audio frames, so the model can process and learn patterns.  
This procedure is known as tokenization  
and produces tokens as its result.  
Tokenization occurs first before the transformer layers  
can aggregate all the important information from the input.  
The next step is to represent the tokens in a uniform way,  
so that the following layers of the neural network,  
the transformer layers, can process them  
in the same fashion.  
Words vary in length, and letters don't carry meaning,  
so we need to map them to another space.  
As seen before in previous lectures,  
every neural network layer performs such transformations,  
so we can use neural networks to encode tokens  
into a uniform vector format, a fixed  
dimensional array of numbers.  
These are the word embeddings.  
A similar process is applied to images as well.  
Every image is represented as a pixel matrix,  
such as 1,024 by 1,004.  
These pixels can be grouped into regions of the image, which  
we call patches.  
These patches serve as our tokens.  
Thus, we tokenize images by grouping pixels into patches,  
resulting in tokens instead of individual pixels.  
The entire image is then represented as a set of tokens.  
Naturally, as in the case of text,  
each token is represented by a vector, the embedding vector,  
so the representation of the whole image  
is a set of vectors, token embeddings, this time.  
Effectively, we end up with a matrix again,  
only this time it carries explicit semantic meaning.  
To summarize, whatever the input may be,  
the first step is to represent it  
in the token space, that is within the token vocabulary  
defined by the tokenizer.  
From there, some neural network layers  
map the tokens into the embedding space.  
This is a mapping that assigns each token  
to its embedding representation.  
As a result, this process produces an embedding matrix  
representing the input tokens from the token vocabulary.  
This process works in a similar way for both text and images,  
as well as for other input types such as audio and video.  
Let's examine in detail how models like GPT  
perform the embedding representation step.  
We'll leave the details aside for now  
and focus on the main intuition.  
The process begins by providing the text to the tokenizer.  
In this example, we've selected the GPT4 tokenizer,  
the well-known transformer model that we  
will cover in detail later.  
In our case, a text of 240 characters  
ends up being described using 49 tokens.  
Here, tokens almost match the words in the text.  
By examining the token IDs, we see  
that this representation relies on the tokenizer's  
predefined vocabulary.  
After that, the tokens go through an encoder,  
a neural network that maps them to their embedding vectors.  
At this stage, we can choose between a smaller or larger  
dimensional representation.  
For this specific model, the smaller embedding representation  
has a dimension of 1,536.  
This is how we end up with the representation of the sentence  
in the embedding space, which will serve as the input  
to the transformer layers.  
You can experiment with these tools  
and observe the results on different examples,  
most of which are openly available for use.  
Let's examine the process of computing output tokens  
within transformer layers.  
We recall that our goal is to transform each input  
token into a representation that captures both  
its own semantic information through its embedding,  
and the contextual information from the related tokens  
in the sequence through their embeddings.  
Let's say we are given the query,  
what is the color of the elephant?  
The yellow block in the figure represents the embedding  
of this specific query.  
Note that it is the same vector for all image patches.  
In contrast, the key token, the red block,  
varies from one image patch to another.  
The darker the red, the more similar the key is to the query.  
In fact, the key token is a learnable vector  
that represents how similar the given image token is  
to any possible query token.  
So by multiplying the query and key tokens,  
we obtain a similarity score which  
represents the attention value the output token should  
assign to that image patch.  
Consider the second patch from the left,  
which depicts the elephant.  
This part is very similar to a query, what  
is the color of the elephant?  
On the other hand, the second patch from the right,  
which depicts parts of the sky, should receive little attention  
from the output.  
The computed attention value is low,  
suggesting the lack of similarity between the query  
and the key tokens.  
Finally, we compute the output token  
by scaling each value token, blue block,  
with its attention weight and then summing across all image  
patches.  
This way, the output token gathers  
all the relevant information from the image.  
We discussed how transformer layers that take images as input  
work.  
We follow a similar process when the input is text.  
Keep in mind that transformers were first  
designed for processing text.  
Let's say we are given the text of the example.  
We are asked the question, how many animals?  
Let's see how the attention mechanism works.  
First, the input token embeddings are computed.  
In the figure, only a few tokens are displayed.  
Here, we also see the corresponding key and value  
tokens for the specific input tokens.  
All these are stored in the weights of the transformer  
as a result of the training process.  
Don't forget there is enough room in these models,  
trillion of weights.  
The query token for the specific question is also computed.  
Then the similarity checks the dot products between the query  
and the key tokens are performed to calculate the attention  
values.  
The attention values are the weights  
that we need for computing the weighted sum that  
results in the output token.  
For example, in this case, it is clear  
that the token elephants is more relevant than the token highly  
to the question, how many animals.  
As expected, multiplying the query token  
with a key token of elephants, we get a bigger attention value  
than with a key token of the token highly.  
This mechanism, which produces the attention values,  
is called self-attention.  
It forms the core of the transformer layers  
and is applied in parallel to multiple queries,  
each focusing on different aspects of the input.  
These parallel processes are known as attention heads.  
We can also see that the attention mechanism  
works the same way for both text and images.  
This is also true for other input modalities.  
The next step is to link these transformer layers  
so they can integrate information from tokens  
in different modalities.  
This is precisely the process that takes  
place in multi-modal LLMs.  
This is why, when prompting, it is  
useful to provide information that connects images and text.  
End of transcript. Skip to the start.  
\`\`\`

L2.4 The Shift in Neural Network Training and Use  
to build a model capable of performing very complex tasks  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Having seen the basic logic of transformer  
layers, let's now explore how we can stack many such layers  
to build a model capable of performing very complex tasks  
with impressive results.  
In previous lectures, we have seen  
that shallow neural networks can perform exceptionally well  
if their input features are well-crafted to accurately  
describe the problem we want to solve.  
We have also seen that deep neural networks aim  
to automatically learn such features through the training  
process.  
Transformers do precisely that.  
They gather all the relevant information  
from the input using the context and represent it  
in feature spaces where most tasks can be effectively solved.  
To achieve this, they use multiple transformer layers,  
like the ones we examined earlier.  
In these layers, specifically in the weights  
of the key query and value token blocks,  
the model stores the statistical relationships  
between all tokens and all the possible texts  
it has been trained on.  
For example, all possible associations of the token  
"elephant" with any other token are stored based on the millions  
of texts in which the token "elephant" has appeared.  
Let's now see how the input to the transformer layers  
is formed for each different type of input.  
Consider the example about elephants.  
The first step is tokenization.  
The text is converted into a sequence of tokens  
that represent the input.  
The following step is embedding.  
The input text is transformed into its embedding  
representation, and the result is the embedding matrix,  
which serves as the input to the core  
of the transformer, the series of transformer layers.  
Then, transformer layers process the input  
by focusing on the most important and contextually  
relevant information.  
Of course, to capture and store all  
these statistical associations between tokens,  
the model needs an enormous number of parameters.  
Training a network with such a vast number of parameters  
becomes extremely challenging.  
Let us recall the title of the paper that introduced  
transformers, "Attention is all you need."  
We can add now, "to scale up."  
After the transformer layers, a shallow neural network  
handles the downstream task according  
to the type of problem.  
For example, if we ask, is there any animal  
represented with more than one individual,  
the system answers with yes or no,  
making it a binary classification problem.  
Transformers are generally divided into three main types  
based on how their layers are arranged, how they are trained,  
and the nature of the tasks they are designed for.  
Encoders learn to transform large amounts of text  
into meaningful embeddings that can then  
be used to solve various downstream tasks when combined  
with a shallow neural network.  
Decoders are trained to generate sequences conditioned  
on the input text, often through next-token prediction,  
to produce fluent and contextually relevant  
continuations.  
Encoder-decoders process an input text with the encoder,  
and then generate a related output text  
with a decoder for tasks like machine translation.  
End of transcript. Skip to the start.  
\`\`\`

L2.5 Milestone Transformers  
that became a milestone in the development of transformers  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: An example of an encoder architecture  
that became a milestone in the development of transformers  
is BERT.  
BERT uses exactly the architecture we just described.  
Specifically, the tokenizer represents the text using 30,000  
tokens.  
The embedder uses embedding vectors of dimension 1,024.  
The transformer part consists of 24 transformer layers,  
each with self-attention mechanisms using 16 heads.  
The query keys and values have dimensions of 64 by 1,024.  
Finally, the shallow neural network at the last stage is  
a fully connected network with 4,096 neurons in each hidden  
layer.  
This neural network is quite large, huge for its time,  
with roughly 340 million parameters.  
BERT, together with similar transformers,  
triggered a paradigm shift in how neural networks  
were both trained and deployed.  
Until then, machine learning engineers  
trained deep neural networks from scratch  
for its application, relying on large labeled data  
sets that were often difficult to collect and curate.  
The shift that occurred during this period,  
known as transfer learning, in which the learning process was  
divided into two stages.  
The first, the pre-training, is performed on a large data set  
and focuses on training the transformer layers.  
We will discuss this later.  
The second, the fine tuning, focuses primarily  
on the shallow neural network, adapting  
the pre-trained transformer to a particular downstream task using  
a dramatically smaller labeled data set.  
Let's now explore how BERT is pre-trained.  
Training BERT's parameters demands a massive amount  
of data.  
Domain specific data sets, such as those for medical diagnosis,  
are usually too small to train transformers from scratch.  
We should use general purpose data  
sets such as massive internet text corpora.  
The key innovation here was the use of self-supervised learning.  
The advantage is that we can exploit massive data  
sets without manually annotating every single example.  
Take any unlabeled text and turn it into a learning task,  
for example by masking out words and asking the model  
to predict them.  
So the example itself provides the supervision.  
The BERT pre-training uses self-supervised learning.  
Specifically, 3.3 billion word corpus  
is used, randomly replacing a small fraction  
of tokens with mask.  
The model is then trained for one million steps,  
about 50 epochs over the 3.3 billion word corpus.  
We aim to predict each masked word  
mask using its corresponding output embedding.  
This approach proved highly effective  
establishing pre-trained BERT as one  
of the most widely adopted encoders,  
adaptable to a broad range of downstream tasks through fine  
tuning.  
Following transfer learning, a second paradigm shift  
occurred, transformer models capable of few shot learning.  
This paradigm was first introduced  
by the generative pre-trained transformer commonly known  
as GPT.  
GPT is an example of how a decoder-only transformer can  
be applied effectively to generative tasks.  
The design is similar to an encoder  
stacking transformer layers on top of learned word embeddings.  
By processing the input, the encoder  
generates a representation of the text  
that can be adapted to many NLP applications.  
GPT3 is autoregressive.  
It generates text by predicting the next token,  
adding it to the sequence, and then using  
that updated sequence to predict the following token.  
Consider the text example, particularly  
its opening segment.  
We know quite well from decades of film studies.  
These are the first nine words of the document.  
Let's assume that, in this case, each word of the sentence  
corresponds directly to a token from the tokenizer.  
The question that motivates autoregressive models  
is what is the probability to randomly write this sentence?  
From mathematics and probability theory,  
we know that this can be computed  
from the joint probability of the sentence's words,  
namely the probability to write we multiplied by the probability  
to write know after you wrote we,  
multiplied by the probability to write quite after you  
wrote we know multiplied by--  
and so on.  
If we could access every text ever written,  
calculating these probabilities would be a computationally  
demanding task.  
While the huge size of the data makes this task difficult,  
it remains a problem that can be solved computationally.  
This is exactly what autoregressive models do.  
By computing the joint probability,  
the model can identify the most probable next word.  
After adding the predicted word to the sequence,  
the model fits it back in to generate the following word,  
repeating this cycle.  
This is how the model generates text  
starting from a piece of text, a paragraph, a sentence, or even  
a word.  
Let's now look at the architecture of GPT3.  
GPT3 keeps the transformer architecture like BERT,  
but this time at a much larger scale.  
It represents its token with a more than 12,000 dimensional  
embedding vector.  
The transformer model is composed of 96 transformer  
layers, and each layer includes a self-attention mechanism  
with 96 heads.  
Queries, keys, and values have dimensions of 128 by 12,288.  
Think of the final layer as a selector,  
pushing the probability of the correct next token  
as high as possible.  
In total, GPT3 has approximately 175 billion of parameters.  
It was trained on a massive data set of about 300 billion tokens,  
working on text sequence lengths of 2,048 tokens.  
Most importantly, transformers of this scale, like GPT3,  
demonstrate remarkable few shot learning capabilities.  
This means the model no longer requires fine tuning.  
By providing more context and a few examples in the input,  
the model can produce the correct answer.  
In other words, these are general purpose language models.  
Tell the model what the problem is,  
give a few examples of a good solution,  
and the model will follow the instructions all  
through prompting.  
Transformers have been successfully applied to images.  
Once again, the architecture is very similar.  
Here, the tokenizer is based on images of 16 by 16\.  
The patches are then projected linearly  
into embeddings via learned transformation.  
The patch embeddings are fed into a transformer encoder,  
and the outputs are passed through a softmax function  
to produce class probabilities.  
The visual and transformer ViT is pretrained in a supervised  
manner on 303 million labeled images across 18,000 classes.  
After pre-training, the system is  
adapted to the target classification task  
by replacing its final layer with one  
that maps to the required number of classes.  
Although the training of visual transformers  
was especially hard at first, modern vision transformers  
have demonstrated impressive results  
and are now the state of the art.  
And of course, they have been combined  
with language transformers, and now,  
most of the models that we use are multi-modal.  
In summary, what is the take home message of this lecture?  
First, it's important to remember  
that transformers have changed how we train and use  
deep neural networks.  
Before transformers, stacking many hidden layers  
made networks almost untrainable.  
Transformers unlocked this depth.  
Transformers allow stacking almost unlimited hidden layers,  
leading to a huge increase in parameters.  
While transformers demand very large data sets for training,  
the learning process does successfully  
converge in practice.  
Key enabler, the attention mechanism.  
Fully connected layers struggle to focus on the important parts  
of the input.  
Convolutional layers exploited a powerful inductive bias,  
locality.  
This proved extremely effective for images.  
The locality bias was a good start,  
but not enough to allow very deep neural networks  
to train successfully.  
With attention, each layer can develop its own inductive bias,  
learning to highlight and combine  
the most relevant information, even over very large input  
sequences.  
Transformers not only improved performance,  
but also fundamentally reshaped the process of training  
and using deep learning models.  
Instead of relying on enormous labeled data sets,  
we train transformers in two phases,  
first, pre-training on vast, unlabeled text,  
and second, fine tuning on specific tasks  
with smaller labeled data.  
During pre-training, the model learns  
from large data sets built from web data  
using a self-supervised approach.  
In fine tuning, only the final layers  
are trained on task-specific data,  
which is tiny compared to the massive pre-training data set.  
For sufficiently large models, explicit fine tuning  
is often redundant.  
By formulating the task as a prompt  
and providing at most a couple of examples,  
the model can perform the task effectively.  
Finally, beyond the shift from training from scratch  
to transfer learning and few shot learning,  
transformers also unlocked the ability  
to use the same model architecture  
across diverse input types, including text, images,  
and audio.  
We are now at a stage where deep learning models  
can exploit all relevant data, not only for model training,  
but also for prompting modern visual language models.  
Thanks for watching.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
In this lecture, we examined how large language models (LLMs) work, focusing on attention, transformers, and training paradigms. Attention mechanisms allow models to capture long-range dependencies—such as linking pronouns back to nouns in text or aggregating features across an image—something earlier architectures struggled to achieve. Transformers operationalize this by using queries, keys, and values to direct focus, applying multi-head self-attention across many layers to store statistical associations between tokens.

We also explored how transformers reshaped training practices. With models like BERT (encoder) and GPT (decoder), pretraining on billions of tokens with self-supervised objectives became standard, followed by fine-tuning or prompting for downstream tasks. This transfer learning approach, combined with scaling to billions of parameters, has enabled LLMs to become general-purpose models that work across text, images, audio, and multimodal data.

Key takeaways:  
Attention mechanisms let models capture long-range dependencies, both in text and images.  
Transformers use queries, keys, and values to direct focus, with self-attention applied in multiple heads.  
Stacking transformer layers enables models to encode rich statistical associations across huge datasets.  
Transfer learning and self-supervised pretraining (e.g., BERT, GPT) replaced training from scratch with more efficient pipelines.  
Scaling transformers has made LLMs general-purpose models, capable of handling diverse modalities through prompting.  
Congratulations on completing this lecture\! You now have a clearer understanding of how transformers and attention mechanisms underpin LLMs, and how scaling and pretraining strategies transformed them into today’s powerful, general-purpose AI systems.  
\`\`\`

Lecture 3: Prompting LLMs  
\`\`\`  
Overview  
\`\`\`  
Welcome to Lecture 3: Prompting LLMs, taught by Professor Georgios Stamou, Professor at the School of Electrical and Computer Engineering at the National Technical University of Athens, Greece, and Visiting Professor at MIT.

In this lecture, we dive into the art and science of prompting large language models (LLMs). Prompting is the process of crafting effective inputs to guide LLMs toward generating relevant, accurate, and useful outputs. While LLMs are trained on vast datasets and contain incredible amounts of knowledge, the way we phrase a question, provide context, or structure an instruction can drastically change the quality of the response.

We will explore strategies for designing prompts, understand the impact of context and examples, and learn how prompting enables practitioners to unlock the true potential of LLMs without retraining them. By the end of this lecture, you’ll gain practical tools to make your interactions with LLMs more precise, reliable, and goal-directed.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define prompting and explain its role in extracting value from LLMs.  
Recognizethe impact of different prompt structures on model performance.  
Apply techniques such as zero-shot prompting, few-shot prompting, and chain-of-thought prompting.  
Understandthe trade-offs between concise versus detailed prompts.  
Use prompting as a method to align LLM responses with specific objectives or tasks.  
\`\`\`

L3.1 What is Prompting?  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Previously, we explored  
the key aspects of LLM design, training, and functioning.  
We also examined the features that have contributed  
to their widespread adoption.  
We show that LLMs generally follow a pretraining prompting  
approach.  
Simply put, these models are first  
trained on huge data sets gathered from the internet.  
Training them is tough, slow, and comes  
with huge computational needs.  
As a result, the process can take a long time to finish  
and comes at a high cost.  
But after they are trained, LLMs can be used in any application  
just by prompting them during inference.  
That doesn't mean using them is simple  
or that we can skip using proper methodologies.  
Anyone can ask an LLM a question and get an answer,  
but that doesn't mean they can do it well.  
They have to understand how prompting actually works.  
When it comes to prompting, there  
are established methodologies and lots  
of videos and online resources to learn from.  
LLMs evolve constantly, and each new version  
may require a different prompting approach  
to yield the best results.  
To stay future proof, this lecture  
focuses on the core LLM traits that stay  
roughly the same over time.  
Any prompting methodology should follow fundamental steps that  
stay consistent, while adapting to the advanced features  
of state-of-the-art LLMs.  
Building on what we learned before,  
we look at how to use LLMs' advanced features  
to get the best out of them.  
This is the goal of this lecture.  
First of all, we'll summarize the LLM abilities  
we've covered so far.  
Then, we'll look at additional capabilities that  
appear in very large models.  
These are referred to as emergent abilities,  
since they emerge from the model size  
and were not fully anticipated from LLM characteristics.  
You can refer to this paper for more information.  
Let's now look at the standard abilities of LLMs.  
First, LLMs can recognize patterns like, summarize this,  
or translate English to Greek, because they've  
seen millions of similar examples during training.  
These examples allow them to handle new tasks  
without the need for extra training.  
This is called zero-shot generalization.  
Second, LLMs pick up context by reading and using  
the information in the input and their \[? weights ?\] memory,  
as a result of their attention mechanism.  
And third, thanks to the large and varied data  
set they encounter, they learn to identify  
stylistic or role-based patterns.  
They then align their responses with the instruction  
they receive to emulate different styles and roles.  
Let's move on to emergent abilities.  
Among the most important when it comes to prompting is reasoning.  
LLMs are capable of a kind of reasoning,  
such as answering questions that require background knowledge  
or intermediate reasoning steps.  
That's why they can adjust their responses in real time  
when they receive feedback indicating corrections  
or refinements.  
It is important to note that these abilities emerge  
from recognizing patterns and statistical relationships  
in massive text data sets, not from true understanding  
of meaning or knowledge.  
That's why they are not comparable  
to human intelligence.  
End of transcript. Skip to the start.  
\`\`\`

L3.2 Approaches to Prompting  
So what they end up doing is engaging  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Most users think of prompting as just talking  
to the LLM.  
So what they end up doing is engaging  
in a kind of black-box communication with the LLM.  
They provide a prompt as input and receive a response.  
For example, they might ask the LLM  
to explain overfitting in machine  
learning in simple terms for a high school student.  
This prompt clearly defines the task  
and indicates the preferred style for the answer.  
The answer is pretty good and can  
be useful in the right context.  
The second example shows that LLMs have many abilities  
and can respond to more complex tasks effectively,  
as long as the instructions are clear.  
The result is quite impressive, despite the simplicity  
of the prompt.  
Clearly, prompting should be more than just  
straight communication with an LLM.  
It's really about guiding the LLM to give an answer closer  
to what we are looking for.  
Let us consider an example that illustrates the importance  
of effectively guiding the LLM.  
Imagine we want to explain black holes to someone  
who barely knows any physics.  
If we just ask an LLM, "Explain black holes,"  
the answer will be good enough, but not really the best  
for our situation.  
If we ask more specifically, "Explain black holes  
to a 12-year-old using a fun analogy,  
in 3 sentences or less," the answer gets much better  
because we've set the context and the format.  
In short, prompting is the process  
of guiding the model, typically through natural language  
or multi-modal instructions.  
Instructions like word count, tone, and context  
guide the model and make the output much better.  
Next, we look at how we organize the prompting process  
so that we can take advantage of the abilities of LLMs.  
Put simply, prompting can be described  
as the process of unlocking the abilities of pretrained models  
without the need for fine-tuning.  
This is precisely why it is essential to have  
a clear understanding of what these abilities are.  
Certain abilities are triggered quite naturally,  
while others, such as reasoning, require more advanced techniques  
that users need to learn.  
Let's consider an example.  
It is well known that LLMs struggle  
with quite basic arithmetic tasks.  
To compensate for the model's weakness in arithmetic,  
we can guide it more precisely through prompting.  
For example, we could suggest effective approaches  
like solving the problem step by step.  
To do this, we prompt the model with, "Solve this step by step--  
A museum has 245 manuscripts.  
It digitizes 3/5 of them.  
How many are digitized?"  
We see here that the model can do with the right guidance.  
Step 1, 3/5 times 245 equals blah, blah, blah, 147\.  
Answer-- 147 manuscripts are digitized.  
This is an example of unlocking arithmetic reasoning  
through prompting.  
Likewise, more complex abilities,  
like logical reasoning, can be unlocked,  
again through prompting.  
For example, let's say we prompt a model with,  
"Use logical reasoning to determine the artifact's origin  
based on the following facts.  
1-- Room A stores only Greek artifacts.  
2-- Room B stores only Roman artifacts.  
3-- Room C stores both Greek and Roman artifacts.  
An artifact is found in room A. What is its origin?"  
Since we prompt for deductive reasoning,  
we unlock logical reasoning and we get,  
"Since Room A stores only Greek artifacts,  
the artifact must be Greek," which is right.  
Of course, these kind of questions are simple,  
and most modern LLMs do in fact handle them well,  
without the need for elaborate prompting.  
However, the difference becomes much more clear  
on harder problems, where other prompts fail.  
Let's now break down prompting in a more systematic way.  
Prompting is an iterative interaction process  
aimed at unlocking the capabilities  
of pretrained models, without the need for fine-tuning.  
For this process to work, prompt engineering  
or the process of crafting the prompt we send to the LLM  
is crucial.  
It typically involves the careful design and structuring  
of prompts by formulating instructions, context, examples,  
and feedback.  
During this phase, relevant background knowledge  
may also be incorporated.  
In essence, background knowledge is  
anything we add to the prompt to help the model think better,  
stay focused, or simply get the task right.  
Then, the LLM's response is evaluated,  
potentially with input or assistance from the user.  
During evaluation, we judge whether the model's response  
meets the desired requirements, quality standards,  
and constraints, before using it.  
If the criteria are met, the response  
is evaluated as satisfactory, and the process concludes.  
Otherwise, feedback is provided to the prompt engineering phase  
to initiate another iteration, which will hopefully  
lead to an improved response.  
End of transcript. Skip to the start.  
\`\`\`

L3.3 Formalizing Prompting  
that should be included in a well-designed prompt.  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's break down what  
makes up a prompt, namely its structure and its content.  
Let's look at a simple classification task  
from cultural heritage, something researchers  
in the field often deal with.  
We want to perform an initial classification of artifacts  
based on a description that might  
appear on each item's label.  
To keep things simple, let's assume a binary classification  
problem determining whether the artifact is Roman or Greek.  
This prompt is, of course, much shorter than what we typically  
see in real application, but it still  
contains all the key elements required for it  
to work effectively.  
Let's break it down.  
The first part of the prompt outlines the task  
to be performed.  
It is crucial to state the task objective explicitly.  
We should prompt the model with something  
like, you are asked to classify historical artifacts as either  
Greek or Roman based on their description.  
That's how we guide the LLM toward the correct path  
from the beginning.  
Next comes the part of the prompt where we assign roles.  
We use role assignment to guide the tone, style,  
and scope of knowledge in the model's response.  
For example, we prompt the model with,  
you are an expert archaeologist specializing  
in ancient Mediterranean cultures.  
Provide explanations like an archaeologist would.  
Here we define the model's role, scope of knowledge, and response  
style.  
The next section is particularly important  
and significantly influences the quality of the model's response.  
Here we clearly illustrate to the model,  
through a set of good examples, what the expected answer should  
look like.  
In our case, we provide the following two examples.  
Example 1 description: a marble bust depicting Julius Caesar.  
Answer: Roman-- Julius Caesar is a Roman historical figure.  
And Example 2 description: A red figure pottery vase  
with scenes of Olympian gods.  
Answer: Greek-- red figure pottery is characteristic  
of ancient Greek.  
Our examples are clear and informative.  
This is what we call \[INAUDIBLE\] thought learning.  
The next section is also highly important,  
but it rarely seen in everyday prompts.  
However, it is crucial for result quality.  
It has been demonstrated that prompting the model  
to think in steps while solving a problem  
activates its reasoning capabilities.  
In our example, we can trigger step-by-step reasoning,  
known as Chain-of-Thought reasoning,  
by simply prompting the model with:  
think step-by-step, identify any cultural or historical clues  
in the description, then match them to Greek or Roman origins,  
and then provide the classification  
and a brief explanation.  
By outlining the steps an ideal classification system would  
follow, we essentially suggest a reasoning  
path that we know from our human experience is effective.  
And by breaking the task into sub tasks,  
we make the problem more manageable for the LLM.  
The final step is to clearly state  
the query, which must, of course, be  
consistent with the instructions and descriptions provided  
earlier.  
Description: a bronze helmet with a Corinthian design.  
Answer: the next time you use an LLM,  
try building your prompt using this structured approach.  
Knowing how to build prompts that produce accurate responses  
is a valuable skill.  
The better we understand LLMs, the better  
we get at crafting prompts that yield accurate responses.  
So, before using LLMs, we need to improve our knowledge  
about how they are structured, how they work,  
and how they are trained.  
There are three fundamental levels of interacting with LLMs.  
It's progressively more challenging.  
As the level increases, so does the potential  
for more accurate AI responses.  
Let's take a closer look at the three main levels of LLM use  
and the corresponding level of understanding required at each.  
The first level involves simple communication with the LLM  
through the standard user interface tools provided,  
like ChatGPT.  
These tools let you use long prompts and give feedback  
like in sessions, so you can apply the process we went  
through to get a good answer.  
To craft effective prompts, you need  
to design instructions that are clear, specific, and grounded  
in relevant context.  
To this end, it is very useful to be  
familiar with the fundamental characteristics of LLMs.  
First of all, we need to know how attention works in order  
to understand how the model processes information  
and why context, task description, and role  
specification are so important.  
If we know how transformers use attention  
to represent important information,  
we can better understand how the model combines that information  
to produce a response.  
This is especially helpful when diagnosing issues  
and giving feedback.  
Moreover, understanding the core architecture of LLMs  
can help in determining the most appropriate format  
for our input.  
For example, depending on the architecture  
of a multi-modal LLM, we can decide whether including images  
in the context makes sense.  
The second level involves designing  
prompts that boost LLMs reasoning abilities.  
In doing so, we guide the model toward more logical, systematic,  
and accurate reasoning, which can substantially improve  
the quality of its response.  
Don't forget, LLMs owe their success to reasoning,  
but it's also where most of their problems  
come from, like hallucination or bias.  
To improve how LLMs reason, we need  
to understand the following key points.  
How do LLMs perform reasoning?  
And why does their approach differ so fundamentally  
from human reasoning?  
What are the various types of reasoning LLMs are capable of?  
And what are the primary methods used to trigger such reasoning?  
What are the primary causes of hallucination and bias in LLMs  
that stem from their reasoning mechanisms?  
We'll dive deeper into these topics  
as we move through the presentation.  
The third level focuses on automatically  
structuring and optimizing our interactions with LLMs.  
AI engineers use this kind of prompting a lot.  
This level typically requires solid coding abilities  
and a solid understanding of AI.  
For the moment, we'll briefly cover  
how LLM embeddings are generated, how LLM APIs work,  
and how to deploy and coordinate multi-agent systems built  
around LLMs.  
Building on the prompt structure we discussed earlier,  
let's now look at the essential elements  
that should be included in a well-designed prompt.  
We begin with a well-defined task description  
that clearly specifies the task itself,  
along with its objective, intended goals, and the expected  
output query.  
We also specify the roles and point of view  
the model should take when completing the task.  
We let the model know either who it should act like  
or who it's speaking to so that its tone, level of detail,  
and style fit the use case.  
Then we provide the model with the necessary context  
to understand the task.  
Keep in mind that LLMs are trained on massive data sets,  
so most of the information we include here  
is probably already familiar to them.  
Still, it's crucial to give the model the right context,  
so the attention mechanism works effectively and focuses  
on what matters.  
Remember that the transformer layers activate  
the parts of the LLM that are most relevant to the information  
provided in the prompt.  
So we add a brief overview of the domain knowledge,  
including key facts or definitions,  
if we want the model to use them.  
We also add any external information  
we consider useful or necessary for the model  
to produce better results.  
We can include short texts, tables, images, plots  
or any other file containing structured data as knowledge.  
Then it helps to define the output  
format and any constraints.  
This steers the model toward clear and useful answers.  
It's also good to include examples of the task,  
since LLMs pick up patterns from the context  
and tend to replicate the style they see.  
The key information to remember here  
is that background knowledge, facts, context, roles,  
and instructions activate the model's internal memory  
by directing it toward the relevant statistical  
associations stored in its weights  
without the need to retrain the model.  
An effective prompt aims to get the model  
to focus via its attention mechanisms  
on the most relevant information and patterns it has learned.  
End of transcript. Skip to the start.  
\`\`\`

L3.4 Enhancing LLM Reasoning  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The next level of prompting  
is to unlock the true potential of LLMs  
by designing prompts that activate their emergent  
abilities.  
Because of their scale, LLMs go beyond  
basic statistical learning.  
They develop emergent skills like abstract thinking,  
compositional reasoning, and creative synthesis.  
This is why they often seem more intelligent  
than simple search and retrieval or classification tools.  
We don't fully understand how emergent abilities arise,  
but they likely come from the interaction of three  
fundamental properties.  
The first is the ability to construct  
highly-effective distributed representations of concepts.  
Concepts are encoded as high-dimensional vectors,  
enabling flexible recombination, similarity, and abstraction.  
The second is the attention mechanism,  
which enables the model to focus on relevant information  
during input processing.  
Transformers focus on relevant context  
to recall semantic relationships,  
not just memorize n-grams.  
Lastly, LLMs seem to build advanced statistical  
representations on top of distributed representations.  
As models grow larger, they encode, translate,  
and use more advanced statistics,  
like reasoning schemes.  
For example, if A gives B and we have A, then we get B.  
So because of their high capacity,  
LLMs can store knowledge retrieved via attention  
and use abstract processes to create new insights  
from what they already know.  
This is a form of reasoning.  
Reasoning is the process of deriving conclusions  
from facts and knowledge.  
It is the act of making implicit knowledge explicit.  
By scaling statistical and transfer learning,  
LLMs unlock reasoning abilities.  
That's how they appear intelligent rather than merely  
retrieval engines.  
Of course, LLMs don't perform reasoning like humans.  
Instead, they rely on statistical regularities  
in the data they've been trained on to generate responses.  
The reasoning we observe in LLMs comes from their massive ability  
to capture and encode logic, math, and commonsense patterns  
from their training data sets.  
That's why we need to be careful.  
What appears to be reasoning in LLMs can be misleading.  
LLMs don't actually understand or think consciously,  
so their outputs can easily be incorrect.  
Regardless of prompting, LLMs apply a kind of reasoning  
to produce outputs, and that's often  
where hallucinations originate.  
By using prompting, methods like few-shot or chain-of-thought,  
we can guide the model's attention  
toward reasoning strategies that match our task in order  
to reduce the chance of hallucinations.  
End of transcript. Skip to the start.  
\`\`\`

L3.5 Challenges with LLM Reasoning  
that can be used to activate them.  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let us now explore examples  
of different types of reasoning and prompting techniques  
that can be used to activate them.  
The first important form of reasoning to consider  
is deductive reasoning.  
We use if-then statements and known facts as premises  
to reach a specific conclusion.  
We include a specific example in the prompt.  
We aim to classify artifacts as Roman or Greek  
based on available information such as color, storage  
location, and other attributes.  
For instance, we are given the following premises.  
If an artifact is found in room A, it is Greek.  
Artifact X is found in room A. We can therefore  
derive the conclusion, artifact X is Greek.  
We guide the LLM by showing that in this case,  
it should respond with "artifact X is Greek because it is found  
in room A and all artifacts in room A are Greek."  
The LLM has access to background knowledge containing  
various details about vase A, including  
the fact that it is red.  
We can therefore expect it to use this information  
to classify vase A as Roman based on its red color.  
Note that deductive reasoning produces logically  
sound outcomes.  
When used properly, the conclusions are always valid.  
In this example, we see that deductive reasoning  
can be triggered through prompting  
techniques such as chain-of-thought and few-shot  
learning.  
Another highly useful reasoning scheme  
is abductive reasoning, which involves  
using general world knowledge and implicit assumptions  
to solve problems.  
For example, we know that the artifact is located in room A.  
Furthermore, we know that all artifacts located in room  
are of Greek origin.  
From these premises, we can infer  
that artifact X is likely of Greek origin, given  
that it was found in room A.  
It is important to note that abductive reasoning does not  
always lead to correct conclusions,  
because if you think about it, there's  
a chance that artifact X wasn't found in room A after all.  
The fact that all artifacts found in room A  
are Greek does not necessarily imply  
that all Greek artifacts were found  
in room A. It is a possibility, but not a sure thing.  
That's why when activating this type of reasoning,  
it's important to emphasize that the LLM should frame both  
its responses and its internal reasoning as probable rather  
than certain, like so--  
"artifact X is probably in room A."  
Abductive reasoning is activated here  
through the use of common prompting techniques  
like one-shot learning and chain-of-thought prompting.  
In our example, we want to verify the color of vase A.  
If we know or can infer that vase A is Roman based  
on some piece of data, then, like any researcher,  
we'd want to consider whether it might be red given  
that all red vases are Roman.  
Another very interesting reasoning scheme  
that is used to derive general patterns  
or rules from specific examples or observations  
is inductive reasoning.  
Let's explain it through an example.  
We observe that a set of objects possesses property A  
and also shares property B, so we  
conclude that objects with property A  
also have property B. Here, we apply one-shot learning  
by providing an example with the following assumptions.  
One, artifacts A, B, and C are found in room A. Two,  
artifacts A, B, and C are Greek.  
And the conclusion is, artifacts found in room A  
are probably Greek.  
Our goal is that when we ask the question "can you derive any  
rule for Greek vases," the model,  
using the information above, should answer,  
"Artifacts found in room A are probably Greek."  
This would be very useful in making explicit  
the statistical patterns or rules that  
might exist in our data set.  
For instance, we could derive this conclusion.  
"Red vases are probably Roman based on the properties  
exhibited by the artifacts we already know."  
There are many other forms of inductive reasoning.  
We focused on a specific one here  
that is known as inductive generalization,  
but similar approaches can be applied  
like statistical reasoning, causal inference,  
analogical argumentation, and others.  
Beyond logical reasoning, a major source of error in LLMs  
is their struggle with arithmetic calculations.  
It's probably difficult to program an automated system that  
can handle every type of calculation problem  
in any domain, and it becomes even harder  
when problems are expressed in natural human language.  
However, with prompting, we can reduce LLM errors  
by tapping into the mathematical reasoning they  
developed during training.  
For example, it has been shown that the combined  
use of chain-of-thought and few-shot learning  
can significantly reduce errors.  
With this technique, we start with one or more simple examples  
similar to the problem at hand and use them  
to outline the solution steps.  
Next, we carefully describe our problem,  
which may be more complex but follows the same underlying  
logic.  
This way, the model can solve the problem more effectively  
and even show the intermediate steps, allowing  
us to verify the solution.  
Similarly, by employing analogies,  
we can also partially unlock commonsense reasoning.  
Commonsense reasoning is one of the most complex forms  
of human reasoning.  
It remains extremely challenging to automate and integrate  
commonsense reasoning into machines.  
It involves evaluating properties, constraints,  
or relationships between objects to draw conclusions  
that appear obvious to humans, who naturally apply them  
when reasoning.  
However, they are far from obvious to machines.  
For example, anyone would immediately  
state that a baby can't possibly lift something  
that weighs 50 kilograms.  
We don't recall this as a memorized fact.  
It's something we infer through commonsense reasoning.  
Is it possible for an LLM to incorporate  
commonsense reasoning in the generation of its responses?  
Without commonsense reasonings, the hallucinations  
an LLM generates can be quite frustrating  
and sometimes lead to serious mistakes.  
The use of chain-of-thought supported by few-shot learning  
with analogical examples relevant to the task  
can unlock a form of LLM commonsense reasoning  
that significantly reduces hallucinations.  
Several other types of reasoning can also  
be valuable in real-world scenarios.  
Spatial reasoning deals with understanding  
spatial relationships like position, direction, and shape.  
Temporal reasoning involves analyzing  
time-based relationships, including sequences of events,  
timelines, and durations.  
Multi-hop reasoning integrates information  
from multiple contexts in order to reach a conclusion.  
Counterfactual reasoning involves alternate realities  
or hypothetical situations, those  
that did not occur but could have  
under different circumstances.  
It explores what-if scenarios and how outcomes might differ.  
Finally, analogical reasoning involves solving a problem  
or understanding a concept by identifying analogies  
with a different but structurally similar situation.  
It transfers knowledge from a known source scenario  
to a new target scenario based on similarities  
in their underlying relationships.  
LLMs have seen massive amounts of data, much of which  
reflects reasoning patterns found in real-world scenarios.  
The study of LLMs' emergent abilities  
provides strong evidence that corresponding reasoning schemes  
have been encoded within the models' weights.  
Prompting techniques like few-shot learning and chain  
of thought can unlock these types of LLM reasoning,  
leading to better answers.  
The previously discussed reasoning schemes  
are not applied just once.  
They can be activated sequentially or repeatedly  
throughout the prompting process.  
The type of reasoning and the steps taken  
are important for the accuracy and usefulness of the results.  
There are two main ways in which LLMs can reason.  
The first is vertical reasoning.  
Vertical reasoning follows a linear and rule-based path.  
Each step depends on the previous one,  
and the process unfolds logically and analytically.  
Its focus is on deepening one line of thought  
in a structured and thorough manner.  
It is typically grounded in deductive reasoning.  
The second is lateral reasoning.  
Lateral reasoning is non-linear and exploratory.  
It looks for creative or alternative paths  
instead of sticking to one logical route.  
The focus is on expanding the range of possibilities,  
promoting problem reframing and solution seeking  
through a non-sequential exploratory approach.  
Usually, it is based on inductive or analogical  
reasoning.  
When designing prompts for specific reasoning types,  
they usually relate to either vertical or lateral reasoning.  
Deductive, mathematical, spatial, and temporal reasoning  
schemes usually unlock vertical reasoning.  
On the other hand, inductive, analogical, multi-hop,  
and counterfactual reasoning usually  
unlock lateral reasoning.  
End of transcript. Skip to the start.  
\`\`\`

L3.6 Optimizing LLM Interactions  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: From the previous discussion,  
it's clear that the demonstration part of prompting  
plays a critical role in the quality of the results.  
The examples chosen for the prompt  
are a key factor in how well the strategy performs.  
Use examples that are highly relevant to both  
the nature of the task and the domain  
in which the query operates.  
Avoid using examples that are irrelevant or lack clarity.  
Use a range of examples, including  
less typical or borderline cases,  
to improve the model's generalization across the task.  
Don't repeat yourself.  
Varied examples help the model learn more.  
Cover all classes.  
Don't let one dominate your examples.  
The ordering of the examples is also critically important.  
Begin with clear, easy-to-understand examples,  
followed by slightly more complex ones  
to guide the model's reasoning process.  
Go from easy to hard.  
This helps the model learn how to generalize step by step.  
Split examples by type, like deductive, then inductive,  
so the model can follow its reasoning path more clearly.  
The way a prompt is formatted and presented  
plays a role in its effectiveness.  
Start by clearly stating the task,  
then present relevant examples, and finish with a query  
for the model to respond to.  
Use a uniform format for all input examples--  
input, reasoning steps, final output--  
as LLMs rely on consistent patterns  
to generalize effectively.  
Use clear markers like, Example 1, Example 2,  
to help the model distinguish and learn from each case.  
Be consistent-- same style, same format.  
It keeps the model and you on track.  
Incorporate chain-of-thought reasoning or intermediate steps  
within the examples to effectively guide  
the model's output generation.  
Store your templates in a database.  
It is easy to reuse and stay consistent.  
There are plenty more rules and guidelines  
we could add to boost prompting quality.  
Keep in mind that applying or deliberately avoiding  
specific rules always depends on the user and the context.  
This is why we speak of effective prompting as an art  
to master.  
LLMs often show reasoning-like behavior,  
but they still suffer from core reasoning flows that  
can unexpectedly impact their reliability,  
transparency, and trust.  
Major challenges arise due to the statistical basis  
of LLM reasoning, the absence of true semantic comprehension,  
as well as contextual limitations.  
One major limitation, often resulting from LLM reasoning,  
is hallucination.  
LLMs can sometimes produce output  
that is fluent and convincing in form,  
yet factually incorrect, ungrounded,  
or entirely fabricated.  
Such output may misinterpret the prompt or context,  
include imaginary or inaccurate facts,  
or lead to logical inconsistencies  
and incorrect conclusions.  
For example, if we ask, "Who won the Nobel Prize in physics  
in 2023 for their work on time crystals,"  
we might get the answer, "Dr. Emily Zhao and Dr.  
Michael Thorne won the 2023 Nobel Prize in physics  
for pioneering experimental work on time crystals."  
Just to clarify, the physics Nobel  
was given for work in light physics, not for time crystals.  
It was actually awarded to three other scientists,  
not to Emily Zhao and Michael Thorne.  
This example illustrates how incorrect information  
in the input, such as the claim that the prize was  
awarded for time crystals, can trigger hallucinations in LLMs.  
The most reliable mitigation strategy  
for avoiding hallucinations is to ensure accurate information  
in the prompt, and to verify the response using trusted databases  
or search engines.  
In modern AI systems, this process  
can be automated, for instance, through Retrieval Augmented  
Generation, RAG, or symbolic reasoning  
engines for factual and logical verification.  
A second significant issue associated with LLMs  
is the presence of bias in their outputs.  
Sometimes, LLMs tend to produce biased or unfair responses.  
This can be due to their training  
data, their internal design, or how they've been  
aligned with human feedback.  
LLMs are affected by multiple kinds of bias  
throughout their operation.  
Training data bias is the first and most common type,  
arising directly from the data sets used during model training.  
LLMs are trained on internet-scale corpora, which  
often reflects societal, cultural, and political biases  
embedded in the source texts.  
The second category is algorithmic bias,  
which arises from the model's architecture, training  
objective, or optimization process.  
Due to their architecture, LLMs may  
prefer responses that are statistically likely, even  
if they are not accurate or reasonable.  
And last but not least, we have user interaction bias.  
LLMs tend to adapt to user prompts and may reinforce  
the user's assumptions, a phenomenon known  
as "sycophancy."  
They often prioritize being helpful, polite, and safe,  
occasionally at the cost of factual accuracy  
or diversity of perspective.  
To mitigate bias, we can use bias-sensitive prompts,  
apply bias monitoring tools, vary  
the types of prompts we use to break repetitive patterns,  
and encourage the model to review  
its own responses for internal consistency and bias.  
We use the term "prompt engineering"  
to describe the thoughtful crafting of prompts that help  
guide LLMs toward targeted responses.  
While humans usually handle prompt creation in everyday  
practice, it's worth asking, "Could AI agents handle the act  
of prompting as well?"  
The idea is to use LLMs themselves to refine and improve  
prompts with little or no human intervention.  
The heart of the system is the meta prompter,  
a controller responsible for managing and optimizing  
the generation, adaptation, and orchestration of prompts  
for LLM agents.  
The meta prompter reasons about the prompting  
process itself, determining what to ask, how best to phrase it,  
and how to refine queries to enhance accuracy, efficiency,  
and reliability.  
The meta prompter orchestrates multiple multi-modal LLMs  
that handle various stages of the prompting process,  
including describing the problem, breaking it  
down, generating and adjusting prompts,  
as well as assessing their quality.  
It has access to background knowledge,  
but also maintains a prompt and an example repository.  
Specifically, a collection of prompt templates  
is tailored to a particular task type or application.  
And a library of examples used in few-shot learning.  
For prompt evaluation, the Meta prompter  
uses a prompt scoring system, providing  
a score for the prompt answer.  
And the symbolic AI engine Detecting  
Hallucinations or Bias.  
Meta prompters express optimization challenges  
in natural language, and guide LLMs to iteratively generate  
novel solutions by leveraging problem,  
definitions and previously, identified answers.  
One major benefit of using LLMs for optimization  
is their flexibility.  
Us changing the task often requires nothing more  
than rephrasing the prompt.  
So what is the take-home message of this lecture?  
Before LLMs and prompting. applying machine learning  
typically involved training or fine-tuning models,  
which demanded both deep technical understanding  
and considerable resources.  
Thanks to prompting, artificial intelligence technologies  
have now become significantly more accessible.  
However, this doesn't mean that prompting LLMs is an easy task.  
Just because anyone can interact with an LLM  
doesn't mean they can do it effectively.  
Knowing how to design prompts that consistently  
produce accurate answers is a highly valuable skill.  
It is grounded on a clear understanding  
of how LLMs are designed, how they function,  
and how they are trained.  
There are three levels of interacting with LLMs,  
each progressively more challenging.  
The first level involves communicating with the LLM  
through the standard user interface.  
Tools provided, like ChatGPT.  
The second, following systematic approaches  
for designing probes that unlock higher LLM abilities  
and greatly improve the quality of LLM responses.  
And finally, the third one focuses  
on how we can automatically structure and optimize  
our interactions with LLMs.  
The majority of people use only the first level of prompting,  
as they do not understand how LLMs are built and trained,  
nor do they know the methodologies  
behind effective prompting.  
AI engineers, on the other hand, use the third level  
of prompting to build LLM-based applications.  
Most people should aim for the second level  
of prompting to harness the full potential of LLMs.  
This lecture was primarily intended  
to help move us in this direction.  
Thanks for watching.  
End of transcript. Skip to the start.  
\`\`\`

Summary  
\`\`\`  
In this lecture, we explored the foundations of prompting techniques and how they unlock the full potential of Large Language Models. We examined different approaches to prompting, from simple direct instructions to structured methods that enhance reasoning. By understanding how prompts guide the model’s text generation, we learned that the quality of responses depends as much on the prompt design as on the underlying model itself.

Key takeaways:  
Prompting is the bridge between user intent and model output. The way a question or instruction is phrased strongly shapes the LLM’s response.  
Structured prompting improves reasoning. Techniques like chain-of-thought or few-shot prompting help models handle complex tasks more reliably.  
Good prompting reduces errors and biases. Careful prompt design can steer models away from vague, irrelevant, or misleading outputs.  
Congratulations on completing this lecture\! You’ve learned how prompting transforms raw language models into powerful, task-specific tools, giving you greater control over their behavior and usefulness.  
\`\`\`

Recitation 1: Exploring LLMs, Tokenization, Attention, Decoding, and Prompting  
\`\`\`  
Recitation Overview  
Welcome to Recitation 1, taught by Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.

In this recitation, we walk through how large language models (LLMs) process text, starting from raw language input and ending with generated output. We begin with tokenization, showing how text is split into smaller units and converted into numerical IDs. We then introduce embeddings, explaining how tokens are represented as vectors that capture meaning, and how positional information allows models to account for word order.

Next, we examine the attention mechanism, developing intuition for queries, keys, and values and using attention matrices to show how models combine information across tokens. We also discuss common decoding strategies, including greedy decoding, temperature scaling, top-K, and top-P sampling, and how these choices affect the quality and variability of generated text. The recitation concludes with prompting strategies, comparing zero-shot, few-shot, and structured prompts, and outlining practical guidelines for writing clear and effective prompts when working with LLMs.

The notebook used in this recitation is available at this link.

Due to potential memory issues, you are advised to not run this notebook on the server and just review the outputs.

If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Lectures covered by this recitation

Lecture 1: Foundations of Large Language Models  
Lecture 2: Understanding LLMs  
Lecture 3: Prompting LLMs  
Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.  
\`\`\`

R1.1: Tokenization  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
Welcome to today's recitation about LLMs and concepts  
that are relevant to this, like tokenization, attention,  
decoding and prompting.  
We are going to cover all of these topics,  
not in much detail, but to give you  
an idea about how LLMs work in a low-level basis  
and how we go from this to very powerful LLMs  
that we are used to use in our everyday lives,  
like ChatGPT, Gemini, et cetera.  
So we are going to start with the first concept, tokenization,  
where basically, we're going to see how models break text  
into subword units.  
Then they map them to some integer IDs  
and use those to reconstruct text.  
Embeddings are basically the next step  
of the processing inside our LLM, where the token IDs are  
actually transformed formed into high-dimensional meaning  
vectors.  
We are going to visualize how close these embeddings are.  
We are going to examine the relationships between the words,  
basically, in the embedding space.  
Then we are going to briefly go over the attention mechanism.  
And we are going to intuitively explain  
how queries, keys, and values work, what they mean,  
and how attention connects tokens by mixing information  
across them.  
Then we are going to see how attention heatmap looks like.  
Basically, this is because we want  
to visualize which words attend to which other words, and how  
this influences the modeling of each word inside the model.  
Then we are going to see how LLMs decode the representations  
they have, the final representations they have,  
in actual words and sentences.  
And we're going to compare different decoding strategies,  
like the greedy decoding, temperature sampling, top-K  
and top-P decoding methods.  
And we're going to see how each of these methods  
changes the style and creativity of the text that's generated.  
Last but not least, we're going to see conceptually  
what prompting is and what different kinds of prompting  
exist.  
And also, we are going to go through many examples  
of good and bad practice so that you can all  
see what's a good idea and what's  
a bad idea when we prompt LLMs, even on an everyday basis.  
So let's start.  
Let's dive in the content.  
I have already run the notebook so you  
can see the outputs printed.  
But, of course, you can run along if you want.  
So first of all, we are going to load our packages  
and our libraries as always.  
And after doing that, we're going  
to start with tokenization.  
So I briefly talked about it.  
But the idea is that we start from words and sentences.  
But before a transformer or, in general,  
a whole LLM can process text, it must turn words  
into some kind of numerical representation.  
So what it does is that it basically  
turns each word into a vector.  
And when we do that, the model can actually  
operate on this vector.  
So let's get a very simple example sentence.  
The cat sat.  
We have this tokenizer, right?  
Sorry.  
Yeah.  
We have this tokenizer, where, basically, we  
convert each piece of text into a certain ID.  
For example, the word "the" is mapped to the ID number 262,  
cat to 9246, et cetera.  
Inside the model, inside the first step,  
cat is literally just a number.  
And there's no meaning in these numbers.  
They're just assigned to these words.  
And they are, of course unique, such  
that each ID only uniquely maps to a certain word.  
Now, the tokenization does not just map each word  
into a certain ID.  
Not all words have a certain idea associated with them.  
Sometimes the tokens are not the full words,  
as we saw, but can be subwords.  
For example, if we have the word unbreakable,  
this would be broken in three separate subwords, un, break,  
and able, and each of them would be mapped to a certain ID.  
If there are tokens that are unknown,  
that are not in our pre-specified vocabulary,  
we match them to an unknown token, basically.  
So let's take a few words.  
And we're going to load a certain tokenizer from the GPT-2  
model, which is an older version of a generative text model.  
And we're going to use this tokenizer just  
to see to which ID each word is mapped to  
and how these words are basically broken.  
So we're going to take a look at the words cat,  
"the," unbreakable, NewYork as a single word,  
New York as two words, xylophonic,  
and the full sentence, the cat sat on the mat because it was  
tired.  
So we load the tokenizer.  
We load the tokenizer.  
We pass the text, each word, through the tokenizer.  
We get the encoded quantity, basically.  
And then we can get the ID of each of the quantity.  
And we can convert back anytime the IDs  
that we get into the initial tokens.  
And then we can also use the same tokenizer to decode the IDs  
and get back our decoded, reconstructed version  
of the text.  
So, for example, cat, as we saw earlier too, the token is cat.  
The token ID is 946\.  
And the decoded word is, again, cat.  
We do the same for "the."  
Unbreakable, as we said earlier, just  
breaks into three different subwords.  
Each of them is a certain token.  
NewYork, again, doesn't exist.  
When there is no space between the NewYork,  
the tokenizer treats it as a separate word.  
There's no NewYork word.  
The whole word is not NewYork.  
There should be a space between the words New and York.  
And that's why it breaks it in the best way it can.  
But when we provide New York as two separate words,  
you can see that these are mapped in different now tokens.  
Xylophonic is a very niche word.  
It doesn't exist in our vocabulary.  
So the tokenizer has to break it in subparts, in subwords again.  
And then the cat sat on the mat because it was tired--  
these are all the tokens.  
They are the separate words.  
Here, we don't have a break of word into subwords.  
We have the token IDs.  
And then if we reconstructed the initial sentence  
from the tokens, we get back the same sentence.  
The cat sat on the mat because it was tired.  
So that's how basically each word  
is mapped to a certain numerical ID inside the model.  
End of transcript. Skip to the start.  
\`\`\`

R2.2: How are Words Represented as Numbers?  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, as we said, this  
is not enough because there is no meaning in these tokens.  
The numbers are just assigned to the words.  
There is no relationship between them.  
But we want to represent the words in a way that  
is semantically meaningful.  
What does this mean?  
It means that we need to have representations  
so that words that are very similar in context or in meaning  
end up being very close in this representation space and words  
that are dissimilar should be far from each other  
in this space.  
So how do we go from the token IDs to the embeddings?  
Basically, the model has a large learned lookup  
table that we call the embedding matrix.  
So you can think about it as small table.  
Here, each token is mapped to a certain ID.  
And each ID is then mapped through this lookup table  
to a certain embedding vector.  
So it's as simple as for, say, the first word,  
"the," we are just looking at the embedding matrix  
at the position of the token ID.  
And this is the embedding that will represent the word "the"--  
same for the word "cat" and same for the word "sat."  
So this, of course, produces a sequence of vectors  
that we call the input embeddings.  
Now, there is another detail about finding  
the final embedding representation.  
The thing is that embeddings are informative  
and they tell the model what each word is,  
but not where it appears inside the sentence.  
So that is why, after we get the token embedding,  
we add a positional embedding that basically allows the model  
to distinguish cases where we have  
the same words but different order.  
For example, cat, sat should have a different representation  
than sat, cat in the model, even though they  
contain the exact same tokens.  
So for the final embedding, we take the token embedding  
that we extracted from the lookup table,  
and we add what we call a positional embedding.  
So this is how the embedding representation of each word  
looks like.  
And then we are ready to pass this representation  
to the rest of the model.  
Now, to give you an idea, what we are going to do  
is, we are going to just load an LLM.  
This is a BERT type model.  
You don't need to know how this works, of course,  
and what exactly it is, but it is a kind of small LLM.  
We also write this get embedding function here,  
whose goal is to return the embedding vector  
for a single-token string.  
So basically, we take the tokenizer.  
We map our token into a certain ID.  
And then we load the embedding matrix  
from the model, the input embedding matrix.  
And then we just return the representation  
for the specific token ID.  
That's what we're going to do now.  
And that's exactly what you can see here.  
So say we start with a token, cat.  
Then we extract the embedding.  
It's a 768-dimensional embedding.  
So it is a vector with 768 numbers.  
And here, we can just print out, visualize the first 10 out  
of these the 768\.  
As you can see, each of the words  
has a different representation, which makes sense.  
Now, how do these embeddings relate to each other?  
We are going to visualize where they lie in this representation  
space.  
So basically, as we said earlier,  
we want the embeddings to carry semantic information.  
So if we take these pairs of words here,  
cat and mat, cat and dog, cat and tired, the and mat,  
we expect, for example, cat and dog to be very close.  
But cat and mat or cat and tired should be less close  
compared to cat and dog.  
So what we do is, we take the representation, the embeddings  
for each of the words.  
And then we calculate what we call the cosine similarity  
between these two vectors.  
You don't have to know the math behind it.  
But basically, it is a way to calculate  
how close the vectors are, the distance between the vectors.  
So if we print this, we will see that, as we expected,  
the cat and dog pair has the highest similarity score  
between the rest of the pairs.  
The smallest is between the word "the" and "mat,"  
which makes sense because "the" is a very general word since it  
can be used before every noun, for example.  
So there shouldn't be any reason why "the" and "mat"  
should be close together.  
So we just visualize that here.  
Now let's see what happens visually on a plot.  
We are going to visualize all of these words-- cat, dog, lion, et  
cetera.  
We're going, basically, to calculate the embedding of each  
of these words.  
This embedding is 768-dimensional.  
So we're going to take the embedding.  
We're going to project this embedding in a 2D space.  
You don't need to worry about how.  
But we're going to map this in a 2D space so that we can  
visualize it easily.  
Because as you might imagine, we cannot just visualize  
a 768-dimensional thing.  
So after we mapping, after projecting these words to 2D  
space, we're going to plot where each of these words lies.  
And we're going to see whether words that we expect to be close  
together are actually close together  
and words that are not as related are far apart.  
So, again, we take the tokenizer,  
we convert the tokens to the ID numbers,  
and we use the embedding matrix, the lookup table,  
to just find these embeddings, these vectors.  
We perform PCA.  
PCA is the method that projects to the 2D space.  
And then we just use the Matplotlib library  
to plot the points.  
And we also annotate each point with the actual word  
it corresponds to so that we can understand what we're looking.  
So what do we see here?  
At the bottom right corner, you can  
see that there is a concentration of words  
that are all animals--  
tiger, dog, lion, and cat.  
And they're all kind of similarly looking animals.  
Like, they're not fish, for example.  
So, again, fish in theory should be closer to this than to other  
words, but it's a good sign that we see that all of these animals  
are mapped on the 2D space having a very small distance  
between each other.  
Similarly, on the upper-right corner,  
you can see that we have a concentration of emotions.  
So we have adjectives such as sad, happy, tired, angry.  
These are all mapped together in this 2D space.  
We could have expected mat, floor, and drag  
to be closer together.  
But what's good is that they are at least  
far from the other clusters that we observe.  
Now, this is how we move.  
I repeat.  
We start from words.  
We got the token IDs.  
Then for each token ID, we mapped to a certain embedding.  
This is what we looked here.  
And then inside the model, its embedding  
is finalized through adding this positional encoding, basically.  
End of transcript. Skip to the start.  
\`\`\`

R1.3: Attention Mechanism  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: We could have expected mat, floor, and track  
to be closer together.  
But what's good is that they are at least  
far from the clusters, the other clusters that we observe.  
Now, this is how we move.  
I repeat.  
We start from words.  
We got the token IDs.  
Then for each token ID, we mapped to a certain embedding.  
This is what we looked here.  
And then inside the model, its embedding  
is finalized through adding this positional encoding, basically.  
Now, after we show how words are actually  
represented in the models, we're going  
to move to the next part, which is, on a high level,  
how exactly transformers work and how the attention  
mechanism works.  
Before moving on, it would be good to make  
a distinction between different types of LLMs.  
So we have the decoder-only models,  
like GPT, Llama, Mistral.  
ChatGPT, for example, is this type of model.  
These models are trained to predict the next token from left  
to right.  
They are always trained to predict the next word.  
We also have encoder-only models, like BERT or DistilBERT,  
that we used to take embeddings from.  
These are not used for text generation.  
They are mostly used for getting embeddings out of the model  
that we can then use for classification.  
And by getting embeddings, I don't mean the input embeddings.  
I get embeddings at the end of the architecture  
after we have passed some layers of the deep architecture.  
It's just an encoder.  
It encodes text into embeddings.  
It is trained using masked language  
modeling, which basically means that some tokens are hidden.  
The model must predict them.  
And these tokens are not just next words or next tokens.  
So we mask words before and after.  
That's the distinction between the encoder and the decoder  
architectures.  
Decoder architectures only learn to predict the next word.  
So BERT keeps the encoder.  
It is used to get useful embeddings that  
are good for classification.  
But we are not using BERT for generation.  
On the other hand, GPT, Llama, all these models  
that we are used to use in our everyday life, basically,  
only keep the decoder.  
So they are only used for generation in the future.  
I mean one, can use them to get embeddings too.  
But their main functionality is to predict, basically,  
the next word to generate text.  
Now, moving on, after we explained the embeddings,  
we're going to take a look at how attention works  
on a very, very high level.  
And this was the beginning of the transformers, basically,  
that then led to even more advanced architectures that  
eventually led to the LLMs as we know them today.  
So the idea behind all of this is a very simple idea  
of three quantities--  
query, key, and value.  
Query basically corresponds to asking the question,  
what am I looking for?  
The key corresponds to the question,  
what information do I contain?  
And value corresponds to the question, what information  
should be passed forward?  
So for each word, you can think about it like the query  
is basically asking, what does each word  
want to pay attention to?  
The key is, what information does the word  
offer to the other words?  
And the value is the final content that we contribute  
and that we pass forward in the network.  
These are all learned.  
These are all the parameters of the network that  
are learned during training.  
Because up to this point, the input embeddings, all of this  
is fixed.  
So for each token embeddings, which  
is, I remind you, the input embedding  
and the positional encoding, we basically  
get this query, key, and value by calculating the dot  
product between the token embedding  
and these query weights, key weights, value weights, which  
are the learnable parameters.  
So the idea is that, as we said, the query  
is about what we are asking from the other tokens.  
So for each token, for each word,  
we can calculate what we call an attention score, which  
is basically a dot product between the query of this token,  
what we are asking to learn, and the keys of the other tokens.  
So basically, for each other token,  
we can calculate how much we want each information, how much  
each of the tokens wants the information that it  
gets from the other tokens.  
We ask.  
And this ask is specific for the word we are looking,  
for the anchor word we are looking.  
And we ask for what for information  
from the other token.  
So if this product is high, the current token  
finds the other token that it attends  
to relevant and close and important.  
So after calculating this attention score, which basically  
says how much out of each word I want to get,  
we use a softmax function, which basically just turns  
these scores into attention weights.  
This is basically a transformation  
that makes all of the scores positive to add up to 1  
and to basically, as before, represent how much the anchor  
token attends to each of the other tokens.  
Say, for example, we have a current token,  
and this is the attention scores for the other tokens.  
This means that our current token mostly  
attends to token number 2\.  
Now we are using these attention weights to basically,  
as we said, calculate how we are going to use the information  
to move forward.  
So basically, here, we have, as we said,  
token 2, pay 70% attention token 1, 15% attention to token 3,  
and almost no attention to token 0\.  
So we are going to multiply this with the value vector, which  
contains the actual information that we want to pass forward.  
So for each token i, we're going to use each of the attention  
weights that we have.  
And we're going to multiply this value that, again, contains also  
learnable parameters.  
And eventually, these linear combination of things  
is what is going to move forward in the next layer  
of the network.  
And that is why, basically, we are  
saying that it contains the actual information that  
gets passed.  
Because we multiply the attention weight  
with this value, and that's what proceeds in the next layers.  
This is the final new representation of token i  
after, say, the first attention layer.  
We can visualize all of these using what  
we call an attention matrix.  
So you can think about each row as the anchor word.  
And then in each row, we will see a heat map.  
But you can also just visualize the exact numbers.  
And each number shows how much the row,  
the word, the anchor word, corresponds to each  
of the other words around it.  
So basically, we're going to visualize now this attention  
matrix by focusing on a very specific sentence.  
The big, fluffy cat chased the small mouse.  
We are again using the same BERT model as before.  
We are tokenizing the sentence.  
We are passing the sentence through our model.  
And we get the attention matrices from the final output.  
We access these attention matrices.  
And we're going to focus on the second layer here.  
So focusing on this layer, we're going  
to get the attention matrix.  
We are going to get the tokens because we  
want to be able to see the tokens on both axes.  
And we are going to visualize how the attention weights look  
like.  
So, for example, here, we have the queries,  
so the anchor words--  
the big fluffy cat, et cetera.  
And here, we have the keys, the other words  
that we are attending to.  
And what do we observe?  
Obviously, the darker the color, the higher the weight.  
So, for example, you can see that the word "big"  
mostly attends to the word "cat."  
This makes sense because the word "big"  
refers to the word "cat."  
So it's good to see that among--  
and after ignoring the separator.  
That usually takes a lot of weight.  
This is the separator between consecutive sentences.  
As you can see, comparing with these lighter blue entries,  
"big" makes sense to refer to the cat.  
Because this is what it characterizes, basically,  
the cat.  
Another meaningful example is the word  
small attends to the word fluffy and cat  
but also attends to the word mouse, which is good,  
and that's what we want, because the small actually  
refers to the word mouse.  
And you can keep taking a look and playing around with this.  
And if we chose different layers,  
we could visualize how the attention matrices look  
like as we move from the first layer  
to deeper parts of the architecture.  
End of transcript. Skip to the start.  
\`\`\`

R1.4: Decoding LLM Outputs  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: OK, so basically, you can think about it  
I'm just repeating initial sentence.  
We get the token IDs.  
Each word is mapped to a certain ID,  
and then each ID is mapped to a certain embedding.  
Adding the positional encoding, we  
get the token and the final token embedding.  
And then we use these embeddings as the representations  
when we calculate this attention mechanism, which basically moves  
the information in a flow--  
yeah, basically moves information deeper  
in the network by calculating these attention  
weights which show for each token how much information we  
are going to get from the tokens around it.  
After passing through all the layers  
that the network might have, we end up  
at the final layer, where our model eventually  
needs to decode and choose the next token.  
There are multiple strategies about how to use--  
sorry, how to select the next token.  
The first and simplest one is greedy decoding.  
So for all of the possible tokens,  
the output is a probability distribution over the token.  
So basically, for each token, we have the probability  
of it being the next token, the next word.  
The greedy decoding just selects the most likely next token.  
This is deterministic.  
It is fast, but it's often repetitive and not necessarily  
the best quality text.  
Another approach is what we call temperature sampling.  
So basically, we, in the output of the model, we get the logits.  
And then we divide them by some temperature value.  
If the temperature is less than 1,  
we make the next word prediction more standard.  
And if we increase the temperature,  
we make it more random.  
So this controls how much creative  
we want our model to be.  
Another approach is the top k sampling.  
So instead of considering all tokens,  
we only keep the k most likely, and we pick out  
of this k which token we're going to generate next.  
So this reduces randomness compared to the temperature  
sampling, for example.  
And then we also have the top p sampling,  
which basically chooses the smallest set of tokens whose  
cumulative probability exceeds some threshold p that we define.  
So say the first word has a probability of 0.3,  
the next has a probability of 0.05,  
and the next has a probability of 0.04,  
and our threshold is 0.37.  
We would just keep these three words  
because it's the minimum number of words  
that if we add the probabilities,  
they exceed the 0.37 threshold.  
So we have the different techniques, methods here.  
And we can compare them.  
Only the greedy one is deterministic.  
It has low creativity, but it's very repetitive.  
Temperature has a smaller risk of repetition,  
but it's more prone to chaos in some sense  
to not making much, much sense.  
The top k, as we said, is we select  
the top however many we want.  
The top p, we consider the ones whose cumulative probability  
exceeds a certain threshold.  
So we are going to use this Distill GPT 2 model.  
It's not a very advanced model.  
It's kind of an older version, but we just have it here  
for educational reasons.  
And we're going to use these.  
We're going to, OK, load the tokenized random model,  
first of all.  
And we are going to use this generate function  
that what it does is it basically uses the tokenizer.  
It takes as input the prompt.  
It converts the prompt to the model input for the model.  
And then we use this generate function.  
We pass the inputs as an argument.  
We specify how many new tokens we want the model to generate.  
And these are just some other arguments.  
Like, you don't need to worry about them.  
But the idea is that we ask a model  
to generate a new text after the prompt that we are providing.  
So here, we're going to use this prompt which  
says artificial intelligence will transform medicine by.  
This is the prompt, and we are going  
to use this more primitive kind of LLM.  
And we're going to explore the different types of decoding  
that we talked about.  
Grading, temperature, top k, and top p--  
so the greedy decoding resulted in a sentence that  
doesn't really make much sense.  
Artificial intelligence will transform medicine  
by creating a new kind of artificial intelligence.  
This doesn't make sense.  
When we have this temperature, again, this doesn't necessarily  
have an actual meaning.  
Like, artificial intelligence will transform medicine  
by eliminating the risk of having people think differently,  
it is probably not true.  
But it looks more valid compared to the first one.  
And then for the top k where we did top 50 basically here  
and the top p which we want to choose from,  
the number of words whose cumulative probability is  
above 0.9, you can see that we get  
a bit more plausible or credible sentences, although the quality  
is still kind of low.  
It's just a model that we use for this demonstration purposes.  
Another thing that-- of course, you can also play around,  
think about how other sentence or examples would look like.  
We added another one here.  
The astronaut looked out the window  
and saw something impossible.  
So here, a black hole is actually,  
it kind of makes sense.  
The last one, which is kind of funny, the top p method,  
it says that the astronaut saw something  
impossible-- a nice shelf of ice with a little snow.  
And then this doesn't make much sense.  
It increases the randomness, as we said,  
whereas for the greedy decoding, which is deterministic,  
it kind of actually picked a very space-related set of words.  
There's no right or wrong decoding strategy.  
It depends on what our purposes are.  
But these are just different ways  
to translate the output of the model to an actual sentence  
basically.  
So--  
End of transcript. Skip to the start.  
\`\`\`

R1.5: Prompting  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: For the final part, we  
are going to focus on prompting.  
And prompting is something that you probably already use  
in your everyday life when you use models like ChatGPT, Gemini,  
and whatever other model it uses.  
And prompting has been a key skill  
for working effectively and efficiently with modern AI  
systems and, basically, LLMs.  
Good prompts can help using the LLM in many different ways.  
We can ask it to become a classifier, a summarizer,  
a reasoning engine, a tutor, a generator of structured data.  
There are so many possibilities about how we  
can use the LLMs and prompting.  
But we need to be also careful and learn  
how to prompt in the best and safest way possible.  
So here, we are first going to see some examples of types  
of prompting.  
We're going to use these LLM.  
It's called Mistral.  
It's not a very big LLM, and it's not very new also.  
But again, this is just for small examples here  
and for demonstration purposes.  
So we load the tokenizer, the tokenizer  
that comes with the model.  
We load the model itself.  
We load it, and we set it to the evaluation mode.  
We're not training it, basically, now.  
And then we define this function here,  
which is called chat Mistral, which what it does  
is it takes the messages that we want to give to the model.  
So the messages here are defined like that.  
And this is very standard when we code LLMs to generate words.  
We have this role, which is set to first the system and then  
the user, and the content.  
This is very typical.  
So yeah, we don't need to pay much attention to that.  
The prompt text is basically, we ask our tokenizer  
to apply this chat template.  
This is a function inside the tokenizer.  
We pass the messages.  
And we ask for generation.  
This is the most important.  
So the inputs are basically, we take the tokenizer.  
We put the prompt text that is written using this messages  
template here.  
And we pass this to the device which here is a GPU.  
Now, without training the model, we just  
ask the model to generate given the inputs.  
We are also giving the maximum number of tokens.  
We set this temperature parameter  
which controls the randomness of the output, the generation.  
Yeah.  
These two here generate the creativity, as we said.  
We also have the top-P parameter.  
And eventually, what we do is that after predicting,  
we use the decoder of the tokenizer  
to go back to the reconstructed text,  
basically, go back to the text.  
OK.  
So let's explore different types of prompting.  
First of all, we have the zero-shot prompting,  
and we also have the few-shot prompting.  
Zero shot is more or less what we mostly  
use in our everyday life.  
We are asking the model to solve a task without examples.  
So we have this sentence here, this review.  
The movie started slow, but the second half  
was surprisingly funny and heartfelt.  
What the zero-shot prompt looks like is,  
we basically ask the model to classify the sentiment  
as positive, neutral, or negative.  
We ask it to give us back the review.  
And this is what the model did.  
We ask it to respond with only one word.  
It didn't follow that.  
But it said it's neutral with a positive tilt,  
as the second half was praised.  
Now, this is usually how we prompt.  
We just ask ChatGPT to do something for us.  
However, what's sometimes very useful  
is utilizing few-shot prompting.  
So basically, to classify this review, instead of just giving  
the raw review and ask the model to classify the sentiment,  
we can actually give some examples first.  
That's why this is called few shot, because we give  
a few examples to the model.  
These are examples of reviews and what  
the actual label looks like.  
So this guides our model into being more loyal or faithful,  
more loyal to what we want it to do  
by giving some examples, which makes sense.  
The answer, after we gave all these examples,  
for the specific movie was that it's  
positive with a caveat for a slow start.  
So you can see that the response of the model under the two  
prompts was different.  
In the first, the model classified the movie as neutral,  
whereas in the second, it classified as positive.  
Honestly, it's hard even for humans  
to say if it's fully negative, fully positive.  
But it's just interesting to see how different prompts can lead  
to different generated outputs.  
The second type of prompts that you can see  
is chain-of-thought reasoning prompts,  
where we ask the model to solve a small problem  
and to explain in smaller steps how it went from each step  
to the other to reach the final solution.  
For example, we can ask the model  
to solve step by step a very small,  
elementary-school-level problem of how many cars  
a factory produces in each week.  
This is an example of a good prompt  
because we first instruct the model to solve it step by step  
and to clearly explain its reasoning.  
And that is important because there are many times LLMs just  
hallucinate with numbers.  
So it does all the math here, basically.  
Then another very important functionality is summarization.  
So we can use LLMs-- we can provide a small or longer text,  
and we can ask the model to summarize.  
So by doing that, we expect the model  
to just keep the most important information,  
rewrite it in fewer words.  
And that's exactly what we do here.  
We summarize into bullet points that you can see here.  
It's just two sentences, these two sentences.  
Then we have the role-based prompt  
where we are asking a model to act like it's something  
specific.  
For example, we can tell the model,  
you are a clinical data scientist.  
Explain to a hospital administrator  
how machine learning models can assist with predicting  
patient readmission risk.  
And we also give an extra instruction about the length  
of the text we want.  
When we do that, we basically try  
to generate content in a very specific context with a very  
specific potential tone and with a very specific point of view  
or angle, which is important when we want to actually  
simulate real-life situations.  
Like, you can ask a model to help you explain something  
to someone that has no experience  
or to explain the same thing to someone that  
has a very relative background.  
These two explanations should be different.  
And by doing this role-based prompt,  
we basically ensure that the model takes this into account.  
Or we hope that the model takes this into account  
as much as possible.  
End of transcript. Skip to the start.  
\`\`\`

R1.6: Good and Bad Prompting Practices  
\`\`\`  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now, just for the end,  
we won't have any more code, but I just  
wanted to go through some examples of good  
versus bad prompts that can be useful even  
in everyday life practice.  
Also, I think that this is important  
because we have started using LLMs so much--  
and they have become so good-- that I think we gradually reduce  
the quality of our prompts because we hope, or know,  
or we assume that the model will fully  
understand what we want it to do, even if we are vague  
and we don't spend much time on prompting.  
Vague or underspecified prompts I  
think is one of the most common bad-practice cases where,  
for example, if we just say, explain neural networks,  
this is too broad, no target audience,  
no depth specified, no context.  
We can improve this prompt by explaining  
to whom do we want to explain the neural networks.  
As we said, the target person matters.  
We can also give instructions, like use  
a small example, such as a network that  
classifies handwritten digits.  
We can be more specific about what we want the model to do.  
A second type is missing constraints.  
And this usually leads in a follow-up  
prompt when we realize that we haven't constrained  
the model enough to do what we wanted to do.  
A bad prompt is a very general sentence,  
like write about diabetes.  
There's no format, no purpose, no length, nothing.  
We should add some constraints to help  
the LLM create an answer more tailored to what we want.  
For example, we can say, write a concise,  
three-sentence explanation of type 2  
diabetes for a certain purpose.  
We then have ambiguous tasks, like summarize this.  
What kind of summarization do we want?  
Do we want it to be short, long?  
Do we want it to be in bullet points, in paragraph-like text?  
Or who is the target reader?  
There's no length constraint.  
This is extremely ambiguous.  
We can improve our prompt by adding a few more things.  
Summarize the following text in two  
to three bullet points for the certain purpose.  
Another example is asking for complex reasoning  
without guidance.  
So as I briefly mentioned before,  
LLMs tend to hallucinate math steps.  
So instead of just telling the model, solve this math problem,  
the same that we saw earlier, we can actually  
improve the prompt by instructing the model  
to solve it step by step to display the reasoning.  
And even the syntax sometimes might improve things.  
This is the chain-of-thought prompting we talk about.  
And this is important for the model to give right answers.  
Another type of bad practice is using prompts  
with hidden assumptions.  
For example, why are electric cars worse for the environment?  
This assumes that electric cars are worse for the environment  
and we're asking why.  
This can force the model to generate an explanation  
to match our assumption, whereas it would be better--  
and it would lead to better answers--  
if we were just keeping a more neutral prompt  
and didn't misguide the model towards a certain type  
of response.  
For example, we can improve the prompt by writing,  
compare the environmental impact of electric cars and cars  
that work with gas.  
This has both benefits and drawbacks, citing also  
typical lifecycle factors.  
This is way more informative for the model prompt.  
Another example is-- we covered it a bit earlier--  
the unclear role, the unclear perspective.  
The role-based prompts are important.  
Tell me about machine learning models in health care.  
That's extremely broad.  
There's no role, no tone.  
And the response might be too generic  
and not tailored to what we want.  
Whereas from the beginning, we can do the role-based prompting  
and say, you are a clinical data scientist.  
Explain to the hospital administrators how machine  
learning in health care works.  
Another example is prompts that makes multiple tasks  
without any structure.  
For example-- and I'm pretty sure we are all doing that.  
We can write, summarize this text,  
and also tell me if it seems reliable,  
and maybe rewrite the summary but shorter.  
This is three tasks in the same sentence.  
The model might even do all of them  
but with a worse quality of output  
or might skip one of them.  
We can just improve the prompt by a lot.  
Separate the tasks from each other.  
And basically, try to guide the model with the different steps.  
So the first step is to summarize the text.  
The second is to evaluate whether the information appears  
reliable.  
And the third is to provide an even more  
concise, one-sentence summary.  
And last but not least, there are  
prompts without examples for few-shot tasks,  
as we saw earlier.  
A bad kind of generic prompt again  
is, extract medical conditions from this text.  
So the LLM doesn't know the output format.  
If we had given examples, we would have also  
guided it into what type of format  
we want the extraction to be.  
There are no examples of these conditions,  
and there are no rules about what  
counts as a medical condition.  
We can give a more specific prompt by basically saying,  
extract medical conditions from the text,  
return them in a certain way, and use these examples  
as a guide.  
So the input is, the patient has diabetes and hypertension.  
The output is diabetes and hypertension, for example,  
in a list in the same way as we asked it  
to do with this sentence here.  
Overall, this is all for today.  
I want you to remember the key takeaways from this recitation.  
We went through the whole process, starting from raw text  
all the way to how the models represent this text, how they  
process it, how they decode it, and eventually,  
how these LLMs eventually came to be these very large and very  
practical and useful LLMs we use in our everyday lives.  
And we also explored the way we communicate with these models,  
which is prompting.  
So tokenization-- LLMs do not operate on words.  
They operate on subword tokens.  
We have tokenizers that map text to IDs.  
We have the embeddings.  
Each token ID corresponds to a learned vector  
that encodes a certain meaning.  
Similar words tend to have similar embeddings.  
And positional encodings inject the sequence order  
into the model.  
Attention is the mechanism that lets tokens look at other tokens  
and decide what information from these other tokens to use.  
Queries, keys, and values are three learned transformations.  
And the attention matrix describes  
who listens to whom, basically, by multiplying the attention  
weights with a value vector, passes  
the contextual information forward in the network.  
At the end, the model outputs a probability distribution  
over the next potential tokens.  
And there are different methods to decode the token.  
The greedy is a deterministic decoding.  
Temperature controls how creative we want to be.  
And then we have top-K and top-P methods.  
Then we also covered prompting.  
Prompts determine how the model interprets a task, basically.  
We saw different types of prompting,  
like zero-shot, few-shot with examples, chain-of-thought,  
which encourages intermediate reasoning, and role prompts,  
which shape the tone, the style, and the perspective  
of the response.  
Good prompts are clear, constrained, structured,  
and contextualized.  
Bad prompts are generic, vague, and ambiguous  
or contain hidden assumptions.  
So yeah, the overall pipeline we get from text  
to tokens to embeddings, multi-layer attention,  
next-token distribution, decoding, and output.  
This is all for today.  
I hope you enjoyed this recitation.  
And good luck with the rest of the module.  
End of transcript. Skip to the start.  
\`\`\`

Recitation Summary  
\`\`\`  
In this recitation, we traced how text moves through a large language model, from tokenization and embeddings to attention, decoding, and prompting. We examined how embeddings represent meaning, how attention determines which parts of the input influence each generated token, and how different decoding strategies affect the reliability and diversity of model outputs.

We also highlighted the role of prompting in shaping model behavior. Clear instructions, structured examples, and well-defined constraints lead to more consistent and useful responses, while poorly specified prompts can produce ambiguous or unreliable outputs. By connecting these internal mechanisms to practical usage, the recitation helps clarify how large language models function and how they can be used thoughtfully in medical and real-world applications.

Key takeaways  
Tokenization and embeddings: text must be converted into tokens and embeddings before a language model can process it.  
Attention mechanisms: models combine information across tokens based on context.  
Decoding strategies: influence whether generated text is deterministic, diverse, or conservative.  
Prompt design: guides model outputs and improves reliability.  
Model internals: understanding them helps users apply large language models effectively and responsibly.  
Congratulations on completing this recitation\! You now have a clear understanding of how large language models represent and generate text, and how choices in decoding and prompting shape model behavior. This foundation will help you use LLMs more effectively and critically as tools within the broader Holistic AI in Medicine framework.  
\`\`\`

Assignment Overview  
\`\`\`  
Overview and Learning Objectives  
Welcome to Assignment 1\! All questions in this assignment will refer to this notebook, and you should use the code and outputs in this notebook to answer these questions.

This assignment is broken up into five parts. Each question in this assignment corresponds to the part with the same number. For example, Question 2 corresponds to Part 2 in the notebook. The five parts of this assignment and the corresponding goals for each part are:

Part 1: Implement toy tokenization and inspect token IDs/decoding  
Part 2: Train a tiny autoregressive bigram language model and try greedy, top-k, top-p, and temperature decoding  
Part 3: Build a minimal scaled dot-product attention demo and visualize attention weights  
Part 4: Practice prompting strategies: zero-shot, few-shot, and chain-of-thought using lightweight, local proxies (no external APIs)  
Part 5: Apply Parts 1-4 to a large language model, loaded locally from HuggingFace  
Lectures covered by this assignment

Lecture 1: Foundations of Large Language Models  
Lecture 2: Understanding LLMs  
Lecture 3: Prompting LLMs  
If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.  
\`\`\`

Assignment Summary  
\`\`\`  
Summary  
In this assignment, you explored the inner workings of large language models (LLMs) through hands-on experiments with setup, prompting, and interpretation. You began with tokenization, seeing how raw text is transformed into token IDs that serve as model inputs. You then compared different text generation strategies, observing how decoding parameters influence outputs from deterministic completions to more creative generations.

Key takeaways:  
Prompting strategies  
Zero-shot prompts rely only on instructions.  
Few-shot prompts provide examples to guide outputs.  
Chain-of-thought prompts encourage step-by-step reasoning.  
Decoding methods: Parameters such as temperature and top-k sampling control output diversity and creativity.  
Attention analysis: Visualized how tokens attend to each other using heatmaps and row analyses, revealing how models connect words and ground later tokens in earlier context.  
Congratulations on completing this assignment\! You have gained practical experience with tokenization, prompting techniques, decoding strategies, and attention analysis—building intuition for how LLMs generate and structure language.  
\`\`\`

Module Summary  
\`\`\`  
Module Summary  
In this module, we explored the foundations of large language models, how scaling laws and transformers fuel their capabilities, and the ongoing challenges of data, compute, evaluation, and ethics. We also examined cutting-edge advances such as prompt engineering.

Key takeaways:  
Scaling up data, compute, and architecture drives LLM performance, but introduces practical and ethical challenges.  
LLMs are powerful text generators that rely on probabilistic prediction, not guaranteed reasoning.  
Evaluation requires caution due to benchmark leakage and bias in training data.  
Techniques like distillation help balance performance with efficiency, making LLMs more practical for real-world use.  
Prompting is a critical interface—allowing us to unlock reasoning and guide outputs without retraining the model.  
Congratulations on completing this module\! You’ve gained a foundation for understanding how LLMs are built, why they work, and the opportunities and challenges they create for AI applications.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.  
\`\`\`

