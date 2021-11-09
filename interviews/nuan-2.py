"""
data = [
    ["Inpatient Facility", "Maternity"],
    ["Maternity", "Mother"],
    ["Maternity", "Well Newborn"],
     ["Professional", "Inpatient Visits"],
    ["Skilled Nursing Facility"],
    ["Professional", "Inpatient Surgery"],
]

Example of patient visits:

1. Inpatient Facility -> Maternity -> Well Newborn
2. Professional -> Inpatient Visits
3. Skilled Nursing Facility

Goal:

Develop a routine that provides N random patient visits.
"""
import random

def getChoices(val, arrData):
    arrChoices = []

    for data in arrData:
        if data[0] == val:
            arrChoices.append(data)

    return arrChoices

def generateVisits(arrData, n):
    arrResult = []
    setRoot = set()
    setNonRoot = set()

    for i in range(len(arrData)):
        rootNode = arrData[i][0]
        nodeFound = False

        for j in range(len(arrData)):
            if j != i:
                if rootNode in arrData[j][1:]:
                    nodeFound = True
                    break

        if not nodeFound:
            setRoot.add(rootNode)
        else:
            setNonRoot.add(rootNode)

    arrRootNodes = list(setRoot)
    arrNonRootNodes = list(setNonRoot)

    while n > 0:
        currentRoot = random.choice(arrRootNodes)
        currentChoice = random.choice(getChoices(currentRoot, arrData))

        if len(currentChoice) == 1:
            arrResult.append(currentChoice)
        else:
            while currentChoice[-1] in arrNonRootNodes:
                tempChoice = random.choice(getChoices(currentChoice[-1], arrData))
                currentChoice.extend(tempChoice[1:])
            arrResult.append(currentChoice)

        n -= 1

    return arrResult


data = [
    ["Inpatient Facility", "Maternity"],
    ["Maternity", "Mother"],
    ["Maternity", "Well Newborn"],
    ["Professional", "Inpatient Visits"],
    ["Skilled Nursing Facility"],
    ["Professional", "Inpatient Surgery"],
]

result = generateVisits(data, 10)

for r in result:
    print(" -> ".join(r))

