# Adolph, Hall and Kruchten — "Using grounded theory to study the experience of software development"


## 1. What this paper is and why it matters (Intro and Sec. 2)

- Its **both**:
    1. A **methods papers:** how to actually do **classical (Glaserian) Grounded Theory (GT)** in software engineering.
    2. A **meta-experience report:** what worked, what went wrong, and 15 guidelines for SE research.
- Their substantive study (background):
  - Question: **"How do people manage the process of software development?"**
  - Focus: **social processes** and how software practitioners resolve their **main practical concerns,** not tools/tech only.
  - They ultimately developed a GT about **"Reconciling Compromise"** (how people reconcile perspectives to "get their job done").

For my thesis: this is my **"how to actually do classical GT in SE"** reference (even tho ill follow the STGT); it complements Stol's review and STGT by being very concrete and SE-specific.


## 2. Grounded Theory in a nutshell, as they frame it (Sec. 3)

### 2.1 What GT is

- **Grounded Theory** = a method for **generating mid-level substantive theory** from data (not just testing theory).
- It aims to explain **"whats going on here":** how people **manage a problematic situation** over time.
- Output: a **set of integrated conceptual hypotheses** (categories + relations) explaing participants' **main concern** and how they resolve it.

### 2.2 GT vs. "normal" SE research

- SE research mostly focuses on **methods, tools, notations;** only a tiny fraction addresses **organisational / social issues** with qualitative methods.
- GT is appropriate when:
  - the are is **under-theorized,**
  - you want a **fresh perspective,**
  - you want to **generate** theory about social processes (e.g., how teams use modelling, how students experience modelling education).
- GT is **not** for questions like "is X better than Y?" but for questions like:
  "How do people manage X in practice?"


## 3. Their GT analysis model — how it actually works (Sec. 3-4)

They give a clear process model (Fig. 1) that i can reuse in my thesis methodology section:

1. **Data collection and open coding**
   - Collect qualitative data (interviews, observations, docs).
   - Break into **indicators** (words, sentences, paragraphs pointing to some behaviour/event).
   - Compare **indicator <-> indicator** and group them into **concepts** (patterns of behaviour).
2. **Concepts, categories, properties (Sec. 4.2)**
   - **Concept**: recurring pattern of social behaviour (e.g., "Scouting").
   - **Category**: a higher-level concept aggregating multiple concepts (more abstract).
   - **Property**: a dimension of category (e.g., "plurality" ranging from individual <-> group).
   - They modelled this using UML classes to keep it clear for engineers (Fig. 4).
3. **Constant comparison (Sec. 4.3-4.4)**
   - Continually compare new indicators to:
     - other indicators,
     - existing concepts/categories.
   - This sharpens concepts, adds properties, and eventually leads to **saturation**: new data add no new properties -> indicators become **interchangeable**.
4. **Theoretical sampling (Sec. 4.5)**
   - Sampling is driven by **the emerging theory,** not by statistical representativeness.
   - Start with **judgemental sampling** to "bootstrap".
   - Once interesting categories appear (e.g., "Uncertainty", "Perspectives"), seek new data that **develop** these categories.
5. **Theoretical sensitivity (Sec 4.6)**
   - Your prior experience/knowledge gives you **"theoretical sensitivity"** (ability to see patterns).
   - BUT it must be treated as **just another source of data,** not imposed on the theory.
6. **Selective and theoretical coding (Sec. 5.4)**
   - **Selective coding:** identify a **core category** that:
     - recurs frequently,
     - is "most connected" (integrates other categories),
     - explains how the main concern is resolved.
   - They tried "Scouting" and "Bunkering" but these lack parsimony; finally, **"Reconciling Compromise"** emerged as a better core category.
   - **Theoretical coding:** use coding "families" (e.g., process, strategy, cause, context) to express how categories relate (e.g., movement through stages, causal links).
7. **Memoing, sorting, literature (Sec. 5.5-5.7)**
   - **Memoing** is central: write down every idea about concepts/relations as it "pops".
   - Later, **sort memos** to build the structure of the theory.
   - Literature review in **two phases**:
     - early broad "framing" phase,
     - deep comparison only after you have a stable core category (to avoud "forcing").


## 4. Grounded Theory in practice: issues and lessons (Sec. 5-6)

They are very honest about the messy reality, which i can quote or paraphrase as "leasons learned":

- GT is **tedious and non-linear**: many false starts, dead ends, "ah-ha" moments that later collapse.
- **Tools**: they avoided heavy CAQDAS tools and used Word + a Wiki to stay close to data, warning that tools can give a **false sense of productivity** while distancing you from the material.
- **Data collection:**
  - they used **both** semi-structured interviews **and** participant observation;
  - observation was crucial to see what people actually do vs. what they say.
- **Ethics and access:** they stress ethics review, long-term field access, and regular visits to maintain trust.
- **Rigor and quality:**
  - Use **Lincoln and Guba's trustworthiness criteria** (confirmability, dependability, credibility, transferability) instead of qualitative validity/reliability.
  - Use **Glaser's criteria:** fit, workability, relevance, modifiability, parsimony and scope.

They emphasise **auditability**:

- keep process memos (research diary),
- member checks (participants review interpretations),
- rich description of sites and sampling decisions.


## 5. The 15 guidelines (Sec. 7 — Summary)

Section 7 turns their experience into **15 practical guidelines** for SE researchers doing classical GT, such as:

- Reach out to **experts in Nursing/Education/Sociology** for support.
- Be explicit about **which GT flavour** you use.
- Start with a **broad problem area,** not a narrow predefined research question.
- Use **participant observation** as a first-class method, not only interviews.
- Bootstrap **theoretical sampling** from **judgemental sampling**, then let concepts drive where you look next.
- Treat **memoing as mandatory**
- Accept that **open/selective/theoretical coding happen in parallel,** not in neat phases.
- Judge your theory by **fit, workability, relevance, modifiability,** not by statistical validity.

I can summarise theses as **design principles** for my own methodology section.

## 6. Thesis-ready one-paragraph summary


Adalph, Hall and Kruchten report on their use of classical Glaserian Grounded Theory to study how people manage the process of software development and, in doing so, provide a concrete, software-engineering-oriented guide to using GT. They explain key GT concepts such as indicators, concepts, categories and properties, and descrive how constant comparison, theoretical sampling, theoretical sensitivity and memoing interact in an iterative process that culminates in the identification of a core category—in their case, a process they call "Reconciling Compromise". The paper details practical decisions about data collection (semi-structured interviews plus participant observation), tool use (simple text + wiki tools to stay close to data), and ethics and field access, and discusses rigor using Lincoln and Guba's trustworthiness criteria and Glaser's notions of fit, workability, relevance and modifiability. They conclude with 15 guidelines aimed at novice GT researchers in software engineeringm emphasising broad initial problem framing, the central role of memoing and participant observation, the importance of a clearly articulated core category, and the need to treat GT as a demanding but powerful method for generating theory about social and human aspects of software development.


