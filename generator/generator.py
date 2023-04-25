import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
fake_en = Faker('EN')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(10000, 100000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
    )


def generated_file():
    path = rf'C:\Users\123\PycharmProjects\automation_qa\filetest{random.randint(0, 999)}.txt'
    file = open(path, "w+")
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generated_subject():
    yield Person(
        subjects=["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce",
                  "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    )


def generated_color():
    yield Color(
        color_name=["Aqua", "Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo"]
    )


def generated_date():
    yield Date(
        year=fake_en.year(),
        month=fake_en.month_name(),
        day=fake_en.day_of_month(),
        time="12:00",
    )
