# Negative-Case Test: Formality and Modelling Purpose

## Initial Claim

Formal modelling languages provide shared syntax and semantics that support precision, consistency, communication, validation, and automation.

## Supporting Evidence

Formal semantics can help:

- Distinguish relationship types
- Prevent invalid model construction
- Support cross-model consistency
- Enable execution or simulation
- Establish shared vocabulary
- Provide traceability
- Make assessment criteria more explicit

Lecturer cases especially value semantic discipline when models support requirements reasoning, execution, code generation, or formal validation.

Relevant notes:

- [[comparison_tools_progressive_guidance|Tools and progressive guidance]]
- [[negative_case_semantic_tools|Semantic tools and learning burden]]

## Negative and Limiting Cases

### Formal frameworks introduce entry cost

S2 describes free-form modelling as intuitive while named frameworks and formal conventions create friction. The learner must understand the framework before representing the problem.

Relevant memo:

- [[../03_memos/memo_S2M2|S2M2: Formal frameworks add entry cost]]

### Informal representations can still be useful

Students use lightweight sketches to:

- Clarify an idea before coding
- Explain system architecture
- Coordinate with teammates
- Compare possible designs
- Reduce mental complexity

These models may not satisfy formal notation rules but still perform meaningful cognitive and communicative work.

### Formal notation can obscure purpose

When learners focus on:

- Correct arrows
- Required symbols
- Tool-specific operations
- Framework compliance

the intended modelling question or message can become secondary.

S1 and S2 describe formality becoming arbitrary when its benefit is not visible.

### Precision can add unnecessary cost

Not every modelling task requires:

- Executability
- Automated transformation
- Complete traceability
- Formal verification
- Long-term shared maintenance

Applying maximum formality to a temporary exploratory model can make modelling slower without improving its intended use.

## Refined Interpretation

> Formality should be introduced in proportion to the modelling purpose: lightweight representations can support early reasoning, while formal semantics become valuable when precision, validation, traceability, or automation is required.

Formality is therefore a design choice, not a universal quality level.

## Purpose-Formality Continuum

### 1. Personal exploration

Typical needs:

- Speed
- Flexibility
- Cognitive offloading
- Low commitment

Suitable representations:

- Notes
- Boxes and arrows
- Rough sketches
- Partial diagrams

### 2. Team negotiation

Typical needs:

- Shared vocabulary
- Readability
- Stable identifiers
- Versioning

Suitable representations:

- Lightweight conventions
- Collaborative diagrams
- Agreed local notation
- Selected formal elements

### 3. Stakeholder communication

Typical needs:

- Audience-appropriate abstraction
- Explanation
- Traceability to concerns
- Avoidance of unnecessary technical notation

Suitable representations:

- Purpose-specific views
- Annotated diagrams
- Simplified formal models

### 4. Engineering coordination and assessment

Typical needs:

- Consistency
- Explicit semantics
- Comparable quality criteria
- Cross-model links

Suitable representations:

- Standard modelling languages
- Typed modelling tools
- Rationale and traceability

### 5. Execution, transformation, or verification

Typical needs:

- Precise syntax and semantics
- Constraints
- Machine-processable models
- Deterministic validation where possible

Suitable representations:

- Executable or formal models
- Constraint languages
- Integrated semantic tooling

The continuum does not imply that every model must progress through all stages.

## Progressive Formalisation

A modelling process may begin informally and add precision as purpose becomes clearer:

1. Explore the problem with a lightweight representation.
2. Identify audience and downstream use.
3. Select the necessary notation subset.
4. Add semantic constraints where they provide value.
5. Validate, trace, or execute only when required.

Progressive formalisation can reduce entry burden while preserving the benefits of formal models.

## Risks

### Too little formality

- Ambiguous interpretation
- Invalid relations
- Weak traceability
- Difficult collaboration
- Inability to validate or automate

### Too much formality

- High entry cost
- Tool and notation overload
- Reduced experimentation
- Attention diverted from modelling purpose
- Models abandoned because maintenance cost exceeds value

## Teaching Implications

- Begin with the modelling question and audience.
- Explain why particular formal elements are needed.
- Teach notation subsets progressively.
- Compare informal and formal versions of the same representation.
- Ask what precision adds and what it costs.
- Avoid grading decorative notation that does not serve the task.
- Show transitions from sketches to more disciplined models.

## Tool Implications

Tools can support progressive formalisation through:

- Sketch and formal modes
- Optional semantic constraints
- Conversion of informal elements into typed elements
- Warnings when increased precision is required
- Multiple views for different audiences
- Preservation of rationale during formalisation

## Revised Proposition

> Formal modelling contributes educational and engineering value when its level of semantic discipline matches the representation's purpose and downstream use. Progressive formalisation can preserve low-friction exploration while introducing precision when shared interpretation, validation, traceability, execution, or automation requires it.

## Remaining Tests

- Compare the purposes for which students use informal and formal models.
- Examine whether informal-first work improves later formal models.
- Identify where local notation creates communication failures.
- Determine which formal elements provide the greatest educational value.
- Test whether progressive formalisation reduces tool and framework avoidance.

