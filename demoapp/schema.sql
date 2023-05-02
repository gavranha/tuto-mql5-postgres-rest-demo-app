DROP TABLE IF EXISTS deals;
DROP TABLE IF EXISTS accs;

CREATE TABLE accs (
    a_id SERIAL PRIMARY KEY,
    a_login INTEGER, -- MQL5 integers
    a_trade_mode VARCHAR,
    a_leverage INTEGER,
    --a_limit_orders INTEGER,--?? not in json
    a_margin_so_mode VARCHAR,
    a_trade_allowed BOOLEAN,
    a_ea_allowed BOOLEAN,
    -- a_margin_mode VARCHAR,
    -- a_currency_digits INTEGER,
    -- a_fifo_close BOOLEAN,
    -- a_hedge_allowed BOOLEAN,
    a_balance NUMERIC, -- MQL5 doubles
    a_credit NUMERIC,
    a_profit NUMERIC,
    a_equity NUMERIC,
    a_margin NUMERIC,
    a_margin_free NUMERIC,
    a_margin_level NUMERIC,
    a_margin_so_call NUMERIC,
    a_margin_so_so NUMERIC,
    -- a_margin_initial NUMERIC,
    -- a_margin_maintenance NUMERIC,
    -- a_assets NUMERIC,
    -- a_liabilities NUMERIC,
    -- a_commision_blocked NUMERIC,
    a_name VARCHAR, -- MQL5 strings
    a_server VARCHAR,
    a_currency VARCHAR,
    a_company VARCHAR
);

GRANT ALL PRIVILEGES ON TABLE accs TO mt5_user;

CREATE TABLE deals (
    d_id SERIAL PRIMARY KEY,
    d_ticket INTEGER,
    d_order INTEGER, -- MQL5 integers
    d_position INTEGER,
    d_time TIMESTAMP,
    d_type VARCHAR,
    d_entry VARCHAR,
    d_magic INTEGER,
    d_reason VARCHAR,
    d_symbol VARCHAR, -- MQL5 string
    d_volume NUMERIC, -- MQL5 doubles
    d_price NUMERIC,
    d_profit NUMERIC,
    d_swap NUMERIC,
    d_comission NUMERIC
    );

GRANT ALL PRIVILEGES ON TABLE deals TO mt5_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO mt5_user;
-- insert some fixture data
-- INSERT INTO accs (id, broker, acc_nr, balance) 
--     VALUES (default, 'Raw Trading', '12345678', 1.000);
-- INSERT INTO deals (id, symbol) 
--     VALUES (default, 'EURUSD');

