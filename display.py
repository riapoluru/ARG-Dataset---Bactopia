import pandas as pd
from tabulate import tabulate

df = pd.read_csv("amrfinderplus.tsv", sep="\t")

# Select the corrected columns
display_columns = ["Element symbol", "Class", "Contig id", "Start", "Stop", "Method"]

# Clean and format the table
table_data = df[display_columns].fillna("N/A").values.tolist()

# Print formatted table
print("AMR Genes in SRR15144755")
print(tabulate(table_data, headers=display_columns, tablefmt="pretty"))

#-----------------------------------------------------------

# Group by AMR class and sum counts
#class_counts = df.groupby("Class")["Count"].sum().reset_index()
#print(class_counts)

#class_counts = df.groupby("Class").size().reset_index(name='Gene_Count')
#print(class_counts)
print("\n")

print("Count by Class")
class_counts = df.groupby("Class", dropna=False).size().reset_index(name='Gene_Count')
class_counts['Class'] = class_counts['Class'].fillna('NA')
print(class_counts)
