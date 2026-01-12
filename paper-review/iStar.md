# Li et al. — "Understanding the challenges and requirements for facilitating iStar learning: An empirical study with iStar learners"


## 1. What this paper is and why it matters (Intro, Sec. 1-2)

- **What is it**:
    An empirical study on why iStar is hard to learn/practice and what requirements (strategies + tool support) are needed to make it easier. It combines:
    - **Revised Bloom's taxonomy** (to frame learning difficulties);
    - **Strauss and Corbin—style Grounded Theory** (to build a theory of difficulties + strategies);
    - A **prototype iStar tool** implementing many of the derived requirements.
- **Why it matters for my thesis**:
  - It is **exactly about conceptual modeling education**, but focused on iStar.
  - It uses **Bloom + Grounded Theory + tool design**, which matches my own methodological stack.
  - They explicitly claim the **procedure and part of the findings are transferable to other modeling methods**, not just iStar.

This is my **core empirical + conceptual anchor**: "how to systematically uncover modeling learning challanges and turn them into requirements and tool features".


## 2. Theoretical lenses and research questions (Sec. 2 and 4.1)

### 2.1 Background: iStar and Bloom (Sec. 2)

- **iStar 2.0** = goal- and agent-oriented RE framework; actors (roles/agents), intentional elements (goals, qualities, tasks, resources), dependencies (depender/dependee/dependum), associations (is-a, participates-in), multiple views (SD, SR, Hybrid).
- **Revised Bloom's taxonomy** (cognitive domain) with 6 levels: remember, understand, apply, analyze, evaluate, create. They briefly explain all but **focus their study on the mid-levels**.
- They adopt **CaMeLOT's mapping of typical modeling tasks to Bloom levels** (Table 1), e.g.:
  - Understand: exemplify terms, linkk concept <-> notation, explain in own words.
  - Apply: use patterns/heuristics to solve modeling tasks.
  - Analyze: determine completeness, distinguish relevant/irrelevant info, explain modeling choices.

### 2.2 Research Questions (Sec. 4.1)

They consciously restrict to beginners and three Bloom levels:

- **RQ1**:
  What specific challenges do beginners face when learning iStar at different cognitive levels, particularly understanding, applying and analyzing?
- **RQ2**:
  How can the iStar modeling process be improved to address the challenges in learning and practicing?

Their racionale (still Sec. 4.1):

- **Remembering** is necessary but not where the real pain is; the main hurdles arise when beginners must understand, apply, and analyze iStar.
- **Evaluate/Create** are too advanced for novices and could overload them. So they deliverately study the **middle of Bloom** as the "bottleneck region" for learning a complex modeling method.

This is useful if i want to justify **why my own thesis also focuses on certain cognitive levels rather than all six**.


## 3. Study design: who, what, how (Sec. 3-4)

### 3.1 Participants and context (Sec. 4.2 + Table 4)

- **10 iStar learners (B1-B10):**
  - CS / Software Engineering undergrads and master's students.
  - All had:
    - Basic RE knowledge and at least one other modeling approach (e.g., use cases, DFD);
    - Developed a **real software system runing for more than 6 months and with more than 100 users**, to unsure meaningful requirements experience.
- **3 iStar lectures (L1-L3)**:
  - Each has **more than 10 years** of iStar teaching/practice, with different emphases: general RE, domain-specific RE, and RE education.

This is important: the paper works with **relatively strong novices** (real dev experience), not complete beginners.

### 3.2 Data collection flow (Fig. 2, Sec. 4.2)

Each learner did a **single individual sequence**:
1. **iStar tutorial (one-to-one)** - using a standard slide deck; learners can ask question until they feel confortable.
2. **iStar modeling session:**
   - Scenarion: **their own existing software system** (to avoid domain confusion).
   - Medium: **paper + 2 coloured pens (black/red)**, no tool, so they focus on concepts instead of tool quirks.
   - Goal: model current requirements + potential future updates.
   - Lecturers later review the models, fix syntax mistakes, and clarify confusing concepts.
3. **Semi-structured interview:**
   - Separete protocols for learners and lecturers; main questions are mapped to RQ1/RQ2 (Tables 2 and 3).
   - Interviews continue until no new information emerges (local saturation).


Additionally:
- **Model artifact analysis:** they examine the produced models for recurring errors.
- **Literature review (Sec. 5.3):** on iStar learning difficulties and iStar tools, to triangulate and extend the emerging theory.


### 3.3 Grounded Theory procedures (Sec. 5.4)

They follow **Strauss and Corbin** (not Glaser) and Stol's SE guidance:

- **Open coding**: line-by-line tagging, grouping into concepts and higher-level categories.
- **Axial coding with a coding paradigm**: map thing into "phenomenon, context, causal conditions, intervening conditions, strategies". They **omit consequences** because the "consequences" in this study are exactly the strategies/requirements they want to produce.
- **Selective coding**: build the final storyline and treat **"strategies" as the core category** that connects all others.
- **Tooling**: NVivo for coding and memoing; coding done collaboratively with regular meetings to resolve disagreements.

This is my template for any "Grounded Theory method" subsection.


## 4. Empirical finding: errors + challenges (Sec. 5.1-5.2)

### 4.1 Modeling results and common errors (Sec. 5.1)

- **Model size**:
    Modeling sessions ranged **20-90 minutes** (mean ~ 46 mins). Final models had **10-91 elements** (mean ~47). Learners usually modelled **approx. 3 actors**, with around **7 dependencies** on average. Almost none used **is-a / participates-in** relationships.
- **Typical error types**:
    1. **Conceptual misinterpretations** - e.g., confusing **goals vs tasks**; 7 of 10 learners mislabelled them at least once.
    2. **Dependency misuse** - wrong direction or swapped depender/dependee.
    3. **Incomplete refinements** - goals left at a high level with insufficient decompositions.
    4. **Semantic ambiguity** - vague labels like "Check data" with no clear intention.
    5. **Scalability/complexity issues** - cluttered layouts in larger models, reducing readability.

The concrete errors become **evidence for later "strategies" like S1.2, S2 (syntax help), S9 (visual/layout support)**.

### 4.2 Challenges at Bloom levels (answering RQ1 - Sec. 5.2.1)

They map the difficulties to **Understand / Apply / Analyze**:

**a) Understand: grasping concepts and semantics**
Main issues:
- Many learners found:
  - The **number of element types** (goals, tasks, qualities, resources, etc) and relationships overwhelming.
  - Hard to distinguish **softgoals vs goals, agents vs roles**, and different relationship types.
- Quote examples: learners say they dont know which relationships to use, and that "dependencies are confusing at first".

So at this level, the bottleneck is **semantic clarity and categorization** of elements, not just remembering notation.

**b) Apply: using iStar for real modeling**
Difficulties:
- **No clear modeling process**.
    Learners tend to naturally follow a **top-down-ish process** (from actors to internal intentions) but struggle when:
    - Requirements are not fully clear;
    - They dont know whether to go top-down (goals -> tasks) or bottom-up.
  - Lectures observe that students often:
    - Over-focus on details too early;
    - Lack heuristics for "where to start" (actors vs goals vs dependencies).
  - Expressing **complex natural language requirements as iStar diagrams** is hard: multiple possible decompositions; abstraction choices affect the whole model and feel "fragile".

So at Apply, the problem is **process and mapping from text -> model**, not only the language itself.

**c) Analyze: understanding strangths/limits of iStar**
Key findings:
- All learners perceived iStar as more abstract and complex than flowchaarts, UML class diagrams, etc.
- They struggle with:
  - **Hierarchies of intentional elements** (whats high-level vs low-level).
  - Seeing **where iStar is better or worse** than other frameworks.
- Lecturers report learners often **dont recognise iStar unique strenghts/limitations**, because they come from a UML/flowchart mindset.

So at Analyze, the difficulty is **meta-understanding**: how to compare frameworks, judge completeness, and reason about the model quality.


## 5. The theory: coding paradigm and strategy space (Sec. 5.4)

### 5.1 Coding paradigm structure (Fig. 3, Sec. 5.4.4)

They summarise everything using Strauss and Corbin's coding paradigm (Fig.3):

- **Phenomenon**:
  Learners find iStar modeling difficult.
- **Context (CT)**:
  - CT1 - Software development experience;
  - CT2 - Requirements modeling experience;
  - CT3 - Experience in other modeling methods.
    These shape how difficult iStar feels.
- **Causal conditions (CS)**:
  - CS1 - Complexity of iStar modeling.
  - CS2 - Understanding of requirements modeling.
  - CS3 - Quality of learning resources.
- In**tervening conditions (I)**:
  - **I1 - Understanding iStar modeling:**
    - I1.1 understanding concepts/principles;
    - I1.2 ability to detect/locate errors.
  - **I2 - Applying iStar modeling:**
    - I2.1 proficiency with real-world scenarios;
    - I2.2 ability to express practical requirements;
    - I2.3 effectiveness of modeling methods/best practices;
    - I2.4 ability to express non-functional requirements.
  - **I3 - Analyzing iStar modeling:**
    - I3.1 ability to compare iStar to other frameworks.
  - **I4 - Practical limitations:**
    - I4.1 quality of artifact being modeled;
    - I4.2 layout/view preferences;
    - I4.3 time/effort for editing;
    - I4.4 support for modularization/scalability.
- **Strategies (S):**
  = the **requirements/solutions** to address the phenomenon under given conditions. These are the main contribution and are grouped into four areas: undestanding, applying, analyzing, and practical limitations.

They then **filter strategies** with the lecturers: ideas suggested by <2 participants or considered impractical (e.g., full ML-driven automatic modeling, real-time collaborative editing) are discarded, keeping only **educationally realistic** requirements.


### 5.2 Strategy / requirement catalogue (S1-S9, Sec. 5.4.4)

The final strategies (S1-S9) are my "requirement list" for educational support:


**A. Understanding iStar (S1-S2)**
- **S1 - Provide technical help for understanding iStar:**
  - **S1.1**: clear definitions + graphical notation for all elements;
  - **S1.2**: explanations and categorisation support for intentional elements:
    - S1.2.1 help abtract and categorise;
    - S1.2.2 distinguish goals vs tasks;
    - S1.2.3 help refine intentional elements;
    - S1.2.4 clarify conceptual hierarchy;
    - S1.2.5 distinguish dependencies vs internal elements;
    - S1.2.6 clarify types and directions of dependencies;
    - S1.2.7 distinguish agents vs roles.
- **S2 - Automated syntax checking and hints:**
  - S2.1 automatic model syntax checking;
  - S2.2 hints/suggestions for fixing errors.


**B. Applying iStar (S7-S8 - note numbering jump)**
- **S7 -Process guidance and examples**
  - S7.1 intro to iStar modeling with examples;
  - S7.2 highlight strenghts/limitations of iStar;
  - S7.3 help map domain requirements to actors and intentions;
  - S7.4 guidance on choosing modeling starting points (actors? goals? dependencies?);
  - S7.5 support for expressing NFRs through appropriate patterns.
- **S8 - Provide model templates:**
  - S8.1 standard template library for generic iStar models;
  - S8.2 domain-specific iStar template library;
  - S8.3 support for template-based buld element creation.


**C. Analyzing iStar (S9)**
- **S9- Advanced visualization and interaction:**
  - S9.1 auto-layout for clear diagrams;
  - S9.2 navigations across different model elements and views;
  - S9.3 multiple views (e.g., different stakeholders perspectives);
  - S9.3.1 model element selection + filtering;
  - S9.3.2 alternative views for the same model.


**D. Practical limitations and automation (S3-S6)**
- **S3 - Batch editing operations** (add elements, multiple dependencies, etc.).
- **S4 - Automated modeling from textual requirements:**
  - S4.1 extract elements from SRS to iStar;
  - S4.2 automatic creation of model elements from text.
- **S5 - Suggest subsequent modeling operations** (recommend next steps).
- **S6 - Support modularization and scalability** (e.g., sub-models, modular structures).


I dont need to memorise the numbers; for my thesis, what matters is **the structure**:
> "They derive a catalogue of strategies spanning conceptual help, syntax support, process guidance, templates, visualization, batch operations, text-to-model extraction, and modularization".


## 6. Literature review: situating their results (Sec. 5.3)

They cross-check their findings against prior iStar education/usability work:
- **Horkoff** - conceptual ambiguities for novices (dependencies vs internal elements; abstract actors). Recommends hybrid SD/SR, clear focus on participants and boundaries first.
- **Estrada et al.** - industrial evaluations; highlight limitations in detail refinement and modularization (scalability problems).
- **Carvallo e Franch** - non-technical stakeholders struggle with dependency types/directions and NFRs; recommend context-driven examples and structured guidelines, not just tools.

They also summarise several existing **iStar tools** (REDEPEND, J-PRiM, Creative Leaf, piStar) and what each supports (syntax checking, creativity support, extensibility, etc.).

This helps them show what current **tools already do** vs. **what their strategies add**.


## 7. Prototype tool: implementing the requirements (Sec. 6)

To show that the strategies are **actionable**, they:

- Build a **prototype on top of piStar**, since piStar is open-source and iStar 2.0 compliant.
- Implement key features corresponding to S3-S4-S8-S9:
  - **Multiple ways to add elements**:
    - Batch addition;
    - **Template-based addition** for common patterns (actors, intentions, dependencies);
    - **Text-to-model from SRS**:
      - Input sentences -> actor entity extraction -> actor relation extraction -> intention entity extraction -> add to the iStar model. (Fig. 4) 
  - **Guided workflow for adding elements** via templates (Fig. 5)
  - **Auto-layout** to keep diagrams readable after batch insertions.

They dont present a full evaluation yet; future work is to **evaluate this tool in real courses**.


## 8. How this paper feeds my thesis

I can use this paper as:

1. **Empirical base**:
    - Concrete evidence of **what students and lecturers find hard** in a complex modeling language.
    - **Error patterns** and **perceived difficulties** mapped to Bloom levels.
2. **Methodology blueprint**:
    - How to combine **Bloom, CaMeLOT, and Strauss and Corbin GT** in SE education.
    - How to structure my **coding paradigm-based theory** (context, causal, intervening, strategies).
3. **Requirements catalogue**:
    - Reusable **strategy space (S1-S9)** i can use:
      - Generalise to other modeling methods (UML, BPMN, ER, etc);
      - Compare with finding from CaMeLOT, Domain Modelling in Bloom, Bork's framework, etc.
4. **Inspiration for tooling** (probably wont be required):
    - Shows what **kinds of features** students actually ask for and lecturers consider realistic: syntax help, templates, auto-layout, text-to-model, multi-view, etc.
    - I can position my own future prototype (or design recommendations) relative to theirs.


## 9. Thesis-ready one-paragraph summary

Li et al. present an empirical study that systematically investigatges the challenges beginners face when learning and practicing iStar 2.0 goal-oriented requirements framework, and derives requiremetns to support more effective iStar education. Using revised Bloom's taxonomy and CaMeLOT's mapping of modeling tasks to cognitive levels, they design a research protocol involving ten experienced student developers and three expert lecturers who complete an iStar tutorial, a paper-based modeling session on their own software systems, and semi-structured interviews. The data, triangulated with model artifact analysis and a literature review, are analysed using Strauss and Corbin's grounded theory (open, axial and selective coding) to build a coding-paradigm-based theory in which the phenomenon "finding iStar modeling difficult" is explained by contextual factors, causal conditions, and intervening conditions related to understanding, applying analyzing and practically using iStar. From this they derive a catologue of strategies and requirements—ranging from conceptual and syntax support to process guidance, templates, advanced visualization, batch operations, and semi-automatic medling from textual requirements—which they partially implement in a prototype tool extending piStar with batch addition, template-based modeling, SRS-to-model extraction, and auto-layout. The work not only clarifies iStar-specific learning challenges but also proposes a transferable procedure for studying and supporting the learning of complex conceptual modeling methods.

