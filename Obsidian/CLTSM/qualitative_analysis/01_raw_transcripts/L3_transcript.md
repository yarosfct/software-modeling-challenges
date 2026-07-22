---
case_id: L3
role: lecturer
version: cleaned
timestamp_style: none  # none | start | range
---

# Interview L3 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was cleaned from the audio-derived recording. Repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning. Consent and boilerplate introduction were trimmed because consent was already obtained beforehand.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and teaching context

**Interviewer:** <!-- T001 -->
Thanks for meeting. To situate your answers, what modelling-related course or courses do you teach, and which modelling families do you cover?

**Participant:** <!-- T003 -->
At the moment I am teaching a software engineering course, so it is not specifically about modelling. Before my last sabbatical leave, however, I was teaching a modelling course at the undergraduate level. I do not recall the exact course acronym right now, but it was a course where I covered most of UML, roughly eight or nine of the thirteen UML 2 diagrams.

**Interviewer:** <!-- T004 -->
Was that an introductory or advanced course, for example at bachelor's or master's level?

**Participant:** <!-- T005 -->
It was for undergraduate students, typically in the second semester of the second year.

**Interviewer:** <!-- T006 -->
How long have you been teaching this content?

**Participant:** <!-- T007 -->
I taught that particular course for around six or seven years, but before coming here I was also a professor at Nova University, where I taught modelling topics as well. Altogether, I have been teaching modelling for about two decades.

## Course goals and learning outcomes

**Interviewer:** <!-- T008 -->
By the end of the course, what should students be able to do with modelling? What is the intended outcome?

**Participant:** <!-- T009 -->
Formally, the course had official learning outcomes, and I followed them seriously. They were not just bureaucratic objectives. In practice, students had to do many modelling exercises and learn to work with a wide range of UML diagrams.

**Interviewer:** <!-- T010 -->
Which modelling activities mattered most in your course: interpreting, creating, refining, or evaluating?

**Participant:** <!-- T011 -->
In the practical assignments, the emphasis was more on synthesis, meaning creating models, rather than only interpreting them. Of course, students first had to learn how to interpret example models, and I provided many examples in slides and lectures. Then they had to synthesise their own models from problem descriptions.

**Interviewer:** <!-- T012 -->
What do you mean exactly by synthesis?

**Participant:** <!-- T013 -->
It means giving students a natural-language description and asking them to produce a model from it.

**Interviewer:** <!-- T014 -->
So essentially converting from natural language into a model?

**Participant:** <!-- T015 -->
Exactly.

**Interviewer:** <!-- T016 -->
And what about assessment?

**Participant:** <!-- T017 -->
The course was offered to three undergraduate programmes, so we had between 200 and 300 students in total. We had a large teaching team, around six people, including professors, PhD students, and sometimes top master's students helping in lab classes. In exams, because there is limited time, we usually used a mixture of model interpretation and model synthesis. Full synthesis tasks take more time, so in short exams we often combined both.

**Interviewer:** <!-- T018 -->
Is there anything you care about in modelling that your current assessment did not capture well?

**Participant:** <!-- T019 -->
I was actually quite happy with the assessment approach I used, because it relied on executable UML, which was something rather distinctive compared with what many colleagues were doing.

## USE tool and executable modelling

**Interviewer:** <!-- T020 -->
Can you explain that a little more?

**Participant:** <!-- T021 -->
I used an environment called the UML Specification Environment, or USE. It was originally developed in Germany, first at Bremen and later in Hamburg. The tool allows you to execute models. You can instantiate class models with object diagrams, use a textual DSL to instantiate and manipulate them, and execute sequence and state-based behaviour. That means I could actually run my students' models and check whether they behaved correctly. For assignments such as an ATM or a vending machine, students could see the models executing. This was useful both for learning, because the models became dynamic rather than static, and for grading, because it helped us validate what students had produced.

**Interviewer:** <!-- T022 -->
Is that tool mainly for lecturers, or can students also use it directly?

**Participant:** <!-- T023 -->
Students can also use it directly. In fact, I first explored it together with your supervisor, who was my first PhD student. The tool is open source, on GitHub, written in Java, and easy to install and run.

**Interviewer:** <!-- T024 -->
Is the tool intuitive enough, or does it create extra friction for students?

**Participant:** <!-- T025 -->
It definitely creates some friction. It is a sophisticated tool, and one reason is that it supports a part of UML that students usually do not learn deeply, namely OCL, the Object Constraint Language. OCL allows you to express constraints and business rules that cannot be represented only with diagrams. That is powerful, but it also means students have to learn a new language, and that was one of the biggest sources of difficulty in the course.

**Interviewer:** <!-- T026 -->
So that learning curve was a real cost?

**Participant:** <!-- T027 -->
Yes. I probably pushed them quite hard on OCL because without it they could not build executable models.

**Interviewer:** <!-- T028 -->
What mattered most in choosing that tool? Was it mainly the semantic checking and grading support?

**Participant:** <!-- T029 -->
Yes, definitely. It helped a lot with grading. If I had had access at the time to the kind of large language models we have today, I would have liked something that could compare an OCL constraint with the original natural-language requirement and help assess whether they matched semantically. But at the same time, if students had had those tools back then, many of them might simply have asked the model to write the constraint for them and would not really have learned the language.

**Interviewer:** <!-- T030 -->
Beyond grading, did students also benefit directly from the semantic checking?

**Participant:** <!-- T031 -->
The tool itself does not provide much guidance in the sense of next-step suggestions or tutoring. It does not tell students what to do next. That would be a very interesting add-on. As far as I know, it has a plug-in architecture, so in principle it would be possible to create something like that.

**Interviewer:** <!-- T032 -->
So a guidance layer on top of the tool would be useful?

**Participant:** <!-- T033 -->
Very useful. And honestly, today I would have to rethink how to teach modelling altogether because large language models are highly disruptive in this area. A few years ago the use of LLMs in modelling was still quite naive, but now their ability to interpret models has improved enormously. If students can simply take a picture of a model and ask an LLM what it means, then the whole teaching approach changes.

**Interviewer:** <!-- T034 -->
Yes, I understand what you mean.

**Participant:** <!-- T035 -->
Still, I do not believe human understanding can simply be replaced. Modelling is fundamentally about abstraction, and abstraction has to be trained. If we stop training those abilities, we lose important human capabilities.

**Interviewer:** <!-- T036 -->
I share that concern. Do you know how students perceived the tool?

**Participant:** <!-- T037 -->
Like in most universities, students were very unevenly distributed. About one third were very good students who were happy to learn new things and benefit from the challenge. The other two thirds often felt the course was too demanding, that the learning curve was too steep, and that I made them work hard. At the time, they did not have LLMs to help them, so if they wanted a good grade, they really had to think and put in the effort. On top of that, I had around 20 to 30 percent of students who were essentially no-shows.

## Teaching process and lab support

**Interviewer:** <!-- T038 -->
When students face a new modelling task, do you teach an explicit process from the problem statement to a first workable model?

**Participant:** <!-- T039 -->
Not in a rigid step-by-step way for every diagram. UML has many diagram types, and some are more straightforward than others. In general, I would describe the approach as learn by doing, supported by adequate tools. By adequate tools, I mean tools that do not let students commit invalid modelling operations.

**Interviewer:** <!-- T040 -->
Can you give an example of what you mean?

**Participant:** <!-- T041 -->
A tool like Visio can let you draw almost anything, just like paper does. You can connect elements that should not be connected and still produce something that looks like a diagram. I did not want students learning that way. I wanted them to use strongly typed tools with model-checking features, so that certain mistakes would simply not be allowed.

**Interviewer:** <!-- T042 -->
So you did not usually use pen-and-paper exercises?

**Participant:** <!-- T043 -->
No. I tried to keep everything tool-based.

**Interviewer:** <!-- T044 -->
And in the practical classes, did you focus on exercises, group work, or both?

**Participant:** <!-- T045 -->
A mixture of both. Typically, students started with individual warm-up exercises and then continued into group assignments.

**Interviewer:** <!-- T046 -->
In those warm-up exercises, where did students usually break down?

**Participant:** <!-- T047 -->
Their behaviour was very diverse, so it is hard to generalise. But when students had trouble interpreting the problem or getting started, I instructed the lab assistants to break the problem into smaller parts. We would take one small piece and show on the board how that piece could be modelled, or we would show a similar example from another domain. That helped students see that the problem was manageable.

**Interviewer:** <!-- T048 -->
Do students wait for that kind of teacher intervention before they really begin?

**Participant:** <!-- T049 -->
We tried to promote autonomy first, especially through small-group discussion. Only when the majority of students were stuck would we intervene together at the whiteboard. In some weeks, if I already knew the assignment would be too difficult based on what I had covered in the theoretical class, I told the teaching team to begin the lab with a worked example on the board. I also prepared written guides for the lab sessions and sometimes pointed students back to specific lecture slides with similar examples.

**Interviewer:** <!-- T050 -->
Do you think the lecture materials alone are enough for students who skip theoretical classes?

**Participant:** <!-- T051 -->
Ideally, I would like students to study some material in advance and then come to class with questions, as happens in some places. But in my experience that does not work well with Portuguese students. If students skip the theoretical class, the lab should not become a repeated theory session. That would not scale. A lab assistant should be there to facilitate learning and remove barriers, not to reteach the whole lecture to each small group.

**Interviewer:** <!-- T052 -->
So you saw the lab as support, not replacement?

**Participant:** <!-- T053 -->
Exactly. Students still need to make the effort to understand the context instead of assuming they can skip theory and recover everything later in the lab.

## Assessment and continuous evaluation

**Interviewer:** <!-- T054 -->
What is your opinion on continuous evaluation?

**Participant:** <!-- T055 -->
I used two assessment modes. The standard one was continuous evaluation with assignments developed in groups during the semester, usually groups of three or four. There was also an individual assessment component worth at least 50 percent of the final grade. In addition, I allowed students to choose a long final exam, usually around three hours, where they had to interpret and synthesise models.

**Interviewer:** <!-- T056 -->
Did you compare the two?

**Participant:** <!-- T057 -->
Yes. I statistically compared the averages of the students who followed continuous evaluation with those who took the exam-only route, and the continuous-evaluation group performed clearly better, by roughly two or three points on a twenty-point scale.

**Interviewer:** <!-- T058 -->
Did continuous evaluation consist of a staged project?

**Participant:** <!-- T059 -->
Yes, with multiple submissions, probably around four, although I do not recall the exact number now.

**Interviewer:** <!-- T060 -->
Did students receive feedback at each step and then refine the same models afterward?

**Participant:** <!-- T061 -->
Not really, because each stage covered a different part of modelling. For example, if one stage focused on use cases, we usually did not return to use case modelling later. In an ideal world I would provide feedback, students would revise, and we would reassess the same artefact. But with the available time, that was not feasible. There are simply too many aspects of UML to cover.

**Interviewer:** <!-- T062 -->
So again, time is the limitation?

**Participant:** <!-- T063 -->
Yes. Ideally, I would have liked a tool that could provide students with immediate feedback, because doing that manually at scale is very difficult for professors.

## Project domains and motivation

**Interviewer:** <!-- T064 -->
How did you choose project domains? Did students pick their own?

**Participant:** <!-- T065 -->
No. We chose one common domain for the whole class each semester, partly for fairness and partly so the work remained comparable across groups. One year it might be a travel agency, another year a railway company, another a hotel.

**Interviewer:** <!-- T066 -->
Did you try to choose domains that would motivate students?

**Participant:** <!-- T067 -->
Yes. I usually tried to build a motivating story around the domain. For example, one year I used the football world championship as a theme. I would put students in the role of consultants developing a system for a client.

**Interviewer:** <!-- T068 -->
But you never let students choose their own domain?

**Participant:** <!-- T069 -->
No, that would not be feasible with 300 students. Some would choose very simple domains and others very complex ones. Also, some students would choose something trivial that already had complete models available online and would simply copy them, which would be unfair.

## Desired changes: LLM feedback

**Interviewer:** <!-- T070 -->
If you could make one realistic change that would most improve modelling learning in your context, what would it be?

**Participant:** <!-- T071 -->
I think large language models should be used, because they are part of real life now. What I would really like is an LLM-based feedback system. A student could build a model, and the tool would explain back in natural language what that model actually means. Then the student could compare that explanation with what they intended to model. That kind of semantic feedback would help a lot.

**Interviewer:** <!-- T072 -->
So the idea is not to have the LLM solve the task for the student, but to critique and explain the student's model?

**Participant:** <!-- T073 -->
Exactly. Existing tools already do syntactic checking reasonably well. What is still missing is semantic checking. That is where an LLM could make the biggest difference.

**Interviewer:** <!-- T074 -->
And regarding pedagogy and course conditions more generally, are you satisfied?

**Participant:** <!-- T075 -->
Not entirely. One thing I find missing, even in the books I used, is good guidance on how to break down a complex real-world problem into smaller parts that can be modelled. Textbook examples fit on one page, but real problems do not. That makes it difficult to teach practical modelling methodology through books alone.

## BPMN and modelling families

**Interviewer:** <!-- T076 -->
Is there anything important about teaching or learning modelling that I did not ask?

**Participant:** <!-- T077 -->
One thing is that we focused mostly on UML, but I also teach BPMN at the master's level. Many of the points I made about tools still apply there, although BPMN tools differ in some important ways.

**Interviewer:** <!-- T078 -->
I assumed it was only UML because of the beginning of the interview.

**Participant:** <!-- T079 -->
That is understandable. In BPMN, one very important feature is the ability to collaborate on models. Students should be able to work cooperatively, and ideally the professor should also be able to observe the work remotely, trace changes, and provide feedback directly in the same environment.

**Interviewer:** <!-- T080 -->
So cooperative editing and traceability matter a lot there?

**Participant:** <!-- T081 -->
Yes. For BPMN I use Signavio, which is a collaborative tool. It supports cooperative editing and some traceability features, and it lets me provide feedback directly in the same environment where students are modelling. It is very good in that respect. What it lacks, at least in the academic version, is model execution or simulation, which I would also like to have because I teach process simulation.

**Interviewer:** <!-- T082 -->
Do some students take both UML and BPMN?

**Participant:** <!-- T083 -->
Yes, some do.

**Interviewer:** <!-- T084 -->
Do you notice friction when they move from one modelling family to another?

**Participant:** <!-- T085 -->
I usually joke with them that BPMN is easier because it extends the idea of activity diagrams. But in reality BPMN is very rich and much more sophisticated than that simple comparison suggests. It has many kinds of events, gateways, and constructs.

**Interviewer:** <!-- T086 -->
And the BPMN tool you use is domain-specific, not just a general drawing tool?

**Participant:** <!-- T087 -->
Yes, it is BPMN-specific and quite powerful.

**Interviewer:** <!-- T088 -->
Does that help motivation?

**Participant:** <!-- T089 -->
Yes, especially at master's level. I show students that BPMN can describe not only business processes in companies but also research workflows. I use examples from the research processes of master's and PhD students, such as data collection, storage, and testing. Since master's students are preparing dissertations, that connection to research is often motivating.

## Closing

**Interviewer:** <!-- T090 -->
Thank you very much. This was very helpful. If you are interested, I can share a short summary of my findings later when I finish the thesis, and I might also follow up with one or two clarification questions.

**Participant:** <!-- T091 -->
Okay. I would like that.

## Editorial note

A short segment of the conversation was not recorded here. The lecturer explained that there was a strong correlation between attendance and grades, and that he showed students statistical evidence of that relationship at the beginning of the semester. The conversation then continued with continuous evaluation.
