#! /usr/bin/python
import gitlab

def custom_sort(t):
    return t[2]

activity_list = []
mytoken = 'xxxxxxxxxxxxxxxxxxxxxx'

gl = gitlab.Gitlab('https://gitlab.com', private_token=mytoken)

users = gl.users.list(per_page=100)

for i in users:
    if 'block' not in i.state:
        a = str(i.username), str(i.created_at), str(i.last_sign_in_at), str(i.last_activity_on), str(i.state)
        activity_list.append(a)

print("username    created_at    last_sign_in_at    last_activity_on")
print("==============================================================")
activity_list.sort(key=custom_sort)
for j in activity_list:
    print j

