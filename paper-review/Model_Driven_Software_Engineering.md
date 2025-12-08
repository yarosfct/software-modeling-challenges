# Model Driven Software Engineering in Education: A Multi-Case Study on Perception of Tools and UML

## 1. Problem and Research Question (Intro + Related Work)

- Modelling and MDE/MDA are recommended in CS/SE curricula and can improve quality and enable code generation, but **actual adoption is low**; many practitioners and students stay **code-centric.**
- Industrial studies report challanges such as:
  - modelling perceived as **not useful enough** or only for very complex systems,
  - MDE adoption hampered by **inadequate academic preparation,**
  - graduates perceiving UML/MDA as **ineffective**.
- A recurring suspected culprit: **tooling**
  - Industry: usability, complexity, interoperability, handling large models.
  - Education: anecdotal claims that industrial tools are "unwieldy", too complex,, or encourage use of features students dont understand; others aregue industrial tools should be used with proper support.


**Gap:**
Lots of **experience reports,** but little **systematic empirical evidence** on how tool and course context shape students' perception of modelling.

**Research questions (RQ1-RQ3):**

1. **RQ1**: How do students perceive modelling tools?
2. **RQ2**: How do course context and tool use influence students' perception of modelling?
3. **RQ3**: Compared to industrial use, what characteristics do modelling tools need in education?


## 2. Method: Two Courses, Four "Units of Analysis" (Section III)

- **Multiple-case study** with **two 3rd-year modelling/design courses:**
  - **Case I - US course:** focus on **MDA**, strong emphasis on code generation.
  - **Case II - Sweden course:** focus on broader **MBE**, including requirements, analysis, design and code gen.
- **Four units of analysis (UoA):**
  - **UoA1 (US):** Umple (textual UML/MDE tool).
  - **UoA2 (US):** Papyrus (UML tool) instead of Umple.
  - **UoA3 (SE):** Papyrus **with dedicated course-internal tool support.**
  - **UoA4 (SE):** Papyrus **without** that dedicated support.
- In all runs:
  - students created **structural + behavioural UML models,**
  - delivered a **running system,**
  - applied >80% of lecture material in the project (constructive alignment).
- **Data:**
  - **Quantitative**: 369 anonymous end-of-course questionnaries (6 likert items about tools and UML).
  - **Qualitative**: open questions, free-text comments, plus follow-up intervies (US case).
  - Qualitative data coded in a **grounded-theory-inspired** manner.

## 3. Key Results - Perception of Tools vs UML (Section IV and V)

### 3.1 Tools: Umple vs Papyrus and the role of support (Case I and II)

**US course (Umple vs Papyrus - UoA1 vs UoA2):**

- **Umple (UoA1):**
  - Tool usefulness and impact on project: **clearly positive** (~65% agree it helped the project, ~40% see it as useful for large systems).
  - Ease of learning: **majority positive** (~65% agree).
- **Papyrus (UoA2):**
  - Tool usefulness and impact on project: **strongly negative** (~80% disagree it helped or is useful for large systems).
  - Ease of learning: mixed/negative (~48% disagree it is easy to learn).

**Swedish course (Papyrus with vs without dedicated support - UoA3 vs UoA4):**

- **With extra support (UoA3):**
  - Tool evaluation **balanced**: roughly a third positive, a quarter negative.
- **Without that support (UoA4):**
  - Perception turns clearly **negative** (about half disagree Papyrus was useful or easy to learn).
- The change in Papyrus evaluation between UoA3 and UoA4 is **statistically significant** (p < 0.01) for all tool-related questions.

**Interpretation (Section V):**

- Students perceive tools as **cumbersome** especially when:
  - the tool is complex,
  - code generation is fragile (poor round-trip support -> fear of overwriting code -> ugly workarounds),
  - **support is insufficient.**
- Dedicated tool support from **a teacher who understands both the tool and the course context** significantly improves perceptions; relying only on vendor/community documentation is not enough.


### 3.2 UML: More robustly positive, but sensitive to context

- **In US course:**
  - With Umple (UoA1): most students agree UML is useful for large/complex systems and that modelling before coding is beneficial, though many doubt whether benefits outweigh effort.
  - With Papyrus (UoA2): UML perception becomes **much more negative;** fewer students see UML as useful or modelling as beneficial, mirroring their bad experience with the tool.
- **In Swedish course:**
  - Across UoA3 and UoA4, UML perception is **consistently very positive:** ~85%-90% agree its useful for large systems and that modelling before coding helps; ~65%-70% say benefits outweigh effort.
  - Notably, this **doesnt change much** even when Papyrus perception worsesn in UoA4.


**Interpretation:**

- UML itself is often viewed **more positively** than the tools.
- Perception of UML is:
  - **strongly coupled to tool experience** when modelling is used mostly for **formal, code-generation-focused MDA** (US case).
  - More **robustly positive** when modelling is used for a **mix of informal and formal tasks** (requirements, analysis, communication + some code generation) as in the Swedish MBE course.


## 4. Observations: What Actually Affect Perception (Section V)

### 4.1 MBE vs MDA and formal vs informal models

- **Case I (US):** strong MDA orientation (formal models for code generation).
  - Tools must support precise semantics and round-trip engineering; when this fails or feels heavy, students' perception of both **tool and UML** drops.
- **Case II (Sweden):** broader MBE orientation:
  - Students model vague requirements, explore the problem domain, create domain and communication-oriented models, plus some code-oriented models.
  - This **informal + formal mix** correlates with **consistently positive UML perception,** even when tool perception is only moderate.

**Takeaway:**
> Students tend to value modelling more when they use it **early and informally** for understanding and communication, not just as a precise input to code generators.

### 4.2 Project domain and task design

- US course: project domain **familiar and tightly specified** (e.g., registration system), so students focus mainly on design and implementation.
- Swedish course: only **vague initial description** (hotel booking), students must **elicit and refine requirements** themselves; modelling supports exploration and shared understanding.

Result:
- Domain that requires **exploration and clarification** seems to enhance the perceived usefulness of UML for **requirements and communication.**


### 4.3 Round-trip engineering and feedback

- Where code generation and regeneration are **clunky** (Papyrus with limited regeneration support, manual workaround), students become frustrated; they see the tool as an obstacle.
- Where code generation is integrated (Umple, EMF with protected regions), students appreciate the added value once they have mastered the process.
- Authors link this to **feedback**:
  - Tools like Papyrus mainly give **negative feedback** (error messages) -> similar to compiler errors, which are known to hurt motivation.
  - This can provoke low motivation and negative tool perception even though the feedback is actually useful.
  - There is a risk of **"feeling of knowing":** without strict tools, students think their imprecise models are fine because they look familiar. Too-enforced errors break that illusion but also hurt feelings.

**Implication:**
> For education, we need tools (or configurations) that still give **constructive, education-tailored feedback** rather than only harsh error messages.

### 4.4 Educational vs Industrial tool characteristics (RQ3)

Overlap with industry concerns:
- **Usability** and complexity are issues in both domains.

Differences for education:
- Less critical in education:
  - interoperability between many tools,
  - handling very large models,
  - organisational deployment issues.
- More critical in education:
  - **positive, understandable feedback,**
  - quick and **effective** (not necessarily industrial-strength) code generation,
  - **tight alignment with course project scope** and learning goals,
  - sufficient **in-course support** (teacher or tutor who knows the tool and the assignment).

## 5. Synthesised Takeaways for my thesis

I can reuse those as conceptual bullets or design implications:

- **Tool perception is context-dependent:** same tool (Papyrus) is evaluated very differently depending on support, project scope, and emphasis on formal code generation vs inforaml modelling.
- **UML reputation is fragile** in code-generation-heavy MDA courses, but **strong and stable** in MBE courses that use models for requirements, analysis, and communication.
- **Informal modelling early in the lifecycle** increases perceived usefulness; a purely code-generation view can make modelling seem like overhead. 
- **Education-tailored feedback** is crucial: negative, compiler-like errors may improve correctness but hurt motivation; the paper calls for more constructive, "encouraging" feedback mechanisms.
- **Educational tools dont need full industrial feature sets;** they need:
  - reasonable usability,
  - simple but reliable code generation and regeneration,
  - alignment with learning outcomes,
  - and strong pedagogical support.

## 6. Thesis-Ready one-paragraph summary

Liebel et al. report a two-case multi-year study of third-year modelling courses in the US and Sweden, comparing students' perceptions of modelling tools (Umple and Papyrus) and UML in different curricular contexts. Their survey and qualitative data show that tool perception is shaped not only by complexity and usability, but also by course design, project domain, the role of code generation, and the availability of dedicated tool support. Industrial-grade tools like Papyrus are perceived as cumbersome and demotivating when used mainly for precise, code-oriented MDA without sufficient support or reliable round-trip engineering, whereas a mix of informal and formal modelling tasks in a broader MBE setting leads to consistently positive perceptions of UML, even if the tool itself is only moderately linked. The authors argue that modelling tools for education should prioritise constructive, education-tailored feedback and simple, effective code-generation wrorkflows over industial concerns such as large-scale interoperability, and that modelling courses should balance informal requirements and analysis modelling with more formal, code-oriented uses to foster both learning and motivation.