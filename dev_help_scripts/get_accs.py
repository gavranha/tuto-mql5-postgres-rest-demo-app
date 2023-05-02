from psycopg2 import TimestampFromTicks
from psycopg2.extras import DictCursor
import psycopg2

sql = "SELECT * FROM deals"
conn = psycopg2.connect(
    "dbname=my_remote_db user=mt5_user password=123 host=172.20.155.236")
with conn:
    with conn.cursor(cursor_factory=DictCursor) as c:
        c.execute(sql)
        results = [{key: value for key, value in row.items()} for row in c]
        print(results)


# for lis in dic["acc_info"]:
#     print("\n")
#     for k in lis:
#         print(k + " = "+str(lis[k]))
#         login = lis["login"]
#         trade_mode = lis["trade_mode"]
#         leverage = lis["leverage"]
#         margin_so_mode = lis["margin_so_mode"]
#         trade_allowed = bool(lis["trade_allowed"])
#         ea_allowed = bool(lis["ea_allowed"])
#         balance = lis["balance"]
#         credit = lis["credit"]
#         profit = lis["profit"]
#         equity = lis["equity"]
#         margin = lis["margin"]
#         margin_free = lis["margin_free"]
#         margin_level = lis["margin_level"]
#         margin_so_call = lis["margin_so_call"]
#         margin_so_so = lis["margin_so_so"]
#         name = lis["name"]
#         server = lis["server"]
#         currency = lis["currency"]
#         company = lis["company"]
#         with conn:
#             with conn.cursor() as cur:
#                 cur.execute(sql, (login, trade_mode, leverage, margin_so_mode, trade_allowed, ea_allowed, balance, credit, profit,
#                             equity, margin, margin_free, margin_level, margin_so_call, margin_so_so, name, server, currency, company),)
# lis = dic["deals"]
# print(type(lis))
# print(lis[0])
# print(len(lis))
# print(dic["acc_info"][0])
# print(list(dic), len(dic))
