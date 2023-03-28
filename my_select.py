import sys

from database.db import session
from database.models import Teacher, Student, Grade, Discipline, Group
from sqlalchemy import and_, func, desc

help_message = """
Виберіть який запит ви хочете виконати?
0 -- Вихід
1 -- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2 -- Знайти студента із найвищим середнім балом з певного предмета.
3 -- Знайти середній бал у групах з певного предмета.
4 -- Знайти середній бал на потоці (по всій таблиці оцінок).
5 -- Знайти які курси читає певний викладач.
6 -- Знайти список студентів у певній групі.
7 -- Знайти оцінки студентів у окремій групі з певного предмета.
8 -- Знайти середній бал, який ставить певний викладач зі своїх предметів.
9 -- Знайти список курсів, які відвідує певний студент.
10 -- Список курсів, які певному студенту читає певний викладач.
"""


def get_query_1():
    students = session.query(Student.first_name, Student.last_name,
                             func.round(func.avg(Grade.grade), 2).label('avg_rate')).select_from(
        Grade).join(Student).filter(Grade.student_id == Student.id).group_by(Student.id).order_by(
        desc('avg_rate')).limit(5)

    for student in students:
        print(f'{student[0]} {student[1]} - {student[2]}')


def get_query_2():
    students = session.query(Student.first_name, Student.last_name,
                             func.round(func.avg(Grade.grade), 2).label('avg_rate'), Discipline.name).select_from(
        Grade).join(Student).join(Discipline).filter(and_(Grade.student_id == Student.id, Grade.discipline_id == 1)).\
        group_by(Student.id, Discipline.id).order_by(desc('avg_rate')).limit(1)

    for student in students:
        print(f'{student[3]} * {student[1]} {student[0]} - {student[2]}')


def get_query_3():
    grades = session.query(Group.name, Discipline.name, func.round(func.avg(Grade.grade), 2).label('avg_rate')).\
        select_from(Grade).join(Discipline).join(Student).join(Group).group_by(Discipline.id, Group.id).\
        order_by(desc('avg_rate')).all()

    for grade in grades:
        print(f'{grade[0]} | {grade[1]} - {grade[2]}')


def get_query_4():
    grades = session.query(func.round(func.avg(Grade.grade), 2).label(
        'avg_rate')).select_from(Grade).all()

    for grade in grades:
        print(f'Avg. grade (from all students) - {grade[0]}')


def get_query_5():
    disciplines = session.query(Discipline.name, Teacher.first_name, Teacher.last_name).select_from(Discipline).join(Teacher).\
        filter(Teacher.id == 1).all()

    for discipline in disciplines:
        print(f'{discipline[1]} {discipline[2]} - {discipline[0]}')


def get_query_6():
    students = session.query((Student.first_name + ' ' + Student.last_name), Group.name).select_from(Student).\
        join(Group).filter(Group.id == 1).all()

    for student in students:
        print(f'{student[1]} - {student[0]}')


def get_query_7():
    grades = session.query((Student.first_name + ' ' + Student.last_name), Group.name, Grade.grade, Discipline.name).\
        select_from(Grade).join(Student).join(Group).join(
            Discipline).filter(and_(Group.id == 3, Discipline.id == 4)).all()

    for grade in grades:
        print(f'{grade[1]} - {grade[3]} - {grade[0]} - {grade[2]}')


def get_query_8():
    grades = session.query(Teacher.first_name + ' ' + Teacher.last_name, func.round(func.avg(Grade.grade), 2).
                           label('avg_rate'), Discipline.name).select_from(Grade).join(Discipline).join(Teacher).\
        filter(Teacher.id == 1).group_by(
            Teacher.id, Discipline.id).order_by(desc('avg_rate')).all()

    for grade in grades:
        print(f'{grade[0]} - {grade[2]} - {grade[1]}')


def get_query_9():
    subjects = session.query((Student.first_name + ' ' + Student.last_name), Discipline.name).select_from(Grade).\
        join(Student).join(Discipline).filter(Student.id ==
                                           11).group_by(Student.id, Discipline.id).all()

    for subject in subjects:
        print(f'{subject[0]} - {subject[1]}')


def get_query_10():
    subjects = session.query((Student.first_name + ' ' + Student.last_name),
                             Teacher.first_name + ' ' + Teacher.last_name, Discipline.name).select_from(Grade).\
        join(Student).join(Discipline).join(Teacher).filter(and_(Student.id == 1, Teacher.id == 1)).\
        group_by(Student.id, Teacher.id, Discipline.id).all()

    for subject in subjects:
        print(f'{subject[0]} - {subject[1]} - {subject[2]}')


def get_data():
    queries = {
        1: get_query_1,
        2: get_query_2,
        3: get_query_3,
        4: get_query_4,
        5: get_query_5,
        6: get_query_6,
        7: get_query_7,
        8: get_query_8,
        9: get_query_9,
        10: get_query_10,
    }

    print(help_message)
    while True:
        task = int(input("Виберіть номер запиту: "))
        if task == 0:
            sys.exit()

        try:
            queries[task]()
        except KeyError as e:
            print('Запит не знайдений: ', e)


if __name__ == "__main__":
    get_data()
