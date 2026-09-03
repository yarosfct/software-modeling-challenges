# Security Policy

## Research Data Security

Qualitative Research Pro handles qualitative research data that may include sensitive participant information. Data security is critical.

### Principles

1. **No participant data in commits** — Never commit interview transcripts, field notes, or any data containing participant information to version control
2. **Pseudonyms always** — All examples, templates, and agent outputs use pseudonyms, never real participant names
3. **Local data only** — Research data stays on the researcher's local machine. Agents process data in-session only.
4. **No cloud storage of raw data** — Raw qualitative data should not be stored in cloud services without proper IRB-approved data management plans
5. **Encryption at rest** — Recommend encrypting qualitative data files on disk

### What to Report

If you discover that:
- An agent or skill inadvertently encourages storing participant data in version control
- A hook transmits research data to external services
- A template or example contains real (non-pseudonymized) participant information
- Any component could lead to a breach of research participant confidentiality

Please report it responsibly.

### Reporting

Email security concerns to the repository maintainer. Include:
- Description of the concern
- Steps to reproduce
- Potential impact on research participant confidentiality

### Scope

This policy covers the Qualitative Research Pro codebase only. It does not replace your institution's IRB data management requirements or applicable data protection regulations (GDPR, HIPAA, FERPA, etc.).
