import sys
import re

string = input("Введите строку: ")

def isValidNumber(string):
    return string.isdigit() and len(string) in [13, 15, 16]

def getCheckSum(string):
    checkSum = 0
    for i in range(len(string) - 2, -1, -2):
        val = int(string[i]) * 2
        checkSum += val - 9 if val > 9 else val
    for i in range(len(string) - 1, -1, -2):
        checkSum += int(string[i])
    return checkSum

def getCardType(string):
    if (len(string) == 13 or len(string) == 16) and string.startswith("4"):
        return "Visa"
    if len(string) == 15 and (string.startswith("34") or string.startswith("37")):
        return "American Express"
    if len(string) == 16 and re.match(r'5[1-5]', string[:2]):
        return "Master Card"
    return "Invalid"

if not isValidNumber(string):
    print("Неверный формат номера")
    sys.exit()

if getCheckSum(string) % 10 != 0:
    print("Неверная контрольная сумма")
    sys.exit()

print("Тип карты: ",getCardType(string))