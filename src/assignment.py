# Grade Calculator Assignment
# This script calculates a student's academic standing based on their scores and assignment completion.

# Do not modify these test scores and settings
test_score = 85
exam_score = 78
all_assignments_completed = True

# TASK 1: Calculate the final score as the average of test_score and exam_score
# ===== YOUR CODE HERE =====
class_grade = ((test_score + exam_score) / 2)
final_score = int(class_grade)
  # Replace None with the calculation
print(final_score)
# ===== END YOUR CODE =====

# TASK 2: Determine if the student passed
# A student passes if their final_score is 60 or higher
# ===== YOUR CODE HERE =====
if final_score >= 60:
    passed = True
else:
    passed = False
  # Set to True or False using an if statement

# ===== END YOUR CODE =====

# TASK 3: Assign a letter grade based on the final_score
# Score 90-100: "A"
# Score 80-89: "B"
# Score 70-79: "C"
# Score 60-69: "D"
# Score below 60: "F"
# ===== YOUR CODE HERE =====
if final_score >= 90:
    letter_grade = "A"
elif final_score >= 80 and final_score <= 89:
    letter_grade = "B"
elif final_score >= 70 and final_score <= 79:
    letter_grade = "C"
elif final_score >= 60 and final_score <= 69:
    letter_grade = "D"
else:
    letter_grade = "F"
  # Set the letter grade using if-elif-else

# ===== END YOUR CODE =====

# TASK 4: Determine honor roll status
# To be on the honor roll, a student needs:
# - A final_score of 90 or higher
# - All assignments completed
# ===== YOUR CODE HERE =====
if final_score >= 90:
    honor_roll = True
else:
    honor_roll = False
honor_roll = None  # Set to True or False using an if statement

# ===== END YOUR CODE =====

# TASK 5: Determine if the student can take the advanced course
# Students can take the advanced course if:
# - They passed (final_score >= 60)
# - AND they either:
#   - Have a letter grade of "A" OR
#   - Have a letter grade of "B" AND have completed all assignments
# ===== YOUR CODE HERE =====
if passed == True and letter_grade == "A" or letter_grade == "B":
    can_take_advanced = True
else:
    can_take_advanced == False
  # Set to True or False using if statements with AND/OR

# ===== END YOUR CODE =====

# This prints the results (do not modify)
print("Final Score:", final_score)
print("Passed:", passed)
print("Letter Grade:", letter_grade)
print("Honor Roll:", honor_roll)
print("Can Take Advanced Course:", can_take_advanced)