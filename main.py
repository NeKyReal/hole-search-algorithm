from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo


# программа
def main():
    # тут будут храниться кнопки
    table = []

    # кастомизация рабочего поля
    size = {
        "length": 10, # длина поля
        "height": 10, # высота поля
        "block": 30 # размер одной ячейки
    }

    custom = Tk()
    custom.geometry(f"{size['block']*9}x{size['block']*5}")
    custom.resizable(False, False)
    custom.title("Создание поля")

    # запись данных о размере поля
    def get_state():
        if not length_spinbox.get() == "":
            size["length"] = int(length_spinbox.get())
        if not height_spinbox.get() == "":
            size["height"] = int(height_spinbox.get())

    length_label = ttk.Label(text="Введите длину поля\n(по умолчанию 10)")
    length_label.place(x=size['block'], y=size['block']/2, height=size['block'])

    length_spinbox = ttk.Spinbox(custom, from_=2, to=60, state="readonly", command=get_state)
    length_spinbox.place(x=size['block']*6, y=size['block']/2, width=size['block']*2, height=size['block'])

    height_label = ttk.Label(text="Введите высоту поля\n(по умолчанию 10)")
    height_label.place(x=size['block'], y=size['block']*2, height=size['block'])

    height_spinbox = ttk.Spinbox(custom, from_=2, to=30, state="readonly", command=get_state)
    height_spinbox.place(x=size['block']*6, y=size['block']*2, width=size['block']*2, height=size['block'])

    next_button = ttk.Button(custom, text="Далее", command=custom.destroy)
    next_button.place(x=size['block'], y=size['block']*4-size['block']/2, width=size['block']*2, height=size['block'])

    custom.mainloop()

    # создание рабочего поля
    matrix = []
    for i in range(size['height']):
        matrix.append([0]*size['length'])

    # обработка ячеек
    def click(x, y):
        if table[size['height']*(x-1)+y-1]['text'] == "■":
            table[size['height'] * (x - 1) + y - 1]['text'] = ""
            matrix[y - 1][x - 1] = 0
        else:
            matrix[y-1][x-1] = 1
            table[size['height']*(x-1)+y-1]['text'] = "■"

    # запуск алгоритма
    def run(matrix):
        i = 0
        j = 0

        # добавляем края полю, чтобы можно было добавлять элементы по краям
        for line in matrix:
            line.append(0)
            line.insert(0, 0)
        matrix = [[0]*len(matrix[1])] + matrix + [[0]*len(matrix[1])]

        # сам алгоритм
        for y in range(len(matrix) - 1):
            for x in range(len(matrix[0]) - 1):
                if matrix[y][x] + matrix[y][x + 1] + matrix[y + 1][x] + matrix[y + 1][x + 1] == 1:
                    i += 1
                if matrix[y][x] + matrix[y][x + 1] + matrix[y + 1][x] + matrix[y + 1][x + 1] == 3:
                    j += 1

        # вычисление количества отверстий
        showinfo(title="Вывод", message="Формула: N = (i - j) / 4",
                 detail=f"Решение: N = ({i} - {j}) / 4 = {int((i - j) / 4)}")

        # возвращаем матрицу в исходное состояние
        for line in matrix:
            line.pop(0)
            line.pop(len(line)-1)
        matrix.pop(0)
        matrix.pop(len(matrix)-1)

    root = Tk()
    root.title("By Kirill Ruchin")
    root.geometry(f"{(size['length']+2)*size['block']}x{(size['height']+4)*size['block']}")
    root.resizable(False, False)

    # циклы отрисовывают поле
    for x in range(1, size['length']+1):
        for y in range(1, size['height']+1):
            # здесь в качестве обработчика используется лямбда, которая передает свои параметры в метод для
            # обработки кнопки. почему именно так? иначе команда выполняется исключительно при отрисовке кнопки
            button = ttk.Button(root, text="", command=lambda x=x, y=y: click(x, y))
            button.place(x=x*size['block'], y=y*size['block'], width=size['block'], height=size['block'])
            # добавляю созданные кнопки в список
            table.append(button)

    finish_button = ttk.Button(root, text="Начать", command=lambda matrix=matrix: run(matrix))
    finish_button.place(x=size['block'], y=(size['height']+2)*size['block'], width=2*size['block'], height=size['block'])

    root.mainloop()


# точка входа в программу
if __name__ == '__main__':
    main()
