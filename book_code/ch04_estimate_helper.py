import pandas as pd

req = pd.read_csv("data/requests.csv")
req["ratio"] = req["actual_hours"] / req["est_hours"]
p80 = req.groupby("request_type")["ratio"].quantile(0.8)

def quote(gut_hours, request_type):
    """Turn a gut-feel estimate into a range you can say out loud."""
    is_type = req["request_type"] == request_type
    low = gut_hours * req.loc[is_type, "ratio"].median()
    high = gut_hours * p80[request_type]
    return f"{request_type}: {low:.0f} to {high:.0f} hours"

print(quote(8, "Dashboard change"))
print(quote(20, "Deep dive"))
