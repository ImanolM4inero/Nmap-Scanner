#!/usr/bin/python3

print('Bienvenido a mi primer programa de escaneo')
print('<------------------------------------------>')

import nmap

ip_ad = input('INGRESE LA IP A ESCANEAR: ')

scanner = nmap.PortScanner()

print('LA IP QUE INGRESO ES LA ', ip_add)
type(ip_add)

respuesta = input('''\n Por favor seleccione el tipo de escaneo
  1) Puertos TCP
  2) Puertos UDP \n''')

print('Su seleccion fue: ', respuesta)

if respuesta=='1':
  print('Nmap version: ', scanner.nmap_version())
  scanner.scann(ip_add, '1-1024', '-O', '-v')
  print(scanner.scaninfo())
  print('Estado IP: ', scanner[ip_add].state())
  print(scanner[ip_add].all_protocols())
  print('Puertos abiertos: ', scanner[ip_add][tcp].keys())

if respuesta=='2':
  print('Nmap version: ', scanner.nmap_version())
  scanner.scan(ip_add, '1-1024', '-sU', '-v')
  print(scanner.scaninfo())
  print('Estado de IP: ', scanner[ip_add].state())
  print(scanner[ip_add].all_protocols())
  print('Puertos abiertos: ', scanner[ip_add]['udp'].keys())
