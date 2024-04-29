from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from configs.config import HOST, PORT, DBNAME, USER, PASSWORD

engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}')
Session = sessionmaker(bind=engine)