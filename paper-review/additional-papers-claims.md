# Additional papers and the claims they strengthen

A reading aid for Section 3.7.2 (`subsec:rw_additional`) and the matching paragraphs in Chapter 6. These six papers were added because the core related-work set is thin on delayed diagram feedback, group versus individual UML, consistency across views, and LLM-generated UML. They strengthen selected claims. They do not replace the core literature, and they are not findings of this thesis.

Cards live in `paper-review/cards/`. Bib keys are in `4-Bibliography/bibliography.bib`.

## How to check a claim

1. Read the thesis sentence in the “Where it appears” column.
2. Open the card. The card’s takeaway should match the thesis sentence.
3. If the thesis says more than the “Strengthens” column, that extra part has to come from the interviews, not from the paper.

| Paper | Bib key | Claim | Strengthens | Does not cover | Where it appears |
|---|---|---|---|---|---|
| Hasker & Rowe, UMLint (ASEE 2011) | `hasker2011umlint` | CAT5, PH2 | Late instructor critique of student UML is a known teaching problem. Diagrams can be syntactically fine and still wrong. A checker is one design response. | Who can get the comment (CAT6). Whether these courses used UMLint. | Ch. 3 §3.7.2; Ch. 6, support-needs paragraph |
| Foss, Urazova & Lawrence, AutoER (SIGCSE 2022) | `foss2022autoer` | CAT5, PH2 | Delayed marking of UML database-design diagrams is treated as a bottleneck; immediate automated feedback is a published alternative to waiting on the lecturer. | Multi-family courses. CAT6 access. Evidence that this corpus had such a tool. | Same two places as UMLint |
| Silva, Gadelha, Steinmacher & Conte (SBES 2018) | `silva2018group` | CAT9 | Groups are not uniformly better than individuals on UML correctness and completeness. Group work is not automatically the better pedagogy. | Code-first pressure, exclusive notation ownership, a defence audience. Those conditions are from S4, S7, and S10. | Ch. 3 §3.7.2; Ch. 6, CAT9 paragraph |
| Sikkel & Daneva (REET 2010) | `sikkel2010consistency` | CAT14 | Consistency across UML views is taught content, not something students do automatically. Textbooks often skip it. | iStar-to-UML (S6) and BPMN-to-class (S10) incidents. Whether a course teaches the difference up front. | Ch. 3 §3.7.2; Ch. 6, CAT14 paragraph (with Buchmann and Verbruggen) |
| Verbruggen & Snoeck (EMMSAD 2022) | `verbruggen2022multiperspective` | CAT14 | A class diagram and a BPMN model answer different questions about the same case. Knowing which requirements belong in which view is part of model quality. | The lived translation losses in this corpus. Small observational study, not these interviews. | Same two places as Sikkel |
| Cámara, Troya, Burgueño & Vallecillo (SoSyM 2023) | `camara2023chatgpt` | CAT13, PH3; also CAT12 | ChatGPT on UML class diagrams with OCL was unreliable compared with code generation. Using a chatbot to explain, rather than to submit a generated model, fits that result. It also blocks any claim that current LLMs already compile models. | An evaluation of S4, S5, S6, or S10. L3’s wish for an explainer. Any particular tool working in these courses. | Ch. 3 §3.7.2; Ch. 6, CAT13 paragraph |

## Paper by paper

### UMLint and AutoER — the late signal is a known problem

**Interview claim.** Because a model does not compile (CAT12), students often learn they are wrong when a teacher, or a late comment, tells them (CAT5, PH2).

**What the papers add.** Other educators already treat that wait as a teaching bottleneck and have built checkers (UMLint for UML defects; AutoER for database-design UML). So “the teacher is the compile button” is not only a local story, and “more lecturer hours” is not the only response on record.

**Check.** The thesis must still say these papers do not speak to CAT6 (public board versus desk, graded versus ungraded, who asks). If a sentence sounds like UMLint or AutoER was used by L1–L4 or S1–S10, that sentence is too strong.

### Silva et al. — groups are not automatically better

**Interview claim.** Groups can kill a diagram (code-first pressure, a rushed teammate, split ownership that diverges) or keep it alive (ownership, pairs, draft-and-review). CAT9.

**What the paper adds.** A classroom comparison already found that group UML was not uniformly more correct or more complete than individual UML. That supports the two-sided claim and argues against “just put them in groups.”

**Check.** Silva’s measures are correctness and completeness of exercises. The thesis’s extra conditions — code-first pressure, exclusive notation ownership, a defence reader — have to stay tied to S4, S7, and S10.

### Sikkel & Daneva, and Verbruggen & Snoeck — different diagrams, different questions

**Interview claim.** Moving from one family to another drops goals, process structure, or the question the model was answering (CAT14; S6, S10). S7 is a lighter syntax-at-switch bound.

**What the papers add.** Teaching consistency across UML views, and teaching UML class diagrams beside BPMN on one case, are already published as curriculum problems. “Models answer different questions” is not only this corpus’s phrasing.

**Check.** Neither paper is the S6 iStar-to-UML incident or the S10 BPMN-pool-into-classes incident. Neither paper shows whether these courses teach that difference before the diagram goes wrong. That limit is stated at the end of the CAT14 paragraph in §3.7.2.

### Cámara et al. — generation is a weak compile button

**Interview claim.** Students who used AI asked it to explain or compare, and they would not submit generated homework (CAT13: S4, S5, S6, S10). That stance feeds PH3 with the wish for checks (CAT7).

**What the paper adds.** An experience report found ChatGPT unreliable on UML class diagrams with OCL, and weaker than on code. That makes the explain-not-generate stance intelligible, and it blocks reading CAT12 as “an LLM already supplies the missing compile result.”

**Check.** Four student cases are not an AI-education evaluation. L3’s wish for a model explained back in ordinary language stays an implication in Chapter 6, not part of CAT13.

## What these papers are not asked to do

Section 3.7.3 still lists the thin spots after these papers are counted: feedback access (CAT6), groups under code-first pressure, AI used as an explainer inside these courses, and course load as a blocker of demos and feedback (CAT11). None of the six papers closes those.

The core frame stays in §§3.1–3.6 and in §3.7.1: Maslov, the Bloom frameworks, the iStar learning study, Chakraborty and Liebel, Liebel et al. on tools, Buchmann, Grassl, Holmes, and EVELIN. The six papers above sit beside that frame.
