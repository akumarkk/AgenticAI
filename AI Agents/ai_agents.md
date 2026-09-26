###### Types of ai agents
Stuart Russell and Peter Norvig authored "Artificial Intelligence: A Modern Approach" (AIMA), the standard textbook used across the field.   Their framework defines AI around the concept of "Rational Agents"—systems that take in percepts from an environment and choose actions to maximize expected performance.   The classical taxonomy of agent architectures (Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, and Learning Agents) comes directly from Chapter 2 of their book.

```

```

| Category | Agent / Paradigm | Real-World System | Category Rationale (Why it fits here) |
| :--- | :--- | :--- | :--- |
| **Classical** | **Simple Reflex** | **Smart Thermostat** | Operates strictly on instantaneous sensor thresholds (e.g., if temp > 72°F → turn on AC). It has no memory of past temperatures and does not predict future conditions. |
| **Classical** | **Model-Based** | **Robot Vacuum** | Keeps an internal memory (a spatial map) of where it has already cleaned and where obstacles are located, allowing it to function when areas are out of direct sensor view. |
| **Classical** | **Goal-Based** | **GPS Navigation** | Evaluates long sequences of future actions (turn-by-turn routes) to reach a explicit end target (the destination), ignoring options that don't lead toward the goal. |
| **Classical** | **Utility-Based** | **Rideshare Surge Pricing** | Weighs trade-offs using a mathematical scoring function to maximize a objective (balancing driver availability, rider wait times, and profit margin) rather than just reaching a single binary goal. |
| **Classical** | **Learning Agent** | **Recommendation Engine** | Continuously updates its internal preference weights based on real-time user feedback (clicks, watch time, skips) to improve future performance over time. |
| **System Struct.** | **Multi-Agent (MAS)** | **Automated Code Pipeline** | Uses specialized, autonomous agents (e.g., Coder, Tester, Security Auditor) that exchange messages and negotiate to finalize a pull request. |
| **System Struct.** | **Hierarchical** | **Enterprise Task Automation** | A manager agent receives a complex objective (e.g., "Launch Marketing Campaign"), breaks it into sub-tasks, and delegates them to worker agents (e.g., Copywriter, Image Generator). |
| **Modern** | **Generative AI** | **Large Language Models (LLMs)** | Generates entirely new sequences of text, code, or images based on learned underlying statistical patterns from massive training datasets. |
| **Modern** | **Predictive AI** | **Credit Scoring Systems** | Analyzes historical data features to output numerical probabilities or classifications (e.g., risk of default) rather than taking actions or generating creative content. |
| **Modern** | **Autonomous (ReAct)** | **AI Coding Assistants (e.g., Devin)** | Iteratively reasons about a problem, formulates plans, executes terminal commands or APIs, reads errors, and self-corrects in a loop until the job is done. |
| **Modern** | **Embodied AI** | **Self-Driving Vehicles** | Fuses real-time physical sensor data (LiDAR, cameras) directly with motor control outputs to interact safely with the physical world in real time. |

###### AI agent lifecyle

    ┌────────────────┐       ┌────────────────┐       ┌────────────────┐
    │ 1. Spec & PEAS │ ───>  │  2. Design &   │ ───>  │ 3. Development │
    │   Definition   │       │ Architecture   │       │  & Tooling     │
    └────────────────┘       └────────────────┘       └────────────────┘
            │                                                 │
            │                                                 ▼
    ┌────────────────┐       ┌────────────────┐       ┌────────────────┐
    │ 6. Maintenance │ <───  │ 5. Production  │ <───  │ 4. Evaluation  │
    │  & Adaptation  │       │   Deployment   │       │   & Guardrails │
    └────────────────┘       └────────────────┘       └────────────────┘

    
##### The Agent Execution Loop

| Stage | Core Responsibility | Key Sub-Mechanisms | Classical AI Root | Modern LLM / Agent Primitive | Primary Failure Mode |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Goal Setting** | Defines the explicit success criteria, constraints, scope, and target state of the agent system. | - Constraint specification<br>- Utility function mapping<br>- Intent clarification | **BDI Architecture** *(Desire)* & **PEAS Framework** *(Performance Measure)* | System Prompts, Structured Output Schemas (e.g., Pydantic), User Goal Alignment | Scope creep, ambiguous criteria, misaligned utility weights |
| **2. Planning** | Decomposes high-level goals into an ordered, executable sequence of sub-tasks and dependency graphs. | - Hierarchical Task Networks (HTN)<br>- Sub-goal decomposition<br>- Multi-path reasoning | **STRIPS Planning**, **A* Search**, & **Dijkstra's Algorithm** | Chain-of-Thought (CoT), Tree-of-Thoughts (ToT), Plan-and-Solve | Infinite planning loops, hallucinated dependency steps, fragile step ordering |
| **3. Data Gathering** | Retrieves real-time context, environment observations, and missing facts required for execution. | - RAG / Vector search<br>- API perception<br>- Environment sensing | **Perceptual Processing** & **Belief State Updates** | Tool Calling (e.g., Search, SQL, Web Scraping), In-Context Memory Retrieval | Information overload (context window bloat), retrieval of stale/hallucinated data |
| **4. Execution** | Invokes external tools, runs code, or generates artifacts to change the state of the system or environment. | - Function calling<br>- Code execution sandboxes<br>- API orchestration | **Actuator Operations** & **Condition-Action Rules** | ReAct Action Phase, Function/Tool Calling, Code Interpreter Runtime | API rate limits, tool execution errors, unauthorized state changes |
| **5. Optimization** | Evaluates intermediate outputs against goal criteria, detects errors, and adjusts future execution trajectories. | - Self-reflection / Criticism<br>- Error backtracking<br>- Dynamic re-planning | **Reinforcement Learning** *(Reward Signals)* & **Adaptive Control** | Reflexion Loops, Self-Correction Prompts, Trajectory Evaluation (Evals) | Error propagation (hallucinating success), over-correcting, high token cost |

1. Goal setting
2. Planning
3. data gathering
4. execution
5. optimization
