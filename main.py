import sqlite3
from services.select_tables import *
from services.create_table import *
from services.fill_table import *
from services.settings import DATABASE


def main():
    while True:
        number = input('Please, choose: ')
        print(f'{number=}')
        if number == 'exit':
            print('Good bye)')
            break
        if number == 'help':
            print(assistance())
        # if not command == int:
        #     return 'Send number of query!'
        query_request(number)


def assistance():
    menu = """Commands line:
    help - help
    exit - exit
    from 1 - 10 - choose any query-requests: 
        
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
    """
    print(menu)


def query_request(num):
    COMMANDS: dict = {"Інформація про студентів, викладачів та предмети": 0,
                      "query_1.sql": 1,
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

    for key, value in COMMANDS.items():
        if num.lower() == value:
            print(f'{num.lower() == value =}')
            print(f'{key=}')
            if num == 0:
                print(f'{create_table(conn, create_table_sql)=}')
            else:
                return select_tables(num)
        return value, key
    # num: int = int(num)
    # if num == 0:
    #     return create_table(DATABASE, *args), fill_table()
    # if num <= 10:
    #     return select_tables(num)


# COMMANDS: dict = {create_table: '1', fill_table: '2', select_tables: '3', assistance: 'help'}

#
# def command_parser(command: str) -> None:
#     for key, value in COMMANDS.items():
#         if command.lower() == value:
#             print(f'{command.lower() == value =}')
#             print(f'{key=}')
#             if command.lower() == 1:
#                 return services.create_table(conn, create_table_sql)
#             # if command.lower() == 2:
#
#     else:
#         print('Entered a wrong request. Enter again \n')


if __name__ == "__main__":
    print(f'{assistance()=}')
    # create_table(DATABASE)
    print(f'{fill_table()=}')
    main()
