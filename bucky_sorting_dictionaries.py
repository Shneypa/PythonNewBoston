stocks = {"GOOG": 520.05,
          "AAPL": 99.45,
          "AMZN": 320.34,
          "YHOO": 74.44}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

print(sorted(zip(stocks.keys(), stocks.values())))