from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base,sessionmaker
from data.config import PG_PASS,PG_USER,PG_HOST,PG_PORT,PG_DB



engine = create_engine(f'postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')
Base=declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id =Column(Integer,primary_key=True,autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    fullname =Column(String(50),nullable=False)
    phone = Column(String(12))
    lang = Column(String(2),default='uz')

if __name__ == '__main__':
    user = User(chat_id=1498596298 , fullname='Javohirbek Begmurotov',phone='998991303032')
    session.add(user)
    session.commit()
