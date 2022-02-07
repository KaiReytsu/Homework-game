#Написать игру «Пятнашки».

import tkinter
from random import shuffle

BOARD_SIZE = 4
SQUARE_SIZE = 80
EMPTY_SQUARE = BOARD_SIZE ** 2

root = tkinter.Tk()
root.title('Пятнашки')

gui_board = tkinter.Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
           height=BOARD_SIZE * SQUARE_SIZE, bg='#787474')
gui_board.pack()


def get_inv_count():
    '''Функция считающая количество перемещений'''
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(EMPTY_SQUARE)
    for item in range(len(inversion_board)):
        first_item = inversion_board[item]
        for elem in range(item+1, len(inversion_board)):
            second_item = inversion_board[elem]
            if first_item > second_item:
                inversions += 1
    return inversions

def is_solvable():
    '''Функция определяющая имеет ли головоломка рещение'''
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0

def get_empty_neighbor(index):
    '''Функция поиска пустой клетки'''
    empty_index = board.index(EMPTY_SQUARE)
    abs_value = abs(empty_index - index)
    if abs_value == BOARD_SIZE:
        return empty_index
    elif abs_value == 1:
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    return index

def draw_board():
    '''Функция отрисовки квадратов'''
    gui_board.delete('all')
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            index = str(board[BOARD_SIZE * i + j])
            if index != str(EMPTY_SQUARE):
                gui_board.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#5097ab',
                                   outline='#000')
                gui_board.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2,
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font='Arial {} italic'.format(int(SQUARE_SIZE / 4)),
                              fill='#000')

def show_victory_plate():
    '''Функция отрисовки "победного" квадрата'''
    gui_board.create_rectangle(SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
                       BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
                       fill='#ba1133',
                       outline='#000')
    gui_board.create_text(SQUARE_SIZE * BOARD_SIZE / 2, SQUARE_SIZE * BOARD_SIZE / 1.9,
                  text='ПОБЕДА!', font='Helvetica {} bold'.format(int(10 * BOARD_SIZE)), fill='#000')

def click(event):
    '''Функция события по клику мышку'''
    x, y = event.x, event.y
    # Конвертируем координаты из пикселей в клеточки
    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE
    board_index = x + (y * BOARD_SIZE)
    empty_index = get_empty_neighbor(board_index)
    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    draw_board()
    if board == correct_board:
        show_victory_plate()


gui_board.bind('<Button-1>', click)
gui_board.pack()


board = list(range(1, EMPTY_SQUARE + 1))
correct_board = board[:]
#Создаем случайное распределение чисел
shuffle(board)

while not is_solvable():
    shuffle(board)

draw_board()
root.mainloop()