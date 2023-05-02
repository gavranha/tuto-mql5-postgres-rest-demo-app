import os
from flask import Flask, jsonify

# change the host bellow according to your environment (run hostname -I)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='123',
        DATABASE="dbname=my_remote_db user=mt5_user password=123 host=172.20.155.236",)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    from demoapp.db import get_db
    from psycopg2.extras import DictCursor

    from flask import request
    from psycopg2 import TimestampFromTicks

    @app.post("/accs")
    def accs_post():
        json = request.get_json()
        sql = "INSERT INTO accs (a_login, a_trade_mode, a_leverage, a_margin_so_mode, a_trade_allowed, a_ea_allowed, a_balance, a_credit, a_profit, a_equity, a_margin, a_margin_free, a_margin_level, a_margin_so_call, a_margin_so_so, a_name, a_server, a_currency, a_company) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        conn = get_db()

        for lis in json["acc_info"]:
            # print("\n")
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
                # print(k + " = "+str(lis[k]))
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
        return ""

    @app.post("/deals")
    def deals_post():
        json = request.get_json()
        sql = "INSERT INTO deals (d_ticket, d_order, d_position, d_time, d_type, d_entry, d_magic, d_reason, d_symbol, d_volume, d_price, d_profit, d_swap, d_comission) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        conn = get_db()

        for lis in json["deals"]:
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
        return ""

    @app.get('/accs')
    def accs_get():
        db = get_db()
        cur = db.cursor(cursor_factory=DictCursor)
        sql = "SELECT * FROM accs"
        cur.execute(sql)
        accs = [{key: value for key, value in row.items()} for row in cur]
        print(len(accs))
        return accs

    @app.get('/deals')
    def deals_get():
        db = get_db()
        cur = db.cursor(cursor_factory=DictCursor)
        sql = "SELECT * FROM deals"
        cur.execute(sql)
        deals = [{key: value for key, value in row.items()} for row in cur]
        print(len(deals))
        return deals

    @app.route('/')
    def hello():
        return 'Hello, World!'

    db.init_app(app)

    return app
