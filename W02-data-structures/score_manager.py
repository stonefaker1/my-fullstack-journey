students = [{"name": "张三", "math": 85, "english": 88}, {"name": "李四", "math": 90, "english": 92}, {"name": "王五", "math": 78, "english": 80}, {"name": "赵六", "math": 95, "english": 85}, {"name": "张三", "math": 85, "english": 88}]
for student in students:
    student["total"] = student["math"] + student["english"]
# print(students)

max_student = max(students, key=lambda x: x["math"])
print(max_student)

good_en = [student["name"] for student in students if student["english"] >= 80]
print(good_en)

math_scores = [student["math"] for student in students]
average_math = sum(math_scores) / len(math_scores)
print(average_math)

names = [student["name"] for student in students]
unique_names = set(names)
if len(names) != len(unique_names):
    print("有重复的学生姓名")
    for name in unique_names:
        if names.count(name) > 1:
            print(f"{name} 出现了 {names.count(name)} 次")

print(f"{'姓名':<4} {'数学成绩':<4} {'英语成绩':<4} {'总分':<4}")
print(f"{'----':<4} {'----':<4} {'----':<4} {'----':<4}")
for s in students:
    print(f"{s['name']:<4} {s['math']:<4} {s['english']:<4} {s['total']:<4}")