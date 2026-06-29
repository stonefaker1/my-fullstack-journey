height = float(input("请输入你的身高（m）："))
weight = float(input("请输入你的体重（kg）："))
bmi = weight / (height ** 2)
if bmi < 18.5:
    level = "体重过轻"
elif bmi < 24:
    level = "体重正常"
elif bmi < 28:
    level = "体重超重"
else:
    level = "体重配胖"

print(f"你的 BMI 是 {bmi: .2f}，属于 {level}")
