# Domain Diversity, Motivation, and Inclusion in Software Modelling Education

## 1. Problem and research questions (Sec. 1)

- Software modelling is **fundamental in SE education**, but often:
  - under-emphasised in curricula,
  - taught in a **top-down, formal** style,
  - perceived by students as **conceptually hard, tool-heavy, and detached from practice.**
- Prior research has looked at:
  - tools,
  - assessments,
  - misconceptions,
  but not at **how the choice of problem domains** (what you model) affects **motivation, inclusiveness, and learning.**


**Goal:**

Investigate **how modelling domains and assignment design influence:**
- student **motivation and engagement,**
- perceptions of **inclusiveness,**
- and perceptions of **feedback** in modelling courses.

**Research questions (RQ1-RQ4, Sec. 1):**

1. **RQ1**: How do different modelling domains affect student motivation and engagement?
2. **RQ2**: How do teaching methods and assignment design choices affect motivation?
3. **RQ3**: How is **inclusiveness** perceived in modelling assignments?
4. **RQ4**: How is **feedback** perceived in modelling assignments?

Usefulness: This paper will be my main reference when i talk about human factors, motivation, and inclusion in modelling education.


## 2. Method Overview (Sec. 3)

**Design**: two **parallel surveys**
- **Educator survey:** 22 university educators teaching modelling.
- **Student survey:** 90 CS / SE students who completed at least one modelling-related course.

**Instrumentation (Sec. 3.1-3.2):**
- Demographics: age, gender, country, degree, experience, minority status.
- **MOtivation**(RQ1): Likert ratings for domains such as:
  - Video games
  - Community platforms
  - Public information systems
  - Enterprise and business systems
  - Automation systems
- **Preferences and design (RQ2): question on:**
  - Gamification,
  - collaboration (group vs individual),
  - how educators choose domains.
- **Inclusion and bias (RQ3): question about:** 
  - feeling excluded,
  - whether domain affects inclusivenss and learningm
  - how educators consider diversity
- **Feedback**(RQ4):
  - students: "Does your feedback impact course quality?"
  - educators: how they give feedback and evaluate courses.


**Analysis (sec. 3.3):**
- **Quantitative:** descriptive stats + Fisher's exact test (alpha = 0.05) for differences between:
  - students vs educators,
  - men vs non-men
  - minority vs non-minority students.
- **Qualitative:** mix of **content analysis** (lists, domains) and **thematic analysis** (reasons, reflection), with collaborative coding and triangulation.

## 3. Key results - What matters for me (Sec. 4)

### 3.1 Motivation and Domains (RQ1 - Sec. 4.1, 4.2.1)

**Quantitative highlights (Sec. 4.1.3 / Fig. 1-2):**
- Students' motivation ratings for domains are highly varied - no domain is universally motivating or demotivating.
- Educators, however, have strong assumpstions:
  - they believe video games and automation systems are particularly motivating,
  - they often see enterprise/business systems as demotivating.
- Statistically significant mismatches between students and educators for:
  - **public information systems,**
  - **automation systems,**
  - **enterprise and business systems.**

**Qualitative themes - Students (Sec 4.2.1):**

- **Personal interests are primary drivers**
  > "My motivation depends on whether the domain matches my own interests."
  > Video games are mentioned a lot - but: some like them, some explicitly dont.
- **Societal relevance matters**
  Students report being motivated by **socially relevant topics** (health, climate, community, etc.), not just "fun tech".
- **Working context can matter**
  At least one student explicitly likes **social, collaborative environments** more than the domain itself.

**Qualitative themes - educators (sec. 4.2.1):**
- Educators agree that **students' interests** drive motivaton, but:
  - they often **project stereotypical interests** (e.g., "students like video games") instead of asking.
- Some believe complex "real" examples in engineering settings are motivating; others avoid domains they dont personally know well, even if students might like them.


For the thesis:
I can argue that the **domain choice is a major motivational lever,** and that **educator assumptions about "fun" domains dont always match student reality.**

### 3.2 Gamification and Collaboration (RQ2 - Sec. 4.1.2, 4.2.2)

**Gamification - Students (Sec. 4.1.2, 4.2.2):**

- Majority say **gamification increase motivation** (Strongly agree/agree = 70/90).
- But nuanced concerns:
  - can cause **frustration** if competitive or badly designed,
  - some dislike competition,
  - some feel it can distract from learning,
  - a few find it **condescending**.

**Gamification - Educators (Sec. 4.2.2):**

- Generally see **potential**, but:
  - are more cautious,
  - worry about over-reliance,
  - several have **no experience** using it.

**Collaboration - Students (Sec. 4.2.2):**

- Preferences are **split**:
  - 32 prefer **group projects,**
  - 29 prefer **individual**,
  - 21 no preference.
- Trade-offs they mention:
  - pros: discussion, cross-evaluation, teamwork skills;
  - cons: **distrust of peers,** uneven workload, free-riding.

**Collaboration - Educators (Sec. 4.2.2):**

- Most **believe students prefer groups** and see strong benefits:
  - richer discussion,
  - exposure to multiple solutions,
  - easier scaling of evaluation.
- Some still mix in individual tasks to ensure autonomy and fairness.

**Assignment design - domains used (Sec. 4.2.2):**

- When choosing domains, educators mention:
  - student interest,
  - fit with degree/program and learning goals,
  - general relevance and "tangible" domains.
- Common domains include:
  - travel and transport,
  - organisational/business processes,
  - education and knowledge,
  - digital media and entertainment,
  - cyber-physical systems.

For the thesis:
> I can say that **gamification and collaboration are not universally good;** they **need careful desing** and **sensitivity to individual differences** to avoid backfiring.


### 3.3 Inclusion and Bias in Domain Selection (RQ3 - Sec. 4.2.3)

**Students - experiences of exclusion (Sec. 4.2.3):**

- Many say they **havent felt excluded,** but those who did highlight:
  - **Unfamiliar domains** (e.g., specific games known only in certain cultures; finance concepts like loans).
  - **Representational issues** (e.g., only "male/female" gender option in assignments).
  - **Assignment setup** as exclusionary (e.g, forced large group work in class not accessible to students with disabilities).

**Impact on inclusiveness and learning (Sec. 4.2.3):**

- Students emphasise:
  - **Sense of belonging** - domains targeted at "one type of person" can demotivate others.
  - Background matters: what's familiar and meaningful for some is hard and alienating for others.
  - **Problematic domains** (with built-in misogyny, phobias, etc) are tricky to "sanitize" in modeling assignments.
- Many say familiar and intresting domains clearly **help understanding**, while abstract/unfamiliar ones hinder it; a few feel that with good explanation, domain matters less.


**Preferred domains (Sec. 4.2.3):**

- Students recommend:
  - **Socially relevant topics** (mental health, climate, culture),
  - **Everyday contexts** (Student life, education, transportation),
  - **Community platforms,**
  - Games that are **not tied to hardcore gamer culture.**
- Strong emphasis on **choice**:
  - "Choose your own topic/theme" seen as best for diverse groups.


**Educators - diversity practices (Sec 4.2.3):**

- Three patterns:
  - some **explicitly consider divesity** (avoid conflict-prone domains, include international/familiar contexts, challenge stereotypes),
  - some **implicitly** (use everday or study-related contexts, let students choose),
  - some **do not consider diversity at all** when picking domains.
- Observed differences in preferences (e.g., some game domains appeal more to men; social/ecological projects more to women), but many educators **do not systematically react** to this.
- Suggestions for inclusive modelling education:
  - use **variety of domains and task types,**
  - allow **some autonomy** in domain choice,
  - design **small + medium inclusive cases**, then a larger real-world case,
  - use **accessible tools** and avoid domains that assume certain economic or cultural experience (e.g., staying in hotels).


For the thesis:
> This is a strong evidence that **domain choice is an inclusion issue,** not just a motivation issue, and that **cultural / economic assumptions and representations** matter even in "neutral" modelling tasks.


### 3.4 Feedback (RQ4 - Sec. 4.2.4)

**Students (Sec. 4.2.4):**

- They interpret "feedback" as **course-level feedback**, not just comments on their solutions.
- Three views:
  - **Positive impact** - many believe feedback improves course quality and motivates change. 
  - **Conditional impact** - only if:
    - it is given **early enough** to affect the current cohort,
    - they **see concrete changes** (e.g., isses from previous years being fixed),
    - their views are shared by enough peers.
  - **No impact** - some feel teaching is low-priority and courses rarely change, so feedback doesnt matter.

**Educators (Sec. 4.2.4):**

- Provide **formative feedback** via;
  - consultations,
  - lab/practical sessions,
  - written comments.
- Use **scalable mechanisms**:
  - automatic feedback (exercise platforms),
  - peer review (e.g., double-blind group-to-group reviews).
- Evaluate courses mostly via **standardised surveys** and long-term refinement.

Gap: Students value feedback **only when they see visible action**, while educators often see their own feedback processes as sufficient. This is important if i talk about **feedback and perceived support** as part of modelling challenges.


## 4. Synthesised Recommendations (Section 5.3 and Table 2)

The authors condense their finding into **practical recommendations** for inclusive, motivating modelling education (table 2, sec 5.3):

- **Use students' interests**
  - Offer **choice of domains** where possible.
- **Show societal relevance**
  - Link assignments to **real-world, socially meaningful problems,** not just generic technical examples.
- **Use gamification wisely**
  - Keep it engaging, but avoid strong competitive elements and "gamification for its own sake."
- **Support collaboration**
  - Scaffold teamwork, discuss fair workload, and use mechanisms like peer review to reduce free-riding.
- **Avoid narrow / biased examples**
  - Dont rely on culturally specificm stereotipical, or economically exclusive domains; prefer everyday, accessible context.
- **Make feedback visible**
  - Collect feedback iteratively, show students how it changes the course, andensure minority voices arent drowned out.

For my thesis, this can becaome a **"design implications" bullet list** when  i argue how modelling courses should be improved.


## 5. Thesis-ready one-paragraph summary

This paper investigates how domain choice, assignement design, inclusiveness, and feedback jointly shape motivation in software modelling education, based on parallel surveys with 90 students and 22 educators. The results reveal substantial mismatches between educator assumptions and student preferences: educators tend to assume that technical domains such as video games and automation are broadly motivating, while students' motivation is primarily driven by personal interests and socially relevant, everyday domains. Students highlight that unfamiliar or culturaly specific domains, economic assumptions, and a lack of representation can make assignments feel exclusive, and they strongly value being able to choose or personalise domains. Gamification and groip work are generally seen as motivating but can backfire if overly competitive or poorly scaffolded, especially given students' concerns about unequal collaboration. Feedback is appreciated only when students see visible changes in course design, whereas educators often rely on standardised surveys and believe they already provide adequate feedback mechanisms. Drawing on these finding, the authors recommend student-centred domain selection, careful use of gamification, better scaffolding of collaboration, and more responsive, visible feedback practices to foster inclusive and engaging modelling education.



