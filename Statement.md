1. Problem Statement

Students often struggle to manually calculate their semester GPA because it requires applying formulas, weighting credit hours, and converting marks into grade points. 
This process is time-consuming and prone to mistakes. 
The goal of this project is to build a simple Python program that automates GPA calculation and makes the process quick, accurate, and user-friendly.

Scope of the Project

This project focuses on creating a command-line based GPA calculator using Python. The scope includes:

Accepting course details such as course name, credits, and marks.

Allowing two marking methods: total marks or separate components (Mid-Sem, Internals, End-Sem).

Converting marks into grade points using a simple formula.

Calculating the final GPA based on credit-weighted grade points.

Providing a clean and error-handled user experience.

The project does not include a GUI, grade-letter mapping, or database storage at this stage.


Target Users

College students who want a quick way to calculate their GPA.

Beginners in Python looking for a simple project to understand functions, loops, and user inputs.

Teachers or mentors who may want to demonstrate GPA logic in programming classes.


4. High-Level Features

User-friendly input system for entering course details.

Option to enter total marks or Mid-Sem + Internal + End-Sem marks.

Automatic grade-point calculation using Python’s math.ceil() function.

Weighted GPA calculation based on total course credits.

Basic validation to avoid incorrect or out-of-range inputs.
