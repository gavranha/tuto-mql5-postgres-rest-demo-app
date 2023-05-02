import json
import os
from psycopg2 import TimestampFromTicks
import psycopg2

script_dir = os.path.dirname(__file__)
filename = "deals.json"
json_file = os.path.join(script_dir, filename)
f = open(json_file, "r", encoding="utf-8")
dic = json.load(f)

sql = "INSERT INTO deals (d_ticket, d_order, d_position, d_time, d_type, d_entry, d_magic, d_reason, d_symbol, d_volume, d_price, d_profit, d_swap, d_comission) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
conn = psycopg2.connect(
    "dbname=my_remote_db user=mt5_user password=123 host=172.20.155.236")

for lis in dic["deals"]:
    print("\n")
    ticket = 0
    order = 0
    position = 0
    time = None
    type = ''
    entry = ''
    magic = 0
    reason = ''
    symbol = ''
    volume = 0.0
    price = 0.0
    profit = 0.0
    swap = 0.0
    comission = 0.0
    for k in lis:
        # print(k + " = "+str(lis[k]))
        ticket = lis["ticket"]
        order = lis["order"]
        position = lis["position"]
        time = TimestampFromTicks(lis["time"])
        type = lis["type"]
        entry = lis["entry"]
        magic = lis["magic"]
        reason = lis["reason"]
        symbol = lis["symbol"]
        volume = lis["volume"]
        price = lis["price"]
        profit = lis["profit"]
        swap = lis["swap"]
        comission = lis["comission"]
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (ticket, order, position, time, type, entry,
                              magic, reason, symbol, volume, price, profit, swap, comission),)


# lis = dic["deals"]
# print(type(lis))
# print(lis[0])
# print(len(lis))
# print(dic["acc_info"][0])
# print(list(dic), len(dic))
