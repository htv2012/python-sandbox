import datetime
import peewee
from peewee import SqliteDatabase, Model, CharField, DateField, BooleanField

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_table(Person, safe=True)

    person1 = Person(name='Bob', birthday=datetime.date(1960, 8, 25), is_relative=True)
    person1.save()

