students = [{"name": "张三", "math": 85, "english": 88}, {"name": "李四", "math": 90, "english": 92}, {"name": "王五", "math": 78, "english": 80}]
for student in students:
    student["total"] = student["math"] + student["english"]
# print(students)

max_student = max(students, key=lambda x: x["total"])
# print(max_student)

good_en = [student["english"] for student in students if student["english"] >= 80]
# print(good_en)

math_scores = [student["math"] for student in students]
average_math = sum(math_scores) / len(math_scores)
print(average_math)
