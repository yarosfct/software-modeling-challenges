# S4 reconstructed cleaned interview transcript

## Part 1 — Background, modelling experience, quality and sharing

**Interviewer:** Thanks for meeting with me. I am studying how students learn modelling in higher education, especially what feels difficult, what helps, and how teaching choices, tools, and course conditions affect that experience. You can skip any question. Since this is a reconstructed transcript, I will focus on the content of what was discussed rather than exact wording.

**Participant:** Sure, that is fine.

**Interviewer:** To situate your answers, could you briefly tell me your programme, year, and which modelling-related courses or notations you have worked with?

**Participant:** I am in the fifth year of Computer Science at the university in Wrocław. The modelling I remember most is from Software Engineering and from Systems Analysis and Design. In both courses we used UML: class diagrams, use cases, sequence diagrams, and a little bit of activity diagrams. In Databases we also did ER diagrams, although that felt more like schema design than what I would normally call software modelling.

Right now, in my master's thesis, I am using component diagrams and sequence diagrams to explain the architecture. I have not used BPMN or iStar in graded work, at least not that I remember.

**Interviewer:** Have you used models outside those courses, for example in your thesis or in personal work?

**Participant:** Mainly in the thesis. Sometimes I sketch a small diagram for myself before coding, just to understand an idea, but that is very informal. It is not the same as coursework modelling.

**Interviewer:** Can you describe one concrete moment when modelling felt difficult, confusing, or frustrating?

**Participant:** The clearest example was in Software Engineering, in the second semester of the third year. We had a group project, and the domain was a generic online shop. I did not find the domain very interesting, and the group work was uneven. I was trying to draw the class diagram, but two people in the group wanted to jump directly to implementation in Spring.

So I made a first version of the class diagram alone. When I showed it in the next meeting, one person said it was basically unnecessary paperwork. That was frustrating because, for me, the diagram was the only thing keeping the group aligned.

The hard part was not really the UML notation. I understood classes, associations, and basic multiplicities. The problem was social and motivational. I did not feel the domain was worth modelling carefully, and I also did not feel the group valued the model. Because of that, I stopped refining it. A week later, the diagram was very shallow and no longer matched the code. That experience made modelling feel pointless when the context around it does not support it.

**Interviewer:** When you get a text description and have to build a model, what do you usually do first?

**Participant:** If the domain is interesting, I start quite quickly. I read the text twice and underline nouns and verbs. Nouns become candidate classes or actors, and verbs become possible operations or use cases. Then I open the tool and begin with the simplest diagram that fits the task, usually a use case diagram or a small class diagram.

If the teacher has not shown an example yet, I can still start, but I am less confident. In Systems Analysis, there was one exercise where I waited because I was afraid the teacher expected a very specific style of use case description. Later I realised that my first instinct was basically fine. So I can start alone, but I prefer to check privately with the teacher if the task is ambiguous.

**Interviewer:** When a teacher shows a worked example, what does that actually help you with?

**Participant:** It helps most with the reasoning. It is not just about memorising shapes. For example, when the teacher explains why one relation is composition and another is just association, that stays with me. If the teacher only draws the final diagram, I can see what the answer looks like, but I do not learn how to get there.

One useful moment in Systems Analysis was when the teacher showed two versions of the same class diagram: one too detailed and one too abstract. The teacher explained why the second one was better for the assignment. That helped me because I could reuse the same idea later in my thesis.

**Interviewer:** When you finish a model, how do you decide whether it is good enough?

**Participant:** I have a kind of personal checklist, although nobody gave it to us as an official rubric. First, can I explain every element in plain language? If there is a class or a message I cannot explain, maybe it should not be there. Second, does the diagram match the written requirements? I go back to the task text and tick off the points. Third, readability matters, especially in the thesis, because my supervisor will review it. If the lines cross too much or labels are vague, I fix that even if the semantics are acceptable.

We were told about completeness and consistency in Software Engineering, but mostly in theory. In practice, I learned this checklist from feedback on drafts, not from one lecture.

**Interviewer:** Have you ever finished a model and still felt unsure because more than one answer might be valid?

**Participant:** Yes, especially with multiplicity and with the question of whether something should be a separate class or just an attribute. In Databases it was even worse, because normalisation can sometimes look valid in more than one way. Usually I pick the simpler model first, then show it to the teacher during office hours and ask whether the alternative would also be acceptable. I rarely ask in front of the whole class. If the teacher says both options are acceptable, I choose the one that is easier to explain in the report.

**Interviewer:** If you complete a model before the teacher shows a solution, how comfortable do you feel sharing your approach?

**Participant:** Not very comfortable in public. I am shy, so presenting a half-finished diagram to the whole class is stressful. I am much more comfortable sending a screenshot to the teacher by email or showing it after class. With classmates I share if I trust them and if it is not a graded competition.

In the group project I mentioned earlier, sharing early actually backfired, because the model became something to argue about instead of something to improve. So I prefer individual work or very small pairs. If there were a way to get quick private feedback without public exposure, I would probably share much earlier.

## Part 2 — Cross-family experience, group work, AI, tools and domains

**Interviewer:** You mentioned UML and ER diagrams. What carried over between them, and what felt like starting over?

**Participant:** Entities and classes are similar enough that I did not feel completely lost. Relationships also feel familiar. What changes is the purpose. In ER diagrams I think about tables and keys. In UML class diagrams I think more about responsibilities and behaviour. The drawing may look similar, but the questions behind it are different.

Sequence diagrams felt much more different. There I had to think about time and messages, not only structure. That was the biggest jump for me.

**Interviewer:** In group projects, who actually built and owned the model?

**Participant:** In the online shop project, I owned the model in practice, but without authority. Everyone else owned the code. That is a bad split. In a later individual assignment for Systems Analysis, the topic was a library system with reservations for rare books, and it worked much better because I owned the whole design. The model guided the implementation instead of being ignored.

For me, modelling works when someone really owns the design and when the domain is interesting enough to care about precision. Group work can make me avoid modelling because it becomes negotiation instead of thinking.

**Interviewer:** Have you used ChatGPT, Copilot, or something similar to create, explain, or check a model?

**Participant:** I used ChatGPT to explain sequence diagrams when I was stuck on a thesis diagram. I pasted the problem description and my draft and asked what was confusing in the message flow. That was useful because it answered in plain language. I also asked it once to suggest candidate classes from a text, but the answer was too generic, so I did not use it directly.

I would not want it to generate the final model for graded work, because then I would not understand the choices. But as an explainer, something like “what does this diagram actually say?”, it is useful. I have not changed my exam preparation much because exams are still on paper and timed, but for the thesis I use it more like a tutor than a replacement.

**Interviewer:** How have modelling tools affected your experience?

**Participant:** In coursework we used Visual Paradigm in the lab and draw.io at home. Visual Paradigm felt heavy, but it was clearer for UML semantics. draw.io is faster, but it lets you draw invalid things. I made mistakes there that the official tool would probably have blocked. So I like quick tools for sketching, but for learning a notation I think some semantic support helps.

**Interviewer:** What kinds of domains make modelling feel meaningful or worth the effort?

**Participant:** Interesting domains make a big difference. The rare-book reservation assignment was motivating because the rules were subtle: reservations, cancellations, priority members. I wanted the model to be good because the domain felt worth understanding. In my thesis, I care that the architecture diagram is readable because the application matters to me.

Generic shop or football examples drain me. I will still do the work, but I do not invest as much in polishing the model. So motivation affects how much time I spend refining the model, not whether I understand the notation.

**Interviewer:** Have you modelled for someone who would analyse or use the diagram, such as a supervisor or client?

**Participant:** Yes, my thesis supervisor. Knowing that she would read the diagrams changed how I drew them. I separated components more clearly and avoided clever abbreviations. I also wrote short captions explaining what question each diagram answers. That was not strictly required, but it made the model feel like communication, not just an academic exercise.

**Interviewer:** Have you used modelling in an internship or job?

**Participant:** Only in university so far. I had a short internship, but the team used informal whiteboard sketches, not UML. That surprised me because, from class, I had assumed modelling would be more standard. In practice, the team cared more about the running prototype.

## Part 3 — Closing

**Interviewer:** If you could change one realistic thing about how modelling is taught, what would help you most?

**Participant:** Two things, if I can say two. First, more individual or pair tasks with genuinely interesting domains, not only generic business systems. Second, complete worked examples in the theory materials before labs: full examples with explanation of choices, not only partial slides. That would help shy students like me because I could prepare privately and then ask specific questions after class instead of exposing a half-formed model in front of everyone.

**Interviewer:** Is there anything important about learning modelling that I did not ask?

**Participant:** Maybe that modelling felt much better once I stopped treating it as a group negotiation task. For someone shy, the social format of the course matters as much as the notation.

**Interviewer:** Thank you. This was very helpful.

## quick-reference card 

```
S4-type participant
─────────────────────
Institution:  university in Wrocław (CS, year 4)
Modelling:    UML (SE, Analysis), ER (Databases), thesis diagrams
Personality:  shy; prefers private feedback; dislikes large group projects
Motivation:   high when domain is interesting (heritage, science, culture)
AI:           light tutor use, wary of generated submissions
Gap to probe: RE/BPMN, large-course feedback, executable models (if absent)
```
