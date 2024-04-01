import psutil
from ip2geotools.databases.noncommercial import DbIpCity

def network_monitor():
    connections = psutil.net_connections(kind='inet')
    for con in connections:
        if con.status == "ESTABLISHED":
            print("----------")
            print(con.laddr)
            print("Process name:", psutil.Process(con.pid).name())
            print("----------")

        



network_monitor()