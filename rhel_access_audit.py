#!/usr/bin/env python2.7
import os
import grp
import operator
import pwd


# Print all users
print '\n\n******************** List of users in the system ********************'
for p in pwd.getpwall():
    print p[0]


name = 'wheel'
info = grp.getgrnam(name)
#print 'Name    :', info.gr_name
#print 'GID     :', info.gr_gid
#print 'Password:', info.gr_passwd
print '\n\n******************** Users with sudo access in the system ********************\n', ', '.join(info.gr_mem)

# Load all of the user data, sorted by username

all_groups = grp.getgrall()
interesting_groups = sorted((g
                            for g in all_groups
                            if not g.gr_name.startswith('_')),
                            key=operator.attrgetter('gr_name'))

# Find the longest length for the name
name_length = max(len(g.gr_name) for g in interesting_groups) + 1


print '\n\n\n******************** Group details with members ********************\n'
# Print report headers
#fmt = '%-*s %4s %10s %s'
fmt = '%-*s %4s %s'
print fmt % (name_length, 'Name',
             'GID',
#             'Password',
             'Members')
#print '-' * name_length, '----', '-' * 10, '-' * 30


print '-' * name_length, '----', '-' * 30

# Print the data
for g in interesting_groups:
    print fmt % (name_length, g.gr_name,
                 g.gr_gid,
#                 g.gr_passwd,
                 ', '.join(g.gr_mem))
print '\n'



# Fetch user login times

print '\n\n******************** Last login times of users ********************\n'

login_time = 'cut -d: -f1 /etc/passwd |while read u ; do last -n 1 "$u" |head -n -2 ; done'

os.system(login_time)  # returns the exit code in unix
#print('returned value:', returned_value)


#os.system('cut -d: -f1 /etc/passwd |while read u ; do last -n 1 "$u" |head -n -2 ; done')
#os.system('awk -F ":" '{print $1}' /etc/passwd | while read j ; do last -n 1 "$j" |head -n -2; done')




# Get user status

print '\n\n\n******************** Get status of user accounts ********************\n'
#os.system('for i in `cat /etc/passwd |cut -d: -f1`; do passwd -S $i; done')

#user_status = 'for i in `cat /etc/passwd |cut -d: -f1`; do passwd -S $i; done'
#user_status = 'for i in `cat /etc/passwd |cut -d: -f1`; do `passwd -S $i | awk -F " " '{print $1,$8,$9}'`; done'
user_status = 'for i in `cat /etc/passwd |cut -d: -f1`; do passwd -S $i | cut  -d " " -f1,8,9,10,11,12; done'

os.system(user_status)  # returns the exit code in unix
#print('returned value:', returned_value)

