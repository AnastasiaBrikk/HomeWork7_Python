# запуск программы начинается с этого:
def input_or_show():
    return int(input('Введите 1 чтобы добавить данные или 2 чтобы вывести данные: '))

# если добавить (создаём список который будем отправлять в модели для обработки и сохранения в текстовых файлах)
def get_data():
    data = []
    last_name = str(input('Фамилия: '))
    data.append(last_name)
    name = str(input('Имя: '))
    data.append(name)
    number = input('Номер: ')
    data.append(number)
    discrip = str(input('Описание: '))
    data.append(discrip)
    return data

# если вывести (выводит данные из текстового файла2 через модели)
def show_data():
    with open('txt2.txt', 'r') as file2:
        print(*file2)

if __name__ == '__main__':
    print(get_data())