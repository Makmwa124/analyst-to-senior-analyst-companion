import pandas as pd

req = pd.read_csv("data/requests.csv")
hours = (req.groupby("request_type")["actual_hours"]
            .agg(requests="count", hours="sum")
            .sort_values("hours", ascending=False))
hours["share"] = (hours["hours"] / hours["hours"].sum()
                  * 100).round(1)
print(hours)
print("Total hours:", req["actual_hours"].sum().round(1))
