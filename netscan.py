import scapy.all as scapy

def scan(ip):
    arp = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast/arp
    arp_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
    res = []
    for e in arp_list:
        info = {"ip": e[1].psrc, "mac": e[1].hwsrc}
        res.append(info)
    return res

def display_res(r):
    print("IP Adress \t\tMAC Adress")
    print("-----------------------------------------")
    for client in r:
        print(client["ip"] + "\t\t" + client["mac"])

u_input = input("Enter any address range : ")
off = scan(u_input)
display_res(off)