#!/usr/local/bin/python3
import os

# get problem solved count
problem_count = os.popen("ls -l solutions/ | wc -l").read()
problem_count = int(problem_count)

# delete last readme
os.system("rm README.md")

# write new readme
with open("README.md", "w") as f:
    # create readme file contents
    contents = """# Leetcode Solutions
All solutions are done in Python. Problems are organized in `/solutions` folder where each corresponding solution is under its problem ID as a folder.  

All solutions are interview-friendly, meaning there is minimal "python golf" and mostly everything can be replicated in most languages
    
**Amount Solved**: `%s`
""" % problem_count

    # write
    f.write(contents)

# stage changes + commit + push
os.system("git add -A")
os.system('git commit -m "update readme"')
os.system("git push")