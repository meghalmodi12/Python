import xlrd
import time
import datetime
from operator import itemgetter

fileLocation = ("C:/Study/Python/robinhood/robinhood-2019.xlsx")

workBookIndex = 1
headerRowIndex = 3

workBook = xlrd.open_workbook(fileLocation) 
sheetToProcess = workBook.sheet_by_index(workBookIndex) 

# Append column names
arrColumnsNames = []
for col in sheetToProcess.row_values(headerRowIndex):
    if len(col) > 0:
        arrColumnsNames.append(col)
    else:
        arrColumnsNames.append(None)

# Add values to symbol set
symbolSet = set()
for symbol in sheetToProcess.col_values(0):
    if len(symbol) > 0:
        symbolSet.add(symbol)

# Process stock buy
symbolBuyDict = {}
symbolSellDict = {}
for row in range(headerRowIndex + 1, sheetToProcess.nrows):
    symbol = sheetToProcess.cell_value(row,0)
    if symbol in symbolSet:
        activityType = sheetToProcess.cell_value(row,2)

        if activityType.lower() == 'buy':
            if symbol not in symbolBuyDict:
                symbolBuyDict[symbol] = []

            dateCell = sheetToProcess.cell_value(row,1)
            dateOfTrade = datetime.datetime(*xlrd.xldate_as_tuple(dateCell, workBook.datemode))
            timeStampOfTrade = datetime.datetime.timestamp(dateOfTrade)

            currentRowData = {
                'timeOfTrade': timeStampOfTrade,
                'dateOfTrade': dateCell,
                'pricePerStock': sheetToProcess.cell_value(row,3),
                'lotSize': int(sheetToProcess.cell_value(row,4)),
                'amountPaid': sheetToProcess.cell_value(row,7)
            }

            symbolBuyDict[symbol].append(currentRowData)

        if activityType.lower() == 'sold':
            if symbol not in symbolSellDict:
                symbolSellDict[symbol] = []

            dateCell = sheetToProcess.cell_value(row,1)
            dateOfTrade = datetime.datetime(*xlrd.xldate_as_tuple(dateCell, workBook.datemode))
            timeStampOfTrade = datetime.datetime.timestamp(dateOfTrade)

            currentRowData = {
                'timeOfTrade': timeStampOfTrade,
                'dateOfTrade': dateCell,
                'pricePerStock': sheetToProcess.cell_value(row,3),
                'numOfStocksSold': int(abs(sheetToProcess.cell_value(row,4))),
                'amountGained': sheetToProcess.cell_value(row,5)
            }
            
            symbolSellDict[symbol].append(currentRowData)


# For each symbol sort the list based on timestamp
for symbol, info in symbolBuyDict.items():
    info = info.sort(key=itemgetter('timeOfTrade'))

for symbol, info in symbolSellDict.items():
    info = info.sort(key=itemgetter('timeOfTrade'))

# Start calculating profit / loss for each symbol
symbolProfitDict = {}
for symbol, info in symbolSellDict.items():
    if symbol not in symbolProfitDict:
        symbolProfitDict[symbol] = 0

    sellQueue = info
    buyQueue = symbolBuyDict[symbol]

    while sellQueue:
        trasaction = sellQueue.pop(0)

        while trasaction['numOfStocksSold'] != 0:
            trasaction['numOfStocksSold'] -= 1
            symbolProfitDict[symbol] += (trasaction['pricePerStock'] - buyQueue[0]['pricePerStock'])
            if buyQueue[0]['lotSize'] == 1:
                buyQueue.pop(0)
            else:
                buyQueue[0]['lotSize'] -= 1

# Print final profit / loss
result = 0
for val in symbolProfitDict.values():
    result += val

# print(symbolProfitDict)
# print(symbolBuyDict)
print(result)