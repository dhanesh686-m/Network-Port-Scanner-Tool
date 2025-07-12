import socket
def is_host_live(host_name):
"""Checks whether the host is live.
Args:
host_name: The name of the host to check.
Returns:
True if the host is live, False otherwise."""
try:
#Create a socket and connect to the host.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) socket.connect((host_name, 80))
#If the connection was successful, the host is live.
return True
except Exception:
#If the connection failed, the host is not live.
return False
def scan port (host, port):
try:
#Create a socket object
sock socket.socket(socket.AF_INET, socket. SOCK_STREAM)
sock.settimeout(1) # Set a timeout value of 1 second
        # Attempt to connect to the specified host and port
result = sock.connect_ex((host, port))
if result == 0:
print(f"Port (port) is open")
else:
print(f"Port (port) is closed")
sock.close()
except socket.error:
print (f"Couldn't connect to {host}:{port}")
def scan_host(host, start_port, end_port):
print(f"Scanning host {host}...")
for port in range(start_port, end_port + 1):
scan_port(host, port)
# Usage
scan_host('20.112.250.133', 1, 100)