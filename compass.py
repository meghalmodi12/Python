"""
Design a game

Players take turns moving from island to island

Vehicle
- car
- bike

Islands are connected
- wooden bridge (bikes only)
- metal bridge (car and bike)

helicopter
helicopter route

bike 1 move
car 2 moves
heli 3 moves
"""

1 - [(2, 'wood'), (3, 'metal')]

class Node:
    def __init__(self, val, cType):
        self.val = val
        self.connectionType = cType
        self.playerAtNode = [1, 2]
        self.next = None

class Islands:
    def __init__(self, numOfIsland):
        self.arrIsland = []
        
        for i in range(len(numOfIsland)):
            if i ==
        

class Game:
    def __init__(self, totalPlayers):
        self.totalPlayers = totalPlayers
        self.currentPlayer = 1
        self.island = Islands(4)
        self.isGameFinished = False
        self.players = {
            1: {
                'currentIsland': 0,
                'vehicleType': 'car',
                'isPlaying': True,
            },  
            2: {
                'currentIsland': 0,
                'vehicleType': 'bike',
                'isPlaying': True,
            }, 
            3: {
                'currentIsland': 0,
                'vehicleType': 'car',
                'isPlaying': True,
            }, 
            4: {
                'currentIsland': 0,
                'vehicleType': 'bike',
                'isPlaying': True,
            }, 
        }
        
    def takeTurn(self, currentPlayer):
        movesLeft = 3
        currPlayerAt = self.players[currentPlayer].currentIsland
        head = self.island[currPlayerAt]
        
        if head is None:
            return
        
        while head is not None and movesLeft > 0:
            if head.connectionType == 'helicopter' and self.players[currentPlayer].vehicleType == 'helicopter':
                self.players[currentPlayer].currentIsland = head.next.val
                movesLeft -= 1
                
            elif head.connectionType == 'wood' and self.players[currentPlayer].vehicleType == 'car':
                head = head.next
            else:
                if self.players[currentPlayer].vehicleType != 'helicopter':
                    self.players[currentPlayer].currentIsland = head.next.val
                    movesLeft -= 1
                    
        if movesLeft > 0:
            return 
        
    def isGameOver(self):
        return True
        
    def playGame(self):
        
        while not self.isGameOver():
            if count > self.totalPlayers:
                count = 1
            self.takeTurn(count)
            
        return 'Winner ' + str(count)