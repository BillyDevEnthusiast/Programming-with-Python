n = int(input())

students = {}

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

students_average_4_5 = {}

for key, value in students.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        students_average_4_5[key] = average

for key, value in sorted(students_average_4_5.items(), key=lambda kv: -kv[1]):
    print(f"{key} -> {value:.2f}")
