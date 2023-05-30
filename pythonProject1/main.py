

import random
player_active, message = True, "Привет давай сыграем в игру?\nИгра заключается в том чтобы угадать цвет который выпадет\n" \
                               "Как тебя зовут?: "
current, name = 0, input(message)
print(f'Тогда начнем игру {name}!')
while player_active:
    randomings = random.randrange(0, 37)
    start = int(input('Введи число от 0 до 36: '))
    print(f'Бот вывел: {randomings}')

    if start == 0:
        if randomings == 0:
            current = current + 2
            print(f'{name.title()} ты угадал ЗЕЛЕНЫЙ цвет!\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
    elif (1 <= start <= 10) and (1 <= randomings <= 10):
        if (start % 2 == 0) and (randomings % 2 == 0):
            current = current + 1
            print(f'{name.title()} ты угадал КРАСНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
        else:
            current = current + 1
            print(f'{name.title()} ты угадал ЧЕРНЫЙ цвет цвет!\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
    elif (11 <= start <= 18) and (11 <= randomings <= 18):
        if (start % 2 == 0) and (randomings % 2 == 0):
            current = current + 1
            print(f'{name.title()} ты угадал ЧЕРНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
        else:
            current = current + 1
            print(f'{name.title()} ты угадал КРАСНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
    elif (19 <= start <= 28) and (19 <= randomings <= 28):
        if (start % 2 == 0) and (randomings % 2 == 0):
            current = current + 1
            print(f'{name.title()} ты угадал КРАСНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
        else:
            current = current + 1
            print(f'{name.title()} ты угадал ЧЕРНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
    elif (29 <= start <= 36) and (29 <= randomings <= 36):
        if (start % 2 == 0) and (randomings % 2 == 0):
            current = current + 1
            print(f'{name.title()} ты угадал ЧЕРНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
        else:
            current = current + 1
            print(f'{name.title()} ты угадал КРАСНЫЙ цвет !\nКол-во баллов: {current} из 5')
            if current == 5:
                print(f'{name.title()}, ты набрал {current} из 5\nТы победил!')
                player_active = False
            else:
                continue
    elif 0 > start > 36:
        print('ОШИБКА!')





















































































