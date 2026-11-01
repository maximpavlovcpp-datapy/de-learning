servers = [
    {"name": "web-01", "cpu": 45, "ram": 70, "status": "online"},
    {"name": "web-02", "cpu": 92, "ram": 88, "status": "online"},
    {"name": "db-01", "cpu": 30, "ram": 95, "status": "online"},
    {"name": "cache-01", "cpu": 0, "ram": 0, "status": "offline"},
]
problems=0
online=0
for v in servers :
    if v["status"]=="offline":
         continue
    online+=1
    if v["cpu"]>90 or v["ram"]>90:
         problems+=1
         print(f"{v["name"]}: HIGH LOAD (cpu={v["cpu"]}%, ram={v["ram"]}%")
    else:
         print(f"{v["name"]}: OK")
print(f"проблемных серверов: {problems}, online серверов: {online}")

    

    

