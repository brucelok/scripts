import sys, socket
'''
a simple tool that verify the remote IP/Port connection regardless to the protocol
1st arg is IP
2nd arg is Port
author: lok.bruce@gmail.com
'''

if len(sys.argv) < 3:
    sys.stderr.write("Usage: $ python %s <ip address> <port>" % sys.argv[0])
    sys.exit(1)

ip = sys.argv[1]  #take IP address
port = sys.argv[2]  #take port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

try:
    s.connect((ip, int(port)))
    print('connected to ' + ip + ':' + port)
except socket.error as msg:
    print('failed to '+ ip + ':' + port + ' ' + str(msg))
    sys.exit(1)

s.close()
