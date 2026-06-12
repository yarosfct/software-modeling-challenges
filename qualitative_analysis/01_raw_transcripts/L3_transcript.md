# Interview L3 Transcript

`M = interviewer`  
`T = lecturer`

**M:** Thanks for meeting with me. I'm studying how modeling is taught and learned in higher education, especially the difficulties students face, the kinds of support that help them, and how teaching choices, tools, and course conditions shape that experience. With your permission, I would like to record this so I do not miss any detail. This should take around 20 to 30 minutes, and you can skip any question if you want.

**T:** Okay, no problem.

**M:** To situate your answers, could you briefly tell me what modeling-related course or courses you teach, and which modeling families you cover?

**T:** At the moment I am teaching a software engineering course, so it is not specifically about modeling. Before my last sabbatical leave, however, I was teaching a modeling course at the undergraduate level. I do not recall the exact course acronym right now, but it was a course where I covered most of UML, roughly eight or nine of the thirteen UML 2 diagrams.

**M:** And was that an introductory or advanced course, for example at bachelor's or master's level?

**T:** It was for undergraduate students, typically in the second semester of the second year.

**M:** And how long have you been teaching this content?

**T:** I taught that particular course for around six or seven years, but before coming here I was also a professor at Nova University, where I taught modeling topics as well. Altogether, I have been teaching modeling for about two decades.

**M:** By the end of the course, what should students be able to do with modeling? What is the intended outcome?

**T:** Formally, the course had official learning outcomes, and I followed them seriously. They were not just bureaucratic objectives. In practice, students had to do many modeling exercises and learn to work with a wide range of UML diagrams.

**M:** Which modeling activities mattered most in your course: interpreting, creating, refining, or evaluating?

**T:** In the practical assignments, the emphasis was more on synthesis, meaning creating models, rather than only interpreting them. Of course, students first had to learn how to interpret example models, and I provided many examples in slides and lectures. Then they had to synthesize their own models from problem descriptions.

**M:** What do you mean exactly by synthesis?

**T:** It means giving students a natural-language description and asking them to produce a model from it.

**M:** So essentially converting from natural language into a model.

**T:** Exactly.

**M:** And what about assessment?

**T:** The course was offered to three undergraduate programs, so we had between 200 and 300 students in total. We had a large teaching team, around six people, including professors, PhD students, and sometimes top master's students helping in lab classes. In exams, because there is limited time, we usually used a mixture of model interpretation and model synthesis. Full synthesis tasks take more time, so in short exams we often combined both.

**M:** Is there anything you care about in modeling that your current assessment did not capture well?

**T:** I was actually quite happy with the assessment approach I used, because it relied on executable UML, which was something rather distinctive compared with what many colleagues were doing.

**M:** Can you explain that a little more?

**T:** I used an environment called the UML Specification Environment, or USE. It was originally developed in Germany, first at Bremen and later in Hamburg. The tool allows you to execute models. You can instantiate class models with object diagrams, use a textual DSL to instantiate and manipulate them, and execute sequence and state-based behavior. That means I could actually run my students' models and check whether they behaved correctly. For assignments such as an ATM or a vending machine, students could see the models executing. This was useful both for learning, because the models became dynamic rather than static, and for grading, because it helped us validate what students had produced.

**M:** Is that tool mainly for lecturers, or can students also use it directly?

**T:** Students can also use it directly. In fact, I first explored it together with your supervisor, who was my first PhD student. The tool is open source, on GitHub, written in Java, and easy to install and run.

**M:** Tooling is a really important aspect of learning for me, so I want to ask: is the tool intuitive enough, or does it create extra friction for students?

**T:** It definitely creates some friction. It is a sophisticated tool, and one reason is that it supports a part of UML that students usually do not learn deeply, namely OCL, the Object Constraint Language. OCL allows you to express constraints and business rules that cannot be represented only with diagrams. That is powerful, but it also means students have to learn a new language, and that was one of the biggest sources of difficulty in the course.

**M:** So that learning curve was a real cost.

**T:** Yes. I probably pushed them quite hard on OCL because without it they could not build executable models.

**M:** What mattered most in choosing that tool? Was it mainly the semantic checking and grading support?

**T:** Yes, definitely. It helped a lot with grading. If I had had access at the time to the kind of large language models we have today, I would have liked something that could compare an OCL constraint with the original natural-language requirement and help assess whether they matched semantically. But at the same time, if students had had those tools back then, many of them might simply have asked the model to write the constraint for them and would not really have learned the language.

**M:** Beyond grading, did students also benefit directly from the semantic checking?

**T:** The tool itself does not provide much guidance in the sense of next-step suggestions or tutoring. It does not tell students what to do next. That would be a very interesting add-on. As far as I know, it has a plug-in architecture, so in principle it would be possible to create something like that.

**M:** So a guidance layer on top of the tool would be useful.

**T:** Very useful. And honestly, today I would have to rethink how to teach modeling altogether because large language models are highly disruptive in this area. A few years ago the use of LLMs in modeling was still quite naive, but now their ability to interpret models has improved enormously. If students can simply take a picture of a model and ask an LLM what it means, then the whole teaching approach changes.

**M:** Yes, I understand what you mean.

**T:** Still, I do not believe human understanding can simply be replaced. Modeling is fundamentally about abstraction, and abstraction has to be trained. If we stop training those abilities, we lose important human capabilities.

**M:** I share that concern. Do you know how students perceived the tool?

**T:** Like in most universities, students were very unevenly distributed. About one third were very good students who were happy to learn new things and benefit from the challenge. The other two thirds often felt the course was too demanding, that the learning curve was too steep, and that I made them work hard. At the time, they did not have LLMs to help them, so if they wanted a good grade, they really had to think and put in the effort. On top of that, I had around 20 to 30 percent of students who were essentially no-shows.

**M:** When students face a new modeling task, do you teach an explicit process from the problem statement to a first workable model?

**T:** Not in a rigid step-by-step way for every diagram. UML has many diagram types, and some are more straightforward than others. In general, I would describe the approach as learn by doing, supported by adequate tools. By adequate tools, I mean tools that do not let students commit invalid modeling operations.

**M:** Can you give an example of what you mean?

**T:** A tool like Visio can let you draw almost anything, just like paper does. You can connect elements that should not be connected and still produce something that looks like a diagram. I did not want students learning that way. I wanted them to use strongly typed tools with model-checking features, so that certain mistakes would simply not be allowed.

**M:** So you did not usually use pen-and-paper exercises?

**T:** No. I tried to keep everything tool-based.

**M:** And in the practical classes, did you focus on exercises, group work, or both?

**T:** A mixture of both. Typically, students started with individual warm-up exercises and then continued into group assignments.

**M:** In those warm-up exercises, where did students usually break down?

**T:** Their behavior was very diverse, so it is hard to generalize. But when students had trouble interpreting the problem or getting started, I instructed the lab assistants to break the problem into smaller parts. We would take one small piece and show on the board how that piece could be modeled, or we would show a similar example from another domain. That helped students see that the problem was manageable.

**M:** Do students wait for that kind of teacher intervention before they really begin?

**T:** We tried to promote autonomy first, especially through small-group discussion. Only when the majority of students were stuck would we intervene together at the whiteboard. In some weeks, if I already knew the assignment would be too difficult based on what I had covered in the theoretical class, I told the teaching team to begin the lab with a worked example on the board. I also prepared written guides for the lab sessions and sometimes pointed students back to specific lecture slides with similar examples.

**M:** Do you think the lecture materials alone are enough for students who skip theoretical classes?

**T:** Ideally, I would like students to study some material in advance and then come to class with questions, as happens in some places. But in my experience that does not work well with Portuguese students. If students skip the theoretical class, the lab should not become a repeated theory session. That would not scale. A lab assistant should be there to facilitate learning and remove barriers, not to reteach the whole lecture to each small group.

**M:** So you saw the lab as support, not replacement.

**T:** Exactly. Students still need to make the effort to understand the context instead of assuming they can skip theory and recover everything later in the lab.

**[Editorial note]** A short segment of the conversation was not recorded here. The lecturer explained that there was a strong correlation between attendance and grades, and that he showed students statistical evidence of that relationship at the beginning of the semester. The conversation then continued with continuous evaluation.

**M:** What is your opinion on continuous evaluation?

**T:** I used two assessment modes. The standard one was continuous evaluation with assignments developed in groups during the semester, usually groups of three or four. There was also an individual assessment component worth at least 50 percent of the final grade. In addition, I allowed students to choose a long final exam, usually around three hours, where they had to interpret and synthesize models.

**M:** Did you compare the two?

**T:** Yes. I statistically compared the averages of the students who followed continuous evaluation with those who took the exam-only route, and the continuous-evaluation group performed clearly better, by roughly two or three points on a twenty-point scale.

**M:** Did continuous evaluation consist of a staged project?

**T:** Yes, with multiple submissions, probably around four, although I do not recall the exact number now.

**M:** Did students receive feedback at each step and then refine the same models afterward?

**T:** Not really, because each stage covered a different part of modeling. For example, if one stage focused on use cases, we usually did not return to use case modeling later. In an ideal world I would provide feedback, students would revise, and we would reassess the same artifact. But with the available time, that was not feasible. There are simply too many aspects of UML to cover.

**M:** So again, time is the limitation.

**T:** Yes. Ideally, I would have liked a tool that could provide students with immediate feedback, because doing that manually at scale is very difficult for professors.

**M:** How did you choose project domains? Did students pick their own?

**T:** No. We chose one common domain for the whole class each semester, partly for fairness and partly so the work remained comparable across groups. One year it might be a travel agency, another year a railway company, another a hotel.

**M:** Did you try to choose domains that would motivate students?

**T:** Yes. I usually tried to build a motivating story around the domain. For example, one year I used the football world championship as a theme. I would put students in the role of consultants developing a system for a client.

**M:** But you never let students choose their own domain?

**T:** No, that would not be feasible with 300 students. Some would choose very simple domains and others very complex ones. Also, some students would choose something trivial that already had complete models available online and would simply copy them, which would be unfair.

**M:** If you could make one realistic change that would most improve modeling learning in your context, what would it be?

**T:** I think large language models should be used, because they are part of real life now. What I would really like is an LLM-based feedback system. A student could build a model, and the tool would explain back in natural language what that model actually means. Then the student could compare that explanation with what they intended to model. That kind of semantic feedback would help a lot.

**M:** So the idea is not to have the LLM solve the task for the student, but to critique and explain the student's model.

**T:** Exactly. Existing tools already do syntactic checking reasonably well. What is still missing is semantic checking. That is where an LLM could make the biggest difference.

**M:** And regarding pedagogy and course conditions more generally, are you satisfied?

**T:** Not entirely. One thing I find missing, even in the books I used, is good guidance on how to break down a complex real-world problem into smaller parts that can be modeled. Textbook examples fit on one page, but real problems do not. That makes it difficult to teach practical modeling methodology through books alone.

**M:** Is there anything important about teaching or learning modeling that I did not ask?

**T:** One thing is that we focused mostly on UML, but I also teach BPMN at the master's level. Many of the points I made about tools still apply there, although BPMN tools differ in some important ways.

**M:** I assumed it was only UML because of the beginning of the interview.

**T:** That is understandable. In BPMN, one very important feature is the ability to collaborate on models. Students should be able to work cooperatively, and ideally the professor should also be able to observe the work remotely, trace changes, and provide feedback directly in the same environment.

**M:** So cooperative editing and traceability matter a lot there.

**T:** Yes. For BPMN I use Signavio, which is a collaborative tool. It supports cooperative editing and some traceability features, and it lets me provide feedback directly in the same environment where students are modeling. It is very good in that respect. What it lacks, at least in the academic version, is model execution or simulation, which I would also like to have because I teach process simulation.

**M:** Do some students take both UML and BPMN?

**T:** Yes, some do.

**M:** Do you notice friction when they move from one modeling family to another?

**T:** I usually joke with them that BPMN is easier because it extends the idea of activity diagrams. But in reality BPMN is very rich and much more sophisticated than that simple comparison suggests. It has many kinds of events, gateways, and constructs.

**M:** And the BPMN tool you use is domain-specific, not just a general drawing tool?

**T:** Yes, it is BPMN-specific and quite powerful.

**M:** Does that help motivation?

**T:** Yes, especially at master's level. I show students that BPMN can describe not only business processes in companies but also research workflows. I use examples from the research processes of master's and PhD students, such as data collection, storage, and testing. Since master's students are preparing dissertations, that connection to research is often motivating.

**M:** Thank you very much. This was very helpful. If you are interested, I can share a short summary of my findings later when I finish the thesis, and I might also follow up with one or two clarification questions.

**T:** Okay. I would like that.
