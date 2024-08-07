"""
"name","age"
"alice",20
"bob",21
"""

import csv
from pydantic import BaseModel
from enum import IntEnum

class Sex(IntEnum):
    MALE = 0
    FEMALE = 1

class Person(BaseModel):
    name: str
    age: int
    sex: Sex

def read_csv(csv_file_name: str) -> None:
    with open(csv_file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


def main():
    # read_csv("persons.csv")
    # data = {"name","age", "alice",20, "bob",21}

    # data = {"name": "alice", "age": "20"}
    # person = Person(**data)

    data = {"name": "alice", "age": "20", "sex": "1"}
    person = Person(**data)
    print(person.name, type(person.name))
    print(person.age, type(person.age))
    print(person.sex, type(person.sex))
 
if __name__ == '__main__':
    main()

