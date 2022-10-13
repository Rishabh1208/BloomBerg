# You are given a list of stock exchange along with startTime and endTime in which these exchanges
# operate.
# 0 <= startTime, endTime <= 23

# [
#     ['Exchange A', 2, 7],
#     ['Exchange C', 11, 17],
#     ['Exchange B', 9, 16],
#     ['Exchange D', 14, 20]
# ]
# Then, given a list of buy/sell orders which need to be executed in the given timeframe you need to
# find out what all orders can be served with atleast 1 exchange.

# [
#     ['Order 1', '3', '6'],
#     ['Order 2', '9', '12'],
#     ['Order 3', '21', '22']
# ]
# So in this case Order 1 and 2 can be served but 3 cannot be served by any exchange.

# Follow-up = What if some exchanges operate from night to morning, ex - ['Exchange X', 23, 5].
# Same thing with orders.


def solution(exchanges, trades):

    m_exchanges = []
    sorted_exchanges = sorted(exchanges, key=lambda i: i[0])

    for exchange in sorted_exchanges:

        opening_time, closing_time = exchange
        if closing_time < opening_time:  # works over 24 hours eg 23 - 2
            split_exchange = ((opening_time, 24), (0, closing_time))
        else:
            split_exchange = [exchange]

        for exc in split_exchange:
            cur_opening_time, cur_closing_time = exc
            if len(m_exchanges) < 1:
                m_exchanges.append(exc)
            else:
                last_entry_start, last_entry_end = m_exchanges[-1]
                if cur_opening_time <= last_entry_end:
                    # can merge
                    # keep previous start time, update end time with max
                    m_exchanges[-1] = (last_entry_start,
                                       max(last_entry_end, cur_closing_time))
                else:  # does not overlap
                    m_exchanges.append((exc))

    for trade in trades:
        t_start, t_end = trade

        if t_end < t_start:

            # over midnight, should split
            split_trade = [(t_start, 24), (0, t_end)]
        else:
            split_trade = [trade]

        exchange_found = "none"

        for s_trade in split_trade:
            s_trade_start, s_trade_stop = s_trade

            # search for valid exchange

            for exchange in m_exchanges:
                x_opening_time, x_closing_time = exchange

                if x_opening_time <= s_trade_start and x_closing_time >= s_trade_stop:

                    exchange_found = True if exchange_found == "none" else (
                        exchange_found and True)
                    break

            exchange_found = False if exchange_found == "none" else exchange_found

        print(trade, exchange_found)


e = [(2, 7), (11, 17), (9, 16), (14, 20), (23, 4)]
t = [(3, 6), (9, 12), (21, 22), (23, 2)]

solution(e, t)
