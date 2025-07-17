import subprocess
import sys

baap_command = ["bactopia", "--r1 /fastq/SRR15144755_1.fastq.gz", "--r2 /fastq/SRR15144755_1.fastq.gz", "--sample SRR15144755", "--outdir local-single-sample","-profile docker"]

try:
    print(" Running BaAP pipeline...\n")
    subprocess.run(baap_command, check=True)
    print("BaAP completed\n")
except subprocess.CalledProcessError as e:
    print(f"BaAP run failed: {e}\n")
    sys.exit(1)