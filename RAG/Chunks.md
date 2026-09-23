##### Chunking

+ fundamental unit of retrieval
+ serves as context engg decision;

1. retrieval failures caused by poor chunking;
2. appropriate chunking strategies for document types;;
3. evaluate vector databases, based on functional requirements;

###### Failure pattern
- Retriever - finds the right chunk, but the ans are buried under unrelated sections
- model - struggles to generate clear answers;



###### Chunking strategies
+ Fixed size chunking : splits the text by a hard token count;with overlap;
    + remains as baseline, not the final approach
    + afqs, short articles;
    - limitations
        - splits the sent. in the middle
        - separates a section heading from gov. paragraphs
        - divides a num. list into separate chunks
+ Recursive chunking
+ Semantic chunking;


