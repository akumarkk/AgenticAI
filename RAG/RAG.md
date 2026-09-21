##### RAG
1. Query augmentatin and retrieval


###### RAG assistant/assistant failure
misunderstands the question, misses evidence and improvises

- user : jira access outside India;
- Detected : detected "Jira" and "access" keywords
- retrieved : generic vn doc
    - irrelevant IT checklist

RC : misses security waiver policy;
 - model starved off context

 weak retrieval : results in unreliable generation;
 strong retrieval : enable accurate generation synthesis;

 1. query tranlation example:
    - expanded intent with finance plicy keywords
    - applied filters like date and role
    - improved translation by injecting better context;
    - metadata filters - like country = India

2. Augmentation (post-retrieval)
    - combining the retrieved raw data/documents with the user's original query to feed into the llms;