import os
import snowflake.connector
import pandas as pd

user_name = 'RAJIVMEHTADA'
password='Root@123'
account_identifier = 'dm17579'
region='ap-south-1'

conn = snowflake.connector.connect(user=user_name,password=password,account=account_identifier,region=region,warehouse='COMPUTE_WH')
cursor = conn.cursor()
sql=f'''
SELECT * FROM MELTANO."PUBLIC".DIABETES 
LIMIT 5;
'''
foo=cursor.execute(sql)
print(foo.fetchall())