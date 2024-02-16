# function for retrieval and reranking of source nodes, based on the query
def retrieval_rerank(prompt):
    '''
    Returns the retrieved and subsequently reranked source nodes.
    Reranking is done using the similarity scores.
    
    Inputs : prompt (str) = query to the engine
    Outputs: nodes (Node) = reranked nodes
    '''
    
    # retrieval
    retrieved_nodes = hybrid_retriever.retrieve(prompt)
    # reranking
    reranked_nodes = reranker.postprocess_nodes(
    retrieved_nodes,
    query_bundle=QueryBundle(prompt))

    for node in reranked_nodes:
        display_source_node(node)

    return reranked_nodes


# function to filter the reranked source nodes based on a similarity threshold
def filter_nodes(reranked_nodes, threshold=0.5):
    '''
    Filters the reranked source nodes, based on a similarity threshold.
    
    Inputs : prompt (str) = query to the engine
    Outputs: nodes (Node) = reranked nodes
    '''
    # filtering out irrelevant nodes
    filter = SimilarityPostprocessor(
        similarity_cutoff=threshold)
    filtered_nodes = filter.postprocess_nodes(
        reranked_nodes,
        query_bundle=QueryBundle(prompt))

    for node in filtered_nodes:
        display_source_node(node)

    return filtered_nodes


# function to print the source nodes in Markdown format
def display_nodes(nodes):
    '''
    Prints the source nodes.
    
    Inputs : nodes (List(Node)) = source nodes
    Outputs: reranked nodes printed in Markdown format
    '''
    
    for node in nodes:
        display_source_node(node)


# response generation query engine
def generate_response(prompt, filtering=True, streaming=True):
    '''
    Builds the query engine and generates the response in Markdown format.
    
    Inputs : prompt (str) = query prompt,
             filter=True (bool) = were the reranked nodes filtered based on a similarity threshold?
             streaming=True (bool) = allow streaming of response?
    Outputs: response
    '''
    if streaming==True:
        stream=True
    else:
        stream=False

    query_engine = RetrieverQueryEngine.from_args(
        retriever=hybrid_retriever,
        node_postprocessors=[reranker, filter] if filtering==True else [reranker],
        llm=llm,
        streaming=stream)

    # response generation
    response = query_engine.query(prompt)

    if stream==True:
        response.print_response_stream()
        response.get_formatted_sources()
    else:
        display_response(
            response=response,
            show_source=True,
            show_source_metadata=True)
        
    return response

