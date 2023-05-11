# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

# Функция подключения к БД
def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

# Функция отключения от БД и закрытия
def close_connection(connection):
    if connection:
        connection.close()

# В базе данных teaTcher создаю таблицу Students
# connection = get_connection()
# cursor = connection.cursor()
# sqlquery = """
# CREATE TABLE Students (
# Student_Id INTEGER, 
# Student_Name TEXT, 
# School_Id INTEGER NOT NULL PRIMARY KEY
# ); """
# cursor.execute(sqlquery)
# connection.commit()
# close_connection(connection)

# Наполняю таблицу следующими данными:
# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# connection = get_connection()
# cursor = connection.cursor()
# sqlquery = """ 
# INSERT INTO Students (Student_Id, Student_Name, School_Id) 
# VALUES 
# ('201', 'Иван', 1), 
# ('202', 'Петр', 2), 
# ('203', 'Анастасия', 3), 
# ('204', 'Игорь', 4);
# """
# cursor.execute(sqlquery)
# connection.commit()
# close_connection(connection)

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.
# Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

# Функция формирования запроса и вывода данных

def get_students_info(_studen_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """ SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name
                           FROM Students
                           JOIN School ON Students.School_Id = School.School_Id
                           WHERE Student_Id = ? """
        cursor.execute(select_query, (_studen_id,))
        records = cursor.fetchall()
        print('Данные по студенту с Id: ', _studen_id)
        for row in records:
            print('Id студента: ', row[0])
            print('Имя студента: ', row[1])
            print('Id школы: ', row[2])
            print('Название школы: ', row[3], "\n")
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка в получении данных: ", error)

id = int(input('Введи Id студента: '))
get_students_info(id)




