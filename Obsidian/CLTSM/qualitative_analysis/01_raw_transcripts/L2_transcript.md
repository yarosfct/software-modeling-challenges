---
case_id: L2
role: lecturer
version: cleaned
timestamp_style: none  # none | start | range
---

# Interview L2 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was cleaned from the audio-derived recording. Repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning. Consent and boilerplate introduction were trimmed because consent was already obtained beforehand.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and teaching context

**Interviewer:** <!-- T001 -->
Thanks for meeting. To situate your answers, what modelling-related course or courses do you teach, and which modelling families do you cover?

**Participant:** <!-- T003 -->
I teach UML, mainly the basic diagrams: use case, class, sequence, statechart, and sometimes deployment diagrams. When I teach database systems, I also use entity-relationship diagrams.

**Interviewer:** <!-- T004 -->
Is that course introductory or advanced?

**Participant:** <!-- T005 -->
Introductory.

**Interviewer:** <!-- T006 -->
How long have you been teaching this content?

**Participant:** <!-- T007 -->
More than 20 years.

## Course goals and assessment

**Interviewer:** <!-- T008 -->
By the end of your course, what should students be able to do with modelling?

**Participant:** <!-- T009 -->
First, they should be able to use models to manage complexity. I also try to show them that models are useful for traceability to code. When we do that, it is important to think about modularity and abstraction, because systems change over time and we often need to improve, reuse, or update things. If we have models, traceability to code, and sometimes to tests, we can manage those changes better.

**Interviewer:** <!-- T010 -->
Where do you usually see whether students can actually do that—in exams, in projects, or somewhere else?

**Participant:** <!-- T011 -->
Mainly in projects. We also try to use the same project across different curricular units so we can understand whether students can apply the concepts in different contexts, especially when they are coding. That way they can also realise whether those models are needed or not.

**Interviewer:** <!-- T012 -->
Which activities matter most in modelling for your students: interpreting a model, creating one, refining one, or evaluating one?

**Participant:** <!-- T013 -->
I think all of those are important. In practice, students mostly create and update models, especially refine them. I do not always have enough time to evaluate models in depth, but I do explain the criteria they should use to evaluate them.

**Interviewer:** <!-- T014 -->
So you explicitly teach evaluation criteria to help students understand whether a model is correct or not?

**Participant:** <!-- T015 -->
Yes, I teach the criteria, but I do not always have enough time to work through that issue properly in class.

**Interviewer:** <!-- T016 -->
Is there anything you care about in modelling that your current assessment does not capture well?

**Participant:** <!-- T017 -->
Yes. Students do not spend enough time evaluating their own models.

## Teaching process and student autonomy

**Interviewer:** <!-- T018 -->
When students face a new modelling task, what process do you expect them to follow from the problem statement to a first workable model? Do you explicitly teach a step-by-step process?

**Participant:** <!-- T019 -->
Yes, I teach a step-by-step process. But during that process they still have to make many decisions, because the best model depends on the domain and on the specific problem. I try to tell them that there is no checklist that solves everything. They must think about the best solution and the best model for that problem.

**Interviewer:** <!-- T020 -->
Do you first solve worked examples and then ask students to apply the same ideas to a new problem?

**Participant:** <!-- T021 -->
It depends. Sometimes I do that: first I show an example, then I give them another exercise and they apply the concepts. But sometimes I only give them the exercise and expect them to do it more autonomously.

**Interviewer:** <!-- T022 -->
Do you actually see that autonomy, or do students feel insecure and wait for the teacher to solve the exercise first?

**Participant:** <!-- T023 -->
I have different kinds of students. Some show autonomy and do the work. Others expect me to solve the exercise first. Sometimes, if I do not solve it, some of them leave the classroom because they do not feel comfortable doing the exercise on their own.

**Interviewer:** <!-- T024 -->
So you think confidence or insecurity is part of the problem?

**Participant:** <!-- T025 -->
Yes, of course.

## Student difficulties and breakdown points

**Interviewer:** <!-- T026 -->
Where do students usually break down when they are getting started? Do they struggle more with abstraction, semantics, refinement, or quality checking?

**Participant:** <!-- T027 -->
Mainly semantics, and also refinement. Sometimes they understand that the system has to do something, such as register a user, but they struggle to express that properly in the model and need to look at other examples.

**Interviewer:** <!-- T028 -->
Can you walk me through one concrete moment when students struggled with modelling in your course? I am interested in a real recurring situation rather than a general list.

**Participant:** <!-- T029 -->
Not really in terms of switching between modelling families. We do not have many curricular units using modelling. In the bachelor's degree, software engineering is the main curricular unit that uses these concepts, and students generally do not like modelling very much.

**Interviewer:** <!-- T030 -->
That is common here too. Students often see it as extra documentation and do it because they have to. Usually the students who really become interested in modelling only continue with it later, for example in an advanced master's course.

**Participant:** <!-- T031 -->
Yes, that is true. In the master's degree they struggle a little as well. We use Petri nets there, but it is not the same degree.

**Interviewer:** <!-- T032 -->
In your experience, is the main difficulty understanding the notation or getting started independently when there is no teacher demonstration in front of them?

**Participant:** <!-- T033 -->
Getting started independently. Even when they have to define a concrete process, they may struggle with basic modelling steps such as identifying verbs, actions, or actors. They understand the idea of an actor in theory, but when they actually have to identify one in a specific case, they get stuck.

**Interviewer:** <!-- T034 -->
Do worked examples transfer well to new tasks, or do students still struggle once the details change a little?

**Participant:** <!-- T035 -->
They still struggle when the domain changes a little.

**Interviewer:** <!-- T036 -->
When students hit those difficulties, what kind of support helps them most?

## Tools and tool support

**Participant:** <!-- T037 -->
I use a tool, and I try to use a complete one, especially one that can generate code, because that motivates them. They are always looking for code, whether in Java, C#, or something else. If I choose a tool that helps generate code, they become more motivated.

**Interviewer:** <!-- T038 -->
But do those tools also introduce complexity that can hinder learning?

**Participant:** <!-- T039 -->
They can introduce some complexity, but they also help students improve their models because they prevent some syntax errors and some classic mistakes. The tool does not let them do certain things incorrectly, so they realise it is useful.

**Interviewer:** <!-- T040 -->
So overall you think the tools are helpful?

**Participant:** <!-- T041 -->
Yes, especially because when students go abroad or later work with industry tools, those tools are often quite complex. If they already understand the core concepts of a project and how to organise it with a tool, they can adapt more easily.

**Interviewer:** <!-- T042 -->
What tool do you use?

**Participant:** <!-- T043 -->
Visual Paradigm.

**Interviewer:** <!-- T044 -->
Since you teach multiple modelling families, do you think it works well across the whole course?

**Participant:** <!-- T045 -->
Yes. It has many functionalities and is quite complete for our curricular units, so it is a good choice. It supports more than just one kind of diagram, including some network-related views and other project representations.

**Interviewer:** <!-- T046 -->
Do you think the tool has practical constraints, such as cost or learning curve? Does it slow down the course, or do students learn it on their own?

**Participant:** <!-- T047 -->
I do both. First, I provide short videos covering the main issues, then I ask them to explore the tool. I show the basics with three short videos, each around three or four minutes. That is usually enough. They complain a little about having to install one more tool, but not so much about the complexity itself.

**Interviewer:** <!-- T048 -->
In my view, using one broader tool is actually helpful, because otherwise students have to keep shifting between family-specific tools.

**Participant:**
Yes.

**Interviewer:** <!-- T049 -->
Is there anything missing from the tool? For example, guidance about next steps, collaboration support, or something similar?

**Participant:** <!-- T050 -->
What I miss most is real-time collaboration and communication features. We often need to use tools such as Trello, Notion, or Azure boards to manage the project, while Visual Paradigm is used for the modelling work itself. I think it can be a good idea to separate the product from the process, but more built-in collaboration would help.

## Model quality, feedback, and peer evaluation

**Interviewer:** <!-- T051 -->
Earlier you said you teach evaluation criteria explicitly. How do students learn what counts as a good model in your course? Do you provide feedback, comparison opportunities, or templates?

**Participant:** <!-- T052 -->
I do all of that. It depends on the type of diagram, but I use common evaluation criteria for UML diagrams and I also give students feedback. I use tools that allow their work to be published so it is visible to the whole class, and then I give them 10 to 15 minutes to compare their work with others and classify the models using stars.

**Interviewer:** <!-- T053 -->
That is interesting.

**Participant:** <!-- T054 -->
Of course, it is not a perfect method because it can lead to bias. It can become a kind of contest, and students may give better ratings to their friends.

**Interviewer:** <!-- T055 -->
But it can also create some friendly competition.

**Participant:** <!-- T056 -->
Yes, and sometimes they are even more demanding with each other than I am.

**Interviewer:** <!-- T057 -->
Do you think that motivates them to perform better?

**Participant:** <!-- T058 -->
Yes, of course.

**Interviewer:** <!-- T059 -->
Do you explicitly name criteria such as completeness, consistency, readability, and fit for purpose?

**Participant:** <!-- T060 -->
Yes, I do. I try to make those criteria explicit, even though that is not always easy to do in enough detail.

**Interviewer:** <!-- T061 -->
You mentioned projects. Do you grade them in stages, or is there just one final submission?

**Participant:** <!-- T062 -->
There are two stages.

**Interviewer:** <!-- T063 -->
And I assume you provide feedback after the first stage?

**Participant:**
Yes.

**Interviewer:** <!-- T064 -->
Do students get the chance to revise after feedback? Is that revision also graded?

**Participant:** <!-- T065 -->
Yes, they have the chance to improve, but the revision itself is not evaluated. Only the final submission is graded.

## Course conditions: domain, attendance, and workload

**Interviewer:** <!-- T066 -->
Beyond tools, what conditions shape modelling learning most in your course? Workload, attendance, assignment domain, transition between modelling families, or something else?

**Participant:** <!-- T067 -->
First of all, the domain. Students need to understand the domain, and sometimes that is very hard.

**Interviewer:** <!-- T068 -->
How much does domain familiarity matter? Do you let students choose their own project domain?

**Participant:** <!-- T069 -->
I tried that, but it led to unbalanced projects, because students chose domains of very different complexity.

**Interviewer:** <!-- T070 -->
So it is fairer to have one common domain for everyone?

**Participant:** <!-- T071 -->
Yes. Even then, understanding the domain is difficult, so I try to propose examples that are easier for them to understand.

**Interviewer:** <!-- T072 -->
Do students have any role in choosing that domain, given that different students are interested in different things?

**Participant:** <!-- T073 -->
I usually choose something related to current technologies, but students have very different interests, so I do not usually base the choice on their preferences.

**Interviewer:** <!-- T074 -->
How much do attendance and workload limit what students can actually learn?

**Participant:** <!-- T075 -->
They matter a lot.

**Interviewer:** <!-- T076 -->
Do you see students stop attending classes at certain points?

**Participant:** <!-- T077 -->
Yes, of course. After the big party here in Beja I lose many students. There are two main moments: one is related to the weather, the sun, and parties; the other is when they have many tests and projects in other subjects.

**Interviewer:** <!-- T078 -->
So workload pulls them away from class?

**Participant:**
Yes.

**Interviewer:** <!-- T079 -->
Do you think some concepts are better learned in person than through lecture slides or online materials alone?

**Participant:** <!-- T080 -->
It depends on the student. Some students do very well with my materials, but others look for something else and sometimes they find videos or resources that are not good, or that use different conventions. So I ask them that if they study using other materials, they should ask me first.

**Interviewer:** <!-- T081 -->
That is common here too. Sometimes students follow a YouTube tutorial or some other resource and do not realise that the notation or conventions differ from what they are being taught.

## Desired changes and time constraints

**Interviewer:** <!-- T082 -->
If you could make one realistic change that would improve modelling learning the most in your context, what would it be? For example, a pedagogical change, an assessment change, or a tool change.

**Participant:** <!-- T083 -->
If I had financial support, I would try to buy a very good tool to help us. But the first thing I need is more time.

**Interviewer:** <!-- T084 -->
Do you think the course is more demanding than what the ECTS allocation allows?

**Participant:** <!-- T085 -->
Yes. This course needs more time.

**Interviewer:** <!-- T086 -->
Is that because of the breadth of the course, the learning of a new tool, the presentation of models, or the evaluation of those models?

**Participant:** <!-- T087 -->
It is mainly because of the evaluation. If I really try to use models to manage many things properly, it takes a lot of time. We need time to explain the concepts, let students do exercises, give feedback, give them another exercise, and let them improve. My main improvement would be more time to teach all of this. It is not that I use too many modelling families; I mainly use UML and some models for database systems. Even so, we still need to teach behaviour and structure, give different perspectives of the system, and work on complexity, traceability, and forward and backward links. That is demanding, and continuous assessment with feedback takes a lot of time. So first I would ask for more time, and second for a very good tool.

**Interviewer:** <!-- T088 -->
So a better tool could help with evaluation and feedback as well?

**Participant:**
Yes.

## Industry use and modelling families

**Interviewer:** <!-- T089 -->
To wrap up, is there anything important about teaching or learning modelling that I did not ask but that you think matters?

**Participant:** <!-- T090 -->
I still wonder why companies in industry do not use modelling artefacts more often. It is interesting, because we try to use modelling to manage complexity, and in my opinion it is a good support for software development.

**Interviewer:** <!-- T091 -->
I also thought it was more common in industry. What do you think about the idea of generalising modelling more, so that one family could cover more use cases instead of teaching many different families?

**Participant:** <!-- T092 -->
It would be a good idea to have only one, of course. But it is not easy to reach a consensus, even among teachers and the wider community.

**Interviewer:** <!-- T093 -->
Yes, I understand.

**Participant:** <!-- T094 -->
For example, sometimes I teach BPMN, Business Process Model and Notation, but I notice that not many people use it, and when they do, they often use it incorrectly.

**Interviewer:** <!-- T095 -->
That is part of the problem. When people shift from one family to another, they often assume common patterns that do not really apply.

**Participant:** <!-- T096 -->
Yes. We have several tools here in the polytechnic that use BPMN, and many people use it incorrectly. When I look at those systems, I can immediately see that the notation is wrong, and that is quite disturbing.

## Closing

**Interviewer:** <!-- T097 -->
That is all from my side. Thank you, this was very helpful. If you are interested, I can share a short summary of my findings later when I finish the thesis, and I might also follow up with one or two clarification questions if needed.

**Participant:** <!-- T098 -->
Yes, to both of those. I would like to receive your summary and your work, and of course I am available if you need any clarification later.
