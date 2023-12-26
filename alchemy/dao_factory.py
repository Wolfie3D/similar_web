from sqlalchemy.orm import sessionmaker
from tables import SimilarWeb, engine
from mbackend.alchemy.scoped_dao.dao_factory import DaoFactory


class SimilarDAOFactory(DaoFactory):
    def __init__(self):
        SimilarWeb.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def add_similar_web_data(self, data):
        with self.Session() as session:
            similar_web_instance = SimilarWeb(**data)
            self.insert_and_commit(session, similar_web_instance)

    @staticmethod
    def insert_and_commit(session, instance):
        session.add(instance)
        session.commit()
