import re
ip_addresses =input("Enter an IP address: ") or '''
123.4.255.2
255.100.244.30
145.90.245.197
111.999.365.901
100.999.1.365'''
regular_expression = r'\b(?:\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\b'
regex = re.findall(regular_expression, ip_addresses)

for x in regex:
    print(x)