import pandas as pd
import pymysql
from sqlalchemy import create_engine
flight=pd.read_csv("flights.csv")
engine=create_engine("mysql+pymysql://root:@localhost/Flights")
#{root}:{password}@{url}/{database}
flight.to_sql("flights",con=engine,if_exists='append')