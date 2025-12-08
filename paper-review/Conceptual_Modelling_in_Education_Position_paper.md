# Conceptual Modelling in Education: Position Paper

## 1. What the paper is about and why it matters (Abstract and Sec. 1 - Introduction)

- The paper is a **position paper** on how we teach conceptual modelling (CM) and how students perceive it.
- Main thesis:
  - CM should be presented as a **standalone discipline** with its own **value proposition in any domain** (not just as "a chapter in Software Engineering").
  - **Modelling languages** should be understood as **purposeful knowledge schemas** that can be **agilely adapted** to support model-driven systems and decision processes.
- Motivation:
  - Students and junior researchers often approach CM with **oversimplified preconceptions**, e.g.:
    - "CM is just documentation diagrams"
    - "It's only for SE"
    - "One language is enough for everything"
  - The preconceptions limit how they see the **value of models** and **how broadly CM can be applied.**

### For my thesis:

> This papers gives me conceptual ammo to argue that CM should be treated as a **discipline in its own right,** and that how we frame CM to students (as knowledge schemas, not just diagrams) is crucial for education and research.

## 2. The core position statements (Sec. 2 - Position Statements)

Section 2 lists **6 "oversimplifications"** and counters them with **position statements.**
These are basically teaching messages about CM.


### 2.1 Oversimplification 1 - "CM is just graphical documentation" (Sec. 2)

- **Oversimplification:**
  CM = drawing diagrams that visually document something.
  Students often use PowerPoint/Visio etc. as "modelling tools."
- **Position:**
  CM produces **knowledge structures** that can have a visual form - not just pictures.
  - A model must be **conformant to a knowledge schema** (metamodel / modelling language).
  - This enables **model queries** (e.g., "find all tasks after this decision in the BPMN model"), similar to **database queries.**

So: **a modelling language = schema for a model repository**, not just a drawing style.

Useful for me:
> I can use this to support the idea that learing CM should emphasize **semantics + queryability + structure**, not just how diagrams look.

### 2.2 Oversimplification 2 - "Modelling languages are fixed vocabularies" (Sec. 2)

- **Oversimplification:**
  Modelling languages are static vocabularies defined by standards (e.g., UML, BPMN).
- **Position:**
  Modelling languages are **knowledge schemas that can be tailored to purposeful, evolving requirements.**
  - Analogy: a **database schema** is usually stable, but can be adapted when requirements change -> same for modelling languages.
  - Even standards allow customisation (e.g., **UML stereotypes**)

So: languages should be taught as **adaptable engineering artefacts**, not immutable.

Usefulness:
> Supports the idea of **agile modelling method engineering** and **method tailoring** as part of advanced modelling competences.

### 2.3 Oversimplification 3 - "CM is subordinated to Software Engineering" (Sec. 2)

- **Oversimplification:**
  CM is "a part of SE" (because first contact is often UML in SE/context).
- **Position:**
  CM is applicable to **any domain where complexity must be managed** through abstraction and structuring:
  - e.g., Marketing, Service Design, Service-Dominant Logic, etc.
  - Students are encouraged to use CM for their own domain, with either:
    - existing **domain-specific methods**, or
    - **new abstractions** they design themselves (Design Science).

So: CM should be framed as **cross-domain** and **not tied** to any one discipline.

Usefulness:
> This strongly supports the idea (also present in other papers) that CM is **transdisciplinary** and that CM education should prepare students for multiple domains, not just SE.

### 2.4 Oversimplification 4 - "One modelling language is enough for everything" (Sec. 2)

- **Oversimplification:**
  "I can model everything in language X; i dont need other languages."
- **Position:**
  - In practice, this usually means:
    - stuffing domain-specific info into **labels/annotations**, or
    - **"hacking" semantics** (e.g., misusing BPMN symbols to represent ingredients in a recipe).
  - This breaks **model queries** and semantics
  - Better approach: **adapt or extend the language** to include the missing concepts via **metamodelling** platforms.

Usefulness:
> A nice example of why **tool/notation flexibility and meta-modelling** should be part of advanced CM competences (and why "learn one language and you are done" is wrong).


### 2.5 Oversimplification 5 - "Model value is created only by modellers" (Sec. 2)

- **Oversimplification:**
  Only modellers (e.g., business analysts) create value; methods and languages are "fixed background."
- **Position:**
  - Value is **co-created** by:
    - **modeller**,
    - **modelling method engineer** (who adapts the method/language),
    - plus **domain experts** and other stakeholders.
  - The modelling method engineer is responsible for **capturing the right abstractions** and evolving the language/schema where needed.

Usefulness:
> This supports a view of **CM education** that includes not just end-users of languages, but also **method engineers/metamodellers** as separate role/competence.


### 2.6 Oversimplification 6 - "Languages are just general-purpose vs domain-specific" (Sec. 2)

- **Oversimplification:**
  There are two kinds of languages: "general-purpose" and "domain-specific".
- **Position:**
  They propose **two independent axes:**
  - **Purpose**: from general-purpose to narrow-purpose.
  - **Specificity**: from domain-agnostic to system-specific.
- Languages can move in this **Purpose-Domain space** via **language agility** (adaptation).

Usefulness:
> This is a conceptual tool i can invoke when discussing **variety of modelling languages, DSMLs, and transferability of educational approaches** (e.g., a language isnt just "DSML vs general"; it has a more nuanced position).


## 3. OMiLAB as enabler for this view (Sec. 3 - OMiLAB: the value proposition)

- **OMiLAB (Open MOdels Laboratory)** = a digital ecosystem that **supports the postion statements in practice.**
- It offers:
  - **Open-source modelling tools** that can be tweaked for new domains/purposes.
  - Infrastructure to **prototype new modelling methods** (using the **AMME - Agile Modelling Method Engineering** framework).
  - Features for **model-driven artefacts**, model queries, reasoning, interoperability (RDF, XML, model-as-a-service).
  - A corpus of modelling-related publications and teaching cases.
- Key platform: **ADOxx**, used for metamodeling and rapid tool prototyping, making it easy to **tailor knowledge schemas**.

Usefulness:
> OMiLAB and AMME show that **teaching CM as a flexible, engineered discipline** is not just theory; there are platforms and communities organized explicitly around this educational perspective.


## 4. SUmmary and implications for education (Sec. 4 - Summary)

- The paper's contribution is **not empirical**, but conceptual/educational:
  - It articulates a **set of position statements** to help **novices** move beyond bachelor-level perceptions of CM and understand its value for **design research and innovation**.
  - It frames modelling languages as **knowledge schemas**, emphasizes **language agility, co-creation of model value**, and **cross-domain applicability.**
  - It calls for more **teaching experiences and artefacts** that embody this holistic view of model value and further refine the **Purpose-Domain space.**


## 5. Thesis-ready one-paragraph summary

Buchmann et al. argue that conceptual modelling should be taught as a standalone disciple with a value proposition that extends beyond software engineering to any domain where complexity must be managed through abstraction. They challange common oversimplifications held by students and junior researches - such as viewing CM as mere graphical documentation, assuming modelling languages are fixed vocabularies or subordinated to SE, or believing one language can model everything - and instead position models as instances of adaptable knowledge schemas that enable queries and model-driven functionality. The paer highlights the co-creation of model value by modellers, method engineers and domain experts, and proposes a two-dimensional Purpose-Domain space to characterize modelling languages more precisely than the typical general-purpose vs domain-specific dichotomy. The ideas are supported by the OMiLAB ecosystem and the AMME framework, which provide concrete infrastructure for agile modelling method engineering. Overall, the position paper offers a conceptual foundation for CM education that emphasises language agility, cross-domain applicability, and the need to explicitly teach students about the nature and value of modelling languages as engineered knowledge structures.


