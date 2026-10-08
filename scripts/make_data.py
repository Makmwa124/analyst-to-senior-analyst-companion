"""Generate the Paperbark Mutual practice data used in the book.
Paperbark Mutual and everyone in the data are fictional."""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(2026)
out = Path(__file__).resolve().parent.parent / "data"
out.mkdir(exist_ok=True)

requesters = {
    "Deb Laurent": "Claims", "Marcus Webb": "Claims",
    "Sam Whitfield": "Marketing", "Lena Ortiz": "Marketing",
    "Helen Marsh": "Finance", "Raj Patel": "Finance",
    "Tom Okafor": "Analytics", "Grace Liu": "Member Services",
    "Ben Cartwright": "Member Services", "Anika Shah": "Product",
}
weights = np.array([14, 8, 16, 9, 7, 6, 6, 12, 8, 14], float)
weights /= weights.sum()

types = {  # type: (share, est mean hours, overrun multiplier mean)
    "Ad hoc question": (0.38, 3, 1.6),
    "Recurring report": (0.22, 4, 1.15),
    "Dashboard change": (0.18, 6, 1.5),
    "Deep dive": (0.12, 24, 1.7),
    "Data fix": (0.10, 5, 1.9),
}
tnames = list(types)
tp = np.array([types[t][0] for t in tnames])

n = 184
days = pd.date_range("2025-07-01", "2026-06-30", freq="B")
received = np.sort(rng.choice(days, n))
rows = []
for i in range(n):
    req = rng.choice(list(requesters), p=weights)
    t = rng.choice(tnames, p=tp)
    _, est_mu, over = types[t]
    est = max(1, round(rng.gamma(4, est_mu / 4)))
    urgent = rng.random() < (0.45 if t == "Ad hoc question" else 0.25)
    actual = round(est * rng.lognormal(np.log(over), 0.35), 1)
    lag = int(np.ceil(actual / (5 if urgent else 2.5))) + int(rng.integers(0, 4 if urgent else 8))
    delivered = pd.Timestamp(received[i]) + pd.offsets.BDay(max(lag, 1))
    p_used = {"Ad hoc question": 0.45, "Recurring report": 0.35,
              "Dashboard change": 0.5, "Deep dive": 0.8, "Data fix": 0.7}[t]
    if urgent:
        p_used -= 0.12
    r = rng.random()
    used = "Yes" if r < p_used else ("Unknown" if r < p_used + 0.25 else "No")
    rows.append([f"R{i+1:03d}", pd.Timestamp(received[i]).date(), req, requesters[req], t,
                 "Urgent" if urgent else "Normal", est, actual, delivered.date(), used])

df = pd.DataFrame(rows, columns=["request_id", "received", "requester", "team", "request_type",
                                 "stated_priority", "est_hours", "actual_hours", "delivered",
                                 "used_in_decision"])
df.to_csv(out / "requests.csv", index=False)

stake = pd.DataFrame({
    "name": ["Helen Marsh", "Deb Laurent", "Sam Whitfield", "Grace Liu", "Raj Patel",
             "Anika Shah", "Marcus Webb", "Lena Ortiz", "Ben Cartwright", "Tom Okafor"],
    "role": ["Chief Financial Officer", "Head of Claims", "Marketing Manager",
             "Member Services Manager", "Finance Business Partner", "Product Lead",
             "Claims Team Leader", "Campaign Specialist", "Service Team Leader",
             "Analytics Manager"],
    "influence": [5, 4, 3, 3, 2, 4, 2, 1, 1, 4],
    "interest": [2, 5, 5, 4, 4, 2, 5, 4, 2, 5],
    "stance": ["Neutral", "Supportive", "Sceptical", "Supportive", "Neutral",
               "Unknown", "Supportive", "Neutral", "Neutral", "Supportive"],
})
stake.to_csv(out / "stakeholders.csv", index=False)

ev = pd.DataFrame([
    ["2025-08-14", "Scoping", "Rewrote the claims backlog request as a one-sentence question; cut scope from 9 charts to 3", "Delivered in 4 days, not the 3 weeks first estimated"],
    ["2025-09-03", "Stakeholders", "Set up a fortnightly 20-minute check-in with Deb Laurent", "Ad hoc requests from Claims fell from 6 to 2 a month"],
    ["2025-12-12", "Influence", "Showed that the retention offer went mostly to members who would have stayed anyway", "Marketing narrowed the offer; projected saving $410k a year"],
    ["2025-11-12", "Saying no", "Retired a weekly report nobody opened (12 views in 6 months)", "Freed 3 hours a week"],
    ["2025-12-05", "Delivery", "Shipped the member churn dashboard two days early", "Used in the December board pack"],
    ["2026-01-28", "Team", "Wrote the team's SQL style guide and ran two lunch sessions", "Adopted by all 5 analysts"],
    ["2026-02-17", "Influence", "Persuaded Finance to change the definition of an active member", "Removed a 4% gap between Finance and Analytics reports"],
    ["2026-03-09", "Team", "Mentored graduate analyst Jordan through her first deep dive", "Jordan presented to the Claims leadership team"],
    ["2026-04-22", "Scoping", "Turned a vague 'why are complaints up' request into two testable questions", "Found the cause (a billing letter) within a week"],
    ["2026-05-30", "Delivery", "Automated the monthly claims pack in Python", "Cut 9 hours a month to 40 minutes"],
    ["2026-06-18", "Stakeholders", "Briefed the CFO before the pricing meeting so there were no surprises", "Recommendation approved in the meeting"],
], columns=["date", "skill", "what_i_did", "result"])
ev.to_csv(out / "evidence_log.csv", index=False)
print(len(df), "requests;", len(stake), "stakeholders;", len(ev), "evidence entries")
