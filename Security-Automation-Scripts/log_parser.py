import re
with open('syslog.log') as f:
    for line in f:
        if 'Failed password' in line:
            print(line)