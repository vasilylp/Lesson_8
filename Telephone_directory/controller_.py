from database_ import *
from view_ import *

def main():
    while True:
        num = input_num()
        if num == 1:
            info = input_info()
            write_info(info)
        elif num == 2:
            char = input_char()
            find_info(char)
        elif num == 3:
            chain = input_chain()
            old_info = find_info_chain(chain)
            if len(old_info) == 1:
                new_info = input_new()
                old_info_chain = old_info[0]
            elif len(old_info) > 1:
                quest = input_quest()
                old_info_chain = old_info[quest - 1]
                new_info = input_new()
            new_chain_info(old_info_chain, new_info)
            print(f"Информация {old_info_chain}\nизменена на :{new_info}")
        elif num == 4:
            delete = input_delete()
            del_info = find_info_chain(delete)
            if len(del_info) == 1:
                del_info = del_info[0]
            elif len(del_info) > 1:
                quest = input_quest_del()
                del_info = del_info[quest - 1]
            f_del_info(del_info)
            print(f"Информация {del_info}удалена !")
        elif num == 5:
            print("Выход из программы...........")
            break

main()