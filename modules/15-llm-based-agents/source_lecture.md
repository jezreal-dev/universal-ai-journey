LLM-based Agents  
\`\`\`  
Skip to main content  
Module Overview  
Welcome to LLM-based Agents\!

In this module, you’ll explore why standalone large language models are not sufficient for high-stakes, real-world applications — and how modern AI systems combine symbolic reasoning, retrieval engines, neural networks, and LLMs into integrated architectures.

You’ll begin with symbolic AI, learning how knowledge graphs, RDF triples, URIs, and ontologies represent meaning explicitly and support logical, transparent reasoning.

Next, you’ll examine compound (neurosymbolic) AI systems, where LLMs are orchestrated with retrieval and symbolic components to improve reliability, reasoning, and up-to-date knowledge.

Finally, you’ll study Retrieval-Augmented Generation (RAG) as a practical example of this integration — from chunking and indexing to semantic and graph-based retrieval, and advanced architectures like Contextual, Graph, and Agentic RAG.

By the end, you’ll understand how modern AI moves from monolithic models to orchestrated systems that combine retrieval, reasoning, and generation for more reliable intelligence.

Learning Goals  
By the end of this module, learners will be able to:

Explain the limitations of standalone LLMs.  
Describe how symbolic AI represents knowledge and enables reasoning.  
Define compound/neurosymbolic AI systems and their components.  
Explain the retrieve → augment → generate pipeline of RAG.  
Compare keyword, semantic, and graph-based retrieval methods.  
Distinguish between major RAG architectures and their purposes.  
\`\`\`

Lecture 1: Symbolic AI Engines  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 1: Symbolic AI Engines, taught by Professor Georgios Stamou, Professor at the School of Electrical and Computer Engineering at the National Technical University of Athens, Greece, and Visiting Professor at MIT.

What do recommending the right movie, disambiguating “Taj Mahal,” syncing calendars, and explaining an AI decision have in common? They rely on symbolic AI—turning messy data into shared, machine-readable meaning.

Things, not strings: Queries resolve to entities, not keywords (e.g., Taj Mahal the monument vs. musician).  
Stable IDs: URIs serve as universal identifiers so sources like IMDb, Wikipedia, and schema.org align.  
Facts as graphs: RDF triples (subject–predicate–object) capture statements; graphs reveal structure.  
Shared meaning: Ontologies (OWL) define classes and logic for consistent reasoning (e.g., romantic musical → romantic film).  
Reasoning: Rules and inference surface implied facts while maintaining consistency.  
Integration: Semantic stitching creates an entity-centric view across heterogeneous data.  
Explainability: Formal semantics support traceable explanations and compliance checks.  
Hybrid with LLMs: Symbolic layers enrich retrieval, automation, and interpretation.  
By the end, you’ll see how identifiers, vocabularies, graph-structured facts, and logic-driven inference help modern systems organize, connect, and reason across the web of data.

Learning Objectives  
By the end of this lecture, learners will be able to:

Define symbolic AI and its role alongside machine learning in compound/neurosymbolic systems.  
Describe knowledge graphs and the shift to “things, not strings” for disambiguation.  
Identify URIs as global identifiers for entities, classes, and relationships.  
Explain RDF triples (and the idea of Turtle) as graph-based fact representations.  
Explain how ontologies/OWL encode class hierarchies and axioms for shared meaning.  
Summarize automated reasoning concepts (e.g., modus ponens, materialization, transitivity) and why selective inference matters for practicality and interpretability.  
\`\`\`

L1.1 What is Symbolic AI?  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: In this lecture,  
we explore ideas and methods of symbolic AI,  
a field of great theoretical and practical impact.  
Symbolic AI is one of the two foundational pillars  
of AI development.  
It is not the primary driver of today's AI popularity,  
as the other foundational pillar, machine learning,  
in particular generative models, has delivered  
the most impressive results.  
On the other hand, it offers necessary solutions  
to practical problems, especially  
those related to model data representation and management.  
Additionally, symbolic AI is the best way  
to address many important issues related to the development  
and use of trustworthy AI.  
So it is nowadays a part of most compound AI systems,  
like the LLM-based systems that we use every day.  
In this lecture, we will explore modern symbolic AI methods  
focusing on semantic data and knowledge representation,  
management, and analysis.  
In particular, we will present knowledge graphs,  
the most efficient methods for data and knowledge  
representation and sharing on the web.  
They enable shared understanding of domain knowledge  
between humans and machines.  
In this context, we study the problem  
of automated reasoning of developing algorithms and tools  
for drawing conclusions from data and knowledge.  
We focus on methods that scale, presenting their usefulness  
and challenges related to the importance  
and difficulty of the problem of reasoning as a mental process.  
In most AI applications, it is necessary to describe  
the knowledge about the domain and the relevant data  
that we use.  
This description must be useful for the AI services we develop.  
But at the same time, it must be understandable by humans.  
This is crucial in applications where domain experts  
are involved in the process, defining  
the terminology and the rules governing the field.  
In practice, this knowledge is typically  
represented using symbolic AI in the form of ontologies,  
knowledge graphs, or if-then rules.  
The goal is to represent knowledge  
that is technically sound for AI agents  
but also intuitive, understandable by humans.  
Obviously, we cannot represent all relevant knowledge  
or collect all useful data for the application of interest.  
Usually, we have to accept that both our knowledge  
and relevant data are incomplete.  
One reason for incompleteness is that there  
are important implicit facts or rules beyond what is explicitly  
stated.  
These facts and rules are crucial for the performance  
of AI systems.  
In such cases, humans use logic to derive conclusions  
from existing knowledge through processes  
that consistently lead to reliable and accurate outcomes.  
This cognitive process is known as reasoning.  
Symbolic AI provides technologies that  
emulate this human capability.  
This technology is known as automated reasoning.  
With automated reasoning, we can automatically  
detect knowledge inconsistencies or make implicit knowledge  
explicit and, most importantly, offering  
guarantees for the correctness and completeness of the methods.  
Through the web, we can access vast amounts  
of relevant, up-to-date information.  
Without this information, AI systems  
appear outdated and lose a significant part  
of their credibility.  
Retrieving information from heterogeneous data sources  
is a challenging problem.  
To solve it effectively, automated systems  
must somehow understand the meaning of the search,  
going beyond simple string matching.  
Symbolic AI provides methods for retrieving relevant data  
by leveraging formal domain knowledge descriptions.  
These methods set a new level of effectiveness and efficiency  
in information retrieval.  
Any AI system used in high-risk applications  
must offer clear, intuitive explanations of its functioning.  
This is the most important aspect  
of transparent AI that is necessary for the use of AI,  
particularly in high-risk applications like health care.  
The symbolic AI technologies mentioned earlier  
are highly beneficial in this regard.  
Specifically, by using formal knowledge representation  
and reasoning, we can analyze the operation of AI systems,  
extracting functioning rules that  
are understandable to humans.  
At the same time, we can ensure compliance  
with recommendations or regulatory frameworks,  
enhancing the credibility of AI.  
Let's describe first some milestones  
of the development of symbolic AI.  
The foundations of symbolic AI are actually the foundations  
of AI itself, as this is where the concepts developed  
during the early stages of AI research.  
In the '50s, Alan Turing introduced fundamental concepts  
for machines that think like humans by following formal  
procedures.  
He also proposed methods to evaluate  
whether a machine mimics human thought,  
the well-known imitation game.  
These ideas were later systematized  
by numerous researchers and applied to problem-solving  
using symbolic AI.  
A milestone in this area was the general problem solver  
developed by Newell, Simon, and Shaw,  
utilizing formal mathematical logic to represent and solve  
a wide range of problems.  
In the following decades, particularly until the mid  
'80s, knowledge-based and expert systems significantly developed  
and applied in various domains.  
Here, we have to mention the first attempts to formally  
represent structured knowledge, the semantic networks,  
and the first expert systems that were based on if-then rules  
and used in medicine, chemistry, et cetera.  
Perhaps the most important achievement in the area  
was the development of automated reasoning algorithms, which  
demonstrated both the potential and limitations  
of algorithmic reasoning.  
However, some of these findings contributed to the start  
of the well-known AI winter of the '80s, which lasted more  
or less until the rise of the web.  
The web revolution facilitated the large-scale application  
of machine learning technologies.  
Moreover, the rise of the web also  
sparked a revival of symbolic AI,  
leading to modern symbolic AI engines.  
Specifically, from the millennium,  
symbolic AI systems evolved from standalone intelligence systems  
to data-driven, web-based AI services.  
A key milestone in this evolution  
was the development of the Semantic Web.  
Symbolic AI played a crucial role  
in the semantic representation, retrieval,  
and analysis of data and knowledge on the web.  
Since 2000, the ideas and technologies  
developed in the area have led to efficient management  
and access of vast amounts of information,  
primarily through the web.  
This capability has contributed to the growth of massive data  
sets as a catalyst to the rapid advancement of machine  
learning, particularly deep learning,  
which has become the driving force behind AI development.  
On the other hand, the widespread adoption  
of deep learning and AI, especially  
after 2015 and its integration into numerous applications,  
have also exposed critical challenges  
that must be addressed to sustain this progress.  
In this context, we see the emergence of complex AI systems  
that integrate symbolic AI technologies with deep learning  
models.  
This integration can occur increasingly  
through the development of neurosymbolic AI  
or through hybrid approaches, such as compound AI, which  
represent the next stage in AI development.  
So the focus of modern symbolic AI  
is to provide solutions for up-to-date information  
retrieval, automation of LLM prompting, automated reasoning,  
and the interpretation of deep learning models.  
Data-intensive services are based  
on the management and analysis of diverse data formats  
from multiple sources.  
For instance, this data can originate from physical devices  
such as sensors that capture measurements  
like biometric data, often in real-time.  
Data may also include information  
from public internet sources such as websites,  
scientific data sets, and social media posts.  
Additionally, data can be found in local databases  
such as customer records, hospital patient data, and log  
files, or internal data that include reports, analytics,  
and user surveys.  
Symbolic AI services can be used to gather, integrate, represent,  
and manipulate relevant data.  
Finding relevant data across numerous heterogeneous sources  
is challenging.  
To achieve this, an approach based on semantic understanding  
should be used rather than traditional keyword-based search  
methods.  
To achieve this, domain-specific knowledge  
should be formally represented in a way that is both human  
and machine readable, enabling its use in data integration,  
access, and analysis services.  
Automated reasoning services enhance  
these data-intensive systems by automatically drawing  
conclusions from domain knowledge  
and responding to user queries through the collection  
and analysis of relevant data from multiple sources.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.2 Modern Symbolic AI: Semantic Data and Reasoning  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's describe a simple example,  
a movie recommender that gathers and analyzes relevant data  
and knowledge from the web.  
Through the web, we can access relevant information  
that can prove highly valuable for this app.  
For example, a Google search for La La Land  
retrieves over 4 billion results.  
This vast pool of information is indeed rich,  
but it also contains a considerable amount  
of redundancy.  
It's interesting that the data is presented by Google  
in a structured format.  
This means that the search engine  
uses some type of semantics to organize the presentation  
of the results accordingly.  
Concerning the type of the retrieved data,  
we see structured data about the movie,  
like title, genre, director, actors, awards, et cetera.  
We also see unstructured data, like text, audio, images,  
or video.  
Examples include movie synopsis, scripts, audio clips, trailers,  
photos, soundtracks, and more.  
In addition, meta information about the movie--  
examples are ratings, reviews, and critics' assessments.  
Finally, some user-oriented information,  
like the user's viewing history, preferences,  
likes, and dislikes.  
Using AI services, the movie recommender  
should view this diverse array of information  
as a virtual database containing an exceptionally  
rich and multifaceted relevant information,  
especially if we see this information as entity  
descriptions rather than sets of words.  
Symbolic AI focuses on the use of symbols and rules  
to represent and manipulate knowledge.  
The goal is to emulate the way humans solve  
problems using logical representations and reasoning.  
The first challenge is the semantic data description  
that involves understanding and representing  
data in a semantically rich format using formal semantics  
like common understandable names and references to domain  
terminology.  
This involves the process of making data more meaningful  
and machine understandable by associations  
with knowledge and context.  
This allows the capture of underlying data meaning,  
making it more valuable for decision-making.  
In our example, given the data and terminology,  
we can associate terms from the terminology with the schema  
of data sources.  
The goal is to consume data terminologies  
and their associations-- here, for example,  
data from IMDb and terminology from schema.org or DBpedia.org--  
and produce useful statements with intuitive explicit meaning,  
like has director, La La Land, Damien Chazelle;  
and has author, La La Land, Damien Chazelle.  
Sometimes we find the same information  
in different data sources, for example in IMDb and Wikipedia.  
Semantic data integration technologies  
can help us combine and unify data.  
This is important since in order to make decisions,  
we first need to harmonize and interrelate  
data from different sources to enrich it.  
In this example, these formal statements  
represents information collected from IMDb and Wikipedia.  
The next step is to build technologies  
to see the vast amount of big, heterogeneous data  
as a single database and gather information based  
on the meaning of the data.  
This refers to the ability to pose possibly complex questions  
to a large and diverse set of data  
and get meaningful, context-sensitive answers.  
In this example, using semantic data representation and data  
integration, we can gather information  
about the genre of the movie, its director, release date,  
and production country.  
When analyzing data from different sources,  
we may reach conclusions that are  
based on common knowledge of the domain using reasoning.  
For example, it is evident that every romantic musical film  
is also a romantic film.  
And every romantic film is a love story.  
Taking into account this domain knowledge and the fact  
that La La Land is a romantic musical film,  
we can infer that La La Land is a love story, even if it is not  
explicitly stated.  
This is particularly important in cases  
that the recommender tries to retrieve love stories.  
Here, we understand that only through reasoning,  
we can infer that La La Land is a love story  
and give this information to the recommender.  
Symbolic AI technologies can help  
to automate this human ability and possibly  
enrich data by making explicit some implicit information.  
This is the goal of automated reasoning, which  
involves the use of computational methods  
to draw inferences by making logical deductions.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.3 Semantic Web and Knowledge Graphs  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Following the previous examples,  
the key question is, which technologies can we  
use to effectively represent data and knowledge on the web  
to facilitate a shared understanding of meaning  
among all users, including AI services?  
The original idea here is the semantic web introduced in 2001  
by Tim Berners-Lee, James Hendler, and Ora Lassila.  
Semantic information from the web  
can drive AI agents to develop services  
that facilitate human life.  
Services connected to the web can automatically  
control local devices.  
For example, they can control the volume of the entertainment  
system when the phone rings or set up appointment times  
by checking people's agendas.  
Moreover, agents can use web knowledge  
to interact with each other, providing  
services that help humans.  
For instance, a user AI agent can retrieve information  
about prescribed treatments from a doctor's AI Agent,  
looking up relevant providers close to the user's location  
and well rated by trusted rating services.  
All that, automatically.  
To achieve this objective, the W3C, the Web Consortium,  
introduced a suite of technologies  
to support the so-called web of data.  
The idea is to see the whole web as one database,  
like a brain for the humankind.  
The aim of the web of data is to empower computers  
to perform valuable tasks and foster  
the development of systems that facilitate  
trustworthy interactions across the web.  
With the semantic web efforts, W3C  
envisioned a network of linked data.  
Semantic web technologies empower individuals  
to publish data on the web, construct vocabularies,  
and formulate rules for managing and publishing data  
and terminologies.  
To fulfill this vision, W3C developed  
standards and technologies for data representation,  
vocabulary building, data querying,  
and application development.  
For instance, in sectors such as--  
for instance, in sectors such as healthcare, life sciences,  
and government, integrating decision making capabilities  
into clinical research using semantic web technologies  
can connect diverse forms of biological and medical  
information across different institutions.  
Almost a decade later, following extensive research in the field,  
Google introduced groundbreaking ideas  
that revolutionized how its web search engine represents  
and accesses data.  
The fundamental technology of these innovations  
is known as knowledge graphs.  
It describes a novel approach where information in the web  
is no longer represented as simple strings but as things.  
This departure from merely matching keywords to queries  
was a significant shift.  
Knowledge graphs allow users to search for people, places,  
cities, sports teams, buildings, movies, and more,  
instantly retrieving relevant information.  
This was a crucial step in building the next generation  
of search engines and other web services,  
forming the foundation of the web's collective intelligence  
similar to human understanding.  
For instance, consider a query like Taj Mahal  
in previous search engine versions.  
Taj Mahal might have been treated as a keyword--  
actually, two words.  
So search engines look for Taj Mahal  
appearing in a web document.  
However, Taj Mahal can refer to the monument, the musician,  
the Casino in Atlantic City, or a restaurant.  
This ambiguity is the main problem of keyword-based search  
engines.  
Using knowledge graphs, the search engine  
can predict the entity most relevant to the user query,  
significantly advancing web level operations.  
The key concept behind this innovation  
was labeled as things, not strings.  
Today, knowledge graphs incorporate  
all web of data technologies in an effort  
to harness diverse, dynamic, and large-scale data collections.  
The primary objective of knowledge graphs  
is to organize and connect data, facilitating a deeper  
understanding and analysis of the information published  
on the web.  
Data provide information about entities,  
so formally naming entities and providing reference to them  
is very important.  
Here is the Wikipedia description of the film La La  
Land.  
It provides helpful information in English  
accessible to English-speaking readers.  
In this text we find various entities, such as individuals,  
movies, or cities.  
Examples include Emma Stone, Whiplash, and Los Angeles.  
Some of these entities are widely recognized  
while others may be lesser known.  
If we examine closely, we'll notice  
that many of these entities have hyperlinks  
connected to their names or relevant text strings  
with other web pages or sources of information.  
For example, there are hyperlinks  
that lead to other Wikipedia articles, IMDb  
pages, or GeoNames entries.  
Although these hyperlinks may look different,  
they share a similar technical structure or format.  
These lengthy strings serve as references to resources,  
defining the specific entities and providing information  
about them.  
They are more informative than the name  
of the entity in English.  
Actually, this is a universal approach of identifying things  
through the web compared to the more restricted,  
natural language names in one of the many natural languages  
of the world.  
Every entity of the world has a web name.  
It is considered as the web resource.  
These names are represented by the Uniform Resource  
Identifiers, the URIs.  
A URI is a unique sequence of characters  
that formally identifies a logical or physical resource.  
URIs can be employed to identify a wide range of entities,  
including real-world objects, like people and places,  
abstract concepts, or informational resources  
such as web pages and books.  
Examples of URIs include URLs, email addresses, book ISBNs,  
telephone numbers, et cetera.  
While some URIs provide access to resources  
via the internet, e.g, by clicking the hyperlink,  
others do not.  
The most common approach to formally describing things  
is by categorizing them into relevant classes.  
In the Wikipedia article of our example,  
we can see several references to classes  
ranging from general categories such as city script or film,  
to more specific ones like romantic musical film or jazz  
pianist.  
Similarly to the entities, some of the classes have their URIs.  
Examples of URIs are hyperlinks to other Wikipedia resources  
that provide more detailed descriptions of the class.  
See, for example, the romantic musical film.  
Given that romantic musical film is a movie genre,  
and movie genres play a crucial role in movie recommendation  
systems, one would expect to find a comprehensive movie  
genre terminology somewhere on the web.  
Indeed, detailed movie genre classifications  
can be found in IMDb, Wikipedia, and other sources.  
These classifications often provide  
names of classes, that is, the terminology of the domain,  
as well as the information about how specific classes relate  
to each other, for example, as subclasses  
of more general classes.  
This is a first example of terminological knowledge  
representation that may be used by automated reasoning.  
For example, the subclass relation  
of love story and romantic film lead to the conclusion  
that every romantic film is a love story.  
These formal representations of classifications  
are referred to by various terms,  
including terminologies, hierarchies, taxonomies,  
and ontologies.  
They all serve to organize and categorize  
information in structured ways or as we formally  
say, to provide specifications of conceptualizations.  
Until now, we described how we formally  
assign names to entities and classes using URIs.  
The next step is to link entity names to class names,  
connecting entity URIs to class URIs.  
This is the formal representation  
of categorizations.  
Moreover, we generalize that to describe not only relationships  
between entities to classes but also between entities  
to entities or classes to classes.  
In this description of La La Land,  
there are many natural language references to relationships.  
For instance, the is-a relationship  
signifies categorization La La Land is a romantic musical film.  
Other relationships relate films to directors,  
awards to actors, individuals to universities,  
filming locations to places, and so on.  
Examples are written by, directed by, appear in,  
et cetera.  
All relationships have their own names and descriptions  
on the web as web resources using, again, URIs.  
The link is to a web resource that formally  
defines the relationship.  
Semantic references to entities, classes, and relationships  
using URIs function similarly to words in natural language.  
However, in this case, the meaning of the reference  
is explicitly defined rather than relying  
on human interpretation.  
When we use words in natural language,  
their meaning exists in our minds  
if we understand the language.  
We share this meaning as long as we speak the same language.  
With web resources, the meaning is explicitly defined.  
It is embedded in the URI, which may be more complex but far  
less ambiguous than words.  
Just as words are combined to form meaningful sentences,  
we will now explore how URIs are structured to formally define  
conceptualizations.  
For example, we can formally represent information  
such as La La Land is a romantic musical film by simply putting  
together three URIs by just writing a triple of their URIs.  
Bringing everything together, the only missing piece  
is a way to represent triples of URIs.  
A natural way to model them is as a graph, where  
nodes represent entities or classes,  
and edges represent the relationships.  
This is formally represented using the resource description  
framework, RDF, the W3C standard web language  
for describing and exchanging data and knowledge.  
RDF offers a universal language, or more precisely,  
a standard model for data and knowledge exchange  
across the web.  
Despite their simplicity, RDF descriptions  
are highly expressive, providing elegant and intuitive methods  
for formally exchanging conceptual specifications  
on the web.  
In this manner, the majority of human understandable  
descriptions found in Wikipedia can be represented in a graph  
form using RDF syntax.  
For instance, the information provided by the sentence,  
La La Land is a romantic musical film directed  
by Damien Chazelle, can be represented  
by a graph containing two triples.  
Using RDF, we can formally represent declarations,  
as we do with natural language descriptions.  
Of course, we cannot represent all information of the text  
in the simple triple form.  
The reason is that human language expressivity far  
exceeds that of any formal knowledge representation  
language in AI.  
On the other hand, when exchanging conceptualization,  
thoughts, and knowledge, greater expressivity often introduces  
ambiguity, and ambiguity brings complexity, confusion,  
and misconceptions.  
Humans have the ability to handle misconceptions,  
whereas machines, at least for now, do not.  
So when designing a language to share knowledge with machines,  
simple is beautiful.  
The key question now is whether even the limited expressivity  
of triples can still be used to represent  
more complex knowledge, not just classification or relationships  
between entities but also the axiomatic knowledge of domain.  
For instance, it would be valuable to encode  
knowledge such as anyone who has directed a film is a director.  
A film cannot be both a thriller and a family movie.  
Any film that has won a major award  
is widely recognized by the general public.  
To address this, W3C has developed an additional language  
that builds on RDF, enhancing its expressive capabilities  
for representing various forms of axiomatic knowledge.  
It is the web ontology language, OWL.  
It is important to highlight that all OWLs expressive  
capabilities are grounded in formal semantics,  
ensuring the elimination of ambiguity.  
Additionally, OWL is supported by automated reasoning tools,  
which leverage its axioms to infer new knowledge.  
Knowledge created using OWL can be published on the web  
and become shared knowledge accessible to those developing  
AI services.  
This structured knowledge is commonly  
referred to as ontology.  
Examples include general ontologies  
such as DBpedia, which transforms Wikipedia  
descriptions into a structured, standardized format, SNOMED,  
which captures and organizes complex medical knowledge,  
et cetera.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L1.4 Reasoning with Knowledge Graphs  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now let's explore how inference algorithms  
can automatically process semantic data and knowledge,  
uncovering additional information that is implicitly  
contained within them.  
Let's begin with the formal representation  
of the information explicitly stated  
in the first sentence of our example description.  
Specifically, a set of facts is represented  
in the form of triples.  
These structure representations are  
referred to as the semantic data of our description.  
Besides representing them as triples,  
we can also visualize them as a graph, which is often  
more intuitive for humans, especially when dealing  
with small-scale semantic descriptions.  
Additionally, we can define terminological knowledge  
that describes the domain in a structured manner.  
This knowledge can include axioms  
that define concept hierarchies and axioms that  
describe relationships between concepts within the domain.  
Finally, we can examine the formal representation  
of this knowledge in RDF format, specifically  
using the Turtle file format.  
Every Turtle file can be read by machines  
and represented in the form of triples or as a graph.  
Here, we can observe that this RDF specification utilizes  
URIs from well-known terminologies,  
such as DBpedia and schema.org.  
Now let's explore how a symbolic reasoner operates  
processing knowledge.  
It takes as input the knowledge we previously examined,  
which serves as the formal description of the domain,  
operating in various ways.  
First, it can verify whether the given knowledge is consistent.  
Second, it can take a property that certain entities may  
possess and return the entities in the knowledge base  
that satisfy it.  
Moreover, it can evaluate a hypothesis  
for a specific entity or a specific property  
and determine whether it holds or not.  
Or it can verify whether two entities are connected  
by a specific relationship.  
All these tasks, and many more, are automated reasoning problems  
that symbolic AI reasoners can accurately solve.  
Let's see a specific example.  
The reasoner takes the following question as input.  
Is La La Land a love story?  
And answers yes or no.  
If the assumption is La La Land love story is  
an explicit fact of the knowledge base,  
then the answer is obviously yes.  
If not, we must follow a sequence of systematic steps  
that correspond to rigorous reasoning  
processes to ensure accuracy.  
These processes may involve one or more facts  
combined with one or more rules from the knowledge base.  
To ensure guarantees, the conclusions  
must be logically sound and self-evident.  
In other words, a sequence of deriving logically evident  
conclusions can ultimately lead to a final conclusion that  
may not look obvious at first, just like in human reasoning.  
In our example, the first step involves a specific fact  
and a rule.  
In this case, the fact is La La Land is a romantic musical film.  
And the rule is all romantic musical films  
are romantic films.  
Their combination leads to an obvious conclusion.  
La La Land is a romantic film.  
This conclusion represents a fact  
that is implied by the knowledge,  
although it is not explicitly stated.  
Since this is a logically sound conclusion,  
we can now insert it, expanding our knowledge base.  
In the second step, we follow a similar process.  
We use again a fact and a rule, but the fact now  
is the one that we added in the previous step.  
So we now know that La La Land is a romantic film.  
And thus from the rule all romantic films are love stories,  
the obvious conclusion is that La La Land is a love story.  
This conclusion not only expands our knowledge base  
but is also the answer to the question under consideration.  
Let's now recap and generalize the process.  
Reasoners derive new knowledge out of existing ones,  
making implicit knowledge explicit.  
To do this, they apply knowledge derivation rules,  
many times the conclusions of which are logically  
sound and self-evident.  
The rule applied in both steps of our example  
is intuitive and logically sound.  
If an entity x has a property a and the property a implies  
a property b, then the entity x has the property b.  
This is a version of a well-known and widely used  
logical implication rule called modus ponens.  
A similar logical implication rule  
can be applied to extend knowledge graphs.  
In this case, we are looking for a subgraph pattern, where  
a node x has an is-a successor.  
That is a.  
Then the rule a gives b can be applied and add an is-a edge  
from the node x to the node b.  
This implication process is referred to as materialization.  
Through the process of materialization,  
knowledge graphs can be expanded by adding logically inferred  
information, ensuring that the newly incorporated data remains  
correct and consistent.  
For example, by applying the materialization rule  
we discussed in the example knowledge graph,  
in the first step, we can add an edge between the node La La Land  
and the node Romantic Film.  
In the second step, we can similarly  
add an edge between the La La Land node and the Love Story  
node.  
These materialization rules are not  
the only ones that can be applied  
for the logical expansion of knowledge graphs.  
We can define many more knowledge derivation rules  
based on logical inference to further expand  
and enrich knowledge graphs.  
For example, beyond the simple extension rule  
that led us to add an edge between the La La Land  
node and the Love Story node, as previously demonstrated,  
we can define a rule that links the relationship  
between a node x and a node y with a property  
that belongs to node y rather than node x,  
as in the previous case.  
As an example, consider the implication rule  
that connects the has directed relation of a node x  
with a node y with a categorization of y to director.  
This seems obvious, and if we apply this implication rule  
to the fact La La Land has director Damien Chazelle,  
we get the conclusion that Damien Chazelle is a director,  
not explicit in the knowledge graph--  
intuitive and useful.  
There are additional materialization rules  
that are less obvious.  
For example, some relations may be transitive.  
This means that if a node x has a nar successor y and this nar  
successor has a nar successor z, then z  
should be also an nar successor of x.  
This implication rule may be extremely useful in practice,  
especially when considering relations  
that have this property.  
And there are plenty of them.  
As an example, consider the class-classmate relation.  
We read in the Wikipedia description of La La Land  
that Damien Chazelle, author and director of La La Land,  
was a classmate of Justin Hurwitz that scored La La  
Land at Harvard University.  
It is reasonable to assume that a classmate of Justin Hurwitz  
is also a classmate of Damien Chazelle.  
This is a materialization of the knowledge graph  
that makes sense.  
On the other hand, there is a tricky point here.  
Of course, there are many classmates of Justin Hurwitz.  
Naming and introducing the knowledge graph, some of them,  
and applying the transitivity implication rule,  
we may come up with many implied relationships.  
This is an example why reasoning is a challenging problem.  
Summarizing, although many knowledge derivation rules  
can be applied in practice, and all of them  
may be useful in some use-case scenarios,  
sometimes there are many irrelevant conclusions  
that can be derived from knowledge bases  
using these implication rules.  
This can make the reasoning problem  
unnecessarily impractical.  
This is the reason why symbolic AI  
reasoners should be selective.  
Sophisticated automated reasoning algorithms  
for knowledge graphs should materialize  
only useful conclusions given the user query.  
The good news here is that there are  
many scalable, sophisticated reasoning services that  
can be used in practice to support knowledge graph  
expansion and be used in real-life applications.  
So what is the take-home message of this lecture?  
First, symbolic AI can be leveraged to represent  
semantic data and encode domain knowledge  
in a structured and interpretable manner.  
Second, with symbolic AI, we can efficiently access  
and analyze relevant data based on services  
like data semantification, data integration, data enrichment, et  
cetera.  
Third, there are various successful methods, standards,  
and tools for representing data and knowledge on the web.  
Specifically, these tools and standards  
facilitate the naming, categorization,  
and interrelation of entities on the web,  
enabling domain descriptions that are both accessible  
and machine understandable.  
Fourth, symbolic AI reasoners can transform implicit knowledge  
into explicit knowledge, making hidden relationships  
and logical conclusions computationally accessible.  
And the last message--  
automated reasoning is a challenging problem.  
We should be selective and employ sophisticated strategies  
to prevent the materialization of trivial or irrelevant  
knowledge.  
And this ends the presentation.  
Thanks for watching.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture introduced symbolic AI as a core pillar of AI focused on semantic representation and automated reasoning, explaining how knowledge graphs and ontologies enable machines (and humans) to share, retrieve, and trust information—especially in high-risk settings.

Key Takeaways:  
Why symbolic AI matters now: Complements ML/LLMs by improving knowledge representation, data integration, up-to-date retrieval, and trustworthy/transparent AI (rules, compliance, explanations).  
Knowledge graphs: Represent web information as entities (“things”), not keywords (“strings”), reducing ambiguity (e.g., “Taj Mahal” as multiple entities).  
Semantic identifiers: Use URIs to uniquely name entities, classes, and relations, making meaning explicit and machine-readable.  
RDF triples → graphs: Facts are stored as (subject, predicate, object) triples (often visualized as graphs), enabling scalable linking across sources.  
Ontologies (OWL): Add domain rules/axioms (hierarchies, constraints) on top of RDF for richer, unambiguous knowledge sharing.  
Automated reasoning: Derive implicit facts from explicit ones (e.g., romantic musical → romantic → love story) via logical rules (e.g., modus ponens, transitivity).  
Selectivity is key: Naive materialization can explode into irrelevant inferences, so practical reasoners must focus reasoning on what’s useful for the query while checking consistency.  
\`\`\`

Lecture 2: Beyond Monolithic AI Systems  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 2: Beyond Monolithic AI Systems, taught by Professor Georgios Stamou, Professor at the School of Electrical and Computer Engineering at the National Technical University of Athens, Greece, and Visiting Professor at MIT.

What do diagnosing pneumonia from a chest X-ray, checking a patient’s chart for the latest guideline, and chatting with an AI that cites sources have in common? They all rely on compound AI systems—not one giant model, but LLMs woven together with retrieval and symbolic reasoning.

This lecture introduces beyond-monolithic AI in a nutshell:

From monoliths to systems: Combine specialized models (LLMs, vision nets, symbolic engines) to meet real-world demands.  
Live knowledge, not stale: Search & retrieval bring in up-to-date data from sensors, the web, local DBs, and knowledge graphs.  
Prompting as an automated service: In-context learning, chain-of-thought, prompt chaining, reusable templates, and even optimization (RL/genetic/gradient/Bayesian) make prompts robust.  
Reasoning you can trust: LLM “reasoning” is statistical; symbolic reasoning offers guarantees when facts/rules are formalized; neurosymbolic blends both.  
Operate the system: Deployment needs orchestration, monitoring, careful data pipelines, plus security, reliability, accountability, interpretability.  
The impact? By orchestrating retrieval \+ prompting \+ reasoning, modern AI delivers fresher, clearer, more dependable answers—tackling tasks that a single model can’t.

Learning Objectives  
By the end of this lecture, learners will be able to:

Contrast monolithic vs. compound AI and explain when hybrid systems are needed.  
Identify core services to automate—search/retrieval, prompt engineering, and reasoning—and justify online, real-time retrieval from sensors, web, local/proprietary data, and knowledge graphs.  
Apply prompting techniques: in-context (zero-/few-shot), chain-of-thought, and prompt chaining; leverage templates and basic prompt optimization.  
Distinguish LLM statistical “reasoning” vs. symbolic reasoning; define deductive, inductive, and abductive reasoning and choose appropriately when guarantees are required.  
Diagnose reasoning pitfalls using the La La Land constraint and debtor conditional examples; propose fixes (role-play prompts, symbolic checks).  
Outline system patterns and deployment needs: RAG, multimodal and neurosymbolic setups; plus orchestration, monitoring, data pipelines, and security/reliability/interpretability.  
\`\`\`

L2.1 From Monolithic to Compound AI Systems  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Over the past five years,  
LLMs have achieved impressive results  
and are now widely used, playing a key role  
in the adoption of AI.  
One reason is the enhanced human-AI communication.  
Chatbots powered by LLMs provide human-like interactions.  
LLMs produce very fluent, textual output,  
creating the impression of generating original content that  
is ready to use.  
This creates a growing demand for AI  
to operate across a wider range of applications.  
However, no standalone monolithic AI model  
is sufficient to solve all problems on its own.  
For the next generation of AI, multiple models  
should be integrated.  
In this lecture, we will explore key aspects  
of building AI systems that extend  
beyond monolithic architectures.  
Generative AI has become the primary approach  
for AI-driven problem-solving.  
For example, LLMs act as the core component  
in AI systems development.  
On the other hand, generative AI possess certain limitations  
that restrict its applicability in many practical scenarios.  
Here, we highlight some of the key limitations.  
First, generative AI is computationally demanding.  
For example, it is challenging to deploy  
LLMs on local computers.  
Even when LLMs are open and available to install locally,  
they require supercomputers just to generate a response  
to an input.  
Moreover, training or extensively fine-tuning LLMs  
is practically unfeasible for many users,  
as it demands vast data and large-scale infrastructures.  
This problem introduces significant limitations.  
For example, in practical settings,  
LLMs often rely on outdated information,  
which can limit their applicability  
in many real-world scenarios.  
To optimize the performance of LLMs in practical applications,  
we rely on the prompting process.  
Although prompting can greatly enhance the performance of LLMs,  
potentially mitigating some of the issues mentioned earlier,  
it currently remains a manual ad hoc process.  
LLMs excel in text analysis and generation.  
But we need to combine them with other models  
in applications that require analyzing  
other types of information, such as images, videos, and drawings.  
An additional concern is that LLMs often generate  
inaccurate information, presenting it  
in a convincing manner.  
For example, they may provide incorrect dates  
within an otherwise accurate and fluent description  
of a historical event.  
Identifying these inaccuracies is challenging, precisely  
because LLMs are fluent, making their responses appear credible  
even when incorrect.  
This phenomenon, known as hallucination,  
significantly limits the use of LLMs  
in domains where information accuracy is critical.  
On top of that, LLMs struggle with reasoning.  
While they generate well-structured text,  
they often fail when required to follow logical steps  
to reach a decision.  
Combined with their fluency, these reasoning errors  
become difficult to detect, like hallucinations, making  
them even more problematic.  
This is one of the biggest challenges in AI  
as we focus on the transition to trustworthy AI.  
When using AI in high-risk applications,  
such as medical diagnosis, where transparency and explainability  
are required, AI reasoning with guarantees is a prerequisite.  
For all these reasons, it is clear  
that monolithic AI does not fit all.  
Let's examine how we can combine different AI models.  
Modern AI applications process multimedia data  
in various forms collected from sensors, databases, reports,  
the web, and other sources.  
For example, in medical applications,  
patient data may include biometric measurements,  
diagnostic test results, MRIs, X-rays, EEGs,  
and other medical records.  
Additionally, domain knowledge is often available  
and can be recorded in documents, papers,  
or structured formats such as ontologies and rules.  
This knowledge may include health system reports,  
clinical guidelines, standardized terminologies,  
regulations, scientific publications,  
and other domain-specific resources.  
Different types of AI models are trained, adapted, developed,  
and deployed based on this data, depending  
on the type of data and the specific tasks  
the models need to perform.  
For example, LLMs are used for text analysis and production.  
Deep neural networks are used for image and video analysis.  
Symbolic AI engines are used for knowledge-based data analysis  
and reasoning.  
The different characteristics of AI models  
are useful in practice.  
LLMs dramatically improve human-AI interaction,  
for example in collaboration with doctors  
in medical diagnosis support systems.  
Symbolic AI systems can address challenges  
related to the interpretability of deep neural networks  
and the integration of up-to-date knowledge  
into AI applications, and so on.  
For this reason, the focus is on AI systems  
that combine AI models creating hybrid systems that  
leverage the strengths of multiple methodologies.  
In this way, AI systems can now handle tasks  
closer to human capabilities, expanding  
the scope of AI applications.  
To enhance the integration of multiple AI models,  
many services should be automated.  
For example, search and retrieval  
allows for contextual understanding  
and the aggregation of up-to-date information.  
Prompt engineering enhances the performance and reliability  
of LLMs.  
AI reasoning may provide explanations,  
detect hallucinations, and verify  
the correctness of AI models.  
Automating these services that work  
as intermediates facilitates AI model integration.  
For example, prompt engineering can  
leverage up-to-date knowledge retrieved  
from using search and retrieval, while symbolic AI can  
help detect and control hallucinations of LLM models.  
Image analysis using deep neural networks  
can expand the context when prompting LLMs,  
adding images as input in addition to texts.  
There are plenty of ways to combine AI models, given  
the specific needs of its application,  
helping us in the AI paradigm shift, the transition  
from monolithic AI systems to multicomponent or compound  
AI systems.  
Many AI systems in practical use today are not standalone.  
They consist of multiple integrated components.  
Sometimes they are based on LLMs incorporating  
additional features.  
In fact, many of these features have become so integrated  
that most users assume they are an inherent part of LLM  
functionality.  
An example is Retrieval Augmented Generation, RAG.  
In RAG, automated retrieval services  
gather relevant documents and use  
them to enhance the user query before prompting  
generative models.  
This enables LLMs to incorporate domain-specific and up-to-date  
information into their responses.  
Systems like ChatGPT utilize web search to enhance context  
and provide more relevant and up-to-date responses.  
RAG techniques have advanced significantly  
and are now implemented in most commercial AI systems.  
We also observed that modern commercial LLM-based systems  
feature multimodal capabilities.  
For example, they can process images as input,  
incorporate generative models for multimedia content,  
or connect to devices like mobile phones  
to accept video input.  
Additionally, they incorporate consistency-checking mechanism  
by leveraging formal knowledge representation  
and automated reasoning systems to ensure the reliability  
of their results.  
This integration leads to neurosymbolic AI systems  
which combine the strengths of the two  
main pillars of Al development-- machine  
learning and symbolic AI.  
Several methodologies for automating and optimizing  
the integration of multiple AI components  
have been proposed-- for example, compound AI.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.2 Search and Retrieval in Compound AI Systems  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: When integrating AI models,  
many services that involve humans in the monolithic AI  
approach should be automated.  
One of these technologies is search and data retrieval.  
It is extremely useful, particularly in scenarios  
of prompt enhancement and expansion  
during prompt engineering.  
When prompting LLMs, up-to-date data and knowledge  
are essential.  
Instead of relying solely on static pre-trained models,  
AI components should be able to dynamically fetch and integrate  
knowledge in real time.  
The data accessible to semantic search and retrieval services  
varies depending on the specific application  
and its requirements.  
They can originate from physical devices, such as sensors,  
which capture and record information  
about users or the environment.  
For example, data related to the user's location obtained  
from GPS can significantly improve  
searches that are relevant to local information.  
They also have access to public data sources via the web,  
such as websites, social media posts, scientific data,  
et cetera.  
For example, data from recent social media conversations  
can update the context of a prompt  
with data that has not been used during the training of an LLM.  
Local databases can also include relevant information  
such as customer records, patient data, transaction logs,  
and system log files.  
For example, a patient's medical record  
is crucial for establishing the relevant data  
framework in the AI-assisted medical diagnosis process.  
Proprietary data is also valuable,  
including internal reports, legal documents,  
strategic analysis, analytics, user surveys,  
and other confidential information.  
For example, user questionnaires are  
useful for developing examples during the process of automating  
systems design using LLMs.  
Finally, in many cases, domain-specific knowledge  
is essential, often recorded in ontologies, rules or knowledge  
graphs to provide structured knowledge.  
For example, automated reasoning systems  
need to respond based on the updated rules that  
constitute domain knowledge.  
Knowledge graph embeddings capturing domain knowledge  
are utilized to update and enrich information  
during the prompt engineering process.  
The process of accessing data using search  
should be online, generating the queries in real time.  
The queries are generated automatically, sometimes  
leveraging terminological knowledge  
to ensure precise and relevant information retrieval.  
Moreover, relevant terminological knowledge  
is accessed based on the context facilitating prompt engineering.  
The ultimate goal of this process  
is to collect relevant data and knowledge  
and integrate it into the tasks performed by the AI system.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.3 Prompt Engineering in Compound AI Systems  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: The performance of AI systems, in particular, of LLMs,  
is closely related to how questions  
are formulated, meaning the input provided to the model.  
The automation of prompting in AI systems  
with multiple components is a key element.  
Rather than relying on manual prompting,  
automated techniques allow AI to generate  
dynamic and optimized interactions,  
improving efficiency and adaptability.  
Let's examine the prompting process  
in more detail, focusing on LLM prompting, which  
is both the most complex and has a significant impact  
on system performance.  
Prompting is actually a black-box style communication  
with a model.  
Consider, for example, that we can prompt  
an LLM to compose a poem.  
We just tell the LLM, "Write a short poem about the blue sea."  
The model then generates a poem as output.  
So a prompt is the input to the generative AI model that defines  
the task to be performed.  
Prompt engineering is the process  
of crafting a prompt to optimize the LLM's response.  
This optimization involves structuring  
the prompt to include necessary information and context,  
enabling the LLM to generate a precise and accurate response.  
The prompt is represented in various formats,  
depending on the type of the prompt model.  
For example, we can provide text, an image, a video, audio,  
a multimedia file, or a combination of these as input  
and request a corresponding text, image, video,  
or other format as output.  
The type of prompt can also vary.  
For example, it can be a short statement, a command,  
an evaluation, or a detailed prompt that  
includes context descriptions, example references,  
and specific instructions.  
The goal of the prompt can also vary  
depending on the phases of the interaction with the AI system.  
For example, we can request information  
to establish context describing the style of the desired  
response, provide feedback to the AI system,  
offer methodological guidance by outlining appropriate steps,  
or ask for explanations and reasoning  
behind the AI's response.  
There are numerous examples of the above, such as the prompt,  
"Write a short poem about the blue sea,"  
where we request the generation of a text,  
or, "What is a Turing Award?"  
with which we request information,  
or, "Write this as a native English speaker,"  
with which we specify the style of the generated text.  
Let's now explore some techniques  
used in prompt engineering.  
One of the core techniques is motivated by important findings  
from the analysis of LLM performance,  
particularly of the larger models.  
These findings show that LLMs can adjust their output based  
on examples provided in the input,  
allowing them to adapt to different patterns.  
This process is known as in-context learning.  
For example, a prompt designed to assess  
the likelihood of pneumonia could  
list symptoms and request yes-or-no answer,  
along with a brief explanation.  
This prompt is called zero-shot learning  
because the model is given only the instruction  
without any example.  
On the other hand, we can provide  
the model with labeled examples before asking  
to classify a new input.  
This technique is known as few-shot learning.  
In this example, before requesting an estimate,  
pneumonia or not, we first provide a similar example  
where the right answer is already known and given  
to the LLM.  
In this case, the LLM sticks to a specific form of the answer  
while taking into account the ideal reasoning,  
linking symptoms to a diagnosis.  
In-context learning has been shown  
to be highly effective in practice, significantly  
enhancing the performance of LLMs.  
Moreover, we can automate the construction  
of in-context learning prompts using semantic search and data  
retrieval to retrieve appropriate examples.  
Another powerful prompting technique  
which significantly enhances results  
is chain-of-thought prompting.  
If we know the reasoning process required  
to derive a complex result or conclusion,  
it is highly effective to explicitly include it  
in the prompt.  
In the pneumonia example mentioned earlier,  
we can provide the key reasoning steps involved in diagnosis  
and/or specify the sequence of information  
we want the LLM's response to follow.  
In this case, we can also request  
a detailed response that follows the specified reasoning steps.  
The chain-of-thought technique, when  
combined with in-context learning,  
has proven to be one of the most effective approaches  
for addressing LLMs' hallucination issues  
and reducing LLMs' errors in arithmetic operations  
or reasoning tasks.  
To do this, we provide examples that  
include detail, step-by-step execution of operations,  
or the logical sequence of conclusions being drawn.  
This chain-of-thought concept can be expanded even further  
involving the LLM.  
Provide multiple prompts sequentially,  
guiding the LLM through a structured reasoning process.  
Each prompt refines or builds upon the previous response,  
gradually improving accuracy and coherence.  
This technique is known as prompt chaining.  
In the pneumonia example mentioned earlier,  
we can first ask the LLM to identify relevant symptoms  
before proceeding with the assessment prompt.  
Here, for example, the LLM's response  
may include symptoms such as persistent cough or shortness  
of breath as indicative signs of pneumonia.  
Based on this response, we can ask  
the LLM to assess the likelihood of pneumonia given the presence  
of some of these symptoms.  
The prompt-chaining technique can be applied dynamically  
during user interaction, allowing  
for adaptive and context-aware responses.  
In this example, the LLM can generate specific questions  
for the user, allowing us to gather  
additional relevant information for a more informed response.  
Beyond these fundamental prompting techniques,  
many additional methods enhance prompt engineering services,  
enabling automation and significantly improving  
the performance of AI systems.  
Moreover, during the prompt engineering process,  
additional AI services, such as semantic search and retrieval  
or automated reasoning, can be used  
to gather the necessary information,  
incorporate domain knowledge, verify LLM responses  
for obvious errors, and enhance accuracy and reliability.  
Another technique used in prompt engineering  
is based on prompt templates.  
Specifically, well-crafted, high-quality prompt templates  
are developed for each prompt structure  
and stored in a database for reuse.  
Then specific templates can be selected and, if needed,  
combined and modified accordingly.  
Finally, based on domain knowledge, context,  
and relevant user-specific information,  
templates are customized to generate the appropriate prompt  
for each specific case.  
For example, if we decide to apply the chain-of-thought  
technique, instead of using the simple prompt,  
"Does the chest X-ray show signs of pneumonia?"  
we do the following.  
We find, from the available chain-of-thought prompt  
templates, a suitable one which is  
relevant to medical diagnosis based on imaging.  
Based on the specific scenario, we replace image type  
with chest X-ray, label with lung opacity, and so on,  
customizing the template.  
In this way, we construct a detailed chain-of-thought  
prompt.  
These are methodologies that take an even more systematic  
approach by utilizing optimization algorithms  
to refine and enhance prompt generation.  
Using a score function, optimal prompts  
can be determined using algorithms  
like reinforcement learning, genetic search, gradient-based,  
or Bayesian optimization.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.4 AI Reasoning: Foundations and Representations  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Next, we will explore a key service that  
automates communication processes  
with AI models in multiple component AI systems--  
reasoning.  
Reasoning is the process of deriving conclusions  
from facts and knowledge, transforming implicit knowledge  
into explicit.  
Through reasoning services, we can standardize AI processes  
while ensuring guarantees for consistency, correctness,  
and accuracy of AI models.  
Additionally, with reasoning, we can enable explainability,  
allowing for better interpretation  
of AI-generated results.  
We can also enhance prompt engineering or search  
and retrieval by providing contextual understanding  
and domain knowledge analysis capabilities.  
There are various types of reasoning.  
The three main types are deductive, inductive,  
and abductive reasoning.  
Deductive reasoning allows us to derive conclusions from facts  
by applying logical rules.  
For instance, we know that all patients  
with bacterial pneumonia have elevated white blood cell  
counts.  
We also know that John has bacterial pneumonia.  
So as a conclusion, John's white blood cell count  
should be elevated.  
Inductive reasoning helps us identify relationships  
between facts, allowing us to derive general rules  
from specific observations.  
For example, we observe that 90% of pneumonia patients  
in hospital had a fever.  
We conclude that pneumonia patients likely develop a fever.  
Abductive reasoning helps us identify possible causes  
that explain observed events.  
For instance, we observe that a patient  
has lung capacity and fever.  
As possible explanations, we conclude  
that the patient has pneumonia, the most likely,  
or lung cancer, less likely, or pulmonary edema,  
possible but unlikely.  
Most reasoning services used in multicomponent AI systems  
are categorized on these fundamental types.  
For example, determining the context  
for extracting relevant data, such as inferring  
the possible intent behind the user's query to an AI system,  
is a problem of abductive reasoning.  
The traditional approach to AI reasoning relies on symbolic AI.  
In previous lectures, we described systematic approaches  
to automated reasoning, focusing on deductive reasoning  
through knowledge expansion algorithms.  
Modern LLMs also exhibit automated reasoning  
capabilities.  
Of course, they do not perform reasoning  
in the same way humans do.  
They generate outputs by recognizing and utilizing  
statistical patterns learned from their training data.  
LLM reasoning arises from the model's ability  
to predict the next token in a sequence, capturing  
patterns of logic, mathematics, and common sense learned  
from its training data.  
This creates the illusion of formal reasoning,  
but there is no genuine understanding,  
intentional thought process, or structured reasoning mechanism  
behind LLM reasoning.  
As a result, LLM's conclusions are not always correct,  
even if they are inferred from valid knowledge and facts.  
On the other hand, automated reasoning in symbolic AI systems  
relies on sound inference rules.  
If the knowledge and facts are correct,  
symbolic AI engines will always produce logically  
valid conclusions.  
It is important to deeply understand this distinction  
to choose between LLM reasoning and symbolic reasoning  
in practical applications.  
Before exploring how reasoning is performed by symbolic AI  
systems and LLMs, let's first examine  
how information is represented and stored within these systems.  
We revisit the example from lectures on symbolic AI using  
the Wikipedia description of the movie La La Land.  
The first sentence of the text is represented in LLMs  
with the use of tokens.  
Tokens are the fundamental unit of information representation  
in language models.  
Tokens are data units that represent short character  
sequences.  
They are not necessarily full words  
but can include subwords, individual characters,  
or even punctuation marks.  
A general rule of thumb is that one token corresponds  
to approximately four characters in common English text.  
This means that 75 words typically  
translate to around 100 tokens.  
The GPT-4 tokenizer, which is used in ChatGPT,  
identifies 20 tokens in the example sentence.  
Here, we see the separation into tokens,  
which leads to a dense representation of the sentence,  
which is not fully aligned to the words used in the meaning.  
These tokens are then encoded and are  
assigned unique identifiers, the IDs,  
allowing each sentence to be represented  
as a vector containing the token IDs.  
The operation of LLMs is based on the encoding  
of tokens in another space using embeddings.  
The mapping from the token space to the embedding space  
is done by encoders.  
For instance, the encoder used by ChatGPT maps tokens from each  
text into a vector space with at least 1,500 dimensions.  
This is the small embedding encoding vector  
representing the tokenized text in a high-dimensional space.  
This is the embedding vector representing our input text.  
Embedding vectors are text representations  
with strong statistical properties,  
such as capturing the likelihood of words appearing  
next to each other in a text.  
However, they lose direct semantic reference  
to the actual words, at least as humans perceive them,  
meaning they no longer retain a direct, interpretable connection  
to the original linguistic meaning.  
Therefore, this representation is  
machine understandable but not human  
understandable as it is statistics intensive rather than  
knowledge intensive.  
On the other hand, in symbolic AI,  
information is represented explicitly and structurally.  
Remember, from previous lectures on symbolic AI,  
the same example sentence can be represented  
as a set of formal statements that explicitly  
capture the intended meaning.  
These statements form a structured knowledge  
about the specific subject.  
Specifically, we write that the description refers to the film  
La La Land, which is a romantic musical film directed  
and written by Damien Chazelle in 2016  
and was produced in the United States.  
In modern symbolic AI systems, this information  
is represented on the web as a graph, where nodes represent  
entities or classes, and edges represent their relationships.  
Knowledge representation languages  
have been standardized for graph data representation,  
enabling formal semantic descriptions at the web level.  
In the lecture on symbolic AI, we describe these technologies.  
In the case of LLMs, we observe that embeddings  
capture statistical correlations of the domain  
by encoding them in valued relationships in a form that  
is very effective but not human understandable.  
In symbolic AI systems, domain relationships  
are recorded at a semantic level, represented  
as formal rules.  
For example, we can record that every romantic film is a love  
story.  
We observe that these statements are  
represented in a formal manner.  
And whether they describe events or rules,  
they remain human understandable while  
following syntactic rules that make them machine readable.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.5 AI Reasoning: Symbolic vs. LLM Approaches  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now examine how reasoning  
is handled by both LLMs and symbolic AI reasoners.  
We will compare the answer of ChatGPT  
with the answer of basic automated reasoning  
system for knowledge graphs.  
Let's assume that both systems have only the example sentence  
stored in their memory.  
We will ask whether, based on this data,  
it can be determined that La La Land is a love story.  
For humans, this is straightforward,  
as they understand that every romantic film, including  
romantic musical films like La La Land, is a love story.  
For a symbolic AI system to restrict  
to the information of the sentence  
is straightforward, as we can explicitly provide only  
this knowledge as the input.  
In an LLM, this process is more challenging,  
if not extremely difficult.  
First, we do not need to provide any input,  
as the information from this text  
is already encoded in the weights of the neural network.  
It is reasonable to assume that the model has  
been trained on Wikipedia data.  
Also, the meaning of this information  
is likely present in many publicly available texts that  
were part of its training data.  
However, it is difficult to ensure  
that it knows only the elements of this sentence,  
as LLMs inherently rely on vast amounts of pretrained data  
beyond the given input.  
To ensure the model relies only on this knowledge,  
we use prompting, combining in-context learning  
and role-playing techniques.  
We contextualize the question within a game scenario,  
explicitly instructing the model to only use  
the given information to generate its response.  
And then ask, is La La Land a love story?  
The answer of ChatGPT is correct.  
It is, "Based on the given information,  
I can reasonably conclude that La La Land is a love story."  
With a symbolic AI reasoning, the process is different.  
We give only the statements included in the sentence  
and some relevant rules.  
And we directly input the question,  
"Is La La Land a love story?"  
And the response is correct--  
yes.  
Let's try to examine how reasoning  
is performed in each system.  
In the case of ChatGPT, its output  
includes the reasoning process used to reach the conclusion.  
It is clear that it recognizes the meaning of the sentence.  
Moreover, it more or less follows the suggested game  
scenario, as it restricts itself to using  
only the information contained in the given sentence.  
Finally, in the third step of reasoning,  
ChatGPT appears to use additional domain knowledge,  
specifically the information "a love story is a narrative  
centered around romance."  
That is relevant to the rule "romantic films are love  
stories" that we provided to the symbolic AI reasoner.  
On the other hand, the reasoning process of symbolic AI  
is transparent, as it follows strict logical steps.  
Initially, the fact "La La Land is a romantic musical film"  
and the rule "romantic musical films are romantic films"  
are combined to infer La La Land is a romantic film.  
And this fact, combined with the rule "romantic films are love  
stories," gives the conclusion La La Land is a love story.  
That is the answer to the question.  
So we understand that the symbolic AI reasoning  
follows a transparent, rigorous algorithmic process, which  
is good.  
On the other hand, we must carefully select and provide  
the symbolic AI reasoner with the relevant knowledge  
in a formal language.  
This is challenging.  
With ChatGPT, the knowledge is already there,  
encoded in the weights.  
We don't have to give anything, which is good.  
On the other hand, inside the system,  
reasoning does not follow the step presented by ChatGPT.  
The correct answer is based on complex statistical  
associations, making the text of the answer to more likely follow  
the prompt.  
As a result, in more challenging reasoning problems,  
we may encounter, by LLM reasoning, errors  
that are difficult to trace.  
Let's analyze a reasoning problem  
where such issues arise to understand  
that while LLM reasoning is easy to use,  
it can sometimes be unreliable.  
My company has two debtors--  
Company A and Company B. We know that Company A  
is a bankrupt company.  
We don't know the bankrupt status of Company B.  
Also, we know that Company B is the only debtor of Company A  
and that Company B has only one debtor, Company C, that  
is not a bankrupt company.  
The question is, if my company has a debtor that  
is a bankrupt company and this company has a debtor that is not  
a bankrupt company, this becomes particularly relevant  
if, for example, we need to determine  
whether our company has a recourse to recover funds  
from its bankrupt debtors.  
The specific reasoning problem is difficult  
because of the unknown status of company B.  
The trick is that company B may be a bankrupt company or not.  
If company B is not a bankrupt company,  
then my company has a debtor that  
is a bankrupt company, Company A, which  
in turn has a debtor that is not a bankrupt company, Company B.  
If company B is a bankrupt company,  
then my company still has a debtor that is bankrupt--  
Company B this time--  
which in turn has a debtor which is not bankrupt,  
Company C. So in all cases, the answer to my question is yes.  
Let's examine how ChatGPT responds to this reasoning  
problem.  
First of all, it presents the problem statement  
in a formal manner.  
This description is a sound and complete description  
of the problem.  
Then it presents a step-by-step analysis  
that seems like a goal-oriented reasoning strategy.  
It seems rather intuitive and clear,  
although it does not infer some new knowledge.  
Then comes the answer part.  
The first bullet captures the case  
that Company B is not bankrupt, concluding that in this case,  
the answer is yes.  
This is right.  
The second bullet captures the case that Company B is bankrupt.  
And in this case, it notices that Company A does not  
meet the criteria.  
True but misses the fact that now Company B  
meets the criteria.  
As a result, the answer of ChatGPT is wrong,  
connecting the positive answer with the bankrupt status  
of Company B. This is a problem that  
requires to be solved a challenging reasoning technique  
known as conditional reasoning.  
Unfortunately, many practical problems  
involve conditional reasoning, as they often  
contain unknown facts that require us to assume  
whether they are true or not.  
Let's now examine whether a symbolic AI  
reasoner can effectively handle this problem.  
The first step is to formally represent the knowledge.  
The second step is to formally represent the question.  
If we represent the knowledge as a knowledge graph,  
the goal is to determine whether the available data allows  
us to infer the existence of the hasDebtor  
edge between my company and another node classified  
as bankrupt with a nonbankrupt debtor.  
Sophisticated automated reasoning algorithms  
can effectively handle this problem.  
They distinguish between two cases  
to systematically evaluate it.  
Let's examine this more closely.  
In the first case, Company B is connected to the BankruptCompany  
node, identifying that the desired  
path exists within the knowledge graph in this case.  
With this inference, it has concluded  
that the answer to this question is yes  
when Company B is bankrupt.  
In the second case, Company B is connected  
to the nonbankrupt company node.  
And again, the desired path exists in the knowledge graph,  
although this time it is different.  
With this inference, it has concluded that in this case,  
the answer to the question is also yes.  
So in any case, the answer is yes.  
Therefore, we see that symbolic AI reasoning can effectively  
handle this case.  
Indeed, automated reasoning algorithms  
can effectively handle a wide range of reasoning problems,  
under one condition.  
The facts and rules describing the domain and the problem  
should be formally and precisely formulated.  
This is a challenging task in itself,  
which must be undertaken only if guarantees related to reasoning  
is a requirement of the specific AI application.  
So we need to use symbolic AI reasoners.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L2.6 Challenges in Compound AI Systems  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: To recap, after examining issues related  
to AI system components in multi-component architectures,  
let's now describe some key challenges that  
emerge from the integration of these components.  
There are major design challenges to address.  
There are numerous architectural choices.  
Identifying the optimal design is a complex problem  
that is expected to be systematically addressed  
in the coming years.  
Moreover, while optimization challenges for individual AI  
models are well understood, optimization and training  
of a system integrating multiple AI models  
is a new and complex problem.  
On the other hand, there are great opportunities.  
For example, an AI system can enhance efficiency  
by leveraging multiple smaller, specialized models tailored  
to specific tasks rather than relying  
on a single large model that demands significant resources.  
Finally, new challenges arise in the integration of AI models,  
particularly as they are resource-demanding and evolve  
rapidly.  
For practical deployment, processes such as monitoring  
and orchestration should be automated,  
and data pipelines should be carefully defined.  
Security, reliability, accountability,  
and interpretability challenges should  
be addressed, especially when integrating powerful AI  
systems that automatically retrieve and utilize information  
from the web.  
So what is the take-home message of this lecture?  
First, monolithic AI systems can solve many problems,  
but the growing demands on AI have made it clear  
that only a combination of AI models  
can fully meet modern requirements.  
This is what many AI systems are doing today  
to improve their performance.  
For example, RAG systems combine advanced retrieval with LLMs.  
Modern commercial LLMs integrate multi-modal capabilities--  
for example, image analysis-- or symbolic AI--  
for example, symbolic math engines--  
to enhance their functionality.  
There are now many techniques and approaches  
available to automate the prompting process.  
Prompts can be very sophisticated,  
integrating elements from other systems such as search  
and retrieval, knowledge graphs, and reasoning services.  
Prompt engineering improves LLM's responses.  
Many essential features of AI systems depend on reasoning.  
For example, in domains such as health care, finance, and law,  
AI systems must ensure explainability.  
We can leverage the reasoning capabilities of symbolic AI  
systems or LLMs depending on the specific application  
requirements.  
Combining different AI models can  
tackle more complex problems, but it also  
introduces new challenges that we have not previously  
encountered.  
For example, optimization at the system level rather than  
the model level demands entirely new approaches.  
Moreover, security challenges arising  
from the integration of retrieval engines in LLMs  
introduce new risks, particularly concerning  
personal data protection.  
As we have seen in recent years, the future of AI  
extends beyond monolithic systems,  
making it crucial to address these emerging challenges.  
Thanks for watching.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture explained why monolithic AI systems (e.g., standalone LLMs) are not sufficient for real-world applications and introduced compound AI systems that integrate LLMs, deep learning models, retrieval engines, and symbolic reasoning to build more reliable and trustworthy AI.

Key Takeaways:  
Limits of monolithic LLMs: Computational cost, outdated knowledge, hallucinations, weak logical reasoning, and lack of guarantees make standalone generative models insufficient for high-stakes domains.  
Compound AI architecture: Combines  
LLMs (text interaction),  
Deep neural networks (image/video analysis),  
Symbolic AI engines (logic, guarantees), creating hybrid or neurosymbolic systems.  
Retrieval Augmented Generation (RAG): Use real-time search and retrieval (web, sensors, local databases, knowledge graphs) to inject up-to-date, domain-specific information into prompts.  
Automated prompt engineering: Improve reliability through in-context learning (zero-/few-shot), chain-of-thought, prompt chaining, reusable templates, and optimization-based prompt tuning.  
Reasoning comparison:  
LLMs: statistical, fluent but error-prone (hallucinations, conditional reasoning failures).  
Symbolic reasoning: rule-based, transparent, logically sound when knowledge is formally defined.  
System-level challenges: Integration introduces new problems—architecture design, orchestration, monitoring, optimization at the system level, security, reliability, interpretability.  
Central insight: Reliable next-generation AI requires orchestrating retrieval \+ prompting \+ reasoning \+ multimodal models, leveraging complementary strengths rather than relying on any single model.  
\`\`\`

Lecture 3: Retrieval Augmented Generation  
\`\`\`  
Skip to main content  
Overview  
Welcome to Lecture 3: Retrieval Augmented Generation, taught by Professor Georgios Stamou, Professor at the School of Electrical and Computer Engineering at the National Technical University of Athens, Greece, and Visiting Professor at MIT.

LLMs rely only on their training data, which can lead to outdated or hallucinated answers. RAG addresses this by following three steps:

Retrieve relevant information from a corpus.  
Augment the prompt with that information.  
Generate a grounded response.  
To support this pipeline, documents are chunked and indexed using keyword-based, semantic (embedding-based), or entity-based (knowledge graph) retrieval. These components form architectures such as Standard RAG, Contextual RAG, Graph RAG, and Agentic RAG.

RAG transforms LLMs from static text generators into knowledge-grounded AI systems capable of more accurate, up-to-date responses.

Learning Objectives  
By the end of this lecture, learners will be able to:

Explain why standalone LLMs are limited by static training data.  
Define the retrieve–augment–generate pipeline of RAG.  
Compare keyword-based, semantic, and entity-based retrieval methods.  
Distinguish between major RAG architectures and their purpose.  
\`\`\`

L3.1: Introduction to Retrieval Augmented Generation  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
This lecture describes a popular example  
of multicomponent AI, retrieval-augmented generation,  
RAG.  
Most LLM-based agents use RAG to overcome  
a key limitation of LLMs.  
Their knowledge is restricted to their training data.  
LLMs don't have direct access to the current world, what changed  
yesterday or even minutes ago.  
Their knowledge reflects the state  
of the world at the time their training data was collected,  
which means they can produce outdated or inaccurate  
responses.  
For example, if a prompt involves  
information about live market data,  
updated medical guidelines, or recent events,  
an LLM will still try to answer based  
on patterns from the past, which can lead to confident,  
but incorrect correct answers.  
To address this limitation, we build AI agents  
that extend LLMs with access to live, real-time information.  
Instead of relying solely on what the model learned weeks  
or months ago, we augment the models,  
learn data with up-to-date knowledge.  
When the model receives a prompt,  
it retrieves the most recent relevant information  
and then uses that information to generate the response.  
By combining a powerful LLM with real-time knowledge retrieval,  
LLM-based agents can deliver responses  
that are not only fluent and coherent, but also,  
accurate and up to date.  
When we interact with an LLM, the simplest approach  
is standard prompting.  
We type a question or an instruction,  
and the model gives an answer.  
This answer is based entirely on the patterns and information  
the model encodes during pre-training.  
To improve the quality, accuracy, and relevance  
of responses, we can move beyond standard prompting  
and use what we call knowledge-enriched prompting.  
We don't send the user's prompt directly to the LLM.  
Instead, we inject additional information  
before the LLM gets the prompt.  
This extra information is called background knowledge  
and may come from curated documents, domain expertise,  
structured data, or any relevant source the system has access to.  
Prompt engineering involves enriching  
the prompt with the relevant background  
knowledge so that the enriched prompt contains both a question  
and the relevant knowledge it needs  
to generate a more accurate and meaningful answer.  
One naive idea is to simply embed the entire knowledge base  
into the prompt.  
If we include all the documents, then, in theory,  
the model would have everything it needs to reason directly  
during generation.  
Unfortunately, this doesn't work in practice.  
The first major problem is the LLM's limited context window.  
Every LLM has a maximum amount of text it can process at once.  
It's impossible to fit entire books or databases  
into a single prompt.  
But even if the context window were unlimited,  
there is another problem.  
The model struggles to search inside a very long prompt.  
Long prompts weaken attention mechanism.  
When everything is included, the model cannot effectively  
prioritize what is relevant.  
It has been proved in practice that very long contexts  
introduces noise.  
When we dump huge amounts of irrelevant material  
into the prompt, the model is forced to process all of it.  
This increases cost and latency and also raises the likelihood  
of hallucinations.  
The more unrelated content we add in the prompt,  
the harder it becomes for the model to stay  
grounded in the right information.  
What we need, instead, is a more sophisticated way  
of selecting and injecting the relevant knowledge.  
This is exactly what RAG does.  
The first step is retrieval.  
Instead of sending the model everything,  
we run a targeted search over external knowledge sources.  
The system retrieves only the pieces of information  
that are relevant to the user's prompt.  
This solves the context relevance problem  
by giving the model exactly what it needs and nothing more.  
The second step is augmentation.  
The system takes the user's original prompt  
and enriches it with a retrieved knowledge.  
This new, enriched prompt contains both the user's prompt  
and the important facts required to answer accurately.  
By doing this before interacting with a model,  
we reduce hallucinations since the model is  
guided with the right context.  
The last step is generation.  
Now, that the prompt contains all the necessary information,  
we pass it to the LLM.  
The model generates the final answer  
based on both the user's request and the inserted relevant  
context.  
This produces responses that are accurate, relevant,  
and up to date, while still using the LLM's fluency  
and reasoning abilities.  
So RAG can be summarized as-- retrieve the right context,  
augment the prompt with it, and then ask the model  
to generate the answer.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.2: Preprocessing for RAG  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: RAG operates online, so it needs to be fast.  
For this reason, it is better doing some pre-processing  
like preparing and organizing the data.  
Let's consider the background knowledge  
as a document set, which we call Corpus.  
The first step is splitting large documents  
into smaller, meaningful blocks of text that are manageable,  
but also preserve semantic integrity.  
We call these blocks chunks, and the process of splitting  
the documents, chunking.  
Each chunk should contain a complete idea  
or information or description.  
It is a sentence, a paragraph, or a well-defined section.  
We store them in our retrieval system  
to make it precise and efficient,  
because we search over smaller, focused pieces of text,  
rather than big documents.  
There are different ways to chunk text.  
We can use fixed length chunking, where we simply  
cut the text every certain number of tokens,  
or we can use paragraph-based chunking,  
keeping the natural structure of the text.  
We can use a sliding window, which preserves context overlap,  
or more advanced approaches like semantic chunking, which  
use an AI model to split text based on meaning.  
Here's a simple example using sentence-based chunking.  
Take a short paragraph about the Parthenon.  
Instead of storing it as one long passage,  
we split it into four meaningful chunks.  
Chunk 1 is for the location and dedication of Parthenon;  
chunk 2, for the construction period;  
chunk 3, for its architectural significance;  
chunk 4, for its status as a major archeological site.  
By separately storing chunks, the retrieval system  
can return only the chunks that are  
relevant to the user's prompt.  
However, sometimes individual sentences  
don't carry full meaning on their own,  
as their interpretation relies on surrounding context.  
If we read only chunk 2 to in isolation,  
it's even hard to tell that it refers to the Parthenon.  
An effective strategy to address this issue  
is known as contextual chunking.  
The idea is simple.  
Instead of storing each chunk in isolation,  
we store it together with a small amount  
of surrounding context.  
This extra context helps the retrieval system understand  
where the chunk fits within the full document,  
and what it is really about.  
Here's how it works.  
We start with a Corpus of document.  
We pass a document through the chunker, and we get chunks 1  
to n.  
Then we take each chunk and ask an LLM to situate it  
within the broader document, providing  
a very small amount of context.  
You can see an example of a prompt skeleton on the left.  
For every chunk, we give the model  
two pieces of information, the full document and the chunk  
we want to contextualize.  
We then ask the model to summarize the chunk's role  
or meaning within the entire document.  
This gives us a short, contextual description.  
We then store context plus chunk as a single retrieval unit.  
If we run this prompt for our example,  
the model generates the context, a description  
of the Parthenon's history and significance  
on the Athenian Acropolis.  
This seems very relevant and informative.  
We then combine the context with the chunk itself,  
producing context 2 plus chunk 2\.  
That is a description of the Parthenon's history  
and significance on the Athenian Acropolis.  
It was constructed between 447 and 432 before Christ.  
Now, when the retrieval system searches for relevant context,  
it matches an information unit that is  
both specific and meaningful.  
As expected, the results show in practice  
that during retrieval, this extra context  
improves the results.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.3: Retrieval Methods in RAG  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So far, we've explored  
how to begin with a document, Corpus,  
and build a chunk database.  
The next step is to design methods  
for finding the chunks that are relevant to the user's prompt.  
A simple and very common method is keyword-based search,  
which relies on matching words from the user's query  
to words in the chunks.  
As a preprocessing step, we represent each chunk  
with a set of its most important words.  
To find these words, we define a statistical measure  
called TF-IDF, term frequency, inverse document frequency.  
The intuition of TF-IDF is the following.  
First, we measure the word frequency in the chunk.  
This is the TF, term frequency.  
The more often the word appears, the more indicative  
it might be of that chunk's content.  
Second, we measure how rare that word  
is across the entire Corpus.  
Words that appear everywhere, like the, or, it,  
do not convey much of the chunk meaning.  
This is the IDF, the inverse document frequency.  
By combining these two measures, TF-IDF  
identifies the words that are both  
frequent in the specific chunk and rare across the corpus.  
This becomes the chunk's signature keywords.  
During the system operation, we extract  
the keywords of the prompt and feed them  
to the keyword-based ranker.  
The ranker looks in the tank database  
for chunks whose TF-IDF keywords overlap most with the query.  
It scores and ranks the chunks and returns the top K candidates  
as the most relevant pieces of text.  
Let's see say a simple example to illustrate  
how keyword-based search works in practice.  
The chunk database includes four chunks  
taken from the document about the Parthenon.  
We represent each chunk as a set of its most important keywords  
using TF-IDF.  
For example, chunk 1 includes keywords like Parthenon,  
Athenian, Acropolis, Athena.  
Chunk 2 includes 447, 432, BCE, constructed, et cetera.  
These sets of keywords are included in the TF-IDF index.  
Suppose now that the user prompt is when  
was the Parthenon constructed?  
If we match the query against keywords of the TF-IDF index,  
we see chunk 1 is relevant because it shares the word  
Parthenon with a query, and chunk 2  
is relevant because it shares the word constructed  
with a query.  
Moreover, these chunks are equally  
relevant because they both share one keyword with a prompt.  
This shows how keyword-based search works, but also,  
shows a key limitation.  
Keyword-based search is based only on word overlap,  
not meaning similarity.  
In our example, chunk 2 is more similar than chunk 1,  
because the keywords 447, 432, and BCE are  
relevant to the word when of the prompt  
from a semantic point of view.  
This is ignored by keyword-based search.  
To deal with this problem, there is a more powerful approach,  
semantic search.  
Instead of comparing prompts and chunks based on shared words,  
semantic search compares them based on their meaning.  
Each chunk of the chunk database is  
processed by an encoder that converts  
the text into a high dimensional numerical vector.  
These vectors, called embeddings,  
act like a semantic fingerprint of the text,  
capturing its meaning.  
The embedding vectors of all chunks  
are stored in a vector database.  
Given the user's prompt, we use the same encoder  
to find its embedding vector, and then we  
find the similar chunk embedding vectors  
stored in the vector database.  
Similarity here means that the embedding vectors  
are close to each other in this high-dimensional space, based  
on a distance measure.  
So instead of matching keywords, semantic search  
finds the chunks whose vectors are nearest neighbors  
to the prompt vector.  
Finally, the semantic ranker returns the top K  
most semantically similar chunks to contextualize  
the user prompt.  
Both keyword sets and semantic search retrieve relevant chunks  
based on text similarity.  
There are scenarios where text similarity alone  
isn't enough to get the relevant context, especially  
in complex domains where several entities,  
but also, relationships between entities matter,  
like in medicine or law.  
In such cases, it may be necessary to access  
context spread across multiple documents in the Corpus.  
Entity-based search can be applied in these cases.  
The core idea is to extract structured knowledge,  
like knowledge graphs, from texts.  
Several methods can be applied here.  
For example, starting from the database of text chunks,  
we may ask an LLM to identify entities  
like people, places, symptoms, diseases,  
and the relationships between them.  
These entity relationship pairs are  
stored in a knowledge graph that is a structured representation  
of the document's meaning.  
Then we can generate higher level summaries of the graph,  
like summaries of clusters or communities of related entities.  
These are stored in a knowledge graph index,  
which becomes searchable.  
Given the user's prompt, the system  
performs a prompt-focused summarization.  
Instead of searching text directly,  
It navigates the knowledge graph to retrieve  
the most relevant entities, relationships, and summaries  
connected to the question.  
So while semantic search finds chunks  
that are similar in meaning, entity-based search  
finds chunk communities that are conceptually relevant according  
to a structured map of the domain.  
This has several advantages.  
First, it allows the system to reason  
over facts and relationships, not just words or word meanings.  
Second, entity-based search can retrieve relevant information,  
even if it is distributed across multiple documents.  
And third, it can return concise domain-tailored summaries,  
rather than raw text.  
In our example, rather than treating  
the chunks about Parthenon as isolated pieces of text,  
we analyze them to identify entities, such as Parthenon,  
Athens, Acropolis, and the relationships between them,  
like is that located on or has start date.  
The result is a knowledge graph.  
Each node represents an entity, and each edge  
represents a relationship.  
So chunk 1, the Parthenon, is a temple on the Athenian Acropolis  
dedicated to Athena, becomes a structured graph of facts.  
Parthenon is a temple.  
Parthenon located on Athenian Acropolis.  
Parthenon, dedicated to Athena.  
And classification information.  
Athena is a goddess, Athenian Acropolis  
is an Acropolis, et cetera.  
Chunk 2 is connected to the same node, Parthenon,  
expanding the knowledge graph, providing more information,  
in this case about the construction of Parthenon.  
This transformation aligns data with knowledge and reasoning  
over knowledge and has several benefits.  
We represent explicit semantics, not just implied meaning.  
We disambiguate concepts by linking them  
to related entities.  
We preserve context, provenance, and meaning across chunks.  
We enable logical reasoning like identifying timelines,  
causes, or dependencies, avoiding hallucinations.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.4: RAG Architectures  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Let's now describe some popular RAG architectures,  
starting from the standard RAG.  
As a pre-processing step, The Corpus  
is chunked and stored in the chunk database.  
The chunk database consists of two main components, the vector  
database, which stores the chunk embeddings,  
supporting the semantic search and the TF-IDF index,  
which supports the keyword-based search.  
When a user sends a prompt, the system  
performs two different chunk retrieval tasks in parallel.  
The first is performed by the semantic ranker, which  
finds chunks that are semantically  
similar to the query, even if they  
don't share the same wording.  
The second is performed by the keyword-based ranker,  
which finds chunks that share the same keywords with a query.  
Both ranking methods have strengths and weaknesses.  
Semantic ranking is good at capturing meaning,  
but sometimes misses exact facts.  
Keyword-based ranking is precise, but can miss context.  
To combine advantages of both methods, we use rank fusion.  
Specifically, we aggregate the outputs  
of both ranking mechanisms into a single top-k selection  
of the most relevant chunks.  
The top-k chunks are then sent to the LLM together with a user  
prompt.  
The LLM uses the chunks as context  
to generate a more accurate response.  
Contextual RAG builds on standard RAG,  
but improves both retrieval precision and answer quality  
by using context-aware chunks and improved ranking.  
During preprocessing, we construct the chunk database  
as in the standard RAG The only difference here  
is that contextual chunking is used.  
Each chunk is first stored together  
with a short, semantic summary of its surrounding  
context, which makes retrieval much more accurate.  
When a user submits a prompt, the semantic ranker  
and the keyword-based ranker work as in the standard RAG,  
but now, contextual chunks are used.  
When the two rankers return the candidate-related chunks,  
instead of sending them directly to the model,  
a reranking step is introduced.  
First, the rank fusion combines results  
from both rankers into a unified list, and then  
a reranker scores it chunk by how well  
it matches the user's intent and selects the top-k most relevant  
ones.  
The top-k chunks, together with the user prompt,  
are finally provided to the LLM, which  
uses them as grounding to produce its response.  
Contextual RAG retrieves, not just similar chunks,  
but semantically grounded chunks prioritized  
through a more sophisticated query chunk relevance.  
Graph RAG improves standard RAG, incorporating knowledge graphs  
for retrieving and reasoning.  
We start, again, by chunking the Corpus during preprocessing,  
but now, we further analyze chunks,  
detecting entities and relationships.  
Using this conceptual information and knowledge graph  
is constructed to support entity-based search.  
The knowledge graph captures meaningful, structured  
information like who is connected  
to whom, what events happened when, how concepts relate,  
what belongs to what, et cetera.  
In addition, we build community summaries,  
which group-related parts of the graph  
into coherent topics or subgraphs.  
These allow the system to retrieve and summarize  
clusters of related information, rather than isolated fragments.  
When a user submits a query, the most relevant parts  
of the knowledge graph are retrieved.  
Then hierarchical ranking takes into consideration  
both local relevance and abstract contextual similarity.  
Finally, the selected context, combined with the original user  
prompt, is passed to the LLM, which  
generates a grounded answer.  
The key benefit is that Graph RAG enables entity-based search  
and reasoning, retrieving relevant entity and relationship  
information across different chunks.  
In real-world applications, different retrieval methods  
perform better, depending on the specific use case.  
A new direction in RAG, agentic RAG,  
combines several retrieval methods,  
introducing the idea of the retrieval router agent.  
Instead of a single retrieval pipeline  
that always works the same way, the retrieval router agent  
takes the user's query and decides  
what kind of retrieval strategy to use  
and which search tools to call based on the needs of the task.  
For example, if the query is factual,  
the agent may prioritize keyword-based retrieval.  
If the query is conceptual, or ambiguous,  
it may request semantic search.  
If the query asks for up-to-date information,  
it may trigger websites.  
The router can iteratively combine requests  
to different retrieval agents, each specialized  
in a different strategy.  
So multiple retrieval agents can work  
in parallel or sequentially.  
It's accessing different data sources, like documents,  
vector databases, knowledge graphs, or the web.  
The results from these searches are  
returned to the router, which passes  
to the LLM a curated context.  
Then the LLM produces a response,  
and if the answer is incomplete or uncertain,  
it can ask for more context, triggering a new cycle.  
So with agentic RAG, retrieval becomes an active adaptive loop  
instead of a single, static step.  
This makes agentic RAG particularly  
powerful for complex prompts and scenarios  
where information is spread across multiple heterogeneous  
resources.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

L3.5: Wrap-Up  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So what is the take-home message  
of this lecture?  
We described a very popular method  
to combine LLMs with real-time knowledge retrieval,  
building LLM-based agents that can deliver responses that  
are not only fluent and coherent, but also  
accurate and up to date.  
When we simply prompt an LLM, it answers based only  
on what it learned during training, which can  
limit accuracy and relevance.  
To address this, knowledge-enriched prompting  
injects relevant background information into the prompt  
so the model can ground its answers in external knowledge.  
RAG does this by retrieving useful knowledge,  
augmenting the prompt with it, and then generating  
a grounded, accurate response.  
Concerning RAG implementation, the first step  
is pre-processing.  
RAG needs fast retrieval, so documents  
are preprocessed by splitting them into smaller chunks  
that each contain a meaningful unit of information.  
To retrieve relevant chunks for a user query,  
simple keyword-based search uses TF-IDF  
to identify important words in each chunk  
and matches them with keywords in the prompt.  
However, keyword matching ignores semantic similarity,  
so more advanced systems use semantic search,  
which embeds text into vectors and retrieves  
the chunks whose embeddings are closest to the prompt.  
In complex domains where meaning depends  
on entities and relationships, entity-based search  
extract structure knowledge like a knowledge graph  
to reason over facts, connections, and summaries.  
Concerning the architecture of RAG systems,  
we started from standard RAG that retrieves chunks using  
both semantic and keyword-based search, fuses the results,  
and sends the top k chunks to the LLM,  
combining precision with semantic coverage.  
Moreover, contextual RAG strengthens this  
by using context-aware chunks and adding a reranking step that  
selects the most intent-aligned chunks before generation.  
Graph RAG goes further by building a knowledge  
graph of entities and relationships,  
enabling structured, hierarchical retrieval  
across multiple documents.  
Finally, Agentic RAG dynamically selects and orchestrates  
different retrieval strategies through a router agent,  
making retrieval adaptive and iterative  
for complex heterogeneous queries.  
Beyond these architectures, there  
is a rapid emergence of RAG techniques  
as a result of its importance and growing traction  
in both academic and applied AI.  
So stay tuned.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Summary  
This lecture explained Retrieval-Augmented Generation (RAG) as a core example of multicomponent AI that makes LLM-based agents more accurate and up to date by grounding generation in retrieved external knowledge rather than only training-time memory.

Key Takeaways:  
Why RAG exists: LLMs are limited by static training data, so they can sound confident while being outdated or wrong for live facts (markets, guidelines, recent events).  
RAG \= retrieve → augment → generate:  
Retrieve only the most relevant knowledge from external sources,  
Augment the user prompt with that context,  
Generate an answer grounded in retrieved evidence—reducing noise and hallucinations.  
Preprocessing for speed: Build a Corpus → chunk database by splitting documents into semantically meaningful chunks (fixed-size, paragraph, sliding window, semantic chunking).  
Contextual chunking: Store each chunk with a short LLM-generated situating context so retrieval works better when sentences alone are ambiguous.  
Retrieval methods:  
Keyword search (TF-IDF): precise word overlap, but misses meaning.  
Semantic search (embeddings \+ vector DB): retrieves by meaning similarity.  
Entity/graph-based search: extracts entities \+ relations into a knowledge graph to retrieve conceptually connected context across many documents and support reasoning over relationships.  
RAG architectures:  
Standard RAG: keyword \+ semantic retrieval in parallel \+ rank fusion → top-k chunks → LLM.  
Contextual RAG: contextual chunks \+ fusion \+ reranking to select the most intent-aligned context before generation.  
Graph RAG: retrieve from a knowledge graph (plus community summaries) for structured, multi-hop context.  
Agentic RAG: a router agent chooses retrieval strategies/tools (keyword vs semantic vs web vs graph) and can iterate when more context is needed.  
Overall message: RAG is a practical path from monolithic LLMs to compound systems where retrieval quality (chunking, indexing, ranking, routing) largely determines answer quality.  
\`\`\`

Recitation 1: Prompt Engineering & Retrieval Augmented Generation  
\`\`\`  
Skip to main content  
Recitation Overview  
Welcome to Recitation 1, taught by Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.

In this section, we'll walk through hands-on examples and practice exercises to reinforce the concepts covered in the lectures, focusing on Prompt Engineering. The notebook used in this Recitation is available at the following link:

Recitation 1 Notebook

Due to potential memory issues and access requirements for the Llama model, you are advised to not run this notebook on the server and just review the outputs.

This notebook is complete — all code has already been written and executed — so you will see the outputs from each code cell. Your task is to use these outputs, along with the concepts covered in this module, to answer the questions in this assignment.

If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Lectures covered by this recitation

Lecture 3: Beyond Monolithic AI Systems  
Let’s dive in and explore the material together\!

Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.  
\`\`\`

Skip to main content  
Recitation Overview  
Welcome to Recitation 1, taught by Vassilina Stoumpou, PhD candidate at MIT's Operations Research Center.

In this section, we'll walk through hands-on examples and practice exercises to reinforce the concepts covered in the lectures, focusing on Prompt Engineering. The notebook used in this Recitation is available at the following link:

Recitation 1 Notebook

Due to potential memory issues and access requirements for the Llama model, you are advised to not run this notebook on the server and just review the outputs.

This notebook is complete — all code has already been written and executed — so you will see the outputs from each code cell. Your task is to use these outputs, along with the concepts covered in this module, to answer the questions in this assignment.

If you're new to Jupyter Notebooks, be sure to check out the 'Introduction to Jupyter Notebooks' available in the Resources tab to help you get started.

Lectures covered by this recitation

Lecture 3: Beyond Monolithic AI Systems  
Let’s dive in and explore the material together\!

Note: Please note that the notebook in the recitation video(s) are run in Google Colab, a free, cloud-based Jupyter Notebook environment provided by Google. The code we have provided you is a Jupyter Notebook run in our internal Universal AI servers. Though the environments in your notebook and in the recitations are different, the code itself is the same.  
\`\`\`

R1.1 Introduction to Prompt Engineering and Retrieval-Augmented Generation  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Hello, everyone.  
Welcome to today's recitation.  
Today, we are going to talk about specific concepts  
that you saw in one of this module's lecture,  
and more specifically prompt engineering and retrieval  
augmented generation.  
This module has covered a wide range of topics,  
but today we chose to talk about these specific ones,  
because we think they are also more relevant for everyday  
and real life practice.  
So in this recitation, we are going  
to explore how to interact with large language models  
more effectively and in a more skeptical way.  
We are going to do that through prompt engineering and retrieval  
augmented generation.  
We don't want to rely on a specific model  
and assume that this model knows everything.  
We want to critically approach the outputs of LLMs,  
and we want to investigate how structured and smart prompts  
and also external context can potentially  
improve model responses.  
So we are going to go over different types  
of prompt structures and their impact on model performance.  
We are going to investigate how smaller open source  
LLMs or large language models compare  
to ChatGPT in different prompting scenarios.  
We are going to briefly go over the design and use of RAG,  
or retrieval augmented generation pipelines,  
to improve factual accuracy and reasoning.  
So we hope that by the end of this recitation,  
you are going to have a better understanding of how  
to thoughtfully and critically approach the outputs of LLMs  
and how to use specific prompt design and information  
retrieval to have more reliable and controllable outputs.  
First of all, we need to install some packages that are not  
already available in Google Colab, the ones  
that you can see here.  
And we are noting that one of the models  
that we are going to use today, LLaMA,  
although it's publicly available,  
it requires an access request from Hugging Face, where we  
generally load our models from.  
So what this means is that in order to be used,  
we need to submit a form to Hugging Face  
and then get access to it.  
Of course, I have already done that, otherwise I wouldn't  
be able to run the code.  
But for any user, for any learner that is willing,  
that wants to actually try this themselves, here  
there are detailed instructions about how  
to access Llama on Hugging Face in a step by step fashion.  
Very briefly, first of all, you need  
to create a Hugging Face account,  
and this is the link to do that.  
Then for some of the models on Hugging Face,  
and specifically for the model we're going to use,  
which is this LLaMA 3 model, it's called Meta LLaMA 38b  
instruct, you will need to request access from Meta.  
So you need to click on this expand  
to review and access button.  
There is a form that you will need  
to fill with some of your personal information,  
and then you will need to wait for approval.  
It usually doesn't take long.  
When you get an email that confirms that you are approved  
to use this specific model, you will be actually  
able to access the files.  
In case you want to load these files in Google Colab,  
like we're doing here, you will need to basically authenticate  
through Google Colab.  
So this is why you need to get a Hugging Face access  
token in order to load the models programmatically,  
and you can generate one token by visiting this link here.  
As I mentioned, in order for me to be  
able to use this model here, I actually had to run these lines.  
And when you run this cell, you will  
get a login prompt that asks you to basically input  
your password.  
And then after this is finished, you're all good,  
you're authenticated, and you can actually  
load the weights of the LLaMA model that you want.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.2 Prompt Engineering Basics  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: So let's start with the first section  
of today's recitation, which is simple prompt engineering.  
So prompt engineering is a concept  
that became very popular after ChatGPT emerged.  
And it basically refers to the way  
of writing your prompts to large language models  
in order to get the output that you want  
or that best suits your needs.  
I assume that everyone or most of you in their everyday lives  
use ChatGPT for various tasks depending on your job  
or even for everyday life reasons.  
And you might have also observed that ChatGPT  
doesn't require very thoughtful or well-structured prompts.  
We can more or less write sentences  
with wrong grammar, wrong syntax, or very vague prompts.  
And most of the times, ChatGPT or other LLMs,  
like Gemini from Google or DeepSeek  
can definitely understand what we want them to do,  
and they do it successfully.  
But there is a very important point  
that needs to be made here.  
ChatGPT and all the other models I just  
mentioned, although, we feel like they just  
work without needing carefully designed prompts,  
this happens only because they are massive.  
These models are huge.  
They have a lot of billions of parameters.  
And in order for them to run, they  
require extremely expensive GPUs and lots of memory.  
For that reason, it is impossible to load these models  
and use them programmatically for coding or other machine  
learning tasks in an environment like Google Colab, for example.  
And even if someone was able to load them  
in a huge GPU they might have, it  
would also be very slow for them to work.  
That is why it is still relevant to focus on large language  
models that are smaller, their number of parameters  
is smaller compared to ChatGPT.  
So for example-- that's why today we  
want to focus on models that we can load on Google Colab  
and that they can run fast on it.  
So we selected two models for these recitations  
demonstrations, Llama and OpenChat.  
Llama, as you might have guessed from my previous reference  
to it, is a model developed by Meta.  
There are multiple versions of the Llama model,  
but today, we are going to focus on the 8 billion  
parameter model, which is one of the small models that Meta has.  
OpenChat is another LLM that also has  
around 7 billion parameters.  
Both of these models are definitely  
less strong than ChatGPT 4 that is currently  
available in the ChatGPT website.  
In order to have a clearer picture of how  
the models compare to each other,  
we are going to use the exact same prompt to see what outputs  
we get from the Llama model, the OpenChat model, and ChatGPT,  
the ChatGPT 4 version.  
And we're going to see how much better ChatGPT is.  
But we should always take into consideration  
the fact that the models that run behind it  
are much, much, much bigger.  
First of all, let's load the Llama and OpenChat models.  
We are going to use the Hugging Face Transformers Library.  
And we are going to also use 4-bit quantization in order  
to save GPU memory.  
Here, we first specify--  
we first import some of the packages that we want,  
and then we specify the model IDs for Llama and OpenChat.  
These are the paths as one can find them in Hugging Face.  
And then for each of the two models, we load the tokenizer.  
We specify the quantization configuration, which is,  
as I mentioned, 4-bit, and then we also load the pretrained  
version of the model of each of the models, and basically,  
we load their weights.  
As you can see here, the models are loaded, both Llama  
and OpenChat.  
And then, after we load the models,  
we have to write a generate response function that we'll  
take as an input, a text prompt, and we'll  
use one of the language models that we want to produce  
a natural language response.  
What this function does is that here it first tokenizes  
the prompt, and it makes sure that the input is  
at the same device as the model, in our case, at GPU.  
And then, we are going to use the generate function  
where we specify the input.  
We set the maximum number of tokens  
that we want the model to generate,  
and we also want to allow some randomness in the output.  
This is achieved through these parameters  
here, which correspond to some kind of sampling.  
And the goal of this is to make the responses more varied.  
The default length of the responses we have set here  
is 256, as you can see in the argument here.  
And basically, we use a tokenizer  
to decode the output of the model generation  
and get a human-like reply.  
We also specify this run all models function.  
What this does is that it iterates  
over the different models, which in our case  
are these two, Llama and OpenChat.  
And it generates responses for the specific prompt  
that we have provided.  
Now, we are going to explore different kinds of prompts  
and the reasons for which one could potentially  
want to use them.  
The first and simplest type of prompt,  
which is also the type of prompt that we usually give to ChatGPT,  
and then if ChatGPT doesn't give us the answer we want,  
we might move to more sophisticated prompts,  
is called zero-shot learning.  
So zero-shot learning basically refers to a type of prompt  
where the model is asked to perform a task by just relying  
on the general knowledge it has been trained on  
and the prompt itself.  
So it doesn't receive any kind of example  
that could potentially guide it into what we want it to do.  
Of course, as you might imagine--  
and this is more evident when we work with smaller models.  
This might lead to hallucination,  
which is the case where the model kind of makes up facts  
confidently without them being grounded.  
It can lead to potential bias or a lower accuracy.  
An example of a zero-shot prompt is this one here.  
I love La La Land.  
I hate Babylon.  
Sentiment and question mark.  
What this means is that we are asking our model  
to give us the type of sentiment that these two sentences imply.  
Let's see what each of the two models  
actually gave as an output.  
For Llama, after it outputs the prompt,  
it starts talking about how they are  
big fans of Damien Chazelle, who is the director of La La Land.  
And it kind of imitates a person that  
would use these two sentences.  
So it does not ever--  
if you read the whole, whole output,  
it does not ever give us a specific characterization  
of the sentiment of these two sentences.  
What this means is that the model did not  
understand the task.  
Similarly, for OpenChat, it starts elaborating, again,  
imitating a user that would potentially  
say these two sentences.  
It starts talking about how they have a complicated relationship  
with movies about Hollywood.  
And it kind of justifies these two sentences,  
and it never gives us the exact sentiment that we want.  
One thing that you will observe in all  
of the outputs we are going to explore today  
is that some of the sentences might be cut abruptly.  
This is because we have set this maximum number of tokens  
that can be generated to 256\.  
So if the model wants to keep producing an output  
and it reaches the 256 limit, it will just abruptly cut  
the generated output.  
So conclusion is that none of the two small models  
were able to understand what we wanted them to do.  
Let's see what-- and this is a screenshot from ChatGPT.  
Let's see what happened when we used the same prompt on ChatGPT  
4\.  
ChatGPT immediately realized what we wanted to do.  
It gave us this output where basically says "I love La La  
Land" corresponds to a positive sentiment, and "I hate Babylon"  
corresponds to a negative sentiment.  
So the overall sentiment is mixed or neutral.  
And it also doesn't have the problem  
of having to cut a sentence in half or these things  
that one has to deal with when they work with smaller LLMs.  
How can zero-shot learning, which  
is the most naive way of approaching, of talking in a way  
to an LLM, be improved?  
The extension of zero-shot learning is few-shot learning.  
So few-shot learning is basically  
when a model is given a small number of examples of a task  
within the prompt itself to help it understand the expected input  
and output format before answering a new query.  
So the idea is that here we give an example of "I  
love La La Land.  
Sentiment is positive."  
That is what the answer of the model should be.  
"I hate Babylon.  
Sentiment is negative."  
And then, we provide a new sentence  
for which we want the model to actually produce  
the corresponding sentiment.  
The sentence is "Oppenheimer was very interesting."  
And we are asking the model to fill the sentiment prompt.  
Let's see what happened with Llama.  
So Llama decided that "Oppenheimer was very  
interesting" is a neutral sentiment, which is valid.  
One could be more inclined to say that it is positive,  
but it's also not super enthusiastic, so  
neutral is acceptable.  
At least now, Llama understood what it was supposed to do.  
However, as you can see, it also started  
producing so many other examples of sentences that  
contain some kind of sentiment.  
And it produces outputs without us asking them to do that.  
OpenChat also did the same thing.  
It classified the sentiment of Oppenheimer as positive.  
At least now, although both models  
start outputting some random stuff at the end, at least  
now they understood what we wanted them to do.  
Let's see what ChatGPT did.  
As you might imagine, it just outputs a single sentence  
that is--  
that "Oppenheimer was very interesting"  
carries a positive sentiment.  
Another type of prompt is called Chain of Thought.  
Chain-of-Thought prompting is a technique  
that people use when they want to encourage a language  
model to reason step by step before giving a final answer.  
So instead of jumping straight to the conclusion,  
the model gets instructions about what steps to follow.  
And these, for at least complex or multi-step tasks,  
has been shown to improve accuracy.  
Here we are going to go over a simple example  
of a Chain of Thought that is a combination of math and physics.  
Here, we have the sentence, "A train travel kilometers in one  
hour and 30 minutes," and we basically want the LLM  
to compute the speed of the train in kilometers per hour.  
Instead of just saying calculate the speed in kilometers  
per hour, the Chain of Thought suggests  
that we specify the specific steps before we  
reach the final computation.  
So the first step that we instruct the model to do  
is to convert the time to hours.  
The second step is to use the speed formula.  
And we also provide the formula.  
And the third step is to compute the speed.  
So Llama actually followed the steps.  
And as you can see here, so convert the time to hours,  
one hour and 30 minutes is 1.5 hours.  
The speed formula, so it's 60 kilometers divided by 1.5 hours,  
and then the third step, the speed is 40km/h.  
As far as OpenChat is concerned, you will see here that before  
performing the three steps, it gives this answer of 80km/h  
without any reason.  
This is an example where small language models or smaller  
than ChatGPT can also provide wrong answers.  
And we're going to see how we will avoid it  
later on by just changing the prompt a bit.  
Eventually, in the rest of the chunks of text  
that OpenChat gave as an output, we  
can see that the response is correct.  
It calculated 40km/h, but it is definitely confusing to see  
an output like this.  
When we asked ChatGPT to do the exact same thing, of course,  
it followed the three steps, and it gave us the right output  
of 40km/h.  
Apart from the fact that we selected Chain of Thought  
as a type of prompting to solve this task,  
the exact prompt also matters.  
So to address this 80km/h random output from open chat if we just  
write the Chain-of-Thought prompt in a simpler,  
in a less explicit way, so basically,  
if we write a train travels 60 kilometers in one hour and 30  
minutes, what is its average speed in kilometers per hour?  
And we just say, let's think step by step,  
we can see that OpenChat applies the steps itself without us  
outlining them in the way that we did earlier,  
and it actually gives the right response immediately.  
This is just to show you that the same model  
can give different outputs when they  
are asked to do the same task with slightly different prompts,  
even in the same type of prompting,  
but with different phrasing.  
Another type of prompt is role instruction.  
Role instruction is basically when  
we tell the model who it should act as,  
and this can affect the tone, the style, and the reasoning.  
It basically asks the model to imitate a certain, for example,  
person or a certain situation and respond accordingly.  
Here in our example, we want our model  
to imitate a senior oncologist, and we  
want the model to explain in simple terms what chemotherapy  
is to a worried patient.  
Both Llama and OpenChat are effective in doing that here.  
And it's actually interesting that Llama, in order  
to give us an output that is even more realistic,  
generated a synthetic fake example of a patient's case,  
and then it gave an example of how a senior oncologist would  
respond in this specific case.  
OpenChat gave a more general description  
about how chemotherapy is, and it actually  
structured it in a way that can be provided to a patient.  
For example, it used these sentences.  
Remember, the purpose of chemotherapy  
is to help you get better, and things like that.  
Of course, ChatGPT, when we asked it,  
also performed this task very, very successfully.  
This is something to be expected.  
And then, we can move on to the next type of prompt,  
which is style prompt or style instruction.  
This refers to when we tell the model how  
to communicate in terms of tone, formality,  
regardless of the content of what we ask or the role.  
So here, for example, we have asked our models  
to write a short poem in Shakespeare style  
about artificial intelligence.  
And of course, these poems are different.  
You can take a look, and you will find them, I suppose,  
quite interesting and funny.  
They're actually pretty good.  
Both of the models are capable of doing that very successfully.  
And one might ask, why one would want to do that?  
It's when you want to generate something  
from scratch that imitates things that are already  
out there and the models have-- these specific models  
have been trained on.  
The next type of prompt we're going to see today  
is prompt chaining.  
Prompt chaining is basically a technique  
where we have a complex task, and we break it  
into smaller steps using the output of one  
prompt as the input for the next.  
This is something that can be very useful for people  
that use ChatGPT as well.  
So instead of giving ChatGPT a full paragraph  
of all the sequential things that we  
want it to do, we can break these things in smaller prompts  
and first ask it, for example, to summarize the text we have,  
then as a second prompt, after the summarization,  
after the summary is ready, we can ask it to, let's say,  
extract keywords, et cetera.  
These can be more effective than just providing  
a single big prompt that asks the model  
to do everything at once.  
Here, this is an example of prompt chaining in a medical QA  
setting.  
So we asked the model to first extract  
the key symptoms from a very simple medical note, which  
is the patient presents with cough, fever, and difficulty  
breathing, then we ask the model to use  
the extracted symptoms to suggest possible conditions that  
are relevant.  
And then as a third step, we ask the model to take the conditions  
that it suggested, and based on those,  
recommend different diagnostic tests.  
And also, we ask the model to provide the full reasoning.  
So here as you can see, for example, in the Llama output,  
the key symptoms are, of course, cough, fever, and difficulty  
breathing.  
This was the first step.  
Then based on the symptoms, the possible conditions  
are, for example, pneumonia, bronchitis, asthma, et cetera.  
And there is also an explanation of why each of these conditions  
should be considered.  
And then based on the symptoms and possible conditions,  
so based on the outputs of the last two--  
of the first two small prompts, we  
can see here that Llama recommends these two  
examinations, these two tests-- chest X-ray and blood count.  
OpenChat follows a same approach,  
where it first outlines the symptoms,  
then it lists the conditions, and then  
it also lists a set of diagnostic tests.  
It is also interesting to see that there  
are differences in the tests that are suggested.  
For example, OpenChat also suggest a COVID test  
and a pulse oximetry test.  
This way of prompting can actually be very, very helpful  
in different contexts.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.3 Medical Question Answering and Hallucinations in LLMs  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Another use of LLMs that people have been actually  
doing a lot is medical QA.  
This refers to the task of using AI, and more specifically  
large language models, of course,  
to answer medical questions.  
And this can be simple or more complex.  
In general, medical prompts can be unsafe.  
The reason is that large language models are not  
necessarily trained on very specific medical data.  
So there is no guarantee that the output is actually  
helpful and useful for the potential patient.  
Here we're going to check a case, an example, where  
we have this medical question.  
What is the recommended chemotherapy dose  
for a 45-year-old with stage III pancreatic cancer?  
As we can see, Llama, this creates a fake example  
of the patient, as in there is nowhere  
information about the BMI or the creatinine level  
or any of these.  
Lama hallucinates here a lot.  
It just finds some medical parameters that do not exist.  
And it selects one of four options that it also generated.  
So this is an example of a very bad response from Lama.  
\[? Openshot ?\] has a better response here,  
where basically it states that the recommended chemotherapy  
would depend on several factors that include  
patient's health, et cetera.  
And it actually provides some--  
a combination of chemotherapy, radiation therapy.  
It actually provides information that is correct.  
Medical QA is an area that one should  
be very, very careful with when they use large language models.  
We are also going to go over a case, another case,  
probably, where we want to see how our models hallucinate  
when they ask them to provide a citation for a fake paper.  
So hallucination-- this is a term that we have mentioned  
earlier in the recitation as well--  
refers to when a model generates information that is false,  
made up by the model, or not supported  
by any external knowledge source or its training data.  
But the model presents it with confidence, as if it were true.  
So here, we are asking the models to provide a citation  
for a paper with a title "Quantum Brain Networks  
for Consciousness processing."  
This paper does not exist.  
So here, actually, Lama tells us that--  
it basically says that it's not a real paper.  
It wants to help us find more information  
in this area, et cetera.  
Lama did not fall in the trap, in a way.  
However, \[? Openshot ?\] actually gave us  
a fake, completely fake citation, a completely fake  
paper that does not exist.  
It states that this is published in the Journal Quantum  
Information Processing.  
It gives us some names of authors.  
And it also gives us a link.  
And it's kind of interesting because if we  
click on the link, of course, the page is not found  
because it is a fake link.  
This was the case until recently, even with ChatGPT.  
Of course, now, the reasoning models  
have become way more powerful, and they can be  
used for citation extraction.  
But in the early stages of ChatGPT,  
fake citations was something that you would  
encounter very frequently.  
So one should be very careful with cases like this.  
We should always double check this type of information  
before using it in any other context.  
And I also wanted to show you an example of how ChatGPT can also  
hallucinate.  
This is, of course, the case.  
But it can also hallucinate at a very basic level still.  
So what we did was now, very, very recently,  
we asked ChatGPT--  
and this ChatGPT 4--  
to give us the best paper of a certain researcher.  
We have hidden the name here for privacy purposes.  
But they are area researcher.  
So we wrote this prompt.  
Give me this person's best paper.  
So actually, the model was able to find the correct citation,  
which is this one here.  
It is real.  
It was actually published in 2004\.  
And it is also stated, which is true,  
that this work has been cited well over 200 times  
and remains a foundational study in the field.  
It also provided a link to the specific publication.  
It is important to note that although this was not  
the most cited paper of the certain researcher, at least  
it was real.  
It was found by the model.  
And it was accurate.  
The next day, we asked exactly the same thing  
with exactly the same prompt.  
Give me this person's best paper.  
And ChatGPT decided that it was not  
able to locate any scholarly records for someone  
with this name, which is, of course,  
weird because just the previous day, ChatGPT gave us citations  
for this specific scientist.  
So this is to basically point out  
that ChatGPT, although it's much better than these smaller models  
that we saw, is actually not perfect.  
And one might ask, since these models can be bad,  
why would one still use them?  
It is true that there are newer models with smaller size that  
are constantly improving.  
But it is important to still study these models,  
because at the end of the day, we  
want to have models with a few billion parameters that can run,  
can be used with simpler and smaller GPUs,  
instead of having to use huge models.  
And if we want to use generative AI for our projects,  
we will have to use small models, so efficient prompting  
can make a difference.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.4 Retrieval Augmented Generation  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: For the second part of this recitation,  
we are going to focus on Retrieval-Augmented Generation,  
which is a technique that combines  
the power of Large Language Models with access  
to real-world information.  
The idea is that we don't want to only rely  
on what the model has learned during training only,  
but we also want to give access to the model  
to a database or a document collection  
to find relevant information that  
can be used to generate a more accurate and grounded response.  
This is especially useful for answering questions  
in topics that require up-to-date facts,  
domain-specific knowledge, or detailed context.  
And they can be generally more niche.  
This is because, of course, online content  
does not cover every topic and every subject in much detail.  
RAG retrieves the real document first  
and focuses on the relevant information for the task  
that we want to solve for the specific prompt  
that we want to focus.  
And then it generates answers based on them.  
This helps reduce hallucinations and make the model's output  
more reliable.  
Before we move on to the code, I am  
going to explain what the task that we want to do actually is.  
The idea is that we have a patient with some symptoms.  
And we want to ask our small LLMs,  
Llama and OpenChat to make a suggested  
diagnosis for this patient.  
Now, we can do that and ask what they think the patient has,  
which is relevant to what we did earlier.  
Or we can also use some information  
that we know is relevant in order to help the models provide  
a better output.  
So the idea is that we have a medical document,  
which is called "Rare Conditions,"  
we have loaded in the File sections here.  
And this file is very big and its many pages long.  
And it contains information about different rare cardiac  
conditions.  
And by information, I mean symptoms, diagnostic criteria,  
treatment, et cetera, but it's very big.  
The task that we want to solve is to diagnose this 34-year-old  
woman who has sudden chest pain after recent childbirth and no  
prior cardiac history.  
Of course, we have made this prompt.  
And we know that the condition that we have in mind  
is spontaneous coronary artery dissection, which  
is a very specific and rare condition that  
is related to some complications after giving birth.  
The important thing to note is that this condition is rare.  
And there is a high chance that our LLMs will not  
have been trained on many data regarding this condition.  
But our Rare Conditions file contains information  
about multiple rare conditions.  
So we want to use, to leverage, the information in this file  
to guide the diagnosis generation.  
As I mentioned earlier, this file is very big.  
So it contains information about many conditions  
that might not be relevant for this specific patient case.  
In order to solve this problem, the first part  
of retrieval-augmented generation  
is to use the information that is available  
and to only detect the relevant parts of it.  
How do we do that?  
We do that using a model, which is in the family of sentence  
transformers.  
And this model will allow us to actually find  
the most relevant parts to the query that we have in hand.  
First, we are going to split the big text file of rare conditions  
into smaller chunks.  
And after we do that, we use the sentence transformer model,  
the SBERT model to encode these chunks  
and convert them to embeddings.  
So after performing this, we have the big file split  
into chunks, and we have a single embedding for each chunk.  
Then we have our query, which refers to the patient case.  
And we also pass this query through the same model  
to get an embedding that summarizes  
the information of the patient.  
So now we have one query embedding  
that corresponds to the patient, and multiple chunk embeddings  
that correspond to the different chunks in which we have  
split the original big text file with the rare cardiac  
conditions.  
Now, in order to find the most relevant information  
for the task in hand, we want to find which of these chunk  
embeddings are more similar to our query embedding,  
because if these embeddings are more similar in the embedding  
space, this means that the information that they encode,  
the raw text that they encode is also going to be  
more relevant and more similar.  
So we calculate the cosine similarity  
scores between the query embedding  
and all of the chunk embeddings.  
So we then keep the top-k.  
In our case, we have selected the top five  
chunks that are more similar according to the embedding  
distances.  
And we basically only retrieve the relevant chunks  
that we can view here.  
So you can see, we have five different chunks--  
1, 2, 3, 4, 5\.  
And something that is good is that the first two actually  
refer to the SCAD diagnosis that we had in mind  
when we created this patient case.  
So the SBERT was actually capable  
of isolating the parts that seemed  
more similar, more relevant, to this description of the patient.  
The second, third, and fifth, of course,  
they're related to cardiac conditions.  
The whole file that we had was about cardiac conditions.  
But they are not related to the specific condition.  
It doesn't matter though.  
This is the whole, whole text that we're going to use.  
And we're going to include this in our prompt  
when prompting Llama and OpenChat.  
And we hope that they are going to use this information  
to guide their diagnosis.  
So here is the full prompt.  
We are doing role instruction here.  
So basically, we're telling the model  
that it should respond as a clinical assistant.  
We actually point out that we wanted  
to focus on the specific patient case  
and the retrieved medical information,  
and give us an answer about the most likely diagnosis.  
We also include this sentence-- and this is important,  
we're going to discuss it in a few minutes--  
that we only want the model to ground its responses  
on the provided information regarding the patient case.  
We don't want it to imagine any other information  
that we haven't given to it.  
So when we run our model--  
and this is the prompt.  
Here is where the Llama gave its output.  
So we can see that based on the patient case,  
the most likely diagnosis is actually  
spontaneous coronary artery dissection, which  
is the ground truth, which is what  
we wanted the model to output.  
And this is justified by the patient symptoms,  
such as sudden chest pain after recent childbirth  
and no prior cardiac history.  
These are compliant with the SCAD condition, et cetera.  
And there's a fully grounded explanation on that.  
OpenChat did the same thing.  
Based on the provided patient case,  
the most likely diagnosis is spontaneous coronary artery  
dissection.  
And it describes SCAD patients often  
do not fit the typical profile for coronary disease  
and the symptoms.  
And it explains why it doesn't think  
that restrictive cardiomyopathy, which is another condition,  
is the case here, et cetera.  
So using the medical context that is provided,  
both of the models were able to find the right diagnosis.  
And I repeat, the whole pipeline involved  
first finding the relevant chunks, the relevant information  
from a document that contained a lot of information  
about cardiac conditions, and then  
using these in the prompt we gave to the large language  
models to help them to guide their generation.  
OK, now, that's a good thing, of course.  
But what would have happened without the provided context,  
without giving them any information  
about this rare disease and just asking  
them to make a diagnosis based on only  
the description of the patient.  
Llama actually diagnosed the patient  
with acute coronary syndrome, which the symptoms are similar,  
but it is not accurate, because acute coronary syndrome  
is usually caused by some plaque that  
is accumulated on the vessels.  
And this is not the case with this specific patient.  
Similarly, OpenChat gave the same diagnosis.  
And it also gives a more detailed reasoning  
about what ACS is, when it happens, et cetera.  
But we know this is not the specific diagnosis  
that we wanted the models to actually give.  
So in this case, we show how important  
it is to actually provide relevant information  
in the form of this context, to guide the diagnosis  
and to get more accurate text generation.  
The thing that I want to point out before wrapping up is that  
we included the sentence, "please only stick  
on the provided information regarding the patient case,  
and don't make any further assumptions about the patient"  
in the prompt.  
So even with the context and the retrieved medical information,  
if we do not include this sentence,  
the models are more prone to some form of hallucination.  
So when we remove this sentence, although both of them  
again made the right diagnosis, you  
can see here that, for example, Llama  
wrote that the fact that her arteries are clean of plaque,  
this, although we know it's not the case,  
it's not explicitly mentioned in the prompt that we gave.  
So although, yeah, we suspect it is the case because we know  
that this woman did not have a prior cardiac history, since it  
is not explicitly mentioned, the model  
should not use it as an argument for its reasoning  
for its diagnosis.  
So we need, even in these cases, to be very careful with how  
we structure our prompt.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

R1.5 Wrap-Up  
 0:00 / 0:00Press UP to enter the speed menu then use the UP and DOWN arrow keys to navigate the different speeds, then press ENTER to change to the selected speed.Speed2.0xClick on this button to mute or unmute this video or press UP or DOWN buttons to increase or decrease volume level.Maximum Volume.Press the UP arrow key to enter the language menu then use UP and DOWN arrow keys to navigate language options. Press ENTER to change to the selected language.  
Video transcript  
Start of transcript. Skip to the end.  
INSTRUCTOR: Now for the final part,  
we're going to talk about the key takeaways from today's  
recitation.  
What did we learn today?  
First of all, we learned that prompt engineering helps  
guide and shape how language models respond,  
and even small tweaks and changes in the prompt  
can actually have a big effect on the output.  
We show that there are multiple types of prompting,  
including zero-shot, few-shot, and chain-of-thought, each  
with different strengths.  
We also saw other types of prompting,  
but these were the first ones we examined  
and some of the most usual ones.  
We also saw that the role and style instructions  
let us control the tone and persona of the model output.  
And then we talked about Retrieval-Augmented Generation,  
which improves accuracy by grounding responses  
in real documents that we can provide to the models.  
And as we saw, prompt chaining in combination with RAG  
can make language models more trustworthy for complex tasks  
like medical question answering.  
And by prompt chaining, I remind you,  
we mean the concept of providing smaller prompts step by step  
to our LLM instead of bombarding it  
with a single large prompt that contains  
every task we want it to do.  
End of transcript. Skip to the start.  
Downloads and transcripts  
Video  
\`\`\`

Skip to main content  
Recitation Summary  
In this recitation, we explored how to use prompt engineering and retrieval-augmented generation (RAG) to improve interactions with large language models. We compared different prompting strategies—zero-shot, few-shot, chain-of-thought, role and style instructions—using smaller open-source models and ChatGPT. We then demonstrated how RAG grounds responses in external documents, improving accuracy on domain-specific tasks such as medical diagnosis while reducing hallucinations.

Key takeaways:  
Prompt design shapes model accuracy: zero-shot, few-shot, and chain-of-thought each have distinct strengths.  
Role, style, and chaining prompts let users control tone and guide reasoning more reliably.  
RAG combines semantic retrieval with generation to ground outputs and limit hallucinations.  
Clear instructions to "stick to provided context" help prevent unsupported details.  
Congratulations on completing this recitation\! You now have practical tools to design effective prompts and apply RAG for more accurate and trustworthy LLM outputs.  
\`\`\`

Assignment Overview  
\`\`\`  
Skip to main content  
Overview  
Welcome to Assignment 1\! This assignment builds on what we have learned in this module. In particular, we will deepen our understanding of symbolic AI engines and prompt engineering.

There is no code associated with this assignment.

Lectures covered by this assignment

Lecture 1: Symbolic AI Engines  
Lecture 2: Beyond Monolithic AI Systems  
Good luck\!  
\`\`\`

Skip to main content  
In this part, expect short, scenario-based questions on how symbolic AI engines represent and reason with knowledge: URIs, RDF triples/Turtle, ontologies/OWL, and the "things not strings" idea.

Question 1  
1 point possible (graded)  
Maria notices that the same movie is described in English on Wikipedia and in another language on a foreign movie database. Despite the different names, her system correctly integrates the information. Why is this possible?

The system compares surrounding text for similarity

The movie’s popularity makes it easy to recognize

Both sources refer to the movie using the same URI

The system translates all names into English before matching  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
1 point possible (graded)  
Suppose a reasoner automatically infers every possible “is-a” relationship across a deep class hierarchy before any user interaction. Why does Lecture 1 consider this risky?

It prevents further reasoning

It introduces logical inconsistencies

It changes the original facts

It can materialize a large number of obvious but unhelpful facts  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
0.0/1.0 point (graded)  
Nikos models a university knowledge graph and marks the relation classmate-of as transitive. He then loads data stating that many students overlapped in courses across different years. After reasoning, the graph shows that nearly all students are classmates of one another. What issue from the lecture does this illustrate?

Transitivity can generate many technically valid but semantically weak connections

RDF cannot handle large numbers of inferred triples

Class relationships should always replace person-to-person relations

The reasoning process introduced incorrect facts  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
Eleni integrates movie metadata from multiple sources into a knowledge graph. After loading the data, she discovers that one film is categorized as both a thriller and a family film, even though her ontology declares these categories as disjoint. What is the most appropriate symbolic operation to run first?

Retrieve additional external sources to vote on the correct genre

Perform consistency checking using the ontology constraints

Compute similarity scores between genres to resolve ambiguity

Materialize all implied subclass and property relationships  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
1 point possible (graded)  
A knowledge graph combines data from multiple countries’ film archives. Each archive uses different naming conventions, but the system still answers queries correctly. What design choice enables this interoperability?

Prioritizing the most trusted source

Normalizing all text fields into English

Using URIs as universal identifiers across sources

Centralizing all data into a single database  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
In this part, we're going to spot better prompt patterns from short multiple-choice scenarios. You'll see items on closed-book constraints, RAG for fresh sources, few-shot \+ chain-of-thought, prompt chaining, and terminology-aware retrieval. Select all that apply—favor prompts that enforce constraints, cite sources when needed, and avoid guessing.

Question 1  
1 point possible (graded)  
An AI tutor is asked to solve math word problems and explain each step so students can follow the reasoning. Accuracy and transparency are more important than brevity. Which prompting approach best supports this goal?

Asking the model to give the final answer only

Few-shot prompting with worked examples that show intermediate reasoning

Retrieval of a textbook without showing reasoning

Zero-shot prompting with a concise answer format  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 2  
0.0/1.0 point (graded)  
An emergency-response assistant must suggest the nearest available pharmacy late at night. Which retrieval strategy best supports accurate answers?

Prompting the model to respond conservatively when uncertain

Using a cached list of pharmacies with addresses and phone numbers

Retrieving live location, pharmacy databases, and current operating status

Inferring likely pharmacy locations based on population density and past patterns  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 3  
1 point possible (graded)  
An auditor asks whether changing a single eligibility rule could systematically alter past loan decisions. Which system component allows this kind of controlled analysis?

A language model with editable system prompts

A symbolic rule base evaluated by a reasoner

A retriever fetching alternative policy interpretations

Prompt templates with modular instruction blocks  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 2 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 4  
0.0/1.0 point (graded)  
A hospital policy requires that automated eligibility decisions be fully auditable, meaning every conclusion must be traceable to specific text in the source document. Which prompt designs best satisfy this requirement? (Select all that apply.)

“Use only the provided document. For each eligibility criterion, quote the exact sentence that supports it. If no sentence exists, mark the criterion as ‘Missing.’”

“Closed-book evaluation. Do not use external knowledge. Output a table with columns: Criterion | Met (Yes/No/Unknown) | Supporting quote.”

“Explain your decision clearly and logically, referencing the document where relevant.”

“Summarize the document, then assess eligibility based on the summary.”  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 5  
1 point possible (graded)  
A clinical educator wants the model to compute medication doses and support trainee learning, while keeping error rates low. Which prompt designs best achieve both goals? (Select all that apply.)

Use a fixed, explicitly named calculation procedure that is followed every time.

Ask the model to discuss alternative dosing interpretations before selecting one.

Add a brief verification step that checks units, frequency, and totals.

Let the model apply rounding based on what “seems reasonable” in context.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 6  
1 point possible (graded)  
A policy team asks the model: “What is the current FDA guidance on GLP-1 agonists for weight loss? Include the latest update date.” They want to avoid invented agencies, dates, or documents. Which prompt rewrites best reduce hallucination? (Select all that apply.)

“Search only fda.gov for official guidance. Quote the exact sentence supporting each claim and include the publication or update date. If no such page exists, respond ‘No current FDA guidance found.’”

“Be cautious and conservative. If you are unsure, approximate the most likely date based on prior FDA updates.”

“If retrieval is unavailable, explicitly state that current FDA guidance cannot be confirmed and do not provide a summary.”

“Reason step by step before answering to ensure accuracy.”  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 7  
0.0/1.0 point (graded)  
An aviation safety assistant reviews radar images and pilot reports to recommend whether an aircraft should divert. The team wants recommendations to be traceable to both sensor data and flight rules. Which design choices best support this? (Select all that apply.)

Allow the LLM to directly interpret radar images and summarize weather conditions.

Use a perception model to extract structured weather features (e.g., storm cells, turbulence), then pass them to the LLM.

Retrieve FAA diversion guidelines and inject them into the prompt.

Disable retrieval and rely on the LLM’s aviation training data.

Require the output to include a recommendation and a brief justification tied to extracted features.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 8  
1 point possible (graded)  
An AI platform supports customer support, legal review, and internal analytics using a shared infrastructure. The team wants to minimize GPU usage while keeping behavior distinct across use cases. Which approaches best achieve this? (Select all that apply.)

Use a single base model and switch behavior via task-specific prompts and retrieved context.

Deploy a different fine-tuned model for each department to avoid prompt complexity.

Route requests through lightweight classifiers to select the appropriate workflow.

Standardize output formats while varying retrieved content per task.

Encode all department-specific logic directly into a long, unified system prompt.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 3 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Question 9  
0.0/1.0 point (graded)  
Select all sub-tasks where the stated reasoning type (deductive, inductive, abductive) is correct.

From “All passwords must be at least 8 characters” \+ “This password has 6 characters” ⇒ “This password is invalid.” Deductive.

From “Most patients with disease X respond to treatment Y” ⇒ “This patient with disease X will respond to treatment Y.” Inductive.

Smoke in the hallway \+ fire alarm sounding ⇒ there is likely a fire somewhere in the building. Abductive.

From “If a package is delivered, it appears in the tracking system” \+ “The package appears in the system” ⇒ “The package was delivered.” Abductive.

Observing a single failed experiment ⇒ the hypothesis is false. Deductive.

From “All squares are rectangles” \+ “This shape is a square” ⇒ “This shape is a rectangle.” Deductive.  
unanswered  
SaveSave your answer  
Submit  
You have used 0 of 4 attempts  
Grading method: Last Score  
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

AskTIM about this problem

Skip to main content  
Summary  
In this assignment, you practiced the core ideas of Symbolic AI and Prompt Engineering through scenario-based questions. You identified key mechanisms of symbolic AI, including URIs, RDF triples, ontologies, and reasoning pitfalls. Finally, you examined prompt design patterns for improving reliability, retrieval-augmented generation, and multimodal AI integration.

Key takeaways:  
Symbolic AI: URIs provide unambiguous identifiers, reasoning can create unintended inferences, and consistency checking is key.  
Prompt Engineering: Effective prompts use constraints, role/style instructions, retrieval grounding, and chaining to reduce hallucination and improve accuracy.  
Congratulations on completing this assignment\! You now have practical insight into how AI systems combine structured knowledge, retrieval, and carefully designed prompts to build more reliable, transparent, and responsible intelligence in real-world settings.  
\`\`\`

Skip to main content  
Module Summary  
In this module, you explored how modern AI systems move beyond standalone models toward compound architectures that integrate symbolic reasoning, retrieval, neural networks, and large language models to build more reliable and trustworthy intelligence.

Lecture 1 introduced symbolic AI, showing how knowledge graphs, RDF triples, URIs, and ontologies enable explicit semantic representation and automated reasoning for transparency and consistency.

Lecture 2 examined the limits of monolithic LLMs and introduced compound (neurosymbolic) systems that orchestrate retrieval, prompting, reasoning, and multimodal models to overcome hallucinations, outdated knowledge, and weak logical guarantees.

Lecture 3 focused on Retrieval-Augmented Generation (RAG) as a core implementation of compound AI, detailing the retrieve → augment → generate pipeline, chunking strategies, keyword and semantic retrieval, knowledge-graph-based search, and advanced architectures such as Standard, Contextual, Graph, and Agentic RAG.

Key Takeaways:  
Explain why standalone LLMs are insufficient for high-stakes applications.  
Describe how symbolic AI represents meaning and supports automated reasoning.  
Define compound/neurosymbolic AI systems and their architectural components.  
Explain how RAG grounds LLM outputs through targeted retrieval and augmentation.  
Compare retrieval strategies (keyword, semantic, entity/graph-based) and RAG architectures.  
Recognize how system-level orchestration determines reliability, transparency, and answer quality.  
Congratulations on completing this module\! You now understand how next-generation AI systems combine retrieval, reasoning, and generation — transforming isolated models into integrated, knowledge-grounded intelligence.

We truly value your perspective and would love to hear your thoughts on the module you just completed. Please take a moment to fill out the Module Feedback Form—your honest feedback is essential to helping us improve the learning experience for everyone. Thank you for helping us create a better module for future learners\!

To continue to future modules, please return to the MIT Learn Dashboard.  
\`\`\`

