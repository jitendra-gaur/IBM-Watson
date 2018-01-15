# Delete git commit

git clone URL

### move to the directory
cd Data-Science-Material

### check the git commit history
git log
take the git commit key for restoring(ex : 61511e29f838428fb5a86004d719b70b57152b98)

### rebase the commit
git rebase -i 61511e29f838428fb5a86004d719b70b57152b98

### delete the other commits
Press d to delete the commits not required. When done push page down button and type :wq to save

### git commit will be deleted and will be restored to the above mentioned key.
