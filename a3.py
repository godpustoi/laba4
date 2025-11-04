import sys
s = input("Введите строку: ")
length = len(s)
if length<=5:
    print("Строки должна быть не меньше 5")
    sys.exit()
if not all(ch in "01" for ch in s):
    print("В строке не только 0 и 1")
    sys.exit()

print("Общее количество пакетов: ", length )

loss = s.count('0')
print("Количество потерянных пакетов: ", loss )

max_zeros = 0
current_zeros = 0
for ch in s:
    if ch == '0':
        current_zeros += 1
        if current_zeros > max_zeros:
            max_zeros = current_zeros
    else:
        current_zeros = 0
print("Длина самой длинной последовательности потерянных пакетов: ", max_zeros)

per_loss = (loss / length) * 100
print(f"Процент потерь: {per_loss:.2f}")


if per_loss <= 1:
    print("Качество связи: отличное")
elif per_loss <= 5:
    print("Качество связи: хорошее")
elif per_loss <= 10:
    print("Качество связи: удовлетворительное")
elif per_loss <= 20:
    print("Качество связи: плохое")
elif per_loss > 20:
    print("Качество связи: критическое состояние сети")