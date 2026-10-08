import pandas as pd

req = pd.read_csv("data/requests.csv")
req["ratio"] = req["actual_hours"] / req["est_hours"]

summary = (req.groupby("request_type")["ratio"]
              .agg(requests="count", median="median",
                   p80=lambda s: s.quantile(0.8))
              .round(2)
              .sort_values("median"))
print(summary)
print("Overall median:", req["ratio"].median().round(2))
