# Cross-Case Comparison: Cross-Family Modelling and Integration

## Agreed Interpretation

> Cross-family modelling should be taught as explicit translation and coordination work, using continuous examples and trace links, rather than assuming competence transfers automatically between independently taught notations.

## Integration Is More Than Notation Switching

Cross-family work requires learners to understand:

- What question each model answers
- Which concepts correspond across representations
- What information should be preserved, transformed, added, or omitted
- How abstraction and granularity change between models
- How consistency can be checked across perspectives
- Where no direct one-to-one mapping exists

A learner may understand each notation separately and still fail to construct a coherent chain of representations.

## Evidence from Lecturer Cases

### L1

The course moves across BPMN, SysML, and feature modelling. The lecturer reports cross-model interference and difficulty adopting the different reasoning required by variability modelling, particularly optional-versus-mandatory distinctions.

### L3

The lecturer stresses that modelling-family tool requirements differ. BPMN, UML, and executable models need different forms of validation, collaboration, and execution support. Treating BPMN as merely analogous to UML activity diagrams hides important differences.

### L4

The Requirements Engineering course deliberately spans:

- Strategic actor-goal modelling
- Detailed rationale modelling
- Non-functional requirement refinement
- Translation into UML

The intended competence is not simply producing each diagram. Students must maintain meaning and consistency while moving from organisational goals and stakeholder concerns toward more concrete software representations.

## Evidence from Student Cases

### S3

Repeated exposure to BPMN across courses produces a head start, showing that some knowledge transfers when the same modelling family is revisited. However, advanced terminology and notation still require deeper learning.

### S4 and S5

Students report that diagrams sharing the UML label may still demand different forms of reasoning. Sequence diagrams introduce temporal and interaction reasoning that can feel like a reset despite prior class-diagram experience.

### S6

The clearest integration failure occurs when a syntactically acceptable UML class model loses the goals expressed in an earlier iStar model. The difficulty is not drawing classes or actors; it is preserving traceability and rationale across representational levels.

## What Can Transfer

Potentially transferable competence includes:

- Recognising modelling purpose and audience
- Identifying relevant entities, actors, events, and relationships
- Managing abstraction and granularity
- Checking readability and internal consistency
- Explaining and justifying representational choices
- Tolerating multiple defensible alternatives

Transfer is more likely when these general modelling practices are named explicitly rather than left embedded within one notation.

## What May Not Transfer Automatically

- Construct semantics and permissible relationships
- The worldview or modelling question of each family
- Stopping rules and appropriate granularity
- Quality criteria specific to a model type
- Translation criteria between perspectives
- Tool workflows and validation capabilities
- Traceability between goals, requirements, design, behaviour, and implementation

Similar visual conventions may create false confidence while concealing different semantics or purposes.

## Continuous Example Principle

A continuous example should follow one evolving problem across modelling families. It should show:

1. The question addressed by each representation.
2. The source information used to build it.
3. Which elements carry over from the previous model.
4. Which elements are transformed, refined, introduced, or intentionally omitted.
5. Trace links between related elements.
6. Consistency checks and possible contradictions.
7. Alternatives and rationale where mappings are not deterministic.
8. How later changes propagate backward or forward through the model chain.

The example should expose translation decisions rather than present a sequence of disconnected finished diagrams.

## Pedagogical Implications

- Teach model families through their purposes and perspectives, not only symbol sets.
- Include explicit translation tasks in teaching and assessment.
- Ask students to justify what was preserved or changed between models.
- Use cross-model inconsistency exercises.
- Revisit one case across a course instead of replacing the domain for every notation.
- Distinguish general modelling heuristics from family-specific rules.
- Assess traceability and rationale alongside individual diagram quality.

## Tool Implications

Useful cross-family support includes:

- Shared element repositories or identifiers
- Explicit trace links
- Change-impact warnings
- Model-text and model-model comparison
- Cross-model consistency checks
- Integrated rationale and alternative recording
- Views tailored to each family without losing shared context

Tool integration should not imply automatic one-to-one transformation where modelling judgement is required.

## Boundary Conditions

- Not every course needs multiple modelling families.
- Repeated exposure to one family can deepen competence without cross-family integration.
- A single continuous example may become too large unless carefully scoped.
- Traceability can add overhead and should be aligned with learning purpose.
- Some mappings are interpretive and cannot be completely automated.
- Visual similarity does not establish semantic equivalence.

## Provisional Explanatory Statement

> Cross-family difficulty arises when learners must preserve purpose and meaning while changing representational perspective. Independent knowledge of each notation is insufficient because integration requires explicit decisions about correspondence, refinement, omission, and consistency. Continuous examples, rationale, and trace links can make this translation work observable and learnable.

## Category Connections

- **Representational challenges:** translation, correspondence, consistency, and changing perspectives
- **Learner responses and strategies:** mapping, narrating, documenting alternatives, and checking traceability
- **Pedagogical scaffolding and feedback:** continuous examples and explicit integration exercises
- **Technical mediation and tool support:** trace links, consistency checks, and cross-family environments
- **Social and contextual conditions:** prior exposure and familiarity with each modelling family
- **Assessment and course architecture:** sequencing, repeated exposure, and cross-model assessment
- **Modelling outcomes and perceived value:** coherent model chains or fragmented disconnected artefacts

## Remaining Evidence Checks

- Compare transfer within UML diagram types with transfer across distinct modelling families.
- Identify which general modelling practices participants explicitly recognise as transferable.
- Examine whether continuous examples improve integration or create cognitive overload.
- Distinguish tool fragmentation from conceptual fragmentation.
- Determine which traceability relationships are educationally essential.

