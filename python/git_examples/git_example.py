from git import Repo

repo = Repo('my_repo')

# Check differences between current files and last commit
diff = repo.git.diff(repo.head.commit.tree)
print(diff)