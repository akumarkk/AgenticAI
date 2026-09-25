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



2. LangGraph
    Groups and state machines; dterministic control
  + RANDOM TOOLS, inspect state in each node, inspect token budge etc

  ```
# 5. Build the Graph
builder = StateGraph(State)

# Add nodes
builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

# Add edges
builder.add_edge(START, "chatbot")

# Conditional edge: if the model calls a tool, route to "tools", else END
builder.add_conditional_edges("chatbot", tools_condition)

# Loop back to chatbot after tool execution
builder.add_edge("tools", "chatbot")

# Compile the graph
graph = builder.compile()
  ```
Limitations
- more upfront design, boilerplate, and stirct state schema;

3. Autogen
    Agent conversation
    + agent1, agent2 argues; agent3 judges;
    + 
