msg = ["Hello world", "Hi World"]

for m in msg:
    print(f"m => {m}")

for i in range(1, 10):
    print (i)
    if i < 5:
        print (i)
    else:
        break

stocks = {
    'IBM' : 1,
    'MSFT' : 2,
    'CSCO' : 3
}

for s in stocks:
    print (s)

for k, v in stocks.items():
    print (f"{k} : {v}")

try:
    a = 1 / 0
except Exception as e:
    print (e)    