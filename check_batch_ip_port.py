import sys, socket
'''
a simple tool that read a list of IP addresses/ports from a plaintext file
and verify the remote IP/Port connection.
example file format (comma is required as a delimiter btw IP and Port):
10.0.0.1,8443
10.0.0.2,22
syntax:
$ python check_batch_ip_port.py <text filename>
author: lok.bruce@gmail.com
'''
if len(sys.argv) < 2:
    sys.stderr.write("Usage: $ python %s <text_filename>" % sys.argv[0])
    sys.exit(1)

textfile = sys.argv[1]  #take filename in same directory

with open(textfile, 'r') as f:
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
            print('failed to '+ ip + ':' + port + ' ' + str(msg) +'\n')
            pass

s.close()
f.close()
print('### END OF TEST ###')
