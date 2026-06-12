# Cross-Case Comparison: Tools and Progressive Guidance

## Agreed Interpretation

Effective educational modelling tools should progressively combine low-friction construction with semantic discipline, explainable feedback, and optional guidance appropriate to learner experience and task complexity.

Guidance should support representational judgement rather than imply that every modelling problem has one correct answer.

## Tool Trade-Off in the Data

### Lightweight and free-form tools

Benefits:

- Easy to begin using
- Fast construction and layout
- Familiar interaction patterns
- Flexible informal sketching
- Lower installation or onboarding burden

Limitations:

- Permit syntactically or semantically invalid models
- Provide little explanation of modelling concepts
- Do not help learners distinguish defensible alternatives
- Can reduce modelling to diagram drawing

### Typed, specialised, or executable tools

Benefits:

- Restrict invalid operations
- Expose relevant modelling vocabulary
- Support syntax or workflow validation
- Make some model semantics observable through execution
- Improve consistency and assessment evidence

Limitations:

- Add interface and configuration complexity
- May introduce secondary languages or concepts, such as OCL
- Can be slow, unreliable, or unsuitable for large models
- Often support one modelling family without cross-model integration
- Usually detect violations without explaining the modelling reasoning

## Lecturer Perspective

- L1 distinguishes drawing tools from modelling tools and wants accessible semantic checking and educational guidance.
- L2 values error prevention and code-related motivation but identifies installation and collaboration limitations.
- L3 uses typed and executable tooling to prevent invalid actions and support grading, while recognising the OCL burden and need for a tutoring layer.
- L4 values semantic iStar support but identifies fragmentation across iStar, NFR, and UML tools.

Lecturers generally value stronger semantic support, but their preferred capabilities differ by modelling family, assessment approach, course scale, and available infrastructure.

## Student Perspective

- S1 experiences feature-rich tooling and notation overload together and prefers simpler interaction.
- S2 values speed and imagines suggestive guidance for difficult representational choices.
- S3 values BPMN-specific vocabulary, hover help, and syntax prevention but reports reliability and scale problems.
- S4 accepts that semantically disciplined tools are heavier, while rejecting unrestricted drawing as sufficient learning support.
- S5 values collaboration and wants semantic consistency checking.
- S6 wants model-text comparison, semantic checks, and integration across modelling families.

Students do not simply prefer easy tools or powerful tools. They want low friction for construction and meaningful assistance at moments of uncertainty.

## Layers of Guidance

### 1. Construction guidance

- Constrained palettes
- Relevant element suggestions
- Templates and starter structures
- Clear notation vocabulary
- Low-friction layout and editing

### 2. Syntactic guidance

- Prevention or warning of invalid connections
- Cardinality and element-type checks
- Immediate, localised error messages

### 3. Semantic explanation

- Explanation of why an element or relation is questionable
- Plain-language interpretation of model fragments
- Comparison between model content and requirements
- Traceability checks across related models

### 4. Representational decision support

- Prompts about missing perspectives or assumptions
- Alternative modelling options with trade-offs
- Questions about abstraction, granularity, audience, or purpose
- Examples relevant to the current type of decision

### 5. Reflective and collaborative support

- Rationale and alternative recording
- Peer comments and review workflows
- Version comparison and revision history
- Model maintenance and shared ownership

The later layers should assist reflection without automatically resolving context-dependent choices.

## Progressive Guidance Principle

Guidance should adapt or be configurable according to:

- Learner experience
- Familiarity with the modelling family
- Task novelty and complexity
- Current modelling activity
- Frequency and type of observed errors
- Whether the task is formative or assessed

A possible progression is:

1. Beginners receive constrained construction, terminology support, examples, and explanatory validation.
2. Developing learners receive prompts, comparison tools, and traceability or quality checks.
3. More experienced learners can reduce prompts while retaining on-demand explanations and semantic validation.
4. Advanced learners can focus on integration, rationale, collaboration, execution, and model maintenance.

Guidance should be available on demand and gradually fade where independence is the learning objective.

## Boundaries

- Tools can check formal constraints more reliably than contextual adequacy.
- A warning should not imply that one suggested representation is uniquely correct.
- Automated guidance should reveal criteria and trade-offs rather than generate unexplained final models.
- Tool support cannot replace stakeholder elicitation, peer negotiation, or lecturer judgement in every context.
- More features do not necessarily create better educational support.

## AI-Specific Role

AI is most defensible in the current data as:

- A plain-language explanation layer
- A comparison aid between requirements and models
- A source of alternatives for critique
- A semantic feedback assistant
- A prompt for rationale and overlooked assumptions

Risks include answer substitution, unreliable semantic claims, weakened abstraction practice, and assessment integrity problems. AI guidance should therefore remain explainable, reviewable, and subordinate to learner justification.

## Provisional Explanatory Statement

> Tool support is educationally useful when it reduces incidental construction effort while making modelling semantics and decision criteria more visible. Progressive guidance can move learners from constrained, explanatory assistance toward independent judgement, but tools should preserve space for contextual alternatives, rationale, and human evaluation.

## Category Connections

- **Representational challenges:** tools expose or hide semantic, integration, and quality problems
- **Learner responses and strategies:** learners use validation, explanations, alternatives, and collaboration
- **Pedagogical scaffolding and feedback:** tool guidance can extend feedback but should align with teaching
- **Technical mediation and tool support:** progressive construction, validation, explanation, and reflection
- **Social and contextual conditions:** experience, access, cost, scale, and peer collaboration
- **Assessment and course architecture:** formative versus assessed guidance and AI-integrity constraints
- **Modelling outcomes and perceived value:** confidence, correctness, independence, or tool dependence

## Remaining Evidence Checks

- Determine which guidance layers participants explicitly requested versus those inferred analytically.
- Compare needs across UML, BPMN, iStar, NFR, SysML, and executable modelling.
- Examine when learners disable, ignore, or over-rely on guidance.
- Separate support for learning from support for assessment and grading.
- Identify which forms of feedback are feasible without producing excessive false certainty.

