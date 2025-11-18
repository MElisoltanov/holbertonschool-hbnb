# HBnB

## 🔖 Table of contents

<details>
  <summary>
    CLICK TO ENLARGE 😇
  </summary>
  📄 <a href="#description">Description</a>
  <br>
  📂 <a href="#files-description">Files description</a>
  <br>

  🔧 <a href="#whats-next">What's next?</a>
  <br>
  ♥️ <a href="#thanks">Thanks</a>
  <br>
  👷 <a href="#authors">Authors</a>
  </details>

## 📄 <span id="description">Description</span>

The HBnB project, developed as part of Holberton School's curriculum, is a replica of the Airbnb platform. 

It focuses on building a web application enabling users to create, browse, and reserve lodging listings.

## ⚙️ <span id="architecture">Architecture Overview</span>

- The application follows a multi-layered architecture separating concerns across the following layers:
- Models Layer: Defines SQLAlchemy ORM mappings for entities (User, Place, Review, Amenity, etc.).

- Persistence Layer (Repository Pattern): Manages CRUD operations and abstracts direct database interaction.
- Service Layer (Facade Pattern): Acts as an intermediary between the API and repositories, ensuring business logic consistency.
- API Layer (Flask-RESTX): Exposes endpoints for the main entities, secured with JWT-based authentication.

## 📂 <span id="files-description">File description</span>

| **FILE**            | **DESCRIPTION**                                   |
| :-----------------: | ------------------------------------------------- |
| `part1`       | Documentation and UML files.                          |
| `part2`       | Implementation of Business Logic and API Endpoints.                          |
| `part3`   | Integration of SQLAlchemy ORM, JWT authentication, and database persistence.                          |
| `README.md`     | README file.                        |


## 🧩 <span id="Implemented Features">Implemented Features</span>


- Full SQLAlchemy integration

- Entities (User, Place, Review, Amenity) mapped as SQLAlchemy models.

- Common attributes (id, created_at, updated_at) handled by a shared BaseModel.

- User Repository & Facade Refactor

- Introduced UserRepository for entity-specific queries.

- Updated HBnBFacade to interact with repositories using SQLAlchemy.

- Secure Password Handling

- Passwords are hashed using Flask-Bcrypt before storage.

- Added verification methods for authentication.

- JWT Authentication

- Users can log in to receive tokens.

- Protected routes require a valid JWT.

- Role-based access control (admin vs regular user).

- Persistent Storage

- Data is stored in a relational database instead of in-memory structures.

- Supports full CRUD operations on users, places, reviews, and amenities.

- RESTful API Enhancements

- Added endpoints for creating users, logging in, managing places, and posting reviews.

- Consistent use of namespaces and request models.
## 💡Installation & Run the application

 1. Clone the repository:
 ```
   https://github.com/MElisoltanov/holbertonschool-hbnb.git 
```

2. Create a Virtual Environment (Recommended)
```
python3 -m venv venv  
source venv/bin/activate 
``` 
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
 python run.py
```

## 🔧 <span id="whats-next">What's next?</span>

Implement frontend integration for a visual interface.

Add pagination and filtering for large datasets.

Extend testing coverage with automated unit and integration tests.

Deploy the application with a production-ready database (e.g., PostgreSQL).

## 🔧 Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-DA291C?logo=databricks&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-0078D4?logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)

## ♥️ <span id="thanks">Thanks</span>

- The helpers. 

## 👷 <span id="authors">Authors</span>

**- [Flora S.](https://github.com/flor4)**

**- [Moussa E.](https://github.com/MElisoltanov)**

**- [Daniel R.](https://github.com/ofest)**
