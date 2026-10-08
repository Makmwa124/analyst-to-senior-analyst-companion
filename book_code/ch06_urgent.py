import pandas as pd

req = pd.read_csv("data/requests.csv")
req["used"] = req["used_in_decision"].eq("Yes")
print(pd.crosstab(req["stated_priority"], req["used_in_decision"],
                  margins=True, margins_name="Total"))
print()
rate = req.groupby("stated_priority")["used"].mean() * 100
print(rate.round(0))
