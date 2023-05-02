import json
import os
from psycopg2 import TimestampFromTicks
import psycopg2

script_dir = os.path.dirname(__file__)
filename = "accs.json"
json_file = os.path.join(script_dir, filename)
f = open(json_file, "r", encoding="utf-8")
dic = json.load(f)

sql = "INSERT INTO accs (a_login, a_trade_mode, a_leverage, a_margin_so_mode, a_trade_allowed, a_ea_allowed, a_balance, a_credit, a_profit, a_equity, a_margin, a_margin_free, a_margin_level, a_margin_so_call, a_margin_so_so, a_name, a_server, a_currency, a_company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
conn = psycopg2.connect(
    "dbname=my_remote_db user=mt5_user password=123 host=172.20.155.236")

for lis in dic["acc_info"]:
    print("\n")
    login = 0
    trade_mode = ''
    leverage = 0
    margin_so_mode = ''
    trade_allowed = False
    ea_allowed = False
    balance = 0.0
    credit = 0.0
    profit = 0.0
    equity = 0.0
    margin = 0.0
    margin_free = 0.0
    margin_level = 0.0
    margin_so_call = 0.0
    margin_so_so = 0.0
    name = ""
    server = ""
    currency = ""
    company = ""
    for k in lis:
        print(k + " = "+str(lis[k]))
        login = lis["login"]
        trade_mode = lis["trade_mode"]
        leverage = lis["leverage"]
        margin_so_mode = lis["margin_so_mode"]
        trade_allowed = bool(lis["trade_allowed"])
        ea_allowed = bool(lis["ea_allowed"])
        balance = lis["balance"]
        credit = lis["credit"]
        profit = lis["profit"]
        equity = lis["equity"]
        margin = lis["margin"]
        margin_free = lis["margin_free"]
        margin_level = lis["margin_level"]
        margin_so_call = lis["margin_so_call"]
        margin_so_so = lis["margin_so_so"]
        name = lis["name"]
        server = lis["server"]
        currency = lis["currency"]
        company = lis["company"]
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (login, trade_mode, leverage, margin_so_mode, trade_allowed, ea_allowed, balance, credit, profit,
                        equity, margin, margin_free, margin_level, margin_so_call, margin_so_so, name, server, currency, company),)
# lis = dic["deals"]
# print(type(lis))
# print(lis[0])
# print(len(lis))
# print(dic["acc_info"][0])
# print(list(dic), len(dic))
