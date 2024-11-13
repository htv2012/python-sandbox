import sqlalchemy
from sqlalchemy import Column
from sqlalchemy import LargeBinary
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


engine = sqlalchemy.create_engine('sqlite:///artifact.sqlite')
Base = declarative_base()


class Artifact(Base):
    __tablename__ = "artifact"
    token = Column(String, primary_key=True)
    title = Column(String)
    mime_type = Column(String)
    text_contents = Column(String)
    binary_contents = Column(LargeBinary)


Base.metadata.bind = engine
Base.metadata.create_all()


