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
+ Recursive chunking : not at arbitrary doc point, splits by boundaries like headings, paragraphs, sent, list items etc;
    + each unit is more coherent, self-contained;
    + preserves semantic boundaries, in policy, technical manuals, structured documentation;
+ Semantic chunking;
    + actual changes in meaning, embedding acrtoss ruling window of text
    + llm : segment into topic consistent sections, gets coherent chunks from messy documents
    - processing costs;


###### Chunksize and overlap
descrip: the practice of repeating a specific portion of text at the end of one chunk and the beginning of the next;

+ adjust chunk size to control the retrieved context
+ set the ovrelap to preserve continuity across chunks

- increases index size and duplicates with ovrelap
+ implement deduplication and reranking for accuracy;


###### embeddings
+ captures semantic similarity, with vector proximilty;
+ nns in multidimension space;


###### prompt dilution
+ blend unrelated topics in a single chunk;
+ embeddings of such chunks  match multiple queries, but precisely to none;

##### Semantic visualiation for chunking
Embedding projectors—like TensorBoard Projector or Nomic Atlas—are effective tools for visualizing chunk boundaries. They allow you to project high-dimensional chunk vectors into interactive 3D/2D space (using UMAP, t-SNE, or PCA) and examine topic clusters and outliers.

+ visualize embeddings with tools like embedding projectors;
+ observe clusters forming in the data
+ identify the content clusters like security and HR



