import os
import subprocess
import pandas as pd
import re
import sys
import csv
import glob
import difflib
from collections import defaultdict

# === CONFIGURATION ===
FASTQ_DIR = "/mnt/c/Users/polur/Downloads/fastqs" 
OUTDIR_ROOT = "bactopia_outputs"  
PROFILE = "docker" 

# === SETUP ===
os.makedirs(OUTDIR_ROOT, exist_ok=True)

# Get unique sample names from *_1.fastq.gz files
samples = set()
for file in os.listdir(FASTQ_DIR):
    if file.endswith("_1.fastq.gz"):
        sample = file.replace("_1.fastq.gz", "")
        samples.add(sample)

if not samples:
    print("❌ No FASTQ files found in folder:", FASTQ_DIR)
    sys.exit(1)

# === MAIN LOOP ===
for sample in sorted(samples):
    r1 = os.path.join(FASTQ_DIR, f"{sample}_1.fastq.gz")
    r2 = os.path.join(FASTQ_DIR, f"{sample}_2.fastq.gz")
    outdir = os.path.join(OUTDIR_ROOT, sample)

    if not os.path.isfile(r1) or not os.path.isfile(r2):
        print(f"⚠️ Skipping {sample}: missing R1 or R2 file")
        continue

    command = [
        "bactopia",
        "--r1", r1,
        "--r2", r2,
        "--sample", sample,
        "--outdir", outdir,
        "-profile", PROFILE
    ]

    print(f"Running Bactopia for: {sample}")
    try:
        subprocess.run(command, check=True)
        print(f"✅ Completed: {sample}\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Bactopia failed for {sample}: {e}\n")


'''
fastq_dir = '/Users/connor/Downloads/Illumina_DNA_Reads'

try:
    stat_xlsx = glob.glob(fastq_dir + "/*.xlsx")[0]
    print("📈 Found stat excel sheet: " + stat_xlsx)
except IndexError:
    print("❌ No stat excel sheet found in the directory.")
    sys.exit(1)
df = pd.read_excel(stat_xlsx)
df["Sample Name"] = df["Sample Name"].astype(str)

all_files = os.listdir(fastq_dir)
all_files = glob.glob(os.path.join(fastq_dir, "*.fastq.gz"))
sorted_files = sorted(all_files, key=lambda x: os.path.basename(x))
# print("🗂️ Confirm Sorted Files: " + str([(s.split("/")[-1])[:-9] for s in sorted_files]))
# print("Should the program continue? [y/n]: ")
# cont = first_char = sys.stdin.read(1)
# if cont.lower() != 'y':
#     print("❌ Exiting program. Please check the filenames again")
#     sys.exit(1)

r1_files = sorted_files[::2]
r2_files = sorted_files[1::2]
commands = []

for r1, r2 in zip(r1_files, r2_files):
    difflist = [c for c in list(zip(difflib.ndiff(r1, r2))) if c[0][0] != ' ' ]
    if len(difflist) > 2 or difflist[0][0] != '- 1' or difflist[1][0] != '+ 2':
        r1_name = r1.split("/")[-1]
        r2_name = r2.split("/")[-1]
        #     print("end it its error 3")
        print(f"❌ Mismatched files: {r1_name} and {r2_name}. Please check the filenames.")
        sys.exit(1)

    sample = (r1.split("/")[-1])[:-9]
    outdir = f"bactopia_output"

    cmd = [
        "--r1", os.path.join(fastq_dir, r1),
        "--r2", os.path.join(fastq_dir, r2),
    ]
    commands.append(cmd)
'''