import pandas as pd
import numpy as np

df = pd.read_csv("placement_readiness.csv")

li = df[df["Python_Score"]>75]
print(li["Python_Score"].head())


l2 = (df["Aptitude_Score"]).sort_values(ascending=False)
print(l2.head())

print((df["Python_Score"].sort_values(ascending=False)).head(10))

print((df[df["Python_Score"]>df["Communication_Score"]]))

df["Total_Skill"] = df["Aptitude_Score"] + df["Python_Score"] + df["Communication_Score"] + df["SQL_Score"]
# print(df.head())

df["Average_Score"] = (df["Total_Skill"]/4 ).round(2)
print(df.head())

df["Weakest_Skill"] = df[["Aptitude_Score","Communication_Score","Python_Score","SQL_Score"]].min(axis=1)
print(df.head())

df["Readiness_Score"] = (df["Average_Score"] + 2*df["Projects_Completed"] + df["Mock_Interviews_Attended"]).clip(upper=100)
print(df.head())

df["Readiness_Band"] = "Ready"

df["Readiness_Band"] = np.where((df["Readiness_Score"]<100) & ((df["Readiness_Score"]>=60) & (df["Readiness_Score"]<=74)) , "Almost Ready" , "Not Ready")
print(df["Readiness_Band"].value_counts())
print((df["Readiness_Band"].value_counts()).idxmax())