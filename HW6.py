import yfinance as yf

dat = yf.Ticker("LMT")   #Lockheed Martin because 250k$/year ain't about moral values
history = dat.history(period = '2mo')
history = history[['Open', "Close", 'High', 'Low', 'Volume']]

history["move_avg_7D"] = history['Close'].rolling(window = 7).mean() # для короткого ковзкого візьмемо період тижня - 7 днів.

history["move_avg_30D"] = history['Close'].rolling(window = 30).mean() # для довгого ковзкого період місяця - 30 днів.


signals = []
for i in range(len(history)):

    move_avg_7D = history["move_avg_7D"].iloc[i] #переглядаємо всі значення у колонці для повернення грошових значень
    move_avg_30D = history["move_avg_30D"].iloc[i]

    if move_avg_7D > move_avg_30D:
        signals.append("buy")
    elif move_avg_7D < move_avg_30D:
        signals.append("sell the stocks")
    else:
        signals.append("do not buy, keep")
history['Signal'] = signals   # датафрейм видає в деяких клітинках NaN через недостатню кількість торгових днів
print(history)

# створимо розрахунок прибутку/втрат

start_money = 100000
def trade_strategy (history, start_money):
    current_money = start_money
    stocks_amount = 0
    for i in range(len(history)):
        signals = history['Signal'].iloc[i]
        stock_price = history['Close'].iloc[i]

        if signals == 'buy' and current_money > stock_price:
            available_stock_amount = current_money//stock_price # цілочисельне ділення, адже купівля акції відбувається за цілісним принципом
            current_money -= available_stock_amount * stock_price 
            stocks_amount += available_stock_amount
            #print(stocks_amount)  при першому сигналі buy 2025-06-16 купуємо 214 акцій

        elif signals == 'sell the stocks' and stocks_amount > 0:
            current_money += stocks_amount * stock_price
            stocks_amount = 0        # продаємо всі

    money_received = current_money +  stocks_amount * history['Close'].iloc[-1] # продаж залишків акцій за останньою ціною закриття
    return money_received
print(trade_strategy(history,start_money))
profit = trade_strategy(history,start_money) - start_money
print(profit)

# із цією стратегією на акціях Lockheed Martin я втратив гроші.
# проте це не проблема стратегії, а самих цін на акції компанії.
# у випадку Nvidia я заробив +10.123$ за таких самих умов.