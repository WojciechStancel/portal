from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:xzmno523pR@127.0.0.1:3306/portal")

Base = declarative_base(bind=engine)
