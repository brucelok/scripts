#! /bin/bash
# lok.bruce@gmail.com
DATEFORMAT=`date '+%Y-%m-%d %H:%M:%S'`
echo $DATEFORMAT

curl -s -w \
'\nStatus code:\t%{http_code}\n
Lookup time:\t%{time_namelookup}\n
Connect time:\t%{time_connect}\n
SSL handshake:\t%{time_appconnect}\n
Pre transfer:\t%{time_pretransfer}\n
Redirect time:\t%{time_redirect}\n
Start transfer:\t%{time_starttransfer}\n
Total time:\t%{time_total}\n' \
--connect-timeout 3 \
-o /dev/null \
https://www.python.org
