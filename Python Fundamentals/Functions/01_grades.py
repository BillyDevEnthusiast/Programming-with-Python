def get_grade_text(score):
    if 2.0 <= score <= 2.99:
        return "Fail"
    if 3.0 <= score < 3.5:
        return "Poor"
    if 3.5 <= score < 4.5:
        return "Good"
    if 4.5 <= score < 5.5:
        return "Very Good"
    if 5.5 <= score <= 6.0:
        return "Excellent"


score = float(input())
print(get_grade_text(score))
