#! /usr/bin/python
'''
Description: the script will go through all your Gitlab users and returns
             inactive users with more 90 days or None activity
             You must provide admin's private token
Author: lok.bruce@gmail.com
'''
import sys, socket
import datetime
from prettytable import PrettyTable
import gitlab

mygitlab_url = 'https://your-gitlab.com'
private_access_token = 'xxxxxxxxxxxxxxxxxxxxxx'

now = datetime.datetime.now()
excl_users = ['root','ghost']

gl = gitlab.Gitlab(mygitlab_url, private_access_token)
users = gl.users.list(per_page=100)

pt = PrettyTable()
pt.field_names = ["username", "current_sign_in_at", "last_activity_on", "status"]
pt.align["username"] = "l"
pt.align["current_sign_in_at"] = "l"
pt.align["last_activity_on"] = "l"
pt.align["status"] = "l"

for u in users:
    # username in 'excl_user' list will be excluded
    if any(x in u.username for x in excl_users):
        pass
    # user in 'blocked' status will be skipped
    elif u.state == 'blocked':
        pass
    else:
        # if user never login, 'current_sign_in_at' is 'None'
        # check if inactive day is more than 3 moths or 'current_sign_in_at' is None
        if u.current_sign_in_at is None:
            pt.add_row([u.username, u.current_sign_in_at, u.last_activity_on, u.state])
        else:
            # convert the 'current_sign_in_at' into python iso format
            converted = datetime.datetime.strptime(u.current_sign_in_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            inactive_day = int((now - converted).days)
            #print converted.strftime("%Y-%m-%d")
            if inactive_day > 90:
                pt.add_row([u.username, converted.strftime("%Y-%m-%d"), u.last_activity_on, u.state])

pt.sortby = "current_sign_in_at"
print("Report generated on {}\n".format(now))
print("The list of inactive Gitlab users in the past 3 months")
print(pt)

footer = """
* current_sign_in_at:  updated each time the user logs into the web interface
* last_activity_on:  last recorded activity for the user, including git activity
* status:  active - a working user account
           blocked - blocked locally by gitlab admin user
           ldap_blocked - blocked at AD level, probably an user is suspend or no longer existed
           none - never had activity
"""
print(footer)
