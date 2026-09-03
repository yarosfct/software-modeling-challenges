---
case_id: S8
role: student
version: cleaned
timestamp_style: none  # none | start | range
---

# Interview S8 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was translated from Portuguese (see [[pt/S8_transcript_pt]]) and cleaned for readability and consistency with other cleaned student transcripts. Consent filler, repetitions, and interviewer filler were reduced where they did not affect meaning. Interviewer questions were tightened for clarity. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the Portuguese original and the audio.

## Part 1 — Background, modelling experience, quality and sharing

**Interviewer:** <!-- T002 -->
Can you briefly explain how software modelling relates to you — where you used it, in academic work and, if relevant, professionally?

**Participant:** <!-- T003 -->
As you already know, ISEL has a more practical, project-oriented approach compared with other universities. So I do not know whether my answers will be of much value to you, but I will try my best to be useful.

During the bachelor’s I feel they did not even explain the term software modelling very well. There was probably some course that mentioned it and explained it somehow, but either I did not pay attention or I have already forgotten. If I am not mistaken, my first interactions with software modelling were in Introduction to Information Systems, which is a second-year course — I only know that because I looked it up before the interview to remember a bit. In that course we had to do entity-relationship diagrams, conceptual, logical and physical models, and SQL. Then also on the SQL topic, in the Databases course, we had to do class diagrams, which I think also counts as software modelling.

That was it in the bachelor’s. A bit separately, I feel that my real first interaction with software modelling was in the bachelor’s project, where I had to develop a system and one of the requirements was to create a model of the system to help visualise and explain it. At that time I did not really know what software modelling was: which notations to use, which parts of my system had to be abstracted and modelled. I had the idea that I had to use UML, requirements engineering, and so on, because it was in the project requirements, but I had no idea how to use those notations. It was a funny learning experience, but I managed to get by because they were not very demanding on that point. And then finally in the master’s I did have a course where modelling was properly introduced and explained, even though it was not the main focus of the course, which was Software Engineering.

**Interviewer:** <!-- T004 -->
Was that Software Engineering course more practical or theoretical? Were there lectures explaining modelling concepts and practicals where you modelled from a system description?

**Participant:** <!-- T005 -->
Like a large part of the programme, it was more oriented to the practical side. In this case we had to do a large group project that was probably about 60 or 70 percent of the course, but we also had quite a lot of theory to learn. It was certainly one of the courses with a more balanced practice-to-theory ratio. I assume it was similar to the course you had at FCT, where it was not only modelling: we had concepts such as code smells, design patterns, unit tests, and so on.

I think there were modelling exercises, but it was little: the first classes, because after that we worked on the project in the practicals.

**Interviewer:** <!-- T006 -->
How were those exercises solved? Did you submit them, only practise, present them to the teacher, or wait for the teacher to solve them on the board?

**Participant:** <!-- T007 -->
I do not remember well, but I know the teacher solved them on the board. We did not submit anything. I think we only solved them for practice. I am not sure because it was some time ago, but I have the idea that the teacher started by solving a problem on the board, a large example, explained the concepts and the reasoning behind his decisions, and then we students had a list of similar exercises to do for practice. When we finished the exercises we could leave, but the teacher did not check, so if someone wanted to check whether their solution was correct they had to go to the teacher in person, which in a way was rare. And this applied to almost every topic in that course.

**Interviewer:** <!-- T008 -->
Why do you think students did not go and check their solutions with the teacher? Shyness? Was it hard to talk to him? Did you go yourself?

**Participant:** <!-- T009 -->
Personally I do not think it was shyness. I think it was more a matter of lack of interest or laziness. Those exercises did not count towards the grade. The practical part was worth more than the theoretical part, and I am not sure I remember correctly, but I think the teacher made the solutions available afterwards, or someone did that in the course group.

I personally did go a few times to correct my models and exercises, because at first I found the topic interesting since I had already used it in the project. I even went back and reviewed the models I had made for the project after I became more familiar with those concepts, which was interesting because I found several small defects and errors in the syntax and in the notations.

**Interviewer:** <!-- T010 -->
During those class exercises, what did you do in the first ten minutes after you analysed the system description?

**Participant:** <!-- T011 -->
Because I was already somewhat familiar with creating models, even if they were not completely correct, I simply underlined in the text the details or requirements of the system. If it was something more complex I even created a list in the corner of the page to guide me, and I started by sketching the model in pencil in a simple way, for example only the names of the classes or actors, arrows or relations. Then when I felt it was at an acceptable level I started pressing harder with the pencil, and finally, after reviewing, reinforcing, and confirming that all the requirements were satisfied and I was happy with the model in general, I went over everything in pen and erased the pencil.

**Interviewer:** <!-- T012 -->
When the teacher solved an exercise or demonstrated a solution from a description, what did that actually help you with — notation, reasoning, or the expected answer? Could you transfer that to similar tasks?

**Participant:** <!-- T013 -->
It was certainly the notation and the explanation of using that notation. The reasoning as well, in a way, but that part was more intuitive for me. The expected answer not so much, because we had the solved exercises at the end. Obviously it helped me transfer to similar tasks.

**Interviewer:** <!-- T014 -->
How did you decide whether a model was good enough? Did you have a checklist, compare with classmates or examples, or a tool that “compiled” models?

**Participant:** <!-- T015 -->
Honestly I did not worry much about that. I made sure all the requirements were satisfied. If the model seemed incomplete or too simple, I was a bit suspicious, and if I was very suspicious I compared with other classmates or even asked the teacher. As for tools, we used some but they were not mandatory. I remember Camunda, Archi, and I think there was still another one, but I ended up not using any of those, only draw.io.

## Part 2 — Project feedback, sharing, notation switching, workload and AI

**Interviewer:** <!-- T016 -->
Did you do group work in that course? Were there phases, for example first requirements, then the model?

**Participant:** <!-- T017 -->
No, it was all individual. It was 60 percent project and 40 percent report, and then there was a discussion. It was not phased. It was continuous development.

**Interviewer:** <!-- T018 -->
How did feedback work? Did you have to go and talk to the teacher throughout the project? Did feedback ever imply changes, or even completely redoing the model?

**Participant:** <!-- T019 -->
Yes, we went along showing what we had done throughout the project. Or rather, it was more the teacher who went around checking and giving tips and feedback. If a doubt came up we had to be the ones to go and interact with the teacher.

Completely redoing the model, that I remember, no. But the teacher’s feedback almost always implied changes, large or small. Of course there was also positive feedback in the sense that the model was good and did not need changes, but that was rarer.

**Interviewer:** <!-- T020 -->
In class, when you solved exercises, did students go to the board or show solutions to the class? If you solved an exercise beyond the teacher’s example, how comfortable did you feel showing your solution to other people?

**Participant:** <!-- T021 -->
No. We only solved the exercises, and if we had doubts we could ask the teacher. I do not think there was any case of solving exercises on the board.

It depends a bit. I was never someone who interacted in the course WhatsApp group, and there I feel that several students showed and discussed their solutions. I do not remember whether this was the case in Software Engineering, but it was common. For example I might interact in that group if I knew I had the wrong answer and wanted someone to show me the correct one, but if someone asked for the solution to exercise x and I happened to have it, I hesitated a bit. I waited for someone else to reply. But in my small group of friends, about five classmates, I had no problem at all.

To summarise: generally I have no problem showing my solutions to people close to me, but with strangers I hesitate a bit, more because of a social factor than lack of confidence in my solution. Additionally, when I went to the teacher, even if I was not sure of my answer or solution, I went without a problem, because I am there to learn.

**Interviewer:** <!-- T022 -->
Did you have difficulty switching families or notations, for example from UML to BPMN or to requirements engineering?

**Participant:** <!-- T023 -->
BPMN I am not sure I had. Requirements engineering is not unfamiliar, but I do not remember well. I do remember getting a bit stuck when switching notations, especially when they were similar. I remember that those requirements diagrams looked similar to class diagrams and had similar relations as well. That confused me a bit, but with an example beside me it was fine.

**Interviewer:** <!-- T024 -->
Once you knew one notation, was moving to another easier or harder?

**Participant:** <!-- T025 -->
It was easier. In the end it was almost all the same: I had to abstract a part of the system using a specific notation. So I would say going from something like class diagrams to requirements was easy, as was going from use cases to activity or sequence. I do not remember well now, but those ones where you had an actor and a timeline were easier. Basically, knowing one type of notation made it easier to learn others.

And being honest, it is not that I hated it, but for me those were drawings to explain things. You know when you try to explain something to someone and you joke that you need them to make a drawing? It was like that. That is to say, I gave more importance to the code, so to speak, which felt more tangible, so I did not care much if the models were not perfect, as long as they were there.

**Interviewer:** <!-- T026 -->
What about workload? Did other courses compete with that one, in the sense that you would not dedicate yourself 100 percent to it?

**Participant:** <!-- T027 -->
Other courses, I cannot say. Being honest I do not remember at all which courses I had at the same time. But at that time, in my first year of the master’s, I had started working as a tutor, which certainly affected my interest in that topic. As I said, I do not hate modelling and I even had interest because I had already used it in the bachelor’s project, and it was not very complicated, but starting to work and receiving some money definitely affected my interest in the course and even in the programme in general, I would say.

**Interviewer:** <!-- T028 -->
Did you catch AI at that time, and if so did it help in any way?

**Participant:** <!-- T029 -->
This was about four years ago I think, so yes I caught it, but I do not remember having used AI in that course at least. I feel that for that kind of work AI at the time was not much help. There probably was no image analysis, or it was very weak, and to help with models I feel that feature is essential.

## Part 3 — Closing

**Interviewer:** <!-- T030 -->
If you could make one realistic change to how software modelling is taught, at ISEL or in general, what would it be?

**Participant:** <!-- T031 -->
This is difficult. Let me think a bit. Well, to start with, even today I do not see much utility in software modelling, and it may be a bit controversial, but I think it will die in the next few years with AI. Vibe coding is the new trend, and I do not see anyone explaining systems using modelling. So I think they should really start there: explain better to students the utility of modelling, how it can be applied in the professional world, what the benefits of models are, comparisons with systems that do not have models, things like that. Something that would motivate students to model their systems when they start their personal projects, for example.

**Interviewer:** <!-- T032 -->
Thank you. This was very helpful.
