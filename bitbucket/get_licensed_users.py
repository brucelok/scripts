#!/usr/bin/python
'''
The script get the licensed users' detail from Bitbucket server (datacenter)
author: lok.bruce@gmail.com
'''
import requests, sys, time
import json
requests.packages.urllib3.disable_warnings()

def get_license_users(bb_user, bb_pass):
    '''
    the function requires two arguements admin_username and password
    get the list of licensed users from [license_user_url]
    this URL only returns the username without any details
    '''
    license_user_url = 'https://BITBUCKET-SERVER:PORT/plugins/servlet/users-with/LICENSED_USER'
    print('Retreiving all licensed users from Bitbucket ...')
    try:
        r = requests.get(
            license_user_url, 
            auth=(bb_user, bb_pass),
            timeout=60, 
            verify=False)

        with open("license_users.txt", 'w') as wf:
            wf.write(r.text)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    '''
    the function requires two arguements admin_username and password
    print the detail of licensed users and the last login datetime
    print the total number of licensed users
    '''
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: $ python3 %s $username $password\n" % sys.argv[0])
        sys.exit(1)
    
    bb_api = 'https://BITBUCKET-SERVER:PORT/rest/api/1.0/admin/users?filter='
    bb_user = sys.argv[1]
    bb_pass = sys.argv[2]
    
    get_license_users(bb_user, bb_pass)
    print("USERNAME,EMAIL_ADDRESS,ACTIVE,ACTIVE_DIRECTORY,LAST_AUTHENTICATED")

    with open("license_users.txt", 'r') as rf:
        for line_user in rf:
            line_user = line_user.strip() # remove new line
            api_with_user = bb_api + line_user
            try:
                r = requests.get(
                    api_with_user, 
                    auth=(bb_user, bb_pass),
                    timeout=60, 
                    verify=False)
                # all userful data is at 2nd level of nested dictionary ["values"]
                data = json.loads(r.text)
                name = data['values'][0]['name']
                email = data['values'][0]['emailAddress']
                displayname = data['values'][0]['displayName']
                active = data['values'][0]['active']
                adname = data['values'][0]['directoryName']

                if 'lastAuthenticationTimestamp' not in data['values'][0]:
                    lastauth = 'unknown'
                    pass
                else:
                    lastauth = data['values'][0]['lastAuthenticationTimestamp']
                    fixtimestamp = time.strftime('%Y-%m-%d_%H:%M:%S_%Z', time.localtime(lastauth/1000))
                print(name + ',' + email + ',' + str(active) + ',' + adname + ',' + fixtimestamp)
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
    
    count = len(open("license_users.txt").readlines())
    print("The total numbers of licensed users is %s" %count)
