import subprocess
import sys

condor_batch_type = "condor"
slurm_batch_type = "slurm"
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 WorkQueueFactory.py manager_name batch_type")
        sys.exit(1)
    manager_name = sys.argv[1]
    batch_type = sys.argv[2]

    if batch_type == slurm_batch_type:
        subprocess.run(["work_queue_factory", "-T", batch_type, "-B", "--partition=skx -t 0:20:00", "-M", manager_name, "-w", "10", "-W", "20", "--workers-per-cycle", "10", "--poncho-env=package.tar.gz"])
    elif batch_type == condor_batch_type:
        subprocess.run(["work_queue_factory", "-T", batch_type, "-M", manager_name, "-w", "100", "-W", "300", "--workers-per-cycle", "50", "--poncho-env=package.tar.gz"])
    else:
        print(f"Batch type {batch_type} not supported yet. Please choose between condor and slurm")
