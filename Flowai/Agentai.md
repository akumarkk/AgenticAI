##### Token management

- allocate input budget
- prevent automatic data cutoff problems
- balance instruction, history, retrieval, and output reserve;


###### strategies 
1. truncastion approach: 
2. summarization approach: compresses older content into shorter repr;
    - summary drift over many turns
3. Sliding window: retianing recent messages in details, releasing older context as windows moves; immidiate nuances;
4. context Injection: inject context dynamically, not statically;  loc;d workflow context for approval queries; include policy/data based on intent;

###### Solution
- context window problms are arch problems;
- externize shared memory store, instead of carrying cntext in the prompt;
- boundary conditions; token budget = cpu/mem budget;
