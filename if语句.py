# 需求：给出一个年龄，判断年龄是否满18岁，不满18岁则打印：未满18岁，禁止观看
# age = int(input("请输入你的年龄："))
# if age <18:
#     print("未满18岁，禁止观看")
# else:
#     print("欢迎观看")

# 2.if-else语句
# 需求:给出一个年龄，判断年龄是否满18岁，不满18岁则打印：未满18岁，禁止观看，对18岁以上的可以观看

# 3.if-elif-else语句
# 需求：给出年龄判断年龄段如果1-14将打印儿童，15-30打印青年，36-60打印中年，61及以后打印老年
# age = int(input("请输入你的年龄："))
# if 1 <= age <= 14:
#     print("您的年龄段属于儿童")
# elif 15 <= age <=30:
#     print("您的年龄段属于请你")
# elif 36 <= age <= 60:
#     print("您的年龄段属于中年")
# else:
#     print("您的年龄段属于老年")
#
# 猜拳游戏
import random
# 1.从控制输入要出拳，1石头 2剪刀 3布
player = int(input("请输入1石头 2剪刀 3布您的选择是:"))
# 2. 电脑出拳
computer = random.randint(1,3)

# 3. 判断玩家胜负
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("恭喜玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")










