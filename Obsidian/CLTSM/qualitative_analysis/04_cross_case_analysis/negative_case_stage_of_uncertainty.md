# Negative-Case Test: The Stage of Representational Uncertainty

## Initial Claim

Starting difficulty is a common modelling-learning challenge. Lecturer cases L1 and L2 particularly emphasise the gap between knowing notation and independently producing a first model.

## Negative Cases

### S5: Starting is not the difficulty

S5 begins modelling readily, discusses the problem with peers, extracts actors and events, and produces an initial draft without waiting for teacher demonstration.

The difficulty appears later:

- Sequence diagrams become overly complex.
- The student includes too much detail.
- Granularity and stopping decisions become uncertain.
- Contrastive examples are needed to support simplification.

Relevant memo:

- [[../03_memos/memo_S5M3|S5M3: Granularity problems can appear as over-modelling]]

### S6: Starting is systematic, but integration fails

S6 begins vague requirements tasks with a deliberate strategy:

- Identify stakeholders and goals.
- Separate explicit information from assumptions.
- Delay UML until the requirements perspective is understood.

The difficulty emerges when translating from iStar and NFR models into UML:

- The UML model can be syntactically acceptable while losing goal meaning.
- Traceability criteria are unclear.
- The learner does not know what should be preserved across modelling families.

Relevant memos:

- [[../03_memos/memo_S6M1|S6M1: The missing bridge between early requirements models and UML]]
- [[../03_memos/memo_S6M5|S6M5: Tool integration problems mirror conceptual integration problems]]

### S3: Prior exposure removes the initial barrier

Repeated BPMN exposure allows S3 to start exercises quickly. Uncertainty instead appears around:

- Unfamiliar notation variants
- Visual complexity
- Model quality
- Lecturer confirmation

Relevant memos:

- [[../03_memos/memo_S3M1|S3M1: Repeated BPMN exposure creates a head start]]
- [[../03_memos/memo_S3M2|S3M2: Notation ambiguity and visual complexity]]
- [[../03_memos/memo_S3M3|S3M3: Quality is checked by recovering requirements]]

## Refined Interpretation

> Representational uncertainty can occur at different stages of modelling. Starting is one common point, but uncertainty can migrate to refinement, integration, or evaluation as experience increases.

Starting difficulty should therefore be reported as a recurring early manifestation rather than the universal central challenge.

## Stage Model

### 1. Initiation uncertainty

Questions include:

- What should I model first?
- Which elements are relevant?
- How do I move from text to a representation?

Common responses:

- Wait for teacher initiation
- Search for examples
- Use extraction heuristics
- Produce a tentative draft

### 2. Construction uncertainty

Questions include:

- Which relationship or construct fits?
- How should this information be represented?
- What notation rules apply?

Common responses:

- Reuse familiar patterns
- Seek semantic feedback
- Compare examples
- Guess and revise

### 3. Refinement uncertainty

Questions include:

- Is the model too detailed or too abstract?
- What should be removed, decomposed, or clarified?
- When is the model sufficiently complete?

Common responses:

- Add excessive detail
- Simplify using examples
- Apply readability and purpose criteria
- Seek critique

### 4. Integration uncertainty

Questions include:

- What should transfer between models?
- How are elements traceable across modelling families?
- How can several perspectives remain consistent?

Common responses:

- Apply inappropriate familiar mappings
- Lose rationale during translation
- Document trace links and assumptions
- Seek cross-family methodology or tool support

### 5. Evaluation uncertainty

Questions include:

- Is this model good enough?
- Which alternative is more defensible?
- Will the lecturer, team, or stakeholder accept it?

Common responses:

- Apply self-checks
- Compare and justify alternatives
- Seek calibration
- Change defensible work through self-doubt

### 6. Maintenance uncertainty

Questions include:

- When should the model be updated?
- Which implementation or requirement changes matter?
- Is continued maintenance worth its cost?

Common responses:

- Maintain a living shared model
- Update only for milestones
- Allow model-code divergence
- Abandon the model after assessment

## Theoretical Consequence

Experience may not remove representational uncertainty. Instead, it can relocate uncertainty from basic initiation and notation toward:

- Granularity
- Cross-model consistency
- Rationale
- Quality evaluation
- Maintenance

This supports a developmental interpretation of modelling competence: more experienced learners encounter different decisions rather than simply fewer decisions.

## Revised Proposition

> Prior exposure and scaffolding reduce uncertainty at earlier modelling stages, but uncertainty persists or migrates toward refinement, integration, evaluation, and maintenance. Effective support should therefore target the learner's current modelling stage rather than assume that successful initiation indicates complete independence.

## Implications

- Interview and analysis questions should ask where in the modelling process uncertainty occurs.
- Worked examples should address refinement and integration, not only first steps.
- Tools should offer stage-appropriate guidance.
- Assessment should capture process and revision rather than only initial construction.
- The findings should avoid ranking one modelling activity as universally hardest.

## Remaining Tests

- Map each student case to the stages where uncertainty is strongest.
- Examine whether the stages form a progression or recur iteratively.
- Identify modelling-family differences in the location of uncertainty.
- Test whether maintenance uncertainty is sufficiently supported in the current corpus.

