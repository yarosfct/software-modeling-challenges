---
case_id: S3
role: student
version: cleaned
timestamp_style: range  # none | start | range
---

# Interview S3 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was cleaned against the audio-derived recording. Mixed-speaker segments were corrected where needed, and repetitions, false starts, and interviewer filler were reduced where they did not affect meaning. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the audio.

## Background and modelling experience

**Participant [00:00–00:19]:** <!-- T001 -->
Before we start, I want to say for the recording that I studied this around two years ago. If we are talking about software modelling or the Software Engineering course, that was around two years ago, so I may not remember some things.

**Interviewer [00:19–00:49]:** <!-- T002 -->
That is not a problem. Answer what you remember, and skip anything you do not feel comfortable answering. Can you briefly say your course, year, and which courses or notations related to modelling you have used?

**Participant [00:51–01:18]:** <!-- T003 -->
I am still part of the old integrated master’s degree in Computer Engineering. I have just submitted my thesis, but I have not defended it yet, so I think I am still considered a fifth-year student. I am not completely finished yet. In terms of what I used, I am not sure how best to situate it.

**Interviewer [01:19–01:25]:** <!-- T004 -->
Which courses were related to modelling, and which notations did you use in those courses?

**Participant [01:27–02:16]:** <!-- T005 -->
Starting with Software Engineering, I think that is relevant. In Software Engineering we dealt a lot with design patterns and testing, such as black-box and white-box testing. Apart from that, I had Modelling of Systems and Processes. In that course we focused much more on models, for example BPMN.

**Interviewer [02:16–02:51]:** <!-- T006 -->
That is the part I am most interested in: modelling, models, BPMN, UML, SysML, or similar notations.

**Participant [02:24–03:05]:** <!-- T007 -->
Exactly. Modelling of Systems and Processes was really focused on modelling before programming and before projects. Software Engineering was more focused on developing projects. I think those two courses are the most relevant. Modelling of Systems and Processes is probably exactly what you are looking for.

**Interviewer [03:05–03:20]:** <!-- T008 -->
Have you used models outside classes? For example, some students use modelling in their thesis to describe how a system works.

**Participant [03:20–04:12]:** <!-- T009 -->
Yes. I used BPMN for my thesis, but BPMN was a notation I learned in MSP. Actually, I learned BPMN in three different courses. One was MSP. The other two were optional or cross-course units. One was an Industrial Management course, where we had BPMN in practical classes. The other was a course from Electrical Engineering called Virtual Enterprises, where we also had BPMN, even before MSP. When I got to the thesis, my supervisors thought it made sense and was useful for me to focus on this area.

**Interviewer [04:12–05:24]:** <!-- T010 -->
So you learned BPMN not only in Computer Science courses, but also in courses from other areas?

**Participant [04:30–05:24]:** <!-- T011 -->
The courses were still related in some way. Industrial Management was more statistics-oriented. They used statistics to detect errors in manufacturing processes and similar contexts. BPMN was useful there because it allowed us to outline the whole process and then look for where errors were happening. In Virtual Enterprises, the goal was to plan what the company was going to do and what we were working with. It was more about planning before the process was actually running.

## BPMN across courses

**Interviewer [05:24–05:47]:** <!-- T012 -->
Did you feel any difference in how BPMN was taught across those three courses? Was there one course that helped you understand modelling in more detail?

**Participant [05:47–07:27]:** <!-- T013 -->
Yes. In Industrial Management, the theoretical classes taught the statistics needed to identify errors, and the practical classes taught methods to outline processes and find those errors. BPMN was only taught in practical classes, for maybe two weeks. It was basically a crash course, not very detailed, and we did not go very deep into modelling.

In Virtual Enterprises, BPMN was similar. It was also a crash course at first, but then we continued using it until the end of the practical classes. It was still not very deep, but we had more time to get used to the modelling itself and to the language.

In MSP, we started using more specific symbols and more specific terminology. I do not want to say the terminology was obscure, but it was definitely more specific to the language.

**Interviewer [07:27–07:37]:** <!-- T014 -->
Did you have those courses before or after MSP?

**Participant [07:34–07:37]:** <!-- T015 -->
Before.

**Interviewer [07:37–07:52]:** <!-- T016 -->
Do you think having those two earlier courses influenced your confidence during MSP?

**Participant [07:53–09:00]:** <!-- T017 -->
Yes, definitely. I felt more comfortable. I was able to overcome several difficulties that one of my colleagues was having. I did most of the course alongside a colleague I had known since secondary school, and we helped each other understand things. Because I already had those two previous contacts with BPMN, I felt much more ahead than my colleague. I was able to help him kick-start the modelling. When I got to MSP, I could skip over a whole part of learning how to assemble the basics and focus instead on the new symbols and the less familiar parts of the notation. So yes, it really impacted my experience.

## Learning process and starting models

**Interviewer [09:00–09:50]:** <!-- T018 -->
When you had to build a new model from a problem, what was your first step? Did you already have a process that worked, or was it mainly trial and error? Some students do not start until the teacher begins solving the first exercise on the board. Did you feel that problem, or did your previous experience help you start immediately?

**Participant [09:50–10:31]:** <!-- T019 -->
In MSP, I remember clearly that I could start the exercises as soon as the professor showed them. I did not need to wait. In Industrial Management, I remember the opposite happening: I had to wait until the professor gave an example to really understand that I was building the model incorrectly. But in MSP, I felt that I could build things fluently and that I did not have problems, at least with the basics.

**Interviewer [10:31–11:14]:** <!-- T020 -->
When you finished a model, how did you decide it was good enough? Did you wait for the professor, compare it with previous examples or classmates, or have a mental checklist?

**Participant [11:14–12:41]:** <!-- T021 -->
With BPMN, I definitely waited for feedback from the professor. I think the professor did not always show the answers, but he walked around the room and checked what people were doing, so you could tell when something was right. I always waited for his feedback to be sure.

As for my own checklist, BPMN is process modelling. Usually the question gives a scenario, sometimes imaginary, and through the model we should be able to explain what the process is doing. My checklist was basically: if I transform the symbols into words, can I read the process described in the question through what I modelled? In other words, can I recover all the requirements from the symbols? My strategy was to transform symbols back into words.

**Interviewer [12:41–12:53]:** <!-- T022 -->
If you completed a model before the professor showed a solution, how comfortable did you feel sharing your approach with colleagues, the professor, or the whole class?

**Participant [12:53–14:05]:** <!-- T023 -->
It depends. At the beginning of the course, I was less comfortable. I am a somewhat shy person, so I am always uncomfortable showing something to the whole class or publicly. But I was quite comfortable showing it to my colleague, the one who was encountering BPMN for the first time.

By the time of the final project, we had to create the full modelling for an application. It was not creating the application itself, but modelling the application. At that stage, I was very comfortable doing the BPMN part by myself and showing it to the other group members. So at the end I was very comfortable; at the beginning, less so.

## Difficult and frustrating experiences

**Interviewer [14:05–14:26]:** <!-- T024 -->
Can you describe a concrete moment when modelling felt difficult, confusing, or frustrating?

**Participant [14:26–16:08]:** <!-- T025 -->
I do not think anything confused me much once I was already in MSP, so I would have to go further back. I think it was in Virtual Enterprises that I realised this modelling language has some similar ways of describing the same thing. For example, there can be two symbols for the same type of gateway: an exclusive gateway can be represented with or without a cross. That caused me some confusion.

Another example is tasks and subprocesses. A subprocess can be expanded, so you can see the subprocess inside the task. The first time I saw that, I was very confused. I wondered whether the subprocess should be considered part of the process I was looking at. This was one of the things I later tested. In my thesis, we had an expanded subprocess, and the goal was to see whether people would get stuck on that subprocess.

I would say that BPMN is fairly intuitive, but until you start to fully understand those details about how the model is built, you will feel stuck a lot of times. It will look like you are doing things right and progressing smoothly until you reach a new part that you are unfamiliar with and get overwhelmed by it, questioning its meaning.

**Interviewer [16:10–16:35]:** <!-- T026 -->
So you believe that the biggest initial problem you felt was notation?

**Participant [16:38–17:48]:** <!-- T027 -->
Yes, the bigger initial problem was notation. Sometimes notation felt ambiguous, or complexity increased when a new, less familiar symbol appeared. The less-known symbols are usually what make people stop. Also, the number of symbols in a model matters. When there are many symbols, it is easy to lose track of the sequence flow. I remember that causing me errors when reading models. It is a visual problem, but also partly a modelling problem, because sometimes everything is modelled on top of everything else.

**Interviewer [17:48–18:08]:** <!-- T028 -->
Have you ever finished a model and still felt insecure because there could be more than one valid answer?

**Participant [18:00–19:07]:** <!-- T029 -->
Yes. I do not know if this is just my way of doing things, but when I am undecided between two options, I usually choose the first one that came to mind. I present the two options to myself and see which one seems to work better. But if they seem equally valid, I choose the first one. I am used to doubting myself and asking whether something is correct, and before I would sometimes change something that was already right into something wrong. So when I am unsure, I go with the first option, as long as it seems correct.

**Participant [19:07–19:54]:** <!-- T030 -->
This happened in Databases. I failed the last test and had to go to the exam because I changed a model. I had done it correctly, then I changed some things because I was unsure, and the changed version was wrong. After that, I decided to trust the first option more, and during the master’s that got much better.

**Interviewer [19:54–20:51]:** <!-- T031 -->
Outside tests, did you also ask for feedback from professors or colleagues?

**Participant [20:15–20:51]:** <!-- T032 -->
Yes. I was thinking in terms of tests. Outside tests, I definitely ask other people for their opinion. I try to talk to professors or to my colleague and ask for their views. If they give me a strong opinion with a plausible justification, I choose based on that justification.

## Tools and modelling experience

**Interviewer [20:51–21:22]:** <!-- T033 -->
How did modelling tools affect your experience? For example, draw.io, Visual Paradigm, or other tools.

**Participant [21:23–23:09]:** <!-- T034 -->
For BPMN, I used Bizagi Modeler. I also used StarUML and Visual Paradigm. For BPMN, I remember Bizagi Modeler feeling better. It is a tool specifically made for BPMN modelling. It lets you add a new process, add lanes to an existing process, add events easily, and connect them easily. It is the tool I used for my thesis. I did not create the thesis models from scratch; I translated the models for the thesis. It was also the tool I used during the three courses for BPMN.

> [Participant demonstrated a live interaction using the software]

**Interviewer [23:09–24:47]:** <!-- T035 -->
Did the tool help you understand BPMN concepts? Did it have syntax checking, follow-ups, templates, or similar support?

**Participant [23:29–24:47]:** <!-- T036 -->
Yes. I do not remember exactly where everything is, but the tool lets us evaluate whether the workflow is valid. For example, if something is connected incorrectly, it can warn us.

> [Note: the participant tries to demonstrate “run workflow”, but he needed an account or subscribe to the free trial.]

The good thing is that it presents a lot of the vocabulary directly in the interface. Since vocabulary is one of the hardest things to learn, this is a relevant kick-start. It also helps with “spelling errors” in the sense of syntax or grammar errors in the model, not spelling errors in the written labels.

**Interviewer [24:50–25:30]:** <!-- T037 -->
Did the tool add extra complexity? For example, learning BPMN is already one task, and then you also have to learn the tool on top of that.

**Participant [25:30–27:13]:** <!-- T038 -->
No, not really. The tool presents construction options in such a simple way that when I first opened it in Industrial Management, I saw the symbols and understood that I just had to drag them into the model. It was very simple and intuitive.

I would even say the tool helped me understand things outside the tool. For example, I remember not understanding the difference between two flows. The tool helped me understand the difference. So in the syntax part, where syntax can be complex because there is diversity, the tool helped.

It also gives intuitive guidance. If you hover the mouse over a syntactic object, it explains what that object does in the diagram. That is great for a beginner. It gives enough help for someone to start modelling.

**Interviewer [27:13–27:45]:** <!-- T039 -->
What could be improved in the tool? More collaboration, templates, more AI-oriented guidance, or suggestions based on requirements?

**Participant [27:45–30:02]:** <!-- T040 -->
In terms of productivity, there are definitely things that could be improved. If we are trying to build a very large diagram, it takes a lot of time because we can only add objects one by one. Then we need to rename objects, add descriptions, and add flows one by one. When the diagram is large, the slowness becomes frustrating.

Another problem may be specific to the version I used. Sometimes, after working for a long time, the tool behaves badly. It may fail to save things properly, save one diagram over another, or paste things together. During my thesis, I once finished modelling a diagram, clicked save, closed it, and when I reopened it there was one diagram on top of another on the same page, and everything was broken. I had to start over. That is serious.

I am not sure if it is a memory issue, but the larger the diagram, the higher the probability of problems. So the tool is great for beginners, but it becomes frustrating when the diagram increases in size. Educationally, it is very good. For productivity, it can be frustrating, although the fact that it is BPMN-specific is already very useful.

**Interviewer [30:02–30:15]:** <!-- T041 -->
Since it is BPMN-specific, it would not necessarily transfer well to another modelling family.

**Participant [30:15–31:49]:**
Yes.

## Course conditions

**Interviewer [31:49–32:56]:** <!-- T042 -->
Did course conditions affect your experience? For example workload, deadlines, projects, tests, and the pressure of several courses at the same time.

**Participant [32:16–33:41]:** <!-- T043 -->
Definitely. In Industrial Management and Virtual Enterprises, the situation was exactly like that. The course itself focused on BPMN for one week in practical classes and then moved on. So it forced us to learn it in a concentrated way and then leave it behind.

In MSP, because I already had previous experience, I was more comfortable moving past the part of gaining basic experience with the tool and BPMN. I already had that preliminary work done.

**Interviewer [33:41–34:28]:** <!-- T044 -->
Did you skip practical or theoretical classes because of pressure from other courses?

**Participant [33:59–34:16]:** <!-- T045 -->
I tried to attend everything. I did miss some practical classes, but not because of pressure from other courses; it was due to personal issues.

**Interviewer [34:16–35:51]:** <!-- T046 -->
When you missed classes, were the online materials sufficient, or did you depend on live explanations?

**Participant [34:28–35:51]:** <!-- T047 -->
It depends. There were things in MSP that I missed, and later I had difficulties. My colleague helped me understand them. I remember having problems with the slides. It is confusing to learn alone, especially considering what we discussed before: wanting feedback from the professor to be sure that we are correct.

The theoretical slides do not always include examples, or they include an example that does not show the full syntax. Even with a complete example, we may still be unsure whether we are doing things correctly, even if we think we are following the slides. Reading the slides alone created problems for me. I was not sure whether I was doing things correctly.

This was not about BPMN. It was another topic that I no longer remember.

**Interviewer [35:51–36:27]:** <!-- T048 -->
Could it have been feature models or metamodels?

**Participant [35:56–36:27]:** <!-- T049 -->
I think so. I had some ease with metamodels because before MSP I had taken a course about metamodels with a professor in that area, although I do not remember the name of the course.

**Interviewer [36:27–36:51]:** <!-- T050 -->
The recording is about to stop, so I will restart it for the last questions.

## Domains, motivation, and authenticity

**Interviewer [00:00–01:11]:** <!-- T051 -->
What types of assignments or domains make modelling feel meaningful or worth the effort? Does the domain affect your motivation to model?

**Participant [01:12–02:46]:** <!-- T052 -->
I am not sure how, or whether, I can answer that. Since BPMN is process modelling, as long as the domain has processes that can be modelled, modelling is possible. I had never really thought that the domain would affect my ability or motivation to model. It is possible that it affects motivation. In university, we are usually protected from domains where we do not have much scientific knowledge.

**Interviewer [02:46–03:21]:** <!-- T053 -->
Usually teachers choose familiar domains, such as events or current-world topics. But if the domain were something unfamiliar or uninteresting, do you think it would affect you?

**Participant [03:24–05:10]:** <!-- T054 -->
Yes, the way you put it makes sense. It is work, and it has to be done. That is how I felt during my thesis when the two models got merged on top of each other and I had to delete everything and do it again. It was work, and I had to do it.

Motivation definitely impacts the speed of work, I would say, but I would not say it impacts the final quality that much. After building the model, I try to read it to check whether it is correct and fix things. So I try to ensure quality even when I am not motivated.

The models I worked with were usually in a restricted or limited domain, mostly companies or business processes. BPMN can model processes outside business, but the work I did was quite limited to business process modelling. So I would say motivation affects productivity more than quality.

**Interviewer [05:11–06:14]:** <!-- T055 -->
Did you ever feel motivated because a model could have real impact or be used beyond the course?

**Participant [06:14–07:16]:** <!-- T056 -->
I would say no, or at least that I never really felt that. Even in my thesis, the models could represent real things, but the models themselves were not going to affect those real things. They were not going to be integrated into systems or used outside the experiment.

They did affect my experiment, the data, and the way the results would be analysed. But in terms of the model itself having impact outside that context, I did not feel that.

**Interviewer [07:16–08:56]:** <!-- T057 -->
What about caring that someone else would analyse or understand your model? Did that motivate you to model more carefully?

**Participant [07:36–08:56]:** <!-- T058 -->
Yes, in that sense I should go back on what I said. That was one of the baselines I had when creating the models for the thesis. They were not perfect, because screen space is limited, but because the eye tracker is not perfect and can drift, I tried to separate the elements on the screen as much as possible. That made the model more readable, and it also helped me later, because with the eye tracker it was easier to distinguish the strategy the participant was using.

So if the question is whether I felt that the way I modelled would affect how other people analysed the model, then yes. I had that concern. I tried to pay attention to that as much as possible.

**Interviewer [08:56–10:38]:** <!-- T059 -->
In professional contexts, modelling is often rarely used, or at least students rarely see it being used. Maybe if modelling were more visible professionally, students would take it more seriously during their studies.

**Participant [09:40–10:38]:** <!-- T060 -->
Yes. I found it interesting to discover that BPMN is used more by armies than by industry. Because different departments inside armies need to model things in the same way, they use a common notation, which ended up being BPMN. I feel companies are either not as concerned with this or use other modelling strategies already known by their employees or engineers, rather than BPMN. This was also a problem for me when trying to find volunteers from our area who knew BPMN.

## Desired teaching changes

**Interviewer [10:38–11:07]:** <!-- T061 -->
If you could change one realistic thing about how modelling is taught, what would help you the most? More examples, more explicit steps, better feedback, different tools, more time?

**Participant [11:07–13:09]:** <!-- T062 -->
What helped me the most with BPMN was having multiple points of contact with it. The more it is used, the more people remember it and discover its different parts. I do not think simply extending the time is very feasible. We could replace other things with more modelling, but that depends on what kind of Informatics area or modelling-focused area we want.

If we do not want to change what MSP teaches, but only how it teaches, then I would say the practical exercises should be better connected to the theoretical slides. Students should have their first contact with what is correct, and with doing things correctly, in the theoretical slides. Complete examples would be very useful.

Then, when moving to practical classes, assuming students already understand the basics, the course could start adding the less familiar syntax. That would help.

## Closing

**Interviewer [13:09–13:31]:** <!-- T063 -->
Is there anything important about learning modelling that I did not ask but that you think I should have asked?

**Participant [13:31–13:47]:** <!-- T064 -->
I do not think so. I gave examples as I talked.

**Interviewer [13:47–14:15]:** <!-- T065 -->
Thank you. This was very useful. If needed, I may contact you later for a small clarification by email.

## Anonymisation note

Identifying and personal data have been redacted, including named professors. Degree programme and course acronyms are retained where analytically relevant.
