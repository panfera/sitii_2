from sqlalchemy import create_engine, text
import pandas as pd
from card import card

def postgreSQL_db_getter(id: int) -> (card, list[int], list[int]):
	username = 'user2'
	password = 'iZ3xJBluKntzEd7YHf8I05'
	host = 'rc1b-k9hzjt7fpigoex2c.mdb.yandexcloud.net'
	port = '6432'
	mydatabase = 'db1'
	DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{mydatabase}"
	engine = create_engine(DATABASE_URL, connect_args={'sslmode': 'require'})
	conn = engine.connect()

	with engine.begin() as conn:
		query = text(f"SELECT * FROM sitii_lr2_incidents WHERE id = '{id}';")
		df = pd.read_sql_query(query, conn)
		#print(df)
		#print(df.info())
	df_dict = df.to_dict('list')

	return card(df_dict['name'][0], df_dict['type'][0], df_dict['events_count'][0], df_dict['crit_rate'][0], \
	[], [], df_dict['start_time'][0], df_dict['end_time'][0]), df_dict['assets_id'][0], df_dict['vulnerabilities_id'][0]
