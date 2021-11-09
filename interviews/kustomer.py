"""
Description
-----------
Any Excel user is probably familiar with the bar chart - a simple plot showing vertical bars to represent the frequency of something you counted. For today's challenge you'll be producing bar charts in ASCII.

Input Description
-----------------
You'll be given four numbers on the first line telling you the start and end of the horizontal (X) axis and the vertical (Y) axis, respectively. Then you'll have a number on a single line telling you how many records to read. Then you'll be given the data as three numbers: the first two represent the interval as a start (inclusive) and end (exclusive), the third number is the frequency of that variable. 

Example: 
140 190 1 8 
5
140 150 1
150 160 0 
160 170 7 
170 180 6 
180 190 2 


Output Description
------------------
Your program should emit an ASCII bar chart showing the frequencies of the buckets. Your program may use any character to represent the data point, I show an asterisk below. 

From the above example:
8
7           *
6           *   *
5           *   *
4           *   *
3           *   *
2           *   *   *
1   *       *   *   * 
 140 150 160 170 180 190

Challenge Input
---------------
0 50 1 10
5
0 10 1
10 20 3
20 30 6
30 40 4
40 50 2

"""
def print_ascii_chart(input):
    arrInput = input.split('\n')
    minX, maxX, minY, maxY = arrInput[0].split(' ')
    minX = int(minX)
    minY = int(minY)
    maxX = int(maxX)
    maxY = int(maxY)
    
    rowCount = maxY - minY + 1
    colCount = (((maxX - minX) // 10) * 2) + 2
    
    arrAxisLables = ['']
    arrFrequency = []
    result = []
    
    
    for data in arrInput[2:]:
        currData = data.split(' ')
        arrFrequency.append(int(currData[2]))
        
    for r in range(rowCount):
        result.append([])
        
        for c in range(colCount):
            if c == 0:
                result[-1].append(str(r + 1))
            else:
                if c % 2 == 0:
                    if arrFrequency[(c // 2) - 1] > 0:
                        result[-1].append('*')
                        arrFrequency[(c // 2) - 1] -= 1
                    else:
                        result[-1].append(' ')
                else:
                    result[-1].append(' ')
                    
    result = result[::-1]
    
    rangeStart = minX
    while rangeStart <= maxX:
        arrAxisLables.append(str(rangeStart)) 
        arrAxisLables.append(' ')
        rangeStart += 10
    
    for r in result:
        print("   ".join(r))
        
    print("   ".join(arrAxisLables))
                
    


def main(): 
    input = '0 50 1 10\n5\n0 10 1\n10 20 3\n20 30 6\n30 40 4\n40 50 2'
    print_ascii_chart(input)

main()