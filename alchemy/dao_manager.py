from mbackend.alchemy.scoped_dao.dao_manager import DaoManager

from monseigneur.modules.public.similarweb.alchemy.dao_factory import SimilarDAOFactory


class SimilarDAOManager(DaoManager):
    def __init__(self):
        self.dao_factory = SimilarDAOFactory()

    def save_similar_web_data(self, data):
        # Save data to SimilarWeb table
        self.dao_factory.add_similar_web_data(data)
