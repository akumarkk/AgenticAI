##### questions
1. Crew AI
```
Crew(
    agents = [],
    tasks = []
)\

task1 = ConditionalTask(
    description = "",
    expected_output = "",
    agent = reviewer,
    confidence = is_low_confidence
)

crew exists at task 1 if is_low_confidence is true;

```

    + crew of agents, with assigned roles and resp; run them in struct. workflow
        + Rsearcher, Summarizer, reviewer
    + compsability and clear role definitions
    
    - limits fine grained control over state transitions



2. 