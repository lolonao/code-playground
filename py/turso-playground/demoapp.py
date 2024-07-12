from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select


TURSO_DATABASE_URL = "libsql://demo1-lolonaoo.turso.io"
TURSO_AUTH_TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA3OTQyMzUsImlkIjoiNmI1OGQ4NTUtYjVmYi00NjVlLTkzZjEtYTU1OWFjNTY1NDA4In0.CAmhbZas0Jd2N95H4sQvsgXN1ko-JS7sC-L80oMNVeQijLFe6hQfL12XEiwM-qtP0a7EIYb344cwTwJ7ni3vDw"

sqlite_url = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

class HeroCreate(SQLModel):
    name: str
    secret_name: str
    age: int | None = None

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        db_hero = Hero.model_validate(hero)
        session.add(db_hero)
        session.commit()
        session.refresh(db_hero)

def read_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes


def main():
    pass


if __name__ == "__main__":
    print("hogehoge")

