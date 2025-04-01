import pathlib

import sqlalchemy as sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    alias = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id!r}"
            f", alias={self.alias!r}"
            f", fullname={self.fullname!r}"
            f")"
        )


def main():
    db_path = pathlib.Path(__file__).with_name("users.db")
    db_path.unlink(missing_ok=True)

    engine = sqlalchemy.create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    session.add_all(
        [
            User(alias="kc", fullname="Karen Carpenters", password="t0p0fWorld"),
            User(alias="rc", fullname="Richard Carpenters", password="planet8"),
            User(alias="jw", fullname="John Wayne", password="beowuff2"),
        ]
    )
    session.commit()

    for user in session.query(User):
        print(user)


if __name__ == "__main__":
    main()
