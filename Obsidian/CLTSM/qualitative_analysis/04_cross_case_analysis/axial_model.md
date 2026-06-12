# Provisional Axial Model

## Status

- Accepted as the working axial model on 2026-06-09.
- Organised around four learner-response modes and one cross-cutting pattern-reuse strategy.
- Provisional until each relationship is tested against cases, negative cases, and source excerpts.

## Core Phenomenon

> Learning modelling involves making and justifying representational decisions under uncertainty. Difficulties emerge when learners lack sufficient cognitive, pedagogical, social, or technical support for those decisions.

## Explanatory Sequence

```text
Assessment and course architecture
              +
Social and contextual conditions
              |
              v
Representational uncertainty
              |
              v
Learner-response modes
              |
       modified by
pedagogical and technical support
              |
              v
Modelling and learning outcomes
              |
              v
Feedback into confidence, expectations,
group legitimacy, and later strategies
```

The sequence is not strictly linear. Learners can move between response modes within one task, and outcomes from one experience shape later conditions and responses.

## Conditions

### Assessment and course architecture

- Curriculum timing and prior exposure
- Sequencing and integration of modelling families
- Assignment openness, domain policy, and authenticity
- Assessment criteria and perceived cost of being wrong
- Opportunities for feedback and revision
- Evaluation density, course scale, and teaching capacity

### Social and contextual conditions

- Confidence, shyness, and ambiguity tolerance
- Notation and domain familiarity
- Peer trust and psychological safety
- Shared model ownership and group legitimacy
- Attendance, available time, and competing workload
- Access to lecturers, teaching assistants, and examples
- Visibility of professional or practical modelling value

These conditions do not mechanically determine a response. They influence which response feels feasible, safe, and worthwhile.

## Representational Uncertainty

Uncertainty arises when learners must:

- Start from natural-language or incomplete requirements
- Select relevant entities, actors, events, goals, and relationships
- Choose abstraction, scope, decomposition, and granularity
- Apply unfamiliar notation semantics
- Translate between modelling families
- Compare multiple defensible alternatives
- Judge completeness, consistency, traceability, and fitness for purpose
- Decide whether and how a model should evolve with implementation

Some uncertainty is caused by insufficient instruction or support. Some is inherent to modelling and must be managed through judgement rather than eliminated.

Uncertainty is stage-dependent. It may emerge during initiation, construction, refinement, cross-model integration, evaluation, or maintenance. Prior exposure can reduce uncertainty at an early stage while relocating the main difficulty to later representational decisions. See [[negative_case_stage_of_uncertainty|Negative-case test: the stage of representational uncertainty]].

## Learner-Response Modes

### 1. Defer to Authority

#### Typical actions

- Wait for the teacher to begin
- Seek approval before proceeding
- Treat lecturer expectations as the hidden correct answer
- Change a defensible model after reassurance is unavailable

#### Variant A: Calibration seeking

The learner forms an initial representation or judgement and then seeks expert feedback to calibrate it.

Typical indicators:

- Produces a draft before requesting confirmation
- Can explain the reasoning behind the model
- Uses feedback to compare criteria or alternatives
- Continues working while awaiting feedback
- Applies prior feedback to later tasks

Calibration seeking can be productive, especially with unfamiliar modelling families, ambiguous requirements, or high assessment stakes. It becomes less dependent when feedback makes criteria explicit and transferable.

#### Variant B: Paralysing dependence

The learner does not proceed, commit to a representation, or trust any judgement without lecturer initiation or approval.

Typical indicators:

- Waits for a demonstration before starting
- Searches for an expected answer rather than testing an interpretation
- Abandons or repeatedly changes defensible work without confirmation
- Cannot transfer prior feedback to a changed task
- Treats the lecturer's model as uniquely correct

Paralysing dependence restricts practice and preserves uncertainty because the current task may be completed without the learner acquiring reusable evaluation criteria.

#### Movement between variants

The variants are not fixed learner types. A student may explore independently in a familiar notation but become paralysed in an unfamiliar family, seek healthy calibration during practice but demand certainty under assessment pressure, or move from dependence toward calibration as experience accumulates.

#### Likely conditions

- Low confidence or unfamiliar notation
- High assessment risk
- Ambiguous quality criteria
- Limited peer trust
- Prior experience of answer-centred feedback

#### Possible function

Authority seeking can provide useful calibration. It becomes problematic when learners cannot act or evaluate without confirmation.

#### Possible outcomes

- Corrected current artefact
- Temporary reassurance
- Continued validation dependence
- Weak transfer of quality judgement
- Stronger criteria and later independence when calibration is explanatory and followed by revision

### 2. Explore and Justify Alternatives

#### Typical actions

- Generate multiple representations
- Record assumptions and trade-offs
- Compare alternatives using explicit criteria
- Explain decisions in plain language
- Revise after critique or testing

#### Likely conditions

- Permission for multiple defensible answers
- Explicit quality criteria
- Low-stakes opportunities to attempt and revise
- Rationale-rich examples
- Sufficient time and confidence

#### Possible outcomes

- Ambiguity tolerance
- Independent model-quality judgement
- Transferable decision strategies
- Better traceability and rationale

### 3. Negotiate Collaboratively

#### Typical actions

- Discuss interpretations with peers or stakeholders
- Share incomplete models
- Review and challenge alternatives
- Use the model during team decisions
- Maintain shared representations

#### Likely conditions

- Psychological safety
- Shared model ownership
- Collaborative tools or working spaces
- Modelling recognised as legitimate project work
- Feedback formats compatible with different participation styles

#### Possible outcomes

- Shared understanding and coordination
- Models maintained as working artefacts
- Perspective-taking and stakeholder awareness
- Peer-supported independence

#### Risks

- Group conformity
- Unequal contribution
- Shared misconceptions
- One model owner without decision authority

### 4. Avoid or Abandon Modelling

#### Typical actions

- Move directly to implementation
- Produce the model only near submission
- Stop updating the model
- Delegate modelling to one member
- Reduce the task to minimal rubric compliance

#### Likely conditions

- Weak or invisible modelling purpose
- Implementation-first group culture
- High tool or notation friction
- Evaluation overload and limited time
- No downstream model use
- Repeated experiences of arbitrary or low-value modelling

#### Possible outcomes

- Model-code divergence
- Disposable documentation
- Reduced practice and competence development
- Reinforced belief that modelling is unnecessary overhead

## Cross-Cutting Strategy: Reuse Familiar Patterns

Pattern reuse is not treated as an independent response mode because it usually occurs within authority dependence, exploration, collaboration, or avoidance. It describes how learners use prior examples, conventions, and known structures while enacting those broader responses.

### Reflective reuse

- Compare the current problem with a previous example.
- Identify which conditions are similar or different.
- Understand the rationale behind the reused structure.
- Adapt the pattern to the current purpose and domain.
- Check the result against semantic and quality criteria.

Reflective reuse can support transfer, reduce entry effort, and enable exploration.

### Unreflective reuse

- Copy visible shapes or relations without understanding their meaning.
- Treat lecturer examples as answer templates.
- Apply a familiar modelling paradigm to a family with different semantics.
- Ignore changed domain conditions.
- Retain a pattern despite evidence that it does not fit.

Unreflective reuse can create hidden semantic errors, fragile transfer, and continued dependence.

### Relationship to the four modes

- **Defer to authority:** copy the teacher's preferred pattern to obtain certainty.
- **Explore and justify alternatives:** use a known pattern as a candidate, then adapt and evaluate it.
- **Negotiate collaboratively:** propose and revise shared patterns through peer or stakeholder discussion.
- **Avoid or abandon modelling:** apply a minimal familiar template to satisfy a requirement without deeper engagement.

## Support Mechanisms

### Pedagogical support

- Rationale-rich and contrastive examples
- Progressive complexity and fading
- Explicit decomposition and translation strategies
- Actionable quality criteria
- Multiple feedback channels
- Opportunities to justify and revise
- Authentic audience and downstream use

### Technical support

- Low-friction construction
- Syntax and semantic validation
- Explainable feedback
- Progressive, optional guidance
- Traceability across representations
- Collaboration, versioning, and maintenance support
- AI-supported explanation and critique with learner accountability

Support can change the trajectory of a response:

- Authority seeking can become calibrated independent judgement.
- Unreflective copying can become reflective pattern reuse.
- Private uncertainty can become collaborative negotiation.
- Avoidance can become meaningful participation when purpose and downstream use become visible.

## Outcomes

### Learning outcomes

- Independent representational judgement
- Transferable modelling strategies
- Ambiguity tolerance
- Ability to explain and justify models
- Continued dependence on lecturer validation
- Fragile pattern transfer
- Avoidance of modelling activity

### Artefact and practice outcomes

- Complete, consistent, readable, and traceable models
- Models used for reasoning, communication, coordination, or change
- Maintained working representations
- Over-detailed or prematurely simplified models
- Semantically invalid or disconnected representations
- Models that decay or diverge from implementation

### Perceived-value outcomes

- Modelling understood as meaningful engineering work
- Modelling valued as cognitive and communicative support
- Modelling viewed as arbitrary notation
- Modelling viewed as extra documentation or assessment compliance

## Feedback Loops

### Productive loop

```text
Supported attempt
→ informative feedback
→ justified revision
→ stronger judgement and confidence
→ greater willingness to explore and share
→ more effective later modelling
```

### Dependency loop

```text
Uncertainty
→ authority supplies answer
→ current task is completed
→ criteria remain tacit
→ renewed uncertainty on a new task
→ continued authority dependence
```

### Calibration loop

```text
Independent attempt
→ targeted expert feedback
→ criteria become explicit
→ justified revision
→ stronger later self-evaluation
→ reduced need for confirmation
```

### Value loop

```text
Model used in real decisions
→ visible benefit
→ greater group legitimacy and maintenance
→ better alignment and usefulness
→ stronger perceived value
```

### Abandonment loop

```text
Model disconnected from work
→ low perceived value
→ reduced effort and maintenance
→ model becomes inaccurate
→ group sees further evidence that modelling is useless
```

## Variation and Movement Between Modes

- A student may reuse a pattern to start, then explore alternatives during refinement.
- A learner may independently create a model but seek authority validation before assessment.
- Authority seeking may shift between calibration and paralysis as familiarity, confidence, and assessment risk change.
- Collaborative negotiation may fail and lead to abandonment.
- Public critique may support exploration for one student and trigger withdrawal for another.
- Prior exposure may reduce starting difficulty without eliminating quality uncertainty.
- Tool validation may reduce syntactic uncertainty while leaving contextual decisions unresolved.

The response modes should therefore be coded as situated actions, not fixed learner types.

## Relationship to Research Questions

- **RQ1:** Representational uncertainty identifies where challenges emerge across modelling activities.
- **RQ2:** Response modes and support mechanisms explain how learners and instructors address challenges and what support is needed.
- **RQ3:** Course, social, and technical conditions explain why different responses and outcomes occur.

## Analytic Propositions to Test

1. When quality criteria remain implicit, learners are more likely to defer to authority even after producing a defensible model.
2. Explanatory feedback and revision move authority seeking from paralysing dependence toward calibration and later self-evaluation.
3. Worked examples support reflective transfer when they expose alternatives and rationale; final-only examples encourage unreflective pattern copying.
4. Revision opportunities convert feedback into independent judgement more effectively than final correction.
5. Shared ownership and downstream model use increase maintenance and perceived value.
6. Progressive semantic guidance reduces incidental uncertainty without eliminating contextual judgement.
7. High assessment density shifts learner responses from exploration toward prescription seeking and compliance.
8. Cross-family transitions intensify uncertainty when correspondence and traceability are not explicitly taught.
9. Multiple feedback channels broaden access to critique and reduce avoidant responses.
10. Prior exposure and scaffolding may relocate uncertainty from initiation toward refinement, integration, evaluation, or maintenance rather than removing it entirely.
11. Critique supports learning when feedback is substantive, psychologically safe, and delivered at a tolerable level of social exposure; public visibility alone does not determine its value.
12. Domain choice increases engagement only when scope, access, workload, fairness, and teaching capacity are controlled; otherwise, freedom can increase uncertainty and inequality.
13. Semantic tools improve learning only when their validation and explanatory benefits exceed interaction, reliability, and prerequisite burdens, and when contextual choices remain open to human judgement.
14. Continuous assessment supports modelling competence when it creates manageable feedback-revision cycles; submission frequency without sufficient feedback, revision, and time can instead produce overload and compliance.
15. Formality supports modelling when its semantic discipline matches the representation's purpose; progressive formalisation can preserve exploration while adding precision for shared interpretation, validation, traceability, execution, or automation.

## Remaining Work

- Map each memo to one or more response modes and, where relevant, reflective or unreflective pattern reuse.
- Identify strong, weak, and contradictory evidence for each proposition.
- Build student and lecturer case matrices.
- Distinguish participant evidence from researcher inference.
- Search for incidents not explained by the four response modes or the cross-cutting pattern-reuse strategy.
- Decide whether any mode should be split, merged, or reframed after case-level testing.
