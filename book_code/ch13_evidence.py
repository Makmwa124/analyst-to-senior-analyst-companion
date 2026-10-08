import pandas as pd

ev = pd.read_csv("data/evidence_log.csv", parse_dates=["date"])
print(ev.groupby("skill").size().sort_values(ascending=False))
print()
q = ev["date"].dt.to_period("Q").astype(str)
print(pd.crosstab(ev["skill"], q))
