#!/usr/bin/python
import requests
import sys
import time

requests.packages.urllib3.disable_warnings()

service_name = "api_check"
api_url = "https://www.google.com"

def auth_api():
    r = requests.get(api_url, timeout=3, verify=False)
    return r.status_code


for i in range(1,4):
    try:
        print("attempt: %d" %i)
        code = auth_api()

        if code == 200:
            print('0 ' + service_name + ' - ' + "status_code: %s, API endpoint %s Success" %(code, api_url))
            break

    except Exception as e:
        print(str(e))
        pass

    if i < 3:
        time.sleep(5)
else:
    print('2 ' + service_name + ' - ' + "all %d attempts failed" %i)
    sys.exit(1)
