# IT5016_Assignment3_20250203

## Project Title
**Student Record Manager**

## Course Information
- **Student Name**: Amit  
- **Student ID**: 20250203  
- **Course**: IT5016 - Software Research and Practice

## GitHub Repository
[GitHub Link](https://github.com/amitsharma000/IT5016_Assignment3_20250203)

---

## Project Overview

This project is a simple, console-based Student Record Manager written in Python. The application allows users to add, list, and remove student records. It is designed using core object-oriented principles and follows software design best practices, making it clean, readable, and extensible.

---

## Software Design Principles Analysis

### 1. Single Responsibility Principle (SRP)

This principle is well observed in the application. The `Student` class has the sole responsibility of encapsulating student data, such as name and ID. The `StudentRecordManager` class handles all the operations related to managing the list of student records, including adding, displaying, and deleting entries. By assigning each class a distinct role, the code becomes easier to manage and modify, as changes in one responsibility area won’t impact others.

> Each class has one clear reason to change.

---

### 2. Open/Closed Principle (OCP)

The current design is not fully compliant with OCP, as new features like search or export require modifications to existing methods in `StudentRecordManager`. To better align with OCP, future improvements could include implementing abstract base classes or introducing design patterns like Strategy or Factory. These patterns allow functionality to be extended without altering existing code, improving scalability.

>  Feature extensions currently require code modifications — room for improvement.

---

### 3. DRY (Don't Repeat Yourself)

The code maintains DRY by using reusable class methods and avoiding redundant logic. Operations such as record addition and listing are centralized in methods that can be reused multiple times without rewriting logic. This approach enhances maintainability and ensures consistency across the application.

>  Repetition is minimized through object-oriented design.

---

### 4. KISS (Keep It Simple, Stupid)

This application keeps things simple and straightforward. It avoids unnecessary abstractions and does not overcomplicate logic. Classes and methods are short, purpose-driven, and easy to understand. This simplicity is especially beneficial in academic and early-stage project development, where readability and clarity are key.

>  Clean, readable code that’s easy to follow.

---

### 5. YAGNI (You Aren’t Gonna Need It)

The code strictly follows the YAGNI principle by including only the functionality required to meet the project objectives. There are no unnecessary features like database storage, GUI components, or advanced filtering. This helps keep the project lightweight and focused.

>  No bloated features — only essential functionality is implemented.

---

## Summary

The Student Record Manager showcases effective use of software design principles. It is minimal, well-structured, and designed for clarity and maintainability. While the current version is basic, it lays a solid foundation for further development and feature enhancements.

---

## Future Improvements

- Add persistent storage using JSON or SQLite.
- Implement search and update functionality.
- Introduce input validation and error handling.
- Apply design patterns (e.g., Strategy) for better extensibility.

---

## Author

**Amit Sharma**  
**Student ID**: 20250203  
**Course**: IT5016 - Software Research and Practice
