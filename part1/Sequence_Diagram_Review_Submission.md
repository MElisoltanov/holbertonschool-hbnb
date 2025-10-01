## Sequence Diagram Review Submission
```mermaid
sequenceDiagram
Actor User
participant API
participant BusinessLogic
participant Database

User->>API: Review Submit By User
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Save User Review Data
Database-->>BusinessLogic: Confirm Saved User Review Data
BusinessLogic-->>API: Return Response
API-->>User: Return Success/Failure
```