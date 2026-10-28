"""Loads data/ev_market.csv into MySQL. Set DB_URL, e.g. mysql+pymysql://root:pass@localhost/ev_market"""
import os, pandas as pd
from sqlalchemy import create_engine, text
url=os.environ.get("DB_URL","mysql+pymysql://root:password@localhost/ev_market")
eng=create_engine(url)
with eng.begin() as c:
    for stmt in open("sql/schema.sql").read().split(";"):
        s=stmt.strip()
        if s and not s.upper().startswith(("CREATE DATABASE","USE")): c.execute(text(s))
pd.read_csv("data/ev_market.csv").to_sql("ev_sales",eng,if_exists="append",index=False)
print("loaded")
