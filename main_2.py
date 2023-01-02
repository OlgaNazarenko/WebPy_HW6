import sqlite3

from services.create_table import create_table
from services.fill_table import fill_table
from services.select_tables import select_tables


def assistance() -> str:
    list_of_cmd: str = """Command format:
    help - this help
    1 - tp create tables
    2 - to complete or fill tables
    3 - to select tables. Choose any of the below query-requests: 
        
        0) Інформація про студентів, викладачів та предмети
        1) Інформація про студентів, викладачів та предмети
        1) 5 студентів з найбільшим середнім балом з усіх предметів
        2) Студенти з найвищим середнім балом з певного предмету
        3) Середній бал у групах з певного предмету
        4) Середній бал на потоці
        5) Курси певного викладача
        6) Список студентів певної групи
        7) Оцінки студентів у окремій группі з певного предмету
        8) Середній бал, який ставив певний викладач зі своїх предметів
        9) Список курсів, які відвідував студент
        10) Список курсів, які певний викладач читає певному студенту
   
    exit - exit the program"""
    print(list_of_cmd)
    return list_of_cmd


def query_request():
    COMMANDS: dict = {"query_1.sql": 1,
                      "query_2.sql": 2,
                      "query_3.sql": 3,
                      "query_5.sql": 5,
                      "query_4.sql": 4,
                      "query_6.sql": 6,
                      "query_7.sql": 7,
                      "query_8.sql": 8,
                      "query_9.sql": 9,
                      "query_10.sql": 10
                      }
    nmb = input('Please enter the query number:')
    for key, value in COMMANDS.items():
        if num.lower() == value:
            print(f'{select_tables(num)=}')
        return value


COMMANDS: dict = {create_table: '1', fill_table: '2', select_tables: '3', assistance: 'help'}


def command_parser(user_command: str):
    for key, value in COMMANDS.items():

        if user_command.lower() == value:
            return key
    else:
        return 'Unknown command! Enter again!\n'


if __name__ == '__main__':
    assistance()
    while True:
        user_command = input('Enter command >>> ')
        print(f'{user_command=}')

        if user_command == 'help':
            assistance()
        elif user_command == 3:
            print(f'{query_request()}')
        elif user_command == 'exit':
            print('Good bye!')
            break
        command = command_parser(user_command)
        command()
