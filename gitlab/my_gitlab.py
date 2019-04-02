#! /usr/bin/python
import gitlab

myid = '123456789'
mytoken = 'xxxxxxxxxxxxxxxxxxxxxx'

# personal token at gitlab.com
gl = gitlab.Gitlab('https://gitlab.com', private_token=mytoken)

print gl.users.get(myid)

project = gl.projects.list(owned=True)
for p in project:
    print p.http_url_to_repo
