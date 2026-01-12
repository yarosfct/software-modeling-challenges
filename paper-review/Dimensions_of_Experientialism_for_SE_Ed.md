# Holmes, Allen and Craig — "Dimensions of Experientialism for Software Engineering Education"


## 1. Problem and Motivation (Sec. 1)

- There's a **gap between classroom SE education and workplace practice:**
  abstract concepts vs. messy reality (legacy systems, tools, processes, users, teams).
- The **UCOSP (Undergraduate Copstone Open Source Projects)** program was created to close this gap by giving students a **course-based, real-world-like SE experience:**
  - students from many Canadian universities,
  - work on **existing open-source projects,**
  - in **distributed teams,**
  - mentored by **real project developers.**

**Goal of the Paper:**
Understand how students perceive UCOSP as **complementting traditional coursework,** and derive **"dimensions of experientialism"** useful for curriculum design.

## 2. UCOSP Program in a Nutshell (Sec. 2.4)

- Running **8+ years,** with **737 students** from **30 universities.**
- Each term:
  - UCOSP recruits **open-source projects** with real users and active dev communities (e.g., ReviewBoard: ~600k, >8000 commits, 181 contributors).
  - Students (3rd/4th year, selected strong students) apply, get **course credit** at their home institution.
  - A **home supervisor** meets them biweekly; most of the **technical mentorship** is done by **project mentors.** 
  - Program starts with a **3-day face-to-face sprint,** then continues online (issue trackers, VCS, chat, video calls, etc.).

UCOSP is deliberately built to provide **three "real" aspects:**

1. **Real projects** (existing systems, real users, OSS communities).
2. **Real tasks** (novel contributions that must be deployed).
3. **Real mentors** (actual project developers).


## 3. Methods: Longitudinal Qualitative Study (Sec. 3)

**Research question:**
> How do experimental software development projects augment traditional CS curricula?

**Participants and data:**

- **167 students** from **18 Canadian universities**, surveyed over **6 academic terms** (2013 - 2016).
- Three serveys per term:
  - Pre-program (preferences, background),
  - Post-sprint,
  - **Post-program** (main focus of this paper).
- Post-program questionnaire: 8 open-ended questions (Q1-Q8) about what they gained, differences vs prior courses, motivation, skills, useful/useless aspects, etc. (Table 1).

**Analysis:**

- Responses split into **2,203 "card"** (roughly one sentence each).
- **Grounded-theory style open coding:**
  - cards coded per question,
  - codes merged across questions,
  - 5 **high-level themes** identified:
    1. Real Projects
    2. Real Tasks
    3. Real Mentorships
    4. Soft Skills
    5. Technical Skills
- Inter-rater reliability check on a subset: **Krippendorff's a = 0.87** -> agreement.

## 4. Key Findings — Three Dimensions of "Experientialism" (Sec. 4)

### 4.1 Real Projects (legacy OSS systems and communities)

Students valued working on **large, real codebases** with existing architecture, technical debt and conventions:

- They mention learning to **navigate massive project**, trace behaviour, avoid duplicating code, and manage branches.
- They explicitly contrast this with **greenfield toy assignments** in regular courses.
- OSS context matters:
  - They learn **how to join an OSS project,**
  - how to communicate with a community,
  - how contributions are integrated,
  - and experience **real tool and processes** (issue trackers, CI, testing, code review, etc.).

Students report that this exposure gives them a more realistic view of **complexity, process, and collaboration** than typical coursework.

### 4.2 Real tasks (novel features with real impact)

Tasks in UCOSP are **not throwaway assignments:**

- Students implement **novel functionality** that:
  - is **non-trivial,**
  - is expected to be **merged and deployed,**
  - and is used by **"thousands of real users."**
- This perceived impact is a strong motivators:
  - they contrast it with assignments "just for the grade" or "just for the sake of doing it".
- Tasks often don't have a guaranteed clean solution:
  - dependencies on other project, moving targets, and uncertainty are considered "**OK**", unlike standard course assignments where there is always a neat solution by design.

This "real-tasks" aspect trains students in **practical problem solving, dealing with uncertainty, and self-motivation.**

### 4.3 Real Mentors (embedded project developers)

UCOSP students are mentored primarily by **existing project developers,** not just TAs or instructors:

- Mentors:
  - assign tasks,
  - provide **code reviews,**
  - guide debugging and program understanding,
  - integrate students into the **community of practice.**
- Students highlight:
  - high-quality **feedback via code review,**
  - emphasis on **code quality,** not just functionality,
  - learning "how things are done in practice" (processes, communication, expectations).
- Mentors also bring **tangential benefits:**
  - networking / professional contacts,
  - portfolio (public GitHub contributions),
  - role models for professional behaviour.

This "real mentors" dimension is what ties projects and tasks into a coherent **experimential learning environment.**


## 5. Other Themes: Soft and Technical Skills (Sec. 4.4)

### 5.1 Soft Skills

Students report gains in:

- **Communication** (especially remote/asynchronous, written explanations of problem and solutions).
- **Teamwork and collaboration** in distributed settings.
- **Time management and self-motivation:** Tasks cant be done last-minute; other depend on their work.
- **Career-related benefits:**
  - resume building (public OSS contributions),
  - career planning,
  - "job-like" motivation (peer approval, contribution to a team).

### 5.2 Technical Skills

Expected, but still important:

- New **languages and frameworks** (Go, Rails, etc.).
- **Testing frameworks**, CI, deployment skills.
- **Version control strategies** (branching, merging, pull requests).
- **Program comprehension** in unfamiliar, large codebase.

The concrete skills are perceived aas **more authentic** than in regular lab courses.

## 6. Curriculum implications and limitations (Sec. 5-6)

### 6.1 Cross-cutting insights (Sec. 5.1)

The authors argue that the **three dimensions work best together:**

1. **Real processes and tools**
   - Students really internalise version control, issue tracking, CI, code review when these are **used for real work,** not just simulated.
2. **Providing real value**
   - Because mentors need actual contributions, tasks are meaningful and mentors are motivated to engage seriously.
3. **Mentorship as central glue**
   - Mentors connect students to community practices, enforce quality, and make sure real tasks are feasible.

They discuss that partial implementations are possible (e.g., only real projects), but **benefits and mentor motivation drop** if any dimension is missing.

They suggest that a single institution could design an experiential capstone with:

- OSS or industrial projects,
- remote mentors from companies/communities,
- students doing novel features that are actually deployed.

### 6.2 Threats and scalability (Sec. 5.2, 6)

- **Selection bias:** UCOSP admits **strong, self-motivated students;** it's unclear if the model scales to the general population.
- **Resource-intensity:**
  - expensive (funding, logistics for sprints),
  - mentor time is limited,
  - program reaches relatively **few students** each year.
- Results are based on **self-reported perceptions,** not directly measurement of learning outcomes.

## 7. Thesis-ready one-paragraph summary

Holmes, Allen and Craig qualitatively analyse 2,203 survey responses from 167 students who participated in the multi-university UCOSP capstone program, in which students work on existing open-source systems in distributed teams under the mentorship of project developers. Using grounded-theory-based open coding, they derive five themes, of which three constitute key "dimensions of experientialism": real projects (large, legacy OSS codebases and communities), real tasks (novel, non-trivial features that are actually deployed for real users), and real mentors (embedded project developers who provide code review, guidance, and socialisation into community practices). Students perceive that this combination provides much richer understanding of software engineering than traditional courses, improving their ability to work with complex systems, follow real processes and tools, and develop both soft skills (communication, teamwork, time management, career planning) and technical skills. The authors argue that these three dimensions are mutually reinforcing and that experiential capstone courses should, wher possible, include all three to maximise authenticity and learning, while acknowledging issues of selection bias, cost and scalability.


