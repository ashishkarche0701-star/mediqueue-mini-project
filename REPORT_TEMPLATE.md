# Mini Project Report — Hospital Emergency Management System (MP2)

**Submitted to:** [College / University]  
**Submitted by:** [Student name and roll number]  
**Guided by:** [Guide name]  
**Academic year:** [Year]

## Certificate
[Add your institution's required certificate wording and signature fields.]

## Acknowledgement
[Personalize this section in your own words.]

## Contents
Introduction; Problem Statement; Objectives; Motivation; Scope and Rationale; Methodological Details; Results; Analysis; Inferences; Conclusion; Suggestions; References.

## Introduction and problem statement
This educational web application demonstrates patient-record management using a singly linked list and emergency-first scheduling using a priority queue concept.

## Objectives
- Register demo patient records with input validation.
- Schedule emergency-priority records before normal-priority records.
- Preserve arrival order within each priority group.
- Demonstrate linked-list traversal for patient records.
- Track Waiting, In Treatment, and Treated statuses.

## Methodology
Python, Flask, SQLite, HTML and CSS. SQLite persists records; `PatientLinkedList` links nodes and supports traversal. Waiting patients are sorted by priority with a stable ordering, so equal-priority arrivals remain in arrival order.

## Results, analysis and inferences
Run the app and insert genuine screenshots. Record test cases and outcomes only after executing them; do not claim unperformed tests. Discuss invalid input, empty queue, emergency priority, stable ordering, and limitations.

## Conclusion and suggestions
Summarize verified outcomes. Possible extensions include authentication, audit logging, accessibility testing and a proper clinical-grade triage process; this prototype is not for real medical use.

## References
Add sources actually consulted, such as official Python, Flask and SQLite documentation and your course notes.
