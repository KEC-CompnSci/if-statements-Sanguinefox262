[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18425482)
# Python If Statements Assignment

## Overview
In this assignment, you'll practice using comparison operators and if statements to build a grade calculator system. You'll determine a student's final score, passing status, letter grade, honor roll status, and eligibility for advanced courses.

## Learning Objectives
- Use arithmetic operators to calculate values
- Use comparison operators to compare values
- Implement if, if-else, and if-elif-else statements
- Combine conditions using logical operators (and, or)

## Instructions

### Task 1: Calculate the Final Score
Calculate the `final_score` as the average of `test_score` and `exam_score`.

### Task 2: Determine if the Student Passed
Set the `passed` variable to `True` if the `final_score` is 60 or higher, otherwise set it to `False`.

### Task 3: Assign a Letter Grade
Assign a letter grade based on the `final_score` using these rules:
- Score 90-100: "A"
- Score 80-89: "B"
- Score 70-79: "C"
- Score 60-69: "D"
- Score below 60: "F"

### Task 4: Determine Honor Roll Status
Set the `honor_roll` variable to `True` if the student has:
- A `final_score` of 90 or higher
- All assignments completed (`all_assignments_completed` is `True`)

Otherwise, set it to `False`.

### Task 5: Determine Advanced Course Eligibility
Set the `can_take_advanced` variable to `True` if the student:
- Passed (has a `final_score` of 60 or higher)
- AND either:
  - Has a letter grade of "A" OR
  - Has a letter grade of "B" AND has completed all assignments

Otherwise, set it to `False`.

## Testing Your Code
The assignment includes automatic tests that will check if your solution works correctly. To pass the assignment, all tests must pass. You can run the tests locally to check your progress.

## Tips
- Pay attention to the order of operations in your calculations
- Be careful with your comparison operators (>, <, >=, <=, ==, !=)
- Make sure you're using the correct logical operators (and, or) when combining conditions
- Check the output printed to make sure your variables have the expected values

Good luck!