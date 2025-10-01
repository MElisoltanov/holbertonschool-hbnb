## Sequence Diagram Place Criteria
```mermaid
sequenceDiagram
Actor User
participant API
participant BusinessLogic
participant Database

User->>API: User Requests Places Criterias
API->>BusinessLogic: Validate and Process Request
BusinessLogic->>Database: Search For Specific Data
Database-->>BusinessLogic: Return Data Found
BusinessLogic-->>API: Return Response
API-->>User: Return Success/Failure
```