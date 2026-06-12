# Negative-Case Test: Semantic Tools and Learning Burden

## Initial Claim

Semantically typed or executable modelling tools can improve learning by preventing invalid operations, exposing notation vocabulary, and making some model properties testable.

## Supporting Evidence

- L1 distinguishes educational modelling tools from unrestricted drawing tools and values semantic feedback.
- L2 values tool-supported error prevention.
- L3 uses typed and executable tooling to prevent invalid actions and validate models.
- L4 values PyStar's enforcement of iStar semantics.
- S3 values BPMN vocabulary, hover support, and syntax-error prevention.
- S5 and S6 want semantic consistency and model-text checking.

Relevant notes:

- [[comparison_tools_progressive_guidance|Tools and progressive guidance]]
- [[../03_memos/memo_L3M2|L3M2: Executable modelling makes models dynamic]]
- [[../03_memos/memo_S3M4|S3M4: Bizagi lowers the syntax barrier]]

## Negative and Limiting Cases

### Secondary learning burden

L3's executable UML approach depends on OCL. Students must learn:

- The modelling language
- The modelling tool
- The constraint language
- Execution and debugging conventions

The mechanism that makes semantics visible also adds a substantial prerequisite burden.

Relevant memo:

- [[../03_memos/memo_L3M3|L3M3: Semantic rigor through executability comes with a heavy OCL burden]]

### Feature and interface overload

S1 experiences the tool and notation as part of the same overload. A technically capable environment can make simple relationships feel disproportionately difficult.

Relevant memo:

- [[../03_memos/memo_S1M2|S1M2: Notation and tool overload]]

### Reliability and scale limitations

S3 values Bizagi as a beginner tool but reports failures or degraded usability for large diagrams. Tool interruption becomes part of the modelling difficulty.

### Fragmentation

L4 and S6 describe semantic support for one modelling family but weak integration across iStar, NFR, and UML. Local correctness does not guarantee cross-model consistency.

Relevant notes:

- [[../03_memos/memo_L4M7|L4M7: Semantic tools help, but family fragmentation remains]]
- [[../03_memos/memo_S6M5|S6M5: Tool integration problems mirror conceptual integration]]

### Contextual adequacy remains unresolved

A tool may verify:

- Element types
- Connection rules
- Cardinality syntax
- Executable constraints
- Workflow structure

It cannot mechanically determine every question of:

- Appropriate abstraction
- Domain interpretation
- Stakeholder adequacy
- Model purpose
- Readability
- Best alternative among several defensible representations

## Refined Interpretation

> Semantic tools support learning only when the validation benefit exceeds their interaction and prerequisite burden, and when feedback explains errors without presenting contextual choices as mechanically correct.

## Usability-Semantic Benefit Threshold

A semantic tool produces net educational value when:

```text
Semantic visibility
+ error prevention
+ explanatory feedback
+ useful execution or traceability

is greater than

interface friction
+ installation and access burden
+ prerequisite languages
+ reliability problems
+ attention diverted from modelling
```

This threshold differs by learner experience, modelling family, task complexity, and course purpose.

## Types of Tool Feedback

### Hard error

A formally invalid operation or relation.

The tool can block or clearly identify it.

### Likely inconsistency

A suspicious mismatch within or across models.

The tool should explain the evidence and permit review.

### Quality prompt

A question about completeness, granularity, readability, or traceability.

The tool should provide criteria rather than a definitive answer.

### Contextual alternative

Several representations may be defensible.

The tool should expose alternatives and trade-offs without declaring one universally correct.

Confusing these feedback types creates false certainty.

## Progressive Introduction

Semantic support can be staged:

1. Begin with a constrained subset and low-friction construction.
2. Introduce syntax and semantic checks with explanations.
3. Add execution, constraints, or cross-model validation when foundational competence is established.
4. Allow experienced learners to inspect or override suggestions with rationale.

A tool should not require advanced validation mechanisms before learners understand the represented concepts.

## Role of Pedagogy

Tools do not replace:

- Explanation of modelling purpose
- Worked and contrastive examples
- Stakeholder reasoning
- Quality criteria
- Peer negotiation
- Lecturer calibration

Tool feedback becomes more useful when aligned with the vocabulary and criteria used in teaching and assessment.

## Revised Proposition

> Semantic tooling improves modelling learning when it makes relevant formal properties visible with manageable interaction and prerequisite cost. Its feedback should distinguish formal invalidity from contextual judgement, explain why an issue matters, and progressively fade or expand according to learner experience.

## Implications

- Evaluate educational tools by learning burden as well as feature coverage.
- Use novice modes or constrained palettes.
- Delay advanced constraint languages until conceptually necessary.
- Provide explanations, not only prohibition.
- Separate hard errors from suggestions.
- Preserve learner responsibility for contextual adequacy.
- Consider integration and reliability as pedagogical requirements.

## Remaining Tests

- Compare learning benefits against time spent learning each tool.
- Identify which checks students understand and transfer without the tool.
- Examine whether execution improves semantic understanding or primarily grading.
- Compare novice and advanced responses to the same guidance.
- Test cross-family consistency support separately from local syntax checking.

