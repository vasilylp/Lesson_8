def input_num():
    ask = int(input("1 - Добавить пользователя\n2 - Найти пользователя\n3 - Изменить данные справочника\n4 - Удалить данные из справочника\n5 - Выйти\n" ))
    return ask

def input_info():
    fio = input("Введи ФИО человека (Имя Отчество Фамилия) - ")
    birth = input("Введи дату рождения человека (дд.мм.гг) - ")
    tele = input("Введи телефон человека (ххх-хх-хх) - ")
    info = f"{fio}, {birth}, {tele}\n"
    return info

def input_char():
    char = input("Введите характеристику поиска -")
    return char
def input_chain():
    chain = input("Введите характеристику изменения -")
    return chain

def input_new():
    print("Введите новые данные пользователя :")
    list_2 = []
    list_2 = input_info()
    return list_2

def input_quest():
    quest = int(input("Данные какого из пользователей вы хотите изменить, введите номер -"))
    return quest

def input_delete():
    delete = input("Введите характеристику  пользователя для удаления из справочника -")
    return delete

def input_quest_del():
    quest_del = int(input("Данные какого из пользователей вы хотите удалить, введите номер -"))
    return quest_del