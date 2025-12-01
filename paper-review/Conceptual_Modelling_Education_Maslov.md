
# Conceptual Modeling Education (Maslov)

## What is Conceptual Modeling (CM) and CM Education?

### CM (Sec. 1.1)

- CM = Describing parts of the physical/social world via **abstraction and conceptualization**, usually with **diagrams**.
- Purposes: describe, predict, support practitioners, educate the public, stimulate "scientific habits of mind."
- Historically:
  - Pre-2005: focus on **technical CS/data models.**
  - 2005-2020: expansion to **business process, enterprise modeling, SE** and interest in **general CM theory.**
  - Now: CM is central to **knowledge-intensive domains** (DBs, SE, AI, BPM, enterprise modeling, MDE, low-code, scientific modeling, simulations, etc).

### Why CM quality matters (Sec. 1.1)

- High-quality conceptual models:
  - capture domain reqs,
  - support system maintenance/evolution,
  - are core to model-driven engineering.
- Poor models -> misunderstandings, wrong systems, costly re-eng.

### CM Education (Sec 1.2)

- CM has been taught in IS, CS, and business education for ~50 years.
- It involves demanding cognitive skills: **abstraction, conceptualization, interpretation, communication,** and understanding **syntax, semantics, pragmatics** of languages.
- Current problem: CM education is **fragmented**:
  - Theory, purposes, methods, and artifacts are confined to specific **subtypes** (e.g., only BPMN, only ER).
  - Pedagogical approaches are not shared across subtypes -> little cross-fertilization.

### Usefulness

This gives a solid " why CM & CM education matter" paragraph, and supports my argument that teaching modeling is cognitively heavy and currenly fragmented.


## Research Gaps & Objective

### Research Gaps (Sec. 2)

- **RG1 - Lack of shared knowledge across CM subtypes**
  There is a common ground across CM subfields, but **little shared understanding** and little cross-disciplinary research in CM education.
- **RG2 - CM education is limited and fragmented**
  CM education research:
  - focuses on isolated issues or subtypes,
  - is not systematized,
  - does not fully exploit similarities between subtypes.

### Research Objective (RO) (Sec. 2)

To investigate CM educational research across different subtypes in order to promote **cross-fertilization, external validity** and **transferability** of findings.

### Research questions (RQs) (Sec. 2)

They want to characterize CM education in terms of:

- **methods, contexts, learning theories, and approaches** (RQ1)
- **conceptual structure** (topics/tendencies) (RQ2)
- **social structure** (countries, authors, collaborations) (RQ3)
- **intellectual structure** (most cited works, outlets, emerging topics) (RQ4)

### Usefulness

Can reuse RG1 and RG2 almost directly in your "Problem statement / State of the art" - especially if I argue that modeling-education research is fragmented and needs a more unified, cross-subtype view.

## What they actually did (Method)

### Method
  
- **Bibliometric literature review + semi-automatic content analysis.**
- Data:
  - Initial : 29,114 docs (Scopus + WoS)
  - Filtered (education/learning, CM subtypes, etc.): **1064 publication** (1982 - 2023)
- They automatically tag each paper by:
  - **CM subtype** (24 subtypes overall)
  - **Research method**
  - **educational context**
  - **learning theory/approach** (via keyword searches)

### Usefulness

This can be cited as a large-scale mapping study showing how CM education research is distributed and which learning theories/contexts are used.

## Main findings

### Subtypes and Fragmentation (Sec. 6.2)

**Which CM subtypes are studied?**
- Strongly represented:
  - **Science modeling (248 docs)**
  - **IS modeling (300)**
  - **Data modeling (189)**
  - **Conceptual modeling (188)**
  - **Simulation (164)**
  - **Domain & ontology modeling (151)**
  - **Process modeling (127)**
- Under-represented:
  - **Enterprise (58)**
  - **Business (25)**
  - **User (9)**
  - **Mental (82)**
  - **Meta- (34)**
  - **Ecological (15)**


Interpretation:
- The field is **skewed**: some types (science modeling, IS/data) dominate; others relevant to business/enterprise modelling are **barely explored educationally.**
- Only ~5% of keywords appear in >= papers -> **no shared vocabulary**, reinforcing fragmentation.

### Research Methods & Contexts (Sec. 6.3-6.4)

**Methods (Sec. 6.3)**

- Most common methods:
  - experiments, design science, course design, surveys, interviews, case studies.
- Qualitative > quantitative.
- Very few:
  - **longitudinal** studies,
  - **explicit theory-building** work,
  - **physiological methods** (eye-tracking, etc.)


**Contexts (Sec. 6.4)**

- Dominant context: **higher education** (university courses)
- Next: **vocational training**, then **high school**
- Rare:
  - primary school,
  - teacher training,
  - PhD-level,
  - citizen science

#### Usefulness

I can say: "Most CM education research focuses on higher education and uses relatively standard empirical methods, with a lack of longitudinal or theory-building studies and very little work in pre-university contexts."

### Learning Approaches and Themes (Sec. 6.5)

From the keyword clusters and thematic map:
- **Core CM Education themes:**
  - e-learning, blended learning, EdTech,
  - **feedback and formative assessment,**
  - modeling tools and prototyping,
  - instructional design,
  - gamification and serious games,
  - collaborative/active/project-based learning.
- **Science modeling themes:**
  - model-based learning and **inquiry**,
  - model-based reasoning,
  - conceptual change and nature of science,
  - computational thinking, systems thinking,
  - intelligent tutoring systems.

Key conceptual point:
Many powerful learning approaches (model-based inquiry, gamification, feedback systems, porject-based learning) appear in specific subtypes but **not systematically shared** across the CM education landscape.

**Might be relevant for me if im talk about:**
- **Which pedagogy to use in modeling courses,**
- **How to transfer approaches** (e.g., model-based thinking from science to business/IT modeling).

## Discussion

### Unified Theory and CM education as a discipline (Avenue 1, Sec. 7.1)

**Core idea:**
- Cm is used everywhere, but there is **no widely accepted unifying theory of CM.**
- Education research tends to focus on **single subtypes,** not CM as a whole.
- They propose:
  - Developing a **unified theoretical foundation for CM**
  - Creating a **taxonomy of CM subtypes and languages**
  - Agreeing on common terminology,
  - Treating **CM education as a standalone discipline,** similar to mathematics education,
  - Creating dedicated **outlets/journals** for CM education

Statements like this can support my thesis;
"Current CM education lacks a unifying perspective, my work contributes to understaing X (e.g., challenges, competencies, learning outcomes) in a way that can fit into such a broader framework".


### Coverage of subtypes and business/enterprise Gaps (Avenue 2, Sec. 7.2)

**Main points:**
- Science modeling and core IS/data/conceptual/process modeling are heavily studied; **business-oriented CM subtypes** (busines, enterprise, user modeling) are **under-researched educationally.**
- Suggested research directions:
  - Study **education in less-covered CM subtypes** (enterprise, business, user, mental, meta- , ecological, citizen)
  - Explore **integration between core and non-core subtypes**, both in curricula and pedagogical strategies.
  - Investigate using **standard vs domain-specific languages** in teaching, and their impact on learning.

**Usefulness:**
Focuses on a specific subtype (e.g., requirements / goal modelling / iStar) and i want to show it is a part of a **wider underexplored space** in CM education.

### Tranferring Learning Approaches Across Subtypes (Avenue 3, Sec. 7.3)

This might be the **most directly useful** part for my work.

**Core argument:**

- Different CM subtypes use **different learning paradigms and theories,** but many of them could be **shared**:
  - Model-based learning and inquiry from **science modeling,**
  - Gamification, automated feedback and assessment from **core CM education**
  - Cognitive and constructivist framework, and potentially **connectivism**, across the board.
  
They propose research on:

- Transfering effective learning approaches across CM subtypes.
  - e.g., using **model-based inquiry** from science education to teach business/IT modeling.
- Applying frameworks like:
  - **Bloom's taxonomy**
  - **Zone of Proximal Development**
  - **Connectivist learning**, more explicitly and consistently to CM education.
- Defining **learning objectives in CM** (what exact competencies students should gain).

This fits well if im:
- Designing/Modeling **learning objectives** for modeling courses (Bloom etc.)
- Investigating **challenges and competencies** in modeling education,
- Proposing a **framework or set of recommendations** for teaching modeling.

## Methods, Context and Social structure

### Methods and context (Sec. 7)

- Need more:
  - **Theory-building research**
  - **Longitudinal** studies,
  - **physioligcal** methods (e.g., eye-tracking) to understand modeling cognition.
- CM education should be expanded beyond higher ed into:
  - primary/secondary
  - teacher training,
  - industry/citizen science.

### Social strucute (Sec 7 / 6.6)

- Most authors specialize in 1-2 subtypes; only a minority of **generalists** work across multiple.
- Generalists tend to be more productive and central in networks.
- This specialization fuels **silos** in CM education.

The can support background claims like:

" Current CM education research is dominated bt specialist groups working in separate subfields, which may hinder the transfer of effective pedagogical strategies."




