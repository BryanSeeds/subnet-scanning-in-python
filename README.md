# subnet-scanning-in-python

This code inspects the ARP cache to obtain a list of local host IP addresses.
A DNS lookup is then performed for each IP address to obtain its host name.
The list of hosts is sent to stdout and also displayed as a simple network graph.

** Note: subnet and broadcast addresses are hard coded and must be changed to suit local requirements.
