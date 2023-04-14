""" Database configurations and access """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

from .db_data_access import data_access

database_name = data_access['name']
username = data_access['username']
password = data_access['password']
host = data_access['host']
port = data_access['port']

url_connection = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(username, password, host, port, database_name)
connection = create_engine(url_connection)

Session = sessionmaker(bind=connection)
session = Session()

base = declarative_base()
