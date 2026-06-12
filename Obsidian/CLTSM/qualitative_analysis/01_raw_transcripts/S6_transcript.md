# S6 reconstructed cleaned interview transcript

## Part 1 — Background, modelling experience, quality and sharing

**Interviewer:** Thanks for meeting with me. I am studying how students learn modelling in higher education, especially what feels difficult, what helps, and how teaching choices, tools, and course conditions affect that experience. You can skip any question. Since this is a reconstructed transcript, I will focus on the content of what was discussed rather than exact wording.

**Participant:** Yes, that is okay.

**Interviewer:** Could you briefly tell me your programme, year, and which modelling-related courses or notations you have worked with?

**Participant:** I am in the first year of the master's in Informatics at a university in Munich. In my bachelor's degree at another German university, I had Software Design with UML: class, sequence, and component diagrams. Here in Munich, the most relevant course for your study was Requirements Engineering in the winter semester. We used iStar for strategic actor-goal models and more detailed rationale models. Then we used the NFR Framework for quality attributes such as performance and security, and finally UML use cases and class diagrams as a more concrete layer.

**Interviewer:** Have you used models outside those courses, for example in a thesis, internship, or personal project?

**Participant:** Not really. My experience is mostly from courses.

**Interviewer:** Can you describe one concrete moment when modelling felt difficult, confusing, or frustrating?

**Participant:** The hardest moment was the transition from our iStar rationale model to UML in the Requirements Engineering course. The strategic model made sense: actors, goals, dependencies. The rationale level was already harder because we had to decide how detailed to make the refinement of responsibilities. But when we translated it into UML, our pair produced a class diagram that looked syntactically correct but lost the goals.

The teaching assistant said the classes were fine as objects, but the trace from goals to classes was missing. I felt frustrated because nobody had explicitly explained how much of the iStar model should survive in UML. We knew both notations separately, but the bridge between them was unclear. That was confusion about process and integration, not about drawing actors.

**Interviewer:** When you get a text description and have to build a model, what happens in the first ten minutes?

**Participant:** In Requirements Engineering it depends on whether the brief is intentionally vague. If the assignment gives a short paragraph about an organisation and its problems, my first step is not UML. I list stakeholders and goals from the text, sometimes colour-coding what is explicit and what is assumed. Only after that do I open the modelling tool. In UML-only bachelor's exercises, I started faster with nouns and classes. It was a different habit.

**Interviewer:** When a teacher shows a worked example, what does that help you with?

**Participant:** In Requirements Engineering, examples helped me understand acceptable abstraction: how many actors are enough, and when to stop refining goals. For NFRs, examples showed how a quality attribute links to a softgoal and then to a design decision. Without examples, I would have listed qualities as bullet points rather than modelling them.

**Interviewer:** When you finish a model, how do you decide it is good enough?

**Participant:** In Requirements Engineering we were taught explicit quality ideas: completeness relative to the brief, internal consistency, and justification. My personal check is whether I can tell a story while walking through the model and explaining why each element exists. For NFRs, I ask whether a design choice is traceable to a stated quality.

**Interviewer:** Have you ever finished a model and still felt unsure because more than one answer might be valid?

**Participant:** Often in iStar, because different actor decompositions or dependency directions can be defensible. We documented alternatives in a short note, picked one, and justified it. The course encouraged explicit trade-offs, which reduced my exam anxiety. I still preferred confirmation from the teaching team in office hours.

**Interviewer:** How comfortable were you sharing a model before the teacher showed a solution?

**Participant:** Medium comfort. In pair work I share early with my partner. In the tutorial I am willing to discuss, but I do not volunteer to present an iStar model on the board unless I am confident. The notation is less familiar than UML. For UML labs I am more open. So it depends on notation familiarity and audience.

## Part 2 — Requirements engineering practice, group work, AI, tools and conditions

**Interviewer:** What carried over between UML, iStar, and NFR models, and what felt like starting over?

**Participant:** There is conceptual overlap: actors relate to use-case actors, and classes can realise responsibilities. But the mindset resets. UML felt more structural. iStar felt organisational and political: who depends on whom, which goals conflict. NFRs added a judgement layer. You cannot prove security in a diagram; you argue partial satisfaction.

The course was explicitly multi-family, so starting over was expected. The real pain was the missing methodology for translation between the models.

**Interviewer:** Did the course include vague briefs, stakeholder interviews, or justification?

**Participant:** Yes, that was central. We received a deliberately short brief about improving digital services for international students on campus. We had to identify stakeholders: administration, students, IT support. We interviewed classmates playing roles, and one real staff interview was optional. Different pairs produced different requirement lists after interviews. We also had a second prioritisation round.

Justification was required in the report: why this actor, why this dependency, why this UML class maps to that goal. Role-play felt artificial and a bit silly at first, but it showed how requirements change depending on who you ask. Vague briefs were stressful initially because I wanted a definitive specification, but later I understood that this was the point.

**Interviewer:** In the group project, who owned the model?

**Participant:** It was a pair project, so ownership was fairly equal. We split by diagram type. I owned the iStar refinements; my partner owned the early UML drafts. We reviewed each other's work in weekly syncs. I dislike larger groups because free-riding appears quickly, but pairs work for me. Modelling helped us merge interview notes into one picture before arguing about implementation. Without the strategic model, we would have jumped to features too early.

**Interviewer:** Did you use AI tools for modelling?

**Participant:** I tried ChatGPT once to explain an iStar dependency in plain German. It was useful. I did not use it to generate models for submission because the course warned about AI and academic integrity, and the grading focused on justification that you had to defend orally. I am more interested in AI that compares a model to a natural-language brief semantically, not AI that only draws boxes.

**Interviewer:** How did tools, course scale, and missed material affect the experience?

**Participant:** We used a goal-modelling tool for iStar with semantic checks — I think it was PyStar or something similar. [CHECK: verify the tool name if it matters analytically.] It prevented illegal dependencies, which was helpful. UML was done in a standard drawing tool without integration. Switching tools created friction.

The lecture had roughly eighty students, with tutorials of about twenty. Feedback was mainly in tutorials and in written comments on milestones. That was enough if you attended tutorials. Slides alone were weak for NFR refinements because the examples were partial. I missed one tutorial and had to reconstruct NFR softgoal refinements from PDFs, which was painful.

**Interviewer:** What domains motivated you?

**Participant:** I am less driven by exciting stories than some classmates. I prefer well-bounded organisational problems, such as campus services or compliance workflows, where success means having a coherent model. The international-student service domain worked because the stakeholders were concrete.

**Interviewer:** Have you modelled for someone who would analyse the diagram?

**Participant:** Yes, the teaching assistant and the role-play stakeholder. I cleaned up the layout and used consistent naming because someone else had to read the diagram quickly.

**Interviewer:** Have you used modelling outside university?

**Participant:** Not professionally. In my bachelor's internship we used Jira and Confluence, not iStar. I was surprised by how informal industry felt compared with the Requirements Engineering class.

## Part 3 — Closing

**Interviewer:** What is one realistic teaching improvement?

**Participant:** Teach the translation path explicitly. I would like one continuous example from goals to NFR decisions to UML, with trace links documented. Also, either integrate the tools or at least use a shared rationale table so we do not redraw the same semantics in three places.

**Interviewer:** Is there anything important I did not ask?

**Participant:** Requirements modelling is uncomfortable at first because there is no compile button. You have to live with ambiguity longer than in programming labs.

**Interviewer:** Thank you. This was very helpful.

## quick-reference card

```
S6-type participant
─────────────────────
Institution:  university in Munich (Informatics MSc, year 1)
Modelling:    RE (iStar, NFR, UML); bachelor's UML
Personality:  methodical; pair-work OK; sceptical of large groups
Motivation:   bounded organisational problems; coherence over "fun" domains
AI:           explain-only; integrity-sensitive
Gap to probe: BPMN, industry use, massive MOOC-style courses
```
