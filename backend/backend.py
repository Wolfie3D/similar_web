from mbackend.core.fetcher import Fetcher
from mbackend.core.application import Application
from monseigneur.modules.public.similarweb.alchemy.dao_manager import SimilarDAOManager
import csv


class SimilarWebBackend(Application):

    APPNAME = "SimilarWeb Application"
    VERSION = '1.0'
    COPYRIGHT = 'Copyright(C) 2023 Your Company'
    DESCRIPTION = "Scraping Backend for SimilarWeb"
    SHORT_DESCRIPTION = "SimilarWeb Scraping Example"

    def __init__(self):
        super(SimilarWebBackend, self).__init__(self.APPNAME)
        self.setup_logging()
        self.fetcher = Fetcher(
            absolute_path=r'C:\Users\Administrator\Desktop\monseigneur\monseigneur\monseigneur\modules\public\similarweb\backend\backend.py')
        self.module = self.fetcher.build_backend("similarweb", params={})
        self.dao_manager = SimilarDAOManager("similarweb")

    def main(self):
        csv_file_path = r'./similarweb_add_on_20231207_sample - Feuil1.csv'
        filtered_urls = self.filter_urls_from_csv(csv_file_path)

        for url in filtered_urls:
            similarweb_data = self.module.get_data(url)
            self.insert_into_db(similarweb_data)

    def filter_urls_from_csv(self, csv_file_path):
        list_of_urls = []
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)
            for row in reader:
                if len(row) > 2 and row['url']:
                    list_of_urls.append(row['url'])
        return list_of_urls

    def insert_into_db(self, similarweb_data):
        session, _ = self.dao_manager.get_shared_session()
        try:
            dao = self.dao_manager.get_similarweb_dao(session)
            dao.add_similarweb_data(similarweb_data)
            dao.commit()
        finally:
            session.close()


if __name__ == '__main__':
    my_similarweb_backend = SimilarWebBackend()
    my_similarweb_backend.main()
