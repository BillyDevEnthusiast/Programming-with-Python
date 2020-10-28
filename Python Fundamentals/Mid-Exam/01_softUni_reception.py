import math

students_per_hour_employee1 = int(input())
students_per_hour_employee2 = int(input())
students_per_hour_employee3 = int(input())
students_count = int(input())

total_students_per_hour = students_per_hour_employee1 + students_per_hour_employee2 + students_per_hour_employee3

if total_students_per_hour > 300:
    total_students_per_hour = 300

time_initial = math.ceil(students_count / total_students_per_hour)

time_final = 0

for i in range(1, time_initial + 1):
    time_final += 1
    students_count -= total_students_per_hour

    if i % 3 == 0:
        time_final += 1

    if students_count <= 0:
        break

print(f"Time needed: {time_final}h.")
