available = [['[1]','[2]','[3]'],['[4]','[5]','[6]'],['[7]','[8]','[9]']]
game_field = [['.']*3,['.']*3,['.']*3]

# Функция вывода поля на экран
def print_field():
    print(' ' * 12 + 'Выбор хода:')
    for i in range(3):
        print(*game_field[i] + [' '] * 3 + available[i])

#Обработка ввода пользователя
def choice():
    while True:
        try:
            num = int(input()) - 1
            if 0 <= num <= 8:
                return (num // 3, num % 3)
            print('Недопустимое значение! (1-9)')
        except ValueError:
            print('Введите целое число от 1 до 9!')


# Начало игры
print('Игра началась!\n')
print_field()

game_over = False
turn = 0

while not game_over:
    print(f'Ход игрока {turn%2+1}:')
    row, col = choice()  # перевод ввода игрока в индекс ячейки
    while available[row][col] == '[ ]':
        print("Место занято!")
        row, col = choice()

    #размещение хода игрока в ячейку
    if turn % 2 == 1:
        game_field[row][col] = 'o'
    else:
        game_field[row][col] = 'x'
    available[row][col] = '[ ]'
    turn += 1

    print_field()

    #проверка поля на победу игрока
    game_over = True

# Конец игры
print('\nИгра окончена!')