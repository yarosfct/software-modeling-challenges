# A Research Agenda for Identifying and Developing Required Competencies in Software Engineering


## 1. Problem and Motivation (Intro)

- **Software engineering is hard to learn and to teach.** Reasons:
  - Involves **complex systems,** developed by **teams** over time for real users.
  - Requires **technical skills + social and personal competencies** (teamwork, communication, requirements elicitation).
  - Multiple roles (analyst, architect, tester...) each need **different competence profiles.**
  - Realist, large-scale projects are hard to simulate in university settings.
  - Fast technological changes $\rightarrow$ much factual knowledge becomes outdated; students must be prepared for **lifelong learning.**
- There is **no one-size-fits-all curriculum** for SE:
  - SWEBOK is the closest thing to a standard, but:
    - doesn't distinguish **which area is needed for which role,**
    - doesn't indicate **which didactic approaches** suit which topics,
    - barely addresses **soft skills.**

**Core problem:**
> We don't know **exactly which competencies** (technical + soft) software engineers should have for different contexts, nor **which teaching methods** effectively foster each competence.

## 2. Research Questions and EVELIN Agenda

They launch research project **EVELIN** (Experimental inproVEment of Learing software engINeering) to ststematically study SE learning in their Bachelor/Master programs.

**Two core research questions:**

1. **What competencies should a software engineer have?**
   - Including technical knowledge and soft skills.
2. **For a given competence, which didactic approach is appropriate or best suited?**

### 2.1 High-level research agenda (Fig. 1)

The agenda is an **iterative loop:**

1. **Identify target competencies ($t_0$):**
    - Define technical + soft competencies, and to what degree they are needed.
2. **Measure actual competencies ($t_1$):**
    - Establish a **baseline** (as-is) for students before a course.
    - Measure competencies after the course (to-be).
    - Analyse deficiencies and gaps.
3. **Identify influencing factors:**
    - Distinguish **structural items** (class size, timetable, infrastructure, lecturer attitudes) and **process variables** (teaching methods, interactions).
4. **Modify variables and re-measure ($t_2,t_3,...$):**
    - Change selected structural/process factors in a course.
    - Measure competencies again and compare with baseline / target.
    - Repeat in cycles and across cohorts to approach **stable target competencies** (Figures 3-4).


Goal: build an empirically grounded **subject didactics of software engineering** that links competencies <-> teaching methods <-> constraints.


## 3. Research Design: Grounded Theory + Triangulation

### 3.1 Grounded Theory approach

They explicitly base the project on **Grounded Theory:**

- Aim: develop theory about SE learning/teaching rather than just test pre-existing theories.
- Key characteristics:
  - **No fixed agenda** up front — next steps are planned based on **emerging findings.**
  - **Theoretical sampling:** data collection is guided by research interest; samples evolve over time, not design for statistical representativeness.
  - **Interplay of induction, deduction, and abduction:**
    - start from loose assumptions,
    - derive provisional concepts from data,
    - refine them through repeated cycles.


### 3.2 Mixed methods and triangulation

- **Qualitative methods:**
  - Guided, semi-structured interviews with students and lecturers.
  - Document analysis of curricula and course materials.
  - Focus on uncovering **implicit** aspects (hidden learning outcomes, tacit teaching intentions).
- **Quantitative methods:**
  - Questionnaires (including **BEcaKomp** items for self-assessment of competencies).
  - Exam results, structural data (class size, infrastructure, schedule).

They use **triangulation** (qualitative + quantitative) to strengthen validity.

For my thesis: this is a nice example of **Grounded Theory + design-oriented SE education research**.


## 4. EVALIN Competency Taxonomy (Classification System)

Six levels, not strictly hierarchical but ordered from simpler to more complex:

1. **Remember**
    - Recall information and reproduce it.
    - No requirement to understand it.
2. **Understand**
    - Capture the sense/meaning of information.
    - Often involves **implicit knowledge** (not necessarily verbalised).
3. **Explain**
    - Recognise and explain **relationships and analogies;**
    - typically about **cause-effect** and being able to **justify** an evaluation/choice in theoretical terms.
4. **Use**
    - Apply knowledge in a **define, simple context** with instructions, **without needing deep understanding.**
5. **Apply**
    - Autonomously use knowledge in **complex situations,** choosing and applying suitable solutions based on situation -> requires analysis and evaluation of context.
6. **Develop**
    - Devise **novel solutions or enhance existing ones** in a problem domain.


They argue this taxonomy is:
- expressive enough for SE competencies,
- still manageable for curriculum planning and LO formulation.
    They suspect it could work for generic (soft) competencies too, but that still needs validation.


For me: this is a concrete **competence-level taxonomy** i can cross-reference with Bloom / my own modelling-competency framework (if i choose this approach).

## 5. Data Collection Plan and Factors

### 5.1 Identifying target competencies

To instantiate the taxonomy for specific domains (informatics, embedded systems, etc.), they:

- Conduct **guided interviews with practitioners** (software engineers, managers).
- Analyse **existing curricula** (as documents, including teaching goals and didactic ideas).
- Examine external references such as **SWEBOK**.

This yields a set of **technical and non-technical competencies** needed in practice; they then decide which can/should be targeted in academic settings.


### 5.2 Structural items, process variables, and outcomes

They adopt Donabedian's **structure-process-outcome** perspective:

- **Structural items:**
  - Time of day of classes, class size, infrastructure, technical equipment, lecturers' attitudes and capabilities.
- **Process variables:**
  - Didactic methods, interactions, learning activities (project work, exercises, lectures, etc.).
- **Outcome:**
  - Measured competencies (as-is / to-be), exam results, self-assessments.


**Instruments:**

- Midterm questionnaires about:
  - course structure, didactic setting, technical conditions, motivation;
  - self-assessment of competencies (BEvaKomp).
- Interviews at intervals to uncover:
  - what students feel they learned and how,
  - what facilitated or hindered learning,
  - implicit intentions of lectures vs. actual outcomes.


They then **formulate hypotheses** about which structural/process factors influence learning and **experimentally modify** courses (e.g., emphasising teamwork more explicitly in a SE project course) and re-measure competencies.


## 6. Current Status and Outlook (Summary / Future Work)

At the time of the paper:

- They have:
  - Developed the **EVELIN classification system,**
  - Instantiated it with technical competencies derived from questionnaires, interviews, and curricula,
  - Identified a variety of structural and process variables to consider.
- Next steps:
  - Extend the competence model with **personal and social skills.**
  - Analyse needed competencies in **related domains** (mechatronics, etc.).
  - Investigate **lecturers' aims and attitudes**, since these strongly shape curricula and didactic decisions.
  - Conduct first **experimental course adaptations** (e.g., more explicit team-skills training) and evaluate impact on competencies.

Long-term aim:
> Derive a **theory of learning and teaching SE** and a **subject didactics** that can guide curriculum design, method selection, and continuous improvement.


## 7. Thesis-ready one-paragraph summary

Sedelmaier and Landes outline the EVELIN research agenda, which aims to build an empirically grounded theory of learning and teaching software engineering by identifying required competencies and linking them to effective didactic approaches. Recognising that SE education must cover diverse technical and soft skills under varying structural conditions, they propose an iterative, Grounded Theory-based process in which target competencies are defined, actual student competencies are measured before and after courses, and structural and process variables are systematically modified and re-evaluated across cohorts. A central contribution is the EVELIN classification system, a six-level taxonomy (remember, understand, explain, use, apply, develop) for describing technical competencies and learning objectives. Using mixed qualitative and quantitative methods, including interviews, curriculum analysis, and surveys, the project seeks to uncover how factors such as class size, teaching methods, and lecturer attitudes influence competency development, with the long-term goal of deriving a subject didactics for software engineering that can inform curriculum design and continuous course improvement.

