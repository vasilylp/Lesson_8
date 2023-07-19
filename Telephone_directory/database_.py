def write_info(info):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(info)


def find_info(char):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        count = 0
        for line in lst:
            if char in line:
                count += 1
                print(f"{count}. {line.strip()}")


def find_info_chain(chain):
    with open("data.txt", "r", encoding="utf-8") as file:
        lst = file.readlines()
        lst_1 = []
        count = 0
        for line in lst:
            if chain in line:
                count += 1
                print(f"{count}. {line.strip()}")
                lst_1.append(line)
        return lst_1


def new_chain_info(old_info_chain, new_info):
    with open('data.txt', 'r', encoding="utf-8") as file:
        old_data = file.read()
        new_data = old_data.replace(old_info_chain, new_info)
    with open('data.txt', 'w', encoding="utf-8") as file:
        file.write(new_data)


import re


def f_del_info(del_info):
    with open('data.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
    pattern = re.compile(re.escape(del_info))
    with open('data.txt', 'w', encoding="utf-8") as file:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)
