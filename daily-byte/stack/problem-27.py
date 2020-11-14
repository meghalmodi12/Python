"""
This question is asked by Microsoft. Design a class, MovingAverage, which contains a method, next that is responsible for returning the moving average from a stream of integers.
Note: a moving average is the average of a subset of data at a given point in time.

Ex: Given the following series of events...

// i.e. the moving average has a capacity of 3.
MovingAverage movingAverage = new MovingAverage(3);
m.next(3) returns 3 because (3 / 1) = 3
m.next(5) returns 4 because (3 + 5) / 2 = 4 
m.next(7) = returns 5 because (3 + 5 + 7) / 3 = 5
m.next(6) = returns 6 because (5 + 7 + 6) / 3 = 6
"""

class MovingAverage:
    def __init__(self, size):
        # do intialization if necessary
        self.queue = []
        self.size = size
        self.currentSum = 0
    
    def next(self, val):
        # write your code here
        if len(self.queue) == self.size:
            self.currentSum -= self.queue[0]
            self.queue.pop(0)
            
        self.queue.append(val)
        self.currentSum += self.queue[-1]
        
        return self.currentSum / len(self.queue)