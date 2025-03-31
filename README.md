# Penetration-Testing-Toolkit

COMPANY: CODTECH IT SOLUTIONS

NAME: MANPREET KAUR

INTERN ID: CT6WUNN

DOMAIN: CYBER SECURITY AND ETHICAL HACKING

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

## **Overview**

The Penetration Testing Toolkit is a modular, Python-based tool designed for educational purposes to demonstrate basic penetration testing techniques. It includes two core modules: a Port Scanner for identifying open TCP ports on a target system and an SSH Brute-Forcer for testing SSH login credentials. Built with extensibility in mind, this toolkit serves as a learning resource for security enthusiasts and developers interested in network security.

## **Features**

- Port Scanner:
  - Multi-threaded TCP port scanning
  - Customizable port range (default: 1-1024)
  - Reports open ports with execution time
    
- SSH Brute-Forcer:
  - Attempts SSH login with provided username/password lists
  - Detailed logging of success/failure attempts
  - Configurable target and port (default: 22)
    
- Modular Design: Easily extendable with additional penetration testing modules
  
- Command-Line Interface: Simple usage via argparse

## **Prerequisites**

- Python 3.7+ installed
- paramiko library

      pip install paramiko
  
- Network access to target systems

  
## **Configure Run Configuration** 
*Configure in PyCharm*
- Click "Run" → "Edit Configurations" in the top menu
- Click the "+" button in the top left to add a new configuration
- Select "Python" from the list
- Configure the following:
  - Name: Give it a name (e.g., "PortScan" or "SSHBrute")
  - Script path: Click the folder icon and select pentest_toolkit.py
  - Parameters: Enter command-line arguments based on what you want to run:
    - For port scanner: portscan --target 127.0.0.1
    - For SSH brute forcer: sshbrute --target 127.0.0.1
  - Working directory: Set to your project folder (should be auto-set)
- Click "Apply" then "OK"
  
## **Running the Toolkit**
- To test port scanner:
  - Set parameters to: "portscan --target 127.0.0.1"
  - Click green "Run" button
- To test SSH brute forcer:
  - Set parameters to: "sshbrute --target 127.0.0.1"
  - Click green "Run" button
    
## **Example Runs**

### Port Scanner
- Configuration parameters: portscan --target 127.0.0.1
- This scans localhost ports 1-1024
- Output might look like:

![Image](https://github.com/user-attachments/assets/9686bd3c-a98a-4b21-a4aa-b49883bf90a8)

### SSH Brute Forcer
- Configuration parameters: sshbrute --target 127.0.0.1
- This tries default username/password combinations on localhost SSH
- Output might look like:
  
![Image](https://github.com/user-attachments/assets/1c886f0d-16b5-43cf-9db1-6008e8264916)

## **Troubleshooting**
1. Module Not Found: If you get "No module named 'paramiko'":
   - Double-check paramiko installation in Python Interpreter settings
   - Ensure you're using the correct interpreter (check the bottom-right corner of PyCharm)
2. Permission Denied: Ensure you have network permissions and are testing allowed targets
3. No Output: Verify your target is valid and parameters are correct
4. Run Button Grayed Out: Select a valid run configuration or file first

## **Validation**
- Compare port scanning results with nmap:
  - Nmap is a widely trusted network scanning tool. You can compare your toolkit's results with Nmap's output.

        nmap -p 1-1024 127.0.0.1
  - Example output - For Port Scanner
    
  ![Image](https://github.com/user-attachments/assets/20134a83-cf9c-437b-9409-1eef6855bbc7)
  
- Test SSH brute-forcing against a controlled server with known credentials

### Disclaimer
This toolkit is for educational purposes only. Use it only on systems you own or have explicit permission to test. Unauthorized use may violate laws or terms of service. The authors are not responsible for misuse or damage caused by this tool.

### **Tips**
- Use different run configurations for each module (one for portscan, one for sshbrute)
- Press Ctrl+Shift+F10 to run the current file quickly
- Use the "Debug" button (bug icon) instead of "Run" to step through code
- Check the "Run" tool window for error messages if something fails
