# ^w^
import subprocess
import signal
import sys
import shutil

# ctrl + C 
def handler(sig, frame):
    print("\n\nClose...")
    sys.exit(1)
signal.signal(signal.SIGINT, handler)
print("\nThis is an amazing scanning for nmap scanning and put ur evidence in grep format")
print("\nMake sure exec this script on root mode if err happend")

# Usage
print("\nUsage:")
print("\n-tcp")
print("\n-udp")
print("\n-dns")
print("\n-hdis -> hosts discovery")
print("\n-scr -> this one will send -sCV\n")

# chech nmap
def CheckNmapInPath():
    if shutil.which("nmap") is None:
        print("\n[-] nmap is not in the PATH\n")
        sys.exit(1)
      
def InsertPorts(ip_victim):
    ports = input("Insert ports like '22,80,448':")
    print("\nSending scripts for scanning")
    subprocess.run(["nmap", "-sCV", f"-p{ports}", "ip_victim", "-oN", "scvScan"])
  
def Scan():
    CheckNmapInPath()
    ip_victim = input("Insert ip:")
    option = input("Insert scan:")
    
    #Start Scanning 
    if option == "-tcp":
        subprocess.run(["nmap", "-p-", "--open", "-vvv", "-n", "-Pn", ip_victim, "-oG", "tcpScan"])
    
    elif option == "-udp":
        subprocess.run(["nmap", "--top-ports", "100", "-sU", "-vvv", "-n", "-Pn", ip_victim, "-oG", "udpScan"])
    
    elif option == "-scr":
        InsertPorts(ip_victim)
    
    elif option == "-hdis":
        subprocess.run(["nmap", "-p-", "--open", "--min-rate", "5000", "-vvv", "-n", ip_victim, "-oG", "hostDiscovery"])
    elif option == "-dns":
        subprocess.run(["nmap", "-p-", "--open", "--min-rate", "5000", "-vvv", "-Pn", ip_victim, "-oG", "dsnScan"])
      
if __name__ == "__main__":
    Scan()
