available = [['[1]','[2]','[3]'],['[4]','[5]','[6]'],['[7]','[8]','[9]']]
game_field = [['.']*3,['.']*3,['.']*3]

# Функция вывода поля на экран
def print_field():
    print(' ' * 12 + 'Выбор хода:')
    for i in range(3):
        print(*game_field[i] + [' '] * 3 + available[i])

# Начало игры
print('Игра началась!\n')
print_field()

game_over = False
turn = 0

while not game_over:
    print(f'Ход игрока {turn%2+1}:')
    #перевод ввода пользователя в индекс ячейки

    #размещение хода игрока в ячейку

    print_field()

    #проверка поля на победу игрока
    game_over = True

# Конец игры
print('\nИгра окончена!')