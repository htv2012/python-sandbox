#!/usr/bin/env python3
import getpass
import pwd
import grp

name = getpass.getuser()
password_entry = pwd.getpwnam(name)
group_entry = grp.getgrgid(password_entry.pw_gid)

print(f"User:       {password_entry.pw_name}")
print(f"Display:    {password_entry.pw_gecos}")
print(f"User ID:    {password_entry.pw_uid}")
print(f"Group ID:   {password_entry.pw_gid}")
print(f"Group name: {group_entry.gr_name}")
print(f"Home:       {password_entry.pw_dir}")
print(f"Shell:      {password_entry.pw_shell}")
