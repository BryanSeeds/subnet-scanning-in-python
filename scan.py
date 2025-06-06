# This code inspects the ARP cache to obtain a list of local host IP addresses.
# A DNS lookup is then performed for each IP address to obtain its host name.
# The list of hosts is sent to stdout and also displayed as a simple network graph.
# Note: subnet and broadcast addresses are hard coded and must be changed to suit local requirements.


import os
import networkx as nx
import matplotlib.pyplot as plt

subnet = "subnet \n 192.168.0.0/16"                             #subnet address
broadcast = "192.168.1.255"                                     #subnet broadcast address

os.system(f"ping -b -c 1 {broadcast} > /dev/null")              #ping broadcast address once to wake-up hosts

Graph = nx.Graph()
Graph.add_node(subnet)
host_list = os.popen('ip neigh').read().splitlines()            #run posix ip neigh command and pipe into host list
for host_num, line in enumerate(host_list, start=1):            #iterate through host list
    ip_addr = line.split(" ")[0]                                #first int element is IP addr
    h = os.popen(f'host {ip_addr}').read()                      #run posix dns lookup on IP addr
    hostname = h.split(' ')[-1]                                 #last element is hostname
    print(f"{host_num:>3}: {hostname.strip()} ({ip_addr})")     #print host details to stdout
    node = ip_addr + "\n" + hostname.strip()
    Graph.add_node(node)                                        #add host to network graph
    Graph.add_edge(subnet, node)                                #add edge from 'subnet' node to new host

plt.figure(figsize=(10, 8))
nx.draw(Graph, with_labels=True, node_color="yellow", node_size=800, edge_color="black", font_size=12, font_weight="bold")
plt.suptitle("Discovered Hosts on " + subnet)
plt.show()
        
