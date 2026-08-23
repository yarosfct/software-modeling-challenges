# Follow-up student interviews — IST & ISEL (theoretical sampling)

Sampling guides for new Portuguese-university student interviews after the first-cycle findings map (10 cases: S1–S6, L1–L4). Use alongside [`pilot-student.md`](pilot-student.md) **Guide C**; this file is the triage layer — what to protect, what to skip, and a run script for ~25–30 minutes.

**Cases planned:** IST (Técnico) student, then ISEL student(s).  
**Language:** English or Portuguese (participant preference). Reuse consent language from `pilot-student.md` §2; pt-PT phrasing can follow Guide B/C appendix style.

**Honesty:** These interviews densify open questions and thin categories. They do **not** claim saturation.

---

## 1. Why these interviews (map weaknesses)

Source of truth for the map: `Obsidian/CLTSM/qualitative_analysis/04_cross_case_analysis/findings_map_guide.md` and `category_inventory_working.md`.

### Strong enough already (do not over-spend time)

- Teacher examples unlock work (CAT3) — unless they contradict L4 discovery / withhold-examples stance
- Symbol overload as a generic complaint (CAT2) — keep short unless a vivid incident
- AI as explainer not generator (CAT13) — brief check is enough if they barely use AI
- “Semantic checking is nice” as a wishlist without a concrete incident

### Priority gaps to address

| Priority | Gap | Map link | What “good evidence” looks like |
|---|---|---|---|
| 1 | Wait-to-start vs self-start | PH1 / open Q: lecturer vs student | Concrete first-10-minutes story: wait for demo / draft alone / hunt prior example / prior-course contact |
| 2 | Refine / rework vs only late feedback | RQ1 gap / open Q | After feedback: small fix, full rebuild, or nothing because too late — and why |
| 3 | Feedback access (initiative; public vs private) | CAT6 / PH2 | How they actually got comments in a large UC; shy vs comfortable sharing unfinished work |
| 4 | Course load / theory–practice / materials | CAT11 | Concurrent UCs, missed aulas, slides-only catch-up, continuous assessment pressure |
| 5 | Group kill or save | CAT9 / PH4 | Who owned the diagram; code-first drop vs stand-ups / shared board |
| 6 | Cross-notation transfer | CAT14 (S6-heavy) | **Only if** Q1 shows ≥2 families or RE→UML — what carried over vs starting over; lost traceability |
| Park | Abstraction as root deficit | Parked (lecturer_interp) | Do **not** ask “are you bad at abstracting?” Only code if they volunteer difficulty choosing what to leave out |

### Why IST then ISEL

- **IST (Técnico):** large engineering cohorts → high yield on CAT5/CAT6 (feedback at scale) and wait-to-start under demo-heavy labs.
- **ISEL:** second Portuguese institutional context → constant comparison on CAT11 (load, attendance, materials) and feedback culture without needing a new country.
- Keep the **same question spine** across both so memos compare cleanly.

---

## 2. How this relates to Guide C

| Use | Source |
|---|---|
| Consent, intro, generic probes | `pilot-student.md` §2 |
| Question wording backbone | Guide C (Q1–Q16) |
| Time triage for **these** interviews | This file §3–5 |
| Coding / memos after | `Obsidian/CLTSM/qualitative_analysis/stgt_coding_memo_habit.md` |

**Rule:** Semi-structured. If a gap theme opens early (e.g. rework, shy public board), stay there and cut later blocks. Do not ask every Guide C probe.

**Suggested case IDs after transcription:** next free student IDs (e.g. S7, S8…) under `01_raw_transcripts/` — do not invent quotes in memos.

---

## 3. Success criteria (leave with ≥3)

After each interview you should be able to memo at least **three** of:

1. Waited / didn’t wait / depended on prior contact (PH1)
2. Reworked vs never reworked after feedback (RQ1 open)
3. Real feedback path in their UC (CAT6 / CAT5)
4. Group killed or saved the model (CAT9)
5. Multi-notation translation pain **only if present** (CAT14)
6. Load / missed class / slides vs live practice (CAT11)

You do **not** need another generic “examples help a lot” story unless it **negates** or **bounds** CAT3 (e.g. examples withheld, examples don’t transfer).

---

## 4. Profile triage (first 2 minutes)

From Q1, pick the gap pack:

| If they mention… | Emphasise | De-emphasise |
|---|---|---|
| Large cohort / lab / TA | Q12 feedback, Q7 sharing, rework custom | Long tool brand lists |
| Only one notation (e.g. UML only) | Q3, rework, Q7, Q10, CAT11 | Q8/Q9 (CAT14) |
| Several notations or RE / iStar / BPMN+UML | Q8 + Q9 (CAT14 densify) | Drop Q14 first if short |
| Group project / LEIC-style project | Q10 deeply | — |
| Active ChatGPT use | Q11 briefly | Don’t force if none |
| Thesis / internship modelling | Q13 audience; Q14 short | — |

---

## 5. Run script — IST student (~25–30 min)

Follow this order. Exact ask-lines are ready to read; probes are optional.

### 0. Opening (30–45s)

> Thanks for meeting with me. I’m studying how students learn software modelling in higher education — what feels difficult, what helps, and how teaching, tools, and course conditions shape that. I’m especially interested in concrete situations: how you start a model, how you get feedback, and whether you ever really rework something after comments.
> With your permission I’ll record. About 25–30 minutes; you can skip any question. Answers are anonymised in the thesis (GDPR). English or Portuguese — your choice.

*(Confirm recording + language, then start.)*

### 1. Setup — Guide C Q1 (1–2 min)

**Ask**

* “Briefly: programme, year, and which modelling-related courses or notations you’ve used (UML, BPMN, ER, requirements models, architecture diagrams, etc.)?”

**Probe if needed**

* “Same notation in more than one course, or several different families?”
* “Any modelling in a thesis, internship, or job?”

*Note profile → §4 triage. If multi-notation/RE, protect time for Q8/Q9 later.*

### 2. Incident — Guide C Q2 (3–4 min)

**Ask**

* “Walk me through **one concrete moment** when modelling felt difficult, confusing, or frustrating — one assignment or lab, not a general opinion.”

**Probes**

* Task? What exactly was hard (start / notation / tool / feedback / group / domain)?
* What did you do next?

### 3. Start gate — Guide C Q3 **[PRIORITY 1]** (3–4 min)

**Ask**

* “When you get a text description and must build a model, what happens in the **first ten minutes**? What’s your first move?”

**Probes (use freely)**

* “Process, or mostly trial and error?”
* “If the teacher hasn’t shown an example yet, how confident are you starting alone?”
* “Do you tend to wait for a demonstration before you feel comfortable proceeding?”
* “Did prior contact with that notation in another course change how you started?”

*Memo target: wait / self-start / prior-contact — compare to L1M1, L2, S5M3, S3M1.*

### 4. Examples — Guide C Q4 **short** (1–2 min unless contradiction)

**Ask**

* “When a teacher solves an example on the board, what does that actually help you with?”

**Probes only if thin**

* Notation vs reasoning vs “expected answer shape”?
* Transfer to a similar task alone, or need another example?

*Cut early if they only repeat “examples help.”*

### 5. Good enough — Guide C Q5 (2–3 min)

**Ask**

* “When you finish a model, how do you decide it’s good enough?”

**Probes**

* Checklist / rubric taught? Compare to classmates or past solutions?
* “There’s no compile button — what replaces that for you?”

### 6. Rework — **custom block** **[PRIORITY 2]** (2–3 min)

*(Not a full Guide C item — protect this.)*

**Ask**

* “After you got feedback on a model — mid-course or at the end — what did you **actually change**? A small fix, a full rebuild, or nothing because it was already too late?”

**Probes**

* “Have you ever thrown away a first version and restarted on purpose?”
* “If you didn’t rework, was that because of time, grading only on the final, or you felt it was already fine?”
* “Did early choices (e.g. what counts as a class vs attribute) stick even when you later doubted them?”

*Memo target: dedicated refine/rework challenge vs only late-feedback stakes (open Q1).*

### 7. Sharing / feedback access — Guide C Q7 (+ scale) **[PRIORITY 3]** (3–4 min)

**Ask**

* “If you finish a model before the teacher shows a solution, how comfortable are you sharing your approach?”

**Probes**

* Classmates / teacher privately / whole class?
* What makes you hesitate?
* **IST large-course:** “In a big UC at Técnico, what feedback did you **really** get on models — professor, TA, peers, forum, automated check, or mostly nothing until the end?”
* “Did detailed comments only happen if you asked?”

*Memo target: CAT5 timing + CAT6 initiative/format; shy vs outgoing (S4 vs S5).*

### 8. Selective gap pack (5–7 min) — pick 1–2

#### A. Group — Guide C Q10 *(if project work)*

* “In group projects, who actually built and owned the model?”
* “Did modelling help the team, or become overhead / get dropped for code?”
* “Anything (pairs, shared board, stand-ups) that kept the diagram alive?”

#### B. Cross-family / RE — Guide C Q8–Q9 *(only if Q1 qualifies)*

* “What carried over between notations, and what felt like starting over?”
* “Harder to move from goals/requirements models to something like UML? What got lost?”
* Vague briefs / role-play / justify each element?

#### C. Tools + load — Guide C Q12 *(always useful at IST)*

* Tools: help vs friction (keep short).
* “If you missed classes, were slides enough, or did you need live explanation?”
* Workload / continuous assessment vs time to iterate on models?

#### D. AI — Guide C Q11 *(brief)*

* Create / explain / check? Helpful feedback or shortcut?
* Would you want a tool that explains or validates — without drawing the homework for you?

#### E. Audience — Guide C Q13 *(if thesis/real reader)*

* Did knowing a supervisor/client would read it change care/layout?

### 9. Close — Guide C Q15–Q16 (2 min)

**Ask**

* “If you could change **one realistic** thing about how modelling is taught, what would help most?”
* “Anything important I didn’t ask?”

> Thank you — this was very helpful. May I contact you later for a short clarification if needed?

---

## 6. Run script — ISEL student (~25–30 min)

**Same spine as IST** (Q1 → Q2 → Q3 → Q5 → rework → Q7 → selective → close).

### Emphasis shifts for ISEL

| Keep identical | Push harder | Only if present |
|---|---|---|
| Start gate (Q3), rework custom, sharing (Q7) | CAT11: concurrent UCs, attendance, slides vs labs, continuous evaluation | CAT14 via Q8/Q9 |
| Incident Q2 | Local feedback culture (office hours, Discord, lab) vs end-of-UC only | — |
| Group Q10 if projects | Compare lightly to IST only in **your memo**, not in the interview (“at another school…”) | — |

### Wording tweak for Q7 / load

**Ask**

* “In your modelling-related UCs at ISEL, how did feedback on diagrams actually work?”
* “When several UCs peak at once, what happens to modelling work — still careful, or ‘just finish it’?”

Do **not** ask them to compare IST vs ISEL unless they volunteer multi-school experience.

---

## 7. Time triage (both interviews)

**Always protect:** Q2, Q3, rework custom, Q5, Q7, Q12 (feedback/load slice).

**Drop first:** Q14; long tool lists; executable-UML probe; Q6 if Q5 already covered uncertainty; Q4 if examples already saturated.

**If only 20 minutes:** Q1 → Q2 → Q3 → rework → Q7 (+ large-course feedback) → Q15.

---

## 8. Interviewer don’ts

* Don’t teach your phenomena (“so the teacher is like a compile button…”).
* Don’t probe abstraction as a personal deficit.
* Don’t force CAT14 / iStar talk on a UML-only student.
* Don’t spend half the interview on vendor tool names.
* Don’t merge student self-report with what lecturers say students do — memo voice labels later.
* Don’t invent quotes; use turn IDs after transcription.

---

## 9. After the interview (vault)

1. Transcribe to `Obsidian/CLTSM/qualitative_analysis/01_raw_transcripts/{Case}_transcript.md` with `<!-- Tnnn -->` markers.
2. Open-code under `02_first_cycle_coding/{Case}/` per habit note.
3. Write short memos in `03_memos/` aimed at the gap table in §1 (one idea per memo).
4. Update `category_evidence_map.md` / category canvases only when memo+code IDs exist.
5. Constant-compare especially to: L1M1 / S5M3 (start), S1M5 / S2M4 (feedback), S6M2 (judgment), S1M3 / S5M1 (groups), S6M1 (cross-notation if any).

---

## 10. One-page cheat sheet (print / second screen)

**Spine:** Setup → Incident → First 10 min → Good enough → Rework? → Share / real feedback → Group or Cross-family or Load → One change → Missing?

**Listen for:** wait vs draft; rebuild vs late-only; ask-to-get-feedback; who owns the diagram; slides can’t replace lab; lost trace across notations.

**Park:** abstraction deficit; design wishlists without incident; AI generation ethics lecture.

**Coordinator one-liner if asked:** “These interviews theoretically sample start-gate mismatch, refine/rework as RQ1, feedback access in Portuguese large/local courses, and CAT14 only when multi-notation appears.”

---

## Related files

* [`pilot-student.md`](pilot-student.md) — Guide C full wording + pt-PT appendix
* [`pilot-teacher.md`](pilot-teacher.md) — not used for these student slots
* `Obsidian/CLTSM/qualitative_analysis/04_cross_case_analysis/findings_map_guide.md` — open questions
* `Obsidian/CLTSM/canvases/findings_map_overview.canvas` — PH ↔ open-question edges
