# CaMeLOT

## 1. What CaMeLOT is and why it matters (Sec. 1-2)

- **Context (Sec. 1)**
  - Conceptual data modeling (CDM) is core in SE curricula but **ill-structured** and highly abstract, so students must handle both notation and messy domain context.
  - There is **no generally accepted educational framework** for data modelling. Teachers improvise learning outcomes and course design based on their own experience.
  - Prior work (their earlier study) showed that in existing books/MOOCs/exams, **evaluation tasks are heavily underrepresented,** and scaffolding towards model creation is uneven and inconsistent.
- **Background (Sec. 2)**
  - Curriculum standards (MSIS, IEEE SE2014, SFIA) mention modelling only at a **very high level**, not enough to guide concrete course design or assessment in CDM.
  - Bloom and revised Bloom have been widely used to build frameworks in other disciplines (biology, anatomy, CS), but **nothing domain-specific for CMD** existed.

**Goal of CaMeLOT:**
Create a **domain-specific educational framework for CDM** based on revised Bloom's taxonomy, with:
- adapted **knowledge x cognitive level definitions,**
- explicit **content areas + scaffolding,**
- lots of **example learning outcomes** to guide teachers.

For my thesis: this is basically "Bloom + domain-specific scaffolding + example LOs for CDM" - a concrete framework that responds to exactly the gaps I care about.

## 2. How CaMeLOT was designed (Sec. 3 - Design methodology)

- Uses **Design Science Research (DSR)** with relevance, rigor, and design cycles (Fig. 1).
- **Iteration 1** (their earlier "Domain MOdelling in Bloom" paper):
  - Apply revised Bloom unchanged to existing resources (books, MOOCs, exams).
  - Find big gaps:
    - **No metacognitive knowledge outcomes** anywhere.
    - **Procudural knowledge** tasks strongly underrepresented.
    - Cognitive **Evaluate** almost missing.
  - This leads to a first version of CaMeLOT: Bloom re-interpreted for CDM + a new **content-area dimension.**
- **Current iteration (this paper):**
  - Refine CaMeLOT by **developing concrete assessment items** and **17 example tables** of learning outcomes in 6 content areas.
  - Then **evaluate** it via expert interviews (Sec. 6).

For my methodology chapter: I can treat CaMeLOT as a **DSR taxonomy / framework artifact** that operationalizes Bloom for CDM.

## 3. Structure of CaMeLOT (Sec. 4.1 - Scaffolding + content areas)

### 3.1 Scaffolding tree (Fig.2, Sec. 4.1)

CaMeLOT keeps the same **scaffolding tree** i saw in "Domain Modelling in Bloom" (Object -> Class -> Attribute -> Associations -> Complex model, etc):
- **Class level:** Object, Class, Attribute.
- **Relationships level:** Generalization (inheritance) + Associations (binary, n-ary, recursive, aggregation, association class).
- **Model level:**
  - Simple model (classes + basic binary associations).
  - Complex model (full use of inheritance, n-ary, aggregations, etc.).
- **General Knowledge** on the side (modelling languages, methods, MDE, etc.).

Arrows encode **prerequisites** (A must be understood before B). This formalizes the **learning path** from basic constructs to complex models.

### 3.2 Content-area dimension (Fig.3, Sec. 4.1)

Each learning outcome in CaMeLOT is classified by **three coordinates:**
> (Content area, Knowledge level, Cognitive Level).

Main **content areas:**

1. **Model creation**
   - **Classes** (including inheritance notions).
   - **Relationships** (associations and multiplicities, association classes).
   - **Models** (simple vs complex, patterns, reference models).
2. **General modelling**
   - **Modelling quality** (semantic/syntactic/pragmatic quality, SEQUAL etc.).
   - **Modelling methods** (guidelines, strategies, method engineering).
   - **Model-driven engineering** (MDE, transformations, meta-models).
3. **Modelling languages and notations** (UML, ER, Crow's foot, physics of natation, ...),
4. **MDE technology** (MOF, MDA, transformations, meta-models).
5. **Metacognition** (motivation, self-reflectiomn, learning strategies).

This **content-area dimension** is the big extension beyond standard Bloom: it lets me say where gaps are (e.g., "no procedural LOs in Relationships" or "no metacognitive LOs for modelling quality").

## 4. Bloom's taxonomy adapted for CDM (Sec. 4.2)

They re-interpret both **knowledge levels** and **cognitive levels** with CDM-specific examples. Key ideas (no need for all the details because the "domain modelling in bloom" already covers most):

### 4.1 Knowledge levels (Sec. 4.2.1)

- **Factual** - basic elements and notation:
  - term definitions from textbooks, notation symbols, naming conventions.
- **Conceptual** - relationships between concepts:
  - differences class vs attribute, types of quality (syntactic/semantic/pragmatic), pattern generalization, etc.
- **Procedural** - "how to model":
  - step-by-step guidelines for eliciting classes, applying patterns, quality assessment procedures, model-to-code transformations.
- **Metacognitive** - strategies and self-knowledge:
  - planning how to study modelling, knowing one's typical mistakes, reflecting on progress, motivation.


### 4.2 Cognitive levels (Sec. 4.2.2)

They give **domain-specific task types** for each cognitive level:
- **Remember** - recall terms, match to notations, list error types.
- **Understand** - explain multiplicity, explain quality types, summarize requirements in own words.
- **Apply** - use patterns, apply elicitation guidelines, transform notation or models.
- **Analyze** - compare patterns or models, identify relevant information in requirements, detect incompleteness.
- **Evaluate** - check models for errors, critique notation choices, choose better pattern/strategy.
- **Create** - build a model from requirements, design a new pattern, create one's own guidelines or decison trees.

For my thesis: CaMeLOT gives me a **ready CDM-specific interpretations** of each Bloom cell - I can cite this to justify my classification scheme or example exercises.


## 5. Example learing-outcome tables (Sec. 5) - what they actually built

They instantiate CaMeLOT with **17 tables of example LOs** across 6 content areas (Classes, Relationships, Models, MDE, Modelling quality, Metacognition).

Rathar than list all tables, here's the pattern:

### 5.1 Within a content area, LOs form a Bloom ladder

**Example: Classes - conceptual (Table 2, Sec. 5.1.2)**

For the topic "class vs attribute vs object", LOs progress like:

- Remember: state conditions for modelling something as attribute vs class.
- Understand: give an example of something that should be a class, not an attribute.
- Apply: given precise requirements, decide class vs attribute.
- Analyze: highlight in the requirements which parts describe classes, attributes, objects.
- Evaluate: given a list of classes, decide which are excessive.
- Create: derive a draft list of classes and attributes from requirements.

This pattern repeats for other topics: **inheritance, multiplicity, association classes, model patterns, quality types, etc.**

I can mine these as **templates** for my own questionnaries, exercises, or survey items.


### 5.2 Procedural and metacognitive LOs are made explicit

- **Procedural examples:**
  - Class elicitation steps (Table 4), model building stages (Table 9), transformation from association class to class+association (Table 6), model-to-code transformation (Table 12), quality assessment checklist (Table 15).
- **Metacognitive examples:**
  - Reflecting on motivation, favourite tasks, rating course parts; describing learning strategies; implementing a strategy for a week; writing a reflective report on one's modelling skills (Tables 16-17).

For the thesis this is **important evidence** that:
- It's possible to formulate **metacognitive** and **procedural** LOs for modelling - they are not just theoretical categories.
- Current curricula usually dont include these, which is exactly the gap the authors want to close.

## 6. Evaluation and limitations (Sec. 6-7)

### 6.1 Expert evaluation (Sec. 6)

- **3 experts** (Belgium, USA, Germany; all full profs with 13-28 years of experience teaching modelling) were interviewed using **Technology Acceptence Model (TAM)** lens: perceived ease of use, usefulness, intention to use.
- **Result (Sec. 6.3-6.4):**
  - Two experts:
    - Ease of use: **moderate** (learning the framework takes time, but then it structures course design).
    - Usefulness: **high** - helps set ambition level (basic vs advanced course), diversify exercises, evaluate and improve existent courses.
    - Intention: positive; both planned to use/adapt it.
  - Third expert:
    - Ease of use: **low** - worried about overlaps and classification ambiguity.
    - Usefulness: low; sees it more as a starting point than ready-to-use framework.

### 6.2 Limitations and suggestions (Sec. 7)

- **Ambiguity of classification** (factual vs conceptual, etc.) and **concept shifting** across content areas (e.g. knowledge of notation could belong to "Classes" or "Modelling languages").
- These may require:
  - Stricter classification rules, or
  - accepting some ambiguity as **flexibility**, resolved by multiple raters.
- Suggestions for use (Sec. 7.2):
  - Use CaMeLOT to **assess and improve existing courses** (identify gaps in Bloom x content matrix).
  - Use it to **design new exercises/exams** systematically.
  - Use it to **create a new modelling course from scratch**, picking relavent content areas and Bloom levels (Fig. 4-5).


## 7. Main contributions I can reuse (Sec. 8 - Conclusion)

In conclusion, CaMeLOT:
- Provides a **domain-specific adaptation** of revised Bloom for conceptual data modelling.
- Introduces the **content-area dimension + scaffolding tree** to capture prerequisete structure in modelling education.
- Supplies **work example tables** of learning outcomes (17 tables across 6 content areas) covering factual, conceptual, procedural, and metacognitive knowledge at all cognitive levels.
- Enables:
  - systematic design and evaluation of CDM curricula and assessments,
  - identification of **missing evaluation/procedural/metacognitive LOs**,
  - potential redution in time to design materials while improving quality.


## 8. Thesis ready one-paragraph summary

Bogdanova and Snoeck propose CaMeLOT, a revised-Bloom-based educational framework for conceptual data modelling that addresses the lack of systematic learning outcomes and scaffolding in current CDM courses. Using design science research, they adapt the four knowledge levels and six cognitive levels of the revised taxonomy to CDM and add a content-area dimension with an explicit scaffolding tree, covering model creation (classes, relationships, models), general modelling topics (quality, methods, MDE), notations, technology, and metacognition. They instantiate the framework with 17 tables of example learning outcomes across these content areas, including many procedural and metacognitive objectives that are largely absent from existing textbooks, MOOCs, and exams. An expert evaluation suggests that, despite some classification ambiguity and an initial learning curve, CaMeLOT can help educators structure curricula, set appropriate ambition levels, and systematically design or assess exercises and exams, thereby making modelling education more balanced and transparent in terms of Bloom levels and content coverage.