from faker import Faker
import random

from database.db import session
from database.models import Discipline, Teacher

fake = Faker('uk_UA')


def create_disciplines():
    teachers = session.query(Teacher).all()
    for _ in range(1, 9):
        discipline = Discipline(
            name=fake.job(),
            teacher_id=random.choice(teachers).id
        )
        session.add(discipline)
    session.commit()


if __name__ == "__main__":
    create_disciplines()
