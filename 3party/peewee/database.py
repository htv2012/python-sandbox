import mimetypes

from sqlalchemy import Binary
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///artifacts.sqlite', echo=True)
Base = declarative_base()


class Artifact(Base):
    __tablename__ = 'artifact'
    token = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(String)
    binary = Column(Binary)

    def __repr__(self):
        return '{}(token={!r}, title={!r})'.format(
            self.__class__.__name__,
            self.token,
            self.title,
        )


def main():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    files = 'requirements.txt herman.py people.db'.split()
    for filename in files:
        with open(filename, 'rb') as f:
            contents = f.read()
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type is None:
            is_text = False
        else:
            is_text = 'text' in mime_type
        artifact = Artifact(title=filename,
                            text=contents if is_text else None,
                            binary=contents if not is_text else None,
                            )
        session.add(artifact)

    session.commit()


if __name__ == '__main__':
    main()
    # Base.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()
