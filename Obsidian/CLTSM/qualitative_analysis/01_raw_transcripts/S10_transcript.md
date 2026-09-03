---
case_id: S10
role: student
version: cleaned
timestamp_style: none  # none | start | range
---

# Interview S10 Transcript

`Interviewer` = interviewer  
`Participant` = case participant

## Cleaning notes

This transcript was translated from Portuguese (see [[pt/S10_transcript_pt]]) and cleaned for readability and consistency with other cleaned student transcripts. Consent filler, repetitions, and interviewer filler were reduced where they did not affect meaning. Interviewer questions were tightened for clarity. Grammar was lightly edited for readability without intentionally changing meaning.

For publication-level verbatim quotations, verify the wording against the Portuguese original and the audio.

## Part 1 — Background, modelling experience, and a translation incident

**Interviewer:** <!-- T002 -->
Can you briefly explain your relationship with software modelling — where you learned it, where you used it, and in what context?

**Participant:** <!-- T003 -->
Yes. I studied Informatics at IST. I finished the degree about a year and a half ago, so I still remember reasonably well. I had modelling in some courses, mainly Systems Analysis and Modelling (Análise e Modelação de Sistemas), but even before that we already had class diagrams and databases. Then in the master’s and in the thesis I also went back to using some concepts, although already in a less rigid way.

**Interviewer:** <!-- T004 -->
When you say less rigid, do you mean you were no longer necessarily using the correct notation?

**Participant:** <!-- T005 -->
Yes, basically. In the thesis, for example, I made diagrams to explain the architecture and some interactions, but I was no longer worried about whether everything followed UML one hundred percent. It was more important to communicate the system well.

**Interviewer:** <!-- T006 -->
Going back to university, can you remember one concrete moment when you really had difficulty, confusion, or frustration with modelling?

**Participant:** <!-- T007 -->
Yes. I remember a situation in the modelling project. I do not remember the domain exactly. I think it was something related to reservations or services, but I remember the problem.

We had first done part of the process in BPMN and then we had to represent the system with other models. I got quite confused with an external entity. I think it was a payments service.

In BPMN we had placed that as an external participant, in a separate pool, and it was quite clear. Then when we moved to UML I did not know exactly how to represent the same thing.

**Interviewer:** <!-- T008 -->
Was the difficulty that you did not know which symbol to use, or that you did not know conceptually where to put that entity?

**Participant:** <!-- T009 -->
More the second. Because I understood perfectly what the service did. The problem was understanding whether it should be an actor, a class, an external component, or simply not appear in that diagram. And I remember losing quite a bit of time on that because I was trying to do a translation that was too direct from BPMN.

**Interviewer:** <!-- T010 -->
So you had something in BPMN and you felt you had to find an equivalent in UML?

**Participant:** <!-- T011 -->
Exactly. And that was not how I should have been thinking.

**Interviewer:** <!-- T012 -->
How did you realise that?

**Participant:** <!-- T013 -->
I think it was in a practical. I asked the teacher after class. I did not usually ask much during the class, especially if there were still a lot of people in the room. I normally waited a bit until the end.

He basically explained that the models were answering different questions. In BPMN it mattered to show that there was communication with an external participant during the process. In a class diagram that might not even be relevant. That unblocked the situation quite a lot.

**Interviewer:** <!-- T014 -->
Did you have to redo the model? About how long had you lost before asking? Was it frustrating?

**Participant:** <!-- T015 -->
Not completely. That one was more a local adjustment. We removed some things we had tried to carry directly from BPMN into the class diagram and we reorganised two or three relations. But it was not starting from scratch.

I do not know exactly. Maybe a couple of hours. Not two hours continuously on that one arrow, obviously, but we were working on the model and we kept coming back to that doubt. And there was also that thing of each person in the group having a different opinion.

A bit frustrating, yes. Because it was not a difficulty of not understanding the system. We knew what happened. It was more that feeling of “I know what I want to say but I do not know the correct way to say it in this language.”

**Interviewer:** <!-- T016 -->
When you changed from one modelling family to another, for example BPMN to UML or UML to SysML, did you often feel that? Can you give a concrete example of what carried over and what practically had to start from scratch?

**Participant:** <!-- T017 -->
Yes, but then you get used to it. Initially I treated the models almost as if they were different versions of the same thing. Then I realised they were not. Some information carried over, some did not.

In that reservations example, what carried over quite well were the main concepts. We already knew there was a client, a reservation, a payment, maybe an employee, and certain important operations. So the names of the things and some responsibilities of the system were already identified. The requirements also helped quite a lot because they were more or less independent of the model.

What did not carry over was the structure. In BPMN we had the sequence of the process. First this happens, then this, there is a decision, then there is a message to another participant. That does not automatically tell you how to create the classes. A gateway does not become a class. A lane does not necessarily become an object. A task also does not automatically correspond to a method. I think that is exactly where we had confusion.

**Interviewer:** <!-- T018 -->
So you did try to do that mapping almost one-to-one? In that case something had to restart?

**Participant:** <!-- T019 -->
Yes, initially. And it became a quite bad model. We had classes that were actually actions only because they appeared as tasks in the process. Then we had to look again at the system description and think more in terms of entities, responsibilities, and relations.

Yes. Not all the work, because the domain knowledge was already there. But the reasoning had to restart. We could not simply convert the previous diagram.

**Interviewer:** <!-- T020 -->
Did they teach any kind of traceability, for example this requirement relates to this use case, this BPMN element relates to this part of the UML?

**Participant:** <!-- T021 -->
Yes, I remember them talking about traceability. Especially requirements to system elements. I think in the tool you could also create relations between requirements and other elements. But being honest, I do not remember us doing very rigorous traceability across all the models.

## Part 2 — Labs, sharing, and project feedback

**Interviewer:** <!-- T022 -->
In the practicals, how did the exercises normally work? Did people go to the board? Did you go?

**Participant:** <!-- T023 -->
Normally the teacher explained the material and then there was an exercise with a short description of a system. We tried to solve it on paper or on the computer, depending on the class. Then someone presented the solution. Yes, they went to the board.

If they called me. Voluntarily I think I went once or twice at most.

**Interviewer:** <!-- T024 -->
Why? If you had a ready solution and you knew it was probably correct, would you still not volunteer?

**Participant:** <!-- T025 -->
I do not like speaking to a class very much. It was not exactly fear of being wrong. It was more not liking that situation of having twenty or thirty people watching while I am still trying to think. Probably I still would not volunteer.

**Interviewer:** <!-- T026 -->
When the teacher said “does anyone want to come and solve this?”, what did you do? Did you try to solve it, or wait for the solution? If you had a different solution, did you ever interrupt and say you had done it another way?

**Participant:** <!-- T027 -->
I stayed quiet. No, I normally solved it. I did the exercise in my notebook and then compared it with what appeared on the board.

I tried to understand whether mine was wrong. If it was a small difference I said nothing. If it was something I really did not understand, I would probably ask the teacher at the end. I very rarely interrupted with “teacher, I did this another way.” Maybe if someone was already discussing the same thing. Then it was easier to join the conversation. Starting the discussion myself, no.

**Interviewer:** <!-- T028 -->
Did that ever hurt your learning? For example you had a doubt but because you did not want to ask, you ended up not resolving it. Was sharing a solution of yours with the class uncomfortable?

**Participant:** <!-- T029 -->
Yes. Especially small doubts. Because if it was something that really stopped me from continuing, I asked. But if it was something like “should this arrow be this way or that way?”, sometimes I simply waited for the correction, asked a classmate, or later ended up searching.

Yes, a bit. Sharing with two people from my group, no. Showing the teacher was also not terrible if it was individually. Putting it on the projector or going to the board with a solution I still did not know was right, that I did not like.

**Interviewer:** <!-- T030 -->
And when you were chosen at random? Did the teacher help while you were at the board, or let you get to the end?

**Participant:** <!-- T031 -->
I went. It was not a drama. But I probably talked less than other students. I did the drawing and answered what the teacher asked. I was not there trying to explain to the whole class.

I think it depended. Normally he let you go on a bit. If you were completely blocked he asked a question to guide you. I do not remember anyone being humiliated or anything like that. That helped.

**Interviewer:** <!-- T032 -->
On feedback, did you feel it was useful, or often too late?

**Participant:** <!-- T033 -->
In the project it was useful. In the practicals it was immediate, so it was easy to correct. In the project it already depended on the moment. We had deliveries and then there was feedback. I remember in one of them the teacher pointed out that we were mixing two perspectives in the same model. I think it was BPMN. We had represented a part of the internal system almost as if it were an independent participant, when in reality it made more sense for it to be inside the organisation.

**Interviewer:** <!-- T034 -->
Pool and lane?

**Participant:** <!-- T035 -->
Yes, exactly. I think we had one pool too many. And then some messages were modelled as message flows when they should have been sequence flows because they were inside the same participant.

**Interviewer:** <!-- T036 -->
After that feedback, what happened to the model? If you had to classify it: small fix, local rewrite, or abandon completely? Did you have time to apply that feedback? Did it change how you made later models?

**Participant:** <!-- T037 -->
That one we had to change quite a lot, but not abandon. It was a large local restructuring. We changed pools and lanes, and obviously when you change that you have to touch several arrows and events. But the business process itself stayed almost the same. Local rewrite.

Yes. I think there was still quite a bit of time left before the second delivery.

It changed a bit. After that I started checking the system boundary better before starting. Who is really external, who belongs to the organisation, what is the system I am representing. Because that error had come from starting to draw straight away without defining that very well. Nothing very formal. But before starting another BPMN I asked those questions mentally.

**Interviewer:** <!-- T038 -->
And notation feedback, for example a wrong arrow, did that also result in later changes?

**Participant:** <!-- T039 -->
Yes, but that was more mechanical. If they corrected the same thing twice I eventually memorised it. The part that really stayed was the conceptual feedback.

## Part 3 — AI, group work, quality criteria and closing

**Interviewer:** <!-- T040 -->
Did you use AI for those courses or for modelling tasks at university? How?

**Participant:** <!-- T041 -->
Yes. Mainly to confirm things. For example I made a model, took a screenshot, and asked whether it saw any obvious problem. Or I asked whether a relation was correctly represented.

**Interviewer:** <!-- T042 -->
You actually sent screenshots of the model? Can you give an example of a question you asked?

**Participant:** <!-- T043 -->
Yes. A screenshot and normally also a short description of the system, because if you send only the diagram without context it can interpret things badly.

Something like: “Is this X service external or internal to the system? Does it make sense for it to be represented as an actor in this use case diagram?” Things like that. Small doubts. I never asked “make me the model of this whole system.” I did not trust that that much. If you ask for a whole model it can generate something that looks quite convincing, but then you still have to check everything. And in a modelling course that also defeated the purpose a bit.

**Interviewer:** <!-- T044 -->
Besides notation, did you use it for concepts, or to understand next steps? Did you use it for cross-notation translation, for example “here is BPMN, now transform this into UML”?

**Participant:** <!-- T045 -->
Yes. Sometimes I forgot the difference between aggregation and composition, or between certain types of message in a sequence diagram. Instead of searching through the slides I asked directly.

Yes. For example I had a set of requirements and a diagram and I asked something like: “What would normally be the next useful model to validate these interactions?” And it might suggest a sequence diagram for two or three main use cases. It was not doing it. It was more to organise the process. More or less like a classmate you go to in order to validate a doubt. But a classmate you have to distrust.

Not to transform directly. But yes to ask what should carry over. For example: “I have this BPMN and now I need to make a sequence diagram. What information from this model is relevant?” Or “which of these tasks represent interactions worth detailing?” That helped.

**Interviewer:** <!-- T046 -->
Going back to the university project, what was it like working in a group for you, given that you say you are more reserved? How did you divide the modelling families?

**Participant:** <!-- T047 -->
In a small group I have no problem. It is completely different. With two classmates I can discuss normally. The problem is more presenting to a lot of people.

Initially we tried to divide. One person did BPMN, another requirements, another UML. But we realised that did not work very well, because the models started to diverge. The person doing BPMN interpreted a rule one way and the person doing UML interpreted it another way. Then we had two versions of the same system.

**Interviewer:** <!-- T048 -->
So you changed the process? Was that formal, or something you invented? Did it work? In the defence, did the teacher ask people individually?

**Participant:** <!-- T049 -->
Yes. We still had one person responsible for making the first draft, but the others had to review. And before starting another model we discussed for five or ten minutes what should carry over from the previous one. That was ours. I do not remember the teacher telling us to do it that way.

Yes. Mainly because it forced whoever had not made that model to understand it. It also helped for the defence. I think the teacher did ask individually. You could not have one person do everything and the others stay quiet.

**Interviewer:** <!-- T050 -->
Did that create stress? Did knowing you would have to explain change the quality of the model?

**Participant:** <!-- T051 -->
A bit. I knew how to explain what we had done, but I never liked not knowing which question was coming next.

Yes. Mainly simplifying. Sometimes we made a very loaded model and then when we tried to explain we realised that even we could not follow it easily. So we split it or removed things that did not add much. If three people who made the model had difficulty explaining it, it was probably too complicated. I do not know whether the teacher called it that, but in practice explainability was a quality criterion.

**Interviewer:** <!-- T052 -->
When you received feedback from the teacher in person, did you prefer that to written feedback? Did you find it easy to go and talk to the teacher?

**Participant:** <!-- T053 -->
Yes, because you could ask straight away “but why?”. Written feedback like “incorrect relationship” does not help me much. I think we did get some written notes, but I remember the discussions more.

If it was alone or with the group, yes. During the whole class it was harder. A bit from embarrassment. Also from not wanting to ask a basic question and interrupt the class. Even if the doubt might be shared by other students. I know that rationally it does not make much sense, but that is how it was.

**Interviewer:** <!-- T054 -->
Did the teachers do anything to make it easier for students who did not want to speak to the class?

**Participant:** <!-- T055 -->
In the practicals they walked around the room sometimes. That helped quite a lot. If the teacher comes by your desk and asks “is everything all right?”, it is much easier to show what you are doing than to raise your hand in front of the class. For me that kind of proactive feedback was definitely better.

**Interviewer:** <!-- T056 -->
When you had a finished model and no teacher was available, how did you decide it was good enough? Did you have a checklist? Where did AI fit in that checklist?

**Participant:** <!-- T057 -->
First I compared with the assignment text. Then I checked whether I had used the notation correctly. In the project I showed it to classmates. And sometimes there I already used AI as well.

I do not remember an official checklist. Ours was almost: “Is everything the assignment asks for there?” “Is there something in one model that contradicts another?” “Can we explain this?”

Normally after I had checked it myself. First I made the model and reviewed it. Then I might send a screenshot and context and ask it to find inconsistencies or strange notation. Then I checked the suggestions again. It did not replace the self-check. It was more a second opinion. If the AI and I disagreed, I went to the slides or the documentation, or I asked the teacher, especially if it had an impact on the project.

**Interviewer:** <!-- T058 -->
Do you think having AI available changed how you participated in the practicals? Positive or negative?

**Participant:** <!-- T059 -->
Yes. I probably asked the teacher even fewer small doubts. Both. It was positive because I did not stay blocked. But sometimes the discussion with the teacher taught more. So ideally AI should guide and not simply deliver the answer.

**Interviewer:** <!-- T060 -->
If you could change one realistic thing about how modelling was taught, without inventing a completely new course, what would you change?

**Participant:** <!-- T061 -->
Use the same case study for longer. Start with requirements, then process, then UML, maybe SysML, and keep showing clearly what we are reusing and what we are rethinking.

And maybe give a more private way to check models during the practicals. It could be the tool doing some validation, or a tool with AI. Not to generate the model. Only to say things like “this relation is not valid in this notation”, “this requirement apparently is not covered”, or “you have an element in model A that contradicts model B.” For students like me it would be useful because I could check some doubts before showing them to the class or the teacher.

**Interviewer:** <!-- T062 -->
Do you think that would make you produce better models?

**Participant:** <!-- T063 -->
I think so. Mainly because I would receive feedback earlier. If you only realise a problem after the delivery, you can learn for the next one, but you no longer improve that piece of work. If you realise while you are still building, you can still correct it.

**Interviewer:** <!-- T064 -->
Thank you. This was very helpful.
