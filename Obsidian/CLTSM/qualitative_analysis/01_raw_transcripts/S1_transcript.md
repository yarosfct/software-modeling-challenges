# S1 Cleaned Interview Transcript

`I = Interviewer`  
`S1 = Student participant`

This transcript was cleaned against the audio with user-verified corrections. Mixed-speaker segments were separated, and repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and modelling experience

**I [00:02]:** Can you tell me about your studies and where modelling fits, including which courses involved modelling?

**S1 [00:18]:** The only time I did serious, quote-unquote, modelling was in the Software Engineering course in the third year of my Computer Science bachelor's degree.

**I [00:38]:** What was the purpose of modelling in that course?

**S1 [00:54]:** I mostly remember the final project, where we had to make a bunch of UML diagrams. Some were entity-relationship diagrams, I think, for FreeCol, the game we were implementing features on top of. The point was to understand the different system interactions and how what we wanted to do fitted into that system.

**I [01:29]:** Have you used modelling outside courses?

**S1 [01:49]:** The closest example is my dissertation. We defined the whole system architecture, and it is much easier to work out what to do about which component and how they all fit together when it is properly modelled with a relational diagram showing how each component relates to and overlaps with the others.

## Meaning and usefulness of modelling

**I [02:20]:** When you hear software or conceptual modelling, what first comes to mind?

**S1 [02:41]:** A bit of both diagrams and extra documentation. I think of UML diagrams, entity relationships, activity diagrams, and development models such as spiral, agile, and incremental. Modelling is useful for defining how system components interact up to a certain point. After that, it can feel arbitrary and like extra documentation.

**I [03:19]:** How would you explain modelling to a colleague?

**S1 [03:49]:** It bridges implementation and communication in software engineering. You need to transmit the system concept in an easily readable way without so much fine detail that people who are not implementing it would not understand.

**I [04:13]:** So communication and abstraction are important. Can you remember a moment when modelling was particularly useful?

**S1 [04:44]:** I work in embedded systems, where many components and interactions depend tightly on one another. A diagram helps work out those interactions at a higher level without going into fine details. It guides development before I start changing the internals.

**I [05:18]:** Did it improve your understanding of the system?

**S1 [05:27]:** Yes. It clarifies where everything fits.

**I [05:30]:** Did it affect your motivation or confidence?

**S1 [05:40]:** In a way. It is hard to work out all the moving parts if you dive directly into implementation without planning or making a diagram. A diagram helps establish the baseline priorities and then build on top of them.

## Difficult and frustrating experiences

**I [06:08]:** Can you remember a moment when modelling felt confusing, pointless, or frustrating?

**S1 [06:23]:** The most confusing example was during the FreeCol project, where we had to model player-environment or NPC interactions. Different arrows and boxes meant different things. There was a lot of information to absorb, and it felt arbitrary when trying to do something useful with it.

**I [06:58]:** Was the difficulty caused by notation, tools, task ambiguity, group work, or time pressure?

**S1 [07:21]:** A combination. The tool had so many options that it became completely overwhelming to know how to make a simple entity-to-box relation. That was very frustrating.

I put the teamwork issues more in the category of Agile and Scrum development.

**I [07:48]:** What did you dislike about that process?

**S1 [07:55]:** The enforcement of sprints, tasks, and similar structures felt arbitrary and like an extra step before implementation. It was a large project with six people, and half did not contribute much. Task delegation became frustrating because work remained in the backlog when someone could have taken one large task and completed it.

I understand the purpose, and it can be useful when people cooperate properly.

**I [08:41]:** So group work was negative in this case, although it can support communication and soft-skill development?

**S1 [08:55]:** Yes.

**I [08:57]:** What did you do when you encountered those frustrations?

**S1 [09:31]:** After that, I mostly avoided modelling. Since work had to be done, I got on with it. In that case, assigning tasks to those people was not going anywhere, so the group members who were working had to pick up the work. It became less a modelling effort and more, "We have to get this done."

**I [10:00]:** What would have helped in that situation?

**S1 [10:22]:** A different or smaller group would have helped. Too many people dilute the pressure, whereas in a smaller team everyone knows they must contribute.

Modelling could also have helped because everyone would have had a clear picture of their role in the larger project. More teacher communication might also have helped us handle team members who were not contributing.

## Learning process and representational decisions

**I [11:02]:** When learning a new notation or framework such as UML, what was hardest at the beginning?

**S1 [11:45]:** The high-level concepts were fairly straightforward, but the symbols and notation complicated things. There were many options, so it quickly became overwhelming and created doubt: "Is this the proper notation for this? Is this the proper arrow for that?" That made it harder to begin.

**I [12:13]:** How do you approach creating a model from a textual description?

**S1 [12:37]:** It is a back-and-forth process. I read the description, make an incorrect model, then look at the model and understand why it is incorrect based on the text. I go back and forth until the model agrees with my understanding of the text. It is trial and error, but I do not have much experience with that in particular.

**I [13:10]:** Do you have a structured starting approach?

**S1 [13:36]:** I start with the components that actors interact with, and then place the actors. It is easier for me to think about the system first and then the actors.

**I [13:56]:** Did teachers explicitly teach a step-by-step process?

**S1 [14:20]:** I honestly cannot remember. My impression is that it was more, "Here are the concepts. Here is the text. Get to it." But I cannot say for sure or remember the details.

**I [14:35]:** How do you decide what to include or omit?

**S1 [15:16]:** If something is on the critical or hot path of what I am trying to do, I include it. I am comfortable ignoring side effects that do not affect the outcome if including them would add confusion to the diagram.

**I [15:39]:** So you prioritise readability over including every real-world detail?

**S1 [16:10]:** Yes. A model is a communication tool. If it contains so much that it becomes overwhelming, it defeats its own purpose.

## Model quality and self-evaluation

**I [16:22]:** How do you decide whether a finished model is good enough?

**S1 [17:03]:** I look for readability, correctness, and whether it matches the requirements. I walk through the diagram to see whether every component makes sense. Readability is a major part.

**I [17:19]:** Did the course provide quality rules or checklists?

**S1 [17:42]:** There must have been some guideline or system for validating models, but I cannot remember it. It is not present in my mind now.

**I [18:02]:** Do you compare your models with other models?

**S1 [18:17]:** Yes, for sure.

**I [18:20]:** What do you look for in those comparisons?

**S1 [18:27]:** For my dissertation, I looked at architecture diagrams in other dissertations. I look for clarity. If their architecture and system are clear to me, I try to emulate that presentation so my diagram is clear to an outsider who does not yet know how the system works.

## Tools and modelling experience

**I [19:06]:** Which modelling tools did you use?

**S1 [19:58]:** I used StarUML. It had a bajillion options, which was confusing. Later, I discovered draw.io. For basic diagrams, draw.io is more useful to me because I am not deeply involved in software engineering. Having fewer things available makes it easier to work without being overwhelmed by the options.

**I [20:33]:** Was StarUML's main issue an overwhelming interface?

**S1 [21:12]:** Yes, it was way too much all at once.

**I [21:16]:** Did tools make modelling harder or easier?

**S1 [21:26]:** StarUML made it harder, while draw.io made it easier. It depends on how the tool is implemented.

**I [21:35]:** So tool design can improve the modelling experience?

**S1 [21:50]:** Yes, absolutely.

## Domain, authenticity, and motivation

**I [21:52]:** Can you describe the FreeCol project?

**S1 [22:03]:** FreeCol was an open-source, Civilization-like game. We examined the codebase for code smells and antipatterns, then extended the game with features we designed. The modelling part explained how our features would work with the existing game systems.

**I [22:33]:** Was the game domain interesting and motivating?

**S1 [22:55]:** Yes, because I like video games. Even if it had not been a game, immediately seeing my impact on the application would have made it more motivating. It encouraged me to create something that integrated well because it affected my experience of the application.

**I [23:18]:** Did working with a real, longstanding open-source project improve the experience?

**S1 [23:56]:** Absolutely. Many people had contributed to it over the years, which made it interesting to explore how different people approached problems and how my work could fit into the project. It was a lot of fun.

**I [24:22]:** Does choosing a personally interesting domain affect your motivation and effort?

**S1 [24:56]:** Absolutely. If it is something I am interested in, I go out of my way to make it good and make it stand out. That motivates me to create proper diagrams and explanations because I want them to be understandable not only to me, but communicable to outsiders.

## Feedback

**I [25:21]:** How did you receive feedback on modelling work?

**S1 [25:43]:** We had a large project discussion at the end. We reviewed what everyone had done and discussed the diagrams and what was wrong with them. It was not just a grade or an automatic tool validation.

**I [26:03]:** Was that teacher feedback provided only at the end?

**S1 [26:14]:** Yes, if I remember correctly.

**I [26:15]:** Would earlier or iterative feedback have improved the diagrams?

**S1 [26:30]:** Yes. Problems could have been addressed along the way instead of propagating until the end and becoming, "This is completely wrong. Why would you do that?"

**I [26:48]:** What kind of feedback would have helped most?

**S1 [27:03]:** Examples are more useful for me because I learn by seeing things. For example: "This textual description translates to this model." That would help me make the mental connection between a requested relation and how it is represented in a diagram.

**I [27:31]:** Would templates for common modelling steps or processes help?

**S1 [27:48]:** Yes, I think so.

## Modelling competence and soft skills

**I [27:50]:** What should a good modeller be able to do?

**S1 [28:06]:** A good modeller should represent complex systems in a way that makes them visually less complex.

**I [28:18]:** Abstraction and communication?

**S1 [28:20]:** Yes, abstraction and communicating ideas better.

**I [28:25]:** Clarity?

**S1 [28:36]:** Yes, clarity is part of it.

**I [28:39]:** What about checking, asking good questions, and iteration, or is it mostly abstraction?

**S1 [28:45]:** I do not think a lot of abstraction is necessary. It should be just enough to make the system we are trying to convey clear and consistent. That makes a good model.

**I [29:00]:** Do soft skills such as communication, negotiation, and teamwork matter?

**S1 [29:10]:** There is probably a balance of both technical and soft skills. Someone with good soft skills probably understands how to communicate ideas better, and that translates into how they represent those ideas.

**I [29:25]:** Did the Software Engineering course help develop those skills?

**S1 [29:50]:** The group was not very good, but the teamwork aspect developed. I would not call it leadership, but somebody had to shift tasks around because half the team had to pick up the other half's work. Negotiation also helped because we had to determine what each person needed to do.

## Desired teaching changes

**I [30:32]:** What would you change about how modelling is taught?

**S1 [31:04]:** I would use a more incremental approach to diagrams. For example: "Here is a small system with these relationships; let us model it. Here is a different system with different relationships; let us model that." Then we could put everything together. That might demystify modelling.

**I [31:28]:** Would separate small systems be better, or should the same system evolve incrementally?

**S1 [31:48]:** Maybe evolving the same system would preserve context: "The system is evolving in this way." I think that would be useful.

**I [32:02]:** Any additional remarks about feedback, assignments, or exams?

**S1 [32:20]:** Not really. It is difficult to remember what we did.

## Closing

**I [32:30]:** Is there anything else important about learning or using modelling?

**S1 [33:00]:** I do not think so. It is difficult for me to grasp because I am not deeply involved in this domain, but based on what I know about system modelling and software engineering, I think we covered everything I know.
