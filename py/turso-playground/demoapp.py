from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

DB_URL = "libsql://demo1-lolonaoo.turso.io"
TURSO_DATABASE_URL = DB_URL
TOKEN = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MjA3OTQyMzUsImlkIjoiNmI1OGQ4NTUtYjVmYi00NjVlLTkzZjEtYTU1OWFjNTY1NDA4In0.CAmhbZas0Jd2N95H4sQvsgXN1ko-JS7sC-L80oMNVeQijLFe6hQfL12XEiwM-qtP0a7EIYb344cwTwJ7ni3vDw"
TURSO_AUTH_TOKEN = TOKEN

sqlite_url = f"sqlite+{TURSO_DATABASE_URL}/?authToken={TURSO_AUTH_TOKEN}&secure=true"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

class HeroCreate(SQLModel):
    name: str
    secret_name: str
    age: int | None = None

# @app.on_event("startup")
# # async def startup_event():
# async def on_startup():
#     create_db_and_tables()

# @app.post("/heroes/")
# def create_hero(hero: HeroCreate):
#     with Session(engine) as session:
#         db_hero = Hero.model_validate(hero)
#         session.add(db_hero)
#         session.commit()
#         session.refresh(db_hero)
#         return db_hero

# @app.get("/heroes/")
# def read_heroes():
#     with Session(engine) as session:
#         heroes = session.exec(select(Hero)).all()
#         return heroes

