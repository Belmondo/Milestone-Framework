# Milestone Framework Public Repository

**MILESTONE: A Framework for Continuous Performance Monitoring in Self-Adaptive Systems.**

> 🔗 **[Test API](COLE_AQUI_O_LINK_DO_DEPLOY/BASE_URL)**


### About the API
This API exposes, as a service, the capabilities of the **Milestone** framework proposed in a doctoral thesis, targeting **continuous performance monitoring** and **performance evaluation** in **self-adaptive systems**. The work is motivated by the lack of mechanisms for **continuous performance engineering** in SAS that explicitly connect non-functional requirements to runtime decision-making.

Milestone is organized around the **MAPE-K loop** (**Monitoring, Analysis, Planning, Execution, and Knowledge**). In practice, it works as a supervision layer attachable to different systems: it **collects runtime performance metrics**, **interprets the current state**, **supports adaptive decision-making**, and **records/uses adaptation history**.

Neural networks play a central role in the **Analysis** stage by classifying system state (e.g., “good/bad”) from monitored metrics. The end-to-end cycle includes: monitoring metrics, normalizing inputs, inferring state with the model, planning corrective actions, estimating impact, evaluating success, and registering knowledge for future decisions.

### Architecture
The solution follows a **client–server** architecture with clear responsibility separation: (i) a client that integrates and communicates with the managed system; and (ii) a server (manager) that processes requests and returns responses.

The design is modular and inspired by **MAPE-K**, using well-defined responsibilities and decoupled interfaces to enable evolution and reuse. Stage communication may occur asynchronously, and the cycle can be invoked on a schedule, by events, or in controlled batches, which helps integration into pipelines.

<!-- 
### Evaluation
Milestone was evaluated using **ten simulated scenarios** collecting **response time** and **CPU usage**. Robustness was supported with training on **500 samples** and **10% noise**.

Each stage used metrics aligned with its purpose: Analysis used accuracy, ROC-AUC, and loss; Planning used latency and success rate; Knowledge used effective knowledge utilization (how much of the repository is actually referenced during decisions).

Reported results include: **85% accuracy**, **0.86 ROC-AUC**, and **0.43 loss** in Analysis; planning latency **below 1 second** and **66.67%** success rate; and **100%** effective knowledge utilization. Case studies also describe non-invasive integration and API-based communication with self-adaptive systems to detect degradation and suggest adaptive actions.
-->

### Authors 
- **Name:** Msc. Belmondo Rodrigues Aragão Junior 
- **Name:** PhD. Valéria Lelli Leitão Dantas
- **Name:** PhD. Tales Paiva Nogueira
- **Name:** PhD. Marcio Espíndola Freire
- **Name:** PhD. Rossana M. C. Andrade 

### Lab / University
- **Lab:** Group of Computer Networks, Software Engineering and Systems (GREat) - https://www.great.ufc.br/  
- **University/Institution:** Federal University of Ceara
- **Program:** Master’s and Doctoral Program in Computer Science







<!-- 
The milestone was born with the idea of ​​being a framework to facilitate the process of monitoring, evaluating and aiding adaptation in self-adaptive systems.

Initially, it consisted of a Java library, which had to be imported into the project code.

As the project evolved, the idea of ​​inserting machine learning algorithms was envisioned, making the process more efficient.

With this, the project was changed to Python, and the milestone went from an imported library to code that must be executed on the system server.


<!-- ## Installation

<!-- //Currently, the installation process consists of adding the project classes to the desired self-adaptive system, paying attention to the hierarchy system presented by the project.
## Improvements

The improvements listed for the framework consist of:

I - Convert each subproject into a library to facilitate import and use - DONE

II - Improvement of the planning stage, with the addition of intelligent algorithms native to the framework - DONE


III - Transform the framework into a more complete platform, combined with the LoCCAM Middleware platform
 - [LoCCAM Middleware ](https://dl.acm.org/doi/abs/10.1145/2480362.2480465) - IN PROCESS
-->