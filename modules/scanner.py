import pywifi

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    results = iface.scan_results()
    ssids = set([n.ssid for n in results])
    return list(ssids)
