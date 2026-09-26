###### Types of ai agents

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