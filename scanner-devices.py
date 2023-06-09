#!/usr/bin/python

import nmap

print('Bienvenido, se van a escanear los equipos conectados a nuestra red')
print('<---------------------------------------------------------------->')

def scan_network():
  nm = nmap.PortScanner()
  
  ip_range = '10.0.2.1/10' ## IP range to scan
  
  nm.scan(hosts=ip_range, arguments= '-sn')
  
  for host in nm.all_hosts():
    if 'mac' in nm[host]['addresses']:
      ip = nm[host]['addresses']['ipv4']
      mac = nm[host]['addresses']['mac']
      print('IP: ', ip)
      print('MAC ', mac)

scan_network()
