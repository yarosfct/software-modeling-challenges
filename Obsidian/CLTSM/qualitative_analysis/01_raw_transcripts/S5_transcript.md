# S5 reconstructed cleaned interview transcript

## Part 1 — Background, modelling experience, quality and sharing

**Interviewer:** Thanks for meeting with me. I am studying how students learn modelling in higher education, especially what feels difficult, what helps, and how teaching choices, tools, and course conditions affect that experience. You can skip any question. Since this is a reconstructed transcript, I will focus on the content of what was discussed rather than exact wording.

**Participant:** Sure, no problem.

**Interviewer:** To situate your answers, could you briefly tell me your programme, year, and which modelling-related courses or notations you have worked with?

**Participant:** I am in the fourth year of Computer Science at the university in Wrocław. Most of my modelling experience is UML from Software Engineering and Systems Analysis: class diagrams, use cases, sequence diagrams, and some activity diagrams. We also did ER modelling in Databases.

The course where modelling felt most real to me was Software Engineering last semester, because we had a team project for a campus event app: scheduling talks, rooms, and student clubs. We kept a shared Miro board with living diagrams. I have not done BPMN or iStar in graded work.

**Interviewer:** Have you used models outside those courses?

**Participant:** Only informally. In the project team, even after the graded part, we still updated a simplified component sketch on Miro when we debated features. So modelling continued as a habit for that group.

**Interviewer:** Can you describe one concrete moment when modelling felt difficult, confusing, or frustrating?

**Participant:** The frustration I remember best is from Systems Analysis, not from the group project. We had to build a sequence diagram for a library reservation flow with timeouts and cancellations. I started confidently because our group had already aligned on the class diagram, but the sequence diagram became messy very fast: too many messages, optional fragments, and uncertainty about where to put loops.

I felt stuck on notation and granularity, not on starting. What made it worse is that I usually volunteer to present in labs. I drew something on the board thinking it was fine, and the teacher asked three questions I could not answer, for example whether a synchronous message was on the right lifeline. I was embarrassed, but it was useful. The difficulty was technical and about level of detail, not about whether modelling mattered. My teammates helped after class because we whiteboarded it again together.

**Interviewer:** When you get a text description and have to build a model, what happens in the first ten minutes?

**Participant:** In a group, the first ten minutes are discussion. Someone reads the text aloud, we each say what jumps out, and we decide who drafts the first diagram. Usually that is me, because I do not mind. If I work alone, I still talk through it out loud, sometimes even recording a voice note. Practically, I list actors and main events, then open Miro or Visual Paradigm and place the obvious boxes.

I rarely wait for a teacher demo. If the teacher has not shown an example, I might message the group chat saying, “I will draft version one tonight,” and treat feedback as the safety net.

**Interviewer:** When a teacher solves or discusses an example, what does that help you with?

**Participant:** Examples help me calibrate the level of detail. I tend to over-model because I like the diagram to feel complete. When the teacher shows a simpler acceptable solution, I learn what to leave out. Transfer works if the example explains decisions. In Software Engineering, our teacher compared two class diagrams for the same feature, one bloated and one minimal. That transferred directly to our event app. I used the same idea with my team that week.

**Interviewer:** When you finish a model, how do you decide whether it is good enough?

**Participant:** In a group, good enough means the team can point at the diagram and agree on what we are building next. We literally ask whether a new person could join tomorrow and understand the feature scope from the picture. Personally, I also check consistency: class names in the sequence diagram should exist in the class diagram.

Teachers mentioned completeness and readability, but our internal rule is team comprehension first and rubric second. Before submission I still want the teacher's approval, but internally we decide earlier through peer review in the lab.

**Interviewer:** Have you ever finished a model and still felt unsure because more than one answer might be valid?

**Participant:** Yes, especially with multiplicity and inheritance. In a group we argue it out, sometimes too long. If we cannot agree, we pick the simpler version, implement a small prototype, and let the code expose the mistake. That works for us because we are comfortable disagreeing publicly. I would still ask the teacher if the grade matters, but we do not freeze while waiting for authority.

**Interviewer:** If you complete a model before the teacher shows a solution, how comfortable are you sharing it?

**Participant:** Very comfortable. I will show it in the lab, post it in the group chat, or even present a work in progress to the class if the teacher asks for volunteers. Early sharing is how I learn. What helps is that my teammates also comment without treating the draft as final. If I were shy, I think I would hate that pressure, but for me public drafts reduce anxiety because errors surface early.

## Part 2 — Group work, AI, tools and domains

**Interviewer:** You mentioned UML and ER. What carried over, and what felt like starting over?

**Participant:** Entities to classes was fine. Relationships too. Sequence diagrams were the real reset, because time ordering felt unlike anything in ER. Activity diagrams were somewhere in the middle; they helped for event flows in our app. Because I learn a lot through group explanation, the transition was easier when someone narrated the diagram aloud while drawing.

**Interviewer:** In group projects, who built and owned the model?

**Participant:** We treated the model as shared ownership. I did most of the drawing because I like facilitation, but two teammates owned review: one checked consistency with requirements and another checked feasibility for Android implementation. Every week we had a short “diagram stand-up” for about ten minutes. Modelling helped coordination a lot. Without the Miro board, we would have argued in code.

The only overhead was keeping the diagram updated when someone merged features without telling us. Then someone had to sync the model, usually me, which was annoying but still worth it.

**Interviewer:** Have you used ChatGPT, Copilot, or similar tools with modelling?

**Participant:** Yes, more than my friends admit. I used ChatGPT to suggest alternative class diagrams from a bullet list, then compared options with the team. I also asked it to simplify an overcomplicated sequence-diagram description. For graded work, we rewrote everything ourselves and documented changes, but it was useful as a brainstorming partner.

I would not submit raw AI output. A semantic checker that says, for example, “this message does not match any operation in your class diagram” would be amazing, and more useful than generic text generation.

**Interviewer:** How have tools affected your experience?

**Participant:** Miro lowered the barrier for group modelling because everyone edits live. Visual Paradigm in the lab gave stricter UML semantics, which I appreciated before implementation. draw.io alone would be too free-form for our team pace. Large courses were not my main problem: we had maybe around sixty students, labs of fifteen, and the teaching assistant commented on our Miro link once. That was enough feedback for us.

**Interviewer:** What domains make modelling feel worth the effort?

**Participant:** Interesting domains help, but a good team can make even a medium domain work. The campus event app was motivating because we were building for ourselves. I prefer domains with real users, like campus, clubs, or local services, over abstract enterprise examples. If the team is engaged, I will model carefully anyway. If the team is passive, even a great domain will not save it.

**Interviewer:** Have you modelled for someone who would analyse or use the diagram?

**Participant:** Yes, our teaching assistant and two club coordinators who acted as informal stakeholders for the event app. Knowing they would look at the use case diagram pushed us to use their vocabulary, not only ours.

**Interviewer:** Have you used modelling outside university, in an internship or job?

**Participant:** Not yet. I expect industry to use lighter sketches, but I hope teams still do some diagramming in planning.

## Part 3 — Closing

**Interviewer:** What is one realistic change that would improve how modelling is taught?

**Participant:** More assessed group modelling milestones, not only the final report diagram. Weekly small diagram reviews with peer comments would mirror how good teams already work. I would also teach earlier how to simplify diagrams, because over-modelling costs time in groups too.

**Interviewer:** Is there anything important I did not ask?

**Participant:** Personality matters. For me, group modelling is a social skill as much as a technical one. Courses sometimes assume everyone wants to whiteboard together. That helps people like me, but it can hurt quieter students.

**Interviewer:** Thank you. This was very helpful.


## quick-reference card

```
S5-type participant
─────────────────────
Institution:  university in Wrocław (CS, year 4)
Modelling:    UML + shared Miro in team SE project
Personality:  outgoing; volunteers in labs; enjoys group coordination
Motivation:   team engagement + user-facing campus domains
AI:           team brainstorming with manual rewrite before submit
Gap to probe: RE/BPMN, executable models, very large cohorts
```
