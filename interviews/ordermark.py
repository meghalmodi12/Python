def solution(times, directions):
    result = [None for _ in range(len(times))]
    prevGateState = None

    entryQueue = []
    exitQueue = []

    for i in range(len(times)):
        if directions[i] == 0:
            entryQueue.append([times[i], i])
        else:
            exitQueue.append([times[i], i])

    entryQueue.sort(key = lambda x: x[0])
    exitQueue.sort(key = lambda y: y[0])
    arrTimes = sorted(list(set(times)))

    tick = arrTimes.pop(0)
    entryProcessed = 0

    while entryProcessed < len(times):
        time, employeeIndex = None, None
        currentState = ''

        if prevGateState is None:
            currentState = 'close'
        else:
            currentState = prevGateState

        if currentState == 'open':
            if len(entryQueue) and entryQueue[0][0] <= tick:
                time, employeeIndex = entryQueue.pop(0)
                prevGateState = 'open'
            if employeeIndex is None and len(exitQueue) and exitQueue[0][0] <= tick:
                time, employeeIndex = exitQueue.pop(0)
                prevGateState = 'close'
        else:
            if len(exitQueue) and exitQueue[0][0] <= tick:
                time, employeeIndex = exitQueue.pop(0)
                prevGateState = 'close'
            if employeeIndex is None and len(entryQueue) and entryQueue[0][0] <= tick:
                time, employeeIndex = entryQueue.pop(0)
                prevGateState = 'open'

        if time is None and employeeIndex is None:
            prevGateState = None
            if len(arrTimes):
                tick = arrTimes.pop(0)
            else:
                tick += 1
        else:
            result[employeeIndex] = tick
            entryProcessed += 1
            tick += 1

    return result