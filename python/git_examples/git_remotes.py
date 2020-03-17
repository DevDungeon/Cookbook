import git

repo = git.Repo('test_repo')

# List remotes
print('Remotes:')
for remote in repo.remotes:
    print(f'- {remote} {remote.url}')

# Create a new remote
try:
    remote = repo.create_remote('myremote', url='git@github.com:NanoDano/test_repo')
except git.exc.GitCommandError as error:
    print(f'Error creating remote: {error}')

# Reference a remote by its name as part of the object
print(f'Remote name: {repo.remotes.myremote.name}')
print(f'Remote URL: {repo.remotes.myremote.url}')

# Delete a remote
repo.delete_remote('myremote')

# Pull from remote repo
print(repo.remotes.origin.pull())
# Push changes
print(repo.remotes.origin.push())

