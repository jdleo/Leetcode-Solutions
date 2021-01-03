#!/usr/local/bin/python3
import os, sys

# get problem id from cli arg
problem_id = sys.argv[1]

# commit
os.system("git add -A")
os.system(f'git commit -m "problem #{problem_id} completed"')