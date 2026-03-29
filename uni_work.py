import psutil
import os

# ---- 1. CPU + MEMORY ----
cpu = psutil.cpu_percent()
memory = psutil.virtual_memory()

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory.percent}%")

# ---- 2. TOP 10 PROCESSES ----
print("\nTop 10 memory consuming processes:")

processes = []

for p in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
    try:
        processes.append(p.info)
    except:
        pass

# sort by memory usage
processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)

for proc in processes[:10]:
    print(f"PID: {proc['pid']} | User: {proc['username']} | CPU: {proc['cpu_percent']}% | MEM: {proc['memory_percent']:.2f}%")

# ---- 3 + 4. TERMINATE WITH CONFIRM + PROTECTION ----

# protected PIDs
protected_pids = [0, 1, os.getpid()]

choice = input("\nDo you want to terminate a process? (yes/no): ").lower()

if choice in ['yes', 'y']:
    try:
        pid = int(input("Enter PID: "))

        if pid in protected_pids:
            print("❌ Cannot terminate critical system process.")
        else:
            proc = psutil.Process(pid)
            confirm = input(f"Terminate {proc.name()} (PID {pid})? (yes/no): ").lower()

            if confirm in ['yes', 'y']:
                proc.terminate()
                print("✅ Process terminated.")
            else:
                print("Cancelled.")

    except psutil.NoSuchProcess:
        print("❌ Process not found.")
    except psutil.AccessDenied:
        print("❌ Permission denied.")
    except ValueError:
        print("❌ Invalid PID.")
else:
    print("Done.")