firstInput = input().split(" ")
numGon = int(firstInput[0])
numGroup = int(firstInput[1])

capaGon = []
for i in range(numGon):
    capaGon.append(int(input()))

memberGroup = []
for i in range(numGroup):
    memberGroup.append(int(input()))

currentPeople = 0

for i in memberGroup:
    currentPeople = currentPeople + i

totalPeopleForGon = []
for i in range(numGon):
    totalPeopleForGon.append(0)


count = 0
while currentPeople != 0:
    for index, i in enumerate(capaGon):
        if memberGroup[count] - i > 0:
            remnant = memberGroup[count] - i
            memberGroup.insert(count + 1, remnant)
            currentPeople = currentPeople - i
            totalPeopleForGon[index] = totalPeopleForGon[index] + i
        else:
            currentPeople = currentPeople - memberGroup[count]
            totalPeopleForGon[index] = totalPeopleForGon[index] + memberGroup[count]

        count += 1
        if currentPeople == 0:
            break
        if count == len(memberGroup):
            break
    if count == len(memberGroup):
        break

for i in totalPeopleForGon:
    print(i)
