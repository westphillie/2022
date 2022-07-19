import pandas as pd
from sqlalchemy import create_engine
url = "mysql+pymysql://dev:gtydb5hku0ANC4kwn@104.196.199.57/phillies"
engine = create_engine(url, echo=True)
df = pd.read_csv('prospects.csv')
df.to_sql('prospects', engine)