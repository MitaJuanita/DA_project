```mermaid
flowchart TD
    A[WITH filtered_data
    Filter by diagnosis & date] -->|Pass filtered patients| B[aggregated_data
    Join vitals & prescriptions]
    
    B -->|Get eligible patients| C[ranked_patients
    Assign trial groups]
    
    C -->|Order results| D[Final SELECT
    Get trial groups]

    %% Add tooltips for each step
    click A "Filters last 24 months of encounters"
    click B "Joins patient vitals and prescriptions"
    click C "Assigns patients to trial groups A or B"
    click D "Orders and returns final results"

    %% Style nodes with meaningful colors
    style A fill:#e0f2ff,stroke:#007acc,stroke-width:2px
    style B fill:#d9f99d,stroke:#65a30d,stroke-width:2px
    style C fill:#fde68a,stroke:#ca8a04,stroke-width:2px
    style D fill:#fca5a5,stroke:#dc2626,stroke-width:2px
```
## 🧠 Conceptual Analogy
- Think of CTEs like temporary scratchpads. Each CTE holds a “sub-result” that you’ll build on.

### It’s like a pipeline:

- First, filter the data.

- Then join it with other filtered data.

- Then perform aggregation or classification.

- Each step is a clean, named unit.