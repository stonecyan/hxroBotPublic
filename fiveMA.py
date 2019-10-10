import pandas as pd

# 5 min moving average, if above expect up candle, if below expect down candle

filePath = input("Enter csv file path: ")

df = pd.read_csv(filePath)

success = 0
total = 0

fiveMinPrices = []
fiveMinSum = 0

prediction = ""
startPrice = df.iloc[4]["Close"]

for index, row in df.iterrows():
    if index < 5:
        fiveMinPrices.append(row["Open"])
        fiveMinSum += row["Open"]
    else:
        # At the 4th min, make prediction based off MA
        if (index + 1) % 5 == 0:
            fiveMinMA = fiveMinSum / 5
            if row["Open"] > fiveMinMA:
                prediction = "up"
            elif row["Open"] < fiveMinMA:
                prediction = "down"
        if index % 5 == 0:
            if prediction == "up":
                if row["Close"] > startPrice:
                    success += 1
            if prediction == "down":
                if row["Close"] < startPrice:
                    success += 1
            total += 1
            startPrice = row["Close"]

            remove = fiveMinPrices.pop(0)
            fiveMinSum -= remove
            fiveMinPrices.append(row["Open"])
            fiveMinSum += row["Open"]

print(success, total, success / total)
