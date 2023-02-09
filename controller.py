import models
import view

def start():
    comand = view.input_or_show() #определяем добавление или вывод данных (1 - добавление, 2 - вывод в консоль)

    if comand == 1:
        lst = view.get_data() # собираем у пользователя список данных для добавления в файлы
        models.add_data(lst) # добавляем данные в файлы 

    elif comand == 2:
        view.show_data()