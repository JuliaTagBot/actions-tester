import os
from github import Github

g = Github(os.environ["TOKEN"])
r = g.get_repo("christopher-dG/Notify.jl")
print(r.create_issue("test!!!", "body!!!")

