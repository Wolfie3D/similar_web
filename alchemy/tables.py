from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


SimilarWebBase = declarative_base()


class SimilarWeb(SimilarWebBase):
    __tablename__ = 'SimilarWeb'
    __table_args__ = {'mysql_charset': 'utf8mb4',
                      'mysql_collate': 'utf8mb4_bin'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(400), unique=True, nullable=False)
    domain = Column(String(400), unique=True, nullable=False)
    global_rank = Column(Integer)
    country = Column(String(400))
    country_rank = Column(Integer)
    category = Column(String(400))
    category_rank = Column(Integer)
    sep_2023_visits = Column(Integer)
    oct_2023_visits = Column(Integer)
    nov_2023_visits = Column(Integer)
    country1 = Column(String(400), unique=True)
    country2 = Column(String(400), unique=True)
    country3 = Column(String(400), unique=True)
    country4 = Column(String(400), unique=True)
    country5 = Column(String(400), unique=True)
    country1_percentage = Column(Integer)
    country2_percentage = Column(Integer)
    country3_percentage = Column(Integer)
    country4_percentage = Column(Integer)
    country5_percentage = Column(Integer)
    bounce_rate = Column(Integer)
    pages_per_visit = Column(Integer)
    monthly_visits = Column(Integer)
    avg_visit_duration = Column(Integer)


# Create an engine for SQLAlchemy
engine = create_engine(
    "mysql+mysqlconnector://root:9630@127.0.0.1/Similar_Output")
