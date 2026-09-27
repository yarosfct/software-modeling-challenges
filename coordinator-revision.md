# Coordinator revision log

Working file for the coordinator’s comments on the opening of the thesis. Update this file one issue at a time. Do not bulk-rewrite a chapter from this log until the issue being edited is marked ready.

Shared 25 September 2026. The email itself is undated. He reviewed the first four sections and stopped. In this draft that is Chapters 1–4: Introduction, Background, Related Work, Methodology. Correct this assumption if the marked-up file shows he meant four sections inside one chapter.

## Email

> Hi Yaroslav,
>
> Please find attached my comments on the first four sections. I am stopping there for now, because I have other things to work on.
>
> I will not mince my words here, you have a lot of work to do. Specifically:
>
> 1. You are writing wayyyy to complicated. Clarity is key in academic writing, and your writing is far from that right now. Sentences are overly complex and long and it’s unclear what you’re trying to convey in many parts. Additionally, some parts sound really LLM-ish, which either means you’ve over-used those tools or adopted a similar writing style. For instance, consider the sentence “When a language is treated as a structured schema, models become more than static diagrams: they can become queryable, analysable, and transformable artefacts that enable deeper engagement with a domain.". What this sentence essentially means is “If models are stored in a machine-readable format, they can be used for tasks such as queries, analyses or model transformations.”.
> 2. The background largely overlaps with related work and does not really cover the background (The background section should explain key knowledge needed for the remainder of the thesis in an easy-to-read way).
> 3. The related work section is thin. You rely primarily on a few papers, in particular a few papers by me, but there’s a lot more. You could do something as basic as checking which papers we (and others) cite in our references and who is citing us (e.g., https://scholar.google.com/scholar?cites=17569590030352548355&as_sdt=2005&sciodt=0,5&hl=en and https://scholar.google.com/scholar?cites=7332577916003291855&as_sdt=2005&sciodt=0,5&hl=en), and you’d end up with loads of very relevant papers to your thesis.
>
> Please take a close look at my comments and try to incorporate as much as you possibly can.

## Agreed approach

The email is the revision. Margin notes are instances of these three points. Fix structure before polishing sentences that may be cut or moved.

Chapter jobs:

- **Introduction.** Why this study, what question, what the thesis contributes. One claim per sentence.
- **Background.** The ideas a reader needs before the methods and findings: what a model is, how a language differs from a diagram, Bloom as this thesis uses it, and Socio-Technical Grounded Theory as this thesis uses it. Short and definitional. Almost no “Author et al. found…”.
- **Related Work.** Who has studied learning and teaching modelling, what they found, where they disagree, and what this study adds. Grouped by the claim, not by author.
- **Methodology.** What was done. Use concepts already taught in Background. Do not teach them again.

Background currently does Related Work’s job. `2-MainMatter/chapter2.tex` sections “Modelling education” and “Human factors” walk through Maslov, CaMeLOT, Bogdanova and Snoeck, Bork, iStar, process modelling, and Liebel. `2-MainMatter/chapter3.tex` then opens on the same sources. Strip the literature out of Background. Keep a short definition only where a later chapter uses the idea. Put each empirical claim in Related Work once.

Related Work gets wider only after a reading pass. From the papers already cited, especially his, follow both directions: who they cite, and who cites them, starting from the two Scholar links above. Keep a paper when it changes a claim about learning challenges, teaching practice, tools in education, or human factors. One card in `paper-review/` before any new prose: what they studied, what they found, and which thesis claim it supports or complicates. Citing him less, without adding that neighbouring work, does not answer the comment.

Voice rule for every passage we touch: you write the plain meaning first. The check is whether the claim is accurate, whether the citation belongs, and whether the sentence still does two jobs. His rewrite of the schema sentence is the target register. Do not generate a clarified chapter in one pass.

Page note: printed pages end at 83, cap 100 (`thesis-review-backlog.md`). A thicker Related Work fits if the repeated Background material comes out.

This log overrides backlog item 2. That item said to leave Related Work sections 3.1–3.6 in place unless a figure needed the space. Those sections are part of the overlap and the thin-literature problem, so they are in scope here.

When a margin comment arrives, add it under Inline comments using the template, then fill the fields. Every entry has **In plain words**: what is wrong, what his comment means, and the next step. Label it before rewriting:

| Kind | What to do |
|---|---|
| Wording | Park the sentence. Apply it only if the passage survives the chapter split. |
| Fact or citation | Fix early. |
| Structure | Add it to the move list. Leave the local sentence alone until the section is rewritten. |
| Missing literature | Add it to the reading list. Do not insert a citation into the paragraph yet. |

## Index

| ID | Kind | Status | One line |
|---|---|---|---|
| P1 | Wording | Open | Prose is too complex and often unclear; some of it sounds generated. |
| P2 | Structure | Open | Background repeats Related Work and does not teach the background. |
| P3 | Literature | Open | Related Work is thin and leans on a few papers, especially his. |
| C1 | Fact or citation | Done | [5] in Motivation is a conceptual-modelling paper under a sentence that also says software modelling. |
| C2 | Structure | Done | The aim does not say how the thesis differs from his studies [8], [13], and [20]. |
| C3 | Wording | Done | “Incident probes” in the research-approach overview is unexplained. |
| C4 | Fact or citation | Done | “The iStar learning study” does not name which study. |
| C5 | Wording | Done | Subsection 2.1.3 sounds generated; the highlighted sentence is the email example. |
| C6 | Structure | Done | “Semantics” is used in 2.1.4 before the thesis explains what it means. |
| C7 | Wording | Done | Subsection 2.1.4, and section 2.1 as a whole, is full of big words. He asks what it is trying to say. |
| C8 | Structure | Done | 2.2.1 only says the field is large and authors disagree. He wants one sentence of examples. |
| C9 | Structure | Done | The 2.2.2 closing summary leads with Bloom as a lens. He wants the underrepresentation of evaluation and reflection as the point. |
| C10 | Structure | Open | “Beyond data and structural modelling” treats process and goal modelling as outside conceptual modelling. |
| C11 | Structure | Open | The iStar study in 2.2.3 reads as Related Work, not Background. |
| C12 | Structure | Open | The title says “Modelling”, but the papers in 2.2.4 are software modelling and MDE only. |
| C13 | Wording | Open | “Industrial-grade model-driven engineering” is not explained. |
| C14 | Literature | Open | [20] has a related-work section on other tool papers that this draft does not use. |
| C15 | Fact or citation | Done | [21] is an opinion paper by his group, not a broader discussion that independently supports [20]. |
| C16 | Structure | Done | The closing sentence of 2.2.6 says the literature informs the study, without saying how. |
| C17 | Structure | Open | Chapter-level: Background starts with concepts, then drifts into Related Work. |
| C18 | Structure | Done | The aim in 2.3.4 does not match the aim in 1.3. |
| C19 | Structure | Done | 2.3.4 claims cognition and organisational constraints that 14 interviews do not support. |
| C20 | Structure | Open | The Bloom section arrives after the thesis has already used Bloom at length. |
| C21 | Fact or citation | Open | [16] is general SE education, so subsection 2.5.1 mostly rests on the thin source [13]. |
| C22 | Fact or citation | Open | Subsection 2.5.2 again rests only on [13]. |
| C23 | Structure | Done | Subsection 2.5.3 repeats the earlier account of [20]. |
| C24 | Structure | Open | He will not read Chapter 3 in detail: it discusses the same papers as Background. |
| C25 | Wording | Done | Chapter 4 spells out STGT again after the acronym was already introduced. |
| C26 | Structure | Done | The methods opening says what the study did not do. He wants what it did. |
| C27 | Wording | Done | 4.1 says “Grounded Theory” in many words. He wants “STGT”. |
| C28 | Structure | Done | “Informed by STGT” does not say whether STGT was used. |
| C29 | Structure | Done | The design is “informed by” the iStar study, then says that study’s procedure was not used. |
| C30 | Wording | Done | The research questions are contrasted with hypotheses. He crossed this out. |
| C31 | Wording | Done | “Coping strategies” reads as a psychological term. |
| C32 | Structure | Done | The sentence points to Appendix A.3, which is a mapping table, not the interview guide. |
| C33 | Wording | Done | “Main prompts speak to which research question” is unclear. |
| C34 | Wording | Done | “Related courses” does not say related to what. |
| C35 | Structure | Backlog | The study is described as software modelling after a long conceptual-modelling background. |
| C36 | Wording | Done | “Lecturers” and “instructors” are used for the same people. |
| C37 | Wording | Done | “Corpus” is unexplained. |
| C38 | Structure | Done | “Wave 2” appears before waves have been explained. |
| C39 | Wording | Done | The inclusion sentence above the participant table is unclear. |
| C40 | Structure | Done | The section never says how participants were selected and recruited. |
| C41 | Wording | Done | “Incident probes” is still used without saying what was asked. |
| C45 | Structure | Done | The explanation of incident probing comes after the term was used in the introduction. |
| C42 | Wording | Done | “Student spine” is a new word for the shared guide structure called a backbone earlier. |
| C43 | Structure | Done | The Bloom sentence does not show the questions or how they map to Bloom. |
| C44 | Structure | Done | Pilot interviews were used to change the guide and were also kept as final data. |
| C46 | Wording | Done | “Critical-incident questions” is another undefined label for the same prompts. |
| C47 | Structure | Done | The Grounded Theory variant is discussed under analysis, but it belongs in the study design. |
| C48 | Structure | Done | Constant comparison is described as happening after coding, and also throughout coding. |
| C49 | Wording | Done | The saturation subsection is hard to follow and defends against a global claim qualitative work does not make. |
| C50 | Wording | Done | “Sensitising concept” is undefined. |
| C51 | Structure | Done | Bloom is described as applied after the categories, and also as used when writing the interview guide. |
| C52 | Structure | Done | The rigour section states what was done well. He wants the threats. |
| C53 | Fact or citation | Done | The ethics section says the recordings were anonymised and does not say how. |
| C54 | Structure | Done | The limitations section should be part of the threats discussion in the rigour section. |

## Correction plan

Work in this order. Tick an ID in the index when its text is changed. **P1** is the rule for every step: you write the sentence. Do not start with Chapter 3. He stopped reading it because it repeats Background (**C24**). Polishing it now means writing it twice.

Three decisions gate the later waves. You can make them in a few sentences before Wave C, and you should not rewrite Background before the first one:

1. Is the study about software modelling, or about conceptual modelling in the broader sense? (**C35**)
2. What does this thesis do that his studies [8], [13], and [20] do not? (**C2**)
3. Which parts of STGT were used, which were not, and why? (**C28**)

### Wave A — Change or delete a few words

One sitting. No new reading. These sentences stay even after the later restructure.

- [x] **C30.** Delete the sentence that says the research questions are not hypotheses.
- [x] **C25.** In the Chapter 4 opening, write STGT. Do not spell it out again.
- [x] **C26.** Delete the opening sentence about Strauss and Corbin. Leave the later version of that contrast until **C47**.
- [x] **C37.** Replace “corpus” with “the 14 interviews”.
- [x] **C34.** Replace “related courses” with the courses you mean, or with “courses that include software modelling”.
- [x] **C36.** Pick one word, instructors or lecturers, and use it in section 4.3 and in the participant table.
- [x] **C31.** Replace “coping strategies” in RQ2 in Chapters 1 and 4. Plain candidate: “strategies”.
- [x] **C42.** Replace “student spine” with the same word already used for the shared guide. That word is “backbone”, or say “the same student guide”.
- [x] **C46.** Delete “critical-incident questions”, or replace it with “questions that ask for a specific episode”.
- [x] **C4.** Name Li et al. where Chapter 1 says “the iStar learning study”.
- [x] **C1.** Narrow the Motivation sentence so [5] supports only conceptual modelling. Do not go looking for a software-modelling source yet.
- [x] **C15.** Stop calling [21] a broader discussion that confirms [20]. Call it an agenda paper from that group.
- [x] **C21,** the Holmes half only. Remove [16] from the sentence about modelling outputs. The thinness of [13] waits until Wave F.
- [x] **C16,** the vague sentence only. Delete “These insights inform the research questions…”. Do not write a replacement yet.

### Wave B — One plain sentence you write

One or two sittings. You fill the wording block, then the sentence is edited.

- [x] **C3.** Write what an incident probe asked. Use that wording at the first use in Chapter 1.
- [x] **C41** and **C45.** Use the C3 wording in section 4.4. Subsection 4.4.2 keeps the detail and stops being the first definition.
- [x] **C39.** State the inclusion rule: who had to have done a modelling task, and why.
- [x] **C32** and **C33.** Point section 4.2 at the interview-guide sections, not only at Appendix A.3. Replace “speak to” with “address”.
- [x] **C48.** Keep “throughout” for comparison during coding. In 4.5.3, say only that categories were later merged, split, and bounded.
- [x] **C23.** Delete the second paragraph of 2.5.3. It retells [20], which 2.2.4 already tells.
- [x] **C53.** One sentence on the recordings: what was done to the audio. If only the transcripts were anonymised, say that.

### Wave C — Decisions, then a short paragraph

Several sittings. Each item needs a fact or a choice from you before the prose can be written.

- [x] **C35.** Deferred. The thesis is about software modelling. Conceptual modelling stays in Background, with less emphasis. The trim is backlog item 3, done with Wave E.
- [x] **C2.** Two sentences in section 1.3: what [8], [13], and [20] already did, and what this thesis does that they do not. [13] is the published FSE Companion 2026 paper, not an unpublished manuscript.
- [x] **C18** and **C19.** Make subsection 2.3.4 use that same aim. Drop individual cognition and organisational constraints unless the interviews actually cover them.
- [x] **C28** and **C27.** In section 4.1, say the study used STGT, then name the parts used and the parts not used. “Informed by” goes.
- [x] **C29.** Say what was taken from Li et al. If nothing procedural was taken, delete “informed by”.
- [x] **C40** and **C38.** How people were selected and contacted. Then two sentences on what wave 1 and wave 2 were, before section 4.3 uses “Wave 2”.
- [x] **C44.** What changed in the guide after S1 and S2, and why those two interviews remain in the dataset.
- [x] **C43,** easy path. The questions do not map cleanly onto Bloom levels, so the sentence that says Bloom shaped the prompts is deleted.
- [x] **C51** and **C50.** In 4.5.6, say when Bloom was actually used. Replace “sensitising concept” and “analytic lens” with that account.

### Wave D — Rewrite a subsection in your own words

One subsection per sitting. Do not generate the replacement.

- [x] **C7.** Section 2.1 is rewritten. Subsection 2.1.1 is the purpose and the language-versus-one-model sentences. Subsection 2.1.2 is the short family distinction. Subsection 2.1.3 is the method, the semantics definition, copying, and the machine-readable sentence. Subsection 2.1.4 is the scope sentence.
- [x] **C47.** The STGT account stays in section 4.1. The old 4.5.1 subsection is removed. Coding and memoing now says that open codes were separate notes, and that a memo linked the notes that belonged to its one idea. The Strauss–Corbin contrast is cut.
- [x] **C49.** Subsection 4.5.5 says why interviewing stopped. Dey is not cited. Theoretical sufficiency is defined from Sims and Cilliers in the Background and used in that subsection. The abstract, Chapter 5 caption, Chapter 6, and Chapter 7 still use the old local-saturation wording.
- [x] **C52** and **C54.** Section 4.6 states the threats under credibility, dependability and confirmability, and transferability. The standalone limitations section is deleted.
- [x] **C43,** full path. A partial map is in subsection 4.4.1 (Table of the prompts that aim at a Bloom level). The other prompts are not given a level.

### Wave E — Background and Related Work change jobs

Resume here. Wave D is done through C54. C8 and C9 are done. Next is C10. Do not polish a Background survey and leave it. Move each paper summary from sections 2.2 and 2.5 into Chapter 3, apply the parked comment to the copy that stays, and delete the Background telling. Chapter 3 is not rewritten sentence by sentence until that split is done. The wider reading is Wave F.

This is **P2**, **C17**, and **C24** as one job. Do it after Wave D has settled section 2.1, because 2.1 is the part of Background that should remain.

Move the paper summaries out of sections 2.2 and 2.5 into Chapter 3, and delete the second telling. While doing that, apply the comments that were parked because those passages move:

- [x] **C8.** One sentence on what researchers actually do. Not a survey.
- [x] **C9.** End the Bloom discussion on the underrepresentation of evaluation and reflection.
- [ ] **C10.** Drop “beyond data and structural modelling”.
- [ ] **C11.** One account of the iStar study, in Related Work.
- [ ] **C12** and **C13.** Say that the tool material is software modelling and model-driven engineering, and define those terms if the sentences stay.
- [ ] **C20.** Put the short explanation of Bloom before the first passage that uses it.
- [ ] **C22.** Do not give inclusion and domain diversity their own subsection on [13] alone.
- [ ] **C35,** applied. The thesis is about software modelling. Shorten the conceptual-modelling survey in Background. Keep what the courses and interviews use. Do not remove it. See backlog item 3.

Do not add another “implications for this thesis” subsection. **C16** stays deleted unless a concrete link is obvious while you move the text.

### Wave F — Read, then rewrite Related Work

This is **P3**. Start from the related-work section of [20] (**C14**) and from the two Scholar “cited by” lists in the email. One card in `paper-review/` before a paper enters the chapter.

- [ ] **C14.** Tool papers cited by Liebel, Badreddin, and Heldal (2017).
- [ ] **C21** and **C22.** Other published work on motivation, inclusion, and domain diversity, or cut those passages back to what [13] can support. [13] is now the published FSE Companion 2026 paper. One paper still cannot carry those subsections alone.
- [x] **C1,** the remaining half. A software-modelling source for “before implementation”, if that claim is still in the Motivation after Wave A. The claim was dropped. Kühne, Gorschek et al. (2014), and Petre (2013) are on the revised sentence.
- [ ] **C2,** check. The difference written in Wave C still has to be true once the extra papers are in.
- [ ] **C24.** Rewrite Chapter 3 by the thesis claims. He has no inline comments on this chapter. The job is the split from Wave E plus this wider set of papers.

Mark **P1**, **P2**, and **P3** done only when the wave that carries them is done. **P1** stays in force through Wave F.

## P1 — Clarity

**Status:** Open

**Kind:** Wording. Applies to every passage we edit in Chapters 1–4, not to one sentence only.

**Issue:** Sentences are long, complicated, and often unclear. Some passages sound generated. His example of the failure, and of the register he wants:

> When a language is treated as a structured schema, models become more than static diagrams: they can become queryable, analysable, and transformable artefacts that enable deeper engagement with a domain.

He reads that sentence as:

> If models are stored in a machine-readable format, they can be used for tasks such as queries, analyses or model transformations.

**In plain words:** The writing is hard to follow. Sentences are long, and some sound generated rather than written by you. He wants the same point in ordinary words. Next: when a passage is rewritten, you write that plain sentence yourself.

**Where it sits:** The example is in Background, “Software modelling & conceptual modelling” → “Modelling methods, languages, and artefacts”. The same habit shows up across the opening chapters: stacked clauses, a colon, then a list of abstract adjectives.

**Location:** `2-MainMatter/chapter2.tex`, in `\subsection{Modelling methods, languages, and artefacts}` (`subsec:modelling_methods_languages_artefacts`). The quoted sentence is the second sentence of the paragraph that begins “From this viewpoint, the value of a modelling language…”.

**Possible fix:** Replace that sentence with a plain claim in your words, close to his reading if that reading is accurate. Use the same test on later wording comments: one main clause, concrete nouns, ordinary verbs. Do not clear the whole chapter in one rewrite.

**Your wording:**

```text

```

**Decision:**

```text

```

## P2 — Background versus Related Work

**Status:** Open

**Kind:** Structure

**Issue:** Background largely overlaps Related Work. Background should explain, in plain language, the knowledge the rest of the thesis needs. It should not survey the papers. His chapter-level statement of this problem is C17.

**In plain words:** Background and Related Work tell the same papers. Background should teach the ideas the rest of the thesis needs, in simple language. Next: take the paper summaries out of Background and leave each paper in Related Work once.

**Where it sits:**

- Keep and simplify in Background: what software modelling and conceptual modelling are; model versus language versus method; Grounded Theory and Socio-Technical Grounded Theory as used in the methods; Bloom at the level later chapters use.
- Move the paper-by-paper material out of Background. It currently sits in:
  - `chapter2.tex` `\section{Modelling education}` — Maslov landscape, Bogdanova and Snoeck, Bork, BPMN agenda, iStar learning study, tools and model-driven engineering.
  - `chapter2.tex` `\section{Human factors in modelling and SE education}`.
  - The Bloom subsections that report what those papers found, as distinct from a short explanation of Bloom itself.
- Related Work already retells the same sources, starting at `chapter3.tex` `\section{Conceptual modelling education landscape}` (Maslov again) and continuing through frameworks, iStar, tools, human factors, and competence agendas (sections 3.1–3.6).

**Location:** `2-MainMatter/chapter2.tex` and `2-MainMatter/chapter3.tex`.

**Possible fix:** Give Background the definitional job and Related Work the empirical job. Delete the repeated telling. Each paper is summarised once, in Related Work, after the reading pass in P3. A Background subsection survives only when a later chapter needs that idea, and then only as a short explanation.

**Your wording:**

```text

```

**Decision:**

```text

```

## P3 — Thin Related Work

**Status:** Open

**Kind:** Literature

**Issue:** Related Work relies on a few papers, in particular a few by the coordinator. Much more relevant work is available by reading the reference lists of those papers and the papers that cite them.

**In plain words:** Related Work leans on a handful of papers, especially his. He wants you to follow the papers they cite and the papers that cite them. Next: read those and make a short note for each useful one before rewriting the chapter.

**Where it sits:** Chapter 3 as a whole. The seed he named is “papers by me” plus the two “cited by” lists:

- https://scholar.google.com/scholar?cites=17569590030352548355&as_sdt=2005&sciodt=0,5&hl=en
- https://scholar.google.com/scholar?cites=7332577916003291855&as_sdt=2005&sciodt=0,5&hl=en

Also follow the reference lists of the papers already central in Chapters 2 and 3.

**Location:** `2-MainMatter/chapter3.tex`. New notes go in `paper-review/` before the chapter text changes. `paper-review/literature-index.md` is the existing index.

**Possible fix:** Build a short card per candidate paper, then regroup Chapter 3 by the thesis claims. Keep a paper when it bears on learning challenges, teaching practice, tools in education, or human factors. Write the section after the cards exist. This waits on P2 only in the sense that the new prose replaces the overlap; the reading itself can start now.

**Reading list:**

| Candidate | Why it is here | Card | Kept? |
|---|---|---|---|
| | | | |

**Your wording:**

```text

```

**Decision:**

```text

```

## Inline comments

## C1 — Motivation citation [5] and software modelling

**Status:** Done

**Kind:** Fact or citation

**Chapter:** 1.1 Motivation

**Highlighted sentence:**

> Software systems are complex socio-technical artefacts that must evolve under technical, organisational, and human constraints. In this setting, software and conceptual modelling provide structured abstractions that can support reasoning, communication, and early validation before implementation [5].

**His comment:**

> 5 is on conceptual modelling. Does it also support the "software modelling" direction?

**In plain words:** The sentence claims both software modelling and conceptual modelling, but the cited paper only covers conceptual modelling. He is asking if that paper also supports the software-modelling part. It does not. Next: narrow the sentence so the citation only covers conceptual modelling, or add a different source for the software-modelling claim.

**Where it sits:** First paragraph of the Motivation. The citation is on the clause that names both software modelling and conceptual modelling, and on “early validation before implementation”.

**Location:** `2-MainMatter/chapter1.tex`, `\section{Motivation}` (`sec:intro_motivation`), the `\cite{buchmann2019conceptual}` at the end of the second sentence. In the bibliography this is Buchmann, Ghiran, Döller, and Karagiannis, “Conceptual Modelling in Education: A Position Paper” (BIR 2019 workshops). Local note: `paper-review/cards/buchmann-position.md`.

**Possible fix:** The paper supports the conceptual-modelling half: models as structured abstractions for reasoning and communication, rather than drawings. It does not establish a separate software-modelling claim, and “before implementation” is a software-engineering use that this position paper is not carrying. Narrow the sentence so [5] covers only conceptual modelling, and cite a software-modelling source for that direction and for validation before implementation. If both directions stay in one sentence, the citation has to be split.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
Buchmann is off this sentence. The Motivation now says software modelling represents the parts of a system, or of the problem, that matter for a purpose (Kühne), and that design models are a shared picture for trying out ideas and talking about the system, with use and formality differing by project (Gorschek et al. 2014; Petre 2013). "Before implementation" and "conceptual modelling" were dropped from this sentence.
```

## C2 — How the thesis differs from [8], [13], and [20]

**Status:** Done

**Kind:** Structure

**Chapter:** 1.3 Aim and research questions

**Highlighted sentence:**

> The aim of this thesis is to develop an empirically grounded account of modelling education challenges and support needs in higher education, treating modelling as a socio-technical activity that combines conceptual understanding, procedural strategies, and contextual influences.

**His comment:**

> Given studies like my own (8, 13, 20), how is your thesis different?

**In plain words:** The aim describes a general study of challenges and support needs. His papers already do that kind of study. He wants to know what yours does that those do not. Next: add one or two sentences that name that difference.

**Where it sits:** The whole first paragraph of “Aim and research questions”, before the research questions. The paragraph states the aim and does not say what those studies already did.

**Location:** `2-MainMatter/chapter1.tex`, `\section{Aim and research questions}` (`sec:intro_aim_rq`), the paragraph that begins “The aim of this thesis…”.

The numbers in the current bibliography are:

- [8] `chakraborty2022perceptions` — Chakraborty and Liebel, “We do not understand what it says — studying student perceptions of software modelling”, *Empirical Software Engineering* (2023).
- [13] `grassl2026dei` — Graßl, Lazik, Chakraborty, Liebel, and Goulão, “Domain Diversity, Motivation, Inclusion, and Feedback in Software Modelling Education”, FSE Companion 2026, pages 1051–1062, DOI 10.1145/3803437.3805791. Published 17 July 2026. He is a co-author. Parallel surveys of 90 students and 22 educators.
- [20] `liebel2017model` — Liebel, Badreddin, and Heldal, “Model Driven Software Engineering in Education: A Multi-Case Study on Perception of Tools and UML”, CSEE&T 2017.

**Possible fix:** In this paragraph, say in one or two plain sentences what those three studies already cover and what this thesis does that they do not. [8] and [20] are published empirical studies of student perceptions and of tool/UML perception in education. [13] is his co-authored FSE Companion 2026 paper on domain diversity, motivation, inclusion, and feedback (parallel surveys of 90 students and 22 educators). The aim as written (“an empirically grounded account of challenges and support needs”) is broad enough to describe that work too. The difference has to be concrete: who was interviewed, which modelling activities, or what kind of account. Leave the research questions as they are unless the difference changes them.

**Depends on:** P3. The difference should stay true once Related Work includes more than his papers.

**Your wording:**

```text

```

**Decision:**

```text
Section 1.3 now says what the three studies did, then says this thesis asks lecturers and students about a specific recent incident they can recall, and how they dealt with it, across several notations. It does not say they were asked to describe one modelling task. [13] is cited as the published FSE Companion 2026 paper.
```

## C3 — “Incident probes” is unexplained

**Status:** Done

**Kind:** Wording

**Chapter:** 1.4 Research approach overview

**Highlighted sentence:**

> Guides used incident probes about a recent assignment, laboratory, or text-to-model start; unlike the iStar learning study, this work did not combine a tutorial and a modelling session with a later interview [19].

**His comment:**

> What does this mean?

**In plain words:** “Incident probes” is jargon. He cannot tell what the interviewer asked. Next: say in ordinary words that each interview asked about a recent concrete episode, such as an assignment or a lab.

**Where it sits:** The sentence in the research-approach paragraph that starts “Guides used incident probes…”. “Incident probes” is method jargon, and the sentence does not say what the interviewer asked.

**Location:** `2-MainMatter/chapter1.tex`, `\section{Research approach overview}` (`sec:intro_approach`), the sentence beginning “Guides used incident probes…”.

**Possible fix:** Say in ordinary words what the guides did. For example, that each interview asked about a recent concrete episode, such as an assignment, a lab, or the moment of starting a model from a text. Leave the full procedure for the methods chapter. This comment is only the first half of the sentence. The iStar contrast is C4.

**Depends on:** P1

**Your wording:**

```text

```

**Decision:**

```text
The sentence no longer says "Guides used incident probes". Section 1.4 now says the interview questions asked participants to describe a specific episode, such as a recent assignment, a laboratory, or the start of turning a text into a model. The following sentence names Li et al. and says this study did not run a tutorial and a modelling session before the interview.
```

## C4 — Which iStar learning study?

**Status:** Done

**Kind:** Fact or citation

**Chapter:** 1.4 Research approach overview

**Highlighted sentence:**

> Guides used incident probes about a recent assignment, laboratory, or text-to-model start; unlike the iStar learning study, this work did not combine a tutorial and a modelling session with a later interview [19].

**His comment:**

> which one?

**In plain words:** “The iStar learning study” sounds as if there is only one. He is asking which paper you mean. It is Li et al. (2025). Next: name the authors in the sentence.

**Where it sits:** The same sentence as C3, on the phrase “unlike the iStar learning study”. The citation is present, but the prose never names the authors, so “the” iStar study reads as if there were only one.

**Location:** `2-MainMatter/chapter1.tex`, `\section{Research approach overview}` (`sec:intro_approach`), `\cite{istar-learning}`. In the current bibliography this is [19]: Li, Zhou, Wang, Xiong, Liu, and Ge, “Understanding the Challenges and Requirements for Facilitating iStar Learning: An Empirical Study with iStar Learners”, *Information and Software Technology* 187 (2025).

**Possible fix:** Name the authors in the sentence, and keep [19] on that name. The contrast can stay: this thesis interviewed students and instructors about recent work, and did not run a tutorial plus a modelling session and then interview, as Li et al. did. Do not leave “the iStar learning study” as the only identification.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
Section 1.4 now says "unlike Li et al." with the istar-learning citation on that name. The contrast about the tutorial and modelling session stays. The incident-probe half of the same sentence is still C3.
```

## C5 — Subsection 2.1.3 sounds generated

**Status:** Done

**Kind:** Wording

**Chapter:** 2.1.3 Modelling methods, languages, and artefacts

**Highlighted sentence:**

> When a language is treated as a structured schema, models become more than static diagrams: they can become queryable, analysable, and transformable artefacts that enable deeper engagement with a domain.

**His comment:**

> The way of writing in this entire section sounds veeeery LLM-ish. If you rely on LLMs (assuming that they're allowed at NOVA), please at least rewrite things.

**In plain words:** The whole subsection sounds generated, not only the highlighted sentence. He wants you to rewrite it yourself. Next: rewrite both paragraphs in your own words, and make the highlighted sentence as plain as the example in his email.

**Where it sits:** The whole subsection, not only the highlighted sentence. It is two paragraphs. The highlight is the second sentence of the paragraph that begins “From this viewpoint, the value of a modelling language…”. That sentence is the example in the email (P1).

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Modelling methods, languages, and artefacts}` (`subsec:modelling_methods_languages_artefacts`). The next subsection, “Implications for the scope of this thesis”, is outside this comment.

**Possible fix:** Rewrite both paragraphs in your own words. Keep the content that belongs in Background: a modelling method is a language, a procedure, and mechanisms such as analysis or transformation; students can copy symbols and still not be able to use the method. For the highlighted sentence, use a plain claim close to his reading in P1 if that reading is accurate: a machine-readable model can be queried, analysed, or transformed. Do not generate a replacement for this subsection.

**Depends on:** P1

**Your wording:**

```text

```

**Decision:**

```text
Subsection 2.1.3 now uses the agreed sentences. The method sentence cites Bork only: language, steps for creating a valid model from a description, and what a tool can do with the model once it exists. Semantics is defined as what the symbols mean. The copying sentence and the machine-readable sentence are the second paragraph's replacement. Buchmann, Bogdanova, and Maslov are off this subsection. "Semantics" is still used earlier, in 2.1.2, which is C6.
```

## C6 — “Semantics” is used before it is explained

**Status:** Done

**Kind:** Structure

**Chapter:** 2.1.4 Implications for the scope of this thesis

**Highlighted sentence:**

> It therefore treats modelling as a discipline involving conceptual understanding of modelling constructs and their semantics, procedural competence in constructing and refining model artefacts from problem descriptions, analytical judgement of model quality and fit-for-purpose, and socio-technical awareness of how modelling practices are shaped by tools, learning contexts, and stakeholder needs.

**His comment:**

> You haven't covered what "modelling semantics" is.

**In plain words:** The sentence uses “semantics” as if the reader already knows what it means. The chapter never explains it. Next: add a short explanation earlier, or take the word out.

**Where it sits:** The phrase “and their semantics” in the second sentence of the subsection. Section 2.1 has used “semantics” earlier, in 2.1.2 and 2.1.3, without saying what it means.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Implications for the scope of this thesis}` (`subsec:implications_scope_thesis`). Earlier uses are in `\subsection{Conceptual modelling as a broader discipline}` and `\subsection{Modelling methods, languages, and artefacts}`.

**Possible fix:** Before this sentence relies on the word, add a short plain explanation in section 2.1: semantics is what the constructs mean, as distinct from the symbols used to draw them. If that explanation does not earn its place in Background, take “semantics” out of this sentence.

**Depends on:** P2

**Your wording:**

```text

```

**Decision:**

```text
Subsection 2.1.2 no longer uses the word. The first explanation is now in 2.1.3: what the symbols mean is called the semantics. Later uses in the Bloom and iStar passages come after that definition. Subsection 2.1.4 no longer uses the word.
```

## C7 — What is section 2.1 trying to say?

**Status:** Done

**Kind:** Wording

**Chapter:** 2.1.4 Implications for the scope of this thesis

**Highlighted sentence:**

> Side note on the whole subsection. No single sentence was marked. The note also covers section 2.1.

**His comment:**

> There are a lot of big words in this sub-section (and the whole 2.1). In easy words: What are you trying to convey?

**In plain words:** Section 2.1 is full of big words, so the point is hard to see. He wants that point in easy words. Next: write the point in a few plain sentences, then rewrite the subsection to match.

**Where it sits:** All of subsection 2.1.4, and he extends the same objection to section 2.1, “Software modelling & conceptual modelling” (2.1.1 through 2.1.4).

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Implications for the scope of this thesis}` (`subsec:implications_scope_thesis`), and the parent `\section{Software modelling \& conceptual modelling}` (`sec:software_modelling_conceptual`).

**Possible fix:** Answer his question in a few plain sentences, then rewrite the subsection to that answer. The subsection is currently one long sentence listing “conceptual understanding”, “procedural competence”, “analytical judgement”, and “socio-technical awareness”, plus a second sentence on learning outcomes. C5 already covers the generated tone of 2.1.3. This comment is the plain-language demand for 2.1.4 and for the rest of 2.1.

**Depends on:** P1 and P2

**Your wording:**

```text
A software model shows the parts of a system, or of the problem, that matter for a purpose, such as talking about the system or trying a design. The symbols have an agreed meaning: the same mark is read in the same way. The language is the set of allowed symbols and those meanings. A model is one description written in that language for one problem. A modelling method is that language, the steps for making a model from a description, and what a tool can check or change. Students can copy the symbols and still be unable to take those steps or judge the result. If a model is stored so a machine can read it, it can be queried, analysed, or transformed. Conceptual modelling is the wider family, including data, process, and goal models. This thesis is about software modelling in courses, where students and lecturers deal with what a construct means, how to build a model from a description, and how to judge whether it is good enough.
```

**Decision:**

```text
Point locked on 27 September 2026. All four subsections now follow it. Subsection 2.1.1 is the purpose, the agreed meaning, and language versus one model, citing Kühne, Gorschek, and Petre. "Before implementation," Buchmann, Maslov, and the type/token wording are gone from that subsection. Subsection 2.1.2 is the short family distinction. Subsection 2.1.3 defines the method, names semantics at first use, and keeps the machine-readable sentence. Subsection 2.1.4 is only the scope sentence. The four-pillar list is gone. Read in order, "semantics" is first defined in 2.1.3, conceptual modelling is one short paragraph, and 2.1.4 does not claim a wider study than Chapter 1.
```

## C8 — 2.2.1 names no research directions

**Status:** Done

**Kind:** Structure

**Chapter:** 2.2.1 Overview of conceptual modelling education

**Highlighted sentence:**

> While there is broad consensus on the importance of modelling skills for software professionals, there is less agreement on which specific competencies learners should acquire, how these competencies should be scaffolded, and how learning should be assessed in a reliable and educationally meaningful way.

**His comment:**

> OK, but can you at least give some examples? What are directions? What do people do in the research sphere? In one sentence. Section 2.2.1 really only says "There is a lot of work on conceptual modelling in education and authors don't agree".

**In plain words:** The subsection only says there is a lot of work and that people disagree. He wants one sentence of examples of what researchers actually do. Next: add that sentence, and do not turn the subsection into a survey.

**Where it sits:** The last sentence of subsection 2.2.1. He is judging the whole subsection, not only that sentence. The two paragraphs say that teaching varies, that Maslov et al. map several sub-communities, and that there is less agreement on competencies, scaffolding, and assessment. They do not say what researchers actually do.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Overview of conceptual modelling education}` (`subsec:overview_conceptual_modelling_education`). The highlighted sentence is the last sentence of the second paragraph. The same landscape is repeated at the start of Related Work, `\section{Conceptual modelling education landscape}` in `2-MainMatter/chapter3.tex`.

**Possible fix:** Add one sentence of examples to this subsection: the kinds of work people do, such as learning-outcome frameworks, studies of where learners struggle, and tool support. Do not turn 2.2.1 into a survey. Under P2 this subsection is literature sitting in Background, so the sentence should be written so it can move to Related Work with the rest of the overlap.

**Depends on:** P2

**Your wording:**

```text
Researchers write learning-outcome frameworks, study where learners struggle, and study how tools support modelling.
```

**Decision:**

```text
Point locked on 27 September 2026. The sentence is the last sentence of the Maslov paragraph in Related Work, section 3.1. It has no citation of its own. The Maslov citation stays on the mapping sentence. Subsection 2.2.1 is deleted. Its two paragraphs are not copied into Related Work. Later Maslov mentions in the Chapter 3 dialogue and in Chapter 6 are unchanged.
```

## C9 — The Bloom subsection closes on the wrong point

**Status:** Done

**Kind:** Structure

**Chapter:** 2.2.2 Bloom-based perspectives on modelling learning outcomes

**Highlighted sentence:**

> These works collectively suggest that Bloom's taxonomy can provide a useful lens for reflecting on and improving modelling education, by making learning objectives more explicit and balanced across different dimensions.

**His comment:**

> Yes and no. I find the much more important summary of this section that the more advanced skills (evaluation, reflection) are underrepresented.

**In plain words:** The section ends by saying Bloom is a useful lens. He thinks the real point is that evaluation and reflection get less attention. That point is already in the section, but it is not the ending. Next: end on that finding.

**Where it sits:** The last sentence of subsection 2.2.2. The underrepresentation is already in the subsection: Bogdanova and Snoeck report less attention to evaluation and to procedural and metacognitive knowledge, and the Bork paragraph says evaluation and metacognitive knowledge are underemphasised. The closing sentence then summarises Bloom as a useful lens instead of that finding.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Bloom-based perspectives on modelling learning outcomes}` (`subsec:bloom_perspectives_modelling_learning_outcomes`). The highlighted sentence is the last sentence of the third paragraph.

**Possible fix:** Make the last sentence the finding he names: in this work, evaluation and reflection are underrepresented. Keep “Bloom is a useful lens” as a shorter lead-in, not as the summary of the subsection.

**Depends on:** P2

**Your wording:**

```text
Bogdanova and Snoeck find almost no assessment tasks at the evaluate level, and no metacognitive outcomes. Bork's teaching case gives little explicit practice in evaluation or metacognition.
```

**Decision:**

```text
Point locked on 27 September 2026. The approved comparison ("less attention than understanding, analysis, and creation") and the word "reflection" were dropped after a check. Bogdanova and Snoeck report almost no evaluate-level tasks and no metacognitive outcomes. Bork's teaching case is thin on evaluation and metacognition, and strong on apply, analyse, and create, so it does not support a ranking against understanding. The interviews aim one prompt at evaluate (student Q7). They do not aim a prompt at metacognition. The two sentences are a new paragraph at the end of Related Work section 3.2, after the Bork subsection. Each sentence cites its own paper. The Bork subsection's closing claim that the thesis focuses on reflective judgement is deleted. Subsection 2.2.2 is deleted. Section 2.4 still explains Bloom and still retells these papers. That section is C20.
```

## C10 — “Beyond data and structural modelling”

**Status:** Open

**Kind:** Structure

**Chapter:** 2.2.3 Process and goal modelling education

**Highlighted sentence:**

> Beyond data and structural modelling, there is growing interest in how students learn process and goal-oriented modelling.

**His comment:**

> Why beyond these? So far, you've focused on conceptual modelling, which should include all of those areas.

**In plain words:** “Beyond” makes process and goal modelling sound like a separate topic. You already defined conceptual modelling as including those areas. Next: drop “beyond” and treat them as part of the same scope.

**Where it sits:** The opening sentence of subsection 2.2.3. “Beyond” treats data and structural modelling as the base and process and goal modelling as something extra. Section 2.1 already presents conceptual modelling as including data, process, goal, and enterprise modelling.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Process and goal modelling education}` (`subsec:process_goal_modelling_education`), first sentence.

**Possible fix:** Drop “beyond”. State process and goal modelling as part of the same conceptual-modelling scope already set in section 2.1, then say what is specific about learning them. Do not introduce them as a departure from conceptual modelling.

**Depends on:** P2

**Your wording:**

```text

```

**Decision:**

```text

```

## C11 — The iStar study is Related Work

**Status:** Open

**Kind:** Structure

**Chapter:** 2.2.3 Process and goal modelling education

**Highlighted sentence:**

> Goal-oriented requirements modelling approaches introduce additional layers of complexity, as it requires learners to reason about stakeholder intentions, rationales, and dependencies. An iStar learning study explicitly investigates the challenges students face when learning iStar, using a combination of Bloom-based task framing and grounded theory analysis of tutorials, modelling sessions, and interviews [19].

**His comment:**

> Should this really be background? It sounds much more like related work.

**In plain words:** The paragraph describes one study’s method and findings. That belongs in Related Work, not in Background. Next: move it, and keep a single account in Related Work.

**Where it sits:** The second paragraph of subsection 2.2.3. The highlight stops at the citation, but the paragraph continues with the study’s findings and its catalogue of strategies and tool requirements. The BPMN agenda in the paragraph above is the same kind of paper summary.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Process and goal modelling education}` (`subsec:process_goal_modelling_education`), second paragraph, `\cite{istar-learning}`. That key is [19], Li et al., *Information and Software Technology* (2025), the same study as C4. Related Work already summarises it in `2-MainMatter/chapter3.tex`, `\subsection{iStar learning challenges and support requirements}` (`subsec:rw_istar_learning`).

**Possible fix:** Move this study summary to Related Work and keep a single account there. Background should not retell the tutorials, the modelling sessions, the findings, or the tool catalogue. If a later chapter needs the study, a short pointer is enough.

**Depends on:** P2

**Your wording:**

```text

```

**Decision:**

```text

```

## C12 — The title says modelling; the papers are software modelling

**Status:** Open

**Kind:** Structure

**Chapter:** 2.2.4 Modelling, tools, and model-driven engineering in education

**Highlighted sentence:**

> The word “Modelling” in the subsection title.

**His comment:**

> The papers covered here only focus on software modelling, not conceptual modelling in the sense you introduced earlier. You need to be transparent about that.

**In plain words:** The title says modelling in general, but the papers are only about software modelling and model-driven engineering. That is narrower than the conceptual modelling you defined earlier. Next: say that limit in the opening sentence.

**Where it sits:** The title of subsection 2.2.4. The body cites only [20] and [21], both on model-driven software engineering and UML, not on conceptual modelling in the broader sense of section 2.1 (data, process, goal, enterprise).

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Modelling, tools, and model-driven engineering in education}` (`subsec:tools_mde_education`).

**Possible fix:** Say in the first sentence that this subsection is about tools in software-modelling and model-driven engineering courses, and that it does not cover tools for conceptual modelling more broadly. Keep that limit visible in the title or in the opening sentence.

**Depends on:** P2

**Your wording:**

```text

```

**Decision:**

```text

```

## C13 — “Industrial-grade” is unexplained

**Status:** Open

**Kind:** Wording

**Chapter:** 2.2.4 Modelling, tools, and model-driven engineering in education

**Highlighted sentence:**

> Modelling in educational settings is often mediated by tools, ranging from simple drawing tools and web-based modellers to industrial-grade model-driven engineering (MDE) environments.

**His comment:**

> Meaning what? This is the background section, so you need to explain what things mean.

**In plain words:** “Industrial-grade model-driven engineering” is used without a definition. In Background, a term has to be explained before it is used. Next: say what it means in plain words, or drop the jargon.

**Where it sits:** The phrase “industrial-grade model-driven engineering” in the first sentence. The subsection never says what model-driven engineering is, or what “industrial-grade” adds.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Modelling, tools, and model-driven engineering in education}` (`subsec:tools_mde_education`), first sentence.

**Possible fix:** Define the terms in plain words before using them. Model-driven engineering here means building software by treating models as the source that tools turn into other artefacts, including code. Say what “industrial-grade” is meant to contrast with the drawing tools and web modellers in the same sentence, or drop the adjective if it is not doing that work.

**Depends on:** P1 and P2

**Your wording:**

```text

```

**Decision:**

```text

```

## C14 — Use the tool papers in [20]’s related work

**Status:** Open

**Kind:** Literature

**Chapter:** 2.2.4 Modelling, tools, and model-driven engineering in education

**Highlighted sentence:**

> They also find that perceptions of UML as modelling language are more positive and robust when models are used for requirements and analysis, rather than only as precise inputs to code generators [20].

**His comment:**

> 20 in particular has an extensive related work section on other tool-related modelling papers. You should take a look at those.

**In plain words:** You cite his 2017 paper, and that paper already reviews many other papers about modelling tools. He wants you to read that review and use the ones that matter for this thesis. Next: read it and add the useful papers to the reading list before changing the prose.

**Where it sits:** The last sentence of the first paragraph, on the citation. [20] is `liebel2017model`: Liebel, Badreddin, and Heldal, CSEE&T 2017, the same paper as in C2.

**Location:** `2-MainMatter/chapter2.tex`, first paragraph of `subsec:tools_mde_education`, the second `\cite{liebel2017model}`.

**Possible fix:** Read the related-work section of [20] and add the tool-related modelling papers that bear on this thesis to the P3 reading list, with a card in `paper-review/` before any of them enter the prose. This is one of the backward-citation passes he asked for in the email.

**Depends on:** P3

**Your wording:**

```text

```

**Decision:**

```text

```

## C15 — [21] is not an independent broader discussion

**Status:** Done

**Kind:** Fact or citation

**Chapter:** 2.2.4 Modelling, tools, and model-driven engineering in education

**Highlighted sentence:**

> These findings align with broader discussions of human factors in model-driven engineering, which argue that educational tools should prioritise usability, cognitive support, constructive feedback, and alignment with learning goals over industrial feature completeness [21].

**His comment:**

> 21 is an opinion paper by a very selected group of people (among others, Miguel and me). It's a stretch to consider this "broader discussion" — especially since it's unsurprising that my own two papers align well with each other.

**In plain words:** You present his 2024 paper as outside confirmation of his 2017 paper. It is an opinion paper by a small group that includes him, so the agreement is not independent. Next: describe it as that group’s agenda, and do not use it as outside proof.

**Where it sits:** The first sentence of the second paragraph. “Broader discussions” and “align with” present [21] as outside confirmation of [20].

**Location:** `2-MainMatter/chapter2.tex`, second paragraph of `subsec:tools_mde_education`, `\cite{human-factors-mde}`. In the current bibliography this is [21]: Liebel, Klünder, Hebig, and others, including Goulão and Chakraborty, “Human factors in model-driven engineering: future research goals and initiatives for MDE”, *Software and Systems Modeling* (2024). He is the first author. [20] is also his.

**Possible fix:** Describe [21] as what it is: an opinion and agenda paper from that group, not a broader discussion and not independent support for [20]. If the paragraph needs outside agreement, that has to come from other tool papers, including the ones C14 points to.

**Depends on:** P3

**Your wording:**

```text

```

**Decision:**

```text
The sentence no longer says the 2017 findings "align with broader discussions". It now says that a later agenda paper by Liebel and colleagues argues for usability, feedback, and fit with learning goals over a full set of industrial features.
```

## C16 — “These insights inform…” does not say how

**Status:** Done

**Kind:** Structure

**Chapter:** 2.2.6 Implications for this thesis

**Highlighted sentence:**

> These insights inform the research questions and methodological choices of this thesis, which aims to investigate how students and teachers experience modelling, which challenges they perceive, and what kinds of support may foster the development of modelling competencies in realistic educational contexts.

**His comment:**

> How concretely?

**In plain words:** You say the literature shaped the research questions and the methods, but you never say which point shaped which choice. Next: name those links, or cut the sentence.

**Where it sits:** The last paragraph of subsection 2.2.6. The paragraph before it lists four implications. This sentence then says they inform the research questions and the methods, and restates the aim. It does not name which insight connects to which question or which method choice.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Implications for this thesis}` (`subsec:modelling_education_implications`), the paragraph that begins “These insights inform…”.

**Possible fix:** Replace the sentence with the concrete links, each in plain words: which point from the previous paragraph led to which research question, and which point led to a method choice such as the interview probes. If a link cannot be stated that concretely, cut it. Do not keep a sentence that only says the literature was informative.

**Depends on:** P2

**Your wording:**

```text

```

**Decision:**

```text
Deleted the closing paragraph of subsection 2.2.6, the sentence that began "These insights inform the research questions...". No replacement was written. The preceding paragraph of implications is still there and will be handled with the Background/Related Work split.
```

## C17 — Background drifts into Related Work

**Status:** Open

**Kind:** Structure

**Chapter:** 2 Background (side note on the 2.2.6 page)

**Highlighted sentence:**

> Side note on the Background chapter. No single sentence was marked.

**His comment:**

> I think the background needs work. You need to better introduce fundamental concepts. You do this early on (what is conceptual modelling? What is bloom's taxonomy?), but then drift off into related work.

**In plain words:** He is judging the whole Background chapter. The start does explain the basic ideas. After that, the chapter starts summarising papers, which is Related Work. Next: keep the definitions in Background and move the paper summaries. This is the same job as P2.

**Where it sits:** The chapter as a whole. He accepts the early concept introductions. The drift he is describing is the paper-by-paper material that starts in section 2.2 and continues through the implications in 2.2.6. The same pattern is what C8–C16 have been marking one passage at a time.

**Location:** `2-MainMatter/chapter2.tex`, `\chapter{Background}` (`cha:background`). The early concept passages he names are `\section{Software modelling \& conceptual modelling}` and the Bloom material. The drift is `\section{Modelling education}` and, on the same pattern, `\section{Human factors in modelling and SE education}`.

**Possible fix:** This is P2 in his words. Keep Background for definitions a later chapter needs. Move the paper summaries into Related Work. Do not answer this note by adding another implications subsection.

**Depends on:** P2

**Your wording:**

```text

```

**Decision:**

```text

```

## C18 — Two different aims

**Status:** Done

**Kind:** Structure

**Chapter:** 2.3.4 Implications for this thesis

**Highlighted sentence:**

> This thesis investigates how students and teachers experience software and conceptual modelling, and how they perceive challenges, learning processes, and support needs.

**His comment:**

> Earlier, you write "The aim of this thesis is to develop an empirically grounded account of modelling education challenges and support needs in higher education, treating modelling as a socio-technical activity that combines conceptual understanding, procedural strategies, and contextual influences." — That's not quite the same.

**In plain words:** This sentence states the aim differently from Chapter 1. One version is an account of challenges and support needs. This one is an investigation of experience, and it adds learning processes. Next: pick one aim and use it in both places.

**Where it sits:** The first sentence of subsection 2.3.4. It restates the aim. The earlier statement is the first paragraph of section 1.3, which is also C2.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Implications for this thesis}` (`subsec:gt_implications_thesis`), first sentence. The 1.3 wording is in `2-MainMatter/chapter1.tex`, `\section{Aim and research questions}` (`sec:intro_aim_rq`).

**Possible fix:** Keep one aim. The 1.3 version is an account of challenges and support needs, built from conceptual understanding, procedural strategies, and contextual influences. The 2.3.4 version is an investigation of experience, and it adds learning processes and both software and conceptual modelling. Make 2.3.4 use the same aim as 1.3, or change 1.3 if this sentence is the one you mean. C2 still needs that aim to say how the thesis differs from his studies.

**Depends on:** C2

**Your wording:**

```text

```

**Decision:**

```text
Subsection 2.3.4 now points at the section 1.3 aim: an account of challenges and support needs. It no longer says the thesis investigates experience of software and conceptual modelling, or learning processes.
```

## C19 — The socio-technical list overclaims the study

**Status:** Done

**Kind:** Structure

**Chapter:** 2.3.4 Implications for this thesis

**Highlighted sentence:**

> These are socio-technical questions that involve individual cognition, educational practices, tools, and organisational constraints, and they are not yet well theorised in the software modelling education literature.

**His comment:**

> This statement implies that you will try to do all those things — which is a pretty bold claim, given that you end up with 14 interviews that, as far as I can see, do not so much take into account "individual cognition" and "organisational constraints" either.

**In plain words:** The sentence lists cognition, teaching practices, tools, and organisational constraints, which reads as a promise that the study covers all of them. Fourteen interviews do not really cover individual cognition or organisational constraints. Next: keep only what the interviews can support.

**Where it sits:** The second sentence of subsection 2.3.4. It turns the research questions into four objects of study: individual cognition, educational practices, tools, and organisational constraints. It also says these are not yet well theorised.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Implications for this thesis}` (`subsec:gt_implications_thesis`), second sentence. The interview count is in `2-MainMatter/chapter1.tex`, section 1.4: four instructors and ten students.

**Possible fix:** Narrow the sentence to what the interviews actually cover. Educational practices and tools are in the interview scope. Individual cognition and organisational constraints are not, unless a later finding shows that they are. Drop “not yet well theorised” unless Related Work has shown that gap for the narrower claim. The sentence should justify Grounded Theory for the study you did, not for a larger study.

**Depends on:** C18

**Your wording:**

```text

```

**Decision:**

```text
The interviews did not cover individual cognition or organisational constraints, so those words are gone, along with "not yet well theorised." The subsection now says the interviews ask about a specific recent incident and how people dealt with it, including the practices and tools in that incident, and that STGT is used because the account is built from the interviews.
```

## C20 — Bloom comes after it has already been used

**Status:** Open

**Kind:** Structure

**Chapter:** 2.4 Bloom's Taxonomy and learning outcomes

**Highlighted sentence:**

> The words “Bloom's Taxonomy” in the section title.

**His comment:**

> You talked a lot about Bloom's taxonomy earlier. Therefore, I feel this comes too late.

**In plain words:** The section that explains Bloom arrives after the thesis has already used it at length. He wants the explanation first. Next: move the basic explanation of Bloom to before the passages that apply it, and leave a short pointer where this section stands now.

**Where it sits:** The title of section 2.4. Bloom is already used in section 1.4, and subsection 2.2.2 spends three paragraphs on Bloom levels, Bogdanova and Snoeck, and Bork before this section begins. Grounded Theory (section 2.3) sits between that use and this explanation.

**Location:** `2-MainMatter/chapter2.tex`, `\section{Bloom's Taxonomy and learning outcomes}` (`sec:blooms_taxonomy`). The earlier long use is `\subsection{Bloom-based perspectives on modelling learning outcomes}` (`subsec:bloom_perspectives_modelling_learning_outcomes`), which is C9.

**Possible fix:** Put the short explanation of Bloom’s revised taxonomy before 2.2.2. Keep 2.4 only if a later chapter still needs a definition that has not already been given. The paper findings about evaluation and reflection stay with C9, and under P2 they belong in Related Work rather than in a late concept section.

**Depends on:** P2 and C9

**Your wording:**

```text

```

**Decision:**

```text

```

## C21 — [16] is not about modelling, so [13] carries the subsection

**Status:** Open

**Kind:** Fact or citation

**Chapter:** 2.5.1 Motivation, engagement, and the "value" of modelling

**Highlighted sentence:**

> In modelling education, learners frequently report that motivation depends on whether tasks feel authentic, whether modelling outputs matter beyond grading, and whether modelling is integrated into a meaningful workflow rather than treated as a stand-alone academic exercise [13, 16].

**His comment:**

> 16 is on general SE education, not on modelling. Therefore, it feels that most statements in this section rely on 13, which is quite thin.

**In plain words:** Citation 16 is about software engineering education in general, not about modelling, so it does not support these modelling claims. Once that cite is set aside, almost every statement in the subsection rests on citation 13. That paper is now published (FSE Companion 2026); it is still one source. Next: stop using 16 for the modelling point, and do not let 13 carry the whole subsection. Either add other modelling sources or cut the subsection back to what 13 can support.

**Where it sits:** The phrase “whether modelling outputs” in the third sentence of subsection 2.5.1. That sentence cites both papers. The other sentences in the subsection cite only [13].

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Motivation, engagement, and the ``value'' of modelling}` (`subsec:hf_motivation_value`). [13] is `grassl2026dei`, now the published FSE Companion 2026 paper he co-authored. [16] is `holmes2018dimensions`: Holmes, Allen, and Craig, “Dimensions of Experientialism for Software Engineering Education”, ICSE-SEET 2018. The same reliance on [13] continues in subsection 2.5.2.

**Possible fix:** Keep [16] only for a claim about experiential software engineering education, and say that this is what it is. Do not attach it to “modelling outputs”. For the modelling claims, [13] alone is too thin, and it is not a published paper. Bring in other modelling-education sources, or shorten the subsection to the claim [13] can actually carry. This is part of the reading pass in P3.

**Depends on:** P3

**Your wording:**

```text

```

**Decision:**

```text
Holmes (2018) was removed from the sentence about modelling outputs in subsection 2.5.1. The sentence now cites only grassl2026dei. The thinness of that one paper is still open for Wave F. Other Holmes citations, where the claim is about experiential software engineering education rather than modelling outputs, were left in place.
```

## C22 — Inclusion and domain diversity rest only on [13]

**Status:** Open

**Kind:** Fact or citation

**Chapter:** 2.5.2 Inclusion, domain diversity, and participation barriers

**Highlighted sentence:**

> The words “inclusion, domain diversity” in the subsection title.

**His comment:**

> Again, only relying on [13].

**In plain words:** This subsection is the same problem as C21. Inclusion and domain diversity are supported only by citation 13. That paper is now published, and it is still the only source for the subsection. Next: add other sources, or cut the subsection back to the one claim that paper can carry.

**Where it sits:** The title of subsection 2.5.2. Both paragraphs cite only `grassl2026dei`.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Inclusion, domain diversity, and participation barriers}` (`subsec:hf_inclusion_domain`). [13] is the same Graßl et al. paper as in C21, now published.

**Possible fix:** Do not give inclusion and domain diversity their own subsection on the strength of [13] alone. Either bring in other work on those topics, or fold the one supportable claim into a shorter passage. Publication no longer needs a hedge: [13] is the FSE Companion 2026 paper.

**Depends on:** P3 and C21

**Your wording:**

```text

```

**Decision:**

```text

```

## C23 — Tools subsection repeats [20]

**Status:** Done

**Kind:** Structure

**Chapter:** 2.5.3 Tools as mediators of learning experience

**Highlighted sentence:**

> The whole subsection title, “Tools as mediators of learning experience”.

**His comment:**

> How is this sub-section different from your earlier coverage of [20]?

**In plain words:** This subsection tells the same study again. [20] was already summarised earlier: tool perceptions depend on the course, and UML is viewed more positively when models are used for analysis and communication rather than only for code generation. Next: keep one account of that study, and delete the repeat.

**Where it sits:** The title of subsection 2.5.3. The first paragraph is general. The second paragraph retells `liebel2017model`, which is [20]. The earlier telling is subsection 2.2.4, which is C12–C15.

**Location:** `2-MainMatter/chapter2.tex`, `\subsection{Tools as mediators of learning experience}` (`subsec:hf_tools_mediator`). The earlier coverage is `\subsection{Modelling, tools, and model-driven engineering in education}` (`subsec:tools_mde_education`).

**Possible fix:** Merge the two passages. One summary of [20] is enough. If 2.5.3 has a point that 2.2.4 does not — tools as part of the learning experience rather than as course infrastructure — state that point in a sentence and do not retell the study. Under P2, the remaining summary belongs in Related Work.

**Depends on:** P2 and C14

**Your wording:**

```text

```

**Decision:**

```text
Subsection 2.5.3 no longer retells [20]. It now states only that tools shape how easily students can try ideas, get feedback, and recover from mistakes, and points back to Section 2.2.4 for the study. The summary of [20] stays in 2.2.4 until P2 moves paper summaries into Related Work.
```

## C24 — Related Work repeats Background

**Status:** Open

**Kind:** Structure

**Chapter:** 3 Related Work

**Highlighted sentence:**

> Chapter-level comment. No single sentence was marked. He is not commenting inside the chapter.

**His comment:**

> I won't read this in detail for now. But the same criticism applies here as in earlier statements: You again discuss the same papers that you use in the background. Therefore, the question arises to what extent this is redundant.

**In plain words:** He stopped at the start of Related Work. The chapter goes back over the same papers as Background, so he does not see a separate job for it. Next: give each paper one home. Background keeps the definitions. Related Work keeps the research, and it has to add papers that Background does not already summarise. That is P2 and P3 together.

**Where it sits:** The whole of Chapter 3. The repeat is already marked passage by passage in Background: Maslov (C8), Bloom and the evaluation finding (C9), the iStar study (C11), tools and [20] (C12, C23), [21] (C15), and the human-factors material that rests on [13] (C21, C22).

**Location:** `2-MainMatter/chapter3.tex`, `\chapter{Related Work}` (`cha:related_work`). The overlapping Background material is `\section{Modelling education}` and `\section{Human factors in modelling and SE education}` in `2-MainMatter/chapter2.tex`.

**Possible fix:** Do not revise Chapter 3 sentence by sentence while it still retells Chapter 2. After the Background paper summaries move here, delete the second telling. Then widen the chapter with the reading pass in P3, so Related Work is not only the papers Background already used. He has not given inline comments on this chapter, so there is nothing finer to apply until that split is done.

**Depends on:** P2, P3, and C17

**Your wording:**

```text

```

**Decision:**

```text

```

## C25 — Use the STGT acronym

**Status:** Done

**Kind:** Wording

**Chapter:** 4 Methodology

**Highlighted sentence:**

> The analysis follows Socio-Technical Grounded Theory (STGT) as adapted for software engineering [15, 28].

**His comment:**

> You introduced this acronym earlier. Use it.

**In plain words:** The full name and the acronym are given again at the start of the methods chapter. He already met STGT in the Background. Next: write STGT here, and do not spell it out again.

**Where it sits:** The third sentence of the chapter opening. The acronym is introduced in Background, subsection 2.3.3, “Socio-Technical Grounded Theory”.

**Location:** `2-MainMatter/chapter4.tex`, the unnumbered paragraph under `\chapter{Methodology}`, the sentence that begins “The analysis follows Socio-Technical Grounded Theory (STGT)…”. The first expansion is in `2-MainMatter/chapter2.tex`, `\subsection{Socio-Technical Grounded Theory}` (`subsec:stgt`).

**Possible fix:** Replace the full name in this sentence with STGT. Leave the expansion in Background, once.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
The Chapter 4 opening now says "The analysis follows STGT as adapted for software engineering". The full name remains in Background, subsection 2.3.3.
```

## C26 — Describe what was done

**Status:** Done

**Kind:** Structure

**Chapter:** 4 Methodology

**Highlighted sentence:**

> The chapter describes the procedure that was actually used—open coding, short analytical memos, constant comparison, and category development—rather than a formal Strauss–Corbin axial coding paradigm.

**His comment:**

> Skip this. I would hope that you actually describe what you did, instead of other things.

**In plain words:** The opening spends a sentence on what the study did not do: Strauss and Corbin’s axial coding. He wants that sentence gone. The methods chapter should describe the procedure that was used. Next: delete this sentence from the opening. The same contrast is repeated later in the coding subsection; that repeat should go too unless a reader of this thesis needs it.

**Where it sits:** The last sentence of the chapter opening. A longer version of the same contrast is in the coding subsection: the study did not apply Strauss and Corbin’s axial coding paradigm as a formal stage.

**Location:** `2-MainMatter/chapter4.tex`, the opening paragraph of `\chapter{Methodology}`. The later repeat is in `\subsection{Grounded Theory variant and socio-technical stance}`, the paragraph that begins “The procedure was a lightweight STGT workflow…”.

**Possible fix:** Cut the “rather than Strauss–Corbin” sentence from the opening. Keep the list of what was done — open coding, short memos, constant comparison, and category development — only as a pointer to the section that actually describes those steps. Cut or shorten the later paragraph that explains the paradigms that were not used.

**Depends on:** P1

**Your wording:**

```text

```

**Decision:**

```text
Deleted the whole last sentence of the Chapter 4 opening, from "The chapter describes" through the Strauss–Corbin contrast. The opening now ends with "The analysis follows STGT as adapted for software engineering." The later contrast in the coding subsection stays until C47.
```

## C27 — Say STGT, not a longer Grounded Theory formula

**Status:** Done

**Kind:** Wording

**Chapter:** 4.1 Research design

**Highlighted sentence:**

> The study used a qualitative, theory-building design based on Grounded Theory (GT) as adapted for software engineering research [1, 28].

**His comment:**

> Be precise instead of using many words: You use STGT.

**In plain words:** The sentence uses several labels for the method. He wants one: STGT. Next: replace this opening with a direct statement that the study used STGT.

**Where it sits:** The first sentence of section 4.1. The chapter opening already names STGT, which is C25.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Research design}` (`sec:method_design`), first sentence. The citations are `adolph2011using` and `stol2016grounded`.

**Possible fix:** Open the section with STGT. If Adolph or Stol still needs to be cited, cite them for the specific procedure they support, not as a second name for the method.

**Depends on:** C25

**Your wording:**

```text

```

**Decision:**

```text
Section 4.1 now opens with "The study used STGT." Adolph and Stol are cited on the wave-1 and wave-2 sampling procedure, not as a second name for the method.
```

## C28 — “Informed by STGT” is unclear

**Status:** Done

**Kind:** Structure

**Chapter:** 4.1 Research design

**Highlighted sentence:**

> To attend to the interplay between social and technical elements in modelling education (students and instructors, teaching practices, notations, tools, and artefacts), the analysis was informed by STGT [15].

**His comment:**

> What does this mean? Did you use STGT or not? If you did not use the whole STGT, don't just write "informed by", but state which parts you used, and which not (and why).

**In plain words:** “Informed by” does not say whether the study used STGT. He wants a yes or a no. If only some parts were used, the sentence has to name those parts, name the parts that were not used, and say why. Next: replace “informed by” with that account. C27 already asks for a direct “the study used STGT”, so the two sentences have to agree.

**Where it sits:** The second sentence of section 4.1. The first sentence says the design is based on Grounded Theory. This sentence then says the analysis was only informed by STGT.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Research design}` (`sec:method_design`), second sentence, `\cite{hoda2018socio}`.

**Possible fix:** State the parts of STGT that were used, such as open coding, memos, constant comparison, and theoretical sampling, and the parts that were not, with a reason for each omission. Do not leave “informed by” as the only description. Keep this consistent with C27.

**Depends on:** C27

**Your wording:**

```text

```

**Decision:**

```text
"Informed by" is gone. Section 4.1 names the parts used (open coding, memos, constant comparison throughout, theoretical sampling, attention to practices and tools) and the part not used (Strauss and Corbin's axial coding paradigm), with the reason already given in the analysis section: categories were related through constant comparison and a findings map. The longer variant paragraph in 4.5.1 stays until C47.
```

## C29 — How did the iStar study inform the design?

**Status:** Done

**Kind:** Structure

**Chapter:** 4.1 Research design

**Highlighted sentence:**

> That study used a tutorial and a modelling session before the interview. The present work did not replicate that activity.

**His comment:**

> So your design was informed by 19, but you didn't do what they did? How did the study inform you then?

**In plain words:** The paragraph says the design was informed by the iStar study, then says you did not do what that study did. He cannot see what was taken from it. Next: say what you actually took from that study, or drop the “informed by” claim.

**Where it sits:** The second and third sentences of the second paragraph of section 4.1. The paragraph opens with “The design was also informed by… the iStar learning study [19].” [19] is Li et al. (2025), the same study as C4.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Research design}` (`sec:method_design`), second paragraph, `\cite{istar-learning}`.

**Possible fix:** Name the concrete borrow. If the borrow is only the idea of asking about a recent modelling episode, say that, and say that the tutorial and the modelling session were not used. If nothing procedural was taken, delete “informed by”. The same unnamed study appears in Chapter 1, which is C4.

**Depends on:** C4

**Your wording:**

```text

```

**Decision:**

```text
Section 4.1 no longer says the design was informed by Li et al. It says the thesis took a grounded-theory approach, the revised Bloom taxonomy, and interviews with both lecturers and students. The grounded-theory approach is STGT, not their Strauss and Corbin paradigm. Their tutorial, modelling session, and prototype tool were not used. The interview wording is a specific recent incident the participant could recall, and how they dealt with it. When Bloom was used is still C43, C50, and C51.
```

## C30 — Research questions are not hypotheses

**Status:** Done

**Kind:** Wording

**Chapter:** 4.2 Research questions and operational focus

**Highlighted sentence:**

> Each research question was treated as something to explore rather than a hypothesis to test.

**His comment:**

> They're questions, not hypotheses. No need to state this. This comment was crossed, not highlighted, so the sentence should be removed.

**In plain words:** The sentence explains that the research questions are not hypotheses. He thinks that is obvious. The mark was a cross, not a highlight, so he wants the sentence deleted. Next: delete it.

**Where it sits:** The first sentence of the paragraph after the research-question list in section 4.2.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Research questions and operational focus}` (`sec:method_rq`).

**Possible fix:** Delete the sentence. Leave the next sentences, which say what each research question focused on.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
Deleted. The paragraph in section 4.2 now starts with "RQ1 focused on characterising challenges...".
```

## C31 — “Coping strategies” sounds psychological

**Status:** Done

**Kind:** Wording

**Chapter:** 4.2 Research questions and operational focus

**Highlighted sentence:**

> RQ2 focused on coping strategies and articulated support needs, including the conditions under which particular forms of support were seen as helpful.

**His comment:**

> "Coping strategies are the thoughts, actions, and behaviors you use to manage stress, emotional pain, and difficult life events." — is this really what you mean?

**In plain words:** “Coping strategies” is a term from psychology: how people handle stress and pain. He is asking whether that is what you mean. In this thesis it means what students and instructors did when modelling got difficult. Next: use words that say that, such as the strategies they used, and do not leave “coping” to carry the meaning.

**Where it sits:** The RQ2 sentence in section 4.2. The same phrase is in RQ2 itself, in the list above this paragraph, and in Chapter 1.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Research questions and operational focus}` (`sec:method_rq`). RQ2 in that section, and the matching RQ2 in `2-MainMatter/chapter1.tex`, both say “coping strategies”.

**Possible fix:** Rename the thing. If you mean the practical steps people took when a modelling task was hard, say that. Check every “coping” in the research questions so Chapter 1 and Chapter 4 use the same words.

**Depends on:** none

**Your wording:**

```text
strategies for dealing with these challenges
```

**Decision:**

```text
Replaced "coping strategies" with "strategies for dealing with these challenges" in Chapter 1 (the RQ gloss and the contributions), Chapter 4 section 4.2, and the appendix guide description. The RQ2 question itself already said "strategies ... to address these challenges" and was left as it is. Two wordings inside the interview script were left: the spoken opening that says "coping strategies/support needs", and the probe note "coping response".
```

## C32 — Appendix A.3 is not the interview guide

**Status:** Done

**Kind:** Structure

**Chapter:** 4.2 Research questions and operational focus

**Highlighted sentence:**

> Appendix A.3 lists which main prompts speak to which research question.

**His comment:**

> That doesn't look like an interview guide to me. Do you have an interview guide with concrete questions you asked?

**In plain words:** The sentence sends him to Appendix A.3. That section is a table mapping short question labels to research questions, not the questions themselves. He wants the actual questions that were asked. Next: point this sentence at the guide, and make sure that guide is the list of concrete questions used in the study.

**Where it sits:** The last sentence of section 4.2. Appendix A.3 is the section “Mapping of interview questions to research questions”. The concrete prompts are earlier in the same appendix, titled as pilot guides for instructors and students.

**Location:** `2-MainMatter/chapter4.tex`, the `\ref{app:rq_mapping}` sentence. The appendix is `3-BackMatter/appendix_interviews.tex`: the guides are `\chapter{Pilot interview guides}`, and the mapping he was sent to is `\section{Mapping of interview questions to research questions}` (`app:rq_mapping`).

**Possible fix:** Cite the interview-guide sections for the questions, and cite A.3 only as the mapping. If those guides are still labelled “pilot”, say whether they are the questions that were actually asked. Section 4.5 later points at the same guides, so the two sentences have to agree.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
Section 4.2 now points at the instructor guide and the student guide for the questions, and at the mapping section only for which prompts address which research question. The interviews subsection uses the same two guide references, so it no longer sends the reader to the appendix chapter as if that chapter were the guide.
```

## C33 — “Speak to” is unclear

**Status:** Done

**Kind:** Wording

**Chapter:** 4.2 Research questions and operational focus

**Highlighted sentence:**

> which main prompts speak to which research question.

**His comment:**

> ?

**In plain words:** “Speak to” does not say what the appendix does. He cannot tell what relation you mean between a prompt and a research question. Next: say that the appendix shows which interview question was meant to address which research question.

**Where it sits:** The same sentence as C32. This comment is only on the wording “speak to”. C32 is about where the sentence points.

**Location:** `2-MainMatter/chapter4.tex`, the last sentence of `\section{Research questions and operational focus}` (`sec:method_rq`).

**Possible fix:** Replace “speak to” with a plain verb, such as “address” or “were written for”. Do this when the sentence is repointed for C32.

**Depends on:** C32

**Your wording:**

```text

```

**Decision:**

```text
"Speak to" is now "address" in the mapping sentence.
```

## C34 — “Related” to what?

**Status:** Done

**Kind:** Wording

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> The study was conducted in higher-education software engineering and related courses that include software modelling (for example requirements engineering, software design, business process modelling, or model-driven engineering).

**His comment:**

> Related to what?

**In plain words:** “Related courses” has no anchor. Related to software engineering, or to modelling? Next: name the courses, or say “courses that teach software modelling” and drop “related”.

**Where it sits:** The first sentence of section 4.3, on the word “related”.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Study context and participants}` (`sec:method_context_participants`), first sentence.

**Possible fix:** Replace “software engineering and related courses” with an explicit list or with “courses that include software modelling”. The examples already in parentheses can do that work.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
The opening of section 4.3 now says "higher-education software engineering courses and in other courses that include software modelling", followed by the same examples. "Related" is gone.
```

## C35 — Software modelling or conceptual modelling?

**Status:** Backlog

**Kind:** Structure

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> courses that include software modelling

**His comment:**

> software or conceptual modelling? If software modelling, why does the background go so deep into conceptual modelling?

**In plain words:** The methods chapter says the courses teach software modelling. The Background spends a long time on conceptual modelling, which you defined more broadly. He wants those two to match. Next: say which one the study is about. If it is software modelling, the conceptual-modelling material in Background has to be cut back to what this study uses.

**Where it sits:** The same opening sentence as C34, on “software modelling”. This is the scope question from C12, now asked of the study itself.

**Location:** `2-MainMatter/chapter4.tex`, first sentence of `sec:method_context_participants`. The broader definition is section 2.1 in `2-MainMatter/chapter2.tex`.

**Possible fix:** State the scope in this sentence and keep it. If the interviews are about software modelling courses, say so, and reduce the conceptual-modelling survey in Background to the ideas those courses actually use. If both are in scope, say what “both” means here.

**Depends on:** P2 and C12

**Your wording:**

```text

```

**Decision:**

```text
Deferred. The thesis is about software modelling, so conceptual modelling in Background should get less emphasis, not be removed. That trim waits for Wave E, when Background is rewritten. It is backlog item 3. Section 4.3 is left as it is.
```

## C36 — Lecturers or instructors?

**Status:** Done

**Kind:** Wording

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> Fourteen interviews were completed: four lecturers (L1--L4) and ten students (S1--S10).

**His comment:**

> consistency: You use "instructors" above.

**In plain words:** The bullet above calls this group instructors. The next paragraph calls them lecturers. He wants one word. Next: pick one term and use it for this group throughout.

**Where it sits:** The sentence that gives the interview counts. The instructor bullet is two sentences earlier. The participant table then uses “Lecturer” in the role column.

**Location:** `2-MainMatter/chapter4.tex`, `sec:method_context_participants`, and Table `tab:participants`.

**Possible fix:** Choose “instructors” or “lecturers” and use that word in the prose, the bullets, and the table. If lecturers and teaching assistants are both included, say that once and then use the chosen cover term.

**Depends on:** none

**Your wording:**

```text
lecturers
```

**Decision:**

```text
Section 4.3 now uses lecturers. The bullet no longer says "Instructors: lecturers or teaching assistants." The participant table already said Lecturer. The rest of Chapter 4 still says instructors, including the research questions and the interview-guide paragraphs.
```

## C37 — “Corpus” is unexplained

**Status:** Done

**Kind:** Wording

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> Table 4.1 summarises the corpus in general terms.

**His comment:**

> ?

**In plain words:** “Corpus” is jargon here. He cannot tell what is being summarised. Next: say “the 14 interviews” or “the participants”.

**Where it sits:** The sentence that introduces the participant table.

**Location:** `2-MainMatter/chapter4.tex`, `sec:method_context_participants`, the sentence containing “summarises the corpus”. The table is `tab:participants`.

**Possible fix:** Replace “corpus” with “14 interviews” or “participants”.

**Depends on:** P1

**Your wording:**

```text

```

**Decision:**

```text
Section 4.3 now says the table summarises the 14 interviews. The table caption is "The 14 interviews (anonymised)." Later uses of "corpus" for the coded transcripts were left unchanged.
```

## C38 — Waves are used before they are explained

**Status:** Done

**Kind:** Structure

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> Wave 2 added students at Instituto Superior Técnico (IST; S7, S10), Instituto Superior de Engenharia de Lisboa (ISEL; S8), and one further Portuguese student (S9).

**His comment:**

> What waves? You did not discuss this before.

**In plain words:** “Wave 2” is used as if the reader already knows that the interviews were collected in two rounds. Section 4.1 mentions waves once, in one clause, and never says what a wave is. Next: explain the two rounds before this paragraph uses them, in a sentence or two: who was in the first round, and why a second round was recruited.

**Where it sits:** The Wave 2 sentence in the participant paragraph. The table also has a Wave column. The only earlier mention is in section 4.1: “wave 1 interviews seeded categories, and wave 2 recruitment was directed at open questions”.

**Location:** `2-MainMatter/chapter4.tex`, `sec:method_context_participants`. The earlier mention is the last sentence of the first paragraph of `sec:method_design`. The later account is `\subsection{Theoretical sampling}` (`subsec:method_sampling_saturation`).

**Possible fix:** Add a short explanation before the first use in this section. Point forward to the sampling subsection for the detail, but do not leave “Wave 2” undefined here. C40 asks for the recruitment itself.

**Depends on:** C40

**Your wording:**

```text

```

**Decision:**

```text
Section 4.3 now defines wave 1 as L1–L4 and S1–S6, and wave 2 as S7–S10, before the sentence that names institutions. The second round is a further set of interviews after the first ten had been coded, because open questions remained. It is not described as a sample picked to match each open question.
```

## C39 — The inclusion sentence is unclear

**Status:** Done

**Kind:** Wording

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> Inclusion emphasised direct experience with modelling tasks, so that accounts could stay close to concrete incidents.

**His comment:**

> What does this mean?

**In plain words:** The sentence does not say who was included or what rule was applied. “Inclusion emphasised” and “accounts could stay close to concrete incidents” are vague. Next: say the rule in plain words, for example that a participant had to have done a modelling task in a course, because the interview asked about a specific episode.

**Where it sits:** The paragraph immediately above the participant table. In the printed thesis that table is Table 4.1. The sentence is not inside the table.

**Location:** `2-MainMatter/chapter4.tex`, `sec:method_context_participants`, the paragraph that begins “Inclusion emphasised…”.

**Possible fix:** State the inclusion rule directly. The student bullet above already says they had completed at least one modelling assignment. Use that rule here, or cut this sentence if the bullets already say it.

**Depends on:** P1

**Your wording:**

```text

```

**Decision:**

```text
The sentence now says the interviews were more useful when a participant could still describe a modelling task they remembered closely, and that weak recall or modelling from a long time ago gave less to say about a specific episode. It does not say those people were excluded. S7 and S9 remain in the corpus, and section 4.8 already says they described courses from years earlier.
```

## C40 — How were participants selected and recruited?

**Status:** Done

**Kind:** Structure

**Chapter:** 4.3 Study context and participants

**Highlighted sentence:**

> Side note at the end of section 4.3, or at the start of section 4.4. No single sentence was marked.

**His comment:**

> How was sampling done? I.e., how did you select and recruit participants?

**In plain words:** The section says who was interviewed and where they studied. It does not say how they were found or invited. Next: add a short account of selection and recruitment: who was asked, how they were contacted, and what made someone eligible.

**Where it sits:** The end of section 4.3. Section 4.4 starts data collection and also does not describe recruitment. A later subsection, “Theoretical sampling”, says the second round was chosen to fill open questions. It still does not say how people were contacted.

**Location:** `2-MainMatter/chapter4.tex`, end of `sec:method_context_participants`. The later sampling subsection is `subsec:method_sampling_saturation`.

**Possible fix:** Add the recruitment account at the end of 4.3, before the participant table is asked to stand in for it. Keep the later subsection for why the second round was needed, which is C38. Do not answer this note with only the theoretical-sampling figure.

**Depends on:** C38

**Your wording:**

```text

```

**Decision:**

```text
Section 4.3 now says recruitment was through course and personal contacts. Wave 1 students were colleagues from a software modelling course, one student whose thesis was modelling-related, and students reached through an Erasmus contact. Lecturers were emailed directly; the addresses came through a coordinator. Wave 2 students were contacts who had finished a computer science degree and who confirmed they had done software modelling. No further lecturers were asked. Section 4.1 and the sampling subsection no longer say those four students were recruited against the open questions. Personal details that would identify people were left out.
```

## C41 — “Incident probes” is still undefined

**Status:** Done

**Kind:** Wording

**Chapter:** 4.4 Data collection

**Highlighted sentence:**

> Guides included incident probes that asked for one recent assignment, laboratory, or the first minutes of a text-to-model task, so that talk stayed closer to practice than to general opinion.

**His comment:**

> You keep using this term, but what does it mean?

**In plain words:** “Incident probes” has already appeared in the introduction, and it is still jargon. He wants to know what the interviewer asked. The sentence does list examples, but the term itself is doing the work. Next: say in ordinary words that the guide asked the participant to describe one recent concrete episode, and then use that plain description instead of the label. This is the same term as C3.

**Where it sits:** The first paragraph of section 4.4. The same term is in section 1.4, which is C3, and again in subsection 4.4.2, “Incident-based probing”.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Data collection}` (`sec:method_data_collection`), the sentence that begins “Guides included incident probes…”. The later explanation is `\subsection{Incident-based probing}` (`subsec:method_modelling_task`).

**Possible fix:** Define the ask in plain words at the first use in this chapter, and use those words afterwards. Point to subsection 4.4.2 for the detail if it stays, but do not make the reader wait until that subsection to learn what the term means. When C3 is rewritten, use the same words.

**Depends on:** C3 and P1

**Your wording:**

```text

```

**Decision:**

```text
Section 4.4 now uses the Chapter 1 wording: the questions asked each participant to describe a specific episode, such as a recent assignment, a laboratory, or the start of turning a text into a model. The same plain wording replaced earlier uses in Chapter 2 and in section 4.1, which would otherwise still have said "incident probes" before this section.
```

## C42 — Backbone or spine?

**Status:** Done

**Kind:** Wording

**Chapter:** 4.4 Data collection

**Highlighted sentence:**

> Wave 2 student interviews used the same student spine, with extra probes aimed at the open questions left by wave 1.

**His comment:**

> You keep using different words for the same thing. Stay consistent. Earlier, it was "backbone" (but then it referred to differences between instructors and students).

**In plain words:** “Spine” and “backbone” are two words for the shared part of the interview guide. “Backbone” was used for what students and instructors had in common. “Student spine” then sounds like a student-only structure. Next: pick one word, and say whether you mean the shared questions or the student guide.

**Where it sits:** The second paragraph of section 4.4. The previous paragraph says the two guides had “a shared backbone” and different emphases for students and instructors.

**Location:** `2-MainMatter/chapter4.tex`, `sec:method_data_collection`. “Backbone” is in the first paragraph of that section. “Student spine” is in the next paragraph.

**Possible fix:** Use one term. If the second paragraph means the student guide’s shared questions, say “the same student guide” or “the same shared questions”. Do not introduce “spine”.

**Depends on:** C36

**Your wording:**

```text
the same shared questions
```

**Decision:**

```text
Wave 2 now says "the same shared questions". The previous paragraph no longer says "shared backbone"; it says "shared questions", with the same list of topics.
```

## C43 — Show the questions and the Bloom link

**Status:** Done

**Kind:** Structure

**Chapter:** 4.4.1 Interview guides and pilot

**Highlighted sentence:**

> Bloom-based modelling frameworks informed the formulation of prompts by mapping modelling competence to observable activities (interpreting models, constructing models from text, judging model quality), supporting broad coverage of cognitive demands without imposing Bloom as a coding template.

**His comment:**

> Please provide the concrete questions you asked, and how they relate to Bloom's (revised) taxonomy.

**In plain words:** The sentence says Bloom shaped the questions, but it does not show the questions or which Bloom level each one belongs to. The questions are in the appendix, and the appendix table maps them to research questions, not to Bloom. Next: point to the questions, and add a mapping from each question to Bloom’s revised taxonomy, or drop the Bloom claim.

**Where it sits:** The second sentence of subsection 4.4.1. The concrete prompts are in `3-BackMatter/appendix_interviews.tex`, in the instructor and student guide sections. Appendix A.3, which is C32, maps those prompts to RQ1–RQ3 only.

**Location:** `2-MainMatter/chapter4.tex`, `\subsection{Interview guides and pilot}` (`subsec:method_instruments_pilot`).

**Possible fix:** In this subsection, point to the guide and add a column or a short list that says which Bloom level each main prompt was written for. If that mapping cannot be reconstructed, delete the claim that Bloom informed the prompts. C20 asks for Bloom to be explained earlier. This comment asks for the link to the actual questions.

**Depends on:** C20 and C32

**Your wording:**

```text

```

**Decision:**

```text
The full one-level-per-question map was not possible. Subsection 4.4.1 now says some questions were aimed at remembering a notation, understanding a construct, applying a procedure, and judging a model, and that not every question belongs to one level. Table tab:bloom_prompts lists four prompts: student Q5 (remember, understand, and apply), student Q6 (apply), student Q7 (evaluate), and instructor Q5 (understand and apply). Analyse and create have no prompt of their own. When Bloom was used in the analysis is still C50 and C51.
```

## C44 — Pilot interviews were kept after the guide changed

**Status:** Done

**Kind:** Structure

**Chapter:** 4.4.1 Interview guides and pilot

**Highlighted sentence:**

> Pilot interviews were retained in the final dataset (S1 and S2 appear as ordinary student cases) once the protocol had stabilised; their original role was to validate the protocol, not to stand as a separate subsample.

**His comment:**

> This does not make sense to me. You used the pilot interviews to reach a "stable" protocol (interview guide?), which implies that there were changes. But then you retained them anyway (which would imply you used interviews with a different interview guide in your final data)?

**In plain words:** The pilot was used to settle the interview guide, so the guide changed. S1 and S2 were still kept in the final 14 interviews. That reads as if those two interviews used an earlier guide than the rest. Next: say what changed after S1 and S2, and why those two interviews can still be analysed with the others. If the changes were small, say what stayed the same. If they were large, do not treat S1 and S2 as ordinary cases without saying so.

**Where it sits:** The last sentence of the second paragraph of subsection 4.4.1. The sentence before it says the pilot refined wording, ordering, and probing.

**Location:** `2-MainMatter/chapter4.tex`, `subsec:method_instruments_pilot`. S1 and S2 are the first two student rows in Table `tab:participants`.

**Possible fix:** State the sequence in plain words: what the guide looked like for S1 and S2, what was changed, and the reason those interviews remain in the dataset. Use one word for the guide, not both “protocol” and “interview guide”, unless you say they are the same thing.

**Depends on:** C32

**Your wording:**

```text

```

**Decision:**

```text
The early student guide in git (before the A/B/C variants) already asked for a useful moment, a frustrating moment, what the student did then, text-to-model steps, tools, and domains. Later files add more direct incident questions and extra probes (groups, cross-notation switching, course load, and similar). Subsection 4.4.1 now says that. S1 and S2 stay because they already answered the shared questions. "Protocol" is no longer used for the guide. The working names Guide A/B/C are not in the thesis.
```

## C45 — Incident probing is explained too late

**Status:** Done

**Kind:** Structure

**Chapter:** 4.4.2 Incident-based probing

**Highlighted sentence:**

> The subsection title, “Incident-based probing”.

**His comment:**

> This comes too late. You already used this term in the introduction.

**In plain words:** The place that explains the term is here, in the methods chapter. He already met “incident probes” in the introduction and did not know what it meant. Next: explain it at the first use, in ordinary words, and keep this subsection as the detailed account rather than as the first definition. This is the same term as C3 and C41.

**Where it sits:** The title of subsection 4.4.2. The earlier uses are section 1.4 and the opening of section 4.4.

**Location:** `2-MainMatter/chapter4.tex`, `\subsection{Incident-based probing}` (`subsec:method_modelling_task`). The introduction use is in `2-MainMatter/chapter1.tex`, `sec:intro_approach`.

**Possible fix:** At the first use in Chapter 1, say what was asked. Do not wait until this subsection for the meaning. This subsection can then describe the kinds of episode without introducing the idea for the first time.

**Depends on:** C3 and C41

**Your wording:**

```text

```

**Decision:**

```text
The introduction no longer uses the term, so the comment "you already used this term in the introduction" no longer applies. Chapter 2 and section 4.1 were also changed, because those were still earlier uses. The subsection title "Incident-based probing" is now the first time that label appears. The plain account of what was asked is already in Chapter 1 and again in section 4.4, before this subsection. Two later mentions remain, inside this subsection and in section 4.6, after the reader has the plain account.
```

## C46 — “Critical-incident questions” is undefined

**Status:** Done

**Kind:** Wording

**Chapter:** 4.4.2 Incident-based probing

**Highlighted sentence:**

> These prompts are critical-incident questions inside the interview.

**His comment:**

> Meaning what?

**In plain words:** “Critical-incident questions” is a new technical label for the same prompts. He wants the plain meaning. Next: say what the question asked the participant to do, and do not add a second name unless you explain it in the same sentence.

**Where it sits:** The second sentence of subsection 4.4.2. The sentence before it already lists the episodes: a recent assignment or lab, the first minutes of going from a text to a model, or a classroom moment when students struggled.

**Location:** `2-MainMatter/chapter4.tex`, `subsec:method_modelling_task`.

**Possible fix:** Delete “critical-incident questions”, or replace it with one plain clause: questions that ask for a specific episode rather than a general opinion. The next sentence already says they are not a second data-collection procedure. That point can stay if it is still needed after C45.

**Depends on:** C45 and P1

**Your wording:**

```text
questions that ask for a specific episode
```

**Decision:**

```text
Subsection 4.4.2 now says "These prompts are questions that ask for a specific episode inside the interview." The next sentence, that they are not a second data-collection procedure, stays.
```

## C47 — The GT variant belongs in the study design

**Status:** Done

**Kind:** Structure

**Chapter:** 4.5.1 Grounded Theory variant and socio-technical stance

**Highlighted sentence:**

> The words “Grounded Theory variant” in the subsection title.

**His comment:**

> the overall variant of GT used relates to the overall study design, not just the analysis. You should discuss it there, not here specifically.

**In plain words:** Which kind of Grounded Theory you used is a decision about the whole study, not a detail of the coding section. He wants that discussion in the research-design section. Next: move the choice of variant to section 4.1, and leave this subsection for how that choice showed up in the analysis.

**Where it sits:** The title of subsection 4.5.1, under “Data analysis”. Section 4.1 already starts the method description, but it says “based on Grounded Theory” and “informed by STGT”, which is C27 and C28.

**Location:** `2-MainMatter/chapter4.tex`, `\subsection{Grounded Theory variant and socio-technical stance}` (`subsec:method_gt_variant`), inside `\section{Data analysis}` (`sec:method_analysis`). The design section is `\section{Research design}` (`sec:method_design`).

**Possible fix:** Put the variant — STGT, and which parts were used — in section 4.1, as C27 and C28 already require. In 4.5.1, keep only the consequences for coding: what was compared, how social and technical elements were coded together, and what was not done. Do not introduce the variant for the first time here.

**Depends on:** C27 and C28

**Your wording:**

```text
An open code was a separate note for one matter, such as the notation, the tool, the teaching, or the feedback. Those stayed separate notes even when the participant had described them in one episode. A memo linked the notes that belonged to its one idea, for example a notation note and a tool note, and treated that mix as one difficulty. A teaching note or a feedback note from the same participant stayed in another memo.
```

**Decision:**

```text
Section 4.1 already names STGT and the attention to practices and tools in each incident. The socio-technical explanation stays in the Background and in RQ3. The 4.5.1 subsection is removed, including the label subsec:method_gt_variant, because its sentence did not match the code notes. S1 splits notation, tool, teaching, and feedback into separate codes. S1M1 links the notation notes and the tool note. S1M2 holds the teaching note. S1M5 holds the feedback note. Those sentences now sit in Coding and memoing. "Sometimes" is not used: a memo links the notes that belong to its one idea.
```

## C48 — Constant comparison is placed at two different times

**Status:** Done

**Kind:** Structure

**Chapter:** 4.5.3 Category development and the findings map

**Highlighted sentence:**

> After open coding and memoing, constant comparison was used to merge, split, and bound categories against the research questions.

**His comment:**

> But you said you used it throughout the coding stage, not after.

**In plain words:** This sentence says constant comparison started after coding and memoing. Earlier, the coding subsection says it was used throughout coding, as each new incident was compared with earlier ones. Both cannot be the timing. Next: say which is true. If it ran throughout, this sentence should say what extra comparison happened at the category stage, not that comparison began then.

**Where it sits:** The first sentence of subsection 4.5.3. The earlier statement is in the coding subsection: “Constant comparison was applied throughout: newly coded incidents were compared with previous incidents and codes”.

**Location:** `2-MainMatter/chapter4.tex`, `\subsection{Category development and the findings map}` (`subsec:method_categories`). The earlier statement is in `\subsection{Coding and memoing}`, the paragraph that begins “Analysis was carried out by the author.”

**Possible fix:** Keep “throughout” for the coding comparisons. In this sentence, name only the later use: merging, splitting, and bounding categories. Do not write “after” as if comparison had not already been used.

**Depends on:** C26

**Your wording:**

```text

```

**Decision:**

```text
The 4.5.3 sentence now says constant comparison was used throughout open coding and memoing to merge, split, and bound categories. It no longer says that comparison started after coding.
```

## C49 — Local saturation is hard to follow and argues the wrong point

**Status:** Done

**Kind:** Wording

**Chapter:** 4.5.5 Local saturation of the category set

**Highlighted sentence:**

> Side note on the whole subsection. No single sentence was marked.

**His comment:**

> This is a strange section. First, it is really hard to understand — do you really understand everything you write here? Second, qualitative studies, by design, never claim generalisation. As such, saturation would never imply a global validity. I haven't read Dey (have you?), but I would strongly suspect that this is what they mean: Saturation in a qual. study does not imply a "valid" theory.

**In plain words:** The subsection is difficult to read, and he doubts the jargon is understood. It spends its effort separating “local saturation” from “global theoretical saturation” and from worldwide generalisation. A qualitative study does not claim that kind of generalisation, so saturation was never going to mean a globally valid theory. He thinks that is the point of the Dey citation, and he asks whether Dey was actually read. Next: rewrite the subsection in plain words as the reason interviewing stopped. Do not invent a special contrast with global validity. Keep the Dey citation only after checking that the book says what the sentence claims.

**Where it sits:** All of subsection 4.5.5. The opening contrasts a usual saturation claim with “local saturation of the overview category set” and “theoretical sufficiency”, citing Dey. The closing paragraph then lists what is not claimed, including “global theoretical saturation across modelling courses worldwide” and statistical generalisation. The two tables count categories and wave-2 changes in dense shorthand.

**Location:** `2-MainMatter/chapter4.tex`, `\subsection{Local saturation of the category set}` (`subsec:method_local_saturation`). The Dey citation is `dey1999grounding`. The same “not global theoretical saturation” line is in the caption of Figure `fig:sampling_waves`, in the previous subsection.

**Possible fix:** Say why data collection stopped: four further interviews did not add a 15th overview category, though some categories gained a property or a boundary case. Cut the local-versus-global apparatus, including the worldwide sentence, unless one plain sentence shows a decision that apparatus changed. Before keeping Dey, read the cited passage and match the citation to it. The tables can stay only if a reader can tell what “new”, “inst.”, and “neg.” mean without the caption’s abbreviations.

**Depends on:** P1

**Your wording:**

```text
Interviewing stopped after the four further interviews. They did not add a 15th overview category. The first table counts that: 14 categories after the first ten interviews, and still 14 after the next four. The second table shows what those four interviews added inside the 14 categories. In that table, "new" means a new property, "boundary" means a case at the edge of the category, "known" means another example of a property already recorded, "empty" means no incident for that category, and a dash means the interview did not supply an incident strong enough to use.
```

**Decision:**

```text
Applied 27 September 2026. The title is "Why interviewing stopped". Dey is not cited: the book was not available, and secondary sources disagree on the page. Sims and Cilliers (2023) define theoretical sufficiency in the Background: enough evidence to support the claims of the study. The subsection says the 14 categories were enough to answer the research questions, names that judgment, and says further properties could still appear. The table is the evidence. Abstract, Chapter 5 caption, Chapter 6, and Chapter 7 still use the old local-saturation wording.
```

## C50 — “Sensitising concept” is undefined

**Status:** Done

**Kind:** Wording

**Chapter:** 4.5.6 Bloom's taxonomy as a sensitising concept

**Highlighted sentence:**

> Bloom's revised taxonomy was used as a sensitising concept to support the interpretation and communication of findings, particularly when describing the cognitive character of reported modelling challenges (understanding constructs and their semantics, applying modelling procedures, evaluating model adequacy).

**His comment:**

> Meaning what?

**In plain words:** “Sensitising concept” is method jargon. He cannot tell what Bloom did in this study. Next: say the job in ordinary words, for example that Bloom supplied words for describing what a challenge demanded, and was not a set of boxes the codes had to fit. The timing of that use is C51.

**Where it sits:** The first sentence of subsection 4.5.6, on “sensitising concept”. The same phrase appears in section 1.4.

**Location:** `2-MainMatter/chapter4.tex`, `\subsection{Bloom's taxonomy as a sensitising concept}` (`subsec:method_bloom_sensitising`). The introduction use is in `2-MainMatter/chapter1.tex`, `sec:intro_approach`.

**Possible fix:** Replace “sensitising concept” with the plain job Bloom had. If the term stays, define it in the same sentence. Use the same plain words in section 1.4.

**Depends on:** P1 and C20

**Your wording:**

```text

```

**Decision:**

```text
"Sensitising concept" is gone from section 1.4 and from subsection 4.5.6. The subsection title is now "Where Bloom was used." The plain job is the timeline in the C51 decision.
```

## C51 — When was Bloom used?

**Status:** Done

**Kind:** Structure

**Chapter:** 4.5.6 Bloom's taxonomy as a sensitising concept

**Highlighted sentence:**

> Bloom-inspired terminology was used selectively as an analytic lens and reporting vocabulary where it aligned with participant accounts.

**His comment:**

> What exactly does this mean? You had your finished categories and then you slapped Bloom on it? But that's part of the analysis then after all, isn't it? Or does it mean your GT ends and then you add another analytical stage? Also, earlier you stated that Bloom was already used in designing the interview guide, so you did consider it during the interviews anyway, no?

**In plain words:** “Analytic lens” does not say what was done with Bloom. The previous sentence says Bloom was applied after the categories existed. That can mean the finished categories were redescribed in Bloom’s words, which is still analysis, or it can mean a second stage after Grounded Theory. He also points at an earlier sentence: Bloom was already used to write the interview questions, so it was in the study before the categories. Next: state one timeline. Say whether Bloom shaped the questions, the coding, the write-up, or more than one of those, and what was done at each point.

**Where it sits:** The middle of the second sentence of subsection 4.5.6. The sentence before it says Bloom was applied after the categories had been developed. The interview-guide claim is in subsection 4.4.1, which is C43.

**Location:** `2-MainMatter/chapter4.tex`, `subsec:method_bloom_sensitising`. The guide claim is in `subsec:method_instruments_pilot`.

**Possible fix:** Replace “analytic lens” with the actual step. If Bloom only renamed findings in the write-up, say that, and call it part of the analysis. If it also shaped the questions, say that in the same account and do not also say Bloom entered only after the categories. C43 asks for the question-to-Bloom mapping. This comment asks for the timing to match that mapping.

**Depends on:** C43 and C50

**Your wording:**

```text

```

**Decision:**

```text
Subsection 4.5.6 now states the timeline. Some questions were aimed at remembering a notation, understanding a construct, applying a procedure, and judging a model, with a pointer to the prompt table. Codes and categories were not sorted into those levels. In the findings, those words are used where a challenge already matched them, as part of reporting the analysis. "Analytic lens" and "applied after" are gone. Section 1.4 uses the same account in shorter form.
```

## C52 — Rigour states what is good, not what is threatened

**Status:** Done

**Kind:** Structure

**Chapter:** 4.6 Rigour and trustworthiness

**Highlighted sentence:**

> Side note at the end of the section. No single sentence was marked. He excepts the last sentence.

**His comment:**

> With the exception of the last sentence, you only state what's good with your work. I'd like to see a more honest reflection here on what might NOT be valid in your work. I.e., what are threats to credibility, etc.?

**In plain words:** The section reads as a list of strengths. The last sentence is the exception: the thesis does not claim statistical generalisation. He wants the threats written here: what might weaken credibility, dependability, confirmability, and transferability. A few limits are already in the section, such as no member checking, no second coder, and uneven probes, but they are written as what was done instead, not as what they put at risk. Next: under each heading, say the threat and what it means for the findings.

**Where it sits:** The end of section 4.6. The last sentence of the section is “The thesis does not claim statistical generalisation.” Section 4.7, “Methodological limitations”, then lists recall, the Portuguese sample, no new lecturers in wave 2, and interviews without a model present.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Rigour and trustworthiness}` (`sec:method_rigour`). The following section is `\section{Methodological limitations}` (`sec:method_limitations`).

**Possible fix:** For credibility, dependability, confirmability, and transferability, add the threat, not only the procedure that supports the heading. Use the limits already named in this section and in 4.7, and say what each one puts in doubt. Do not leave the honest account only in the next section. The last sentence can stay, but it is not a substitute for those threats. C49 already says a qualitative study does not claim statistical generalisation, so this sentence should not be the section’s only limit.

**Depends on:** C49

**Your wording:**

```text
Credibility: the accounts depend on memory, including courses described years later, and no model was in the session. Dependability and confirmability: one coder, no agreement score, with a trail from excerpt to category. Transferability: mostly Portuguese higher education, lecturer claims rest on four interviews, no statistical generalisation.
```

**Decision:**

```text
Section 4.6 is rewritten under the three headings. The sentence that said the section uses headings rather than threats is gone. The limitations section is removed in C54.
```

## C53 — How were the recordings anonymised?

**Status:** Done

**Kind:** Fact or citation

**Chapter:** 4.7 Ethics and data management

**Highlighted sentence:**

> Interview recordings and transcripts were anonymised, and potentially identifying details (course identifiers, project names, personal data) were removed or generalised.

**His comment:**

> How did you anonymise the recordings?

**In plain words:** The sentence says the recordings were anonymised. The rest of the sentence describes removing names and course details, which is what you do to a transcript, not to an audio file. Nothing in the chapter says what was done to the recordings themselves. Next: state the concrete steps for the audio. If only the transcripts were anonymised, say that, and do not claim the recordings were.

**Where it sits:** The second sentence of section 4.7. The transcription subsection earlier says the transcripts were anonymised: speaker labels, turn identifiers, and identifying details removed. It does not describe the audio files.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Ethics and data management}` (`sec:method_ethics`). The transcript procedure is in `\subsection{Transcription and analytic identifiers}` (`subsec:method_transcription`).

**Possible fix:** Separate the two. For transcripts, keep the removal of names, course titles, and project names. For recordings, say what was actually done: how files were named, who could hear them, and whether spoken names were removed from the audio. If the audio still contains names, the sentence cannot say the recordings were anonymised.

**Depends on:** none

**Your wording:**

```text

```

**Decision:**

```text
The ethics section no longer says the recordings were anonymised. It says they were deleted after transcription, and that the transcripts were anonymised by removing or generalising course identifiers, project names, and personal data. No GDPR claim was added.
```

## C54 — Limitations belong with the threats

**Status:** Done

**Kind:** Structure

**Chapter:** 4.8 Methodological limitations

**Highlighted sentence:**

> The section title, “Methodological limitations”.

**His comment:**

> This should go to the threats section.

**In plain words:** He does not want a separate limitations section. The contents belong in the rigour section, as threats. That is the same request as C52: say what might not be valid, not only what was done well. Next: move this material into section 4.6, under the threat it belongs to, and remove the standalone section.

**Where it sits:** The title of section 4.8. The section covers recall, interviews at a distance of years, a mostly Portuguese sample, no new lecturers in wave 2, and probes that do not remove recall bias. Section 4.6 is the rigour section he wants these threats written into.

**Location:** `2-MainMatter/chapter4.tex`, `\section{Methodological limitations}` (`sec:method_limitations`). The destination is `\section{Rigour and trustworthiness}` (`sec:method_rigour`).

**Possible fix:** Split these limits across credibility, dependability, confirmability, and transferability in section 4.6, as C52 asks. Do not keep a second section that repeats them. The pointer to Chapter 6 for what the bounds mean can stay with the threat it belongs to.

**Depends on:** C52

**Your wording:**

```text
The limitations section is deleted. Recall and the missing model sit under credibility. The single coder sits under dependability and confirmability. The Portuguese corpus and the four lecturer interviews sit under transferability.
```

**Decision:**

```text
Section 4.8 is removed. Its contents are the three paragraphs in section 4.6. The two pointers that named the limitations section now name the rigour section. The planned-feedback example and the tool-and-notation sentence from the old limitations section were not carried over. The sampling-and-open-questions closer was not carried over. The sentence "No model was in the session, so the questions do not replace watching the work" was removed: the interviews were talk about remembered steps and struggles, and S3 opening a tool was one session, not the method.
```

Wording blocks stay empty until a second pass. When you paste the next highlight, add the next `C` entry from the template below and add a row to the index.

```markdown
## C1 — short label

**Status:** Open

**Kind:** Wording | Fact or citation | Structure | Missing literature

**Chapter:**

**Highlighted sentence:**

>

**His comment:**

>

**In plain words:**

**Where it sits:**

**Location:**

**Possible fix:**

**Depends on:** P1 | P2 | P3 | none

**Your wording:**

​```text

​```

**Decision:**

​```text

​```
```
