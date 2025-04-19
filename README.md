# IT5016_Assignment3_20250203
# IT5016 Assignment 3 - Software Design Analysis

##  GitHub Repository
https://github.com/amitsharma000/IT5016_Assignment3_20250203/edit/main/README.md


## Project Overview
This project is a simple Student Record Manager written in Python. It allows you to add, list, and remove student records.


##  Software Design Principles Analysis

###  1. Single Responsibility Principle (SRP)

- `Student` class handles student data only.
- `StudentRecordManager` handles record operations only.
  
>  _Each class has **one clear reason to change** — this is a good application of SRP._



###  2. Open/Closed Principle (OCP)

- The current design is **not fully OCP-compliant** because new functionality (like search, file export) requires modifying existing methods.
- Future improvements could involve:
  - Abstract base classes or interfaces
  - Dependency injection or strategy patterns



###  3. DRY 

- Code avoids repetition by using object-oriented design.
- `Student` creation and listing logic are reusable.



###  4. KISS 

- Code is clean, readable, and modular.
- No unnecessary abstractions or over-engineering.



###  5. YAGNI 

- No unnecessary features like databases or search functionality — only what's required for the task.



##  Summary

This Student Record Manager is a clean, minimal Python application that demonstrates sound object-oriented principles. The system is well-structured and leaves room for future extensibility.

### Future Improvements

- Add file-based storage (JSON or SQLite)
- Add input validation and error handling
- Implement search and update functionality



## Author

Your Name: Amit 
Student ID: 20250203  
Course: IT5016 Software Research and Practice  
