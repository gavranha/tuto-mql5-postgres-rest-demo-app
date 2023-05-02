import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    "host=172.20.155.236 dbname=my_remote_db user=mt5_user password=123")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * from accs")

# Retrieve query results
records = cur.fetchall()

print(records)
