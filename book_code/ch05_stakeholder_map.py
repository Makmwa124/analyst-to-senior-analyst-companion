import numpy as np
import pandas as pd

st = pd.read_csv("data/stakeholders.csv")
hi_inf = st["influence"] >= 3
hi_int = st["interest"] >= 3
st["approach"] = np.select(
    [hi_inf & hi_int, hi_inf & ~hi_int, ~hi_inf & hi_int],
    ["Manage closely", "Keep satisfied", "Keep informed"],
    default="Monitor")
print(st.sort_values(["approach", "influence"],
                     ascending=[True, False])
        [["name", "influence", "interest", "stance", "approach"]]
        .to_string(index=False))
