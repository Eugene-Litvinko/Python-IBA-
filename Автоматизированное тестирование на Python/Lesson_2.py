# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep


def chek_Availability_porridge():
    porridge = input('Укажите номер каши, которую хотим приготовть?\n1.Гречка\n2.Рис\n3.Овсянка\n4.Другая каша\n5.Каши нету\n')
    return int(porridge)

def prepare_porridge(weight):
    v_castrly = 3000
    print(f'Необходимо взять кастрюлю и налить воды в пропорции 1:3, т.е. {weight*3} мл воды')
    if weight + weight*3 > v_castrly:
        print('Необходимо заменить кастрю')
    print('Спасибо! Теперь поставим кастрюлю на плиту и ждем 10 мин')
    for j in range(1, 11):
        print(f'Прошло {j} минут...')
        sleep(1)

def water_and_porridge():
    print('Сейчас необходимо переодически помешивать кашу, чтобы она не подгорела.\nДелаем это пока не выкипит вся вода!\nОжидание:')
    for j in range(1,11):
        print('.', end='')
        sleep(2)
    print('Воды не осталось!')
    return 0


def main():
    i = True
    while i:
        porridge = chek_Availability_porridge()
        porridges = {
            1: 'Гречка',
            2: 'Рис',
            3: 'Овсянка',
            4: 'Другая каша',
            5: 'Каши нету',
        }
        try:
            if porridge != 5:
                print(f'Здорово! У тебя есть {porridges[porridge]}!')
                weight = input('Укажите количество каши в граммах:\n')
                weight = int(weight) #предусмотреть нужно ввод валидных данных
                prepare_porridge(weight)
                print('Вода закипела!!!\nНебходимо засыпать кашу в кастрюлю с водой, которая стоит на плите!')
                water_and_porridge()
            elif porridge == 5:
                print(f'Вам необходимо купить одну из каш и вернуться к нам')
                i = False
        except:
            print('Ввели неправильный номер. Доступные цифры для ввода: 1,2,3,4,5.\nЗапустите программу снова')
            i = False

        i = False
if __name__ == '__main__':
    print('Вас приветствует алгоритм под названием "Готовка каши"')
    main()

