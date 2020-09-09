class Solution:
    def __init__(self, data):
        self.data = data

    def generatePowerSet(self): 
        data = self.data
        num = (2 ** len(data)) - 1
        result = []

        while num >= 0:
            tempNum = num
            tempArr = []
            tempData = []

            while tempNum > 0:
                tempArr.append(tempNum % 2)
                tempNum = tempNum // 2

            for i in range(len(tempArr)):
                if tempArr[i] == 1:
                    tempData.append(data[i])

            result.append("".join(tempData))
            num -= 1

        return result

if __name__ == "__main__":
    S = Solution('a')
    print(S.generatePowerSet())

        


            
