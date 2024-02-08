<center>
<h1> Retrieval-Augmented Generation (RAG) enabled LLM Application</h1>
<h3><b>Varad V. Deshmukh</b></h3>
<i>Data Scientist - Machine Learning / MLOps Engineer - AI Prompt Engineer</i>
</center><br>
------------------------------------------------------------------------------------

This is the repository for a LLM-powered AI solution for performing in-depth financial research and analysis. This system is based on Retrieval-Augmented Generation (RAG), utilizing a locally run `Llama2-7b-chat` LLM, developed by Meta and the `UAE-Large-V1` text embedding model developed by WhereIsAI. This system uses completely open-source components and takes care of the data security considerations as well, by hosting everything on a local system.
<br>

<b>What is RAG?</b>
<p>Large Language Models (LLMs) are trained on an enormous corpus of data, e.g. Wikipedia pages, software/hardware technical documentation, blogs, etc. But, they are not trained on our personal data. One of the solutions to this issue is to fine-tune the model with our data. This involves altering the neural network architecture that lies underneath the model, including adding some layers and removing some. This altered model is then trained on our data. This appears as a promising approach but has certain drawbacks -</p>

1. Training an LLM is expensive.
2. Due to the high costs associated with training them, its very difficult to continually update them with the latest data.
3. Observability is lacking, implying that we have no means to peek into the process by which the model arrived at the response.

<p>Retrieval-Augmented Generation (RAG) is an alternative, transformative paradigm that works around these problems. Instead of asking the model to generate the response directly, RAG first retrieves information from our data sources, adds it to the context of our query and then asks the model to answer the query based on the enriched prompt. RAG overcomes all three weaknesses of the fine-tuning approach -</p>

1. There is no training involved, so it's <b>cheap</b>.
2. Data is fetched only when you ask for it, so it is <b>always up to date</b>.
3. We can see the documents from where the model retrieved its response, so it is <b>trustworthy</b>

<p>RAG adds our data - stored in varied formats such as text documents, pdfs, images, videos, audios, etc. - to the data LLMs already have access to. Our data is loaded and prepared for queries, i.e. 'indexed'. Almost always, this entails converting it to vector embeddings, which are numerical representations of the data concerned. User queries, or the questions that we want the model to respond to, generally through prompts, act on this indexed data. The RAG approach filters down the data down to the most relevant context, i.e. it chooses which document sources are the most relevant to answer the question at hand. This context and our query then go to the LLM in the form of a prompt, to which the model generates a response.</p>

<b>Stages within RAG</b>

There are five key stages within RAG, which are to be incorporated into any LLM application that we build -

1. <b>Loading</b> : getting our data from where it lives - text files, PDFs, a website, a database or an API - into the pipeline

2. <b>Indexing</b> : converting the data into a format suitable for querying, which almost always is a vector embedding, incorporating the semantics of our data as well as the necessary metadata

3. <b>Storing</b> : storing the indexed data, i.e. the embeddings into a vector database, to avoid having to re-index it

4. <b>Querying</b> : prompting the RAG-enabled model to answer a specific user query, to which it returns a context-aware response, along with the citations to the source documents

5. <b>Evaluation</b> : checking the efficacy of the RAG pipeline and objectively measuring how accurate, faithful and fast the model responses are
