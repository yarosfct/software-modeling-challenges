# Interview L2 Transcript

`M = interviewer`  
`T = lecturer`

**M:** Thanks for meeting with me. I'm studying how modeling is taught and learned in higher education, especially the difficulties students face, the kinds of support they need, and how teaching choices, tools, and course conditions shape those experiences. With your permission, I would like to record this so I do not miss any detail. This should take around 20 to 30 minutes, and you can skip any question if you want. You already consented beforehand, so I will start.

**T:** Yes, I confirm.

**M:** To situate your answers, could you briefly tell me what modeling-related course or courses you teach and which modeling families you cover?

**T:** I teach UML, mainly the basic diagrams: use case, class, sequence, statechart, and sometimes deployment diagrams. When I teach database systems, I also use entity-relationship diagrams.

**M:** Is that course introductory or advanced?

**T:** Introductory.

**M:** And how long have you been teaching this content?

**T:** More than 20 years.

**M:** By the end of your course, what should students be able to do with modeling?

**T:** First, they should be able to use models to manage complexity. I also try to show them that models are useful for traceability to code. When we do that, it is also important to think about modularity and abstraction, because systems change over time and we often need to improve, reuse, or update things. If we have models, traceability to code, and sometimes to tests, we can manage those changes better.

**M:** And where do you usually see whether students can actually do that? In exams, in projects, or somewhere else?

**T:** Mainly in projects. We also try to use the same project across different curricular units so we can understand whether students can apply the concepts in different contexts, especially when they are coding. That way they can also realize whether those models are needed or not.

**M:** Which activities matter most in modeling for your students: interpreting a model, creating one, refining one, or evaluating one?

**T:** I think all of those are important. In practice, students mostly create and update models, especially refine them. I do not always have enough time to evaluate models in depth, but I do explain the criteria they should use to evaluate them.

**M:** So you explicitly teach evaluation criteria to help students understand whether a model is correct or not?

**T:** Yes, I teach the criteria, but I do not always have enough time to work through that issue properly in class.

**M:** Is there anything you care about in modeling that your current assessment does not capture well?

**T:** Yes. Students do not spend enough time evaluating their own models.

**M:** When students face a new modeling task, what process do you expect them to follow from the problem statement to a first workable model? Do you explicitly teach a step-by-step process?

**T:** Yes, I teach a step-by-step process. But during that process they still have to make many decisions, because the best model depends on the domain and on the specific problem. I try to tell them that there is no checklist that solves everything. They must think about the best solution and the best model for that problem.

**M:** Do you first solve worked examples and then ask students to apply the same ideas to a new problem?

**T:** It depends. Sometimes I do that: first I show an example, then I give them another exercise and they apply the concepts. But sometimes I only give them the exercise and expect them to do it more autonomously.

**M:** And do you actually see that autonomy, or do students feel insecure and wait for the teacher to solve the exercise first?

**T:** I have different kinds of students. Some show autonomy and do the work. Others expect me to solve the exercise first. Sometimes, if I do not solve it, some of them leave the classroom because they do not feel comfortable doing the exercise on their own.

**M:** So you think confidence or insecurity is part of the problem.

**T:** Yes, of course.

**M:** Where do students usually break down when they are getting started? Do they struggle more with abstraction, semantics, refinement, or quality checking?

**T:** Mainly semantics, and also refinement. Sometimes they understand that the system has to do something, such as register a user, but they struggle to express that properly in the model and need to look at other examples.

**M:** Can you walk me through one concrete moment when students struggled with modeling in your course? I am interested in a real recurring situation rather than a general list.

**T:** Not really in terms of switching between modeling families. We do not have many curricular units using modeling. In the bachelor's degree, software engineering is the main curricular unit that uses these concepts, and students generally do not like modeling very much.

**M:** That is common here too. Students often see it as extra documentation and do it because they have to. Usually the students who really become interested in modeling only continue with it later, for example in an advanced master's course.

**T:** Yes, that is true. In the master's degree they struggle a little as well. We use Petri nets there, but it is not the same degree.

**M:** In your experience, is the main difficulty understanding the notation or getting started independently when there is no teacher demonstration in front of them?

**T:** Getting started independently. Even when they have to define a concrete process, they may struggle with basic modeling steps such as identifying verbs, actions, or actors. They understand the idea of an actor in theory, but when they actually have to identify one in a specific case, they get stuck.

**M:** Do worked examples transfer well to new tasks, or do students still struggle once the details change a little?

**T:** They still struggle when the domain changes a little.

**M:** When students hit those difficulties, what kind of support helps them most?

**T:** I use a tool, and I try to use a complete one, especially one that can generate code, because that motivates them. They are always looking for code, whether in Java, C#, or something else. If I choose a tool that helps generate code, they become more motivated.

**M:** But do those tools also introduce complexity that can hinder learning?

**T:** They can introduce some complexity, but they also help students improve their models because they prevent some syntax errors and some classic mistakes. The tool does not let them do certain things incorrectly, so they realize it is useful.

**M:** So overall you think the tools are helpful.

**T:** Yes, especially because when students go abroad or later work with industry tools, those tools are often quite complex. If they already understand the core concepts of a project and how to organize it with a tool, they can adapt more easily.

**M:** What tool do you use?

**T:** Visual Paradigm.

**M:** I know that tool. Since you teach multiple modeling families, do you think it works well across the whole course?

**T:** Yes. It has many functionalities and is quite complete for our curricular units, so it is a good choice. It supports more than just one kind of diagram, including some network-related views and other project representations.

**M:** Do you think the tool has practical constraints, such as cost or learning curve? Does it slow down the course, or do students learn it on their own?

**T:** I do both. First, I provide short videos covering the main issues, then I ask them to explore the tool. I show the basics with three short videos, each around three or four minutes. That is usually enough. They complain a little about having to install one more tool, but not so much about the complexity itself.

**M:** In my view, using one broader tool is actually helpful, because otherwise students have to keep shifting between family-specific tools.

**T:** Yes.

**M:** Is there anything missing from the tool? For example, guidance about next steps, collaboration support, or something similar?

**T:** What I miss most is real-time collaboration and communication features. We often need to use tools such as Trello, Notion, or Azure boards to manage the project, while Visual Paradigm is used for the modeling work itself. I think it can be a good idea to separate the product from the process, but more built-in collaboration would help.

**M:** Earlier you said you teach evaluation criteria explicitly. How do students learn what counts as a good model in your course? Do you provide feedback, comparison opportunities, or templates?

**T:** I do all of that. It depends on the type of diagram, but I use common evaluation criteria for UML diagrams and I also give students feedback. I use tools that allow their work to be published so it is visible to the whole class, and then I give them 10 to 15 minutes to compare their work with others and classify the models using stars.

**M:** That is interesting.

**T:** Of course, it is not a perfect method because it can lead to bias. It can become a kind of contest, and students may give better ratings to their friends.

**M:** But it can also create some friendly competition.

**T:** Yes, and sometimes they are even more demanding with each other than I am.

**M:** Do you think that motivates them to perform better?

**T:** Yes, of course.

**M:** Do you explicitly name criteria such as completeness, consistency, readability, and fit for purpose?

**T:** Yes, I do. I try to make those criteria explicit, even though that is not always easy to do in enough detail.

**M:** You mentioned projects. Do you grade them in stages, or is there just one final submission?

**T:** There are two stages.

**M:** And I assume you provide feedback after the first stage.

**T:** Yes.

**M:** Do students get the chance to revise after feedback? Is that revision also graded?

**T:** Yes, they have the chance to improve, but the revision itself is not evaluated. Only the final submission is graded.

**M:** Beyond tools, what conditions shape modeling learning most in your course? Workload, attendance, assignment domain, transition between modeling families, or something else?

**T:** First of all, the domain. Students need to understand the domain, and sometimes that is very hard.

**M:** How much does domain familiarity matter? Do you let students choose their own project domain?

**T:** I tried that, but it led to unbalanced projects, because students chose domains of very different complexity.

**M:** So it is fairer to have one common domain for everyone.

**T:** Yes. Even then, understanding the domain is difficult, so I try to propose examples that are easier for them to understand.

**M:** Do students have any role in choosing that domain, given that different students are interested in different things?

**T:** I usually choose something related to current technologies, but students have very different interests, so I do not usually base the choice on their preferences.

**M:** How much do attendance and workload limit what students can actually learn?

**T:** They matter a lot.

**M:** Do you see students stop attending classes at certain points?

**T:** Yes, of course. After the big party here in Beja I lose many students. There are two main moments: one is related to the weather, the sun, and parties; the other is when they have many tests and projects in other subjects.

**M:** So workload pulls them away from class.

**T:** Yes.

**M:** Do you think some concepts are better learned in person than through lecture slides or online materials alone?

**T:** It depends on the student. Some students do very well with my materials, but others look for something else and sometimes they find videos or resources that are not good, or that use different conventions. So I ask them that if they study using other materials, they should ask me first.

**M:** That is common here too. Sometimes students follow a YouTube tutorial or some other resource and do not realize that the notation or conventions differ from what they are being taught.

**M:** If you could make one realistic change that would improve modeling learning the most in your context, what would it be? For example, a pedagogical change, an assessment change, or a tool change.

**T:** If I had financial support, I would try to buy a very good tool to help us. But the first thing I need is more time.

**M:** Do you think the course is more demanding than what the ECTS allocation allows?

**T:** Yes. This course needs more time.

**M:** Is that because of the breadth of the course, the learning of a new tool, the presentation of models, or the evaluation of those models?

**T:** It is mainly because of the evaluation. If I really try to use models to manage many things properly, it takes a lot of time. We need time to explain the concepts, let students do exercises, give feedback, give them another exercise, and let them improve. My main improvement would be more time to teach all of this. It is not that I use too many modeling families; I mainly use UML and some models for database systems. Even so, we still need to teach behavior and structure, give different perspectives of the system, and work on complexity, traceability, and forward and backward links. That is demanding, and continuous assessment with feedback takes a lot of time. So first I would ask for more time, and second for a very good tool.

**M:** So a better tool could help with evaluation and feedback as well.

**T:** Yes.

**M:** To wrap up, is there anything important about teaching or learning modeling that I did not ask but that you think matters?

**T:** I still wonder why companies in industry do not use modeling artifacts more often. It is interesting, because we try to use modeling to manage complexity, and in my opinion it is a good support for software development.

**M:** I also thought it was more common in industry. What do you think about the idea of generalizing modeling more, so that one family could cover more use cases instead of teaching many different families?

**T:** It would be a good idea to have only one, of course. But it is not easy to reach a consensus, even among teachers and the wider community.

**M:** Yes, I understand.

**T:** For example, sometimes I teach BPMN, Business Process Model and Notation, but I notice that not many people use it, and when they do, they often use it incorrectly.

**M:** That is part of the problem. When people shift from one family to another, they often assume common patterns that do not really apply.

**T:** Yes. We have several tools here in the polytechnic that use BPMN, and many people use it incorrectly. When I look at those systems, I can immediately see that the notation is wrong, and that is quite disturbing.

**M:** That is all from my side. Thank you, this was very helpful. If you are interested, I can share a short summary of my findings later when I finish the thesis, and I might also follow up with one or two clarification questions if needed.

**T:** Yes, to both of those. I would like to receive your summary and your work, and of course I am available if you need any clarification later.
