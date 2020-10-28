import sys
import math

count_students = int(input())
count_lectures = int(input())
initial_bonus = int(input())

max_bonus = -sys.maxsize
attendances = 0
students_enough = True

if count_students == 0:
    max_bonus = 0
    attendances = 0
    students_enough = False
    print(f"Max Bonus: {max_bonus}.")
    print(f"The student has attended {attendances} lectures.")

for student in range(1, count_students + 1):
    student_attendance = int(input())
    total_bonus = math.ceil(student_attendance / count_lectures * (5 + initial_bonus))

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        attendances = student_attendance

if students_enough:
    print(f"Max Bonus: {max_bonus}.")
    print(f"The student has attended {attendances} lectures.")
