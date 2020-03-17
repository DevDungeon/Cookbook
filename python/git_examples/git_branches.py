import git

repo = git.Repo.init('my_new_repo')

# List all branches
for branch in repo.branches:
    print(branch)

# Create a new branch
repo.git.branch('my_new_branch')
# You need to check out the branch after creating it if you want to use it
repo.git.checkout('my_new_branch3')

# To checkout master again:
repo.git.checkout('master')
