# Bork — "A Framework for Teaching Conceptual Modeling and Metamodeling Based on Bloom's Revised Taxonomy of Educational Objectives

## 1. Problem and Goal (Intro - Sec. 1)

- **Context:**
  - Conceptual modelling and metamodeling are **core parts** of CS/IS programs (BPMN, UML, etc.), and industry increasingly expects **modelling capabilities and abstraction skills.**
  - Teachers struggle with:
    - making sure their **teaching is comprehensive,**
    - identifying **motivating domains,**
    - showing that models have value **beyond mere representation** (e.g., analysis, simulation, queries).
- **Research questions:**
  > "How to teach conceptual modelling and metamodeling comprehensively, i.e., including all dimensions of Bloom's revised taxonomy?"
- **Goal of the paper:**
  1. Propose **generic educational frameworks** for:
     - conceptual modelling,
     - metamodeling, based on **revised Bloom's taxonomy** (knowledge x cognitive process).
  2. **Apply** these frameworks to evaluate a **Smart City teaching case** taught at the NEMO summer school.
  3. Use the evaluation to discuss how to **improve CM and metamodeling teaching.**

This paper is basically: "Bloom + generic framework for CM and metamodeling + Smart City case evaluation" — complementary to CaMeLOT but more general (not limited to data modelling).


## 2. Foundations (Sec. 2-3) — What they build on

- **Domain-specific conceptual modeling (Sec. 2.1):**
  - Uses Karagiannis and Kuhn's view: a **modelling method** has 3 core components:
    - **Language** (syntax),
    - **Semantics**,
    - **Notation**,
    - plus **modelling procedure** and **mechanisms and algorithms** (e.g., simulation, transformation).
  - General-purpose languages (BPMN, UML) are often **not adequate** for emerging domains (Smart Cities, etc.), hence the need for **domain-specific methods** and metamodeling.
- **OMiLAB and NEMO (Sec. 2.2-2.3):**
  - **OMiLAB** = open environment for modelling method engineering using **ADOxx.**
  - **NEMO summer school** = annual conceptual modelling education event where the **Smart City case** is used in lectures + exercises (Master/PhD students).
- **Bloom's Revised Taxonomy (Sec. 3):**
  - **Knowledge dimension:** factual, conceptual, procedural, metacognitive.
  - **Cognitive process dimension:** remember, understand, apply, analyze, evaluate, create, in cumulative hierarchy.

These are then specialised to CM and metamodeling.

## 3. Framework 1 — Teaching Conceptual Modelling with Bloom (Sec. 4.1)

### 3.1 Knowledge dimension $\rightarrow$ CM

They map each knowledge type to CM:

- **Factual Knowledge:**
  - Basic elements of conceptual models, purposes and goals.
  - For a specific language: elements, their **semantics**, and **notation**.
- **Conceptual Knowledge:**
  - Valid **combinations** of language elements; structuring of large models (submodels, views).
  - Comparing different languages for **fitness to purpose.**
- **Procedural Knowledge:**
  - **Modelling procedure:** steps to create valid models using a method.
  - Knowing **which method to use** in a given scenario $\rightarrow$ combining conceptual knowledge of methods with criteria for selection.
- **Metacognitive Knowledge:**
  - Stratigic thinking about modelling:
    - target audience and use of the model,
    - time/resources available,
    - one's own experience with the method.

### 3.2 Cognitive process dimension $\rightarrow$ CM (Table 1)

Table 1 maps each cognitive level to CM activities and typical exercises:

- **Remember**:
  - Recall syntax, semantics, notation, procedure, mechanisms.
- **Understand**: 
  - Understand meaning of model elements and their relationships $\rightarrow$ focus on **semantics**.
- **Apply**:
  - Use a modelling method to solve a problem:
    - select appropriate model for a scenario,
    - generate code from a model,
    - transform models following a procedure.
- **Analyze**:
  - Analyse a model's syntax and/or semantics, including decomposition into submodels.
- **Evaluate**:
  - Judge model quality against criteria:
    - syntactic (cardinalities, allowed relationships),
    - semantic (correctness, completeness),
    - using quality frameworks (e.g., Krogstie/Lindland/Sindre).
- **Create**:
  - Create a new conceptual model, including:
    - choosing appropriate elements,
    - modelling them with correct notation,
    - relating them appropriately,
    - possibly following a procedure and using mechanisms/algorithms.

Framework takeaway: **all parts of the modelling method** (language, semantics, notation, procedure, mechanisms) can be tied explicitly to Bloom levels.


## 4. Framework 2 — Teaching Metamodeling with Bloom (Sec. 4.2)

Similarly, they specialise Bloom for **metamodeling** (designing new modelling languages):

### 4.1 Knowledge Dimension $\rightarrow$ metamodeling

- **Factual**:
  - Constituents of metamodels (object types, relationship types, attributes, model types).
  - Foundations of notation (e.g., Moody's Physics of Notation), semantics, and metamodel specification techniques.
- **Conceptual**:
  - **Meta-hierarchies**, meta-metamodels, use of generalization/inheritance in metamodels.
  - How to implement metamodels on a **metamodeling platform** (ADOxx, etc.).
- **Procedural**:
  - Processes and methods for metamodeling:
    - composition of metamodels,
    - DSML development,
    - metamodel metrics,
    - agile / model-driven method engineering approaches.
- **Metacognitive**:
  - Choosing metamodeling techniques **based on context and purpose** (tool dev, documentation, transformation).
  - Reflecting on prior experience and integrating it into current tasks.


### 4.2 Cognitive Process Dimension $\rightarrow$ metamodeling (Table 2)

Table 2 maps cognitive levels of metamodeling tasks:

- **Remember**: recall meta-metamodels, hierarchies, constituents.
- **Understand**: understand how design decisions affect expressiveness and domain coverage.
- **Apply**: use metamodels in scenarios like model weaving, interoperability, consistency management.
- **Analyze**: analyze metamodels, e.g. via metrics.
- **Evaluate**: assess metamodel quality (understandability, correctness, conciseness, consistency) via empirical studies.
- **Create**: design new metamodels for specific domains from textual requirements.

This gives me a **generic Bloom-based framework** for metamodeling education, nicely compatible with CaMeLOT but at a higher level.

## 5. Smart City Teaching Case and Evaluation (Sec. 5)


### 5.1 Smart City case — structure (Sec. 5.1-5.2)

- Motivates **Smart City** as rich, complex domain requiring abstraction and innovation; good for CM + metamodeling.
- Case is taught in **3 sessions** at NEMO, using ADOxx as metamodeling platform:

**Session 1 — Planning a Smart City (metamodeling focus):**

- S1E1: Create a new modelling class (extend minimal Smart City metamodel).
- S1E2: Define static graphical visualization.
- S1E3: Define dynamic (attribute-dependent) visualization.
- S1E4: Create new relation class between metamodel concepts.
- S1E5: Create Smart City models using the new classes/relations.

**Session 2 — Analyzing a Smart City (queries):**

- Theory + demos + hands-on for queries in ADOxx:
  - S2E1: Standard queries.
  - S2E2: Combine queries with logical operators.
  - S2E3: User-defined queries in AQL.
  - S2E4: Configure queries via predefined procedure.

**Session 3 — Simulating a Smart City (simulation):**

- Introduces three simulation types in ADOxx: Path, Capacity, Workload analysis.
  - S3E1: Perform and interpret Path Analysis.
  - S3E2: Prepare models for Capacity/Workload Analysis (link resources, personnel).
  - S3E3: Configure and run Capacity Analysis.
  - S3E4: Configure and run Workload Analysis.


### 5.2 Evaluation against the Bloom frameworks (Sec. 5.3-5.4)

They map each task to **knowledge x cognitive process,** and summarise the coverage in Table 3:

**Findings:**

- **Cognitive process coverage:**
  - Many tasks sit at **Create** (especially Session 1 - metamodels extensions and model creating).
  - Session 2 and 3 introduce **Apply** and **Analyze** (querying, simulation, interpreting results).
  - **Evaluate** is **not covered**; there are no tasks where students explicitly evaluate models or metamodels against quality criteria.
  - **Remember** and **Understand** are present but mostly as **implicit prerequesites** with higher-level tasks (not as standalone exercises).

- **Knowledge dimension coverage:**
  - **Factual and Conceptual knowledge** strongly targeted, especially in tasks about elements, relationships, and model linking.
  - **Procedural knowledge** appears where students must follow specific procedures (query creation, simulation set-up).
  - **Metacognitive knowledge** is **not addressed:** no tasks about reflection on modelling strategies, audience, or learner self-awareness. Authors say this is partly due to NEMO's constraints (heterogeneous participants, only three sessions).


**Discussion (Sec. 5.4):**

- Smart City case is **rich in creation tasks,** but:
  - lacks **evaluation** and **metacognitive** elements,
  - treats **remember/understand** mostly as embedded in larger tasks.
- They suggest future extensions:
  - tasks comparing and **evaluating different Smart City metamodels,**
  - tasks evaluating conceptual models using **quality metrics,**
  - adding explicit **reflection** components.


## 6. Conclusions and Implications (Sec. 6)

- The paper proposes **two generic Bloom-based frameworks:**
  - one for **conceptual modelling,**
  - one for **metamodeling**,
    which can be used to **design and audit** CM courses.
- Application to the Smart City case shows that:
  - even well-designed, practice-oriented cases can be **unbalanced** (e.g., overemphasizing creation and neglecting evaluation/metacognition).
  - Using the Bloom x knowledge grid helps **see these gaps** and plan extensions.
- Future work:
  - revise and extend the Smart City material (possibly as a **MOOC** within OMiLAB)
  - integrate **automated, personalised feedback** as in Serral et al.,
  - make the teaching case accessible to the wider OMiLAB community.


## 7. Thesis-ready one-paragraph summary

Bork proposes Bloom-based educational framework for conceptual modelling and metamodeling and uses them to evaluate a Smart City teaching case at the NEMO summer school. Building on the revised taxonomy's knowledge and cognitive dimensions, he maps factual, conceptual, procedural and metacognitive knowledge to the components of modelling methods (language, semantics, notation, procedure, mechanisms) and defines typical modelling and metamodeling tasks for each cognitive level from remember to create. Applying this grid to three Smart City sessions—covering metamodel extensions, query-based analysis and simulation— reveals that the case strongly emphasises creation, with additional coverage of applying and analysing models, but largely neglects explicit evaluation tasks and does not address metacognitive knowledge. Remembering and understanding are also mostly implicit rather than targeted with dedicated exercises. The paper argues that such Bloom-based frameworks enable educators to systematically assess and redesign modelling courses, identify gaps (e.g., missing evaluation or reflection tasks), and guide the development of richer teaching cases and MOOCs, for instance within the OMiLAB environment.