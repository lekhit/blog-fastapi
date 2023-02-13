from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
url='postgresql+psycopg2://patil1001970:3yS9PWejbGsJ@ep-mute-cherry-902786.ap-southeast-1.aws.neon.tech/neondb'
#engine = create_engine(url,connect_args= {'ssl': {'ca': '/etc/ssl/cert.pem'}})    

engine=create_engine(url)

SessionLocal=sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base=declarative_base()