from seeds.teachers import create_teachers
from seeds.disciplines import create_disciplines
from seeds.grades import create_grades
from seeds.groups import create_groups
from seeds.students import create_students


if __name__ == '__main__':
    create_teachers()
    create_groups()
    create_students()
    create_disciplines()
    create_grades()
