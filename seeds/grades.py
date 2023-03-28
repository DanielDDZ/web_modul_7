from faker import Faker
import random
from datetime import datetime

from database.db import session
from database.models import Grade, Discipline, Student

fake = Faker('uk_UA')


def create_grades():
    disciplines = session.query(Discipline).all()
    students = session.query(Student).all()

    for _ in range(1, 200):
        grade = Grade(
            discipline_id=random.choice(disciplines).id,
            student_id=random.choice(students).id,
            grade=random.randint(4, 12),
            date_of=fake.date_between_dates(
                datetime(2022, 1, 1), datetime(2022, 12, 31))
        )
        session.add(grade)
    session.commit()


if __name__ == "__main__":
    create_grades()
