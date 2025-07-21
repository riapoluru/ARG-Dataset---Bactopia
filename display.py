import pandas as pd
from tabulate import tabulate

#-----------------------------------------------------------

df = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia-runs/bactopia-20250719-232123/merged-results/amrfinderplus.tsv", sep="\t")
df12 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia-runs/bactopia-20250720-003724/merged-results/amrfinderplus.tsv", sep="\t")
df1 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia runs/1_S446_R1_001/bactopia-runs/bactopia-20250720-115233/merged-results/amrfinderplus.tsv", sep="\t")
df2 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia runs/2_S447_R1_001/bactopia-runs/bactopia-20250720-203939/merged-results/amrfinderplus.tsv", sep="\t")
df13 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia runs/13_S450_R1_001/bactopia-runs/bactopia-20250720-110921/merged-results/amrfinderplus.tsv", sep="\t")
df26 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia runs/26_S451_R1_001/bactopia-runs/bactopia-20250720-123711/merged-results/amrfinderplus.tsv", sep="\t")
df27 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia runs/27_S452_R1_001/bactopia-runs/bactopia-20250720-133846/merged-results/amrfinderplus.tsv", sep="\t")
df28 = pd.read_csv("/Users/polur/Documents/Bactopia/ARG-Dataset---Bactopia-11/my-sample-results/bactopia runs/28_S453_R1_001/bactopia-runs/bactopia-20250720-194944/merged-results/amrfinderplus.tsv", sep="\t")

# Select the corrected columns
display_columns = ["Gene symbol", "Class", "Contig id", "Start", "Stop", "Method"]

# Clean and format the table
table_data = df[display_columns].fillna("N/A").values.tolist()
table_data_12=df12[display_columns].fillna("N/A").values.tolist()
table_data_1=df1[display_columns].fillna("N/A").values.tolist()
table_data_2=df2[display_columns].fillna("N/A").values.tolist()
table_data_13=df13[display_columns].fillna("N/A").values.tolist()
table_data_26=df26[display_columns].fillna("N/A").values.tolist()
table_data_27=df27[display_columns].fillna("N/A").values.tolist()
table_data_28=df28[display_columns].fillna("N/A").values.tolist()

#-----------------------------------------------------------

# Print formatted table
print("AMR Genes in _11")
print(tabulate(table_data, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class")
class_counts = df.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts['Class'] = class_counts['Class'].fillna('NA')
print(class_counts)

print("\n")
print("\n")
print("\n")

#-----------------------------------------------------------

print("AMR Genes in _12")
print(tabulate(table_data_12, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (12)")
class_counts_12 = df12.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_12['Class'] = class_counts_12['Class'].fillna('NA')
print(class_counts_12)

print("\n")
print("\n")
print("\n")
#-----------------------------------------------------------

print("AMR Genes in _1")
print(tabulate(table_data_1, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (1)")
class_counts_1 = df1.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_1['Class'] = class_counts_1['Class'].fillna('NA')
print(class_counts_1)

print("\n")
print("\n")
print("\n")

#-----------------------------------------------------------

print("AMR Genes in _2")
print(tabulate(table_data_2, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (2)")
class_counts_2 = df2.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_2['Class'] = class_counts_2['Class'].fillna('NA')
print(class_counts_2)

print("\n")
print("\n")
print("\n")

#-----------------------------------------------------------

print("AMR Genes in _13")
print(tabulate(table_data_13, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (13)")
class_counts_13 = df13.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_13['Class'] = class_counts_13['Class'].fillna('NA')
print(class_counts_13)

print("\n")
print("\n")
print("\n")

#-----------------------------------------------------------

print("AMR Genes in _26")
print(tabulate(table_data_26, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (26)")
class_counts_26 = df26.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_26['Class'] = class_counts_26['Class'].fillna('NA')
print(class_counts_26)

print("\n")
print("\n")
print("\n")

#-----------------------------------------------------------

print("AMR Genes in _27")
print(tabulate(table_data_27, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (27)")
class_counts_27 = df27.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_27['Class'] = class_counts_27['Class'].fillna('NA')
print(class_counts_27)

print("\n")
print("\n")
print("\n")

#-----------------------------------------------------------

print("AMR Genes in _28")
print(tabulate(table_data_28, headers=display_columns, tablefmt="pretty"))

print("\n")

print("Count by Class (28)")
class_counts_28 = df28.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts_28['Class'] = class_counts_28['Class'].fillna('NA')
print(class_counts_28)

print("\n")
print("\n")
print("\n")