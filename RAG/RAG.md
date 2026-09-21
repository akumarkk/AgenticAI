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

    - HyDE (Hypotheticasl Document Embeddings) - generate hypothetical answers;

2. Augmentation (post-retrieval)
    - combining the retrieved raw data/documents with the user's original query to feed into the llms;

###### model, okay
- right evidence lets modest models perform brilliantly., wrng evidence makes the best models misleading;
- retrieval backbone of any RAG system, query transformation and multi-qery strategies 


#### Query rewritting : retrieval effectiveness, not creative writing;
*clearer, canonical retrieval requests*

1. Query rewritting -Multi query retrieval - query and retrieve separately;
    a. Multi query retrieval - query and retrieve separately;
    multi-query ret req:
    - semantic search may lacks precision;
    - embeddings capture meanings but blur specifics;

    benefits of multi-query ret:
    - increases diversitry and boosts recall
    - prevents system from narrow interpretations;

    - tradeoffs : cost, latency

        - 
2. Query expansion - laptop refreshments vs asset refreshments; 
    - bridge vocabulary gaps for better retrieval;
    - Query expansion approach : generate targetted synonyms, related termsd and append synonyms or turn into parallel queries;
    - example : Atlassian access, project management tool access, sso group membership etc

3. HyDE - Hypothetical Document embedding;
    - embed generated text, not raw questions; use generated embeddings as retrieval queries;
    - how do we handle lost access cards? 
        - keywords missed : physical badge, facility access credential, security incident, replacement fee;
        - HyDE Hypothetical paragraph
            employee who lose a facility access badge must report to security within 24 hours, submit an incident report, and request a replacement through facilities;
    - uses hypothetical text for evidence retrieval only; grounds the final answer in retrieved chunks;

4. Decomposition 
    - how do i setup sso for our vendor portal?
        - sso protocol requirements
        - identity providfer configuration
        - security review steps
        - vendor onboarding approvals

Query to query pipelines:
- query transformation
- expansion
- HyDE
- Decomposition
- multi-query

Guardrails for 