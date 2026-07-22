---
case_id: L4
role: lecturer
version: cleaned
timestamp_style: range  # none | start | range
---

# Interview L4 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was cleaned against the audio-derived recording. Mixed-speaker segments were separated where needed, and repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and courses taught

**Interviewer [00:00–01:00]:** <!-- T001 -->
Thank you for meeting with me. I am studying how modelling is taught and learned in higher education, especially the difficulties students face, what kinds of support help them, and how teaching choices, tools, and course conditions shape that experience. With your permission, I would like to record the interview so I do not miss any details. You can skip any question if you do not feel comfortable answering it.

Which modelling-related courses do you teach, and which modelling families do you cover?

**Participant [01:01–01:18]:** <!-- T002 -->
I have been teaching modelling for many years, so perhaps it is better to focus on what I am teaching now.

**Participant [01:18–02:53]:** <!-- T003 -->
Over the years, I have proposed and taught several modelling-related courses, such as Software Engineering, Software Development Methods, Specification Languages, Requirements and Software Architecture, and Requirements Engineering.

Currently, I am focusing on Requirements Engineering. The Computer Science master's degree has recently changed. Previously, I taught a course on Requirements and Software Architecture, but the topics were quite broad, so the course was divided into two separate courses: one on Software Architecture and another on Requirements Engineering. I am teaching the Requirements Engineering course, which will now be in its second edition in this format.

**Interviewer [02:53–03:12]:** <!-- T004 -->
So you are currently teaching advanced courses, mainly in the master's programme?

**Participant [03:04–03:12]:** <!-- T005 -->
Yes. I am involved in two courses: one in the PhD programme and one in the master's programme.

## Modelling families and learning objectives

**Interviewer [03:12–03:29]:** <!-- T006 -->
By the end of your current course, what should students be able to do with modelling? And where in the course do you see whether they can do it?

**Participant [03:30–03:39]:** <!-- T007 -->
Maybe first I should explain which modelling families and languages I teach.

**Participant [03:40–07:17]:** <!-- T008 -->
The course covers both early requirements and late requirements. Early requirements have an intersection with business analysis. The goal is to understand the organisational goals and needs of a company or organisation. This helps students understand the “why” of a problem: why the problem matters, and how a solution can add value to the organisation.

I start with goal-oriented languages. In particular, I teach iStar because it focuses on actors as active entities with their own goals and responsibilities. Actors depend on each other to achieve goals. In iStar, students build two types of models. The first is a strategic model, which shows strategic relationships among actors. These actors may be large entities in a company or external parties with which the company interacts or has some kind of contract. Then we focus on specific actors that are more directly related to the problem and build a more detailed rational model, which refines their responsibilities.

During this process, it is very important for students to differentiate between functional and non-functional requirements. Functional requirements are what students usually think of first, because they are used to implementing functionality. Later, these refinements are translated into UML models, because UML is a language students are supposed to know from the Software Engineering course.

**Interviewer [07:17–07:38]:** <!-- T009 -->
Do you teach non-functional requirements in depth?

**Participant [07:38–08:53]:** <!-- T010 -->
Yes, I go in depth with non-functional requirements. I use specific approaches and languages to refine non-functional requirements into solutions or methods that help satisfy a quality requirement to some degree. These refinements then need to be integrated with the functional part of the system.

So, in terms of modelling families, I teach goal-oriented languages, including iStar and the NFR Framework, which is more specific to non-functional requirements. Then students move toward late requirements and translate goals, actors, and refinements into something more concrete, usually using UML.

**Participant [09:12–10:06]:** <!-- T011 -->
But now answering your question, in terms of learning objectives, students must know how to elicit requirements, both functional and non-functional. They need to understand the role and importance of stakeholders. They need to understand what goals are and what system interactions are. They must be able to translate informal requirements and informal problem descriptions into something structured, represented in a model.

They also need to justify why the model is the way it is, what alternatives existed, and what the quality of the model is. That is something students often have difficulty with.

**Interviewer [10:07–10:22]:** <!-- T012 -->
Do you teach quality criteria explicitly, or are students expected to interpret them?

**Participant [10:22–11:14]:** <!-- T013 -->
They are aware of them. We have a list of quality criteria that models should comply with. However, it is difficult to convey this to students. They come to me quite late in their degree. They used to be in the ninth semester, and now they are in the eighth semester. They have had Software Engineering, but that course is very broad. It covers many things.

**Interviewer [11:14–11:17]:** <!-- T014 -->
It goes from code smells to patterns.

**Participant [11:17–12:06]:** <!-- T015 -->
Exactly. It is very broad. So students do not have enough time to think about modelling. When they arrive in my class, I feel that they look at me and think: “What is this for? I can program a solution for whatever problem you give me.”

Then I give them a problem description. Usually it is a short paragraph about a problem domain they may not be familiar with. They quickly realise that they need more information about the problem before they can build anything. That is when they begin to understand why requirements matter.

## Requirements teaching approach

**Participant [12:21–13:04]:** <!-- T016 -->
My problem descriptions are intentionally short and vague. They concern problems with some dimension, and I deliberately leave ambiguities. Students need to feel that in real life, in a company, this is how things often are. They need to understand that requirements must be discovered, and also that the requirements they initially discover may not be the ones that really matter.

They also need to understand that the requirements are not “their” requirements. The solution is not for them; it is for someone else who has the problem.

**Participant [13:04–14:20]:** <!-- T017 -->
One thing I do is give students a problem and ask them to identify relevant stakeholders. Then they need to interview those stakeholders, similar to what you are doing now. Depending on the problem, they may interview colleagues around campus, people in a company, or others.

They need to understand that requirements are not something for me to simply give them, and they are not something for them to invent. Requirements must be extracted from stakeholders.

**Participant [14:20–16:25]:** <!-- T018 -->
I do have my own understanding of the problem domain, but the same problem can have many different solutions depending on who is interested in it. Different people, companies, markets, partners, and existing systems can shape the problem in different directions.

Students develop a project during the course, and the specification is not necessarily the same for every group. Depending on which companies or stakeholders they interview, they may follow different routes. At some point they may have a long list of requirements, which they need to prioritise. They may conduct a second iteration of interviews so the stakeholders can indicate which requirements are most relevant. In this way, the requirements are not exactly the same for all groups.

## Project design and domain choice

**Interviewer [16:26–16:59]:** <!-- T019 -->
How does the project work in your course? In some courses all students work on the same problem domain. Do students in your course have freedom to choose their own domain?

**Participant [16:50–18:08]:** <!-- T020 -->
Usually I give them freedom. Some students come with their own ideas, although most do not. Some are unsure, or they do not have access to a company or relevant contact. I always provide a problem domain for those who do not have one.

The project has several milestones. At one important milestone, each group submits a subset of the specification. I take it home, mark it, give feedback, and then discuss it with each group. They then adapt their work. Feedback is very important.

**Interviewer [18:08–19:10]:** <!-- T021 -->
Does this creative freedom create problems in terms of fairness? For example, one group might choose a very simple domain while another chooses a complex one.

**Participant [18:42–19:10]:** <!-- T022 -->
I have to accept the problem domain first. If students propose something too simple, I explain that it is not enough. We can then re-evaluate it from another perspective, but it is not just anything they think of.

**Interviewer [19:10–20:25]:** <!-- T023 -->
What if the domain is too complex?

**Participant [19:21–20:25]:** <!-- T024 -->
Then we need to scope it. I may let them start with a more complex problem because I want them to feel why it is complex. They identify stakeholders, prepare questions, conduct interviews, and then return with what they found. At that point, I ask whether they can address all of it in the time they have. Then we do scoping and pruning, ideally with the agreement of the stakeholder or company they are working with.

**Interviewer [20:25–21:08]:** <!-- T025 -->
Does this freedom increase your workload?

**Participant [20:35–21:08]:** <!-- T026 -->
Yes. Giving them that freedom creates much more work for me. It would be much easier to give everyone the same problem with very specific guardrails. But I prefer giving them freedom.

**Participant [21:08–22:35]:** <!-- T027 -->
I hope it motivates them. When I was a student, I did not like football. I remember that the worst programming tests and exams for me were the ones using football or FIFA examples. I did not know the domain. Even if the teacher explained it, it was the first time I was looking at those rules, and I felt disadvantaged. Others who did not like football or did not follow football rules probably felt the same.

I always felt it was unfair for a professor to give me a problem domain I was not interested in. I do not want to do the same to my students.

**Participant [22:35–24:46]:** <!-- T028 -->
Some students propose domains connected to areas where they plan to create a company, for example. I always have one default problem domain, but I give them the freedom to work on something else if they prefer. They just need to write about it, give it to me, and then we fine-tune it to make sure it fits the subject.

The problem cannot be too well defined or too limited. If the problem is simple enough to develop in one or two days, modelling may not be very relevant. These techniques are for problems with some complexity, where communication is needed, where the problem domain is not yours, and where you need to understand someone else’s situation.

## Student readiness and timing

**Interviewer [24:46–25:10]:** <!-- T029 -->
Are you satisfied with the current state of your course, or do you feel you lack time, resources, or tools?

**Participant [25:03–26:45]:** <!-- T030 -->
Ideally, I would like access to students earlier. I get students in their fourth year, after they have already been taught many things, but not much about modelling. They also already have specific interests. The subject is quite small and is not chosen by many students.

I used to work as a consultant for a technology company for many years, and sometimes I gave training to clients. I taught object modelling, object-oriented programming, and object-oriented analysis and design. Occasionally, former students would attend these trainings years later and say: “Now I understand why what you taught was relevant.” As students, they had not felt the need for modelling, but in a company context they realised its value.

**Participant [26:46–28:29]:** <!-- T031 -->
I often find that students only really understand the need and value of modelling when they are in a working context. In the university context, problems are often too well defined.

I am currently supervising a master's student in a company. The student was not in my course, but I meet regularly with them and their company supervisor. I told them that what they need to do is understand the requirements, model those requirements, and talk with the stakeholders involved. But they did not take the course.

People often think that requirements and modelling are not very important. They prefer to build code instead of models. But building a model is much faster than building code. If something needs to change, it is better to change the model than to change the code, because once code exists you are already quite committed to the solution.

## Practical value of modelling

**Interviewer [29:03–31:19]:** <!-- T032 -->
Do you try to show students the practical value of modelling, for example by making them talk to companies or stakeholders?

**Participant [29:34–31:19]:** <!-- T033 -->
It is not easy. The course lasts only one semester, about 13 weeks, with evaluation points throughout the semester. Students are also doing three or four other subjects with continuous evaluation. After the fourth or fifth week, they are already stressed with many evaluations.

Sometimes I think they would prefer a better-defined problem: “Just tell me what to do and I will do it.” It is not easy to leave them in a situation where they have to think, discover, and investigate.

However, almost every semester I receive emails from students afterwards thanking me for the course. Some later work in companies and come back to say that they are using modelling at work, sometimes in places where nobody knew about it before, but colleagues became open to it.

**Participant [31:25–34:17]:** <!-- T034 -->
I once met a former student who told me that two professors had really marked them, and I was one of them. That was very meaningful.

I still wish students had this course earlier. Ideally, they should get some feeling for modelling in the second year. Even using a little bit of UML in programming courses would help. For example, they could build basic class diagrams or sequence charts before writing C++ or Java. That would help them understand object communication and begin to see that building models is useful.

Another very important issue is consistency among models. Different models represent different perspectives of the same problem, so they must be consistent with each other. In UML, for instance, if you have a class diagram and a sequence chart, everything in the sequence chart should somehow be represented in the class diagram, and vice versa. Even working with two models in the first or second year would already be helpful.

## Classroom activities and evaluation

**Interviewer [00:18–01:06]:** <!-- T035 -->
Which modelling activities matter most for students, and which ones do you evaluate most? For example: interpreting models, creating models, refining models, or evaluating models?

**Participant [01:08–01:40]:** <!-- T036 -->
With artificial intelligence, things have changed. The way I evaluate has changed. For example, the project now has less weight, and the exam has more weight.

**Interviewer [01:42–02:38]:** <!-- T037 -->
In the exam, what kinds of activities are mostly evaluated?

**Participant [01:58–02:38]:** <!-- T038 -->
I give students a problem and still ask them to create a small model, but with very clear guardrails because they do not have much time. I also ask them to interpret models. Sometimes I give them models that are wrong.

I tell students that notation is not the most relevant thing. I do not care whether something is a square, a circle, or a triangle. What I care about is the meaning of the symbol. If they do not remember the exact symbol in the exam, they can give me a legend explaining what they decided to use.

**Participant [02:38–04:23]:** <!-- T039 -->
The meaning is the important thing. Different tools may use slightly different symbols. That also creates problems for tool integration. Some good tools have expensive licenses, so students do not have access, and neither do we. We use free tools, but integration across modelling language families does not exist.

For me, the meaning of the concept is fundamental. Students need to understand the problem, the meaning of each concept, how concepts relate to each other, and what a given model represents.

**Participant [04:24–05:31]:** <!-- T040 -->
Sometimes I give students two or three alternative models for the same apparent situation and ask which one better represents the meaning of the description. Meaning is important. Consistency across models is important, and consistency is part of model quality.

One difficulty students often have is understanding what is enough and what the ideal level of granularity is. When is refinement enough? When is the model enough?

**Interviewer [05:33–06:08]:** <!-- T041 -->
Do you teach criteria for knowing when the model is enough?

**Participant [05:47–08:25]:** <!-- T042 -->
We discuss it. I use the whiteboard a lot, although students do not always like it. My room usually has two whiteboards. Since the class is not very large, I sometimes divide each whiteboard into two, so different groups of students work on different parts of the board.

They all address the same problem using their part of the whiteboard. Then they swap and validate what others are doing. It is a kind of peer review. I want them to see that this is also necessary in their project work. If one person builds one model, another builds another, and nobody checks consistency, that creates problems.

Most of my students are standing during my classes, especially in lab sessions. Sometimes we use tools in class, especially the first time we use a new tool, so that I can clarify doubts. But often we use the whiteboard because I want them to discuss, communicate, and play roles.

Sometimes different teams work on different projects or variations of the same project. One team plays the role of stakeholders, while another plays developers or business analysts. They interview each other. I try to simulate what could happen in a company, with a team and a client. This works partly because the class is small. If I had a much larger class, it would be much more difficult.

**Interviewer [08:25–09:02]:** <!-- T043 -->
Does this method help them understand what makes a good model and where to stop?

**Participant [09:02–11:14]:** <!-- T044 -->
I give tips and feedback, and we use some rules of thumb. For example, I sometimes refer to Miller’s rule, seven plus or minus two. But even for professionals, experience matters. Choosing the right level of abstraction is not easy.

I tell students that nobody does anything well the first time. Iteration is fundamental. They must be ready to cross out their model and start again. If they become too attached to a model, that is a problem. They need a critical mind.

I ask them to give their model to me and to colleagues, and I ask colleagues to act as devil’s advocates. They should be demanding and critical, because that is how they discover problems. If they simply say “I like this” because the person is their friend, that does not help.

Students need clear rules and guardrails, but identifying the right level of abstraction is difficult. Even in agile methods, it is not always obvious what the correct granularity of an epic, user story, or use case should be.

## Teaching approach and classroom culture

**Interviewer [11:32–12:51]:** <!-- T045 -->
Do you solve exercises on the whiteboard before students start working?

**Participant [11:43–12:51]:** <!-- T046 -->
No, I do not solve exercises for them. They solve the exercises with me. They go to the whiteboard and work. I move from group to group and ask questions: “What do you mean by that?” “What about this?” I ask the questions I think they need to hear so they can understand by themselves why something does not work. Then they scratch it out and do it again.

**Interviewer [13:11–14:50]:** <!-- T047 -->
Do you think this approach affects shy students? In some courses, students wait for the teacher to solve the first example before they try.

**Participant [13:11–14:50]:** <!-- T048 -->
I give solutions only after discussing with them and after they have tried to solve the problem. If students waited for me to solve the first example, they could wait the whole semester.

That is one reason why I use icebreakers in the first class. The first two-hour class is for getting to know each other. I introduce myself not only as a professional but also as a person, and I encourage students to share a little about themselves. I challenge them with questions so they also talk to each other. When they leave the first class, they are supposed to know each other a little.

**Interviewer [14:50–17:05]:** <!-- T049 -->
Has this ever made students give up the course?

**Participant [14:50–17:05]:** <!-- T050 -->
I had one student who, in the second class, asked whether there would be coding or programming in the course. I said no: they had plenty of programming courses, and now it was time to learn something else. The student said this was not for them and did not return. It was the first time in my career that a student asked me so directly. I appreciated the honesty.

I did offer that, if they wanted, they could program a solution based on the specification they would build, but that would require extra work from them and was not part of the expected course work.

## Soft skills and communication

**Interviewer [17:05–18:57]:** <!-- T051 -->
Do you think soft skills are important for software modelling?

**Participant [17:18–18:57]:** <!-- T052 -->
Very important. Communication is very important. I tell students that if they show a little of who they are, what they are worried about, and what is going on inside them, people will trust them more and open up.

If you go to a client meeting and present yourself as formal, distant, and as if you know everything, you are probably not going to get much from that person. One very important thing in software engineering is empathy. If you cannot see the other person, understand that this is their problem and not yours, listen carefully, and ask follow-up questions, then you will not get the right requirements. Some things will remain unsaid because you did not ask the right questions or because the person did not feel comfortable telling you what they needed.

**Participant [19:19–21:56]:** <!-- T053 -->
I give students examples from my own professional experience. I worked on a long-term project with an organisation to help identify problematic cases in their domain. The goal was to create an indicator of fraud so the organisation could focus scarce expert resources on suspicious cases while handling straightforward cases more efficiently.

I entered the project through senior management. That created problems because operational workers felt threatened. They may have thought they could lose their jobs or that their knowledge was being replaced, especially because we were using machine-learning techniques.

It took many meetings to convince them. Formal meetings with senior management were one thing, but informal meetings without management present were different. I would meet them during coffee breaks and chat with them. That was how I broke the ice and earned their trust. Soft skills were important in that professional context.

**Interviewer [21:56–23:51]:** <!-- T054 -->
Do you try to model that openness with your students?

**Participant [22:25–23:51]:** <!-- T055 -->
Yes. I try to let students know that I do not know everything. I might already have a preferred solution, but I ask them to help me think: “Which one is best? Let’s all think together.”

I tell them from the beginning that if they just want a solution to the exercise, they are not going to get it from me. We solve things on the whiteboard, take pictures at the end, and one or two students send me the pictures. I post them on the course platform. The following week, we start from there and build on it. So the solution is built gradually, through discussion.

## Tools and integration

**Interviewer [23:52–24:28]:** <!-- T056 -->
How do tools affect your teaching? Which tools do you use? What is your opinion on free tools, paid tools, family-specific tools, or drawing tools like draw.io?

**Participant [24:28–27:22]:** <!-- T057 -->
One reason I use the whiteboard a lot is that I do not have good integrated tools for what I want to teach. I do not just want students to give me a model. I want them to explain why something is important, what the consequence is of including or not including it, and what impact a decision has on quality attributes such as security, privacy, or availability.

I want them to ask: Where is this quality requirement specified in the model? What decisions reflect this non-functional requirement? We keep iterating, asking questions about the models, and going back to the initial list of functional and non-functional requirements. With non-functional requirements, they will not be completely mapped in the model, so students need to know what is being lost and why. The rationale for the model needs to be documented.

A good tool would be very useful: a lightweight, integrated tool, not just a drawing tool. I want tools with semantics and validation. For example, I use piStar. It is not integrated with other tools, but if a student builds a model in piStar, I know the model is semantically correct in terms of the language. If the student tries something against the language, the tool does not allow it. That is the kind of tool I value.

**Interviewer [27:22–29:12]:** <!-- T058 -->
So you value semantic checking and guidance?

**Participant [27:28–29:12]:** <!-- T059 -->
Yes. I value semantic checking and guidance. piStar is family-specific and goal-oriented. In the course, I typically start with iStar, then discuss functional and non-functional requirements, the NFR Framework, sustainability requirements, and SUSAF. I raise students’ awareness of sustainability and the responsibility we have as computer scientists. Our products may support sustainability, harm sustainability, or influence people to behave in more or less sustainable ways. Overall, the course includes iStar, the NFR Framework, SUSAF, and UML.

**Interviewer [29:12–30:22]:** <!-- T060 -->
Does switching tools for different diagrams create friction?

**Participant [29:30–30:22]:** <!-- T061 -->
Unfortunately, yes. That really bothers me. If I had project funding for something related to modelling, it would be for tools. Semantic checking, guidance on next steps, templates, and collaboration would be extremely useful in a teaching context.

**Participant [30:22–32:53]:** <!-- T062 -->
There is a difference between drawing tools and method-specific tools. In the 1990s, for example, some tools followed a specific method. Other tools, like Rational Rose, were more method-agnostic. They proposed techniques and had some validity checks, but they did not force you to start with use cases and then follow a specific order.

It would be useful to have an agnostic tool that proposes a set of techniques able to represent the “why,” the “who,” the “what,” and the “how,” while still giving freedom in how to use them. However, I do not see it happening easily in the near future because good tools require large investments.

I try to compensate for the lack of such a tool by using the whiteboard, discussing meaning, seeing how things integrate, and understanding the complementarity of different techniques and models.

## Desired changes and student challenges

**Interviewer [33:21–35:54]:** <!-- T063 -->
If you could make one realistic change to improve modelling learning in your context, what would it be?

**Participant [34:03–35:54]:** <!-- T064 -->
I would definitely like a lightweight tool with validity checks that supports some integration across different paradigms or modelling families. When I am using iStar, I am working in a goal-oriented paradigm. When I move to UML, I am in an object-oriented paradigm. A lightweight integrated tool would be very useful.

I would also like access to students earlier in their training. It is a shame that students learn about software engineering so late in the degree. Most students go to companies, work in teams, and may develop products for clients. It makes sense for software engineering to have a stronger role and to appear earlier.

**Participant [35:55–37:05]:** <!-- T065 -->
Instead of students just sitting in the classroom, listening to the teacher, and then going home to do exercises, it would be interesting to involve them in trying to solve real problems on campus. They could understand processes in accounting, human resources, or other units. They could model and try to understand real organisational problems. But this takes time and requires other people to be available to talk with them, so it is not easy.

**Interviewer [37:05–39:49]:** <!-- T066 -->
Is there anything important about teaching or learning modelling that I did not ask?

**Participant [37:32–39:49]:** <!-- T067 -->
I can summarise some issues I see in students. Some may be because I get them only in the fourth year.

Students undervalue software engineering and, in particular, modelling. They do not understand the value of modelling early enough. They often look at modelling as a few boxes and arrows and ask: “What does this mean? I cannot compile this.”

A good tool with some checking would help. I have that for iStar, but not for NFR refinements. Students need to understand that models are perspectives on a problem. Different models provide complementary perspectives, and together they give a better view of the problem. Making students understand this is not always easy.

I think students are overwhelmed with too many grades, projects, tests, and deadlines. They do not have time to assimilate, think, or relax. I feel they are always trying to get rid of tasks, finish one thing, turn the page, and move on.

## Abstraction and early exposure

**Participant [00:07–00:45]:** <!-- T068 -->
One last thing is that I feel students struggle with abstraction. They like to see things in a very concrete way. They like to try things, compile, test, and feel secure about what they see. I think they struggle with being able to abstract, and abstraction is necessary to build models.

**Interviewer [00:46–01:24]:** <!-- T069 -->
Do software engineering and software modelling courses help students understand abstraction?

**Participant [01:10–01:24]:** <!-- T070 -->
They do use abstraction, but I sometimes think they do not understand that they are using it.

**Participant [01:36–03:31]:** <!-- T071 -->
Programming also focuses on abstraction. The Software Engineering course is heavy for students and teachers. The idea, from my perspective, was to have students do something from beginning to end, including testing and deployment if possible. They still do that to some extent.

There are also important topics like evolution and code smells, because many people later maintain code developed by someone else. Being able to identify those smells is useful. But nothing is perfect.

**Interviewer [03:32–04:02]:** <!-- T072 -->
So, in summary, you think students should be introduced to software modelling and its skills much earlier?

**Participant [03:51–05:43]:** <!-- T073 -->
Much earlier than they are now. There is a school of thought that says students may not have the maturity early on to think about these things, and there may be some truth in that. But since childhood, we understand the value of communication, and adults often teach empathy: do not do to others what you do not want others to do to you.

As students grow into adults, they sometimes forget simple things. By the fourth or fifth year, many are tired of university and eager to get a job and be independent. They may not have the mental space to think about something they believe will not be valuable to them. They think: “I am a computer scientist, so I am going to program,” or they may want distributed systems, computer architecture, or something else. Software engineering is different from that.

## Ethics, socio-technical skills, and AI

**Interviewer [05:43–07:02]:** <!-- T074 -->
There seems to be an ethical dimension to software engineering and modelling, especially because they involve people, communication, and responsibility.

**Participant [06:28–07:02]:** <!-- T075 -->
Ethics is important for humanity. It is important across all subjects: computer science, physics, mathematics, and all sciences. Ethics is fundamental for us.

**Interviewer [07:02–09:42]:** <!-- T076 -->
Software engineering has a socio-technical aspect because it involves communication with people and understanding requirements.

**Participant [08:03–09:42]:** <!-- T077 -->
Life is changing. In the past, one could perhaps be a programmer sitting in a basement, with someone else telling them what to do, and just writing code. Nowadays, things are changing. AI threatens many professions, including computer science.

AI may affect programmers, business analysts, software engineers, and requirements engineers. But at the end of the day, requirements engineers and software engineers still have to communicate with the people who are paying for the product to be built. ChatGPT or Claude do not have that interaction with the client.

Once a requirement specification is built, then it can be given to an AI tool to transform into code or perhaps into models. AI is already building some models, although the quality is not very good yet, and it is definitely writing lines of code.

**Interviewer [09:42–10:00]:** <!-- T078 -->
Nowadays, communication may be what differentiates people, since many people can program.

**Participant [09:53–10:00]:** <!-- T079 -->
There are very good programmers who never attended university.
