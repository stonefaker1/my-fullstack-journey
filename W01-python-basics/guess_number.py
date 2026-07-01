import random
target = random.randint(1, 100)
count = 0
while True:
    guess = int(input("猜数字：1-100："))
    if guess < target:
        print("小了")
    elif guess > target:
        print("大了")
    else:
        print("猜对了！")
        break
