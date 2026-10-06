#6.1
cpu_load=87
memory_load=92
if cpu_load>80:
    cpu_status="HIGH"
else:
    cpu_status="OK"
memory_status="HIGH" if memory_load>80 else "ОК"
if (cpu_status | memory_status):
    system_status="Critical"
else: system_status="Normal"