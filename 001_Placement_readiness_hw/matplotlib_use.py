import pandas as pd
import matplotlib 
matplotlib.use("Agg")

import matplotlib.pyplot as plt

df = pd.read_csv("our_data.csv")
print(df.head())

dict = {
    "Python_Score" : float(df["Python_Score"].mean()),
    "SQL_Score" : float(df["SQL_Score"].mean()),
    "Aptitude_Score" : float(df["Aptitude_Score"].mean()),
    "Communication_Score" : float(df["Communication_Score"].mean())
}

plt.figure(figsize=(10,15))
plt.bar(dict.keys(),dict.values(),color="green")
plt.title("Bar graph on avg skill score")
plt.xlabel("Skills")
plt.ylabel("Avg of skill")
plt.tight_layout()
plt.savefig("charts/f1.png")
plt.close()

d = (df["Readiness_Band"].value_counts()).to_dict()
# print(d)
plt.figure(figsize=(9,10))
plt.bar(d.keys(),d.values(),color="green")
plt.title("Bar graph on readiness band")
plt.xlabel("Readiness")
plt.ylabel("Count of students")
plt.tight_layout()
plt.savefig("charts/f2.png")
plt.close()

u = ((df.groupby("Branch")["Readiness_Score"]).mean().round(2)).to_dict()
plt.figure(figsize=(9,10))
plt.plot(u.keys(),u.values(),marker="s",color="green")
plt.title("Bar graph on avg readiness_score grouped by branch")
plt.xlabel("Branch")
plt.ylabel("Avg. readiness Score")
plt.legend()
plt.tight_layout()
plt.savefig("charts/f3.png")
plt.close()
