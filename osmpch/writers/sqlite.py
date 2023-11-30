from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from osmpch.models.changeset import Base, Changeset

class SQLiteWriter:
    def __init__(self):
        self.db_path = "sqlite:///changesets.db"
        self.engine = create_engine(self.db_path)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def write_changesets(self, changesets: list[Changeset]):
        session = self.Session()
        try:
            session.add_all(changesets)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
