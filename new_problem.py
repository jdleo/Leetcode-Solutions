#!/usr/local/bin/python3
import os, sys

# get problem id from cli arg
problem_id = sys.argv[1]

# create new directory, and new file for solution
os.system(f"mkdir solutions/{problem_id}")
os.system(f"touch solutions/{problem_id}/main.py")

# commit
os.system("git add -A")
os.system(f'git commit -m "create {problem_id}"')