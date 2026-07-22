---
case_id: S1
role: student
version: cleaned
timestamp_style: start  # none | start | range
---

# Interview S1 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was cleaned against the audio with user-verified corrections. Mixed-speaker segments were separated, and repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and modelling experience

**Interviewer [00:02]:** <!-- T001 -->
Can you tell me about your studies and where modelling fits, including which courses involved modelling?

**Participant [00:18]:** <!-- T002 -->
The only time I did serious, quote-unquote, modelling was in the Software Engineering course in the third year of my Computer Science bachelor's degree.

**Interviewer [00:38]:** <!-- T003 -->
What was the purpose of modelling in that course?

**Participant [00:54]:** <!-- T004 -->
I mostly remember the final project, where we had to make a bunch of UML diagrams. Some were entity-relationship diagrams, I think, for FreeCol, the game we were implementing features on top of. The point was to understand the different system interactions and how what we wanted to do fitted into that system.

**Interviewer [01:29]:** <!-- T005 -->
Have you used modelling outside courses?

**Participant [01:49]:** <!-- T006 -->
The closest example is my dissertation. We defined the whole system architecture, and it is much easier to work out what to do about which component and how they all fit together when it is properly modelled with a relational diagram showing how each component relates to and overlaps with the others.

## Meaning and usefulness of modelling

**Interviewer [02:20]:** <!-- T007 -->
When you hear software or conceptual modelling, what first comes to mind?

**Participant [02:41]:** <!-- T008 -->
A bit of both diagrams and extra documentation. I think of UML diagrams, entity relationships, activity diagrams, and development models such as spiral, agile, and incremental. Modelling is useful for defining how system components interact up to a certain point. After that, it can feel arbitrary and like extra documentation.

**Interviewer [03:19]:** <!-- T009 -->
How would you explain modelling to a colleague?

**Participant [03:49]:** <!-- T010 -->
It bridges implementation and communication in software engineering. You need to transmit the system concept in an easily readable way without so much fine detail that people who are not implementing it would not understand.

**Interviewer [04:13]:** <!-- T011 -->
So communication and abstraction are important. Can you remember a moment when modelling was particularly useful?

**Participant [04:44]:** <!-- T012 -->
I work in embedded systems, where many components and interactions depend tightly on one another. A diagram helps work out those interactions at a higher level without going into fine details. It guides development before I start changing the internals.

**Interviewer [05:18]:** <!-- T013 -->
Did it improve your understanding of the system?

**Participant [05:27]:** <!-- T014 -->
Yes. It clarifies where everything fits.

**Interviewer [05:30]:** <!-- T015 -->
Did it affect your motivation or confidence?

**Participant [05:40]:** <!-- T016 -->
In a way. It is hard to work out all the moving parts if you dive directly into implementation without planning or making a diagram. A diagram helps establish the baseline priorities and then build on top of them.

## Difficult and frustrating experiences

**Interviewer [06:08]:** <!-- T017 -->
Can you remember a moment when modelling felt confusing, pointless, or frustrating?

**Participant [06:23]:** <!-- T018 -->
The most confusing example was during the FreeCol project, where we had to model player-environment or NPC interactions. Different arrows and boxes meant different things. There was a lot of information to absorb, and it felt arbitrary when trying to do something useful with it.

**Interviewer [06:58]:** <!-- T019 -->
Was the difficulty caused by notation, tools, task ambiguity, group work, or time pressure?

**Participant [07:21]:** <!-- T020 -->
A combination. The tool had so many options that it became completely overwhelming to know how to make a simple entity-to-box relation. That was very frustrating.

I put the teamwork issues more in the category of Agile and Scrum development.

**Interviewer [07:48]:** <!-- T021 -->
What did you dislike about that process?

**Participant [07:55]:** <!-- T022 -->
The enforcement of sprints, tasks, and similar structures felt arbitrary and like an extra step before implementation. It was a large project with six people, and half did not contribute much. Task delegation became frustrating because work remained in the backlog when someone could have taken one large task and completed it.

I understand the purpose, and it can be useful when people cooperate properly.

**Interviewer [08:41]:** <!-- T023 -->
So group work was negative in this case, although it can support communication and soft-skill development?

**Participant [08:55]:**
Yes.

**Interviewer [08:57]:** <!-- T024 -->
What did you do when you encountered those frustrations?

**Participant [09:31]:** <!-- T025 -->
After that, I mostly avoided modelling. Since work had to be done, I got on with it. In that case, assigning tasks to those people was not going anywhere, so the group members who were working had to pick up the work. It became less a modelling effort and more, "We have to get this done."

**Interviewer [10:00]:** <!-- T026 -->
What would have helped in that situation?

**Participant [10:22]:** <!-- T027 -->
A different or smaller group would have helped. Too many people dilute the pressure, whereas in a smaller team everyone knows they must contribute.

Modelling could also have helped because everyone would have had a clear picture of their role in the larger project. More teacher communication might also have helped us handle team members who were not contributing.

## Learning process and representational decisions

**Interviewer [11:02]:** <!-- T028 -->
When learning a new notation or framework such as UML, what was hardest at the beginning?

**Participant [11:45]:** <!-- T029 -->
The high-level concepts were fairly straightforward, but the symbols and notation complicated things. There were many options, so it quickly became overwhelming and created doubt: "Is this the proper notation for this? Is this the proper arrow for that?" That made it harder to begin.

**Interviewer [12:13]:** <!-- T030 -->
How do you approach creating a model from a textual description?

**Participant [12:37]:** <!-- T031 -->
It is a back-and-forth process. I read the description, make an incorrect model, then look at the model and understand why it is incorrect based on the text. I go back and forth until the model agrees with my understanding of the text. It is trial and error, but I do not have much experience with that in particular.

**Interviewer [13:10]:** <!-- T032 -->
Do you have a structured starting approach?

**Participant [13:36]:** <!-- T033 -->
I start with the components that actors interact with, and then place the actors. It is easier for me to think about the system first and then the actors.

**Interviewer [13:56]:** <!-- T034 -->
Did teachers explicitly teach a step-by-step process?

**Participant [14:20]:** <!-- T035 -->
I honestly cannot remember. My impression is that it was more, "Here are the concepts. Here is the text. Get to it." But I cannot say for sure or remember the details.

**Interviewer [14:35]:** <!-- T036 -->
How do you decide what to include or omit?

**Participant [15:16]:** <!-- T037 -->
If something is on the critical or hot path of what I am trying to do, I include it. I am comfortable ignoring side effects that do not affect the outcome if including them would add confusion to the diagram.

**Interviewer [15:39]:** <!-- T038 -->
So you prioritise readability over including every real-world detail?

**Participant [16:10]:** <!-- T039 -->
Yes. A model is a communication tool. If it contains so much that it becomes overwhelming, it defeats its own purpose.

## Model quality and self-evaluation

**Interviewer [16:22]:** <!-- T040 -->
How do you decide whether a finished model is good enough?

**Participant [17:03]:** <!-- T041 -->
I look for readability, correctness, and whether it matches the requirements. I walk through the diagram to see whether every component makes sense. Readability is a major part.

**Interviewer [17:19]:** <!-- T042 -->
Did the course provide quality rules or checklists?

**Participant [17:42]:** <!-- T043 -->
There must have been some guideline or system for validating models, but I cannot remember it. It is not present in my mind now.

**Interviewer [18:02]:** <!-- T044 -->
Do you compare your models with other models?

**Participant [18:17]:** <!-- T045 -->
Yes, for sure.

**Interviewer [18:20]:** <!-- T046 -->
What do you look for in those comparisons?

**Participant [18:27]:** <!-- T047 -->
For my dissertation, I looked at architecture diagrams in other dissertations. I look for clarity. If their architecture and system are clear to me, I try to emulate that presentation so my diagram is clear to an outsider who does not yet know how the system works.

## Tools and modelling experience

**Interviewer [19:06]:** <!-- T048 -->
Which modelling tools did you use?

**Participant [19:58]:** <!-- T049 -->
I used StarUML. It had a bajillion options, which was confusing. Later, I discovered draw.io. For basic diagrams, draw.io is more useful to me because I am not deeply involved in software engineering. Having fewer things available makes it easier to work without being overwhelmed by the options.

**Interviewer [20:33]:** <!-- T050 -->
Was StarUML's main issue an overwhelming interface?

**Participant [21:12]:** <!-- T051 -->
Yes, it was way too much all at once.

**Interviewer [21:16]:** <!-- T052 -->
Did tools make modelling harder or easier?

**Participant [21:26]:** <!-- T053 -->
StarUML made it harder, while draw.io made it easier. It depends on how the tool is implemented.

**Interviewer [21:35]:** <!-- T054 -->
So tool design can improve the modelling experience?

**Participant [21:50]:** <!-- T055 -->
Yes, absolutely.

## Domain, authenticity, and motivation

**Interviewer [21:52]:** <!-- T056 -->
Can you describe the FreeCol project?

**Participant [22:03]:** <!-- T057 -->
FreeCol was an open-source, Civilization-like game. We examined the codebase for code smells and antipatterns, then extended the game with features we designed. The modelling part explained how our features would work with the existing game systems.

**Interviewer [22:33]:** <!-- T058 -->
Was the game domain interesting and motivating?

**Participant [22:55]:** <!-- T059 -->
Yes, because I like video games. Even if it had not been a game, immediately seeing my impact on the application would have made it more motivating. It encouraged me to create something that integrated well because it affected my experience of the application.

**Interviewer [23:18]:** <!-- T060 -->
Did working with a real, longstanding open-source project improve the experience?

**Participant [23:56]:** <!-- T061 -->
Absolutely. Many people had contributed to it over the years, which made it interesting to explore how different people approached problems and how my work could fit into the project. It was a lot of fun.

**Interviewer [24:22]:** <!-- T062 -->
Does choosing a personally interesting domain affect your motivation and effort?

**Participant [24:56]:** <!-- T063 -->
Absolutely. If it is something I am interested in, I go out of my way to make it good and make it stand out. That motivates me to create proper diagrams and explanations because I want them to be understandable not only to me, but communicable to outsiders.

## Feedback

**Interviewer [25:21]:** <!-- T064 -->
How did you receive feedback on modelling work?

**Participant [25:43]:** <!-- T065 -->
We had a large project discussion at the end. We reviewed what everyone had done and discussed the diagrams and what was wrong with them. It was not just a grade or an automatic tool validation.

**Interviewer [26:03]:** <!-- T066 -->
Was that teacher feedback provided only at the end?

**Participant [26:14]:** <!-- T067 -->
Yes, if I remember correctly.

**Interviewer [26:15]:** <!-- T068 -->
Would earlier or iterative feedback have improved the diagrams?

**Participant [26:30]:** <!-- T069 -->
Yes. Problems could have been addressed along the way instead of propagating until the end and becoming, "This is completely wrong. Why would you do that?"

**Interviewer [26:48]:** <!-- T070 -->
What kind of feedback would have helped most?

**Participant [27:03]:** <!-- T071 -->
Examples are more useful for me because I learn by seeing things. For example: "This textual description translates to this model." That would help me make the mental connection between a requested relation and how it is represented in a diagram.

**Interviewer [27:31]:** <!-- T072 -->
Would templates for common modelling steps or processes help?

**Participant [27:48]:** <!-- T073 -->
Yes, I think so.

## Modelling competence and soft skills

**Interviewer [27:50]:** <!-- T074 -->
What should a good modeller be able to do?

**Participant [28:06]:** <!-- T075 -->
A good modeller should represent complex systems in a way that makes them visually less complex.

**Interviewer [28:18]:** <!-- T076 -->
Abstraction and communication?

**Participant [28:20]:** <!-- T077 -->
Yes, abstraction and communicating ideas better.

**Interviewer [28:25]:** <!-- T078 -->
Clarity?

**Participant [28:36]:** <!-- T079 -->
Yes, clarity is part of it.

**Interviewer [28:39]:** <!-- T080 -->
What about checking, asking good questions, and iteration, or is it mostly abstraction?

**Participant [28:45]:** <!-- T081 -->
I do not think a lot of abstraction is necessary. It should be just enough to make the system we are trying to convey clear and consistent. That makes a good model.

**Interviewer [29:00]:** <!-- T082 -->
Do soft skills such as communication, negotiation, and teamwork matter?

**Participant [29:10]:** <!-- T083 -->
There is probably a balance of both technical and soft skills. Someone with good soft skills probably understands how to communicate ideas better, and that translates into how they represent those ideas.

**Interviewer [29:25]:** <!-- T084 -->
Did the Software Engineering course help develop those skills?

**Participant [29:50]:** <!-- T085 -->
The group was not very good, but the teamwork aspect developed. I would not call it leadership, but somebody had to shift tasks around because half the team had to pick up the other half's work. Negotiation also helped because we had to determine what each person needed to do.

## Desired teaching changes

**Interviewer [30:32]:** <!-- T086 -->
What would you change about how modelling is taught?

**Participant [31:04]:** <!-- T087 -->
I would use a more incremental approach to diagrams. For example: "Here is a small system with these relationships; let us model it. Here is a different system with different relationships; let us model that." Then we could put everything together. That might demystify modelling.

**Interviewer [31:28]:** <!-- T088 -->
Would separate small systems be better, or should the same system evolve incrementally?

**Participant [31:48]:** <!-- T089 -->
Maybe evolving the same system would preserve context: "The system is evolving in this way." I think that would be useful.

**Interviewer [32:02]:** <!-- T090 -->
Any additional remarks about feedback, assignments, or exams?

**Participant [32:20]:** <!-- T091 -->
Not really. It is difficult to remember what we did.

## Closing

**Interviewer [32:30]:** <!-- T092 -->
Is there anything else important about learning or using modelling?

**Participant [33:00]:** <!-- T093 -->
I do not think so. It is difficult for me to grasp because I am not deeply involved in this domain, but based on what I know about system modelling and software engineering, I think we covered everything I know.
