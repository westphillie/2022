from numpy import genfromtxt
from sqlalchemy import Column, Text, Float, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

url = "mysql+pymysql://dev:gtydb5hku0ANC4kwn@104.196.199.57/phillies"
engine = create_engine(url, echo=True)
Base = declarative_base()


class Listing(Base):
    __tablename__ = 'prospects'
    id = Column(Integer, primary_key=True)
    Rank = Column(Integer)
    Top_100 = Column(Integer)
    Trend = Column(String(50))
    Name = Column(String(50))
    Pos = Column(String(20))
    Age = Column(Float)
    Ht = Column(String(50))
    Wt = Column(Integer)
    B = Column(String(1))
    T = Column(String(1))
    School = Column(String(50))
    College_Commit = Column(String(50))
    FV = Column(Integer)
    Risk = Column(String(20))
    Report = Column(Text)
    Video = Column(String(50))
    School_Type = Column(String(20))

Base.metadata.create_all(engine)

session = sessionmaker()
session.configure(bind=engine)
s = session()
try:
        file_name = "prospects.csv"
        data = Load_Data(file_name)
        for i in data:
            record = Listing(**{
                'Rank' : i[0],
                'Top_100' : i[1],
                'Trend' : i[2],
                'Name' : i[3],
                'Pos' : i[4],
                'Age' : i[5],
                'Ht' : i[6],
                'Wt' : i[7],
                'B' : i[8],
                'T' : i[9],
                'School' : i[10],
                'College_Commit' : i[11],
                'FV' : i[12],
                'Risk' : i[13],
                'Report' : i[14],
                'Video' : i[15],
                'School_Type' : i[16]
            })
            s.add(record) #Add all the records
        s.commit()  # Attempt to commit all the records
except:
    s.rollback() #Rollback the changes on error
finally:
    s.close() #Close the connection
