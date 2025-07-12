# Network & Port Scanner

This Python script provides basic network scanning functionalities, including checking if a host is live and scanning a range of ports on a specified host.

## Features

* **Host Liveness Check:** Determines if a given host is reachable.
* **Port Scanning:** Scans a range of ports on a host to identify open or closed ports.

## Getting Started

### Prerequisites

* Python 3.x

### Installation

1.  Clone the repository (or download the `NetWork_&_Port_Scanner.py` file):
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

### Usage

The script can be run directly from the command line.

#### Checking Host Liveness

The `is_host_live` function checks if a host is live by attempting to connect to port 80.

```python
import socket

def is_host_live(host_name):
    """Checks whether the host is live.
    Args:
        host_name: The name of the host to check.
    Returns:
        True if the host is live, False otherwise."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host_name, 80))
        return True
    except Exception:
        return False

# Example usage:
if is_host_live('google.com'):
    print("google.com is live")
else:
    print("google.com is not live")
