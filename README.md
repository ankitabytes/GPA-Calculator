# GPA-Calculator
Beginner-friendly Python project built while learning programming concepts
This project is a simple and easy-to-use Python-based GPA Calculator that helps students calculate their semester GPA using course credits and marks. The program allows users to enter marks either as a total or by separating Mid-Sem, Internal, and End-Sem scores. It then converts the marks into grade points and calculates the final GPA.

Features

~GPA calculation based on credits and marks

~Two modes of marks entry:

~Enter total marks

~Enter Mid-Sem + Internal + End-Sem marks

~Uses Python’s built-in math library

~Handles incorrect inputs gracefully

~Lightweight and beginner-friendly

Technologies Used

~Python 3.x

~math module

GPA-Calculator/
│
├── gpa_calculator.py     # Main project script
├── README.md             # Documentation file
└── (Optional files like screenshots or PDFs)

Input Section

The user provides:

Number of courses

Whether they want to:

Enter total marks (0), or

Enter Mid-Sem, Internal, and End-Sem marks separately (1)

For each course, the user enters:

Course name

Course credits

Marks

GPA Calculation

Grade points are calculated as:

grade_point = ceil(total_marks / 10)


Final GPA is computed with:

GPA = total (grade_point × credits) / total_credits
