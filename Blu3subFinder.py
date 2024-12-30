import requests
from colorama import Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor
import pyfiglet


ascii_banner = pyfiglet.figlet_format("BLU33 \nSUBFINDER")
print(Fore.BLUE+ascii_banner)

def check_subdomain(subdomain, domain):
    protocols = ["http://", "https://"]
    for protocol in protocols:
        url = f"{protocol}{subdomain}.{domain}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Domain found: " , url ) 
                break  
        except (requests.ConnectionError, requests.Timeout):
            pass
    
def subscanner(subdomains, domain):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for subdomain in subdomains:
            executor.submit(check_subdomain, subdomain, domain)


wordlist = open("Subdomain.txt") 
subdomains= wordlist.read().splitlines()
domaine = input("Enter the domaine name : ")

subscanner(subdomains,domaine)
