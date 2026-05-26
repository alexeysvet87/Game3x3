available = [['[1]','[2]','[3]'],['[4]','[5]','[6]'],['[7]','[8]','[9]']]
game_field = [['.']*3,['.']*3,['.']*3]

# Вывод поля на экран
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

# Проверка поля на победу игрока
def Check_Win(table):
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != '.':
            if table[i][0] == 'x': return 1
            else: return 2
        if table[0][i] == table[1][i] == table[2][i] != '.':
            if table[0][i] == 'x': return 1
            else: return 2
        if table[0][0] == table[1][1] == table[2][2] != '.':
            if table[0][i] == 'x': return 1
            else: return 2
        if table[0][2] == table[1][1] == table[2][0] != '.':
            if table[0][i] == 'x': return 1
            else: return 2
    return 0

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
    check = Check_Win(game_field)
    if check == 1:
        print('\nИгрок 2 победил!')
        game_over = True
    elif check == 2:
        print('\nИгрок 1 победил!')
        game_over = True
    elif turn == 9:
        print('\nНичья!')
        game_over = True

# Конец игры
print('\nИгра окончена!')