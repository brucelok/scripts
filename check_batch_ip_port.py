import socket
'''
a simple tool that read a list of IP addresses/ports from a plaintext file
and verify the remote IP/Port connection.
example file format (comma is required as a delimiter btw IP and Port):
10.0.0.1,8443
10.0.0.2,22
author: lok.bruce@gmail.com
'''

with open('ls_ipport', 'r') as f:
    for line in f:
        awk = line.split(",")
        ip = awk[0]
        port = awk[1]
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((ip, int(port)))
            print('connected to ' + ip + ':' + port)

        except socket.error as msg:
            print('failed to '+ ip + ':' + port + str(msg) +'\n')
            pass

s.close()
f.close()
print('\n### END OF TEST ###')