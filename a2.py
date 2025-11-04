rows = int(input("Введите rows: "))
columns = int(input("Введите columns: "))
ch = input("Введите ch: ")

def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end=" ")
        print()

def draw_triangle(rows, ch):
    for i in range(rows +1):
        for j in range(i):
            print(ch, end=" ")
        print()


def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1  or j == 0 or j == columns - 1:
                print(ch, end=" ")
            else:
                print(" ", end=" ")
        print()

draw_rectangle(rows, columns, ch)
draw_triangle(rows, ch)
draw_frame(rows, columns, ch)