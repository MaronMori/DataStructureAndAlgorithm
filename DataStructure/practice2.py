# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def valueChange(target):
    value = ""
    if target == "#":
        value = "."
        return value
    else:
        value = "#"
        return value


highAndWide = input()
highAndWide = highAndWide.split(" ")
rowsInput = []
for i in range(int(highAndWide[0])):
    rowsInput.append(list(input()))

target = input().split(" ")
targetY = int(target[0])
targetX = int(target[1])

changedValue = valueChange(rowsInput[targetY][targetX])
rowsInput[targetY][targetX] = changedValue

# 左上角
if targetY == 0 and targetX == 0:
    # 右
    changedValue = valueChange(rowsInput[targetY][targetX + 1])
    rowsInput[targetY][targetX + 1] = changedValue
    # 下
    changedValue = valueChange(rowsInput[targetY + 1][targetX])
    rowsInput[targetY + 1][targetX] = changedValue

# 右下角
elif targetY == int(highAndWide[0]) - 1 and targetX == int(highAndWide[1]) -1:
    # 左
    changedValue = valueChange(rowsInput[targetY][targetX - 1])
    rowsInput[targetY][targetX - 1] = changedValue
    # 上
    changedValue = valueChange(rowsInput[targetY - 1][targetX])
    rowsInput[targetY - 1][targetX] = changedValue

# 左下角
elif targetY == int(highAndWide[0]) - 1 and targetX == 0:
    # 上
    changedValue = valueChange(rowsInput[targetY - 1][targetX])
    rowsInput[targetY - 1][targetX] = changedValue
    # 右
    changedValue = valueChange(rowsInput[targetY][targetX + 1])
    rowsInput[targetY][targetX + 1] = changedValue

# 右上角
elif targetY == 0 and targetX == int(highAndWide[1]) -1:
    # 左
    changedValue = valueChange(rowsInput[targetY][targetX - 1])
    rowsInput[targetY][targetX - 1] = changedValue
    # 下
    changedValue = valueChange(rowsInput[targetY + 1][targetX])
    rowsInput[targetY + 1][targetX] = changedValue

elif targetY == 0:
    # 左　
    changedValue = valueChange(rowsInput[targetY][targetX - 1])
    rowsInput[targetY][targetX - 1] = changedValue
    # 右
    changedValue = valueChange(rowsInput[targetY][targetX + 1])
    rowsInput[targetY][targetX + 1] = changedValue
    # 下
    changedValue = valueChange(rowsInput[targetY + 1][targetX])
    rowsInput[targetY + 1][targetX] = changedValue

elif targetX == 0:
    # 上
    changedValue = valueChange(rowsInput[targetY - 1][targetX])
    rowsInput[targetY - 1][targetX] = changedValue
    # 下
    changedValue = valueChange(rowsInput[targetY + 1][targetX])
    rowsInput[targetY + 1][targetX] = changedValue
    # 右
    changedValue = valueChange(rowsInput[targetY][targetX + 1])
    rowsInput[targetY][targetX + 1] = changedValue

elif targetY == int(highAndWide[0]) - 1:
    # 左　
    changedValue = valueChange(rowsInput[targetY][targetX - 1])
    rowsInput[targetY][targetX - 1] = changedValue
    # 右
    changedValue = valueChange(rowsInput[targetY][targetX + 1])
    rowsInput[targetY][targetX + 1] = changedValue
    # 上
    changedValue = valueChange(rowsInput[targetY - 1][targetX])
    rowsInput[targetY - 1][targetX] = changedValue

elif targetX == int(highAndWide[1]) - 1:
    # 上
    changedValue = valueChange(rowsInput[targetY - 1][targetX])
    rowsInput[targetY - 1][targetX] = changedValue
    # 下
    changedValue = valueChange(rowsInput[targetY + 1][targetX])
    rowsInput[targetY + 1][targetX] = changedValue
    # 左　
    changedValue = valueChange(rowsInput[targetY][targetX - 1])
    rowsInput[targetY][targetX - 1] = changedValue
else:
    # 上
    changedValue = valueChange(rowsInput[targetY - 1][targetX])
    rowsInput[targetY - 1][targetX] = changedValue
    # 下
    changedValue = valueChange(rowsInput[targetY + 1][targetX])
    rowsInput[targetY + 1][targetX] = changedValue
    # 左　
    changedValue = valueChange(rowsInput[targetY][targetX - 1])
    rowsInput[targetY][targetX - 1] = changedValue
    print(targetX)
    # 右
    changedValue = valueChange(rowsInput[targetY][targetX + 1])
    rowsInput[targetY][targetX + 1] = changedValue

for row in rowsInput:
    print("".join(row))

