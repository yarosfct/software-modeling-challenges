---
case_id: S2
role: student
version: cleaned
timestamp_style: start  # none | start | range
---

# Interview S2 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was cleaned against the audio-derived SRT. Incorrect speaker labels and mixed-speaker segments were corrected. Repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and modelling experience

**Interviewer [00:00]:** <!-- T001 -->
Can you tell me about your studies and where modelling fits, including which courses involved modelling?

**Participant [00:14]:** <!-- T002 -->
I used modelling officially in the Software Engineering course, and more unofficially in my job and dissertation. When I need to demonstrate what a system does, I do some modelling, not necessarily using a particular framework or tool.

**Interviewer [00:35]:** <!-- T003 -->
What was the purpose of modelling in the course, dissertation, and work contexts?

**Participant [00:56]:** <!-- T004 -->
In the course, we used it for a video game. We had to model some processes and actions that characters could take.

For my dissertation, I am modelling a data-mining tool. The point is to show readers who do not know it how it works in an easy, visual way.

At work, I use modelling because the system we are building has grown quite big and complex. It helps us, but also the people we work with who are not directly working on it, understand what we are doing, the design, and why we make certain decisions.

**Interviewer [01:55]:** <!-- T005 -->
Which modelling frameworks or notations did you use in the course?

**Participant [02:08]:** <!-- T006 -->
UML was the main one. I do not remember whether we used another framework, but I remember UML clearly.

**Interviewer [02:24]:** <!-- T007 -->
How long ago was that course?

**Participant [02:24]:** <!-- T008 -->
Two years ago.

## Meaning and usefulness of modelling

**Interviewer [02:31]:** <!-- T009 -->
When you hear software or conceptual modelling, what first comes to mind?

**Participant [02:48]:** <!-- T010 -->
Abstraction, absolutely.

**Interviewer [02:54]:** <!-- T011 -->
How would you explain modelling to a colleague?

**Participant [02:59]:** <!-- T012 -->
It is a way to visually abstract complex systems and processes so that people who may not understand much about them can get a good grasp just by looking at a diagram.

**Interviewer [03:19]:** <!-- T013 -->
Do you see modelling as useful, extra documentation, a communication tool, or something else?

**Participant [03:32]:** <!-- T014 -->
Modelling is very useful, even when you are working alone. Some concepts may be really complex and you cannot fit them in your mind. Making a small diagram can simplify them for you and for others who want to understand your work.

**Interviewer [03:50]:** <!-- T015 -->
Can you remember a moment when modelling was particularly useful?

**Participant [04:02]:** <!-- T016 -->
In my dissertation, I started with one approach to my data-mining tool and later switched to another. To explain that change to readers, I made diagrams showing how the old and new versions worked. They visually demonstrated why one approach was much simpler than the other, which would have been harder to explain through words.

**Interviewer [04:32]:** <!-- T017 -->
Did modelling improve your understanding and communication of the system?

**Participant [04:48]:** <!-- T018 -->
Yes, for sure.

**Interviewer [04:48]:** <!-- T019 -->
Did it affect your motivation or confidence?

**Participant [04:59]:** <!-- T020 -->
It made the system feel simpler. I understood it before and after, but looking at it made it feel simpler and made me slightly more confident. It made a much bigger difference for the people reading it. I felt more confident that I could correctly portray my system.

**Interviewer [05:21]:** <!-- T021 -->
Did it motivate you to work further on the system?

**Participant [05:39]:** <!-- T022 -->
Not really. It was a means to an end and a good tool, but it did not fundamentally change how I work.

## Difficult and frustrating experiences

**Interviewer [05:44]:** <!-- T023 -->
Can you remember a moment when modelling felt confusing, pointless, or frustrating?

**Participant [05:54]:** <!-- T024 -->
Definitely in my Software Engineering course, because I had to use frameworks with which I was unfamiliar. I had to learn them before I could start drawing. I did not feel that as much at work or in my dissertation because I did not use a particular framework. I drew something that felt intuitive and good enough.

**Interviewer [06:19]:** <!-- T025 -->
Was the difficulty caused by the notation, framework, or tool?

**Participant [06:37]:** <!-- T026 -->
The tool itself was not a problem. I think I used draw.io, although I am not completely sure. It had many features that made drawing easy.

What was frustrating was fitting an abstraction into an existing system. The system already had rules that the abstraction had to follow. Creating something myself would have felt easier.

**Interviewer [07:05]:** <!-- T027 -->
Did task ambiguity, feedback, group work, or time pressure affect that frustration?

**Participant [07:24]:** <!-- T028 -->
It made it feel like a chore, but like any other task in the project. It was not more frustrating than everything else. It was just another thing to do.

**Interviewer [07:46]:** <!-- T029 -->
What did you do when you were uncertain?

**Participant [08:05]:** <!-- T030 -->
I used trial and error. I tried something and eventually finished it. Then I showed it to the professor and asked, "Does this look all right?" He said it was about right, and that was it.

**Interviewer [08:21]:** <!-- T031 -->
If you replayed that situation, what would have helped?

**Participant [08:37]:** <!-- T032 -->
I cannot identify anything specific. It had the same difficulty as learning anything else. It was simply something new that I had to learn.

**Interviewer [08:56]:** <!-- T033 -->
What about the size of the problem? FreeCol was a large open-source game.

**Participant [09:18]:** <!-- T034 -->
What made it less difficult was that we could choose what we wanted to model. Because I was a beginner, I chose something I felt I could model easily within those rules. If I had been told to model one specific part, it might have been a bigger challenge.

## Learning process and representational decisions

**Interviewer [09:44]:** <!-- T035 -->
What was the hardest part when learning a modelling notation or framework?

**Participant [10:11]:** <!-- T036 -->
The hardest part of modelling overall is representing relationships between objects. There is a lot of nuance that you may not be able to explain completely through an arrow or a line. Something may not be easily differentiable through line pipes.

**Interviewer [10:38]:** <!-- T037 -->
What did you do to make sense of those relationships?

**Participant [10:45]:** <!-- T038 -->
I looked at a completed model and what it described. I examined each relation: this person is connected to this object, and this relation means that. Then I applied the analogy to my project and selected the corresponding arrow. I wanted to see something similar that was already done and replicate the reasoning in my case.

**Interviewer [11:28]:** <!-- T039 -->
If you receive a textual system description and must build a model, what steps do you take?

**Participant [11:56]:** <!-- T040 -->
I would not say I have a plan, but I would not say I simply wing it. I have a way of thinking that I apply. I would start by drawing the objects, such as a person or a specific process, and then model the relationships between them. Starting with actors or classes feels simpler and more intuitive than starting with relationships.

**Interviewer [12:47]:** <!-- T041 -->
Is your approach structured or based on trial and error?

**Participant [12:52]:** <!-- T042 -->
It is more structured, although there is some trial and error. Once I interpret something in a particular way, I find it difficult to see it differently. If I initially identify something as a class or person, trial and error is unlikely to make me reinterpret it as something else.

**Interviewer [13:28]:** <!-- T043 -->
How do you decide what to include or omit?

**Participant [13:54]:** <!-- T044 -->
I do not have enough experience with that to have a strong opinion.

**Interviewer [14:07]:** <!-- T045 -->
That is fine.

**Participant [14:07]:** <!-- T046 -->
The systems I have modelled have been fairly simple, and I could model the relationships that were present.

**Interviewer [14:16]:** <!-- T047 -->
Were you taught an explicit step-by-step modelling approach?

**Participant [14:40]:** <!-- T048 -->
In theoretical classes, I was taught what each element represented, but not necessarily a step-by-step process. In the practical class, the professor solved a modelling exercise but did not explicitly say what should come first or next. He did it in his way, and perhaps I just copied it.

**Interviewer [15:06]:** <!-- T049 -->
So the process was demonstrated but not made explicit?

**Participant [15:18]:** <!-- T050 -->
I do not remember it being explicit.

## Model quality and self-evaluation

**Interviewer [15:22]:** <!-- T051 -->
How do you decide whether a finished model is good enough?

**Participant [15:45]:** <!-- T052 -->
My two main criteria are completeness and simplicity. If I can look at the model, see every relationship and actor, and fairly simply understand what is happening, I think it is a good model.

**Interviewer [16:07]:** <!-- T053 -->
Did the course provide quality rules or a checklist?

**Participant [16:26]:** <!-- T054 -->
It was probably taught, but I did not memorise it.

**Interviewer [16:32]:** <!-- T055 -->
Do you compare your model with other models?

**Participant [16:57]:** <!-- T056 -->
In my dissertation, my professor gave me previous dissertations with work somewhat similar to mine. I compared my diagrams with theirs. If mine was as simple and understandable as theirs, I considered it a good model.

**Interviewer [17:19]:** <!-- T057 -->
So you were looking for simplicity and clarity? That is the word I was searching for.

**Participant [17:25]:** <!-- T058 -->
Yes, I think it is clarity. When I model something, I usually have a specific goal and want to convey a message. If the diagram conveys the correct message, I consider it a good diagram.

## Tools and tool-supported guidance

**Interviewer [17:56]:** <!-- T059 -->
Which modelling tools have you used?

**Participant [18:25]:** <!-- T060 -->
I used paper in the course and draw.io for my dissertation, where I drew data-mining pipelines. At work, I used Canva to model how modules relate to one another. It was more text-based, which is why we used it.

**Interviewer [18:57]:** <!-- T061 -->
What did you like or dislike about those tools?

**Participant [19:14]:** <!-- T062 -->
Paper is not my preference. Online tools are already simple, intuitive, and fast, so paper feels almost like a waste of time. With a tool, I can connect something in the middle of something else.

**Interviewer [19:40]:** <!-- T063 -->
Tools can also provide templates, clarity, guidance, or warnings about connection errors. Do such features affect your view of modelling?

**Participant [20:07]:** <!-- T064 -->
No. Nothing has changed the view of modelling that I have had for as long as I can remember. Modelling is a means to an end, and I do not think anything has changed that.

**Interviewer [20:23]:** <!-- T065 -->
Do tools make modelling easier or harder than it should be?

**Participant [20:33]:** <!-- T066 -->
I think tools make modelling... That is an interesting question. I would say modelling has an inherent difficulty that tools cannot really simplify. Tools have simplified drawing as much as they can. The hard part is thinking about what I should put where. An AI for modelling might help, if that were possible, but I cannot imagine how it would be made.

**Participant [21:14]:** <!-- T067 -->
So now the tools...

**Interviewer [21:21]:** <!-- T068 -->
The difficulty is more mental than tool-related? Drawing is not difficult, but deciding which abstractions to use and what to represent is?

**Participant [21:33]:**
Yes.

**Interviewer [21:33]:** <!-- T069 -->
Would suggestions or checks about connections and relationships facilitate modelling?

**Participant [21:50]:** <!-- T070 -->
Yes, for sure. For example, that would be useful in database modelling. We recently had to inspect and create some database models on paper. An IDE that warned that a relationship did not make sense, for example because it formed a circle, would be very useful.

**Interviewer [22:48]:** <!-- T071 -->
Guidance through the modelling process would therefore be positive?

**Participant [22:53]:** <!-- T072 -->
Yes, especially for bigger models. I have not worked much with very large models, so I could answer some questions better if I had, but I can imagine that large models would benefit from those features.

## Domains, feedback, and group work

**Interviewer [23:30]:** <!-- T073 -->
Were any assignment or work domains particularly meaningful to you?

**Participant [23:58]:** <!-- T074 -->
Explaining a data-mining pipeline was meaningful. I had to aggregate data from multiple APIs and sources with different fields. Explaining that only through text would have been difficult, so adding a diagram helped.

**Interviewer [24:25]:** <!-- T075 -->
Does choosing an interesting or familiar domain affect motivation?

**Participant [24:52]:** <!-- T076 -->
Everyone has preferences, so choosing something the person prefers would be ideal.

**Interviewer [25:07]:** <!-- T077 -->
Would choosing your own domain affect your motivation and effort?

**Participant [25:20]:** <!-- T078 -->
Yes, without a doubt. It would make modelling easier, especially when starting, because you could choose something more familiar.

**Interviewer [25:30]:** <!-- T079 -->
How did feedback on modelling work in your course?

**Participant [25:47]:** <!-- T080 -->
I guess that is somewhat true. If I had a doubt, I could show the model to the teachers, and they would say whether it was good, bad, or something I probably should not do. But without taking the initiative, it was mostly just a grade. At the final discussion, the teachers had supposedly reviewed the work, but the models were not much of a subject.

**Interviewer [26:20]:** <!-- T081 -->
So unless you took the initiative and went to the teacher, they would not necessarily give detailed modelling feedback?

**Participant [26:37]:** <!-- T082 -->
I would say so, because modelling did not feel like the professors' main concern. There were other project tasks, such as code smells. Everything was a small part, and the model was one of those small parts.

**Interviewer [27:00]:** <!-- T083 -->
Was feedback early enough to improve the model?

**Participant [27:10]:** <!-- T084 -->
I remember receiving feedback in the discussion at the end of the course.

**Interviewer [27:15]:** <!-- T085 -->
Would earlier, iterative feedback have helped?

**Participant [27:26]:** <!-- T086 -->
Yes. I am not sure whether we submitted in two stages, but more stages could have helped. For example, one stage could focus on code smells and another on modelling, with feedback at each stage. That would have helped improve our models, although I understand that teachers may not have time for it.

**Interviewer [27:56]:** <!-- T087 -->
Did group work help or hinder learning modelling?

**Participant [28:10]:** <!-- T088 -->
It helped as much as having someone else doing the same thing helps. However, each person had to make their own model, so it did not feel like much of a group project.

## Competence and desired changes

**Interviewer [28:24]:** <!-- T089 -->
What should a good modeller be able to do?

**Participant [28:43]:** <!-- T090 -->
A good modeller should make something simple and clear that can be understood intuitively. Abstraction is the main skill.

**Interviewer [28:59]:** <!-- T091 -->
Do soft skills matter, or is modelling mostly technical?

**Participant [29:12]:** <!-- T092 -->
For making the model itself, I would say no. For presenting it to other people and explaining it, yes.

**Interviewer [29:21]:** <!-- T093 -->
Could communication skills help make a model more presentable?

**Participant [29:38]:** <!-- T094 -->
No... probably... yes? But I think the degree to which they help is very small.

**Interviewer [29:48]:** <!-- T095 -->
So modelling itself is mostly technical in your view?

**Participant [29:54]:** <!-- T096 -->
Yes, I would say so.

**Interviewer [29:54]:** <!-- T097 -->
What would you change about how modelling was taught in your degree?

**Participant [30:23]:** <!-- T098 -->
Choosing your own domain would be good when starting. At the same time, an unfamiliar domain is also useful because in real life you will not always model something familiar.

I would give modelling more emphasis. It was taught only in passing.

**Interviewer [31:02]:** <!-- T099 -->
So you would give it more emphasis?

**Participant [31:12]:** <!-- T100 -->
Yes, if people consider it important. I would also make modelling tasks more specific. In our project, modelling was simply one of several tasks and did not feel as though it had much purpose.

Giving the model a specific purpose would help. For example, instead of only saying, "Model this system for the stakeholder," the task could say, "Model this system to show **this** to the stakeholder," identifying a concrete message or part of the system.

**Interviewer [32:11]:** <!-- T101 -->
So the task should specify the concrete message or system aspect, rather than being generic?

**Participant [32:18]:**
Yes.

## Final reflection on frameworks

**Interviewer [32:24]:** <!-- T102 -->
Is there anything else important about learning or using modelling?

**Participant [32:40]:** <!-- T103 -->
What really put me off modelling was the frameworks. Having to use a framework feels strange to me. Some principles and standardisation are good, but often when I model, I need to show something, and a specific framework is not always the most useful way to do it.

Something you create yourself can feel more intuitive and simpler than using specific prescribed drawings or classes.

**Interviewer [33:37]:** <!-- T104 -->
Would a single, less complex and more universal framework be positive, so students would not need to learn many different frameworks?

**Interviewer [33:55]:** <!-- T105 -->
Something that lets you create...

**Participant [33:57]:** <!-- T106 -->
Essentially, yes. Having many different frameworks is very hard. I am not going to remember every detail in every single framework.

## Closing

**Interviewer [34:23]:** <!-- T107 -->
Thank you for your time. May I contact you later if I need clarification?

**Participant [34:36]:** <!-- T108 -->
Of course.
