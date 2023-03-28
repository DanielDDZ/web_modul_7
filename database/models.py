from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="CASCADE"))

    groups = relationship("Group", backref="student")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    disciplines = relationship("Discipline", backref="teacher")


class Discipline(Base):
    __tablename__ = "disciplines"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE"))

    grades = relationship("Grade", backref="discipline")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE"))
    discipline_id = Column(Integer, ForeignKey(Discipline.id, ondelete="CASCADE"))
    grade = Column(Integer)
    date_of = Column(DateTime)

    students = relationship("Student", backref="grade")
