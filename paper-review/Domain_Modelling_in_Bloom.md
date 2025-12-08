
# Domain Modelling in Bloom

## 1. What is this paper about and why it matters (Intro - Sec. 1)

- **Domain modeling** = the "what/data" perspective f enterprise modeling (objects, classes, attributes, associations, inheritance, etc), and it's seen as **crucial but hard** in enterprise engineering education.
- Teaching domain modeling is problematic because:
  1. **Ill-Structured problems:** students must model messy natural-language descriptions in diverse domain (software, engineering, enterprise).
  2. **No common pedagogy:** teachers design tasks and learning paths based on personal experience -> huge variation in methods and sequencing.
  3. **Terminology chaos** ("Babylonian" state): same concepts named differently in different communities (OO, DB, Conceptual modeling), which hampers knowledge transfer.
  4. **Unclear picture of a "good modeler**: skill set and learning outcomes are not formalized, so its hard to design proper assessments and scaffolding.

**Goal of the Paper:**
- Take a **concrete slice of CM education** (domain modeling) and:
  - Identify **learning outcomes** used in practice (books, MOOCs, exams),
  - classify them using **revised Bloom's taxonomy**,
  - see how domain modeling is scaffolded,
  - detect **gaps**(e.g., missing cognitive/knowledge levels, missing steps in scaffolding).

This is directly relevant to the thesis because:
- Shows how Bloom can be specialized to modeling.
- Empirically exposes **where teaching and assessment are unbalanced** (e.g., lots of "create" tasks but little evaluation/procedural/metacognitive).

## 2, Bloom's Taxonomy Adapted to Domain Modeling (Method - Sec. 3.1)

The authoes tailor the revised blooms taxonomy (cognitive x knowledge) specifically for domain modeling:

### Cognitive process levels (with domain-modeling examples) - Sec. 3.1

- **Remember** - recall notation and definitions
  - e.g., "Define inheritance", "Name this UML element"
- **Understand**- interpret or explain models
  - e.g. "Explain this class diagram in text", "Give an instance/example of a class or association."
- **Apply**- use learned techniques
  - e.g. "Modify this model to include a new association."
- **Analyze**- decompose and compare models
  - e.g. "Compare two models for the same domain", "Generalize a model"
- **Evaluate**- judge models against criteria
  - e.g. "Find mistakes in this model based on the description", "Choose the best model and justifyy"
- **Create**- build or significantly extend models
  - e.g. "Build a domain model from a requirements text", "Complete an incomplete model".

### Knowledge levels (domain-modeling interpretations) - Sec. 3.1

- **Factual** - terminology and notation (names of constructs)
- **Conceptual** - how modeling concepts relate (e.g., how inheritance vs aggregation vs association differ)
- **Procedural** - methods, rules, modeling strategies and guidelines (step-by-step approaches, modeling heuristics)
- **Metacognitive** - awareness of one's own typical mistakes, strategies for learning/improving modeling.

### Usefulness

This can give me a ready-made definitions if I need/want to build a Bloom-based framework for modeling learning outcomes.

## 3. Scaffolding Tree for Domain Modeling (Method - Sec. 3.2)

They argue bloom alone doesnt capture **prerequisite chains** between concepts, so they define a **scaffolding tree** (fig 1, sec. 3.2):

Four main **scaffolding levels**:

1. **Class level**
   - object, class, attribute (basic building blocks).
2. **Relationship level**
   - **Generalization**: inheritance.
   - **Associations**: binary, n-ary, recursive, aggregation, association class.
3. **Model level**
   - **Simple model**: class level + binary associations only.
   - **Complex model**: full set of relationship concepts (inheritance, n-ary, aggregation, etc).
4. **General knowledge level**
   - modeling languages, notation, general guidelines and conventions.

Arrows indicate "A is a prerequisite of B" (e.g., you must understand class/attribute before complex models).

This might be useful for my thesis as:
- an example of **domain-specific scaffolding** for modeling concepts,
- a structure i can compare to other frameworks (e.g., iStar constructs, BPMN constructs).


## 4. How they collected data (Method - Sec. 3.3-3.4)

Short version:
- Sources = 12 "assessment packages":
  - 4 widely-used **textbook** (OO Modeling, conceptual data modeling, DB design),
  - 3 MOOCs (edX, Open Univesity, Stanford),
  - **Final exam** from 3 universities (KU Leuven, UCLouvain, Namur).
- They classified **291 assessment tasks**:
  - each tasks $\rightarrow$ one or more **learning outcomes**,
  - each LO classified by:
    - Bloom cognitive level,
    - Bloom knowledge level,
    - Scaffolding level from the tree.
  - Classification done by 2 raters, disagreement <10%.

For my thesis: This is **evidence about real practice** (what teachers actually ask), not theoretical wish-list.

## 5. Key findings

### 5.1 Bloom distribution- big gaps in what we assess (Sec. 4.2 and Fig. 2)

From the normalized results across all sources:

- **Cognitive dimension:**
  - Most tasks are **understand**.
  - Next: **Analyze** and **Create**.
  - **Apply** appears, but less.
  - **Remember** and especially **Evaluate** are **strongly underrepresented.**
- **Knowledge Dimension:**
  - **Conceptual** Knowledge dominates.
  - **Procedural** questions: present but clearly fewer.
  - **Factual** knowledge: almost absent.
  - **Metacognitive** knowledge: **not address at all** in any source.

Interpretation (from Discussion - Sec. 5 and Conclusion - Sec.6)

- Domain modeling is treated as something you learn mostly by **doing and conceptual understanding,** not by memorizing terminology - hence little "Remember".
- **Evaluation tasks** (judging models, critiquing, deciding between alternatives) are surprisingly rare, even though evaluation is a key step between analyzing and creating a good model.
- The lack of **procedural** outcomes suggest that **modeling strategies and step-by-step methods** are rarely made explicit or assessed.
- The absence of **metacognitive** tasks indicates that students are not guided to reflect on **how** they model or on their typical mistakes.

For the thesis, i can say:

> Existing assessments in domain modeling largely neglect evaluation, procedural, and metacognitive aspects, which are crucial for developing expert-like modeling competence.

### 5.2 Scaffolding focus - We jump to complex models too fast (Sec. 4.3, 5)

From the scaffolding results (Fig.3, Sec. 4.3):

- Most assessment tasks target:
  - **Model level** (especially **complex models**), and
  - **Relationships level** (associations).
- **General Knowledge** and **class level** tasks are rare.

Discussion (Sec. 5-6):

- This suggests **weak scaffolding:**
  - courses jump quickly to complex models and advanced relationships,
  - without systematically checking understanding of classes/attributes/general guidelines first.
- This imbalance may make learning harder and hide basic misconceptions.

For the thesis:
> I can argue that **scaffolding in modeling courses is often incomplete:** basic and general levels are under-tested relative to complex model tasks, which may hinder gradual development of skills.

### 5.3 Frequent task types - what we actually ask students to do (Sec. 4.4)

They identify **12 frequent task types** across sources; most important ones:

- **Type 1:** Draw a class diagram / domain model from requirements.
- **Type 1a:** Draw a class diagram following given steps/procedures.
- **Type 2:** Modify a model to match a new description.
- **Type 3-4:** Elicit classes and attributes from text.
- **Type 5:** Define multiplicities of associations.
- **Type 7:** Find structural issues / improvements in a model.
- **Type 9:** Develop an alternative design.
- **Type 12:** Explain a class diagram in text.

In Bloom terms (Table 2, Sec. 4.4):

- Many frequent tasks live in **Create** (Type 1,2,9) and **Analyze/Understand** (Types 3,4,6,7,12).
- Very few tasks in **Remember** and **Evaluate**.
- Procedural tasks (Type 1a, 8,11) exist but are relatively rare.

This gives me **concrete examples** of typical modeling tasks mapped to Bloom levels, which i can reuse:
- For designing my **own exercises (if needed)**,
- For justifying **examples** when i talk about Bloom-classified modeling tasks.

## 6. Main Takeaways I can reuse in the thesis (Conclusion - Sec. 6)

The paper's conclusion in thesis friendly form:
- Domain modeling education currently has **unbalanced coverage** of Blooms levels:
  - strong on **understanding, analyzing, creating conceptual knowledge,**
  - very weak on **remember, evaluating, procedural** and specially **metacognitive** knowledge.
- **Scaffolding is incomplete:**
  - assessments focus on complex models and relationships,
  - basic class-level and general notation/guidelines knowledge is rarely assessed,
  - intermediate steps like evaluation are missing in the progression from analysis to creation.
- This unbalence may **hinder both teaching and learning**, making it harder to see where students struggle and to support the transition from novice to expert modeler.
- The authors propose to use ther **domain-specific Bloom adaptation + scaffolding tree** as a basis for:
  - revising learning materials and assessments,
  - designing a **systematic educational framework** for domain modeling (sample tasks, learning paths, validated assessment tools).

## 7. One-Paragraph Thesis-Ready Summary

Bogdanova and Snoeck analyse how domain modeling is taught in practice by classifying 291 assessments tasks from textbooks, MOOCs and university exams into a domain-specific version of the revised Bloom's taxonomy and a scaffolding tree of modeling concepts.They find that current assessment practices strongly emphasize understanding, analyzing and creating conceptual knowledge about domain models, while remembering, evaluation, procedural knowledge and especially metacognitive knowledege are almost absent. Moreover, most tasks target complex models and relationships constructs, with comparatively few tasks checking basic class-level or general notation knowledge, suggesting gaps in scaffolding. These results indicate that domain modeling education is biased towards high-level creation tasks without sufficient support for evaluation, strategy, and self-reflection, motivating the need for more balanced learning outcomes, clearer scaffolding, and a systematic Bloom-based framework for teaching conceptual/domain modeling.


