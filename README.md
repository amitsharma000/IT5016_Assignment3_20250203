# IT5016_Assignment3_20250203

## Project Title
**Ferry- The Requisition System Project**

## Project Overview

This Python application serves as a simple data collection system for staff entries along with purchase-request administration based on total monetary value.
The system requests staff members to provide their name and identify while recording their requested items.
The system calculates complete item prices after which automatic approval happens if the total stays under $500 otherwise manager approval takes effect. 
A unique ID number assigns to every requisition for effective organization.
A computer program developed through basic programming elements while incorporating some class material about software principles.


## Software Design Principles Analysis

### 1. KISS (Keep It Simple, Stupid)

I avoided developing complex or showy code for this task. 
The program only performed essential operations which included get_staff_details(), add_items(), check_approval() and show_details().  
The functions perform only the tasks their names indicate.
The programming remained straightforward and it enabled both testing and understanding.
The document follows a straightforward presentation alongside basic printouts that anyone can easily understand.

### 2. Open/Closed Principle (OCP)

I designed this project with future expansion in mind because different features can be added without impacting the existing operational framework.    
Since the system welcomes new elements while maintaining its current operational effectiveness it remains open to change.


### 3. DRY (Don't Repeat Yourself)

The code maintains DRY by using reusable class methods and avoiding redundant logic.    
Operations such as record addition and listing are centralized in methods that can be reused multiple times without rewriting logic.
This approach enhances maintainability and ensures consistency across the application.


### 4. YAGNI (You Aren’t Gonna Need It)

The code written strictly follows the YAGNI principle by including only functionality required to meet the project objectives also there are no unnecessary features like database storage, GUI components, or advanced filtering. This helps keep the project lightweight and focused.

### 5. Composition Over Inheritance

Since this system contains only a single class I have excluded inheritance from my design but developed functions which require output results from preceding operations.   
The system collects staff information before it moves on to item addition before processing approval with that accumulated total value. Each function depends on the preceding one which results in a smooth process flow. 

### 6. Separation of Concerns in the coding 

I carried out the separation of each code segment.  
The different program tasks run separately as distinct functions handle input gathering, calculation execution and status evaluation together with result printing.  
The program structure facilitates easy management together with protection from interferences between different program sections.

### 7. Easy to Understand the Code

From my perspective computer code should adopt a design that makes it accessible to every reader. 
I refused to use complex techniques and chose straightforward programming style. The names of variables and functions remain straightforward by describing their actions. 
Some comments together with section titles enhance the overall look of the code.  


## Summary

I developed this program during a small assessment task as its primary author.
I worked to maintain clean code writing while making it simple for teachers to execute the program. 
The software principles enabled me to divide the system into smaller components during design and better arrange the written program.The process of development helped me learn many things and future improvements are possible for any needed updates.


## Author
      
**Amit Sharma**  
**Student ID**: 20250203  
**Course**: IT5016 - Software Research and Practice
