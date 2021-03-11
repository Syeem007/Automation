import re
import csv

user = {}
error = {}
location = 'syslog'
f=open(location)
for line in f:
    line=line.strip()
    usrname = (re.search(r"\((.*)\)", line)).group(1)
    msg = (re.search(r"(ERROR|INFO)", line)).group(1)
    if usrname not in user:
        sub = {}
        user.update(sub)
    user[usrname][msg] += 1

f.close()
